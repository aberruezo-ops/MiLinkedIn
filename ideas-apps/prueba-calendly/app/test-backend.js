process.env.RATE_BOOK = '1000';
const assert = require('assert'); const { server, store } = require('./server'); const emails = require('./emails');
(async () => {
  await new Promise(r => server.listen(0, r)); const base = 'http://localhost:' + server.address().port;
  const post = (p, b) => fetch(base + p, { method: 'POST', body: JSON.stringify(b) }).then(async r => ({ s: r.status, b: await r.json() }));
  const sl = await fetch(base + '/api/slots?event=llamada-30&from=' + Date.now() + '&to=' + (Date.now() + 10 * 86400000)).then(r => r.json());
  // 1) reserva encola 2 emails; idempotente
  const bk = await post('/api/book', { event: 'llamada-30', start: sl.slots[5], name: 'Ana', email: 'ana@example.com', tz: 'Europe/Madrid' }); assert.strictEqual(bk.s, 201);
  let ob = await store.emailsAll(); const mine = ob.filter(o => o.booking_id === bk.b.id || !o.booking_id); assert.strictEqual(ob.length >= 2, true);
  const row = await store.getBookingByToken(bk.b.token); await emails.enqueueConfirmation(store, row, 'X', await store.getHost());
  assert.strictEqual((await store.emailsAll()).length, ob.length, 'no duplica emails'); console.log('ok emails encolados sin duplicar');
  // 2) fallo del proveedor -> reintento con espera; luego exito
  emails.failNext(2); let r1 = await emails.processOutbox(store, Date.now()); assert.strictEqual(r1.failed, 2);
  let again = await emails.processOutbox(store, Date.now()); assert.strictEqual(again.ok + again.failed, 0, 'no reintenta antes de la espera');
  let r2 = await emails.processOutbox(store, Date.now() + 120000); assert.strictEqual(r2.ok, 2); assert.strictEqual(emails.sent.length, 2); console.log('ok reintento con espera y envio posterior');
  // 3) tras N fallos pasa a dead letter
  const b2 = await post('/api/book', { event: 'llamada-30', start: sl.slots[9], name: 'Luis', email: 'luis@example.com', tz: 'UTC' }); assert.strictEqual(b2.s, 201);
  emails.failNext(100); let t = Date.now(); for (let i = 0; i < emails.MAX; i++) { await emails.processOutbox(store, t); t += 3600 * 1000 * 2; }
  const dead = (await store.emailsAll()).filter(o => o.status === 'dead'); assert.strictEqual(dead.length, 2); assert(dead[0].last_error); emails.failNext(0); console.log('ok dead letter tras', emails.MAX, 'intentos');
  // 4) cancelar solo con token valido
  assert.strictEqual((await post('/api/bookings/' + 'a'.repeat(24) + '/cancel', {})).s, 404); console.log('ok token falso no cancela');
  // 5) cuerpo enorme y JSON roto
  assert.strictEqual((await fetch(base + '/api/book', { method: 'POST', body: '{' })).status, 400);
  const huge = await fetch(base + '/api/book', { method: 'POST', body: JSON.stringify({ name: 'x'.repeat(50000) }) }).then(r => r.status).catch(() => 'cortado'); assert(huge === 400 || huge === 'cortado'); console.log('ok json roto y cuerpo enorme');
  // 6) path traversal
  const tr = await fetch(base + '/..%2f..%2fetc%2fpasswd'); assert.strictEqual(tr.status, 404); console.log('ok path traversal bloqueado');
  server.close(); await store.close();
})().catch(e => { console.error('FALLO', e.message); process.exit(1); });
