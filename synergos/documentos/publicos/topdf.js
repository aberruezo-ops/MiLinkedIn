const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage();
for(const [f,land] of [['metodo-una-pagina',true],['mapa-plantilla',false]]){await p.goto('file://'+path.join(__dirname,f+'.html'));await p.waitForTimeout(600);
await p.pdf({path:path.join(__dirname,'Synergos-'+f+'.pdf'),format:'A4',landscape:land,printBackground:true,preferCSSPageSize:true});}
await b.close();console.log('ok')})();
