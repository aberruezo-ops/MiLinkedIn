// Cola de emails con reintentos y "dead letter". El proveedor real (Resend) se enchufa con RESEND_API_KEY;
// sin clave se usa un proveedor simulado que solo guarda en memoria. Nada sale a Internet.
const sent = []; let failNext = 0;
const providers = {
  simulated: async m => { if (failNext > 0) { failNext--; throw new Error('fallo simulado del proveedor'); } sent.push({ to: m.to_email, subject: m.subject, body: m.body }); },
  resend: async () => { throw new Error('Proveedor Resend no conectado: falta implementar con la clave del usuario'); },
};
const provider = process.env.RESEND_API_KEY ? providers.resend : providers.simulated;
const MAX = 5, backoff = n => Math.min(60 * 60 * 1000, 30 * 1000 * 2 ** n); // 30 s, 1 min, 2 min...
const fmt = (ms, tz) => new Intl.DateTimeFormat('es', { dateStyle: 'full', timeStyle: 'short', timeZone: tz }).format(ms);
async function enqueueConfirmation(store, booking, eventName, host) {
  const when = fmt(booking.start_at, booking.guest_timezone);
  await store.enqueueEmail({ kind: 'booking_confirmation_guest', booking_id: booking.id, to_email: booking.guest_email,
    subject: `Reserva confirmada: ${eventName}`, body: `Hola ${booking.guest_name}, tu reserva con ${host.name} es el ${when} (${booking.guest_timezone}).\nPara cancelar: /confirmacion?t=${booking.manage_token}` });
  await store.enqueueEmail({ kind: 'booking_confirmation_host', booking_id: booking.id, to_email: host.email,
    subject: `Nueva reserva: ${booking.guest_name}`, body: `${booking.guest_name} (${booking.guest_email}) reservó ${eventName} el ${fmt(booking.start_at, host.timezone)} (${host.timezone}).` });
}
async function processOutbox(store, nowMs = Date.now()) {
  const jobs = await store.claimEmails(nowMs, 20); let ok = 0, failed = 0;
  for (const j of jobs) {
    try { await provider(j); await store.markEmail(j.id, { status: 'sent', sent_at: new Date(nowMs).toISOString(), attempts: j.attempts + 1 }); ok++; }
    catch (e) { const attempts = j.attempts + 1; failed++;
      await store.markEmail(j.id, attempts >= MAX ? { status: 'dead', attempts, last_error: e.message } : { attempts, last_error: e.message, next_try_at: nowMs + backoff(attempts) }); }
  }
  return { ok, failed };
}
module.exports = { enqueueConfirmation, processOutbox, sent, failNext: n => { failNext = n; }, MAX };
