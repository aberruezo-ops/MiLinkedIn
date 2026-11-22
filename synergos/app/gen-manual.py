# Genera manual-gestor.html: manual del Gestor Synergós con glosario.
# Cada término del glosario que aparece en el texto sale como enlace a su entrada,
# con texto alternativo (atributo title) que lleva la definición.
import re, html, sys

GLOS = {  # id: (término, variantes en minúscula, definición)
 'acelerador': ('Acelerador', ['aceleradores', 'acelerador'], 'Tecnología concreta que se activa en un ámbito: la IA dentro del servicio, una plataforma o una herramienta de automatización. Entra solo si se cumple la regla de entrada.'),
 'agente': ('Agente', ['agentes', 'agente'], 'Sistema de IA que usa herramientas, encadena pasos y ejecuta acciones para cumplir un objetivo, con distinto grado de autonomía. Un asistente responde; un agente actúa, y su error es una acción ya hecha.'),
 'alcance': ('Alcance', ['alcances', 'alcance'], 'Etiqueta de cada iniciativa: puntual si mejora una tarea, de flujo si obliga a rediseñar un proceso de principio a fin, de sistema si cambia lo que la organización ofrece.'),
 'alerta': ('Alerta', ['alertas', 'alerta'], 'Aviso que el gestor calcula solo cuando algo incumple una regla del método, por ejemplo una puerta sin criterios firmados antes. Se lee en el Resumen y en cada sección.'),
 'ambito': ('Ámbito', ['ámbitos', 'ámbito'], 'El servicio o el flujo de trabajo que se va a transformar. Cada ámbito tiene una sola restricción principal y su propia lectura de madurez.'),
 'autonomia': ('Nivel de autonomía', ['niveles de autonomía', 'nivel de autonomía', 'autonomía'], 'Escala de cuatro peldaños que dice hasta dónde puede llegar un sistema: 1 sugiere, 2 propone, 3 actúa con revisión, 4 actúa e informa. No es lo mismo que el nivel de madurez.'),
 'avance': ('Indicador de avance', ['indicadores de avance', 'indicador de avance'], 'Indicador con objetivo. Entra en el delta, que mide cuánto se ha recorrido desde la línea base hacia ese objetivo.'),
 'caso-ejemplo': ('Caso de ejemplo', ['caso de ejemplo'], 'Datos ilustrativos que trae el gestor al empezar, de un caso compuesto que no corresponde a ninguna organización real. Se quitan con un botón.'),
 'ciclo': ('Ciclo', ['ciclos', 'ciclo'], 'El recorrido de las cinco fases en un ámbito. Lo aprendido en el sostenimiento alimenta el diagnóstico del ciclo siguiente.'),
 'contrafirma': ('Contrafirma', ['contrafirma'], 'Firma de una persona ajena al equipo del programa, de la segunda línea o de finanzas, que acompaña a la del patrocinador en una puerta.'),
 'controles': ('Controles por nivel', ['controles por nivel', 'control por nivel', 'controles'], 'Lista de lo que tiene que existir para que un agente opere en cada nivel de autonomía, como la parada probada o la lista cerrada de acciones aplicada por el sistema. Es una propuesta del método, sin probar.'),
 'criterio-parada': ('Criterio de parada', ['criterio de parada', 'criterios de parada'], 'Resultado que detiene un piloto antes de tiempo. Se escribe al empezar, junto con una fecha de revisión a noventa días.'),
 'delta': ('Delta', ['delta'], 'Porcentaje que un indicador de avance ha recorrido desde su línea base hacia su objetivo, con un máximo del cien por cien. Desde la versión 2.1 del método el delta se da en dos cifras que no se promedian: la del objetivo de negocio y la de las palancas (personas, conocimiento y tecnología), cada una la media ponderada de sus indicadores.'),
 'dueno': ('Dueño operativo', ['dueño operativo', 'dueños', 'dueño'], 'Persona con nombre, del equipo que opera, que responde de lo que la solución hace cuando el programa se va. Es también el dueño del agente.'),
 'elementos': ('Tres elementos', ['tres elementos', 'elementos'], 'Personas, conocimiento y tecnología. El método pide que crezcan a la vez y los mide por separado, con al menos un indicador por elemento y uno del objetivo de negocio.'),
 'roles': ('Roles', ['roles', 'rol'], 'Los papeles que intervienen cuando se aplica el método, en cuatro familias: quien dirige y decide, quien opera y adopta, quien mide y controla, y quien es oído o recibe el beneficio. Una misma persona puede tener varios, salvo las combinaciones que anulan el control de una puerta (anexo I del método).'),
 'objetivo': ('Objetivo de negocio', ['objetivo de negocio'], 'El resultado que la organización quiere cambiar con la transformación. No es un cuarto elemento: es para qué se mueven los tres. Se escribe por ámbito y la restricción se nombra respecto a él.'),
 'arbol': ('Árbol de valor', ['árbol de valor'], 'La cadena que une la restricción con la cuenta de resultados: indicadores operativos, indicadores de resultado y efecto económico, con su horquilla y el dueño del beneficio. Se corrige en cada puerta con lo medido.'),
 'ficha': ('Ficha del agente', ['ficha del agente', 'fichas', 'ficha'], 'Los once campos que se escriben de cada agente antes de un piloto: dueño, finalidad, acciones permitidas, datos, nivel y techo, aprobación humana, parada, registro, coste, personas y conocimiento, y revisión.'),
 'fase': ('Fase', ['fases', 'fase'], 'Cada una de las cinco etapas del tronco: diagnóstico, diseño, piloto, escala y sostenimiento. Cada una termina en una puerta.'),
 'guarda': ('Indicador de guarda', ['indicadores de guarda', 'indicador de guarda'], 'Indicador con un suelo que no se puede perforar. No entra en la media: se cumple o no se cumple, y ninguno puede bajar de su suelo para pasar una puerta.'),
 'inventario': ('Inventario', ['inventario'], 'Registro único de casos de uso, sistemas y agentes. Cada entrada lleva los campos de la ficha del agente más riesgo, proveedor e incidentes.'),
 'iniciativa': ('Iniciativa', ['iniciativas', 'iniciativa'], 'Cada cambio concreto que sale del diagnóstico. Recorre las cinco fases dentro de su ámbito y tiene su puerta al final de cada una.'),
 'linea-base': ('Línea base', ['línea base'], 'Medida, no estimada, que se toma antes de cambiar nada. Sin ella no hay forma de saber si el programa mejora algo. Lleva la variación normal de cada indicador.'),
 'madurez': ('Madurez', ['nivel de madurez', 'niveles de madurez', 'madurez'], 'Escala de cuatro niveles (puntual, repetible, integrado, sistemático) que se evalúa en personas, conocimiento, tecnología y gobierno. Se hace en horas con el equipo afectado.'),
 'mapa': ('Mapa de lo que nadie escribió', ['mapa de lo que nadie escribió', 'mapa'], 'Tabla del conocimiento que sostiene el trabajo y no está escrito: qué se sabe, quién lo sabe, dónde se usa y cuán concentrado está.'),
 'medicion': ('Medición', ['medición'], 'La función que certifica los datos de una puerta. Certifica, pero no firma la decisión.'),
 'patrocinador': ('Patrocinador', ['patrocinador'], 'Quien decide y firma las puertas. Acepta por escrito la restricción del ámbito.'),
 'programa': ('Programa', ['programas', 'programa'], 'El conjunto de ámbitos que se transforman con el método. Un programa no pasa entero por las fases: las recorre cada iniciativa.'),
 'puerta': ('Puerta', ['puertas', 'puerta'], 'Momento de decisión al final de cada fase. Sus criterios se escriben al empezar la fase, no al terminarla. Tiene tres salidas.'),
 'regla-entrada': ('Regla de entrada', ['regla de entrada'], 'Un acelerador entra en el servicio solo si lo que necesita está en nivel 2 de madurez en los tres elementos y en el gobierno del ámbito.'),
 'restriccion': ('Restricción principal', ['restricción principal', 'restricción', 'restricciones'], 'El punto que limita el resultado del conjunto. Una por ámbito, nombrada y aceptada por el patrocinador. Una lista de diez problemas no es un diagnóstico.'),
 'salidas': ('Salidas de la puerta', ['salidas de la puerta', 'ajustar y repetir', 'salidas', 'salida'], 'Pasar, si se cumplen los criterios; ajustar y repetir, una vez como máximo y con los mismos criterios; retirar, si no funciona.'),
 'techo': ('Techo de autonomía', ['techo'], 'Nivel máximo de autonomía que se fija a un agente en la puerta de diseño. Si decide sobre derechos de las personas, el techo de partida es el nivel 2.'),
 'tronco': ('Tronco', ['tronco'], 'Las cinco fases con sus puertas. Cada iniciativa lo recorre dentro de su ámbito.'),
 'umbral': ('Umbral de concentración', ['umbral'], 'Número de filas críticas del mapa que dependen de una sola persona a partir del cual se para a repartir el conocimiento. Tres es un punto de partida propuesto por un lector, sin probar.'),
 'valle': ('Valle', ['valle'], 'Caída previsible del resultado medido antes de que suba, cuando se cambia la forma de trabajar. El modelo económico lo dice de antemano.'),
 'variacion': ('Variación normal', ['variación normal'], 'Cuánto se mueve un indicador sin que nada haya cambiado. Un cambio menor que esa variación no cuenta ni como mejora ni como retroceso.'),
 'verbos': ('Acelerar, automatizar o aumentar', ['acelerar, automatizar o aumentar', 'tres verbos'], 'Los tres verbos con que se responde, tarea por tarea, qué hace la tecnología: acelera lo mismo, automatiza sacando a la persona del circuito, o aumenta lo que la persona hace.'),
}

VAR = {}
for gid, (t, vs, d) in GLOS.items():
    for v in vs:
        VAR[v.lower()] = gid
ALT = '|'.join(re.escape(v) for v in sorted(VAR, key=len, reverse=True))
RX = re.compile(r'(?<![\wáéíóúüñÁÉÍÓÚÑ])(' + ALT + r')(?![\wáéíóúüñÁÉÍÓÚÑ])', re.I)

def esc(s): return html.escape(s, quote=True)

def L(text):
    """Enlaza los términos del glosario en el texto, sin tocar las etiquetas."""
    parts = re.split(r'(<[^>]+>)', text); out = []; depth = 0
    for p in parts:
        if p.startswith('<'):
            if re.match(r'<a\b', p): depth += 1
            if p.startswith('</a'): depth = max(0, depth - 1)
            out.append(p); continue
        if depth: out.append(p); continue
        def rep(m):
            gid = VAR[m.group(1).lower()]; t, vs, d = GLOS[gid]
            return '<a class="gl" href="#g-%s" title="%s">%s</a>' % (gid, esc(t + ': ' + d), m.group(1))
        out.append(RX.sub(rep, p))
    return ''.join(out)

def P(t): return '<p>' + L(t) + '</p>'
def UL(items): return '<ul>' + ''.join('<li>' + L(i) + '</li>' for i in items) + '</ul>'
def TBL(head, rows):
    return '<div class="scroll"><table><thead><tr>' + ''.join('<th>%s</th>' % h for h in head) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>%s</td>' % L(c) for c in r) + '</tr>' for r in rows) + '</tbody></table></div>'

def STEP(n, title, what, check, where=''):
    return ('<section class="step" id="paso-%d"><div class="num">%d</div><div><h3>%s</h3>%s%s<div class="check"><b>Comprueba:</b> %s</div></div></section>'
            % (n, n, title, ('<p class="where">%s</p>' % esc(where)) if where else '', ''.join(P(w) if isinstance(w, str) else UL(w) for w in what), L(check)))

SECS = []  # (id, título, html)

SECS.append(('para-que', 'Para qué sirve', P('El Gestor Synergós es una página donde llevas un programa de transformación con el método. Guarda lo que decides, lo ordena por ámbito y te avisa cuando algo incumple una regla del método. No decide por ti ni sustituye al criterio del equipo.')
 + P('Cada alerta que verás está en el documento del método. El gestor solo las aplica y las deja a la vista. Si algo del documento cambia, el gestor se actualiza después.')
 + '<div class="note"><b>Cómo leer este manual.</b> Cada término que está en el glosario aparece subrayado con puntos y es un enlace a su entrada. Al pasar el cursor por encima ves la definición breve. En el glosario, el botón «Volver» te devuelve al punto donde estabas.</div>'))

SECS.append(('ideas', 'Cuatro ideas antes de empezar', UL([
 'Un programa se lleva por ámbitos. El ámbito es el servicio o el flujo concreto que vas a transformar, no la organización entera.',
 'Cada ámbito tiene una sola restricción principal: el punto que limita el resultado. Todo lo demás se ordena en torno a ella.',
 'Cada iniciativa recorre las cinco fases del tronco, y cada fase acaba en una puerta. Los criterios de la puerta se escriben antes de empezar la fase.',
 'Los tres elementos, personas, conocimiento y tecnología, crecen a la vez y se miden por separado. Por eso el gestor te pide al menos un indicador de cada uno.',
 'La tecnología se explica tarea por tarea con los tres verbos: acelerar, automatizar o aumentar. Cada uno pide cosas distintas a quien lo diseña.',
 'Al llegar al sostenimiento se cierra un ciclo, y lo aprendido alimenta el siguiente diagnóstico.'])))

pasos = ''.join([
 STEP(1, 'Abre el gestor y mira el caso de ejemplo', [
  'Abre el enlace del gestor con tu sesión de Claude. Los datos se guardan en tu cuenta y solo los ves tú, salvo que compartas la página.',
  'La primera vez verás un caso de ejemplo: una atención de peticiones inventada, compuesta para ilustrar. Dedícale cinco minutos antes de crear nada. Mira el Resumen, abre cada alerta y entra en las secciones Puertas y Agentes.'],
  'que entiendes por qué el ejemplo tiene alertas: una puerta con criterios que no se firmaron antes, cuatro filas del mapa en una sola persona y un indicador de guarda por debajo de su suelo.', 'Sección Resumen'),
 STEP(2, 'Quita el ejemplo', [
  'Pulsa «Quitar el ejemplo y empezar» en el banner superior, o hazlo desde Ajustes. Pide confirmación porque el borrado es definitivo.'],
  'que el Resumen dice que todavía no hay ningún ámbito y te ofrece crear el primero.', 'Banner del Resumen o sección Ajustes'),
 STEP(3, 'Crea el ámbito', [
  'En «Ámbitos e iniciativas» pulsa «Nuevo ámbito». Escribe un nombre que reconozca quien trabaja en él, la restricción principal y el patrocinador.',
  'Escribe una sola restricción. Si el equipo no se pone de acuerdo en cuál es, el programa todavía no sabe qué está tratando de resolver. Déjala sin nombrar si hace falta: el gestor te lo recordará en cuanto pases del diagnóstico.'],
  'que la restricción es una frase y que el patrocinador la ha aceptado por escrito fuera del gestor.', 'Ámbitos e iniciativas > Nuevo ámbito'),
 STEP(4, 'Evalúa la madurez', [
  'En el mismo formulario fija el nivel de madurez de personas, conocimiento, tecnología y gobierno, del 1 al 4, y anota la evidencia en que te apoyas.',
  'La evaluación se hace en horas, con el equipo afectado y no sobre él. Cuando los rasgos de un nivel no se cumplen todos, vale el nivel más bajo.'],
  'que cualquier elemento por debajo del nivel 2 aparece en rojo en el Resumen. Mientras sea así, la regla de entrada no se cumple y la tecnología no debería entrar en el servicio.', 'Formulario del ámbito'),
 STEP(5, 'Mide la línea base', [
  'En Indicadores pulsa «Nuevo indicador». Crea uno del objetivo de negocio (el resultado que se quiere cambiar) y al menos uno por elemento. Para cada uno anota la clase, la línea base medida y la variación normal.',
  ['Indicador de avance: tiene objetivo y pesa en el delta. Anota el objetivo y, si quieres que pese más, el peso.',
   'Indicador de guarda: tiene un suelo, o un techo si mejora cuando baja. No entra en la media. Elige en «Mejor cuando» el sentido correcto.'],
  'La línea base se mide antes de cambiar nada. Si no la tienes, no inventes un valor: deja el indicador sin datos.'],
  'que el estado del indicador dice «Sin datos» hasta que escribas un valor actual, y que un cambio menor que la variación normal se muestra como «Dentro de la variación normal».', 'Indicadores > Nuevo indicador'),
 STEP(6, 'Levanta el mapa de lo que nadie escribió', [
  'En «Mapa de lo que nadie escribió» añade una fila por cada cosa que se sabe y no está escrita en ningún sitio. Anota quién lo sabe, dónde se usa y cuántas personas lo saben.',
  'Marca como crítico lo que, si esa persona falta, para el trabajo. Más adelante, para cada opción de diseño, indica qué pasa con la fila: se queda en la persona, pasa al sistema o se pierde.'],
  'que el contador del ámbito muestra cuántas filas críticas dependen de una sola persona, y que se pone en rojo al llegar al umbral.', 'Mapa de lo que nadie escribió > Añadir fila'),
 STEP(7, 'Añade las iniciativas', [
  'Desde el ámbito pulsa «Añadir iniciativa». Pon su alcance, su fase, el dueño operativo y qué hace la tecnología: acelera, automatiza o aumenta, o ninguna.',
  'Indica si ataca la restricción. Solo los habilitadores y las obligaciones legales pueden no atacarla.'],
  'que cada iniciativa tiene dueño con nombre y que ninguna tecnología está en piloto sin cumplirse la regla de entrada.', 'Ámbitos e iniciativas > Añadir iniciativa'),
 STEP(8, 'Registra las puertas', [
  'En Puertas pulsa «Registrar decisión». Elige la iniciativa y la puerta, escribe la fecha en que se firmaron los criterios y la fecha de la decisión.',
  'Rellena las cinco preguntas si es la puerta de diseño, la salida elegida, la firma del patrocinador y la contrafirma de alguien ajeno al equipo. Marca si Medición certifica los datos.',
  'En un piloto, anota también el criterio de parada: qué resultado lo detiene antes de tiempo.'],
  'que la tarjeta de la decisión dice «Criterios firmados antes». Si la fecha de los criterios es posterior a la de la decisión o está vacía, el gestor lo marca como un voto secreto: un criterio escrito después de ver el dato.', 'Puertas > Registrar decisión'),
 STEP(9, 'Da de alta tus agentes', [
  'En Agentes pulsa «Nueva ficha» y rellena la ficha. Fija el nivel actual, el nivel de entrada y el techo. Si el agente decide sobre derechos de las personas, márcalo: el techo queda en el nivel 2.',
  'Después marca los controles que ya existen para su nivel. Un límite solo cuenta si lo aplica el sistema; una instrucción escrita al agente no es un control.',
  'Cada ficha es la base de una entrada del inventario único de agentes, sistemas y casos de uso.'],
  'que no aparece ninguna alerta de «faltan controles» para el nivel en que opera y que la próxima revisión tiene fecha.', 'Agentes > Nueva ficha'),
 STEP(10, 'Lee las alertas cada semana', [
  'Vuelve al Resumen y trabaja la lista de arriba abajo. Pulsa una alerta para ir a su sección. Cuando la resuelvas desaparece sola.',
  'Después abre Camino, elige el ámbito y mira qué pasos de la fase actual faltan. Los pasos con la etiqueta «auto» se marcan cuando tus datos lo cumplen; los de «manual» los confirmas con una casilla. Pulsa una fase de la fila de arriba para ver sus pasos y su puerta.'],
  'que el Resumen dice «Nada pendiente según las reglas del método». Es una buena señal, pero no una garantía: el gestor solo ve lo que le has contado.', 'Sección Resumen'),
])
SECS.append(('tutorial', 'Tu primer programa en diez pasos', pasos))

SECS.append(('secciones', 'Qué hace cada sección', TBL(['Sección', 'Para qué sirve', 'Qué se guarda'], [
 ['Resumen', 'Ve el estado de cada ámbito de un vistazo y las alertas pendientes.', 'Nada: lo calcula con lo demás.'],
 ['Camino', 'Muestra las cinco fases con su puerta y lo que el documento pide en cada paso, para el ámbito que elijas.', 'Los pasos que marcas a mano. Los demás los comprueba solo con tus datos.'],
 ['Ámbitos e iniciativas', 'Define los ámbitos, su restricción, su madurez y las iniciativas que cuelgan de cada uno.', 'Nombre, objetivo de negocio, restricción, patrocinador, fase, madurez y evidencia. Para cada iniciativa, alcance, fase, tecnología, dueño, valor previsto (horquilla y plazo) y dueño del beneficio.'],
 ['Puertas', 'Registra cada decisión con sus criterios, firmas y salida.', 'Fechas, salida, cinco preguntas, firma, contrafirma y certificación de datos.'],
 ['Mapa de lo no escrito', 'Lleva el conocimiento que no está escrito y su concentración.', 'Qué se sabe, quién, dónde, número de personas, si es crítico y qué pasa con cada opción.'],
 ['Roles', 'Dice quién es quién en cada ámbito y avisa de las combinaciones que no se admiten.', 'Nombres del patrocinador, la dirección del programa, la medición, la contrafirma, la segunda línea, la adopción, quien despliega, el dueño de los datos y quien defiende a quien recibe el servicio, y si la representación legal está informada.'],
 ['Indicadores', 'Mide con línea base, objetivo o suelo, y calcula el delta.', 'Qué mide (objetivo de negocio o uno de los tres elementos), línea base, valor actual, objetivo o suelo, variación normal y peso. Los dos deltas se leen aparte.'],
 ['Agentes', 'Mantiene la ficha de cada agente y sus controles por nivel.', 'Los once campos de la ficha, el nivel, el techo y los controles marcados.'],
 ['Ajustes', 'Cambia el nombre, el umbral y exporta los datos.', 'Nombre del programa y umbral.']])))

SECS.append(('alertas', 'Las alertas, una a una', TBL(['Alerta', 'Qué significa', 'Qué hacer'], [
 ['Combinación de roles que no se admite', 'El patrocinador contrafirma su propia decisión, es también el responsable de medición, el responsable de adopción es quien despliega la herramienta, o el dueño del beneficio es el de la solución.', 'Cambia una de las dos personas. El control de una puerta no puede quedar en las mismas manos.'],
 ['Faltan roles con nombre', 'El ámbito está en diseño o más allá y no tiene responsable de medición o persona que contrafirma. En escala, también responsable de adopción.', 'Nómbralos en el formulario del ámbito. Sin ellos no se pueden dar las firmas que pide el método.'],
 ['Falta escribir el objetivo de negocio', 'El ámbito no tiene escrito el resultado que se quiere cambiar.', 'Escríbelo con quien dirige: resultado, horizonte y quién responde. La restricción se nombra respecto a él.'],
 ['Sin indicador del objetivo de negocio', 'El ámbito está en diseño o más allá y ningún indicador mide el objetivo.', 'Crea un indicador de resultado con su línea base antes de seguir.'],
 ['Las palancas avanzan y el resultado no se mueve', 'El delta de las palancas pasa del 50 % y el del objetivo no llega al 20 %.', 'Revisa si lo que se mueve es lo que ataca la restricción. Un programa ordenado puede no servir al negocio.'],
 ['El resultado mejora y una palanca cae', 'El delta del objetivo pasa del 50 % y el de las palancas no llega al 20 %.', 'Lo ganado se queda sin quien lo sostenga. Recupera la palanca antes de escalar.'],
 ['Falta el valor y su dueño', 'Una iniciativa que ataca la restricción no tiene horquilla en el árbol de valor o dueño del beneficio.', 'Escribe cuánto vale resolverla, aunque sea una horquilla ancha, y quién responde de ese beneficio en el negocio.'],
 ['Falta nombrar la restricción', 'El ámbito está en diseño o más allá y no tiene restricción escrita.', 'Nómbrala con el patrocinador o devuelve el ámbito al diagnóstico.'],
 ['Regla de entrada sin cumplir', 'Hay un acelerador en piloto y algún elemento está por debajo del nivel 2.', 'Sube ese elemento al nivel 2 o saca la tecnología del servicio hasta que lo esté.'],
 ['Conocimiento concentrado', 'Las filas críticas que dependen de una sola persona alcanzan el umbral.', 'Documenta y reparte esas filas antes de seguir, o decide por escrito quién las protege.'],
 ['Indicador de guarda bajo su suelo', 'Un indicador de guarda está peor que su suelo.', 'No pases ninguna puerta hasta recuperarlo, o cambia el diseño.'],
 ['Criterios no firmados antes', 'La puerta no tiene fecha de criterios o es posterior a la decisión.', 'Fija los criterios y repite la puerta con ellos. Una vez como máximo.'],
 ['Puerta sin firma y contrafirma', 'Se pasa sin la firma del patrocinador o sin la contrafirma de una persona ajena.', 'Completa las dos firmas antes de dar la puerta por pasada.'],
 ['Sin datos certificados', 'Medición no ha certificado los datos de una puerta que pasa.', 'Pide a Medición que certifique y marca la casilla.'],
 ['Agente por encima de su techo', 'El nivel actual supera el techo fijado, o supera el 2 cuando decide sobre derechos.', 'Baja el nivel hasta el techo o lleva la subida a una puerta de autonomía.'],
 ['Faltan controles', 'Al nivel en que opera el agente le faltan controles de la lista.', 'Pon el control o baja el nivel hasta el que sí cumples.'],
 ['Revisión vencida', 'La fecha de revisión del agente ya pasó.', 'Revisa el agente y fija la siguiente fecha. Repite los casos de prueba si cambió algo.'],
 ['Agente sin dueño', 'La ficha no tiene una persona con nombre responsable.', 'Escribe quién responde de lo que hace.']])))

SECS.append(('rutinas', 'Tres rutinas que funcionan', '<div class="grid3">'
 + '<div class="card"><h3>Cada semana, cinco minutos</h3>' + UL(['Abre el Resumen y lee las alertas.', 'Actualiza el valor actual de los indicadores.', 'Revisa que no haya agentes sin dueño o con la revisión vencida.']) + '</div>'
 + '<div class="card b"><h3>Antes de una puerta</h3>' + UL(['Comprueba que los criterios están firmados antes de ver el dato.', 'Pide a Medición que certifique los datos.', 'Reúne firma y contrafirma. Anota las cinco preguntas.']) + '</div>'
 + '<div class="card"><h3>Cuando cambia un agente</h3>' + UL(['Si cambia el modelo, las herramientas o los permisos, repite los casos de prueba.', 'Revisa los controles del nivel en que opera.', 'Anota la nueva fecha de revisión.']) + '</div></div>'))

SECS.append(('faq', 'Preguntas frecuentes', '<dl class="faq">'
 + ''.join('<dt>%s</dt><dd>%s</dd>' % (q, L(a)) for q, a in [
  ('¿Puedo compartirlo con el equipo?', 'Se comparte desde el menú de la propia página. Ahora mismo el gestor no distingue roles: quien pueda escribir puede editar y borrar todo. Para un equipo, conviene dar acceso solo de lectura a la mayoría.'),
  ('¿Dónde se guardan mis datos?', 'En la base de datos de la página, ligada a tu cuenta. Puedes exportarlos en JSON desde Ajustes cuando quieras.'),
  ('¿Qué pasa si borro algo?', 'El borrado es definitivo y pide confirmación. Exporta antes si dudas.'),
  ('¿Qué calcula el gestor por mí?', 'El delta, el estado de cada indicador, el recuento de filas críticas, la regla de entrada, el techo de un agente y todas las alertas.'),
  ('¿Qué hago si no tengo línea base?', 'No escribas un valor estimado. Deja el indicador sin datos y mide antes de cambiar nada. Una línea base estimada se puede defender o atacar según convenga.'),
  ('¿Por qué no me deja marcar la puerta como pasada?', 'No lo impide: te avisa. La decisión es del patrocinador. El gestor solo deja visible lo que no cumple las reglas.')])
 + '</dl>'))

SECS.append(('limites', 'Lo que el gestor no hace todavía', UL([
 'No tiene usuarios ni roles por persona.',
 'No calcula el modelo económico ni el valle de cada iniciativa.',
 'No sustituye al registro de decisiones del programa: guarda las puertas, no todas las decisiones.',
 'No se ha probado con un programa real. Los valores de partida, como el umbral de tres filas, son propuestas del método y no están probados con números reales.'])))

gl = ''.join('<article class="gentry" id="g-%s"><h3>%s</h3><p>%s</p><a class="back" href="#" data-back>Volver</a></article>' % (gid, esc(t), esc(d)) for gid, (t, vs, d) in sorted(GLOS.items(), key=lambda kv: kv[1][0].lower().replace('á', 'a').replace('í', 'i').replace('é', 'e')))
SECS.append(('glosario', 'Glosario', '<p class="lead">%d términos. Cada uno aparece enlazado en el texto del manual.</p><div class="ggrid">%s</div>' % (len(GLOS), gl)))

toc = ''.join('<a href="#%s">%s</a>' % (i, t) for i, t, _ in SECS)
body = ''.join('<section id="%s" class="sec"><h2>%s</h2>%s</section>' % (i, t, h) for i, t, h in SECS)

CSS = """
/* Concepto: manual de campo. Texto en columna estrecha, con las formas de hoja de la marca y los términos del glosario subrayados con puntos. */
:root{--bg:#F5F7F5;--surface:#FFFFFF;--ink:#1F1D1A;--muted:#58605C;--line:#DCE1DD;--green:#2C6D3F;--green-soft:#E3EEE6;--terra:#B5512A;--terra-soft:#F6E6DD;--alb:#8A6508;--alb-soft:#F6EACB;--ink-soft:#ECEEED;--serif:'EB Garamond',Georgia,serif;--sans:'Public Sans',system-ui,sans-serif;--leaf:6px 0 30px 0;--leafb:0 6px 0 30px}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#131614;--surface:#1B1F1C;--ink:#EDEEE9;--muted:#A3ABA6;--line:#323835;--green:#7CC490;--green-soft:#1F3226;--terra:#E68F68;--terra-soft:#3A2519;--alb:#E2B957;--alb-soft:#3A3119;--ink-soft:#262A27;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#131614;--surface:#1B1F1C;--ink:#EDEEE9;--muted:#A3ABA6;--line:#323835;--green:#7CC490;--green-soft:#1F3226;--terra:#E68F68;--terra-soft:#3A2519;--alb:#E2B957;--alb-soft:#3A3119;--ink-soft:#262A27;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.6;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 64px;scroll-behavior:smooth}
.wrap{max-width:920px;margin:0 auto}
.top{padding-block:28px 8px}
.kick{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--green);font-weight:600;margin-top:14px}
.brand{font-family:var(--serif);font-size:26px;line-height:1}.brand b{color:var(--green);font-weight:500}
h1{font-family:var(--serif);font-weight:400;font-size:clamp(38px,7vw,60px);line-height:1.02;margin:6px 0 10px;text-wrap:balance}
.sub{color:var(--muted);max-width:60ch;margin:0 0 20px}
nav.toc{display:flex;flex-wrap:wrap;gap:6px;padding-block:10px;position:sticky;top:env(safe-area-inset-top,0px);background:var(--bg);z-index:5;border-bottom:1px solid var(--line)}
nav.toc a{font-size:13px;text-decoration:none;color:var(--muted);padding:5px 12px;border-radius:0 12px 0 5px;background:var(--ink-soft);white-space:nowrap}
nav.toc a:hover{color:var(--green)}
h2{font-family:var(--serif);font-weight:400;font-size:clamp(28px,4.5vw,38px);line-height:1.1;margin:0 0 12px;text-wrap:balance}
h3{font-family:var(--serif);font-weight:500;font-size:22px;line-height:1.2;margin:0 0 6px;text-wrap:balance}
.sec{padding-block:36px 8px;scroll-margin-top:64px}
p{margin:0 0 12px;max-width:68ch}ul{margin:0 0 12px;padding-left:20px;max-width:68ch}li{margin-bottom:6px}
.lead{color:var(--muted)}
a.gl{color:inherit;text-decoration:underline dotted var(--green);text-underline-offset:3px;text-decoration-thickness:1.5px}
a.gl:hover,a.gl:focus-visible{color:var(--green);text-decoration-style:solid}
a:focus-visible,button:focus-visible{outline:2px solid var(--green);outline-offset:2px}
.note{background:var(--green-soft);padding:14px 18px;border-radius:var(--leaf);max-width:68ch}
.step{display:grid;grid-template-columns:56px 1fr;gap:6px 16px;padding:22px 0;border-top:1px solid var(--line);scroll-margin-top:64px}
.step .num{font-family:var(--serif);font-size:44px;line-height:1;color:var(--green)}
.step>div:last-child{min-width:0}
.where{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
.check{background:var(--alb-soft);padding:10px 16px;border-radius:0 14px 0 5px;max-width:68ch;font-size:15px}
.scroll{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:14.5px;min-width:560px}
th{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);text-align:left;padding:8px 12px;border-bottom:2px solid var(--ink)}
td{padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
td:first-child{font-weight:600;white-space:normal}
.grid3{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(min(100%,250px),1fr))}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--leaf);padding:18px 20px 12px;min-width:0}.card.b{border-radius:var(--leafb)}
.faq dt{font-family:var(--serif);font-weight:500;font-size:21px;margin-top:18px}.faq dd{margin:4px 0 0;max-width:68ch}
.ggrid{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(min(100%,380px),1fr))}
.gentry{background:var(--surface);border:1px solid var(--line);border-radius:var(--leaf);padding:16px 20px 14px;scroll-margin-top:72px;min-width:0}
.gentry:nth-child(even){border-radius:var(--leafb)}
.gentry:target{border-color:var(--green);background:var(--green-soft)}
.gentry p{margin:0 0 8px;font-size:15px}
.back{font-size:13px;color:var(--muted);text-decoration:none;border:1px solid var(--line);padding:3px 12px;border-radius:0 10px 0 4px;display:inline-block}
.back:hover{color:var(--green);border-color:var(--green)}
footer{margin-top:48px;color:var(--muted);font-size:13px;border-top:1px solid var(--line);padding-top:16px}
@media (max-width:520px){.step{grid-template-columns:1fr}.step .num{font-size:34px}}
@media (prefers-reduced-motion:reduce){body{scroll-behavior:auto}}
"""

PAGE = """<title>Synergós Champion</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Public+Sans:wght@400;500;600&display=swap">
<style>%s</style>
<div class="wrap">
<header class="top"><div class="brand">Syner<b>gós</b></div><div class="kick">Manual del gestor y glosario</div><h1>Synergós Champion</h1><p class="sub">Cómo llevar un programa con el método, paso a paso, con el glosario de cada término. Pensado para quien lo usa por primera vez.</p></header>
<nav class="toc" aria-label="Secciones del manual">%s</nav>
<main>%s</main>
<footer>Versión 1.2, al día con el método 2.1 y su anexo de roles · noviembre de 2026 · Alejandro Berruezo. Documento de trabajo del método Synergós.</footer>
</div>
<script>
(function(){
var prev=null;
document.addEventListener('click',function(e){
  var a=e.target.closest('a.gl');
  if(a){prev=window.scrollY}
  var b=e.target.closest('[data-back]');
  if(b){e.preventDefault();if(prev!=null){window.scrollTo({top:prev,behavior:'smooth'})}else{history.back()}}
});
})();
</script>
""" % (CSS, toc, body)

open('/home/user/MiLinkedIn/synergos/app/manual-gestor.html', 'w', encoding='utf-8').write(PAGE)
n_links = len(re.findall(r'class="gl"', PAGE))
used = set(re.findall(r'href="#g-([a-z\-]+)" title', PAGE))
print('enlaces', n_links, 'términos usados', len(used), 'de', len(GLOS), 'sin uso:', sorted(set(GLOS) - used))
