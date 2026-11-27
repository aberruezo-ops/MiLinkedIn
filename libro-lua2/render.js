const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const jobs = [['interior.html', 'interior-KDP.pdf', {width:'8.5in', height:'11in'}], ['portada.html', 'cubierta-KDP.pdf', null]];
  for (const [src, out, size] of jobs) {
    const p = await b.newPage();
    await p.goto('file://' + path.resolve(__dirname, src));
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
    await p.close();
  }
  await b.close();
})();
