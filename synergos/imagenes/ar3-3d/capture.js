// Captura de fotogramas con Playwright + Chromium (WebGL por software) y montaje con ffmpeg.
// Uso: NODE_PATH=$(npm root -g) node capture.js <salida.mp4> [desde] [hasta] [carpetaFrames]
const { chromium } = require('playwright'); const { execSync } = require('child_process'); const fs=require('fs'); const path=require('path');
(async () => {
  const out=process.argv[2]; const dir=process.argv[5]||out+'.frames'; fs.mkdirSync(dir,{recursive:true});
  const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium', args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist','--enable-webgl'] });
  const p = await b.newPage({ viewport:{width:720,height:1280}, deviceScaleFactor:1 });
  p.on('console',m=>{if(m.type()==='error')console.log('console:',m.text())}); p.on('pageerror',e=>console.log('pageerror',e.message));
  await p.goto('file://'+path.join(__dirname,'index.html')); await p.waitForFunction(()=>window.READY,null,{timeout:60000});
  await p.waitForTimeout(800);
  const total=await p.evaluate(()=>window.TOTAL), fps=await p.evaluate(()=>window.FPS);
  const frames=Math.round(total*fps); const from=+(process.argv[3]||0), to=+(process.argv[4]||frames);
  const t0=Date.now();
  for(let i=from;i<to;i++){ await p.evaluate(t=>window.renderFrame(t),i/fps); await p.screenshot({path:`${dir}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});
    if(i%25===0) console.log('frame',i,'/',frames,((Date.now()-t0)/1000).toFixed(0)+'s'); }
  await b.close();
  if(from===0&&to===frames){ execSync(`ffmpeg -y -loglevel error -framerate ${fps} -i ${dir}/f%04d.jpg -c:v libx264 -pix_fmt yuv420p -crf 28 -movflags +faststart "${out}"`); console.log('ok',out); }
})();
