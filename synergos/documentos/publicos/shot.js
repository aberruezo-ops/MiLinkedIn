const { chromium } = require('playwright'); const path=require('path');
(async()=>{const [,,f,w,h,scale]=process.argv;const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:+w,height:+h},deviceScaleFactor:+(scale||1)});await p.goto('file://'+path.join(__dirname,f+'.html'));await p.waitForTimeout(700);
await p.screenshot({path:path.join(__dirname,f+'.png')});
await p.pdf({path:path.join(__dirname,f+'.pdf'),width:w+'px',height:h+'px',printBackground:true,pageRanges:'1'});await b.close();console.log('ok')})();
