const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const jobs = [
    ['tablero.html', 'tablero-identidad.png', 2400, 2060, false],
    ['logo.html', 'logo-destiempo.png', 1500, 440, false],
    ['logo_transparente.html', 'logo-destiempo-transparente.png', 1500, 440, true],
    ['portada1.html', 'portada-1-concepto.png', 800, 1200, false],
    ['portada2.html', 'portada-2-concepto.png', 800, 1200, false],
    ['portada3.html', 'portada-3-concepto.png', 800, 1200, false],
  ];
  for (const [src, out, w, h, transparent] of jobs) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + path.resolve(__dirname, src));
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: out, omitBackground: transparent });
    await p.close();
  }
  await b.close();
})();
