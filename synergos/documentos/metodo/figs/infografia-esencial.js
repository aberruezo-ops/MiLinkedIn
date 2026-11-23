// Infografía esencial del método en tres páginas (A4). NODE_PATH=$(npm root -g) node figs/infografia-esencial.js
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const dir = __dirname, out = path.join(dir, '..'), IM = path.join(dir, '../../../imagenes/');
const FONTDIR = '/tmp/claude-0/-home-user-MiLinkedIn/8b3653e3-6315-50f3-96b3-ad0bde922485/scratchpad/ttf/';
const W = 1240, H = 1754, GA = 137.50776405 * Math.PI / 180;
const INK = '#1F1D1A', PAPER = '#F6F5F1', T = '#B5512A', G = '#2C6D3F', A = '#C89A2A', AT = '#8A6508';
const TV = '#E0693A', GV = '#58B27A', AV = '#E6B53C', MUT = '#C9D2CD', GREY = '#5B5F5C';

function girasol({ cx, cy, n, c, rot = 0, s0 = 4, sk = 0.018, cols = [TV, GV, AV], op = 1, w = W, h = H, from = 1 }) {
  let g = '';
  for (let i = from; i <= n; i++) {
    const a = i * GA + rot, r = c * Math.sqrt(i), x = cx + r * Math.cos(a), y = cy + r * Math.sin(a), s = s0 + r * sk, rr = s * 1.7;
    const d = `M${-s},${-s} L${s - rr},${-s} A${rr},${rr} 0 0 1 ${s},${-s + rr} L${s},${s} L${-s + rr},${s} A${rr},${rr} 0 0 1 ${-s},${s - rr} Z`;
    g += `<path d="${d}" fill="${cols[i % 3]}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)}) rotate(${(a * 180 / Math.PI + 45).toFixed(1)})"/>`;
  }
  return `<svg class="sun" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" style="opacity:${op}">${g}</svg>`;
}
// Un solo tamaño y una sola posición para el girasol en todas las páginas
const SUN = (rot, cols, op) => girasol({ cx: 1262, cy: 392, n: 480, c: 13, rot, s0: 3.2, sk: .02, ...(cols ? { cols } : {}), ...(op ? { op } : {}) });
const EJ = `<span style="display:inline-block;background:${AV};color:${INK};padding:3px 10px;font-size:11px;letter-spacing:3px;text-transform:uppercase;font-weight:700;border-radius:0 8px 0 3px">Ejemplo</span>`;
const face = (fam, file, wt = 400, st = 'normal') => `@font-face{font-family:'${fam}';src:url('file://${FONTDIR}${file}');font-weight:${wt};font-style:${st}}`;
const css = `
${face('Garamond', 'eb-garamond-400-normal.ttf')}${face('Garamond', 'eb-garamond-500-normal.ttf', 500)}${face('Garamond', 'eb-garamond-400-italic.ttf', 400, 'italic')}
${face('Sans', 'public-sans-400-normal.ttf')}${face('Sans', 'public-sans-600-normal.ttf', 600)}${face('Sans', 'public-sans-700-normal.ttf', 700)}
*{margin:0;padding:0;box-sizing:border-box}
@page{size:${W}px ${H}px;margin:0}
html,body{width:${W}px;background:${INK};font-family:'Sans',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{position:relative;width:${W}px;height:${H}px;overflow:hidden;padding:70px 80px 64px;page-break-after:always;break-after:page}
.dark{background:${INK};color:#F4F6F6}.green{background:#1F4A2C;color:#F4F6F6}.green .top span{color:#A9D9B8}.green .foot{color:#CFE3D5}.green .foot i{color:#A9D9B8}.light{background:${PAPER};color:${INK}}
.earth{background:#5C2613;color:#FBF3EC}.earth .top span{color:#F0C3A4}.earth .foot{color:#EBD3C4}.earth .foot i{color:#F0C3A4}
.sun{position:absolute;left:0;top:0;pointer-events:none}
.z{position:relative;z-index:2}
.top{display:flex;justify-content:space-between;align-items:center;font-size:15px;letter-spacing:5px;text-transform:uppercase;font-weight:600}
.top img{height:50px}
.dark .top span{color:${GV}}.light .top span{color:${G}}
.pg{font-family:'Garamond',serif;font-size:30px;letter-spacing:0;text-transform:none;font-weight:400}
.k{font-size:15px;letter-spacing:5px;text-transform:uppercase;font-weight:700}
h1{font-family:'Garamond',serif;font-weight:400;line-height:.92;letter-spacing:-4px}
h2{font-family:'Garamond',serif;font-weight:400;font-size:46px;line-height:1.05;letter-spacing:-.5px}
.ser{font-family:'Garamond',serif}
.leaf{border-radius:14px 0 64px 0}.leafb{border-radius:0 14px 0 64px}
.foot{position:absolute;left:80px;right:80px;bottom:36px;display:flex;justify-content:space-between;align-items:baseline;font-size:14px;letter-spacing:3px;text-transform:uppercase;z-index:3}
.foot i{font-family:'Garamond',serif;font-style:italic;font-size:26px;letter-spacing:0;text-transform:none}
.dark .foot{color:${MUT}}.dark .foot i{color:${GV}}.light .foot{color:${GREY}}.light .foot i{color:${G}}
.tri{display:flex;height:8px;width:260px}.tri b{flex:1}
`;
const tri = (a = TV, b = GV, c = AV) => `<div class="tri"><b style="background:${a}"></b><b style="background:${b}"></b><b style="background:${c}"></b></div>`;
const top = (n, dark) => `<div class="top z"><img src="file://${IM}${dark ? 'logo-synergos-dark.svg' : 'logo-synergos.svg'}"><span>Lo esencial del método</span><span class="pg" style="color:inherit">${n} <span style="opacity:.45">/ 3</span></span></div>`;
const foot = t => `<div class="foot"><i>Crecer a la vez.</i><span>${t}</span></div>`;

// 1 · La idea
const PAL = [['Personas', TV, INK, 'Quien hace el trabajo y cómo lo hace.'], ['Conocimiento', GV, INK, 'Lo que la casa sabe, esté escrito o no.'], ['Tecnología', AV, INK, 'Las herramientas, incluida la IA.']];
const p1 = `<section class="page dark">${SUN(0)}
${top(1, true)}
<div class="z" style="margin-top:120px">
  <div class="k" style="color:${GV}">La idea</div>
  <h1 style="font-size:150px;margin-top:18px">Un objetivo.<br>Tres palancas.<br><span style="font-style:italic;color:${AV}">Un camino.</span></h1>
  <div style="font-size:30px;line-height:1.35;color:${MUT};margin-top:34px;width:820px">Synergós es una forma ordenada de cambiar cómo se trabaja para que el negocio mejore, y para que la mejora dure.</div>
</div>
<div class="z" style="position:absolute;left:80px;right:80px;top:960px">
  <div class="leaf" style="background:#F4F6F6;color:${INK};padding:30px 40px 34px;text-align:center"><div class="k" style="color:${T}">El objetivo</div><div class="ser" style="font-size:76px;line-height:1;margin-top:8px">Que el negocio mejore</div></div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px;margin-top:0">
    ${PAL.map(() => `<svg width="100%" height="74" viewBox="0 0 340 74"><path d="M170 74 V20" stroke="#F4F6F6" stroke-width="4"/><path d="M152 30 L170 6 L188 30 Z" fill="#F4F6F6"/></svg>`).join('')}
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px">
    ${PAL.map(([n, c, fg, t], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${c};color:${fg};padding:30px 28px 38px;height:270px"><div class="k" style="font-size:13px;opacity:.75">Palanca ${i + 1}</div><div class="ser" style="font-size:54px;line-height:1;margin-top:10px">${n}</div><div style="font-size:23px;line-height:1.32;margin-top:16px">${t}</div></div>`).join('')}
  </div>
  <div class="ser" style="font-size:40px;line-height:1.15;text-align:center;margin-top:44px;font-style:italic;color:#F4F6F6">Hacen falta las tres. Si una se queda atrás, el negocio no mejora.</div>
</div>
${foot('La idea')}
</section>`;

// 2 · El camino
const F = [
  ['Diagnóstico', T, '#fff', 'Entender dónde se pierde tiempo, calidad o dinero.'],
  ['Diseño', G, '#fff', 'Decidir qué se cambia y cómo.'],
  ['Piloto', A, INK, 'Probar en pequeño, con gente y casos reales.'],
  ['Escala', T, '#fff', 'Extender lo que ha funcionado.'],
  ['Sostenimiento', G, '#fff', 'Que la mejora siga sin el equipo que la trajo.'],
];
const XL = 230, XR = 1010, Y0 = 640, DY = 196, R = 74;
const pt = i => [i % 2 ? XR : XL, Y0 + i * DY];
let road = `M${XL} ${Y0 - 130} L${XL} ${Y0}`;
for (let i = 0; i < 4; i++) { const [x1, y1] = pt(i), [x2, y2] = pt(i + 1); road += ` C${x1} ${y1 + DY * .75} ${x2} ${y2 - DY * .75} ${x2} ${y2}`; }
road += ` L${XL} ${Y0 + 4 * DY + 120}`;
const p2 = `<section class="page light">
<svg class="sun" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><path d="${road}" fill="none" stroke="#E3DFD2" stroke-width="46" stroke-linecap="round" stroke-linejoin="round"/><path d="${road}" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="18 16"/>
${F.map(([n, c, fg], i) => { const [x, y] = pt(i); return `<circle cx="${x}" cy="${y}" r="${R}" fill="${c}"/><text x="${x}" y="${y + 30}" text-anchor="middle" font-family="Garamond" font-size="92" fill="${fg}">${i + 1}</text>`; }).join('')}
</svg>
${top(2, false)}
<div class="z" style="margin-top:56px">
  <div class="k" style="color:${T}">El camino</div>
  <h1 style="font-size:104px;letter-spacing:-3px;margin-top:14px">Cinco pasos, <span style="font-style:italic;color:${G}">siempre<br>en este orden.</span></h1>
</div>
<div class="z" style="position:absolute;left:${XL + 60}px;top:${Y0 - 150}px;background:${INK};color:#F4F6F6;padding:12px 22px;font-size:22px;border-radius:0 14px 0 14px"><b style="color:${AV}">Salida.</b> Algo frena al negocio.</div>
${F.map(([n, c, fg, t], i) => { const [x, y] = pt(i); const left = i % 2 === 0;
  return `<div class="z" style="position:absolute;top:${y - 62}px;${left ? `left:${x + R + 34}px;text-align:left` : `right:${W - x + R + 34}px;text-align:right`};width:560px"><div class="ser" style="font-size:62px;line-height:1;color:${c === A ? AT : c}">${n}</div><div style="font-size:25px;line-height:1.3;margin-top:8px;color:${INK}">${t}</div></div>`; }).join('')}
<div class="z leaf" style="position:absolute;left:${XL + 60}px;right:80px;top:${Y0 + 4 * DY + 84}px;background:${INK};color:#F4F6F6;padding:16px 28px 20px"><span class="ser" style="font-size:40px;line-height:1.1"><b style="color:${AV};font-weight:500">Llegada.</b> El negocio mejora y la mejora se mantiene.</span></div>
<div class="z" style="position:absolute;left:80px;right:80px;top:1606px;font-size:23px;line-height:1.35;color:${GREY};text-align:center">Al final de cada paso se decide por escrito: <b style="color:${INK}">seguir, ajustar o parar.</b></div>
${foot('El camino')}
</section>`;

// 3 · Cuatro ideas
const R4 = [
  ['Primero, el negocio', 'Se empieza por lo que más frena al negocio. No por la herramienta.', TV],
  ['Antes de automatizar, quitar', 'Si una tarea no hace falta, se elimina. Lo demás se acelera, se automatiza o se mejora.', GV],
  ['La gente, antes que la máquina', 'Primero las personas y lo que saben. La tecnología entra después.', AV],
  ['Se mide en el negocio', 'Dos números: cuánto mejora el trabajo y cuánto gana el negocio con ello.', '#F4F6F6'],
];
const p3 = `<section class="page green">${SUN(.6, ['#2E6B41', '#3A7E50', '#286039'])}
${top(3, true)}
<div class="z" style="margin-top:56px">
  <div class="k" style="color:#A9D9B8">Para recordar</div>
  <h1 style="font-size:124px;margin-top:14px">Cuatro ideas<br><span style="font-style:italic;color:${AV}">y nada más.</span></h1>
</div>
<div class="z" style="margin-top:50px">
  ${R4.map(([h, t, c], i) => `<div style="display:flex;gap:34px;align-items:center;padding:24px 0;border-top:2px solid rgba(244,246,246,.25)"><div class="ser" style="font-size:150px;line-height:.8;color:${c};width:96px;text-align:center">${i + 1}</div><div><div class="ser" style="font-size:54px;line-height:1.02">${h}</div><div style="font-size:25px;line-height:1.32;color:#DCEBE0;margin-top:8px;width:880px">${t}</div></div></div>`).join('')}
</div>
<div class="z leaf" style="position:absolute;left:80px;right:80px;top:1338px;background:#F4F6F6;color:${INK};padding:26px 36px 30px">
  <div>${EJ}</div>
  <div style="display:flex;align-items:center;gap:36px;margin-top:10px">
    <div class="ser" style="font-size:118px;line-height:.9;white-space:nowrap"><span style="color:${GREY}">40</span> <span style="color:${T}">→</span> <span style="color:${G}">28</span> <span style="font-size:54px">días</span></div>
    <div style="font-size:24px;line-height:1.34">Resolver un expediente pasa de 40 a 28 días. El método sirve para llegar ahí sin perder por el camino a la gente ni lo que sabe.</div>
  </div>
</div>
${foot('Cuatro ideas')}
</section>`;

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  const f = path.join(dir, '_ese.html'); fs.writeFileSync(f, `<!doctype html><html lang="es"><head><meta charset="utf-8"><style>${css}</style></head><body>${p1}${p2}${p3}</body></html>`);
  await p.goto('file://' + f); await p.waitForTimeout(900);
  console.log('alturas', (await p.evaluate(() => [...document.querySelectorAll('.page')].map(s => s.scrollHeight))).join(' '));
  for (let i = 0; i < 3; i++) await p.screenshot({ path: path.join(out, `infografia-esencial-${i + 1}.png`), clip: { x: 0, y: i * H, width: W, height: H }, fullPage: true });
  await p.pdf({ path: path.join(out, 'Synergos-Lo-esencial-del-metodo.pdf'), width: W + 'px', height: H + 'px', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  fs.unlinkSync(f); await b.close(); console.log('ok');
})();
