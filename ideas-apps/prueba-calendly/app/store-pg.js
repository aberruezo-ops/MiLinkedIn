// Capa de datos Postgres. La anti doble reserva la garantiza la constraint no_double_booking de la base.
const { Pool } = require('pg');
const pool = new Pool({ connectionString: process.env.DATABASE_URL, max: 10 });
const ms = d => (d instanceof Date ? d.getTime() : +d);
const bk = r => ({ ...r, start_at: ms(r.start_at), end_at: ms(r.end_at) });
module.exports = {
  name: 'postgres', pool,
  async getHost() { return (await pool.query(`select id,name,slug,timezone,email from users where slug='demo'`)).rows[0]; },
  async getEventType(slug) { return (await pool.query(`select * from event_types where slug=$1 and active`, [slug])).rows[0] || null; },
  async getAdminEventType() { return (await pool.query(`select * from event_types order by created_at limit 1`)).rows[0]; },
  async updateEventType(f) { return (await pool.query(`update event_types set name=$1,duration_min=$2,buffer_before_min=$3,buffer_after_min=$4,updated_at=now() where id=(select id from event_types order by created_at limit 1) returning *`,
    [f.name, f.duration_min, f.buffer_before_min, f.buffer_after_min])).rows[0]; },
  async getRules() { return (await pool.query(`select weekday, to_char(start_local,'HH24:MI') start_local, to_char(end_local,'HH24:MI') end_local from availability_rules where user_id=(select id from users where slug='demo') order by weekday,start_local`)).rows; },
  async setRules(rules) {
    const c = await pool.connect();
    try { await c.query('begin'); await c.query(`delete from availability_rules where user_id=(select id from users where slug='demo')`);
      for (const r of rules) await c.query(`insert into availability_rules(user_id,weekday,start_local,end_local) values((select id from users where slug='demo'),$1,$2,$3)`, [r.weekday, r.start_local, r.end_local]);
      await c.query('commit'); } catch (e) { await c.query('rollback'); throw e; } finally { c.release(); }
  },
  async bookingsBetween(hostId, from, to) { return (await pool.query(`select * from bookings where host_id=$1 and status='confirmed' and end_at > to_timestamp($2/1000.0) and start_at < to_timestamp($3/1000.0)`, [hostId, from, to])).rows.map(bk); },
  async createBooking(b) {
    try { return bk((await pool.query(`insert into bookings(event_type_id,host_id,start_at,end_at,guest_name,guest_email,guest_timezone,answers) values($1,$2,to_timestamp($3/1000.0),to_timestamp($4/1000.0),$5,$6,$7,$8) returning *`,
      [b.event_type_id, b.host_id, b.start_at, b.end_at, b.guest_name, b.guest_email, b.guest_timezone, b.answers || {}])).rows[0]); }
    catch (e) { if (e.code === '23P01') { const x = new Error('slot_taken'); x.code = 'slot_taken'; throw x; } throw e; }
  },
  async getBookingByToken(t) { const r = (await pool.query(`select b.*, e.name event_name, u.name host_name from bookings b join event_types e on e.id=b.event_type_id join users u on u.id=b.host_id where b.manage_token=$1`, [t])).rows[0]; return r ? bk(r) : null; },
  async cancelBooking(t) { return (await pool.query(`update bookings set status='cancelled', updated_at=now() where manage_token=$1`, [t])).rowCount > 0; },
  async enqueueEmail(m) { await pool.query(`insert into email_outbox(kind,booking_id,to_email,subject,body) values($1,$2,$3,$4,$5) on conflict (booking_id,kind) do nothing`, [m.kind, m.booking_id, m.to_email, m.subject, m.body]); },
  async claimEmails(nowMs, limit) { return (await pool.query(`select * from email_outbox where status='pending' and next_try_at <= to_timestamp($1/1000.0) order by created_at limit $2 for update skip locked`, [nowMs, limit])).rows; },
  async markEmail(id, p) { const keys = Object.keys(p); const sets = keys.map((k, i) => k === 'next_try_at' ? `${k}=to_timestamp($${i + 2}/1000.0)` : `${k}=$${i + 2}`).join(',');
    await pool.query(`update email_outbox set ${sets} where id=$1`, [id, ...keys.map(k => p[k])]); },
  async emailsAll() { return (await pool.query('select * from email_outbox order by created_at')).rows; },
  async close() { await pool.end(); },
};
