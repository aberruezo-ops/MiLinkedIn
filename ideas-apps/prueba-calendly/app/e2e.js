const { chromium } = require('playwright'); process.env.RATE_BOOK = '1000'; const { server } = require('./server');
const OUT = require('path').resolve(__dirname, '../clone-screens'); const assert = require('assert');
(async () => {
  await new Promise(r => server.listen(0, r)); const base = 'http://localhost:' + server.address().port;
  const b = await chromium.launch(); const errs = [];
  for (const [w, h, tag] of [[1440, 900, 'desktop'], [390, 844, 'movil']]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, timezoneId: 'America/New_York', locale: 'es-ES' }); const p = await ctx.newPage();
    p.on('console', m => m.type() === 'error' && errs.push(tag + ': ' + m.text())); p.on('pageerror', e => errs.push(tag + ': ' + e.message));
    await p.goto(base + '/admin'); await p.waitForSelector('#rules .rule'); await p.screenshot({ path: `${OUT}/S03-S05-${tag}.png`, fullPage: true });
    assert((await p.evaluate(() => document.documentElement.scrollWidth)) <= w, 'sin scroll horizontal admin ' + tag);
    await p.goto(base + '/book/llamada-30'); await p.waitForSelector('.day.free'); await p.screenshot({ path: `${OUT}/S06-${tag}.png`, fullPage: true });
    await p.click('.day.free'); await p.waitForSelector('.slot'); await p.screenshot({ path: `${OUT}/S07-${tag}.png`, fullPage: true });
    await p.click('.slot'); await p.waitForSelector('#form:not([hidden])');
    await p.click('#go'); assert((await p.textContent('#enm')).length > 0 && (await p.textContent('#eem')).length > 0, 'errores de formulario'); await p.screenshot({ path: `${OUT}/S08-errores-${tag}.png`, fullPage: true });
    await p.fill('#nm', 'María '.repeat(10).trim()); await p.fill('#em', 'maria@example.com'); await p.screenshot({ path: `${OUT}/S08-${tag}.png`, fullPage: true });
    await Promise.all([p.waitForURL(/confirmacion/), p.click('#go')]); await p.waitForSelector('#c');
    assert(/Reserva confirmada/.test(await p.textContent('#out'))); await p.screenshot({ path: `${OUT}/S09-${tag}.png`, fullPage: true });
    assert((await p.evaluate(() => document.documentElement.scrollWidth)) <= w, 'sin scroll horizontal confirmacion ' + tag);
    // hueco ocupado mientras otro invitado rellena: estado 409
    const p2 = await ctx.newPage(); await p2.goto(base + '/book/llamada-30'); await p2.waitForSelector('.day.free'); await p2.click('.day.free'); await p2.waitForSelector('.slot');
    const txt = await p2.textContent('.slot'); await p2.click('.slot'); await p2.fill('#nm', 'Otra'); await p2.fill('#em', 'otra@example.com');
    const r = await fetch(base + '/api/slots?event=llamada-30'); const sl = (await r.json()).slots; const take = sl[0]; // ocupar el primer hueco por API
    await fetch(base + '/api/book', { method: 'POST', body: JSON.stringify({ event: 'llamada-30', start: take, name: 'Rival', email: 'r@x.com', tz: 'UTC' }) });
    await p2.click('#go'); await p2.waitForSelector('.banner'); const bt = await p2.textContent('.banner');
    console.log(tag, 'conflicto:', /acaba de ocuparse/.test(bt) ? 'aviso mostrado' : 'SIN AVISO (hueco elegido ' + txt + ')'); await ctx.close();
  }
  // solo teclado: Tab hasta un dia libre, Enter, Tab a hora, Enter, rellenar, enviar
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } }); const k = await ctx.newPage();
  await k.goto(base + '/book/llamada-30'); await k.waitForSelector('.day.free');
  await k.focus('.day.free'); await k.keyboard.press('Enter'); await k.waitForSelector('.slot'); await k.focus('.slot'); await k.keyboard.press('Enter');
  await k.waitForSelector('#nm'); await k.focus('#nm'); await k.keyboard.type('Teclado'); await k.keyboard.press('Tab'); await k.keyboard.type('t@example.com'); await k.keyboard.press('Enter');
  await k.waitForURL(/confirmacion/); console.log('teclado: reserva completada'); await b.close(); server.close();
  console.log('errores de consola:', errs.length ? errs : 'ninguno');
})().catch(e => { console.error('FALLO', e.message); process.exit(1); });
