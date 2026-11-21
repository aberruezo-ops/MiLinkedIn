// Diez figuras más para entender el método de un vistazo, en el estilo de hoja.
// Uso: NODE_PATH=$(npm root -g) node figs/mas-figs.js [nombre-de-figura ...]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const dir = __dirname, out = path.join(dir, '..');
const INK = '#1F1D1A', GREEN = '#2C6D3F', TERRA = '#B5512A', ALB = '#C89A2A', ALBT = '#8A6508', GREY = '#56606A', LINE = '#D7DCDC';
const LOGO = 'file://' + path.join(dir, '../../../imagenes/logo-synergos.svg');
const css = `*{box-sizing:border-box;margin:0;padding:0}body{width:1600px;background:#fff;font-family:'Public Sans',sans-serif;color:${INK}}
#f{width:1600px;background:#fff;padding:54px 60px 50px;position:relative}
.mark{position:absolute;right:60px;top:50px;height:50px}
h1{font-family:'EB Garamond',serif;font-weight:normal;font-size:58px;line-height:1.05;margin-bottom:10px;max-width:1150px}
.sub{font-size:22px;color:${GREY};margin-bottom:34px;line-height:1.35;max-width:1250px}
.row{display:flex;gap:22px;align-items:stretch}.col{display:flex;flex-direction:column;gap:18px}.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.card{background:#EAF2EC;padding:24px 26px 28px;flex:1;border-radius:10px 0 46px 0}
.card.b{border-radius:0 10px 0 46px}
.card b{font-family:'EB Garamond',serif;font-weight:normal;font-size:34px;display:block;line-height:1.15;margin-bottom:8px}
.card span{font-size:19px;line-height:1.4;color:${GREY};display:block}
.card .r{color:${INK};font-weight:600;margin-top:14px;font-size:18px}
.num{font-family:'EB Garamond',serif;font-size:56px;line-height:1;color:${GREEN};display:block;margin-bottom:6px}
.k{font-size:16px;letter-spacing:2px;text-transform:uppercase;color:${GREEN};display:block;margin-bottom:8px}
.t{background:#F8E9E1}.t .num,.t .k{color:${TERRA}}.a{background:#F8EDD0}.a .num,.a .k{color:${ALBT}}.i{background:#ECEEEE}.i .num,.i .k{color:${INK}}
.dark{background:${INK};color:#fff}.dark span{color:#D7DCDC}.dark .k{color:#B9C0BE}.dark .num{color:#fff}
.chip{background:#F4F6F6;padding:16px 26px 16px 20px;font-size:20px;line-height:1.3;border-radius:0 26px 0 10px}
.arrow{align-self:center;font-size:38px;color:${GREEN};flex:0 0 auto}
.pie{margin-top:30px;font-size:19px;color:${GREY};line-height:1.4;border-top:2px solid ${LINE};padding-top:18px}
.pie b{color:${INK};font-weight:normal;font-family:'EB Garamond',serif;font-size:22px}
.tag{display:inline-block;font-size:14px;letter-spacing:1.5px;text-transform:uppercase;background:#fff;color:${GREEN};padding:4px 12px 4px 10px;border-radius:0 12px 0 4px;margin-bottom:10px;font-weight:600}
.door{background:${INK};color:#fff;border-radius:0 16px 0 80px;padding:26px 44px 30px}
.door b{font-family:'EB Garamond',serif;font-weight:normal;font-size:36px;display:block;margin-bottom:6px}.door span{font-size:20px;color:#D7DCDC;line-height:1.4;display:block}
.mx{display:grid;grid-template-columns:230px repeat(4,1fr);gap:10px}
.mx div{padding:16px 18px;font-size:18px;line-height:1.35;border-radius:0 18px 0 6px}
.mx .h{font-size:15px;letter-spacing:2px;text-transform:uppercase;color:${GREY};padding:6px 4px;background:none}
.mx .l{font-family:'EB Garamond',serif;font-size:32px;background:none;padding:14px 4px}
.mx .c1{background:#F4F6F6}.mx .c2{background:#CFE3D5;font-weight:600}.mx .c3{background:#E1EDE4}.mx .c4{background:#EAF2EC}
.dm{display:grid;grid-template-columns:420px repeat(6,1fr);gap:8px 8px;align-items:center}
.dm .h{font-size:13px;letter-spacing:0.5px;text-transform:uppercase;color:${GREY};text-align:center}
.dm .n{font-size:21px;padding:6px 0}.dm .p{height:34px;border-radius:0 14px 0 6px;background:#F4F6F6}.dm .p.on{background:${GREEN}}.dm .p.on.x{background:${ALB}}
`;
const page = (h1, sub, body, pie = '') => `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div id="f"><img class="mark" src="${LOGO}"><h1>${h1}</h1><div class="sub">${sub}</div>${body}${pie ? `<div class="pie">${pie}</div>` : ''}</div></body></html>`;
const card = (cls, k, b, s, extra = '') => `<div class="card ${cls}">${k ? `<span class="k">${k}</span>` : ''}<b>${b}</b><span>${s}</span>${extra}</div>`;
const ar = '<div class="arrow">→</div>';

const figs = {
  'fig-causas.png': page('Tres patrones detrás de casi todos los fracasos', 'Mirada con calma, la tabla de causas del capítulo 2 se reduce a tres cosas. Cada una tiene su respuesta en el método.',
    `<div class="row">
     ${card('i', 'Uno', 'El orden', 'Casi nunca se hace algo mal. Se hace en el momento equivocado: elegir la solución antes del diagnóstico, comprar la tecnología antes de rediseñar el trabajo, formar a la gente después de decidir.', '<span class="r">Respuesta: el orden y las puertas</span>')}
     ${card('t b', 'Dos', 'Lo que no se ve', 'Existe y nadie lo mira: el conocimiento que no está escrito, el incentivo que sigue premiando lo de antes, el supuesto que nadie cuestiona, el usuario que no estaba en la sala.', '<span class="r">Respuesta: entregables que lo hacen visible, como el mapa de lo que nadie escribió</span>')}
     ${card('a', 'Tres', 'La balanza', 'La tecnología puede sustituir a las personas o ampliar lo que pueden hacer. Zuboff lo dijo en 1988 con dos verbos, automatizar o informar. Synergós usa tres.', '<span class="r">Respuesta: acelerar, automatizar o aumentar, tarea por tarea</span>')}
    </div>`),

  'fig-principios.png': page('Los seis principios', 'Se aplican cuando el método no dice nada concreto. Cada uno dice de dónde sale y qué se arriesga si se aplica mal.',
    `<div class="g3">
     ${card('', '1', 'Diagnóstico antes que solución', 'Nada entra en diseño sin una restricción nombrada y una línea base medida.')}
     ${card('a b', '2', 'Elemento antes que acelerador', 'Un acelerador entra en el servicio si lo que necesita está en nivel 2 en los tres elementos y en el gobierno.')}
     ${card('t', '3', 'Pocas cosas a la vez', 'La IA dentro del servicio y uno o dos aceleradores más por ciclo, los que atacan la restricción.')}
     ${card('i b', '4', 'Puertas con criterios fijados antes', 'Los criterios se escriben al empezar la fase, no al terminarla.')}
     ${card('', '5', 'Nada nuevo encima de lo no mirado', 'Cada iniciativa se coloca donde no haga sombra a las personas ni a lo que ya funcionaba.')}
     ${card('a b', '6', 'El método se supervisa a sí mismo', 'Si una pieza no aporta en un programa, se retira. Lo decide el patrocinador y se anota.')}
    </div>`),

  'fig-diagnostico.png': page('Los seis entregables del diagnóstico', 'Se hacen con quien trabaja, no sobre quien trabaja. Tres de ellos son los que abren la puerta al diseño.',
    `<div class="g3">
     ${card('', 'Diseño del trabajo', 'Mapa del flujo real', 'No el del procedimiento, el que se hace. Se observa en el puesto.')}
     ${card('i b', 'Dirección del programa', 'Restricción principal', 'Una por ámbito, nombrada y aceptada por el patrocinador.', '<span class="r">Abre la puerta</span>')}
     ${card('a', 'Medición', 'Línea base', 'Medida, no estimada. Al menos un indicador por elemento.', '<span class="r">Abre la puerta</span>')}
     ${card('t b', 'Dirección del programa', 'Mapa de actores', 'Quién gana, quién pierde, quién decide, quién bloquea y quién sabe.')}
     ${card('', 'Medición', 'Madurez', 'Un nivel por elemento y uno de gobierno, con su evidencia. Sirve a la regla de entrada.')}
     ${card('t', 'Conocimiento', 'Mapa de lo que nadie escribió', 'La aportación propia de Synergós. Se levanta a la vez que el mapa del flujo.', '<span class="r">Abre la puerta</span>')}
    </div>
    <div class="door" style="margin-top:24px"><b>Puerta del diagnóstico</b><span>Para pasar al diseño: la restricción está nombrada y aceptada, la línea base está medida y el mapa de lo que nadie escribió existe y el patrocinador ha firmado su compromiso de uso.</span></div>`),

  'fig-piloto.png': page('Cómo es un piloto', 'Un piloto prueba en pequeño, con gente real y datos reales, lo que el diseño ha decidido. Los criterios se escribieron antes.',
    `<div class="row">
     <div class="col" style="flex:1.5">
       ${card('i', 'Antes de empezar', 'Lo que se deja escrito', 'Los criterios para pasar, el criterio de parada, la fecha de revisión a noventa días, el registro de supuestos y los casos de prueba que prepara quien hace el trabajo.')}
       ${card('', 'El entorno', 'Con una condición difícil', 'Rotación, volumen alto, casos raros o sistemas antiguos. La pregunta útil no es dónde va a funcionar, sino dónde puede fallar.')}
       ${card('a', 'La comparación', 'Contra la línea base y un grupo sin el cambio', 'Un cambio menor que la variación normal del indicador no cuenta como mejora.')}
     </div>${ar}
     <div class="col" style="flex:1">
       <div class="door"><b>La puerta</b><span>Tres salidas. Los criterios no se reescriben al ver el resultado.</span></div>
       ${card('', 'Si se cumplen', 'Pasar', 'Va a escala.')}
       ${card('a b', 'Prometedor pero incompleto', 'Ajustar y repetir', 'Una vez como máximo y con los mismos criterios.')}
       ${card('t', 'Si no funciona', 'Retirar', 'Se anota qué pasa con las filas del mapa y con las personas.')}
     </div></div>`),

  'fig-escala.png': page('Cómo se pasa a escala', 'Nunca de golpe. La escala se sostiene con personas con nombre y con tiempo, no solo con una herramienta desplegada.',
    `<div class="row">
     <div class="col" style="flex:1">
       <span class="k" style="color:${INK}">Cómo se despliega</span>
       ${card('', '', 'Por etapas', 'Cada etapa tiene su minipuerta: los indicadores tienen que aguantar al ampliar. La decide el dueño operativo.')}
       ${card('a b', '', 'Formación en el puesto', 'Acompañamiento mientras se trabaja, no un curso de un día.')}
     </div>
     <div class="col" style="flex:1.4">
       <span class="k" style="color:${INK}">Quién lo sostiene</span>
       <div class="row">${card('t', '', 'Responsable de adopción', 'Con nombre y tiempo, distinto de quien despliega.')}${card('', '', 'Varios referentes por área', 'Quien ya usa bien la herramienta, con tiempo reconocido para ayudar.')}</div>
       <div class="row">${card('i b', '', 'Normas de equipo', 'Cuándo se usa la IA y cuándo no, por escrito.')}${card('a', '', 'Roles, carreras e incentivos', 'Si el trabajo cambia y la evaluación no, la gente hace lo que se evalúa.')}</div>
     </div></div>
     <div class="door" style="margin-top:24px"><b>Puerta de escala</b><span>Los indicadores aguantan al ampliar y los tres elementos aguantan la carga: personas formadas, conocimiento donde tiene que estar y tecnología que soporta el volumen.</span></div>`),

  'fig-sostenimiento.png': page('Cómo se sostiene lo que ya funciona', 'El programa termina y el servicio sigue. Hace falta alguien que responda cuando el equipo del programa ya no esté.',
    `<div class="row">
     <div class="g3" style="flex:2;grid-template-columns:1fr 1fr">
       ${card('i', '', 'Un dueño operativo', 'Con nombre, que acepta la responsabilidad.')}
       ${card('', '', 'Presupuesto recurrente', 'No el del proyecto.')}
       ${card('a b', '', 'Indicadores en régimen', 'Un cuadro que se mira sin que nadie lo pida.')}
       ${card('t', '', 'Evaluación que no termina', 'Un sistema de IA cambia aunque nadie lo toque.')}
     </div>${ar}
     <div class="door" style="flex:1.2;display:flex;flex-direction:column;justify-content:center"><b>Puerta de sostenimiento</b><span>El dueño acepta por escrito y los indicadores aguantan dos periodos de medición sin el equipo del programa. La convoca el dueño y decide el patrocinador.</span></div>
    </div>
    <svg width="1480" height="130" viewBox="0 0 1480 130" style="margin-top:14px"><path d="M1380 0 C1380 100 1300 118 1150 118 L330 118 C180 118 100 100 100 20" fill="none" stroke="${GREEN}" stroke-width="3.5" stroke-linecap="round"/><path d="M100 4 L88 34 L112 34 Z" fill="${GREEN}"/></svg>
    <div style="text-align:center;font-size:21px;color:${GREY};margin-top:-6px">Lo aprendido alimenta el diagnóstico del siguiente ciclo: el tronco se cierra sobre sí mismo.</div>`),

  'fig-madurez.png': page('La escala de madurez y la regla de entrada', 'Cuatro niveles, evaluados en horas con el equipo afectado. Cuando los rasgos de una celda no se cumplen todos, vale el nivel más bajo.',
    `<div class="mx">
     <div class="h"></div><div class="h" style="text-align:left">1. Puntual</div><div class="h" style="text-align:left;color:${GREEN};font-weight:600">2. Repetible · lo que pide la regla</div><div class="h" style="text-align:left">3. Integrado</div><div class="h" style="text-align:left">4. Sistemático</div>
     <div class="l" style="color:${TERRA}">Personas</div><div class="c1">Buena voluntad, sin roles ni tiempo</div><div class="c2">Patrocinador con tiempo fijo y forma acordada de implicar a quien trabaja</div><div class="c3">Roles, incentivos y formación se rediseñan con el trabajo</div><div class="c4">La cartera nace en parte de empleados y usuarios</div>
     <div class="l" style="color:${GREEN}">Conocimiento</div><div class="c1">Está en personas y nadie lo ha escrito</div><div class="c2">Lista escrita de lo crítico que está en una sola persona y registro de decisiones en uso</div><div class="c3">Datos con dueño y calidad medida</div><div class="c4">La concentración se mide y se reduce a propósito</div>
     <div class="l" style="color:${ALBT}">Tecnología</div><div class="c1">Uso individual, sin reglas</div><div class="c2">Reglas de uso, datos autorizados, lista de lo que se usa y un responsable por solución</div><div class="c3">Entra por criterios escritos antes; la autonomía sube por niveles</div><div class="c4">Se vigila lo emergente y hay salida pactada con proveedores</div>
     <div class="l">Gobierno</div><div class="c1">Decide quien trae la tecnología; nadie responde de un error</div><div class="c2">Tabla de quién decide qué y quién firma y contrafirma</div><div class="c3">Criterios previos; riesgos, seguridad y datos desde el diseño</div><div class="c4">Los derechos de decisión se revisan y lo que no aporta se retira</div>
    </div>`,
    '<b>La regla de entrada:</b> un acelerador entra en el servicio solo si lo que necesita está en nivel 2 en el ámbito. El nivel de madurez no es lo mismo que el nivel de autonomía de un sistema.'),

  'fig-uso-informal.png': page('Qué hacer con la IA que ya se usa', 'En casi todas las organizaciones hay gente usando herramientas que nadie aprobó. Prohibirlo sin ofrecer alternativa lo esconde.',
    `<div class="row">
     ${card('', '1', 'Averiguar', 'Qué se usa de verdad, con una consulta anónima en el diagnóstico.')}${ar}
     ${card('a b', '2', 'Ofrecer', 'Herramientas aprobadas que sirvan para lo que la gente hace con las otras.')}${ar}
     ${card('', '3', 'Abrir un canal', 'Para pedir herramientas nuevas, con respuesta en plazo.')}${ar}
     ${card('t b', '4', 'Garantizar', 'Contar un uso para que se evalúe no trae sanción. No exime de comunicar una posible fuga de datos.')}
    </div>`,
    '<b>Lo que la gente usa a escondidas dice dónde está la necesidad.</b> Qué datos pueden usarse con cada herramienta lo dice el módulo 11.'),

  'fig-modulos.png': page('En qué fases pesa cada módulo', 'Los módulos 1 a 14 se cruzan con las cinco fases. Los diez siguientes pesan más en unas que en otras.',
    `<div class="card i" style="margin-bottom:26px;border-radius:10px 0 46px 0"><b>Módulos 1 a 14</b><span>Pesan en las cinco fases. Su cruce, celda por celda, está en la tabla que sigue al módulo 14.</span></div>
    <div class="dm">
     <div class="h" style="text-align:left">Módulos 15 a 24</div><div class="h">Antes del tronco</div><div class="h">Diagnóstico</div><div class="h">Diseño</div><div class="h">Piloto</div><div class="h">Escala</div><div class="h">Sostenimiento</div>
     ${[['15. Los mandos intermedios', [0, 1, 1, 1, 0, 0]], ['16. Cultura y estructura', [0, 1, 1, 0, 0, 0]], ['17. Plazos realistas (y antes de cada puerta)', [0, 0, 1, 0, 0, 0]], ['18. Los trabajadores ante los algoritmos', [0, 1, 1, 1, 0, 0]], ['19. Cuando un puesto desaparece', [0, 0, 1, 0, 1, 0]], ['20. Inclusión', [0, 1, 1, 0, 0, 0]], ['21. Quien recibe el servicio', [0, 1, 1, 1, 0, 0]], ['22. La huella material', [0, 0, 1, 0, 0, 0]], ['23. Innovar con IA (carril de exploración)', [1, 0, 0, 0, 0, 0]], ['24. Los agentes', [0, 0, 1, 1, 1, 1]]].map(([n, v]) => `<div class="n">${n}</div>${v.map((x, i) => `<div class="p ${x ? 'on' : ''} ${i === 0 && x ? 'x' : ''}"></div>`).join('')}`).join('')}
    </div>`,
    '<b>Un módulo 23 aparte:</b> el carril de exploración va antes del tronco y enlaza con el diagnóstico cuando un experimento pasa a la cartera.'),

  'fig-mejora.png': page('Cómo se corrige el método', 'El método se aplica a sí mismo sus herramientas: línea base, control de causas, doble bucle y registro de decisiones.',
    `<div class="row">
     ${card('i', 'Punto de partida', 'Línea base', 'La versión 1.0. Todo cambio se compara con ella.')}${ar}
     ${card('a b', 'Control', 'Tabla de causas', 'Cada pieza dice a qué causa de fracaso responde.')}${ar}
     ${card('', 'Constancia', 'Registro de decisiones', 'Con fecha y motivo.')}${ar}
     ${card('t b', 'Cada trimestre', 'Doble bucle', 'Si las piezas funcionan y si los supuestos siguen siendo ciertos.')}${ar}
     ${card('a', 'Con quien lo lee', 'Objeciones', 'Parte de las mejoras vino de conversaciones públicas.')}
    </div>
    <svg width="1480" height="120" viewBox="0 0 1480 120" style="margin-top:14px"><path d="M1380 0 C1380 90 1300 108 1150 108 L330 108 C180 108 100 90 100 20" fill="none" stroke="${GREEN}" stroke-width="3.5" stroke-linecap="round"/><path d="M100 4 L88 34 L112 34 Z" fill="${GREEN}"/></svg>
    <div style="text-align:center;font-size:21px;color:${GREY};margin-top:-6px">Nueva versión, anotada en el registro de versiones del anexo F.</div>`,
    '<b>Todavía no ha habido ninguna revisión trimestral completa.</b> El supuesto más importante del método sigue sin probar.'),
};

(async () => {
  const only = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1600, height: 1200 }, deviceScaleFactor: 2 });
  for (const [name, html] of Object.entries(figs)) {
    if (only.length && !only.includes(name)) continue;
    const tmp = path.join(dir, '_' + name.replace('.png', '.html')); fs.writeFileSync(tmp, html);
    await p.goto('file://' + tmp); await p.waitForTimeout(500);
    await (await p.$('#f')).screenshot({ path: path.join(out, name) }); fs.unlinkSync(tmp);
    console.log('ok', name);
  }
  await b.close();
})();
