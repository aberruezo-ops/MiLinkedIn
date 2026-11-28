// Datos de prueba ficticios (ninguna persona real). Uso: DATABASE_URL=... node scripts/seed.js
const { Pool } = require('pg');
(async () => {
  const pool = new Pool({ connectionString: process.env.DATABASE_URL });
  await pool.query(`insert into users(email,name,slug,timezone) values('anfitrion@example.com','Anfitrión de prueba','demo','Europe/Madrid') on conflict (email) do nothing`);
  const u = (await pool.query(`select id from users where slug='demo'`)).rows[0].id;
  const has = await pool.query('select 1 from availability_rules where user_id=$1', [u]);
  if (!has.rowCount) for (const wd of [1, 2, 3, 4, 5]) await pool.query(`insert into availability_rules(user_id,weekday,start_local,end_local) values($1,$2,'09:00','13:00')`, [u, wd]);
  await pool.query(`insert into event_types(owner_id,slug,name,duration_min,min_notice_min) values($1,'llamada-30','Llamada de 30 minutos',30,60) on conflict (owner_id,slug) do nothing`, [u]);
  console.log('seed ok'); await pool.end();
})();
