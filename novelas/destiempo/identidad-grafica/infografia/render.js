const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1600,height:1000},deviceScaleFactor:1.5});
await p.goto('file://'+__dirname+'/personajes.html');await p.waitForTimeout(700);
await p.screenshot({path:__dirname+'/personajes-destiempo.png',fullPage:true});await b.close();})();
