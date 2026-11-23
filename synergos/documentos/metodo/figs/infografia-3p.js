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
const top = (n, dark) => `<div class="top z"><img src="file://${IM}${dark ? 'logo-synergos-dark.svg' : 'logo-synergos.svg'}"><span>El método en ocho páginas · versión 2.1</span><span class="pg" style="color:inherit">${n} <span style="opacity:.45">/ 8</span></span></div>`;
const TRAIL = [['Para qué', 'Para qué'], ['El itinerario', 'Itinerario'], ['Personas y conocimiento', 'Qué mirar'], ['El tronco: fases y puertas', 'Camino'], ['Los roles del método', 'Quién'], ['Cómo se mide', 'Medir'], ['IA e innovación', 'IA']];
const foot = t => { const cur = TRAIL.findIndex(x => x[0] === t);
  if (cur < 0) return `<div class="foot"><i>Crecer a la vez.</i><span>Anexo · El método se aplica a sí mismo</span></div>`;
  const crumb = (txt, state, last) => `<span style="display:inline-flex;align-items:center;gap:6px"><span style="${state === 'now' ? 'font-weight:700;color:var(--nc);border-bottom:3px solid var(--tc)' : state === 'done' ? 'opacity:.9' : 'opacity:.5'}">${txt}</span>${last ? '' : '<span style="opacity:.4">›</span>'}</span>`;
  const items = [['Inicio', 'done']].concat(TRAIL.map((x, i) => [x[1], i === cur ? 'now' : i < cur ? 'done' : 'todo'])).concat([['Impacto en el negocio', cur === TRAIL.length - 1 ? 'goal' : 'todo']]);
  const html = items.map(([txt, st], i) => st === 'goal' ? `<span style="display:inline-flex;align-items:center;gap:6px"><span style="font-weight:700;color:${AV}">${txt}</span></span>` : crumb(txt, st, i === items.length - 1)).join(' ');
  return `<div class="foot" style="--tc:${AV};--nc:${(t === TRAIL[1][0] || t === TRAIL[3][0]) ? INK : '#fff'}"><i>Crecer a la vez.</i><span style="display:flex;gap:8px;align-items:center;font-size:12.5px;letter-spacing:2px">${html}</span></div>`; };

// ---------- Página 1: para qué ----------
const STEP = (n, t, c, body, fg = '#F4F6F6') => `<div style="display:grid;grid-template-columns:170px 1fr;gap:26px;align-items:stretch"><div class="${n % 2 ? 'leaf' : 'leafb'}" style="background:${c};color:${INK};display:flex;flex-direction:column;justify-content:center;padding:22px 20px"><span class="ser" style="font-size:64px;line-height:.9">${n}</span><span class="k" style="font-size:13px;letter-spacing:3px;margin-top:8px">${t}</span></div><div style="padding:4px 0">${body}</div></div>`;
const ARR = (t) => `<div style="display:flex;align-items:center;gap:14px;margin:30px 0 30px 70px;color:${MUT};font-size:17px;letter-spacing:3px;text-transform:uppercase;font-weight:600"><span style="font-size:24px;color:${GV}">↓</span>${t}</div>`;
const p1 = `<section class="page dark">
${SUN(0.5)}
${top(1, true)}
<div class="z" style="margin-top:40px">
  <div class="k" style="color:${GV}">1 · ¿Para qué sirve este método?</div>
  <h1 style="font-size:150px;margin:12px 0 0 -6px">Crecer<br><span style="font-style:italic;color:${GV}">a la vez.</span></h1>
  <p style="font-size:24px;line-height:1.42;color:${MUT};width:600px;margin-top:18px">El destino es el resultado del negocio; el camino, que personas, conocimiento y tecnología avancen en el mismo orden.</p>
</div>

<div class="z" style="margin-top:44px">
  ${STEP(1, 'El problema', TV, `<div class="ser" style="font-size:42px;line-height:1.05">Las transformaciones se rompen</div><div style="font-size:20px;line-height:1.42;color:${MUT};margin-top:8px">Casi siempre por una de tres causas: se elige la solución antes de entender el problema, la tecnología llega antes que el cambio en la forma de trabajar, o se sustituye a quien sabía sin haberlo mirado.</div>`)}
  ${ARR('Por eso el método fija')}
  ${STEP(2, 'El objetivo', AV, `<div class="ser" style="font-size:42px;line-height:1.05">Impacto en el negocio</div><div style="font-size:20px;line-height:1.42;color:${MUT};margin-top:8px">Ingresar más, gastar menos, servir mejor o poder hacer algo que antes no se podía. Es para qué se mueve todo lo demás.</div>`)}
  ${ARR('Y lo busca moviendo tres palancas a la vez')}
  ${STEP(3, 'Las palancas', GV, `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px"><div class="leaf" style="background:${TV};color:#fff;padding:12px 16px 14px"><div class="ser" style="font-size:32px">Personas</div><div style="font-size:16.5px;line-height:1.35;margin-top:4px">Liderazgo, roles e incentivos. Interacción entre quien ejecuta el trabajo y quien enseña cómo se realiza la tarea.</div></div><div class="leafb" style="background:${GV};color:${INK};padding:12px 16px 14px"><div class="ser" style="font-size:32px">Conocimiento</div><div style="font-size:16.5px;line-height:1.35;margin-top:4px">Lo escrito, lo que nadie escribió y lo que aprende el programa.</div></div><div class="leaf" style="background:${AV};color:${INK};padding:12px 16px 14px"><div class="ser" style="font-size:32px">Tecnología</div><div style="font-size:16.5px;line-height:1.35;margin-top:4px">La IA entra cuando lo demás está listo.</div></div></div><div style="font-size:19px;line-height:1.4;color:${MUT};margin-top:10px">Ninguna crece a costa de las otras.</div>`)}
  ${ARR('Con un orden')}
  ${STEP(4, 'El orden', '#E8DFC9', `<div class="ser" style="font-size:42px;line-height:1.05">Un orden con puertas</div><div style="font-size:20px;line-height:1.42;color:${MUT};margin-top:8px">Cinco fases con una puerta al final de cada una, y los elementos que las sostienen: estrategia, gobierno, modelo económico, medición, madurez y dimensionamiento.</div>`)}
</div>
<div class="z" style="margin-top:34px;font-size:18px;line-height:1.4;color:${MUT}">En las páginas siguientes: el itinerario completo, qué se mira primero, cómo se avanza, quién interviene, cómo se sabe que funciona y dónde entra la IA.</div>
${foot('Para qué')}
</section>`;

// ---------- Página 2: el itinerario ----------
const IT = [
  ['Diagnóstico', T, '#fff', ['Se escucha a quien hace el trabajo y a sus jefes directos.', 'Se apunta en una tabla lo que nadie escribió.', 'Todavía no entra en el servicio. Se anota lo que ya se usa.', 'Se toma la foto de partida.'], 'Se sabe cuál es el atasco principal y cómo está hoy.'],
  ['Diseño', G, '#fff', ['Se rediseña el trabajo: qué hace cada uno y quién enseña el oficio.', 'Se decide qué pasa con cada cosa que se sabe.', 'Se elige tarea a tarea: eliminar, acelerar, automatizar o mejorar.', 'Se firma qué resultado se da por bueno y cuánto vale.'], 'Cinco preguntas respondidas por escrito.'],
  ['Piloto', A, INK, ['Prueban quienes hacen el trabajo, con casos reales.', 'Se comprueba que no se ha perdido nada importante.', 'Entra en pequeño y con poca autonomía.', 'Se compara con la foto de partida.'], 'Se cumple lo firmado. Si no: ajustar y repetir, o retirar.'],
  ['Escala', T, '#fff', ['Formación en el puesto y alguien que se ocupa de que se use.', 'Lo que se sabe pasa a procedimientos y a formación.', 'Se amplía por etapas. Más autonomía solo si se decide.', 'Se vigila que los resultados se mantienen al ampliar.'], 'Los resultados aguantan con más gente y más casos.'],
  ['Sostenimiento', G, '#fff', ['La operación se hace responsable. El equipo del programa se va.', 'Lo aprendido queda escrito y al día.', 'Se revisa cada año: mantener, cambiar o retirar.', 'Dos periodos seguidos sin el equipo del programa.'], 'La mejora se mantiene sola.'],
];
const TRACK = (cur, label) => `<div style="display:flex;align-items:center;gap:8px;margin-top:6px">${[1, 2, 3, 4, 5].map(i => `<span style="width:26px;height:26px;border-radius:50%;background:${i < cur ? G : i === cur ? T : '#E3E0D6'};color:${i <= cur ? '#fff' : GREY};font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center">${i}</span>${i < 5 ? `<span style="flex:0 0 14px;height:3px;background:${i < cur ? G : '#D9D6CC'}"></span>` : ''}`).join('')}<span style="font-size:14px;color:${GREY};margin-left:6px">${label}</span></div>`;
const pi = `<section class="page light">
${SUN(0.9)}
${top(2, false)}
<div class="z" style="margin-top:30px;width:880px">
  <div class="k" style="color:${T}">2 · ¿De dónde a dónde vamos?</div>
  <h1 style="font-size:70px;letter-spacing:-2px;margin-top:8px;line-height:.98">El itinerario, <span style="font-style:italic;color:${G}">de un vistazo.</span></h1>
  <div style="font-size:17px;line-height:1.4;color:${GREY};margin-top:10px;width:760px">Se lee de arriba abajo. Las fases van una detrás de otra. Dentro de cada fase, las cuatro columnas ocurren a la vez.</div>
</div>

<div class="z leaf" style="margin-top:20px;background:${INK};color:#F4F6F6;padding:14px 24px 16px;display:grid;grid-template-columns:230px 1fr;gap:24px;align-items:center">
  <div><div class="k" style="color:${AV};font-size:12.5px">Punto de partida</div><div class="ser" style="font-size:30px;line-height:1.05;margin-top:2px">Dónde estamos</div></div>
  <div style="font-size:16.5px;line-height:1.4">Un servicio con un atasco, un objetivo de negocio escrito y un directivo que responde del programa. ${EJ} Un servicio de expedientes donde los casos complejos tardan 40 días porque dependen de tres personas.</div>
</div>

<div class="z" style="margin-top:12px;display:grid;grid-template-columns:150px repeat(4,1fr);gap:6px">
  <div></div>
  ${[['Personas', T, '#fff'], ['Conocimiento', G, '#fff'], ['Tecnología', A, INK], ['Medición', INK, '#F4F6F6']].map(([t, c, fg]) => `<div style="background:${c};color:${fg};padding:7px 12px;font-size:13px;letter-spacing:3px;text-transform:uppercase;font-weight:700;text-align:center">${t}</div>`).join('')}
</div>
${IT.map(([n, c, fg, cells, gate], i) => `<div class="z" style="margin-top:6px;display:grid;grid-template-columns:150px repeat(4,1fr);gap:6px;align-items:stretch">
  <div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${c};color:${fg};padding:10px 12px;display:flex;flex-direction:column;justify-content:center"><span class="ser" style="font-size:44px;line-height:.9">${i + 1}</span><span class="ser" style="font-size:21px;line-height:1.05;margin-top:4px">${n}</span></div>
  ${cells.map(t => `<div style="background:#fff;border:1.5px solid #D9D6CC;padding:12px 14px;font-size:16.5px;line-height:1.34;min-height:116px">${t}</div>`).join('')}
</div>
<div class="z" style="margin-top:6px;display:grid;grid-template-columns:150px 1fr;gap:6px;align-items:center">
  <div style="text-align:center;font-size:22px;color:${G};line-height:1">↓</div>
  <div style="background:#ECE8DC;padding:9px 14px;font-size:16.5px;line-height:1.3;display:flex;gap:12px;align-items:baseline"><span class="k" style="font-size:12px;letter-spacing:3px;color:${c === A ? AT : c};white-space:nowrap">Puerta ${i + 1} · se decide</span><span>${gate}</span></div>
</div>`).join('')}

<div class="z leafb" style="margin-top:10px;background:${G};color:#fff;padding:14px 24px 18px;display:grid;grid-template-columns:230px 1fr;gap:24px;align-items:center">
  <div><div class="k" style="color:#E3EEE6;font-size:12.5px">Destino</div><div class="ser" style="font-size:30px;line-height:1.05;margin-top:2px">A dónde llegamos</div></div>
  <div style="font-size:16.5px;line-height:1.4">El resultado del negocio ha mejorado y se mantiene sin el equipo del programa. Lo aprendido sirve para el siguiente diagnóstico. ${EJ} Los casos complejos tardan 28 días y los resuelve más de una persona.</div>
</div>
<div class="z" style="margin-top:10px;display:grid;grid-template-columns:1fr 1.25fr;gap:10px">
  <div style="background:#fff;border:1.5px solid #D9D6CC;padding:10px 16px 12px"><div class="k" style="font-size:12px;letter-spacing:3px;color:${T}">Nivel 1 · cada cambio propuesto</div>${TRACK(5, 'Recorre las cinco fases con sus puertas')}</div>
  <div style="background:#fff;border:1.5px solid #D9D6CC;padding:10px 16px 12px"><div class="k" style="font-size:12px;letter-spacing:3px;color:${G}">Nivel 2 · el programa, con varios ámbitos a la vez</div>${TRACK(4, 'Ámbito A')}${TRACK(2, 'Ámbito B')}${TRACK(1, 'Ámbito C')}</div>
</div>
${foot('El itinerario')}
</section>`;

// ---------- Página 3: lo que nadie escribió ----------
const PG = '#A9D9B8', GD = '#173A22';
const pm = `<section class="page green">
${SUN(3.1, [AV, '#7CC090', TV], .95)}
${top(3, true)}
<div class="z" style="margin-top:42px;width:940px">
  <div class="k" style="color:${AV}">3 · ¿Qué se mira primero?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">Antes de decidir,<br><span style="font-style:italic;color:${AV}">mirar lo que nadie escribió.</span></h1>
  <p style="font-size:21px;line-height:1.42;color:#DCEBE1;width:690px;margin-top:20px">En toda organización hay cosas que solo saben una o dos personas y que no están en ningún manual. Antes de cambiar nada, se apuntan en una tabla.</p>
</div>

<div class="z leaf" style="margin-top:30px;background:${PAPER};color:${INK};padding:22px 28px 26px">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><div><span class="k" style="color:${G}">Lo primero que se hace</span><div class="ser" style="font-size:44px;line-height:1.05;margin-top:4px">El mapa de lo que nadie escribió</div></div><div style="text-align:right;width:230px">${EJ}<div style="font-size:14px;color:${GREY};line-height:1.35;margin-top:4px">Caso inventado, por perfiles y sin nombres.</div></div></div>
  <div style="display:grid;grid-template-columns:1.55fr 1fr .8fr .9fr;gap:6px;margin-top:14px;font-size:17px;line-height:1.32">
    ${['Qué se sabe', 'Quién lo sabe', 'Dónde se usa', 'Cuántos lo saben'].map(t => `<div class="k" style="font-size:12.5px;letter-spacing:3.5px;color:${G};padding:8px 12px;background:#E3EEE6">${t}</div>`).join('')}
    ${[['Qué peticiones acabarán en reclamación', 'Perfil A y perfil B', 'Al clasificar', 'Dos personas', 0], ['A quién llamar en otra unidad cuando algo se atasca', 'Perfil A', 'Excepciones', 'Una persona', 1]]
      .map(([a, b, c, d, hot]) => [a, b, c, d].map((t, j) => `<div style="padding:12px 12px;background:${hot ? (j === 3 ? T : '#F7E4DA') : '#EFEDE6'};color:${hot && j === 3 ? '#fff' : INK};font-weight:${j === 3 || j === 0 ? 600 : 400}">${t}</div>`).join('')).join('')}
  </div>
  <div style="font-size:16.5px;line-height:1.4;margin-top:12px;color:${GREY}">Una fila que dice "una persona" se ve, y con cada opción de diseño fila a fila se va respondiendo qué le pasa a ese conocimiento.</div>
</div>

<div class="z" style="margin-top:30px;display:grid;grid-template-columns:1.08fr 1fr;gap:44px">
  <div>
    <div class="k" style="color:${AV}">Cómo se hace</div>
    <h2 style="margin:8px 0 10px;font-size:40px">Cinco preguntas a quien hace el trabajo</h2>
    ${['¿Qué casos parecen iguales y no lo son? ¿Cómo los distingues?', '¿Cuándo no sigues el procedimiento y por qué?', '¿A quién llamas cuando algo se atasca? ¿Y quién te llama a ti?', '¿Qué sabes de un caso antes de leerlo entero?', '¿Qué pasaría mañana si tú no vinieras?']
      .map((t, i) => `<div style="display:flex;gap:16px;align-items:baseline;padding:8.5px 0;border-top:1px solid rgba(244,246,246,.28)"><span class="ser" style="font-size:32px;line-height:.9;color:${AV};flex:0 0 24px">${i + 1}</span><span style="font-size:18px;line-height:1.34">${t}</span></div>`).join('')}
  </div>
  <div>
    <div class="k" style="color:${AV}">Antes de aprobar un cambio</div>
    <h2 style="margin:8px 0 12px;font-size:40px">Qué pasa con cada cosa que se sabe</h2>
    ${[['Se queda en la persona', 'y la tecnología la ayuda.', '#7CC090', INK], ['Pasa al sistema', 'de forma que se pueda revisar.', AV, INK], ['Se pierde', 'y se decide sabiéndolo.', TV, '#fff']]
      .map(([a, b, c, fg], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${c};color:${fg};padding:11px 22px 14px;margin-bottom:8px"><span class="ser" style="font-size:30px;line-height:1.05">${a}</span> <span style="font-size:17px">${b}</span></div>`).join('')}
    <div style="font-size:16.5px;line-height:1.42;color:#DCEBE1;margin-top:12px;border-left:6px solid ${AV};padding-left:14px"><b style="font-weight:700;color:#fff">Una condición.</b> Antes de empezar, quien dirige el programa firma que esta tabla no se usará para evaluar a nadie ni para decidir despidos. Sin esa firma, no se hace.</div>
  </div>
</div>

<div class="z" style="margin-top:30px">
  <div class="k" style="color:${AV}">Una pregunta que casi nadie hace</div>
  <h2 style="margin:8px 0 12px;font-size:40px">Si la tarea con la que se aprendía la hace una máquina, ¿quién enseña el oficio?</h2>
  <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px">
    ${['Aprender corrigiendo', 'Tareas reservadas para formar', 'La IA como tutora', 'Tiempo reconocido para enseñar', 'Turnos para los casos difíciles']
      .map((t, i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${GD};padding:12px 14px 18px;min-height:112px"><div class="ser" style="font-size:34px;line-height:.9;color:${AV}">${i + 1}</div><div style="font-size:16.5px;font-weight:600;line-height:1.25;margin-top:6px">${t}</div></div>`).join('')}
  </div>
  <div style="font-size:15.5px;line-height:1.4;color:#CFE3D5;margin-top:8px">Son cinco formas posibles de resolverlo. Ninguna está probada todavía: se elige una al diseñar, no se aplica como una receta.</div>
</div>

${foot('Personas y conocimiento')}
</section>`;

// ---------- Página 3: el tronco ----------
const F = [
  ['Diagnóstico', T, '#fff', 'Entender dónde se pierden tiempo, calidad o dinero, y por qué.', 'Se sabe cuál es el atasco principal, se ha medido cómo está hoy y está hecha la tabla de lo que nadie escribió.'],
  ['Diseño', G, '#fff', 'Decidir qué se cambia, cómo y con qué tecnología.', 'Cada cambio propuesto ataca ese atasco y responde por escrito a cinco preguntas.'],
  ['Piloto', A, INK, 'Probar en pequeño, con gente y datos reales.', 'Cumple los criterios que se firmaron antes de empezar.'],
  ['Escala', T, '#fff', 'Extender lo que funciona.', 'Los resultados se mantienen al ampliar, y personas, conocimiento y tecnología aguantan la carga.'],
  ['Sostenimiento', G, '#fff', 'Que la mejora siga cuando el equipo del programa se vaya.', 'Alguien de la operación se hace responsable y los resultados se mantienen dos periodos seguidos.'],
];
const p2 = `<section class="page light">
${SUN(1.3, [T, G, A], .55)}
${top(4, false)}
<div class="z" style="margin-top:42px;width:900px">
  <div class="k" style="color:${T}">4 · ¿Cómo se avanza?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">Cinco fases.<br>Cada una acaba en<br><span style="font-style:italic;color:${G}">una puerta.</span></h1>
  <p style="font-size:20px;line-height:1.4;color:${GREY};width:640px;margin-top:14px">Una puerta es una decisión por escrito, con los criterios fijados de antemano.</p>
</div>

<div class="z" style="margin-top:32px;position:relative">
  <div style="position:absolute;left:55px;top:40px;bottom:40px;width:3px;background:repeating-linear-gradient(${INK} 0 9px,transparent 9px 18px);opacity:.35"></div>
  ${F.map(([n, c, fg, pq, pu], i) => `<div style="display:grid;grid-template-columns:112px 1fr 400px;gap:26px;align-items:stretch;margin-bottom:11px">
    <div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${c};color:${fg};display:flex;align-items:center;justify-content:center;position:relative;z-index:2"><span class="ser" style="font-size:70px;line-height:1">${i + 1}</span></div>
    <div style="padding:8px 0 6px;border-top:2px solid ${INK}"><div class="ser" style="font-size:44px;line-height:1">${n}</div><div style="font-size:18px;line-height:1.36;color:${GREY};margin-top:5px">${pq}</div></div>
    <div class="${i % 2 ? 'leaf' : 'leafb'}" style="background:#fff;border:1.5px solid #D9D6CC;padding:11px 18px 14px"><div class="k" style="font-size:12.5px;letter-spacing:4px;color:${c === A ? AT : c}">Puerta ${i + 1} · para pasar</div><div style="font-size:16.5px;line-height:1.34;margin-top:5px">${pu}</div></div>
  </div>`).join('')}
</div>

<div class="z" style="margin-top:12px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px">
  ${[['Pasar', G, 'Se cumplen los criterios.'], ['Ajustar y repetir', AT, 'Promete, pero está incompleto.'], ['Retirar', T, 'No funciona. Retirar es una salida legítima.']]
    .map(([t, c, d]) => `<div style="border-top:6px solid ${c};padding:9px 4px 0"><div class="ser" style="font-size:30px;line-height:1">${t}</div><div style="font-size:16.5px;line-height:1.38;color:${GREY};margin-top:6px">${d}</div></div>`).join('')}
</div>

<div class="z leaf" style="margin-top:22px;background:${INK};color:#F4F6F6;padding:22px 34px 28px;display:grid;grid-template-columns:330px 1fr;gap:38px;align-items:start">
  <div><div class="k" style="color:${AV}">Antes de aprobar un cambio</div><div class="ser" style="font-size:46px;line-height:1;margin-top:8px">Cinco preguntas, por escrito</div><div style="font-size:15.5px;line-height:1.4;color:${MUT};margin-top:10px">Se responden antes de ver ningún resultado. Se puede aprobar un cambio que pierde conocimiento, pero no sin saberlo.</div></div>
  <div>${['¿Resuelve el atasco principal, y cuánto vale resolverlo?', '¿Elimina la tarea, la acelera, la automatiza o mejora lo que hace la persona?', '¿Qué pasa con lo que sabía quien hacía ese trabajo?', '¿Quién responde si falla, y quién enseña el oficio a los nuevos?', '¿Mejoran a la vez personas, conocimiento y tecnología, o una mejora a costa de las otras?']
    .map((t, i) => `<div style="display:flex;gap:18px;align-items:baseline;padding:7px 0;${i ? 'border-top:1px solid rgba(244,246,246,.22)' : ''}"><span class="ser" style="font-size:34px;line-height:.9;color:${[TV, GV, AV][i % 3]};flex:0 0 26px">${i + 1}</span><span style="font-size:18.5px;line-height:1.3">${t}</span></div>`).join('')}</div>
</div>

<div class="z" style="margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:26px;font-size:16px;line-height:1.4">
  <div style="border-left:6px solid ${A};padding-left:16px"><b style="font-weight:700">Condición para meter tecnología.</b> Solo entra en el servicio cuando lo básico está por escrito: quién decide, qué se usa y qué sabe una sola persona.</div>
  <div style="border-left:6px solid ${G};padding-left:16px"><b style="font-weight:700">Y vuelta a empezar.</b> Lo aprendido al final sirve para el siguiente diagnóstico.</div>
</div>
${foot('El tronco: fases y puertas')}
</section>`;

// ---------- Página 4: los roles ----------
const FAM = [
  ['Quién dirige y decide', AV, INK, [['Comité de dirección', 'Fija el objetivo y cuánto riesgo se acepta'], ['Patrocinador', 'El directivo que responde del programa. Decide y firma'], ['Dirección del programa', 'Coordina el día a día del programa'], ['Comité de puertas', 'Los cuatro que intervienen en cada decisión']]],
  ['Quién opera y adopta', '#7CC090', INK, [['Responsable de la operación', 'Responde de cómo funciona después'], ['Responsable de adopción', 'Se ocupa de que la gente lo use de verdad'], ['Quien hace el trabajo', 'Se le escucha antes de decidir. Puede pedir que se pare'], ['Mando intermedio', 'Se le escucha antes. Sabe dónde está el atasco']]],
  ['Quién mide y controla', TV, '#fff', [['Responsable de medición', 'Da fe de los datos. No decide'], ['Segunda firma', 'De alguien ajeno al programa'], ['Riesgos, seguridad y legal', 'Revisan y pueden objetar desde el principio'], ['Responsable de los datos', 'Alguien del negocio, no de informática']]],
  ['Quién es oído o recibe el beneficio', '#E8DFC9', INK, [['Responsable de la mejora', 'Responde de que llegue a la cuenta de resultados'], ['Representantes de los trabajadores', 'Se les escucha si cambian condiciones de trabajo'], ['La voz del cliente', 'Alguien que lo defiende. Opina, no decide'], ['El cliente o el ciudadano', 'Se le pregunta y se mide cómo le va']]],
];
const NOP = ['Quien decide no pone también la segunda firma.', 'Quien da fe de los datos no firma la decisión.', 'Quien se ocupa de que se use no es quien instala la herramienta.', 'Quien responde de la mejora es del negocio, no del programa.', 'El responsable de los datos es del negocio, no de informática.', 'La voz del cliente opina, pero no decide.'];
const pr = `<section class="page dark">
${SUN(5.1)}
${top(5, true)}
<div class="z" style="margin-top:42px;width:900px">
  <div class="k" style="color:${GV}">5 · ¿Quién interviene?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">Quién es quién<br><span style="font-style:italic;color:${GV}">en cada decisión.</span></h1>
  <p style="font-size:21px;line-height:1.42;color:${MUT};width:780px;margin-top:20px">Una misma persona puede tener varios roles. Lo que el método no admite es que quien decide sea también quien controla.</p>
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
<div class="z" style="margin-top:16px;font-size:16px;line-height:1.42;color:${MUT}">En un programa pequeño varios papeles recaen en la misma persona, pero quien decide y quien pone la segunda firma son siempre dos personas distintas.</div>
<div class="z" style="margin-top:10px;font-size:16px;line-height:1.42;color:${MUT}">Y quien trabaja con la herramienta a diario puede parar o avisar de un fallo, por escrito, sin miedo a represalias.</div>
${foot('Los roles del método')}
</section>`;

// ---------- Página 5: cómo se mide ----------
const ED = '#451A0B', EL = '#F0C3A4', ET = '#EBD3C4';
const pv = `<section class="page earth">
${SUN(4.0, [AV, '#7CC090', TV], .95)}
${top(6, true)}
<div class="z" style="margin-top:42px;width:900px">
  <div class="k" style="color:${AV}">6 · ¿Cómo se sabe que funciona?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">Se mide antes,<br><span style="font-style:italic;color:${AV}">durante y después.</span></h1>
  <p style="font-size:21px;line-height:1.42;color:${ET};width:800px;margin-top:20px">No vale la impresión de la gente ni lo que declara el proveedor. Vale lo que se midió contra lo que había antes.</p>
</div>

<div class="z" style="margin-top:34px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px">
  ${[['1', 'Antes', 'La foto de partida', 'Se mide cómo está hoy, antes de cambiar nada, y cuánto varía por sí solo.'], ['2', 'Durante', 'Criterios escritos antes', 'Se firma qué resultado se da por bueno, antes de ver ningún dato.'], ['3', 'Después', 'El avance', 'Cuánto se ha recorrido desde la foto de partida hasta el objetivo.']]
    .map(([n, k, t, d], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${PAPER};color:${INK};padding:14px 20px 20px"><div style="display:flex;gap:12px;align-items:baseline"><span class="ser" style="font-size:44px;line-height:.9;color:${T}">${n}</span><span class="k" style="font-size:12px;letter-spacing:4px;color:${T}">${k}</span></div><div class="ser" style="font-size:29px;line-height:1.05;margin-top:4px">${t}</div><div style="font-size:16px;line-height:1.38;color:#3F423F;margin-top:6px">${d}</div></div>`).join('')}
</div>

<div class="z" style="margin-top:30px">
  <div class="k" style="color:${AV}">Qué se mide: del problema a la cuenta de resultados</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:10px">
    ${[['El atasco', 'El punto que más frena el resultado.', TV, '#fff'], ['El día a día', 'Tiempos, errores que obligan a repetir, carga de trabajo.', '#2A2824', '#F4F6F6'], ['El resultado', 'Para el cliente y para la organización.', '#2A2824', '#F4F6F6'], ['El dinero', 'En euros, con su plazo y contando con que al principio se empeora.', AV, INK]]
      .map(([a, b, c, fg], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${c};color:${fg};padding:12px 16px 16px;min-height:112px"><div style="display:flex;gap:10px;align-items:baseline"><span class="ser" style="font-size:34px;line-height:.9;opacity:.75">${i + 1}</span><span class="ser" style="font-size:25px;line-height:1.05">${a}</span></div><div style="font-size:15.5px;line-height:1.34;margin-top:6px;opacity:.92">${b}</div></div>`).join('')}
  </div>
  <div style="font-size:16.5px;line-height:1.42;color:${ET};margin-top:10px">Cada mejora tiene un responsable en el negocio, y la cuenta se corrige en cada decisión con lo medido.</div>
  <div style="background:#5B2D18;padding:10px 18px 12px;margin-top:10px;font-size:15.5px;line-height:1.4;color:${ET}">${EJ} <b style="color:#fff">Expedientes complejos:</b> el atasco son tres personas de las que todo depende; cada día de espera genera reclamaciones y repetición de trabajo; el efecto previsto es de 80.000 a 150.000 euros al año, tras unos meses en los que se empeora antes de mejorar.</div>
</div>

<div class="z" style="margin-top:28px;display:grid;grid-template-columns:1fr 1fr;gap:18px">
  <div class="leaf" style="background:#5B2D18;padding:16px 22px 20px"><div class="k" style="color:${AV}">Dos lecturas, no una</div><div class="ser" style="font-size:30px;line-height:1.05;margin:6px 0 8px">Resultado y palancas</div><div style="font-size:16.5px;line-height:1.4;color:${ET}">El avance del resultado y el de las tres palancas se miran por separado. Si las palancas mejoran y el resultado no se mueve, no se ha servido al negocio. Si el resultado mejora y una palanca empeora, lo ganado no se va a sostener.</div></div>
  <div class="leafb" style="background:#5B2D18;padding:16px 22px 20px"><div class="k" style="color:${AV}">Lo que no puede empeorar</div><div class="ser" style="font-size:30px;line-height:1.05;margin:6px 0 8px">Los límites</div><div style="font-size:16.5px;line-height:1.4;color:${ET}">Hay cosas que no pueden empeorar aunque todo lo demás mejore, como la calidad cuando se gana velocidad. Si una baja de su límite, no se sigue adelante.</div></div>
</div>

<div class="z" style="margin-top:28px">
  <div class="k" style="color:${AV}">Cuánto se pide según el tamaño</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:10px">
    ${[['Puntual', 'Mejora una tarea.', 'Lo mínimo: el atasco, la foto de partida, la tabla de lo que nadie escribió, la decisión en una página, un indicador por elemento y uno por objetivo, cuándo se para, cómo se deshace y un responsable.'], ['De flujo', 'Rediseña un proceso de principio a fin.', 'Se añaden el rediseño del trabajo, las pruebas con casos reales, quién se ocupa de que se use y a qué se dedica el tiempo ganado.'], ['De sistema', 'Cambia lo que la organización ofrece o cómo se organiza.', 'Se añaden las cuentas completas, el comité de decisiones y todo el detalle del método.']]
      .map(([t, d, q], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${PAPER};color:${INK};padding:12px 18px 18px;border-top:8px solid ${[AV, '#7CC090', TV][i]}"><div class="ser" style="font-size:30px;line-height:1">${t}</div><div style="font-size:15.5px;font-weight:700;line-height:1.3;margin-top:4px">${d}</div><div style="font-size:14.5px;line-height:1.36;color:#3F423F;margin-top:6px">${q}</div></div>`).join('')}
  </div>
  <div style="font-size:15px;line-height:1.4;color:${ET};margin-top:8px">Reparto todavía sin probar. Si un cambio pequeño no cabe en pocas páginas, se está pidiendo de más.</div>
</div>
${foot('Cómo se mide')}
</section>`;

// ---------- Página 6: IA e innovación ----------
const N = [['Sugiere', 'La persona decide y hace todo.'], ['Propone', 'La persona revisa cada propuesta y decide.'], ['Actúa con revisión', 'La persona revisa una muestra y todo lo raro.'], ['Actúa e informa', 'La persona vigila los resultados y atiende las excepciones.']];
const p3 = `<section class="page dark">
${SUN(2.2)}
${top(7, true)}
<div class="z" style="margin-top:42px">
  <div class="k" style="color:${AV}">7 · ¿Y dónde entra la IA?</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">La IA entra<br><span style="font-style:italic;color:${AV}">por la puerta.</span></h1>
  <p style="font-size:21px;line-height:1.42;color:${MUT};width:800px;margin-top:18px">Como cualquier otra tecnología: tarea a tarea, con criterios escritos y sin darle más autonomía sin decidirlo antes.</p>
</div>

<div class="z" style="margin-top:30px">
  <div class="k" style="color:${MUT}">Para cada tarea, cuatro opciones</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:12px;margin-top:14px">
  ${[['Elimina', '#E8DFC9', INK, 'La tarea deja de existir porque no hacía falta.', 'Antes se comprueba para qué servía.', 'leafb'],
     ['Acelera', TV, '#fff', 'La misma tarea, más rápido, con la misma persona.', 'Se escribe a dónde va el tiempo que se gana.', 'leaf'],
     ['Automatiza', AV, INK, 'La tarea la hace el sistema, sin la persona.', 'La tarea se entiende bien y las reglas se pueden escribir.', 'leafb'],
     ['Aumenta', GV, INK, 'La persona hace algo que antes no podía, o lo hace mejor.', 'Se dice cómo se va a comprobar.', 'leaf']]
    .map(([t, c, fg, d, cond, sh]) => `<div class="${sh}" style="background:${c};color:${fg};padding:16px 16px 22px"><div class="ser" style="font-size:38px;line-height:1">${t}</div><div style="font-size:16px;line-height:1.36;margin-top:8px">${d}</div><div style="font-size:14.5px;line-height:1.36;margin-top:10px;padding-top:10px;border-top:1.5px solid ${fg === INK ? 'rgba(31,29,26,.35)' : 'rgba(255,255,255,.5)'}"><b style="font-weight:700">Condición.</b> ${cond}</div></div>`).join('')}
  </div>
</div>

<div class="z" style="margin-top:32px;display:grid;grid-template-columns:1.18fr 1fr;gap:44px;align-items:end">
  <div>
    <div class="k" style="color:${GV}">Cuánta autonomía se le da</div>
    <h2 style="margin:8px 0 14px;font-size:40px">Cada escalón se sube con una decisión. Y se puede bajar.</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;align-items:end">
      ${N.map(([t, d], i) => `<div style="display:flex;flex-direction:column;justify-content:flex-end"><div style="font-size:14.5px;line-height:1.36;color:${MUT};padding:0 4px 10px">${d}</div><div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:${['#3A372F', '#4A4636', '#7A6220', AV][i]};color:${i === 3 ? INK : '#F4F6F6'};height:${78 + i * 46}px;padding:10px 14px"><div class="ser" style="font-size:40px;line-height:.9">${i + 1}</div><div style="font-size:16px;font-weight:600;line-height:1.2;margin-top:6px">${t}</div></div></div>`).join('')}
    </div>
    <div style="font-size:16.5px;line-height:1.4;color:#E7EBE9;margin-top:12px">Más autonomía no significa menos control. Cambia dónde se ejerce.</div>
  </div>
  <div class="leafb" style="background:#2A2824;padding:20px 26px 26px">
    <div class="k" style="color:${TV}">Agentes</div>
    <div class="ser" style="font-size:33px;line-height:1.08;margin:6px 0 10px">¿Hace falta un agente, o basta un proceso fijo con IA dentro?</div>
    ${['Cada agente tiene su ficha: qué hace y qué no.', 'Un responsable con nombre y apellidos.', 'Una lista cerrada de lo que puede hacer, y cómo se para.', 'Tener presupuesto no es tener permiso.']
      .map(t => `<div style="display:flex;gap:12px;font-size:16.5px;line-height:1.36;padding:6px 0;border-top:1px solid rgba(244,246,246,.2)"><span style="color:${TV};font-weight:700">·</span><span>${t}</span></div>`).join('')}
  </div>
</div>

<div class="z" style="margin-top:40px">
  <div>
    <div class="k" style="color:${AV}">Innovar con IA</div>
    <h2 style="margin:8px 0 10px;font-size:40px">Probar cosas nuevas sin tocar el servicio</h2>
    ${['Un espacio de pruebas pequeño, con experimentos de días y lo que se quiere comprobar escrito antes.', 'La IA amplía, combina y critica ideas. Elige una persona, con criterios escritos.', 'Nada pasa al servicio real sin recorrer las cinco fases.']
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

// ---------- Página 8: ahora ----------
const CAJA = (t, c, fg, extra = '') => `<div style="background:${c};color:${fg};padding:10px 10px;font-size:17px;line-height:1.25;font-weight:600;text-align:center;display:flex;align-items:center;justify-content:center;min-height:84px;${extra}">${t}</div>`;
const EMP = [
  ['Banco grande', ['El mapa de lo que nadie escribió, la decisión en una página y eliminar antes de acelerar.', 'Enlazar con la validación de modelos y los proveedores críticos.']],
  ['Pyme industrial', ['El atasco, la foto de partida y cinco preguntas en una página.', 'Versión corta, ejemplos de taller y qué hacer sin finanzas ni segunda firma.']],
  ['Hospital público', ['El uso informal de la IA, el mapa y poder parar.', 'Seguridad del paciente, datos de salud y quién decide de verdad.']],
  ['Distribución y comercio', ['Las cuatro opciones por tarea y los límites que no pueden empeorar.', 'Calendario de campaña, tiendas de control y rotación alta.']],
  ['Software en crecimiento', ['El diagnóstico, la decisión en una página y poder parar.', 'Una versión de una página. Sobran comité y escala de madurez.']],
  ['Servicios profesionales', ['El mapa, la foto de partida y quién enseña el oficio.', 'Cómo encaja con la facturación por horas y qué hace el júnior.']],
];
const pe = `<section class="page dark">
${SUN(5.6)}
${top(8, true)}
<div class="z" style="margin-top:34px;width:860px">
  <div class="k" style="color:${GV}">8 · ¿Y qué hacemos ahora?</div>
  <h1 style="font-size:72px;letter-spacing:-2px;margin-top:8px;line-height:.98">Ahora el método <span style="font-style:italic;color:${GV}">se aplica a sí mismo.</span></h1>
  <p style="font-size:19px;line-height:1.4;color:${MUT};width:760px;margin-top:12px">Es el mismo itinerario, un nivel más arriba. Primero se escucha, luego se decide y después se prueba en un programa real.</p>
</div>

<div class="z" style="margin-top:28px">
  <div class="k" style="color:${AV}">Dos niveles, el mismo recorrido</div>
  <div style="display:grid;grid-template-columns:120px repeat(5,1fr);gap:6px;margin-top:10px;align-items:stretch">
    <div style="font-size:14px;line-height:1.3;color:${MUT};align-self:center">Nivel 1<br><b style="color:#F4F6F6">En una empresa</b></div>
    ${CAJA('Diagnóstico', T, '#fff')}${CAJA('Diseño', G, '#fff')}${CAJA('Piloto', A, INK)}${CAJA('Escala', T, '#fff')}${CAJA('Sostenimiento', G, '#fff')}
    <div style="font-size:14px;line-height:1.3;color:${MUT};align-self:center">Nivel 2<br><b style="color:#F4F6F6">En el método</b></div>
    ${CAJA('Dos revisiones: cuatro roles y seis empresas', '#2A2824', '#F4F6F6', 'border:2px solid ' + GV)}${CAJA('Decisión de Alejandro y versión 2.2', '#2A2824', '#F4F6F6', 'border:2px dashed ' + AV)}${CAJA('Primer programa real', '#2A2824', '#F4F6F6', 'border:2px dashed ' + MUT)}${CAJA('Aplicarlo en más empresas', '#2A2824', '#F4F6F6', 'border:2px dashed ' + MUT)}${CAJA('Versión 3.0', '#2A2824', '#F4F6F6', 'border:2px dashed ' + MUT)}
  </div>
  <div style="display:grid;grid-template-columns:120px repeat(5,1fr);gap:6px;margin-top:6px"><div></div><div style="grid-column:2 / span 1;text-align:center;font-size:13px;color:${GV};font-weight:700;letter-spacing:2px;text-transform:uppercase">Hecho</div><div style="text-align:center;font-size:13px;color:${AV};font-weight:700;letter-spacing:2px;text-transform:uppercase">Estamos aquí</div><div style="grid-column:4 / span 3;text-align:left;font-size:13px;color:${MUT};letter-spacing:2px;text-transform:uppercase">Falta</div></div>
</div>

<div class="z" style="margin-top:30px">
  <div class="k" style="color:${AV}">Seis empresas lo han evaluado ${EJ}</div>
  <div style="font-size:16px;color:${MUT};margin-top:4px">Perfiles inventados: son lecturas plausibles, no clientes reales. Ninguna lo adoptaría entero.</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:10px">
    ${EMP.map(([n, [q, f]], i) => `<div class="${i % 2 ? 'leafb' : 'leaf'}" style="background:#2A2824;padding:14px 18px 18px"><div class="ser" style="font-size:29px;line-height:1.05">${n}</div><div style="font-size:16px;line-height:1.38;margin-top:8px"><b style="color:${GV}">Se quedaría con</b> ${q}</div><div style="font-size:16px;line-height:1.38;margin-top:8px"><b style="color:${AV}">Le falta</b> ${f}</div></div>`).join('')}
  </div>
</div>

<div class="z" style="margin-top:26px;display:grid;grid-template-columns:1fr 1fr;gap:16px">
  <div class="leaf" style="border:2px solid rgba(244,246,246,.4);padding:16px 22px 20px"><div class="k" style="color:${GV}">Lo que coincide</div>
    ${['Las seis se quedan con la decisión escrita en una página, con criterios fijados antes.', 'Cinco de seis, con el mapa de lo que nadie escribió y con poder parar y deshacer.', 'Tres piden una versión de una página con un orden de magnitud de esfuerzo.'].map((t, i) => `<div style="display:flex;gap:10px;align-items:baseline;font-size:17px;line-height:1.38;margin-top:8px"><span class="ser" style="font-size:28px;line-height:.9;color:${[TV, GV, AV][i]}">${i + 1}</span><span>${t}</span></div>`).join('')}</div>
  <div class="leafb" style="border:2px solid rgba(244,246,246,.4);padding:16px 22px 20px"><div class="k" style="color:${AV}">Lo que viene</div>
    ${['Decidir qué entra: las propuestas de las dos rondas.', 'Escribir la versión de una página, con ejemplos por sector.', 'Probarla en un primer programa real.'].map((t, i) => `<div style="display:flex;gap:10px;align-items:baseline;font-size:17px;line-height:1.38;margin-top:8px"><span class="ser" style="font-size:28px;line-height:.9;color:${[TV, GV, AV][i]}">${i + 1}</span><span>${t}</span></div>`).join('')}</div>
</div>
${foot('Ahora')}
</section>`;

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  const f = path.join(dir, '_inf.html'); fs.writeFileSync(f, `<!doctype html><html lang="es"><head><meta charset="utf-8"><style>${css}</style></head><body>${p1}${pi}${pm}${p2}${pr}${pv}${p3}${pe}</body></html>`);
  await p.goto('file://' + f); await p.waitForTimeout(900);
  const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map(s => s.scrollHeight));
  console.log('alturas', over.join(' '));
  for (let i = 0; i < 8; i++) await p.screenshot({ path: path.join(out, `infografia-metodo-${i + 1}.png`), clip: { x: 0, y: i * H, width: W, height: H }, fullPage: true });
  await p.pdf({ path: path.join(out, 'Synergos-El-metodo-en-ocho-paginas.pdf'), width: W + 'px', height: H + 'px', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  fs.unlinkSync(f); await b.close(); console.log('ok');
})();
