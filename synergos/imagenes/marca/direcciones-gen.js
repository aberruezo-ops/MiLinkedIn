const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const F = path.join(__dirname, '../fuentes/node_modules/@fontsource');
const face = (fam, pkg, w, style = 'normal') => `@font-face{font-family:'${fam}';font-weight:${w};font-style:${style};src:url('file://${F}/${pkg}/files/${pkg}-latin-${w}-${style}.woff2')}`;
const faces = [
  ...[400, 600, 800, 900].map(w => face('Archivo', 'archivo', w)), ...[500, 700].map(w => face('Archivo Narrow', 'archivo-narrow', w)),
  ...[400, 500, 600].map(w => face('Plex', 'ibm-plex-sans', w)), face('Plex', 'ibm-plex-sans', 400, 'italic'), ...[400, 500].map(w => face('PlexMono', 'ibm-plex-mono', w)),
  ...[400, 600, 800].map(w => face('Bricolage', 'bricolage-grotesque', w)), ...[400, 600].map(w => face('Public', 'public-sans', w)), ...[500, 700].map(w => face('Caveat', 'caveat', w)),
  ...[700, 900].map(w => face('Shoulders', 'big-shoulders-display', w)), ...[400, 500, 600].map(w => face('Instrument', 'instrument-sans', w)),
].join('\n');
const IM='/home/user/MiLinkedIn/synergos/imagenes/';
const LOGO=(h)=>`<img src="file://${IM}logo-synergos.svg" style="height:${h}px">`;
const LOGOD=(h)=>`<img src="file://${IM}logo-synergos-dark.svg" style="height:${h}px">`;
const INK = '#1F1D1A', GREEN = '#2C6D3F', TERRA = '#B5512A', ALB = '#C89A2A', GREY = '#5A5F63';
const dots = (n, cx, cy, R, col, op = 1) => { let s = ''; const GA = 137.50776405 * Math.PI / 180, c = R / Math.sqrt(n); for (let i = 1; i <= n; i++) { const r = c * Math.sqrt(i), t = i * GA; s += `<circle cx="${(cx + r * Math.cos(t)).toFixed(1)}" cy="${(cy + r * Math.sin(t)).toFixed(1)}" r="${(c * (0.34 + 0.12 * Math.sqrt(i / n))).toFixed(1)}" fill="${col}" opacity="${op}"/>`; } return s; };
const TXT = 'Un piloto prueba en pequeño, con gente real y datos reales, lo que el diseño ha decidido. Si se elige el equipo más motivado y el servicio más sencillo, funciona muy bien y no representa al resto.';
const pil = [['Personas', TERRA, 'Quién responde y quién enseña'], ['Conocimiento', GREEN, 'Lo que nadie ha escrito'], ['Tecnología', ALB, 'Acelera, automatiza o aumenta']];

const A = `<div class="s" style="background:#fff;font-family:Plex;color:#111">
 <div style="display:flex;justify-content:space-between;align-items:flex-end;border-bottom:6px solid #111;padding-bottom:18px">
  ${LOGO(92)}
  <div style="font-family:PlexMono;font-size:17px;text-align:right;line-height:1.5">MÉTODO · V1.8<br>CRECER A LA VEZ</div></div>
 <div class="lab" style="font-family:PlexMono">A · TALLER</div>
 <div style="font-family:Archivo;font-weight:800;font-size:60px;line-height:1.02;letter-spacing:-1.5px;margin:10px 0 18px">Un piloto que no representa no prueba nada.</div>
 <p style="font-size:23px;line-height:1.5;max-width:900px">${TXT}</p>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);margin-top:34px;border:3px solid #111">
  ${pil.map(([t, c, d], i) => `<div style="padding:22px;${i ? 'border-left:3px solid #111' : ''}"><div style="font-family:PlexMono;font-size:17px">0${i + 1}</div><div style="height:16px;background:${c};margin:10px 0 14px"></div><div style="font-family:Archivo;font-weight:800;font-size:34px;letter-spacing:-.5px">${t}</div><div style="font-size:19px;color:#444;margin-top:6px;line-height:1.35">${d}</div></div>`).join('')}</div>
 <div style="margin-top:30px;display:flex;border-top:3px solid #111;border-bottom:3px solid #111"><div style="background:#111;color:#fff;font-family:PlexMono;font-size:16px;padding:18px 16px;writing-mode:vertical-rl;transform:rotate(180deg)">SEÑAL DE FALLO</div><div style="padding:20px 24px;font-size:22px;line-height:1.45">Las puertas se aprueban por calendario y no por evidencias. Cuando la puerta se pasa porque toca, deja de ser una puerta.</div></div>
 <div class="foot" style="font-family:PlexMono">Archivo + IBM Plex · papel blanco, tinta negra, color en bloques · aire de plano técnico</div></div>`;

const B = `<div class="s" style="background:#FBFBF8;font-family:Public;color:${INK};background-image:radial-gradient(#d9d9d2 1.3px,transparent 1.4px);background-size:26px 26px">
 <div style="display:flex;align-items:center;gap:22px"><svg width="96" height="96">${dots(90, 48, 48, 44, GREEN)}</svg>
  <div>${LOGO(84)}<div style="font-family:Bricolage;font-weight:600;font-size:26px;color:${GREEN};margin-top:6px">Crecer a la vez.</div></div></div>
 <div class="lab">B · CUADERNO</div>
 <div style="position:relative;background:#fff;padding:34px 38px;margin-top:8px;box-shadow:0 1px 0 #cfcfc8, 0 10px 30px rgba(0,0,0,.06)">
  <div style="font-family:Bricolage;font-weight:800;font-size:54px;line-height:1.05;letter-spacing:-1px">Un piloto que no representa <span style="background:linear-gradient(transparent 62%,#F1D98A 62%)">no prueba nada</span>.</div>
  <p style="font-size:23px;line-height:1.55;margin-top:18px;max-width:840px">${TXT}</p>
  </div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:44px">
  ${pil.map(([t, c, d]) => `<div style="background:#fff;padding:22px;border-radius:14px 14px 14px 2px;border:2.5px solid ${c === ALB ? '#8A6508' : c}"><div style="width:44px;height:44px;border-radius:50%;background:${c};margin-bottom:12px"></div><div style="font-family:Bricolage;font-weight:800;font-size:32px">${t}</div><div style="font-size:19px;color:${GREY};margin-top:6px;line-height:1.35">${d}</div></div>`).join('')}</div>
 
 <div class="foot">Bricolage Grotesque + Public Sans · papel con puntos, subrayado de rotulador · tono de cuaderno de trabajo</div></div>`;

const C = `<div class="s" style="background:${INK};font-family:Instrument;color:#F3F1EC;padding:0">
 <div style="background:${GREEN};padding:44px 50px 36px;position:relative;overflow:hidden"><svg width="520" height="520" style="position:absolute;right:-120px;top:-150px">${dots(420, 260, 260, 250, '#fff', .16)}</svg>
  ${LOGOD(130)}
  <div style="font-size:24px;font-weight:500;margin-top:14px;letter-spacing:.5px">Crecer a la vez.</div></div>
 <div style="padding:20px 50px 0"><div class="lab" style="color:#A9B0A9;margin-top:10px">C · CARTEL</div>
 <div style="font-family:Shoulders;font-weight:900;font-size:96px;line-height:.9;text-transform:uppercase;margin:8px 0 18px">Un piloto que no representa <span style="color:${ALB}">no prueba nada.</span></div>
 <p style="font-size:23px;line-height:1.5;max-width:900px;color:#D8D6CF">${TXT}</p></div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);margin-top:30px">
  ${pil.map(([t, c, d]) => `<div style="background:${c};color:${c === ALB ? INK : '#fff'};padding:26px 26px 30px"><div style="font-family:Shoulders;font-weight:900;font-size:58px;text-transform:uppercase;line-height:.95">${t}</div><div style="font-size:20px;margin-top:10px;line-height:1.35;font-weight:500">${d}</div></div>`).join('')}</div>
 <div style="padding:26px 50px"><div style="border-left:10px solid ${TERRA};padding-left:22px;font-size:22px;line-height:1.45"><b style="font-family:Shoulders;font-size:30px;letter-spacing:1px;text-transform:uppercase;color:#E08A66">Señal de fallo</b><br>Las puertas se aprueban por calendario y no por evidencias.</div>
 <div class="foot" style="color:#A9B0A9;border-color:#444">Big Shoulders + Instrument Sans · fondo oscuro, color a toda página · tono de cartel</div></div></div>`;

const css = `${faces}*{box-sizing:border-box;margin:0;padding:0}body{background:#888;display:flex;gap:30px;padding:30px;width:3690px}.s{width:1190px;min-height:920px;padding:50px;position:relative}.lab{font-size:17px;letter-spacing:3px;color:${GREY};margin:34px 0 6px}.foot{margin-top:30px;border-top:1.5px solid #bbb;padding-top:14px;font-size:17px;color:${GREY}}`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3690, height: 1100 }, deviceScaleFactor: 1 });
  const html = path.join(__dirname, 't.html');
  fs.writeFileSync(html, `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${A}${B}${C}</body></html>`);
  await p.goto('file://' + html); await p.waitForTimeout(1200);
  const els = await p.$$('.s'); const names = ['A-taller', 'B-cuaderno', 'C-cartel'];
  for (let i = 0; i < 3; i++) await els[i].screenshot({ path: path.join(__dirname, names[i] + '.png') });
  await p.screenshot({ path: path.join(__dirname, 'tres.png'), fullPage: true }); await b.close();
})();
