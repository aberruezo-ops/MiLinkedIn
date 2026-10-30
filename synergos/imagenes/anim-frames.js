// Captura fotogramas PNG con fondo transparente (para superponer sobre un vídeo con ffmpeg).
const { chromium } = require('playwright'); const fs=require('fs');
(async () => {
  const [,, inp, dir] = process.argv; fs.mkdirSync(dir, {recursive:true});
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(async()=>chromium.launch());
  const H = process.argv[4] ? +process.argv[4] : 1080; const p = await b.newPage({ viewport: { width: 1080, height: H } });
  await p.goto('file://' + inp); await p.waitForTimeout(400);
  const total = await p.evaluate(() => window.TOTAL), fps = await p.evaluate(() => window.FPS);
  const frames = Math.round(total*fps);
  for (let i=0;i<frames;i++){ await p.evaluate(t => window.renderFrame(t), i/fps); await p.screenshot({ path: `${dir}/f${String(i).padStart(4,'0')}.png`, omitBackground:true }); }
  await b.close(); console.log('ok', frames, 'fotogramas en', dir);
})();
