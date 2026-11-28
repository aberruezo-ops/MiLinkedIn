// Calculo de huecos. Todo en UTC; la disponibilidad se define en la zona del anfitrion.
function tzOffsetMs(utcMs, tz) {
  const p = new Intl.DateTimeFormat('en-US', { timeZone: tz, hourCycle: 'h23',
    year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' })
    .formatToParts(new Date(utcMs)).reduce((a, x) => (a[x.type] = x.value, a), {});
  return Date.UTC(p.year, p.month - 1, p.day, p.hour, p.minute, p.second) - utcMs;
}
// Hora local (y,m,d,h,mi) en tz -> instante UTC en ms. Dos pasadas para respetar el cambio de hora.
function localToUtc(y, m, d, h, mi, tz) {
  const guess = Date.UTC(y, m - 1, d, h, mi);
  let t = guess - tzOffsetMs(guess, tz);
  t = guess - tzOffsetMs(t, tz);
  return t;
}
function localDateParts(utcMs, tz) {
  const p = new Intl.DateTimeFormat('en-CA', { timeZone: tz, year: 'numeric', month: '2-digit', day: '2-digit', weekday: 'short' })
    .formatToParts(new Date(utcMs)).reduce((a, x) => (a[x.type] = x.value, a), {});
  const wd = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(p.weekday);
  return { y: +p.year, m: +p.month, d: +p.day, wd };
}
const hm = s => s.split(':').map(Number);

function computeSlots({ host, eventType, rules, bookings, nowMs, fromMs, toMs }) {
  const out = [];
  const dur = eventType.duration_min * 60000;
  const bb = eventType.buffer_before_min * 60000, ba = eventType.buffer_after_min * 60000;
  const earliest = Math.max(fromMs, nowMs + eventType.min_notice_min * 60000);
  const latest = Math.min(toMs, nowMs + eventType.max_days_ahead * 86400000);
  const busy = bookings.filter(b => b.status === 'confirmed' && b.host_id === host.id);
  const perDay = {};
  // recorre dias locales del anfitrion (con margen de un dia a cada lado)
  // Recorre dias locales civiles (no bloques de 24 h UTC) para no saltar ni repetir dias en los cambios de hora.
  const s0 = localDateParts(fromMs - 86400000, host.timezone);
  for (let i = 0; i < 400; i++) {
    const dt = new Date(Date.UTC(s0.y, s0.m - 1, s0.d + i));
    const y = dt.getUTCFullYear(), m = dt.getUTCMonth() + 1, d = dt.getUTCDate(), wd = dt.getUTCDay();
    if (localToUtc(y, m, d, 0, 0, host.timezone) > toMs + 86400000) break;
    const key = `${y}-${m}-${d}`;
    const dayRules = rules.filter(r => r.weekday === wd);
    let count = busy.filter(b => { const q = localDateParts(b.start_at, host.timezone); return `${q.y}-${q.m}-${q.d}` === key; }).length;
    for (const r of dayRules) {
      const [sh, sm] = hm(r.start_local), [eh, em] = hm(r.end_local);
      const start = localToUtc(y, m, d, sh, sm, host.timezone), end = localToUtc(y, m, d, eh, em, host.timezone);
      for (let s = start; s + dur <= end; s += dur) {
        if (s < earliest || s > latest) continue;
        if (eventType.daily_limit && count >= eventType.daily_limit) continue;
        const gap = bb + ba; // separacion minima entre dos reuniones, en los dos sentidos
        const clash = busy.some(b => s < b.end_at + gap && s + dur + gap > b.start_at);
        if (!clash) out.push(s);
      }
    }
  }
  return [...new Set(out)].sort((a, b) => a - b).filter(s => s >= fromMs && s < toMs);
}
module.exports = { computeSlots, localToUtc, tzOffsetMs, localDateParts };
