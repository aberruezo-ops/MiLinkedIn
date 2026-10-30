// Captura fotogramas de anim-logo.html y los monta en MP4 con ffmpeg.
const { chromium } = require('playwright'); const { execSync } = require('child_process'); const fs=require('fs');
(async () => {
  const [,, inp, out] = process.argv; const dir = out + '.frames'; fs.mkdirSync(dir, {recursive:true});
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(async()=>chromium.launch());
  const p = await b.newPage({ viewport: { width: 1080, height: 1080 } });
  await p.goto('file://' + inp); await p.waitForTimeout(400);
  const total = await p.evaluate(() => window.TOTAL), fps = await p.evaluate(() => window.FPS);
  const frames = Math.round(total*fps);
  for (let i=0;i<frames;i++){ await p.evaluate(t => window.renderFrame(t), i/fps); await p.screenshot({ path: `${dir}/f${String(i).padStart(4,'0')}.png` }); }
  await b.close();
  execSync(`ffmpeg -y -loglevel error -framerate ${fps} -i ${dir}/f%04d.png -c:v libx264 -pix_fmt yuv420p -movflags +faststart -crf 20 "${out}"`);
  fs.rmSync(dir, {recursive:true}); console.log('ok', out, frames, 'fotogramas');
})();
