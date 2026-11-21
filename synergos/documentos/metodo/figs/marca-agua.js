// Marca de agua: cuarto de girasol en la esquina inferior derecha, fondo transparente. NODE_PATH=$(npm root -g) node figs/marca-agua.js
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const dir = __dirname, out = path.join(dir, '..');
const S = 900, COL = ['#B5512A', '#2C6D3F', '#C89A2A'], GA = 137.50776405 * Math.PI / 180;
let g = '';
for (let i = 1; i <= 560; i++) {
  const a = i * GA, r = 13.2 * Math.sqrt(i), x = S + r * Math.cos(a), y = S + r * Math.sin(a), s = 3 + r * 0.02, rr = s * 1.7;
  const d = `M${-s},${-s} L${s - rr},${-s} A${rr},${rr} 0 0 1 ${s},${-s + rr} L${s},${s} L${-s + rr},${s} A${rr},${rr} 0 0 1 ${-s},${s - rr} Z`;
  g += `<path d="${d}" fill="${COL[i % 3]}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)}) rotate(${(a * 180 / Math.PI + 45).toFixed(1)})"/>`;
}
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: S, height: S }, deviceScaleFactor: 1 });
  const f = path.join(dir, '_m.html');
  fs.writeFileSync(f, `<!doctype html><html><head><style>*{margin:0}html,body{width:${S}px;height:${S}px;background:transparent;overflow:hidden}svg{opacity:.24}</style></head><body><svg width="${S}" height="${S}" viewBox="0 0 ${S} ${S}">${g}</svg></body></html>`);
  await p.goto('file://' + f); await p.waitForTimeout(400);
  await p.screenshot({ path: path.join(out, 'marca-agua.png'), omitBackground: true }); fs.unlinkSync(f); await b.close(); console.log('ok marca-agua');
})();
