// Tres figuras de base del documento, en el estilo de hoja (esquinas opuestas redondeadas).
// Uso: NODE_PATH=$(npm root -g) node figs/base-figs.js
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const dir = __dirname, out = path.join(dir, '..');
const INK = '#1F1D1A', GREEN = '#2C6D3F', TERRA = '#B5512A', ALB = '#C89A2A', ALBT = '#8A6508', GREY = '#56606A', LINE = '#D7DCDC';
const LOGO = 'file://' + path.join(dir, '../../../imagenes/logo-synergos.svg');
const base = `*{box-sizing:border-box;margin:0;padding:0}body{background:#fff;font-family:'Public Sans',sans-serif;color:${INK}}
.serif{font-family:'EB Garamond',serif}.mark{position:absolute;right:50px;top:44px;height:44px}`;

// 1. Arquitectura: el orden contiene los tres elementos
const arq = `<style>${base}
body{width:1600px;height:1060px;position:relative}
h1{position:absolute;left:60px;top:44px;font-family:'EB Garamond',serif;font-weight:normal;font-size:56px}
.obj{position:absolute;left:60px;right:60px;top:112px;height:104px;background:#fff;border:3px solid ${INK};border-radius:16px 0 60px 0;padding:0 40px;display:flex;align-items:center;gap:44px}
.obj b{font-family:'EB Garamond',serif;font-weight:normal;font-size:44px;white-space:nowrap}
.obj span{font-size:22px;line-height:1.38;color:${GREY}}
.obj i{font-style:normal;font-size:16px;letter-spacing:4px;text-transform:uppercase;font-weight:600;color:${TERRA};white-space:nowrap}
.panel{position:absolute;left:60px;right:60px;top:150px;height:860px;background:#F4F6F6;border-radius:16px 0 110px 0}
.lab{position:absolute;left:60px;top:34px;font-size:18px;letter-spacing:4px;text-transform:uppercase;color:${GREEN};font-weight:600}
.sub{position:absolute;left:60px;top:66px;font-size:23px;color:${GREY}}
.blk{position:absolute;top:244px;width:400px;height:360px;padding:34px 36px;color:#fff}
.blk b{font-family:'EB Garamond',serif;font-weight:normal;font-size:56px;display:block;margin-bottom:14px}
.blk span{font-size:23px;line-height:1.4;display:block}
.base{position:absolute;left:60px;right:60px;top:590px;height:150px;background:${INK};color:#fff;border-radius:0 16px 0 70px;padding:32px 44px}
.base b{font-family:'EB Garamond',serif;font-weight:normal;font-size:40px;display:block;margin-bottom:8px}
.base span{font-size:22px;color:#D7DCDC}
.cierre{position:absolute;left:60px;top:772px;font-family:'EB Garamond',serif;font-style:italic;font-size:34px;color:${GREEN}}
</style><img class="mark" src="${LOGO}"><h1>Un objetivo, tres elementos, un orden</h1>
<div class="panel"><div class="lab">Los tres crecen a la vez</div><div class="sub">Ninguno avanza solo. El orden decide en qué secuencia y con qué puertas.</div>
<div class="obj"><i>El objetivo</i><b>Impacto en el negocio</b><span>El resultado que la organización quiere cambiar. Los tres elementos son las palancas para alcanzarlo.</span></div>
<div class="blk" style="left:60px;background:${TERRA};border-radius:16px 0 100px 0"><b>Personas</b><span>Liderazgo, roles e incentivos, seguridad psicológica, interacción, quién enseña</span></div>
<div class="blk" style="left:540px;background:${GREEN};border-radius:0 16px 0 100px"><b>Conocimiento</b><span>Explícito, tácito (el mapa), supervisión de doble bucle</span></div>
<div class="blk" style="left:1020px;background:${ALB};color:${INK};border-radius:16px 0 100px 0"><b>Tecnología</b><span>IA en sus dos papeles, frontera, autonomía, entorno, radar, medida justa</span></div>
<div class="base" style="top:644px;left:60px;right:60px"><b>El orden</b><span>Fases y puertas · estrategia · gobierno · modelo económico · medición y delta · madurez</span></div></div>`;

// 2. Fases: cinco fases, cinco puertas y el bucle de aprendizaje
const fase = (n, t, d, c) => `<div class="f" style="background:${c[0]}"><i style="color:${c[1]}">${n}</i><b>${t}</b><span>${d}</span></div>`;
const fases = `<style>${base}
body{width:1800px;height:700px;position:relative}
h1{position:absolute;left:50px;top:36px;font-family:'EB Garamond',serif;font-weight:normal;font-size:46px}
.row{position:absolute;left:50px;right:50px;top:140px;display:flex;align-items:center}
.f{flex:1;height:250px;padding:26px 26px;border-radius:12px 0 64px 0}
.f i{font-family:'EB Garamond',serif;font-style:normal;font-size:50px;display:block;line-height:1;margin-bottom:8px}
.f b{font-family:'EB Garamond',serif;font-weight:normal;font-size:38px;display:block;margin-bottom:8px}
.f span{font-size:20px;line-height:1.38;color:${GREY};display:block}
.ar{flex:0 0 60px;text-align:center;font-size:36px;color:${GREEN}}
.loop{position:absolute;left:50px;right:50px;top:430px}
.foot{position:absolute;left:50px;top:610px;width:1700px;text-align:center;font-size:22px;color:${GREY}}
</style><img class="mark" style="right:50px;top:34px;height:40px" src="${LOGO}"><h1>Cinco fases, cinco puertas</h1>
<div class="row">${fase(1, 'Diagnóstico', 'Restricción, línea base, mapa de lo que nadie escribió', ['#EAF2EC', GREEN])}<div class="ar">→</div>${fase(2, 'Diseño', 'Cartera, trabajo nuevo, cinco preguntas', ['#F8EDD0', ALBT])}<div class="ar">→</div>${fase(3, 'Piloto', 'Gente y datos reales, criterios previos', ['#F8E9E1', TERRA])}<div class="ar">→</div>${fase(4, 'Escala', 'Por etapas, con roles e incentivos', ['#EAF2EC', GREEN])}<div class="ar">→</div>${fase(5, 'Sostenimiento', 'Dueño, presupuesto, dos periodos sin el equipo', ['#ECEEEE', INK])}</div>
<svg class="loop" width="1700" height="150" viewBox="0 0 1700 150"><path d="M1560 0 C1560 120 1450 140 1300 140 L400 140 C250 140 140 120 140 22" fill="none" stroke="${GREEN}" stroke-width="3.5" stroke-linecap="round"/><path d="M140 6 L128 36 L152 36 Z" fill="${GREEN}"/></svg>
<div class="foot">Una puerta al final de cada fase: pasar, ajustar y repetir, o retirar. Lo aprendido en el sostenimiento alimenta el siguiente diagnóstico.</div>`;

// 3. Girasol: el ángulo de 137,5 grados
const gira = `<style>${base}
body{width:1200px;height:1040px;position:relative}
canvas{position:absolute;left:0;top:0}
.tag{position:absolute;left:690px;top:300px;background:${GREEN};color:#fff;font-family:'EB Garamond',serif;font-size:62px;padding:8px 40px 14px 30px;border-radius:0 16px 0 40px}
.cap{position:absolute;left:60px;right:60px;top:968px;font-size:24px;color:${GREY}}
</style><canvas id="c" width="1200" height="1040"></canvas><div class="tag">137,5°</div><div class="cap">Cada semilla nueva se gira 137,5° respecto a la anterior. Así crece sin dejar huecos ni solaparse.</div>
<script>
const g=document.getElementById('c').getContext('2d');const GA=137.50776405*Math.PI/180,N=900,cx=520,cy=500,R=430,c=R/Math.sqrt(N);
const mix=(A,B,t)=>{const p=h=>[1,3,5].map(i=>parseInt(h.substr(i,2),16));const a=p(A),b=p(B);return '#'+a.map((v,i)=>Math.round(v+(b[i]-v)*t).toString(16).padStart(2,'0')).join('')};
for(let n=1;n<=N;n++){const r=c*Math.sqrt(n),th=n*GA;const t=n/N;g.fillStyle=t<.62?mix('${INK}','${GREEN}',Math.min(1,t*1.6)):mix('${GREEN}','#7CC090',(t-.62)/.38);g.beginPath();g.arc(cx+r*Math.cos(th),cy+r*Math.sin(th),c*(0.42+0.12*Math.sqrt(t)),0,7);g.fill();}
g.strokeStyle='${TERRA}';g.lineWidth=6;g.lineCap='round';g.beginPath();g.moveTo(cx,cy);g.lineTo(cx+330,cy);g.stroke();g.beginPath();g.moveTo(cx,cy);g.lineTo(cx+330*Math.cos(-GA),cy+330*Math.sin(-GA));g.stroke();
g.beginPath();g.arc(cx,cy,100,-GA,0);g.stroke();
</script>`;

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1800, height: 1100 }, deviceScaleFactor: 2 });
  for (const [name, html, sel] of [['fig-arquitectura.png', arq, 'body'], ['fig-fases.png', fases, 'body'], ['fig-girasol.png', gira, 'body']]) {
    const tmp = path.join(dir, '_' + name + '.html'); fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"></head><body>${html.replace(/^<style>/, '<style>')}</body></html>`);
    await p.goto('file://' + tmp); await p.waitForTimeout(600);
    await (await p.$(sel)).screenshot({ path: path.join(out, name) }); fs.unlinkSync(tmp); console.log('ok', name);
  }
  await b.close();
})();
