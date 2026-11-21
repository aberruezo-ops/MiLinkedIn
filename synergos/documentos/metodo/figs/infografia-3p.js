// Infografía del método en tres páginas (A4). NODE_PATH=$(npm root -g) node figs/infografia-3p.js
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
.dark{background:${INK};color:#F4F6F6}.light{background:${PAPER};color:${INK}}
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
const top = (n, dark) => `<div class="top z"><img src="file://${IM}${dark ? 'logo-synergos-dark.svg' : 'logo-synergos.svg'}"><span>El método en tres páginas · versión 2.0</span><span class="pg" style="color:inherit">${n} <span style="opacity:.45">/ 3</span></span></div>`;
const foot = t => `<div class="foot"><i>Crecer a la vez.</i><span>${t}</span></div>`;

// ---------- Página 1: por qué y con qué ----------
const p1 = `<section class="page dark">
${girasol({ cx: 1075, cy: 492, n: 800, c: 13, rot: .5, s0: 3.4, sk: .02 })}
${top(1, true)}
<div class="z" style="margin-top:52px">
  <div class="k" style="color:${GV}">Un método para dirigir transformaciones</div>
  <h1 style="font-size:188px;margin:14px 0 0 -8px">Crecer<br><span style="font-style:italic;color:${GV}">a la vez.</span></h1>
  <p style="font-size:27px;line-height:1.45;color:${MUT};width:540px;margin-top:24px">Personas, conocimiento y tecnología avanzan en el mismo orden. Ninguno crece a costa de los otros.</p>
</div>

<div class="z" style="margin-top:44px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">
  ${[['Personas', TV, '#fff', 'Liderazgo, roles e incentivos, interacción con quien hace el trabajo y quién enseña lo que la tarea enseñaba.', 'leaf'],
     ['Conocimiento', GV, INK, 'Lo que está escrito, lo que nadie escribió y lo que aprende el propio programa.', 'leafb'],
     ['Tecnología', AV, INK, 'La capacidad de gobernar y usar tecnología. La IA entra como acelerador, cuando lo demás está listo.', 'leaf']]
    .map(([t, c, fg, d, sh]) => `<div class="${sh}" style="background:${c};color:${fg};padding:22px 26px 28px;min-height:196px">
      <div class="k" style="opacity:.8">Elemento</div><div class="ser" style="font-size:46px;line-height:1.05;margin:4px 0 10px">${t}</div><div style="font-size:17.5px;line-height:1.4">${d}</div></div>`).join('')}
</div>
<div class="z leafb" style="margin-top:16px;border:2px solid rgba(244,246,246,.45);padding:16px 26px 20px;display:flex;gap:34px;align-items:center;background:rgba(31,29,26,.72)">
  <div style="flex:0 0 250px"><div class="k" style="color:${MUT}">El cuarto componente</div><div class="ser" style="font-size:46px;line-height:1.05;margin-top:4px">El orden</div></div>
  <div style="font-size:19px;line-height:1.45;color:#E7EBE9">Cinco fases con una puerta al final de cada una, y lo que las sostiene: estrategia, gobierno, modelo económico, medición, madurez y dimensionamiento.</div>
</div>

<div class="z" style="margin-top:38px;display:grid;grid-template-columns:1.02fr 1fr;gap:54px">
  <div>
    <div class="k" style="color:${TV}">Por qué se rompen</div>
    <h2 style="margin:8px 0 12px">Tres causas que se repiten</h2>
    ${['Se elige la solución antes de entender el problema.', 'La tecnología llega antes que el cambio en la forma de trabajar.', 'Se sustituye a quien sabía sin haberlo mirado.']
      .map((t, i) => `<div style="display:flex;gap:18px;align-items:flex-start;padding:11px 0;border-top:1px solid rgba(244,246,246,.22)"><span class="ser" style="font-size:40px;line-height:.9;color:${[TV, GV, AV][i]};flex:0 0 34px">${i + 1}</span><span style="font-size:19.5px;line-height:1.36">${t}</span></div>`).join('')}
    <div class="leaf" style="margin-top:14px;background:#2A2824;padding:18px 24px 22px">
      <div class="ser" style="font-size:38px;font-style:italic;line-height:1.05">«Eso lo sabe Marta.»</div>
      <div style="font-size:16.5px;line-height:1.42;color:${MUT};margin-top:8px">La frase que se oye en casi todas las organizaciones. Marta no aparece en el organigrama con ese papel ni en ningún plan de proyecto.</div>
    </div>
  </div>
  <div>
    <div class="k" style="color:${AV}">Las reglas de fondo</div>
    <h2 style="margin:8px 0 12px">Seis principios</h2>
    ${['Diagnóstico antes que solución', 'Elemento antes que acelerador', 'Pocas cosas a la vez', 'Puertas con criterios fijados antes', 'Nada nuevo encima de lo no mirado', 'El método se supervisa a sí mismo']
      .map((t, i) => `<div style="display:flex;gap:16px;align-items:baseline;padding:8.5px 0;border-top:1px solid rgba(244,246,246,.22)"><span style="font-weight:700;font-size:15px;letter-spacing:2px;color:${[TV, GV, AV][i % 3]};flex:0 0 28px">0${i + 1}</span><span class="ser" style="font-size:27px;line-height:1.1">${t}</span></div>`).join('')}
    <div style="margin-top:16px;display:flex;gap:20px;align-items:center">
      <div class="ser" style="font-size:66px;line-height:.9;color:${AV}">137,5°</div>
      <div style="font-size:17px;line-height:1.42;color:${MUT}">El ángulo con que el girasol coloca cada semilla nueva respecto a la anterior. Nada tapa a nada.</div>
    </div>
  </div>
</div>
${foot('Por qué y con qué')}
</section>`;

// ---------- Página 2: el tronco ----------
const F = [
  ['Diagnóstico', T, '#fff', 'Entender dónde se pierden tiempo, calidad o dinero, y por qué.', 'Restricción nombrada, línea base medida y mapa de lo que nadie escribió.'],
  ['Diseño', G, '#fff', 'Decidir qué se cambia, cómo y con qué aceleradores.', 'Cada iniciativa ataca la restricción y responde por escrito a las cinco preguntas.'],
  ['Piloto', A, INK, 'Probar en pequeño, con gente y datos reales.', 'Cumple los criterios que se firmaron antes de empezar.'],
  ['Escala', T, '#fff', 'Extender lo que funciona.', 'Los indicadores aguantan al ampliar y los tres elementos aguantan la carga.'],
  ['Sostenimiento', G, '#fff', 'Que la mejora siga cuando el equipo del programa se vaya.', 'El dueño acepta la responsabilidad y los indicadores aguantan dos periodos de medición.'],
];
const p2 = `<section class="page light">
${girasol({ cx: 1262, cy: 420, n: 480, c: 13, rot: 1.3, s0: 3.2, sk: .02, cols: [T, G, A], op: .55 })}
${top(2, false)}
<div class="z" style="margin-top:42px;width:900px">
  <div class="k" style="color:${T}">El tronco</div>
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
  <div>${['¿Ataca la restricción?', '¿Acelera, automatiza o aumenta?', '¿Qué le pasa a cada fila del mapa de lo que nadie escribió?', '¿Quién responde de los errores, y quién enseña lo que la tarea enseñaba?', '¿Hace crecer a la vez a los tres elementos, o abarata uno a costa de los otros?']
    .map((t, i) => `<div style="display:flex;gap:18px;align-items:baseline;padding:7px 0;${i ? 'border-top:1px solid rgba(244,246,246,.22)' : ''}"><span class="ser" style="font-size:34px;line-height:.9;color:${[TV, GV, AV][i % 3]};flex:0 0 26px">${i + 1}</span><span style="font-size:18.5px;line-height:1.3">${t}</span></div>`).join('')}</div>
</div>

<div class="z" style="margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:26px;font-size:16px;line-height:1.4">
  <div style="border-left:6px solid ${A};padding-left:16px"><b style="font-weight:700">Regla de entrada.</b> Un acelerador entra en el servicio solo si personas, conocimiento, tecnología y gobierno están en el nivel 2 de madurez: repetible.</div>
  <div style="border-left:6px solid ${G};padding-left:16px"><b style="font-weight:700">El tronco se cierra.</b> Lo aprendido en el sostenimiento alimenta el diagnóstico del siguiente ciclo.</div>
</div>
${foot('El tronco: fases y puertas')}
</section>`;

// ---------- Página 3: IA e innovación ----------
const N = [['Sugiere', 'La persona decide y hace todo.'], ['Propone', 'La persona revisa cada propuesta y decide.'], ['Actúa con revisión', 'Revisión por muestreo y de todo lo que se sale del patrón.'], ['Actúa e informa', 'La persona supervisa indicadores y atiende excepciones.']];
const p3 = `<section class="page dark">
${girasol({ cx: 1262, cy: 392, n: 480, c: 13, rot: 2.2, s0: 3.2, sk: .02 })}
${top(3, true)}
<div class="z" style="margin-top:42px">
  <div class="k" style="color:${AV}">IA e innovación</div>
  <h1 style="font-size:94px;letter-spacing:-2px;margin-top:10px;line-height:.98">La IA entra<br><span style="font-style:italic;color:${AV}">por la puerta.</span></h1>
</div>

<div class="z" style="margin-top:30px">
  <div class="k" style="color:${MUT}">La segunda pregunta, por tarea</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-top:14px">
  ${[['Acelera', TV, '#fff', 'La misma tarea, más rápido, con la misma persona.', 'Se escribe a dónde va el tiempo que se gana.', 'leaf'],
     ['Automatiza', AV, INK, 'La tarea la hace el sistema y la persona sale del circuito.', 'La tarea se entiende bien y el criterio se puede escribir.', 'leafb'],
     ['Aumenta', GV, INK, 'La persona hace algo que antes no podía, o lo hace mejor.', 'Se dice con qué indicador se va a ver.', 'leaf']]
    .map(([t, c, fg, d, cond, sh]) => `<div class="${sh}" style="background:${c};color:${fg};padding:18px 24px 26px"><div class="ser" style="font-size:46px;line-height:1">${t}</div><div style="font-size:17px;line-height:1.38;margin-top:8px">${d}</div><div style="font-size:15.5px;line-height:1.38;margin-top:12px;padding-top:10px;border-top:1.5px solid ${fg === INK ? 'rgba(31,29,26,.35)' : 'rgba(255,255,255,.5)'}"><b style="font-weight:700">Condición.</b> ${cond}</div></div>`).join('')}
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

<div class="z" style="margin-top:40px;display:grid;grid-template-columns:1fr 1fr;gap:44px">
  <div>
    <div class="k" style="color:${AV}">Innovar con IA</div>
    <h2 style="margin:8px 0 10px;font-size:40px">Explorar tiene su carril</h2>
    ${['Un laboratorio pequeño, con experimentos de días y el supuesto escrito antes.', 'La IA amplía, combina y critica ideas. Elige una persona, con criterios escritos.', 'Nada pasa al servicio sin entrar en la cartera y recorrer las puertas.']
      .map((t, i) => `<div style="display:flex;gap:16px;align-items:baseline;padding:9px 0;border-top:1px solid rgba(244,246,246,.22)"><span class="ser" style="font-size:32px;line-height:.9;color:${AV};flex:0 0 24px">${i + 1}</span><span style="font-size:17.5px;line-height:1.36">${t}</span></div>`).join('')}
  </div>
  <div>
    <div class="k" style="color:${GV}">Medir</div>
    <h2 style="margin:8px 0 10px;font-size:40px">La percepción no es medida</h2>
    ${['Línea base antes de cambiar nada.', 'Indicadores de avance, con objetivo, e indicadores de guarda, con suelo.', 'El resultado se lee por nivel de pericia y no solo por la media.']
      .map((t, i) => `<div style="display:flex;gap:16px;align-items:baseline;padding:9px 0;border-top:1px solid rgba(244,246,246,.22)"><span class="ser" style="font-size:32px;line-height:.9;color:${GV};flex:0 0 24px">${i + 1}</span><span style="font-size:17.5px;line-height:1.36">${t}</span></div>`).join('')}
  </div>
</div>

<div class="z" style="position:absolute;left:80px;right:80px;bottom:92px">
  ${tri()}
  <div style="display:grid;grid-template-columns:1fr 1.1fr;gap:34px;margin-top:16px;align-items:end">
    <div class="ser" style="font-size:38px;font-style:italic;line-height:1.08">Crecer a la vez vale también para el método.</div>
    <div style="font-size:16.5px;line-height:1.44;color:${MUT}"><b style="color:#F4F6F6;font-weight:700">Estado, noviembre de 2026.</b> Versión 2.0. A la fecha ningún programa ha aplicado el método completo, y lo que no está probado se dice. Eso es lo que pide la siguiente versión.</div>
  </div>
</div>
${foot('IA e innovación')}
</section>`;

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  const f = path.join(dir, '_inf.html'); fs.writeFileSync(f, `<!doctype html><html lang="es"><head><meta charset="utf-8"><style>${css}</style></head><body>${p1}${p2}${p3}</body></html>`);
  await p.goto('file://' + f); await p.waitForTimeout(900);
  const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map(s => s.scrollHeight));
  console.log('alturas', over.join(' '));
  for (let i = 0; i < 3; i++) await p.screenshot({ path: path.join(out, `infografia-metodo-${i + 1}.png`), clip: { x: 0, y: i * H, width: W, height: H }, fullPage: true });
  await p.pdf({ path: path.join(out, 'Synergos-El-metodo-en-tres-paginas.pdf'), width: W + 'px', height: H + 'px', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  fs.unlinkSync(f); await b.close(); console.log('ok');
})();
