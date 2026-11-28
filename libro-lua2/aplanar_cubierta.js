// Rasteriza portada.html a 300 ppp (PNG) para generar una cubierta KDP aplanada.
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const html = path.resolve(__dirname, 'portada.html');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1674, height: 1080 }, deviceScaleFactor: 300 / 96 });
  await p.goto('file://' + html); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  await p.locator('svg').first().screenshot({ path: path.resolve(__dirname, 'cubierta-300ppp.png') });
  await b.close();
})();
