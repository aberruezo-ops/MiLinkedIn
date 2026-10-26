const { chromium } = require('playwright');
(async () => {
  const [,, inp, out, w, h] = process.argv;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(async()=>chromium.launch());
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  await p.goto('file://' + inp); await p.waitForTimeout(400);
  await p.screenshot({ path: out, type: 'png' }); await b.close(); console.log('ok', out);
})();
