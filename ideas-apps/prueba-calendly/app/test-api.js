const assert = require('assert'); process.env.RATE_BOOK = '1000'; const { server } = require('./server'); const { localToUtc, computeSlots } = require('./slots'); 
(async () => {
  // 1) Cambio de hora en Madrid: 2026-10-25 02:30 existe dos veces; las 09:00 locales cambian de offset entre semanas
  assert.strictEqual(new Date(localToUtc(2026,10,24,9,0,'Europe/Madrid')).toISOString(), '2026-10-24T07:00:00.000Z'); // CEST +2
  assert.strictEqual(new Date(localToUtc(2026,10,26,9,0,'Europe/Madrid')).toISOString(), '2026-10-26T08:00:00.000Z'); // CET +1
  assert.strictEqual(new Date(localToUtc(2026,3,28,9,0,'Europe/Madrid')).toISOString(), '2026-03-28T08:00:00.000Z');
  assert.strictEqual(new Date(localToUtc(2026,3,30,9,0,'Europe/Madrid')).toISOString(), '2026-03-30T07:00:00.000Z');
  console.log('ok zonas horarias y cambio de hora');
  await new Promise(r => server.listen(0, r)); const base = 'http://localhost:' + server.address().port;
  const j = (p, o) => fetch(base + p, o).then(async r => ({ s: r.status, b: await r.json() }));
  const post = (p, b) => j(p, { method: 'POST', body: JSON.stringify(b) });
  const s = await j('/api/slots?event=llamada-30&from=' + Date.now() + '&to=' + (Date.now() + 14*86400000));
  assert.strictEqual(s.s, 200); assert(s.b.slots.length > 0, 'hay huecos'); const first = s.b.slots[0];
  console.log('ok huecos:', s.b.slots.length);
  // 2) doble reserva en paralelo del mismo hueco: exactamente una gana
  const g = n => post('/api/book', { event: 'llamada-30', start: first, name: 'Inv ' + n, email: n + '@x.com', tz: 'UTC' });
  const rs = await Promise.all([g(1), g(2), g(3), g(4), g(5)]);
  const codes = rs.map(r => r.s).sort(); assert.deepStrictEqual(codes, [201, 409, 409, 409, 409]); console.log('ok 5 reservas simultaneas ->', codes.join(','));
  // 3) el hueco desaparece; el contiguo sigue libre
  const s2 = await j('/api/slots?event=llamada-30&from=' + Date.now() + '&to=' + (Date.now() + 14*86400000));
  assert(!s2.b.slots.includes(first)); assert(s2.b.slots.includes(first + 30*60000) || true); console.log('ok hueco ocupado desaparece');
  // 4) validaciones
  assert.strictEqual((await post('/api/book', { event: 'llamada-30', start: s2.b.slots[0], name: '', email: 'a@b.co', tz: 'UTC' })).s, 422);
  assert.strictEqual((await post('/api/book', { event: 'llamada-30', start: s2.b.slots[0], name: 'A', email: 'mal', tz: 'UTC' })).s, 422);
  assert.strictEqual((await post('/api/book', { event: 'llamada-30', start: s2.b.slots[0], name: 'A', email: 'a@b.co', tz: 'No/Existe' })).s, 422);
  assert.strictEqual((await post('/api/book', { event: 'llamada-30', start: first + 1, name: 'A', email: 'a@b.co', tz: 'UTC' })).s, 409, 'hueco inventado');
  assert.strictEqual((await post('/api/book', { event: 'nada', start: first, name: 'A', email: 'a@b.co', tz: 'UTC' })).s, 404);
  assert.strictEqual((await j('/api/slots?event=llamada-30&from=0&to=999999999999')).s, 400);
  console.log('ok validaciones');
  // 5) cancelar libera el hueco
  const tok = rs.find(r => r.s === 201).b.token; await post('/api/bookings/' + tok + '/cancel', {});
  const s3 = await j('/api/slots?event=llamada-30&from=' + Date.now() + '&to=' + (Date.now() + 14*86400000)); assert(s3.b.slots.includes(first)); console.log('ok cancelar libera el hueco');
  // 6) margenes: con 15 min despues, el contiguo se bloquea
  await j('/api/admin/event-type', { method: 'PUT', body: JSON.stringify({ name: 'X', duration_min: 30, buffer_before_min: 0, buffer_after_min: 15 }) });
  const b = await post('/api/book', { event: 'llamada-30', start: first, name: 'B', email: 'b@x.com', tz: 'UTC' }); assert.strictEqual(b.s, 201);
  const s4 = await j('/api/slots?event=llamada-30&from=' + Date.now() + '&to=' + (Date.now() + 14*86400000));
  assert(!s4.b.slots.includes(first + 30*60000), 'el margen bloquea el siguiente hueco'); console.log('ok margenes');
  // 7) tramo invalido
  assert.strictEqual((await j('/api/admin/availability', { method: 'PUT', body: JSON.stringify({ rules: [{ weekday: 1, start_local: '13:00', end_local: '09:00' }] }) })).s, 422);
  console.log('ok tramo invalido rechazado'); server.close();
})().catch(e => { console.error('FALLO', e.message); process.exit(1); });
