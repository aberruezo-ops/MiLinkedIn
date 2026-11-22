// Infografía del método en seis páginas (A4). NODE_PATH=$(npm root -g) node figs/infografia-3p.js
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
const top = (n, dark) => `<div class="top z"><img src="file://${IM}${dark ? 'logo-synergos-dark.svg' : 'logo-synergos.svg'}"><span>El método en seis páginas · versión 2.1</span><span class="pg" style="color:inherit">${n} <span style="opacity:.45">/ 6</span></span></div>`;
const TRAIL = [['Para qué', 'Para qué'], ['Personas y conocimiento', 'Qué mirar'], ['El tronco: fases y puertas', 'Camino'], ['Los roles del método', 'Quién'], ['Cómo se mide', 'Medir'], ['IA e innovación', 'IA']];
const foot = t => { const cur = TRAIL.findIndex(x => x[0] === t);
  const crumb = (txt, state, last) => `<span style="display:inline-flex;align-items:center;gap:6px"><span style="${state === 'now' ? 'font-weight:700;color:var(--nc);border-bottom:3px solid var(--tc)' : state === 'done' ? 'opacity:.9' : 'opacity:.5'}">${txt}</span>${last ? '' : '<span style="opacity:.4">›</span>'}</span>`;
  const items = [['Inicio', 'done']].concat(TRAIL.map((x, i) => [x[1], i === cur ? 'now' : i < cur ? 'done' : 'todo'])).concat([['Impacto en el negocio', cur === TRAIL.length - 1 ? 'goal' : 'todo']]);
  const html = items.map(([txt, st], i) => st === 'goal' ? `<span style="display:inline-flex;align-items:center;gap:6px"><span style="font-weight:700;color:${AV}">${txt}</span></span>` : crumb(txt, st, i === items.length - 1)).join(' ');
  return `<div class="foot" style="--tc:${AV};--nc:${t === TRAIL[2][0] ? INK : '#fff'}"><i>Crecer a la vez.</i><span style="display:flex;gap:8px;align-items:center;font-size:12.5px;letter-spacing:2px">${html}</span></div>`; };

// ---------- Página 1: para qué ----------
const STEP = (n, t, c, body, fg = '#F4F6F6') => `<div style="display:grid;grid-template-columns:170px 1fr;gap:26px;align-items:stretch"><div class="${n % 2 ? 'leaf' : 'leafb'}" style="background:${c};color:${INK};display:flex;flex-direction:column;justify-content:center;padding:22px 20px"><span class="ser" style="font-size:64px;line-height:.9">${n}</span><span class="k" style="font-size:13px;letter-spacing:3px;margin-top:8px">${t}</span></div><div style="padding:4px 0">${body}</div></div>`;
const ARR = (t) => `<div style="display:flex;align-items:center;gap:14px;margin:30px 0 30px 70px;color:${MUT};font-size:17px;letter-spacing:3px;text-transform:uppercase;font-weight:600"><span style="font-size:24px;color:${GV}">↓</span>${t}</div>`;
const p1 = `<section class="page dark">
${girasol({ cx: 1100, cy: 330, n: 420, c: 10, rot: .5, s0: 3, sk: .02 })}
${top(1, true)}
<div class="z" style="margin-top:40px">
  <div class="k" style="color:${GV}">1 · ¿Para qué sirve este método?</div>
  <h1 style="font-size:150px;margin:12px 0 0 -6px">Crecer<br><span style="font-style:italic;color:${GV}">a la vez.</span></h1>
  <p style="font-size:24px;line-height:1.42;color:${MUT};width:600px;margin-top:18px">Para que una transformación mejore el negocio, de verdad, y se mantenga cuando el equipo del programa se vaya.</p>
</div>

<div class="z" style="margin-top:44px">
  ${STEP(1, 'El problema', TV, `<div class="ser" style="font-size:42px;line-height:1.05">Las transformaciones se rompen</div><div style="font-size:20px;line-height:1.42;color:${MUT};margin-top:8px">Casi siempre por una de tres causas: se elige la solución antes de entender el problema, la tecnología llega antes que el cambio en la forma de trabajar, o se sustituye a quien sabía sin haberlo mirado.</div>`)}
  ${ARR('Por eso el método fija')}
  ${STEP(2, 'El objetivo', AV, `<div class="ser" style="font-size:42px;line-height:1.05">Impacto en el negocio</div><div style="font-size:20px;line-height:1.42;color:${MUT};margin-top:8px">Ingresar más, gastar menos, servir mejor o poder hacer algo que antes no se podía. Es para qué se mueve todo lo demás.</div>`)}
  ${ARR('Y lo busca moviendo tres palancas a la vez')}
  ${STEP(3, 'Las palancas', GV, `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px"><div class="leaf" style="background:${TV};color:#fff;padding:12px 16px 14px"><div class="ser" style="font-size:32px">Personas</div><div style="font-size:16.5px;line-height:1.35;margin-top:4px">Liderazgo, roles, incentivos y quién enseña el oficio.</div></div><div class="leafb" style="background:${GV};color:${INK};padding:12px 16px 14px"><div class="ser" style="font-size:32px">Conocimiento</div><div style="font-size:16.5px;line-height:1.35;margin-top:4px">Lo escrito, lo que nadie escribió y lo que aprende el programa.</div></div><div class="leaf" style="background:${AV};color:${INK};padding:12px 16px 14px"><div class="ser" style="font-size:32px">Tecnología</div><div style="font-size:16.5px;line-height:1.35;margin-top:4px">La IA entra cuando lo demás está listo.</div></div></div><div style="font-size:19px;line-height:1.4;color:${MUT};margin-top:10px">Ninguna crece a costa de las otras.</div>`)}
  ${ARR('Con un orden')}
  ${STEP(4, 'El orden', '#E8DFC9', `<div class="ser" style="font-size:42px;line-height:1.05">Cinco fases, cada una con una puerta</div><div style="font-size:20px;line-height:1.42;color:${MUT};margin-top:8px">En cada puerta se decide por escrito: pasar, ajustar y repetir, o retirar. Así un error cuesta poco y se puede deshacer.</div>`)}
</div>
<div class="z" style="margin-top:34px;font-size:18px;line-height:1.4;color:${MUT}">En las páginas siguientes: qué se mira primero, cómo se avanza, quién interviene, cómo se sabe que funciona y dónde entra la IA.</div>
${foot('Para qué')}
</section>`;

// ---------- Página 2: lo que nadie escribió ----------
const PG = '#A9D9B8', GD = '#173A22';
const pm = `<section class="page green">
${girasol({ cx: 1262, cy: 400, n: 480, c: 13, rot: 3.1, s0: 3.2, sk: .02, cols: [AV, '#7CC090', TV], op: .95 })}
${top(2, true)}
<div class="z" style="margin-top:42px;width:940px">
  <div class="k" style="color:${AV}">2 · ¿Qué se mira primero?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">Antes de decidir,<br><span style="font-style:italic;color:${AV}">mirar lo que nadie escribió.</span></h1>
  <p style="font-size:21px;line-height:1.42;color:#DCEBE1;width:690px;margin-top:20px">El conocimiento vive en las personas, en la organización y en la tecnología. Lo que decide una transformación es a dónde va.</p>
</div>

<div class="z leaf" style="margin-top:30px;background:${PAPER};color:${INK};padding:22px 28px 26px">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><div><span class="k" style="color:${G}">El entregable del diagnóstico</span><div class="ser" style="font-size:44px;line-height:1.05;margin-top:4px">El mapa de lo que nadie escribió</div></div><div style="font-size:14px;color:${GREY};text-align:right;width:230px;line-height:1.35">Ejemplo compuesto e ilustrativo, por perfiles y sin nombres.</div></div>
  <div style="display:grid;grid-template-columns:1.55fr 1fr .8fr .9fr;gap:6px;margin-top:14px;font-size:17px;line-height:1.32">
    ${['Qué se sabe', 'Quién lo sabe', 'Dónde se usa', 'Concentración'].map(t => `<div class="k" style="font-size:12.5px;letter-spacing:3.5px;color:${G};padding:8px 12px;background:#E3EEE6">${t}</div>`).join('')}
    ${[['Qué peticiones acabarán en reclamación', 'Perfil A y perfil B', 'Triaje', 'Dos personas', 0], ['A quién llamar en otra unidad cuando algo se atasca', 'Perfil A', 'Excepciones', 'Una persona', 1]]
      .map(([a, b, c, d, hot]) => [a, b, c, d].map((t, j) => `<div style="padding:12px 12px;background:${hot ? (j === 3 ? T : '#F7E4DA') : '#EFEDE6'};color:${hot && j === 3 ? '#fff' : INK};font-weight:${j === 3 || j === 0 ? 600 : 400}">${t}</div>`).join('')).join('')}
  </div>
  <div style="font-size:16.5px;line-height:1.4;margin-top:12px;color:${GREY}">Una fila que dice "una persona" se ve. Y con cada opción de diseño se responde, fila a fila, qué le pasa a ese conocimiento.</div>
</div>

<div class="z" style="margin-top:30px;display:grid;grid-template-columns:1.08fr 1fr;gap:44px">
  <div>
    <div class="k" style="color:${AV}">Cómo se levanta</div>
    <h2 style="margin:8px 0 10px;font-size:40px">Cinco preguntas por las grietas</h2>
    ${['¿Qué casos parecen iguales y no lo son? ¿Cómo los distingues?', '¿Cuándo no sigues el procedimiento, y por qué?', '¿A quién llamas cuando algo se atasca? ¿Y quién te llama a ti?', '¿Qué sabes de un caso antes de leerlo entero?', '¿Qué pasaría mañana si tú no vinieras?']
      .map((t, i) => `<div style="display:flex;gap:16px;align-items:baseline;padding:8.5px 0;border-top:1px solid rgba(244,246,246,.28)"><span class="ser" style="font-size:32px;line-height:.9;color:${AV};flex:0 0 24px">${i + 1}</span><span style="font-size:18px;line-height:1.34">${t}</span></div>`).join('')}
  </div>
  <div>
    <div class="k" style="color:${AV}">Con cada opción de diseño</div>
    <h2 style="margin:8px 0 12px;font-size:40px">Tres destinos para cada fila</h2>
    ${[['Se queda en la persona', 'y la tecnología la ayuda.', '#7CC090', INK], ['Pasa al sistema', 'de forma revisable.', AV, INK], ['Se pierde', 'y se decide sabiéndolo.', TV, '#fff']]
      .map(([a, b, c, fg], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${c};color:${fg};padding:11px 22px 14px;margin-bottom:8px"><span class="ser" style="font-size:30px;line-height:1.05">${a}</span> <span style="font-size:17px">${b}</span></div>`).join('')}
    <div style="font-size:16.5px;line-height:1.42;color:#DCEBE1;margin-top:12px;border-left:6px solid ${AV};padding-left:14px"><b style="font-weight:700;color:#fff">El compromiso de uso.</b> Antes de empezar, el patrocinador firma que el mapa no se usará para evaluar a nadie ni para decidir despidos. Sin esa firma, el mapa no se hace.</div>
  </div>
</div>

<div class="z" style="margin-top:30px">
  <div class="k" style="color:${AV}">La cuarta pregunta de la puerta</div>
  <h2 style="margin:8px 0 12px;font-size:40px">¿Quién enseña lo que la tarea enseñaba?</h2>
  <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px">
    ${['Aprender corrigiendo', 'Tareas reservadas para formar', 'La IA como tutora', 'Tiempo reconocido para enseñar', 'Rotación por el caso difícil']
      .map((t, i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${GD};padding:12px 14px 18px;min-height:112px"><div class="ser" style="font-size:34px;line-height:.9;color:${AV}">${i + 1}</div><div style="font-size:16.5px;font-weight:600;line-height:1.25;margin-top:6px">${t}</div></div>`).join('')}
  </div>
  <div style="font-size:15.5px;line-height:1.4;color:#CFE3D5;margin-top:8px">Cinco diseños posibles. Ninguno está probado lo bastante: se eligen en el diseño, no se dan por receta.</div>
</div>

${foot('Personas y conocimiento')}
</section>`;

// ---------- Página 3: el tronco ----------
const F = [
  ['Diagnóstico', T, '#fff', 'Entender dónde se pierden tiempo, calidad o dinero, y por qué.', 'Restricción nombrada, línea base medida y mapa de lo que nadie escribió.'],
  ['Diseño', G, '#fff', 'Decidir qué se cambia, cómo y con qué aceleradores.', 'Cada iniciativa ataca la restricción y responde por escrito a las cinco preguntas.'],
  ['Piloto', A, INK, 'Probar en pequeño, con gente y datos reales.', 'Cumple los criterios que se firmaron antes de empezar.'],
  ['Escala', T, '#fff', 'Extender lo que funciona.', 'Los indicadores aguantan al ampliar y los tres elementos aguantan la carga.'],
  ['Sostenimiento', G, '#fff', 'Que la mejora siga cuando el equipo del programa se vaya.', 'El dueño acepta la responsabilidad y los indicadores aguantan dos periodos de medición.'],
];
const p2 = `<section class="page light">
${girasol({ cx: 1262, cy: 420, n: 480, c: 13, rot: 1.3, s0: 3.2, sk: .02, cols: [T, G, A], op: .55 })}
${top(3, false)}
<div class="z" style="margin-top:42px;width:900px">
  <div class="k" style="color:${T}">3 · ¿Cómo se avanza?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">Cinco fases.<br>Cada una acaba en<br><span style="font-style:italic;color:${G}">una puerta.</span></h1>
</div>

<div class="z" style="margin-top:32px;position:relative">
  <div style="position:absolute;left:55px;top:40px;bottom:40px;width:3px;background:repeating-linear-gradient(${INK} 0 9px,transparent 9px 18px);opacity:.35"></div>
  ${F.map(([n, c, fg, pq, pu], i) => `<div style="display:grid;grid-template-columns:112px 1fr 400px;gap:26px;align-items:stretch;margin-bottom:11px">
    <div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${c};color:${fg};display:flex;align-items:center;justify-content:center;position:relative;z-index:2"><span class="ser" style="font-size:70px;line-height:1">${i + 1}</span></div>
    <div style="padding:8px 0 6px;border-top:2px solid ${INK}"><div class="ser" style="font-size:44px;line-height:1">${n}</div><div style="font-size:18px;line-height:1.36;color:${GREY};margin-top:5px">${pq}</div></div>
    <div class="${i % 2 ? 'leaf' : 'leafb'}" style="background:#fff;border:1.5px solid #D9D6CC;padding:11px 18px 14px"><div class="k" style="font-size:12.5px;letter-spacing:4px;color:${c === A ? AT : c}">Puerta ${i + 1} · tiene que ser cierto</div><div style="font-size:16.5px;line-height:1.34;margin-top:5px">${pu}</div></div>
  </div>`).join('')}
</div>

<div class="z" style="margin-top:12px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px">
  ${[['Pasar', G, 'Se cumplen los criterios.'], ['Ajustar y repetir', AT, 'Promete, pero está incompleto.'], ['Retirar', T, 'No funciona. Retirar es una salida legítima.']]
    .map(([t, c, d]) => `<div style="border-top:6px solid ${c};padding:9px 4px 0"><div class="ser" style="font-size:30px;line-height:1">${t}</div><div style="font-size:16.5px;line-height:1.38;color:${GREY};margin-top:6px">${d}</div></div>`).join('')}
</div>

<div class="z leaf" style="margin-top:22px;background:${INK};color:#F4F6F6;padding:22px 34px 28px;display:grid;grid-template-columns:330px 1fr;gap:38px;align-items:start">
  <div><div class="k" style="color:${AV}">La puerta de diseño</div><div class="ser" style="font-size:46px;line-height:1;margin-top:8px">Cinco preguntas, por escrito</div><div style="font-size:15.5px;line-height:1.4;color:${MUT};margin-top:10px">Los criterios se escriben antes de ver el resultado. Se puede aprobar una opción que pierde conocimiento, pero no sin saberlo.</div></div>
  <div>${['¿Ataca la restricción, y cuánto vale resolverla?', '¿Elimina, acelera, automatiza o aumenta?', '¿Qué le pasa a cada fila del mapa de lo que nadie escribió?', '¿Quién responde de los errores, y quién enseña lo que la tarea enseñaba?', '¿Hace crecer a la vez a los tres elementos, o abarata uno a costa de los otros?']
    .map((t, i) => `<div style="display:flex;gap:18px;align-items:baseline;padding:7px 0;${i ? 'border-top:1px solid rgba(244,246,246,.22)' : ''}"><span class="ser" style="font-size:34px;line-height:.9;color:${[TV, GV, AV][i % 3]};flex:0 0 26px">${i + 1}</span><span style="font-size:18.5px;line-height:1.3">${t}</span></div>`).join('')}</div>
</div>

<div class="z" style="margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:26px;font-size:16px;line-height:1.4">
  <div style="border-left:6px solid ${A};padding-left:16px"><b style="font-weight:700">Regla de entrada.</b> Un acelerador entra en el servicio solo si personas, conocimiento, tecnología y gobierno están en el nivel 2 de madurez: repetible.</div>
  <div style="border-left:6px solid ${G};padding-left:16px"><b style="font-weight:700">El tronco se cierra.</b> Lo aprendido en el sostenimiento alimenta el diagnóstico del siguiente ciclo.</div>
</div>
${foot('El tronco: fases y puertas')}
</section>`;

// ---------- Página 4: los roles ----------
const FAM = [
  ['Quien dirige y decide', AV, INK, [['Órgano de dirección', 'Escribe el objetivo y acepta el riesgo'], ['Patrocinador', 'Decide y firma en las puertas'], ['Dirección del programa', 'Coordina fases, cartera y puertas'], ['Comité de puertas', 'Los cuatro que intervienen en cada puerta']]],
  ['Quien opera y adopta', '#7CC090', INK, [['Dueño operativo', 'Responde de lo que hace la solución'], ['Responsable de adopción', 'Nombra y coordina a los referentes'], ['Quien hace el trabajo', 'Oído antes. Puede dejar de usar y pedir parada'], ['Mando intermedio', 'Oído antes. Fuente del diagnóstico']]],
  ['Quien mide y controla', TV, '#fff', [['Responsable de medición', 'Certifica los datos, no la decisión'], ['Quien contrafirma', 'Ajeno al equipo del programa'], ['Segunda línea', 'Revisa y puede objetar desde el diseño'], ['Dueño de los datos', 'En el negocio, no en sistemas']]],
  ['Quien es oído o recibe el beneficio', '#E8DFC9', INK, [['Dueño del beneficio', 'En el negocio, no en el programa'], ['Representación legal', 'Oída cuando se tocan condiciones de trabajo'], ['Quien defiende a quien recibe el servicio', 'Oída antes, no decide'], ['Quien recibe el servicio', 'Se le pregunta y se miden sus resultados']]],
];
const NOP = ['El patrocinador no contrafirma su propia decisión.', 'El responsable de medición certifica los datos y no firma la decisión.', 'El responsable de adopción no es quien despliega la herramienta.', 'El dueño del beneficio está en el negocio, no en el programa.', 'El dueño de los datos está en el negocio, no en sistemas.', 'Quien defiende a quien recibe el servicio no decide en la puerta.'];
const pr = `<section class="page dark">
${girasol({ cx: 1262, cy: 392, n: 480, c: 13, rot: 5.1, s0: 3.2, sk: .02 })}
${top(4, true)}
<div class="z" style="margin-top:42px;width:900px">
  <div class="k" style="color:${GV}">4 · ¿Quién interviene?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">Quién es quién<br><span style="font-style:italic;color:${GV}">en una puerta.</span></h1>
  <p style="font-size:21px;line-height:1.42;color:${MUT};width:780px;margin-top:20px">Una misma persona puede tener varios roles. Lo que el método no admite es que el control de una puerta quede en las mismas manos.</p>
</div>

<div class="z" style="margin-top:34px;display:grid;grid-template-columns:1fr 1fr;gap:16px">
  ${FAM.map(([t, c, fg, rs], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:#2A2824;overflow:hidden;display:flex;flex-direction:column">
    <div style="background:${c};color:${fg};padding:13px 22px 14px"><div class="k" style="font-size:12px;letter-spacing:4px;opacity:.8">Familia ${i + 1}</div><div class="ser" style="font-size:32px;line-height:1.02;margin-top:2px">${t}</div></div>
    <div style="padding:4px 22px 12px">${rs.map(([a, b], j) => `<div style="padding:9px 0;${j ? 'border-top:1px solid rgba(244,246,246,.18)' : ''}"><div class="ser" style="font-size:25px;line-height:1.1">${a}</div><div style="font-size:16px;line-height:1.35;color:${MUT};margin-top:2px">${b}</div></div>`).join('')}</div>
  </div>`).join('')}
</div>

<div class="z leaf" style="margin-top:20px;border:2px solid rgba(244,246,246,.45);padding:16px 26px 18px">
  <div class="k" style="color:${AV}">Combinaciones que no se admiten</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px 34px;margin-top:10px;font-size:17px;line-height:1.38">
    ${NOP.map((t, i) => `<div style="display:flex;gap:12px;align-items:baseline"><span class="ser" style="font-size:26px;line-height:.9;color:${[TV, GV, AV][i % 3]};flex:0 0 22px">${i + 1}</span><span>${t}</span></div>`).join('')}
  </div>
</div>
<div class="z" style="margin-top:16px;font-size:16px;line-height:1.42;color:${MUT}">En un programa acotado varios roles recaen en la misma persona, pero la firma del patrocinador y la contrafirma de alguien ajeno siguen siendo dos personas distintas.</div>
${foot('Los roles del método')}
</section>`;

// ---------- Página 5: cómo se mide ----------
const ED = '#451A0B', EL = '#F0C3A4', ET = '#EBD3C4';
const pv = `<section class="page earth">
${girasol({ cx: 1262, cy: 392, n: 480, c: 13, rot: 4.0, s0: 3.2, sk: .02, cols: [AV, '#7CC090', TV], op: .95 })}
${top(5, true)}
<div class="z" style="margin-top:42px;width:900px">
  <div class="k" style="color:${AV}">5 · ¿Cómo se sabe que funciona?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">Se mide antes,<br><span style="font-style:italic;color:${AV}">durante y después.</span></h1>
  <p style="font-size:21px;line-height:1.42;color:${ET};width:800px;margin-top:20px">No vale la impresión de la gente ni lo que declara el proveedor. Vale lo que se midió contra lo que había antes.</p>
</div>

<div class="z" style="margin-top:34px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px">
  ${[['1', 'Antes', 'La línea base', 'Se mide antes de cambiar nada, con lo que se mueve el indicador sin que pase nada.'], ['2', 'Durante', 'Criterios escritos antes', 'Se firma qué resultado hace pasar la puerta, antes de ver ningún dato.'], ['3', 'Después', 'El delta', 'Cuánto camino se ha recorrido desde la línea base hacia el objetivo.']]
    .map(([n, k, t, d], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${PAPER};color:${INK};padding:14px 20px 20px"><div style="display:flex;gap:12px;align-items:baseline"><span class="ser" style="font-size:44px;line-height:.9;color:${T}">${n}</span><span class="k" style="font-size:12px;letter-spacing:4px;color:${T}">${k}</span></div><div class="ser" style="font-size:29px;line-height:1.05;margin-top:4px">${t}</div><div style="font-size:16px;line-height:1.38;color:#3F423F;margin-top:6px">${d}</div></div>`).join('')}
</div>

<div class="z" style="margin-top:30px">
  <div class="k" style="color:${AV}">Qué se mide: del problema a la cuenta de resultados</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:10px">
    ${[['La restricción', 'El punto del flujo que más limita el resultado.', TV, '#fff'], ['Indicadores operativos', 'Tiempo, trabajo que vuelve, carga.', '#2A2824', '#F4F6F6'], ['Indicadores de resultado', 'Para quien recibe el servicio y para la organización.', '#2A2824', '#F4F6F6'], ['Efecto económico', 'En euros, con su horizonte y el valle previsto.', AV, INK]]
      .map(([a, b, c, fg], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${c};color:${fg};padding:12px 16px 16px;min-height:112px"><div style="display:flex;gap:10px;align-items:baseline"><span class="ser" style="font-size:34px;line-height:.9;opacity:.75">${i + 1}</span><span class="ser" style="font-size:25px;line-height:1.05">${a}</span></div><div style="font-size:15.5px;line-height:1.34;margin-top:6px;opacity:.92">${b}</div></div>`).join('')}
  </div>
  <div style="font-size:16.5px;line-height:1.42;color:${ET};margin-top:10px">Cada beneficio tiene un dueño en el negocio, y el árbol se corrige en cada puerta con lo medido.</div>
</div>

<div class="z" style="margin-top:28px;display:grid;grid-template-columns:1fr 1fr;gap:18px">
  <div class="leaf" style="background:#5B2D18;padding:16px 22px 20px"><div class="k" style="color:${AV}">Dos lecturas, no una</div><div class="ser" style="font-size:30px;line-height:1.05;margin:6px 0 8px">Resultado y palancas</div><div style="font-size:16.5px;line-height:1.4;color:${ET}">El delta del objetivo y el de las palancas se leen aparte y cada uno tiene su umbral. Si las palancas avanzan y el resultado no se mueve, no se ha servido al negocio. Si el resultado mejora y una palanca cae, lo ganado se queda sin quien lo sostenga.</div></div>
  <div class="leafb" style="background:#5B2D18;padding:16px 22px 20px"><div class="k" style="color:${AV}">Lo que no puede empeorar</div><div class="ser" style="font-size:30px;line-height:1.05;margin:6px 0 8px">Indicadores de guarda</div><div style="font-size:16.5px;line-height:1.4;color:${ET}">Tienen un suelo y no entran en la media: se cumplen o no. La calidad que acompaña a una mejora de velocidad es el ejemplo. Ninguno puede bajar de su suelo para pasar una puerta.</div></div>
</div>

<div class="z" style="margin-top:28px">
  <div class="k" style="color:${AV}">Cuánto se pide según el tamaño</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:10px">
    ${[['Puntual', 'Mejora una tarea.', 'Ocho piezas: restricción, línea base, mapa, decisión de una página, un indicador por elemento y uno del objetivo, criterio de parada, cómo se deshace y dueño.'], ['De flujo', 'Rediseña un proceso de principio a fin.', 'Se añaden el rediseño del trabajo, los casos de prueba, los supuestos, el responsable de adopción y el destino del tiempo.'], ['De sistema', 'Cambia lo que la organización ofrece o cómo se organiza.', 'Se añaden el modelo económico con valle, el gobierno completo y los módulos 1 a 22.']]
      .map(([t, d, q], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${PAPER};color:${INK};padding:12px 18px 18px;border-top:8px solid ${[AV, '#7CC090', TV][i]}"><div class="ser" style="font-size:30px;line-height:1">${t}</div><div style="font-size:15.5px;font-weight:700;line-height:1.3;margin-top:4px">${d}</div><div style="font-size:14.5px;line-height:1.36;color:#3F423F;margin-top:6px">${q}</div></div>`).join('')}
  </div>
  <div style="font-size:15px;line-height:1.4;color:${ET};margin-top:8px">Propuesta sin probar. Si lo puntual no cabe en pocas páginas, se está pidiendo de más.</div>
</div>
${foot('Cómo se mide')}
</section>`;

// ---------- Página 6: IA e innovación ----------
const N = [['Sugiere', 'La persona decide y hace todo.'], ['Propone', 'La persona revisa cada propuesta y decide.'], ['Actúa con revisión', 'Revisión por muestreo y de todo lo que se sale del patrón.'], ['Actúa e informa', 'La persona supervisa indicadores y atiende excepciones.']];
const p3 = `<section class="page dark">
${girasol({ cx: 1262, cy: 392, n: 480, c: 13, rot: 2.2, s0: 3.2, sk: .02 })}
${top(6, true)}
<div class="z" style="margin-top:42px">
  <div class="k" style="color:${AV}">6 · ¿Y dónde entra la IA?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">La IA entra<br><span style="font-style:italic;color:${AV}">por la puerta.</span></h1>
  <p style="font-size:21px;line-height:1.42;color:${MUT};width:800px;margin-top:18px">Como cualquier otra tecnología: por tarea, con criterios escritos y sin pasar de nivel sin que lo decida una puerta.</p>
</div>

<div class="z" style="margin-top:30px">
  <div class="k" style="color:${MUT}">La segunda pregunta, por tarea</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:12px;margin-top:14px">
  ${[['Elimina', '#E8DFC9', INK, 'La tarea deja de existir porque no hacía falta.', 'Antes se escribe qué sostenía el paso.', 'leafb'],
     ['Acelera', TV, '#fff', 'La misma tarea, más rápido, con la misma persona.', 'Se escribe a dónde va el tiempo que se gana.', 'leaf'],
     ['Automatiza', AV, INK, 'La tarea la hace el sistema y la persona sale del circuito.', 'La tarea se entiende bien y el criterio se puede escribir.', 'leafb'],
     ['Aumenta', GV, INK, 'La persona hace algo que antes no podía, o lo hace mejor.', 'Se dice con qué indicador se va a ver.', 'leaf']]
    .map(([t, c, fg, d, cond, sh]) => `<div class="${sh}" style="background:${c};color:${fg};padding:16px 16px 22px"><div class="ser" style="font-size:38px;line-height:1">${t}</div><div style="font-size:16px;line-height:1.36;margin-top:8px">${d}</div><div style="font-size:14.5px;line-height:1.36;margin-top:10px;padding-top:10px;border-top:1.5px solid ${fg === INK ? 'rgba(31,29,26,.35)' : 'rgba(255,255,255,.5)'}"><b style="font-weight:700">Condición.</b> ${cond}</div></div>`).join('')}
  </div>
</div>

<div class="z" style="margin-top:32px;display:grid;grid-template-columns:1.18fr 1fr;gap:44px;align-items:end">
  <div>
    <div class="k" style="color:${GV}">La escala de autonomía</div>
    <h2 style="margin:8px 0 14px;font-size:40px">Cada peldaño se sube por una puerta. Y se puede bajar.</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;align-items:end">
      ${N.map(([t, d], i) => `<div style="display:flex;flex-direction:column;justify-content:flex-end"><div style="font-size:14.5px;line-height:1.36;color:${MUT};padding:0 4px 10px">${d}</div><div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${['#3A372F', '#4A4636', '#7A6220', AV][i]};color:${i === 3 ? INK : '#F4F6F6'};height:${78 + i * 46}px;padding:10px 14px"><div class="ser" style="font-size:40px;line-height:.9">${i + 1}</div><div style="font-size:16px;font-weight:600;line-height:1.2;margin-top:6px">${t}</div></div></div>`).join('')}
    </div>
    <div style="font-size:16.5px;line-height:1.4;color:#E7EBE9;margin-top:12px">Subir de nivel no debe bajar el control. Cambia dónde se ejerce.</div>
  </div>
  <div class="leafb" style="background:#2A2824;padding:20px 26px 26px">
    <div class="k" style="color:${TV}">Agentes</div>
    <div class="ser" style="font-size:33px;line-height:1.08;margin:6px 0 10px">Antes de la ficha, una pregunta: ¿hace falta un agente o basta un flujo fijo?</div>
    ${['Una ficha de once campos por agente.', 'Un dueño con nombre, que responde.', 'Lista cerrada de acciones y condiciones de parada.', 'Un presupuesto no es una autorización.']
      .map(t => `<div style="display:flex;gap:12px;font-size:16.5px;line-height:1.36;padding:6px 0;border-top:1px solid rgba(244,246,246,.2)"><span style="color:${TV};font-weight:700">·</span><span>${t}</span></div>`).join('')}
  </div>
</div>

<div class="z" style="margin-top:40px">
  <div>
    <div class="k" style="color:${AV}">Innovar con IA</div>
    <h2 style="margin:8px 0 10px;font-size:40px">Explorar tiene su carril</h2>
    ${['Un laboratorio pequeño, con experimentos de días y el supuesto escrito antes.', 'La IA amplía, combina y critica ideas. Elige una persona, con criterios escritos.', 'Nada pasa al servicio sin entrar en la cartera y recorrer las puertas.']
      .map((t, i) => `<div style="display:flex;gap:16px;align-items:baseline;padding:9px 0;border-top:1px solid rgba(244,246,246,.22)"><span class="ser" style="font-size:32px;line-height:.9;color:${AV};flex:0 0 24px">${i + 1}</span><span style="font-size:17.5px;line-height:1.36">${t}</span></div>`).join('')}
  </div>
</div>

<div class="z" style="position:absolute;left:80px;right:80px;bottom:92px">
  ${tri()}
  <div style="display:grid;grid-template-columns:1fr 1.1fr;gap:34px;margin-top:16px;align-items:end">
    <div class="ser" style="font-size:38px;font-style:italic;line-height:1.08">Crecer a la vez vale también para el método.</div>
    <div style="font-size:16.5px;line-height:1.44;color:${MUT}"><b style="color:#F4F6F6;font-weight:700">Estado, noviembre de 2026.</b> Versión 2.1. A la fecha ningún programa ha aplicado el método completo, y lo que no está probado se dice. Eso es lo que pide la siguiente versión.</div>
  </div>
</div>
${foot('IA e innovación')}
</section>`;

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  const f = path.join(dir, '_inf.html'); fs.writeFileSync(f, `<!doctype html><html lang="es"><head><meta charset="utf-8"><style>${css}</style></head><body>${p1}${pm}${p2}${pr}${pv}${p3}</body></html>`);
  await p.goto('file://' + f); await p.waitForTimeout(900);
  const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map(s => s.scrollHeight));
  console.log('alturas', over.join(' '));
  for (let i = 0; i < 6; i++) await p.screenshot({ path: path.join(out, `infografia-metodo-${i + 1}.png`), clip: { x: 0, y: i * H, width: W, height: H }, fullPage: true });
  await p.pdf({ path: path.join(out, 'Synergos-El-metodo-en-seis-paginas.pdf'), width: W + 'px', height: H + 'px', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  fs.unlinkSync(f); await b.close(); console.log('ok');
})();
