// Portada del documento, estilo editorial blanco. NODE_PATH=$(npm root -g) node figs/portadas.js
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const dir = __dirname, out = path.join(dir, '..'), IM = path.join(dir, '../../../imagenes/');
const INK = '#1F1D1A', GREEN = '#2C6D3F', TERRA = '#B5512A', ALB = '#C89A2A', GREY = '#57534D', RULE = '#C9CFCD';
const css = `*{margin:0;padding:0;box-sizing:border-box}html,body{width:1240px;height:1754px;background:#fff;color:${INK};font-family:'Public Sans',sans-serif;overflow:hidden}
.k{font-size:20px;letter-spacing:7px;text-transform:uppercase;color:${GREY}}`;
const cover = `<img src="file://${IM}logo-synergos.svg" style="position:absolute;left:110px;top:100px;height:96px">
<div style="position:absolute;left:110px;right:110px;top:250px;border-top:2px solid ${RULE}"></div>
<div class="k" style="position:absolute;left:110px;top:320px;color:${GREEN};font-weight:600">Documento de trabajo · uso interno</div>
<div style="position:absolute;left:104px;top:400px;font-family:'EB Garamond',serif;font-size:250px;line-height:.95;letter-spacing:-6px;white-space:nowrap">El método</div>
<div style="position:absolute;left:110px;top:770px;font-family:'EB Garamond',serif;font-style:italic;font-size:96px;color:${GREEN}">Crecer a la vez.</div>
<div style="position:absolute;left:110px;top:930px;width:760px;font-size:30px;line-height:1.5;color:${GREY}">Personas, conocimiento y tecnología avanzando en el mismo orden.</div>
<div style="position:absolute;left:110px;right:110px;bottom:330px;display:flex;gap:0">
 ${[['Personas',TERRA],['Conocimiento',GREEN],['Tecnología',ALB]].map(([t,c],i)=>`<div style="flex:1;background:${c};height:150px;padding:22px 26px;margin-right:22px;border-radius:${i==1?'0 10px 0 56px':'10px 0 56px 0'};color:#fff"><span class="k" style="font-size:19px;color:#fff;letter-spacing:5px">${t}</span></div>`).join('')}</div>
<div style="position:absolute;left:110px;bottom:130px;font-size:26px;line-height:1.6"><b style="font-weight:600;font-size:30px">Alejandro Berruezo</b><br><span style="color:${GREY}">Versión 1.8 · noviembre de 2026</span></div>`;
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1240, height: 1754 }, deviceScaleFactor: 1 });
  const f = path.join(dir, '_p.html'); fs.writeFileSync(f, `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${cover}</body></html>`);
  await p.goto('file://' + f); await p.waitForTimeout(700); await p.screenshot({ path: path.join(out, 'portada-doc.png') }); fs.unlinkSync(f); await b.close(); console.log('ok portada'); })();
