// Capa de datos en memoria (para pruebas rapidas). Misma interfaz async que store-pg.js.
const crypto = require('crypto');
const db = {
  user: { id: 'u1', name: 'Anfitrión de prueba', slug: 'demo', timezone: 'Europe/Madrid', email: 'anfitrion@example.com' },
  rules: [1, 2, 3, 4, 5].map(wd => ({ weekday: wd, start_local: '09:00', end_local: '13:00' })),
  et: { id: 'e1', slug: 'llamada-30', name: 'Llamada de 30 minutos', duration_min: 30, buffer_before_min: 0, buffer_after_min: 0, daily_limit: null, min_notice_min: 60, max_days_ahead: 60, active: true },
  bookings: [], outbox: [],
};
module.exports = {
  name: 'memory',
  async getHost() { return db.user; },
  async getEventType(slug) { return db.et.slug === slug && db.et.active ? db.et : null; },
  async getAdminEventType() { return db.et; },
  async updateEventType(f) { Object.assign(db.et, f); return db.et; },
  async getRules() { return db.rules; },
  async setRules(rules) { db.rules = rules.map(r => ({ weekday: r.weekday, start_local: r.start_local, end_local: r.end_local })); },
  async bookingsBetween(hostId, from, to) { return db.bookings.filter(b => b.host_id === hostId && b.status === 'confirmed' && b.end_at > from && b.start_at < to); },
  async createBooking(b) {
    if (db.bookings.some(x => x.host_id === b.host_id && x.status === 'confirmed' && b.start_at < x.end_at && b.end_at > x.start_at)) { const e = new Error('slot_taken'); e.code = 'slot_taken'; throw e; }
    const row = { id: crypto.randomUUID(), status: 'confirmed', manage_token: crypto.randomBytes(12).toString('hex'), ...b }; db.bookings.push(row); return row;
  },
  async getBookingByToken(t) { const b = db.bookings.find(x => x.manage_token === t); return b ? { ...b, event_name: db.et.name, host_name: db.user.name } : null; },
  async cancelBooking(t) { const b = db.bookings.find(x => x.manage_token === t); if (b) b.status = 'cancelled'; return !!b; },
  async enqueueEmail(m) { if (db.outbox.some(o => o.booking_id === m.booking_id && o.kind === m.kind)) return; db.outbox.push({ id: crypto.randomUUID(), status: 'pending', attempts: 0, next_try_at: 0, ...m }); },
  async claimEmails(nowMs, limit) { return db.outbox.filter(o => o.status === 'pending' && o.next_try_at <= nowMs).slice(0, limit); },
  async markEmail(id, patch) { Object.assign(db.outbox.find(o => o.id === id), patch); },
  async emailsAll() { return db.outbox; },
  async close() {},
};
