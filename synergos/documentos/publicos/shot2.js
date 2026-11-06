const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1240,height:1754}});await p.goto('file://'+path.join(__dirname,'infografia-mapa.html'));await p.waitForTimeout(700);
await p.screenshot({path:path.join(__dirname,'infografia-mapa.png'),clip:{x:0,y:0,width:1240,height:1754}});
await p.screenshot({path:path.join(__dirname,'infografia-mapa-2.png'),clip:{x:0,y:1754,width:1240,height:1754},fullPage:true});
await p.pdf({path:path.join(__dirname,'infografia-mapa.pdf'),width:'1240px',height:'1754px',printBackground:true,preferCSSPageSize:true});await b.close();console.log('ok')})();
