// Portada y portadillas del documento (dirección C: cartel). NODE_PATH=$(npm root -g) node figs/portadas.js
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const dir = __dirname, out = path.join(dir, '..'), IM = path.join(dir, '../../../imagenes/');
const T = path.join(__dirname, '../../../../../tmp'); // no se usa
const INK = '#1F1D1A', GREEN = '#2C6D3F', TERRA = '#B5512A', ALB = '#C89A2A';
const FD = '/tmp/claude-0/-home-user-MiLinkedIn/8b3653e3-6315-50f3-96b3-ad0bde922485/scratchpad/ttf/';
const dots = (n, cx, cy, R, col, op) => { let s = ''; const GA = 137.50776405 * Math.PI / 180, c = R / Math.sqrt(n); for (let i = 1; i <= n; i++) { const r = c * Math.sqrt(i), t = i * GA; s += `<circle cx="${(cx + r * Math.cos(t)).toFixed(1)}" cy="${(cy + r * Math.sin(t)).toFixed(1)}" r="${(c * (0.34 + 0.12 * Math.sqrt(i / n))).toFixed(1)}" fill="${col}" opacity="${op}"/>`; } return s; };
const css = `@font-face{font-family:BS;font-weight:900;src:url('file://${FD}big-shoulders-display-900-normal.ttf')}
@font-face{font-family:BS;font-weight:800;src:url('file://${FD}big-shoulders-display-800-normal.ttf')}
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1240px;height:1754px;background:${INK};color:#F3F1EC;font-family:'Public Sans',sans-serif;overflow:hidden}
.band{position:absolute;left:0;right:0;height:330px;background:${GREEN};overflow:hidden}
.blocks{position:absolute;left:0;right:0;bottom:0;display:flex;height:300px}.blocks div{flex:1;padding:34px 34px}.blocks b{font-family:BS;font-weight:900;font-size:62px;text-transform:uppercase;line-height:.95;display:block}.blocks span{font-size:22px;line-height:1.35;display:block;margin-top:12px;font-weight:600}
.k{font-family:'Public Sans';font-size:22px;letter-spacing:5px;color:#A9B0A9;text-transform:uppercase}`;
const blocks = `<div class="blocks"><div style="background:${TERRA}"><b>Personas</b><span>Quién responde y quién enseña</span></div><div style="background:${GREEN}"><b>Conocimiento</b><span>Lo que nadie ha escrito</span></div><div style="background:${ALB};color:${INK}"><b>Tecnología</b><span>Acelera, automatiza o aumenta</span></div></div>`;
const logo = f => `<img src="file://${IM}${f}" style="position:absolute;left:96px;top:96px;height:150px">`;
const girasol = `<svg width="760" height="760" style="position:absolute;right:-250px;top:-300px">${dots(520, 380, 380, 360, '#fff', .16)}</svg>`;
const cover = `<div class="band">${girasol}</div>${logo('logo-synergos-dark.svg')}
 <div style="position:absolute;left:96px;top:420px"><div class="k">Documento de trabajo · uso interno</div>
 <div style="font-family:BS;font-weight:900;font-size:300px;line-height:.82;text-transform:uppercase;margin-top:30px">El<br>método</div>
 <div style="font-family:BS;font-weight:900;font-size:120px;line-height:.9;text-transform:uppercase;color:${ALB};margin-top:34px">Crecer a la vez.</div>
 <p style="font-size:30px;line-height:1.45;margin-top:40px;max-width:820px;color:#D8D6CF">Personas, conocimiento y tecnología avanzando en el mismo orden.</p></div>
 <div style="position:absolute;left:96px;bottom:360px;font-size:24px;line-height:1.6;color:#D8D6CF"><b style="font-family:'Public Sans';font-weight:700;color:#fff;font-size:28px">Alejandro Berruezo</b><br>Versión 1.8 · noviembre de 2026</div>${blocks}`;
const partes = { 'I': 'Por qué un método', 'II': 'La arquitectura', 'III': 'El tronco', 'IV': 'Los tres elementos y el orden', 'V': 'El detalle', 'VI': 'Un método que se corrige a sí mismo' };
const portadilla = n => `<div class="band" style="height:560px">${girasol}</div><img src="file://${IM}logo-synergos-dark.svg" style="position:absolute;left:96px;top:96px;height:90px">
 <div style="position:absolute;left:96px;top:215px;font-family:BS;font-weight:900;font-size:330px;line-height:.8;color:${INK};opacity:.9">${n}</div>${blocks}`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1240, height: 1754 }, deviceScaleFactor: 1 });
  const shot = async (body, name) => { const f = path.join(dir, '_p.html'); fs.writeFileSync(f, `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${body}</body></html>`); await p.goto('file://' + f); await p.waitForTimeout(700); await p.screenshot({ path: path.join(out, name) }); fs.unlinkSync(f); console.log('ok', name); };
  await shot(cover, 'portada-doc.png');
  for (const n of Object.keys(partes)) await shot(portadilla(n), `portadilla-${n}.png`);
  await b.close();
})();
