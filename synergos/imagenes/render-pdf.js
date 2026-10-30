// Genera un PDF por página HTML (1200x1500) y los une: carrusel de LinkedIn.
const { chromium } = require('playwright'); const { execSync } = require('child_process');
(async () => {
  const [,, out, ...pages] = process.argv;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(async()=>chromium.launch());
  const p = await b.newPage({ viewport: { width: 1200, height: 1500 } });
  const parts = [];
  for (const [i, f] of pages.entries()) {
    await p.goto('file://' + f); await p.waitForTimeout(400);
    const part = `${out}.part${i}.pdf`;
    await p.pdf({ path: part, width: '1200px', height: '1500px', printBackground: true, margin: {top:0,right:0,bottom:0,left:0}, pageRanges: '1' });
    parts.push(part);
  }
  await b.close();
  execSync(`pdfunite ${parts.map(x=>`"${x}"`).join(' ')} "${out}"`);
  parts.forEach(x => require('fs').unlinkSync(x)); console.log('ok', out);
})();
