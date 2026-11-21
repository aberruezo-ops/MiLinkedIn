// Genera las infografías del documento del método (PNG a doble densidad) a partir de HTML.
// Uso: NODE_PATH=$(npm root -g) node figs/infografias.js
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const dir = __dirname, out = path.join(dir, '..');
const INK = '#1F1D1A', GREEN = '#2C6D3F', LIGHT = '#7CC090', TERRA = '#B5512A', ALBERO = '#C89A2A', ALBT = '#8A6508', GREY = '#56606A', PALE = '#F4F6F6', LINE = '#D7DCDC';
const css = `*{box-sizing:border-box;margin:0;padding:0}body{width:1600px;background:#fff;font-family:'Public Sans',sans-serif;color:${INK}}
#f{width:1600px;background:#FFFFFF;padding:54px 60px 50px;position:relative}
.mark{position:absolute;right:60px;top:50px;height:50px}
h1{font-family:'EB Garamond',serif;font-weight:normal;font-size:60px;line-height:1.05;margin-bottom:10px;max-width:1150px}
.sub{font-size:22px;color:${GREY};margin-bottom:36px;line-height:1.35}
.row{display:flex;gap:22px;align-items:stretch}.col{display:flex;flex-direction:column;gap:18px}
.card{background:#EAF2EC;border:0;padding:24px 26px 28px;flex:1;border-radius:10px 0 46px 0}
.card b{font-family:'EB Garamond',serif;font-weight:normal;font-size:36px;display:block;line-height:1.15;margin-bottom:8px}
.card span{font-size:19px;line-height:1.38;color:${GREY};display:block}
.num{font-family:'EB Garamond',serif;font-size:62px;line-height:1;color:${GREEN};display:block;margin-bottom:6px}
.k{font-size:16px;letter-spacing:2px;text-transform:uppercase;color:${GREEN};display:block;margin-bottom:8px}
.arrow{align-self:center;font-size:38px;color:${GREEN};flex:0 0 auto}
.pie{margin-top:30px;font-size:19px;color:${GREY};line-height:1.4;border-top:2px solid ${LINE};padding-top:18px}
.pie b{color:${INK};font-weight:normal;font-family:'EB Garamond',serif;font-size:22px}
.chip{background:#F4F6F6;border:0;padding:16px 26px 16px 20px;font-size:20px;line-height:1.3;border-radius:0 26px 0 10px}
.t{background:#F8E9E1}.t .num,.t .k{color:${TERRA}}.a{background:#F8EDD0}.a .num,.a .k{color:${ALBT}}.i{background:#ECEEEE}.i .num,.i .k{color:${INK}}
.dark{background:${INK};color:#fff;border-radius:0 46px 0 10px}.dark span{color:#D7DCDC}.dark .k{color:#B9C0BE}
`;
const LOGO = 'file://' + path.join(dir, '../../../imagenes/logo-synergos.svg');
const page = (h1, sub, body, pie = '') => `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div id="f"><img class="mark" src="${LOGO}"><h1>${h1}</h1><div class="sub">${sub}</div>${body}${pie ? `<div class="pie">${pie}</div>` : ''}</div></body></html>`;
const card = (cls, k, b, s, num = '') => `<div class="card ${cls}">${num ? `<span class="num">${num}</span>` : ''}${k ? `<span class="k">${k}</span>` : ''}<b>${b}</b><span>${s}</span></div>`;
const ar = '<div class="arrow">→</div>';

const figs = {
  'fig-estructura.png': page('Qué recorre el tronco', 'Un programa no pasa entero por las fases. Las recorre cada iniciativa, dentro de su ámbito.',
    `<div class="row">${card('i', 'Uno', 'Programa', 'Tiene uno o varios ámbitos')}${ar}${card('i', 'Por ámbito', 'Diagnóstico', 'Una restricción, una línea base y un mapa por ámbito')}${ar}${card('', 'La cartera', 'Iniciativas', 'Salen del diagnóstico y se ordenan por la restricción')}${ar}${card('', 'En el diseño', 'Opciones', 'Cada iniciativa compara opciones con las cinco preguntas')}${ar}${card('a', 'Cada iniciativa', 'Piloto, escala y sostenimiento', 'Con su puerta al final de cada fase')}</div>`,
    '<b>Una restricción por ámbito.</b> Solo los habilitadores y las obligaciones legales pueden no atacarla. En cada puerta de escala se comprueba si sigue siendo la misma.'),

  'fig-puerta.png': page('Las cinco preguntas de la puerta', 'Una página por opción de diseño. Las cinco se contestan por escrito antes de aprobar un piloto.',
    `<div class="row">${card('i', 'El objetivo', '¿Ataca la restricción, y cuánto vale?', 'Sí o no, y cómo. Qué resultado del negocio cambia y quién es el dueño del beneficio', '1')}${card('a', 'Tecnología', '¿Acelera, automatiza o aumenta?', 'A quién y en qué tareas. Qué criterio gana o pierde la persona', '2')}${card('', 'Conocimiento', '¿Qué pasa con el mapa?', 'Qué filas se quedan en la persona, cuáles pasan al sistema y cuáles se pierden', '3')}${card('t', 'Personas', '¿Quién responde y quién enseña?', 'Quién responde si el sistema se equivoca. Quién enseña lo que la tarea enseñaba', '4')}${card('i', 'Los tres', '¿Crecen a la vez?', 'Qué indicador de cada elemento mejora y cuál empeora', '5')}</div>`,
    '<b>Tres salidas:</b> pasar, ajustar y repetir, o retirar. &nbsp; <b>Firma</b> el patrocinador y <b>contrafirma</b> una persona ajena al equipo del programa. Medición certifica los datos.'),

  'fig-verbos.png': page('Acelerar, automatizar o aumentar', 'Se responde por tarea, no por herramienta. Dos preguntas bastan para saber cuál de los tres verbos es.',
    `<div class="row" style="align-items:center"><div class="card dark" style="flex:0 0 250px"><span class="k">Para cada tarea</span><b>¿Qué le pasa a la persona?</b></div>${ar}
    <div class="col" style="flex:1">
      <div class="row" style="align-items:center"><div class="chip" style="flex:0 0 430px">¿La persona <b>sale</b> del circuito?</div><div class="arrow">sí →</div>${card('i', '', 'Automatiza', 'La tarea la hace el sistema. Hay que decir quién responde y qué pasa con lo que esa tarea enseñaba')}</div>
      <div class="row" style="align-items:center"><div class="chip" style="flex:0 0 430px">Sigue, y se espera <b>solo tiempo</b></div><div class="arrow">sí →</div>${card('a', '', 'Acelera', 'Lo mismo, más rápido. Hay que decir a qué se dedica el tiempo ganado')}</div>
      <div class="row" style="align-items:center"><div class="chip" style="flex:0 0 430px">Sigue, y se espera <b>mejor calidad o algo que antes no hacía</b></div><div class="arrow">sí →</div>${card('', '', 'Aumenta', 'La persona hace más o mejor de lo que hacía. Se dice con qué indicador se va a comprobar')}</div>
    </div></div>`),

  'fig-autonomia.png': page('La escala de autonomía', 'Cada peldaño se gana en una puerta, con criterios escritos antes. Bajar es tan legítimo como subir.',
    `<div class="row" style="align-items:flex-end">
      <div class="card" style="min-height:230px">${'<span class="num">1</span><b>Sugiere</b><span>El sistema ofrece información o un borrador. La persona decide y hace todo</span>'}</div>
      <div class="card t" style="min-height:300px"><span class="num">2</span><b>Propone</b><span>El sistema propone una decisión completa. La persona revisa cada propuesta y decide</span><span style="margin-top:14px;color:${TERRA}"><b style="font-size:20px;font-family:'DejaVu Sans';color:${TERRA}">Techo de partida</b>para decisiones que afectan a derechos, que no se pueden deshacer o que hay que poder explicar</span></div>
      <div class="card a" style="min-height:370px"><span class="num">3</span><b>Actúa con revisión</b><span>El sistema decide en los casos tipo. La persona revisa por muestreo y todos los casos fuera de patrón</span></div>
      <div class="card i" style="min-height:440px"><span class="num">4</span><b>Actúa e informa</b><span>El sistema decide y ejecuta dentro de límites. La persona supervisa indicadores y atiende excepciones</span></div>
    </div>`,
    '<b>Antes de cada peldaño, por escrito:</b> el criterio de subida, quién responde si el sistema se equivoca y qué se registra de cada acción. Los controles mínimos de cada nivel están en el módulo 24.'),

  'fig-comite.png': page('Quién decide en una puerta', 'Deciden pocos. A los demás se les oye antes, por escrito, y sus objeciones quedan anotadas.',
    `<div class="row"><div class="col" style="flex:1.25"><span class="k" style="color:${INK}">Deciden cuatro</span><div class="row">${card('i', '', 'Patrocinador', 'Decide y firma')}${card('', '', 'Dueño operativo', 'Responde de la solución cuando el programa se va')}</div><div class="row">${card('a', '', 'Medición', 'Certifica los datos. No firma la decisión')}${card('t', '', 'Persona ajena', 'De la segunda línea o de finanzas. Contrafirma')}</div></div>
    <div class="col" style="flex:1"><span class="k" style="color:${INK}">Son oídos antes, por escrito</span><div class="chip">Quien hace el trabajo</div><div class="chip">El mando intermedio del ámbito</div><div class="chip">Quien defiende a quien recibe el servicio</div><div class="chip">El área de tecnología</div><div class="chip" style="background:#F8E9E1">La representación legal, cuando la decisión toca condiciones de trabajo</div></div></div>`,
    '<b>Programa acotado:</b> no hay comité. Firma el patrocinador con quien dirige el programa y contrafirma alguien ajeno.'),

  'fig-medicion.png': page('Cómo se mide', 'Dos clases de indicador y, como mínimo, uno del objetivo y uno por elemento. La línea base se toma antes de cambiar nada.',
    `<div class="row">${card('', 'Indicadores de avance', 'Tienen objetivo', 'Entran en el delta: cuánto se ha recorrido desde la línea base hacia el objetivo. El objetivo y los pesos se firman en el diseño y no cambian hasta el siguiente ciclo')}${card('t', 'Indicadores de guarda', 'Tienen un suelo', 'No entran en la media. Se cumplen o no se cumplen. Ninguno puede bajar de su suelo para pasar una puerta')}</div>
    <div class="row" style="margin-top:22px">${card('i', 'Objetivo de negocio', 'Resultado', 'Lo que cambió en el servicio o en el negocio. Su delta se lee aparte del de las palancas')}${card('t', 'Personas', 'Capacidad y carga', 'Casos fuera de patrón que el equipo resuelve sin escalar. La carga percibida, como guarda')}${card('', 'Conocimiento', 'Concentración', 'Cuántas filas críticas del mapa siguen en una sola persona')}${card('a', 'Tecnología', 'Uso', 'El uso es condición del resultado y no lo prueba. Se lee junto a la capacidad')}</div>`,
    '<b>Se lee por equipo.</b> Una lectura individual se pacta antes con el equipo y con la representación legal. Un cambio menor que la variación normal del indicador no cuenta ni como mejora ni como retroceso.'),

  'fig-curva.png': page('El valle que hay que prever', 'Al cambiar la forma de trabajar, el resultado medido suele bajar antes de subir. El modelo económico lo dice de antemano.',
    `<svg width="1480" height="440" viewBox="0 0 1480 440"><line x1="70" y1="380" x2="1440" y2="380" stroke="${INK}" stroke-width="3"/><line x1="70" y1="40" x2="70" y2="380" stroke="${INK}" stroke-width="3"/>
    <line x1="70" y1="200" x2="1440" y2="200" stroke="${GREY}" stroke-width="2" stroke-dasharray="10 8"/><text x="1430" y="188" text-anchor="end" font-size="19" fill="${GREY}">línea base</text>
    <path d="M70 200 C260 200 300 330 470 330 C700 330 760 90 1440 60" fill="none" stroke="${GREEN}" stroke-width="8" stroke-linecap="round"/>
    <path d="M150 200 C260 200 300 330 470 330 C590 330 650 250 720 200 Z" fill="${TERRA}" opacity="0.14"/>
    <text x="440" y="270" text-anchor="middle" font-family="EB Garamond" font-size="30" fill="${TERRA}">valle previsto</text>
    <text x="440" y="366" text-anchor="middle" font-size="18" fill="${GREY}">rediseño del trabajo, formación, procesos nuevos</text>
    <circle cx="720" cy="200" r="11" fill="${INK}"/><text x="745" y="246" font-size="19" fill="${INK}">se recupera la línea base</text>
    <text x="1100" y="80" text-anchor="middle" font-family="EB Garamond" font-size="30" fill="${GREEN}">resultado</text>
    <text x="755" y="418" text-anchor="middle" font-size="19" fill="${GREY}">tiempo</text><text x="40" y="215" font-size="19" fill="${GREY}" transform="rotate(-90 40 215)" text-anchor="middle">resultado medido</text></svg>`,
    '<b>Criterio del piloto:</b> ningún indicador de guarda baja de su suelo, y los indicadores con valle previsto no bajan más de lo previsto. Llevar la curva de la empresa a un programa es una analogía del autor.'),

  'fig-nucleo.png': page('Qué es obligatorio según el alcance', 'El método no se aplica entero a todo. Cada alcance añade piezas al anterior.',
    `<div class="col">
      <div class="card i"><span class="k">Siempre · iniciativa puntual</span><b>Ocho piezas</b><span>Restricción nombrada · línea base · mapa del trabajo afectado · decisión de puerta de una página · un indicador por elemento · criterio de parada · cómo se deshace · dueño</span></div>
      <div class="card" style="margin-left:70px;border-radius:0 10px 0 46px"><span class="k">Se añade · iniciativa de flujo</span><b>Rediseñar y adoptar</b><span>Rediseño del trabajo · casos de prueba · registro de supuestos · responsable de adopción y referentes · destino del tiempo</span></div>
      <div class="card a" style="margin-left:140px"><span class="k">Se añade · iniciativa de sistema</span><b>El método completo</b><span>Modelo económico con valle · las tres miradas · gobierno completo</span></div>
    </div>`,
    '<b>Si hay un agente,</b> su ficha es obligatoria en cualquier alcance. Quitar una pieza lo decide el patrocinador y se anota en el registro de decisiones.'),

  'fig-carriles.png': page('Innovar con IA: dos carriles', 'Mejorar lo que ya se hace y explorar lo que todavía no se hace piden reglas distintas.',
    `<div class="col">
      <div class="row" style="align-items:center"><div class="card dark" style="flex:0 0 300px"><span class="k">Carril de mejora</span><b>Explotar</b></div>${card('', '', 'Sigue el tronco', 'Diagnóstico, diseño, piloto, escala y sostenimiento, con sus puertas')}${card('', '', 'Se mide por resultado', 'Delta sobre la línea base e indicadores de guarda')}</div>
      <div class="row" style="align-items:center"><div class="card a" style="flex:0 0 300px"><span class="k">Carril de exploración</span><b>Explorar</b></div>${card('a', '', 'Un laboratorio pequeño', 'Experimentos de días o semanas, cada uno con su supuesto escrito')}${card('a', '', 'Se mide por lo aprendido', 'Experimentos cerrados, supuestos caídos, tiempo hasta la primera evidencia')}</div>
    </div>`,
    '<b>Un experimento termina de tres maneras:</b> se descarta y se anota lo aprendido, se repite con otro supuesto, o entra en la cartera y recorre el tronco desde el diagnóstico de su ámbito. Nada llega al servicio por fuera de las puertas.'),
};

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1600, height: 1200 }, deviceScaleFactor: 2 });
  for (const [name, html] of Object.entries(figs)) {
    const tmp = path.join(dir, '_' + name.replace('.png', '.html')); fs.writeFileSync(tmp, html);
    await p.goto('file://' + tmp); await p.waitForTimeout(500);
    await (await p.$('#f')).screenshot({ path: path.join(out, name) }); fs.unlinkSync(tmp);
    console.log('ok', name);
  }
  await b.close();
})();
