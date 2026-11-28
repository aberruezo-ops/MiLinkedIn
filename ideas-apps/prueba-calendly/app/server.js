const http = require('http'), fs = require('fs'), path = require('path');
const store = require('./store');
const { computeSlots } = require('./slots');
const emails = require('./emails');
const PUB = path.join(__dirname, 'public');
const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript' };
const json = (res, code, obj) => { res.writeHead(code, { 'content-type': 'application/json' }); res.end(JSON.stringify(obj)); };
const body = req => new Promise(r => { let s = ''; let big = false; req.on('data', c => { s += c; if (s.length > 20000) { big = true; req.destroy(); } }); req.on('end', () => { if (big) return r(null); try { r(JSON.parse(s || '{}')); } catch { r(null); } }); });
const emailOk = e => typeof e === 'string' && e.length <= 254 && /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(e);
const tzOk = tz => { try { new Intl.DateTimeFormat('en', { timeZone: tz }); return true; } catch { return false; } };
const now = () => (global.__NOW || Date.now());

// Limite de peticiones por IP (en memoria, una sola instancia). Detras de un proxy hay que leer la IP real del proxy de confianza.
const hits = new Map();
function limited(req, key, max, windowMs) {
  const k = key + '|' + req.socket.remoteAddress, t = Date.now(), arr = (hits.get(k) || []).filter(x => t - x < windowMs);
  arr.push(t); hits.set(k, arr);
  if (hits.size > 5000) for (const [kk, v] of hits) if (!v.some(x => t - x < windowMs)) hits.delete(kk);
  return arr.length > max;
}

async function slotsFor(slug, fromMs, toMs) {
  const et = await store.getEventType(slug); if (!et) return null;
  const host = await store.getHost(), rules = await store.getRules();
  const pad = 2 * 86400000, bookings = await store.bookingsBetween(host.id, fromMs - pad, toMs + pad);
  return { et, host, slots: computeSlots({ host, eventType: et, rules, bookings, nowMs: now(), fromMs, toMs }) };
}

const server = http.createServer(async (req, res) => {
  const u = new URL(req.url, 'http://x'); const p = u.pathname;
  try {
    if (req.method === 'GET' && p === '/api/slots') {
      const fp = u.searchParams.get('from'), tp = u.searchParams.get('to');
      const from = fp === null ? now() : Number(fp), to = tp === null ? from + 14 * 86400000 : Number(tp);
      if (!Number.isFinite(from) || !Number.isFinite(to) || to <= from || to - from > 62 * 86400000) return json(res, 400, { error: 'rango_invalido' });
      const r = await slotsFor(u.searchParams.get('event'), from, to);
      if (!r) return json(res, 404, { error: 'evento_no_encontrado' });
      return json(res, 200, { event: { name: r.et.name, duration_min: r.et.duration_min }, host: { name: r.host.name, timezone: r.host.timezone }, slots: r.slots });
    }
    if (req.method === 'POST' && p === '/api/book') {
      if (limited(req, 'book', +process.env.RATE_BOOK || 10, 60000)) return json(res, 429, { error: 'demasiadas_peticiones' });
      const b = await body(req); if (!b) return json(res, 400, { error: 'json_invalido' });
      const name = String(b.name || '').replace(/[\u0000-\u001f\u007f\u2028\u2029]/g, ' ').replace(/\s+/g, ' ').trim();
      if (!name || name.length > 120) return json(res, 422, { error: 'nombre_invalido' });
      if (!emailOk(b.email)) return json(res, 422, { error: 'email_invalido' });
      if (!tzOk(b.tz)) return json(res, 422, { error: 'zona_invalida' });
      const start = Number(b.start); if (!Number.isFinite(start)) return json(res, 422, { error: 'hora_invalida' });
      const r = await slotsFor(b.event, start, start + 1);
      if (!r) return json(res, 404, { error: 'evento_no_encontrado' });
      if (!r.slots.includes(start)) return json(res, 409, { error: 'slot_taken' });
      try {
        const row = await store.createBooking({ event_type_id: r.et.id, host_id: r.host.id, start_at: start, end_at: start + r.et.duration_min * 60000,
          guest_name: name, guest_email: b.email.trim(), guest_timezone: b.tz, answers: {} });
        await emails.enqueueConfirmation(store, row, r.et.name, r.host);
        return json(res, 201, { id: row.id, token: row.manage_token, start_at: row.start_at, end_at: row.end_at, event: r.et.name });
      } catch (e) { if (e.code === 'slot_taken') return json(res, 409, { error: 'slot_taken' }); throw e; }
    }
    let m;
    if (req.method === 'GET' && (m = p.match(/^\/api\/bookings\/(\w+)$/))) {
      const b = await store.getBookingByToken(m[1]); if (!b) return json(res, 404, { error: 'no_encontrada' });
      return json(res, 200, { start_at: b.start_at, end_at: b.end_at, status: b.status, guest_name: b.guest_name, event: b.event_name, host: b.host_name });
    }
    if (req.method === 'POST' && (m = p.match(/^\/api\/bookings\/(\w+)\/cancel$/))) {
      if (!(await store.cancelBooking(m[1]))) return json(res, 404, { error: 'no_encontrada' });
      return json(res, 200, { status: 'cancelled' });
    }
    if (p === '/api/admin/availability') {
      if (req.method === 'GET') return json(res, 200, { timezone: (await store.getHost()).timezone, rules: await store.getRules() });
      if (req.method === 'PUT') {
        const b = await body(req); if (!b || !Array.isArray(b.rules) || b.rules.length > 100) return json(res, 400, { error: 'json_invalido' });
        for (const r of b.rules) if (!Number.isInteger(r.weekday) || r.weekday < 0 || r.weekday > 6 || !/^\d\d:\d\d$/.test(r.start_local) || !/^\d\d:\d\d$/.test(r.end_local) || r.end_local <= r.start_local) return json(res, 422, { error: 'tramo_invalido' });
        await store.setRules(b.rules); return json(res, 200, { ok: true });
      }
    }
    if (p === '/api/admin/event-type') {
      if (req.method === 'GET') return json(res, 200, await store.getAdminEventType());
      if (req.method === 'PUT') {
        const b = await body(req); if (!b) return json(res, 400, { error: 'json_invalido' });
        const dur = Number(b.duration_min); if (!(dur >= 5 && dur <= 720)) return json(res, 422, { error: 'duracion_invalida' });
        if (!String(b.name || '').trim()) return json(res, 422, { error: 'nombre_invalido' });
        const bb = Math.max(0, Math.round(+b.buffer_before_min || 0)), ba = Math.max(0, Math.round(+b.buffer_after_min || 0));
        if (!(bb <= 1440 && ba <= 1440)) return json(res, 422, { error: 'margen_invalido' });
        const evName = String(b.name).replace(/[\u0000-\u001f\u007f\u2028\u2029]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 120);
        if (!evName) return json(res, 422, { error: 'nombre_invalido' });
        return json(res, 200, await store.updateEventType({ name: evName, duration_min: Math.round(dur), buffer_before_min: bb, buffer_after_min: ba }));
      }
    }
    let file = p === '/' || p === '/admin' ? 'admin.html' : p.startsWith('/book/') ? 'book.html' : p.startsWith('/confirmacion') ? 'confirm.html' : p.slice(1);
    const full = path.join(PUB, path.normalize(file).replace(/^(\.\.[\/\\])+/, ''));
    if (!full.startsWith(PUB) || !fs.existsSync(full) || fs.statSync(full).isDirectory()) { res.writeHead(404); return res.end('No encontrado'); }
    res.writeHead(200, { 'content-type': TYPES[path.extname(full)] || 'application/octet-stream' }); fs.createReadStream(full).pipe(res);
  } catch (e) { console.error(e.message); json(res, 500, { error: 'error_interno' }); }
});
if (require.main === module) {
  const port = process.env.PORT || 3000; server.listen(port, () => console.log(`http://localhost:${port} (datos: ${store.name})`));
  setInterval(() => emails.processOutbox(store).catch(e => console.error('outbox', e.message)), 15000).unref();
}
module.exports = { server, store };
