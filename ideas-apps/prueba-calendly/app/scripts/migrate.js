// Uso: DATABASE_URL=... node scripts/migrate.js   (aplica migrations/*.sql en orden, una vez cada una)
const { Pool } = require('pg'), fs = require('fs'), path = require('path');
(async () => {
  const pool = new Pool({ connectionString: process.env.DATABASE_URL });
  await pool.query('create table if not exists schema_migrations (name text primary key, applied_at timestamptz not null default now())');
  const dir = path.join(__dirname, '..', 'migrations');
  for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.sql')).sort()) {
    const done = await pool.query('select 1 from schema_migrations where name=$1', [f]); if (done.rowCount) { console.log('ya aplicada', f); continue; }
    const c = await pool.connect();
    try { await c.query('begin'); await c.query(fs.readFileSync(path.join(dir, f), 'utf8')); await c.query('insert into schema_migrations(name) values($1)', [f]); await c.query('commit'); console.log('aplicada', f); }
    catch (e) { await c.query('rollback'); console.error('FALLO', f, e.message); process.exit(1); } finally { c.release(); }
  }
  await pool.end();
})();
