// Portada, fondos de portadilla y contraportada del documento, con el girasol de hojas.
// NODE_PATH=$(npm root -g) node figs/portadas-v2.js
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const dir = __dirname, out = path.join(dir, '..'), IM = path.join(dir, '../../../imagenes/');
const INK = '#1F1D1A', W = 1240, H = 1754;
// colores vivos sobre fondo oscuro: tierra, verde, albero
const COL = ['#E0693A', '#58B27A', '#E6B53C'];
const GA = 137.50776405 * Math.PI / 180;

// girasol: hojas con dos esquinas opuestas redondeadas, color por indice mod 3 (los tres elementos pesan igual)
function girasol({ cx, cy, n, c, rot = 0, s0 = 4, sk = 0.02, op = 1, cols = COL }) {
  let g = '';
  for (let i = 1; i <= n; i++) {
    const a = i * GA + rot, r = c * Math.sqrt(i), x = cx + r * Math.cos(a), y = cy + r * Math.sin(a);
    const s = s0 + r * sk, rr = s * 1.7, col = cols[i % 3];
    const d = `M${-s},${-s} L${s - rr},${-s} A${rr},${rr} 0 0 1 ${s},${-s + rr} L${s},${s} L${-s + rr},${s} A${rr},${rr} 0 0 1 ${-s},${s - rr} Z`;
    g += `<path d="${d}" fill="${col}" opacity="${op}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)}) rotate(${(a * 180 / Math.PI + 45).toFixed(1)})"/>`;
  }
  return `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" style="position:absolute;left:0;top:0">${g}</svg>`;
}
const base = `*{margin:0;padding:0;box-sizing:border-box}html,body{width:${W}px;height:${H}px;background:${INK};color:#F4F6F6;font-family:'Public Sans',sans-serif;overflow:hidden;position:relative}`;
const tri = (w = 360, h = 12) => `<div style="display:flex;width:${w}px;height:${h}px"><i style="flex:1;background:${COL[0]}"></i><i style="flex:1;background:${COL[1]}"></i><i style="flex:1;background:${COL[2]}"></i></div>`;

const cover = `<img src="file://${IM}logo-synergos-dark.svg" style="position:absolute;left:110px;top:110px;height:92px;z-index:3">
${girasol({ cx: 1070, cy: 1380, n: 1500, c: 15.8, rot: 0.4, s0: 3.5, sk: 0.017 })}
<div style="position:absolute;left:110px;top:270px;font-size:20px;letter-spacing:7px;text-transform:uppercase;color:#7CC090;font-weight:600;z-index:3">Documento de trabajo · uso interno</div>
<div style="position:absolute;left:100px;top:340px;font-family:'EB Garamond',serif;font-size:270px;line-height:.95;letter-spacing:-7px;white-space:nowrap;z-index:3">El método</div>
<div style="position:absolute;left:110px;top:650px;font-family:'EB Garamond',serif;font-style:italic;font-size:104px;color:#7CC090;z-index:3">Crecer a la vez.</div>
<div style="position:absolute;left:110px;top:800px;width:520px;font-size:30px;line-height:1.5;color:#C9D2CD;z-index:3">Personas, conocimiento y tecnología avanzando en el mismo orden.</div>
<div style="position:absolute;left:110px;bottom:120px;z-index:3;font-size:26px;line-height:1.6"><b style="font-weight:600;font-size:32px">Alejandro Berruezo</b><br><span style="color:#C9D2CD">Versión 2.1 · noviembre de 2026</span></div>`;

// fondos de portadilla: seis composiciones del mismo girasol, con otro encuadre cada una
const POR = [
  { cx: 1000, cy: 1560, n: 1300, c: 17, rot: 0.2 },
  { cx: 1150, cy: 250, n: 1000, c: 12.5, rot: 1.1 },
  { cx: 170, cy: 1520, n: 1200, c: 16, rot: 2.0 },
  { cx: 1040, cy: 1580, n: 1300, c: 17, rot: 2.9 },
  { cx: 1200, cy: 220, n: 1000, c: 12.5, rot: 3.8 },
  { cx: 120, cy: 1540, n: 1200, c: 16, rot: 4.7 },
];
const contra = `${girasol({ cx: 620, cy: 700, n: 900, c: 14, rot: 0.6, s0: 3.5, sk: 0.02 })}
<img src="file://${IM}logo-synergos-dark.svg" style="position:absolute;left:50%;transform:translateX(-50%);top:1380px;height:84px">
<div style="position:absolute;left:0;right:0;top:1500px;text-align:center;font-family:'EB Garamond',serif;font-style:italic;font-size:64px;color:#7CC090">Crecer a la vez.</div>
<div style="position:absolute;left:0;right:0;top:1610px;text-align:center;font-size:22px;letter-spacing:5px;text-transform:uppercase;color:#C9D2CD">Versión 2.1 · noviembre de 2026</div>`;

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  const shot = async (body, file) => {
    const f = path.join(dir, '_p.html'); fs.writeFileSync(f, `<!doctype html><html><head><meta charset="utf-8"><style>${base}</style></head><body>${body}</body></html>`);
    await p.goto('file://' + f); await p.waitForTimeout(600); await p.screenshot({ path: path.join(out, file) }); fs.unlinkSync(f); console.log('ok', file);
  };
  await shot(cover, 'portada-doc.png');
  for (let i = 0; i < 6; i++) await shot(girasol({ ...POR[i], s0: 4, sk: 0.018 }), `portadilla-fondo-${i + 1}.png`);
  await shot(contra, 'contraportada.png');
  await b.close();
})();
