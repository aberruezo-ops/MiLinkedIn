# Ronda 2, scaleup de software: evaluación de Synergós 2.1

Qué he leído: capítulos 1 a 3 y 5 a 14 (partes I a III), el capítulo 18 entero, el anexo C, la tabla "Qué es obligatorio según alcance" y la síntesis de la ronda 1. No he leído los módulos 1 a 24 salvo por sus menciones en esos textos, ni los anexos D e I, y de la infografía solo he visto la cabecera del script, no sus textos. Todo lo que digo de los módulos es por referencia. Lo que sigue es la lectura de un perfil plausible, no una validación.

## 1. Mi empresa en tres frases (perfil inventado)

Somos una scaleup de software de unos 300 empleados que vende una plataforma de facturación y cobros a pymes en varios países. Tenemos equipos de producto autónomos, casi nadie con título de jefe y poca tolerancia a procesos que no se puedan explicar en una pantalla. La transformación que tenemos entre manos es meter IA en el trabajo diario (ya la usa casi todo el mundo, sin orden ni inventario) y, sobre todo, decidir si un agente puede asumir una parte del soporte a clientes, donde crecemos más rápido que la plantilla.

## 2. Lo que me aportaría el método, de lo más a lo menos valioso

1. **El mapa de lo que nadie escribió (capítulo 9, anexo B) y la tercera pregunta de la puerta (capítulo 11).** Es lo único que no tengo. Mi soporte depende de cinco o seis personas que "saben" qué cliente es en realidad un problema de integración y no de facturación. Si pongo un agente sin ese mapa, repito el caso de los dos ejemplos públicos del capítulo 18. Es útil, barato (el ejemplo del capítulo 9 habla de dos semanas de una persona, cifra ilustrativa que el propio texto dice que no vale para un área grande) y se explica en una frase.
2. **Elegir restricción antes que herramienta (principio 1, capítulo 9).** Las dos preguntas sobre el flujo (dónde se acumula la cola, qué pasa si se duplica la capacidad ahí) las puedo usar mañana. Mi tendencia es comprar la herramienta y ya veremos. Esto me obliga a nombrar un cuello y un resultado de negocio.
3. **Línea base con variación normal y criterios del piloto escritos antes (capítulos 12 y 18).** "Un cambio menor que la variación normal no cuenta" es el mejor argumento que he leído contra mi propia costumbre de celebrar una semana buena. La regla de que el piloto escribe qué decisión cambia su resultado es oro: la mitad de mis experimentos de IA no cambiarían ninguna decisión.
4. **Las cuatro verbos, con "eliminar" primero (capítulo 11, pregunta 2).** Mi equipo automatiza procesos que no deberían existir. Preguntar primero si la tarea debe existir me ahorra más dinero que cualquier modelo.
5. **Retirar como salida legítima, criterio de parada y revisión a noventa días (capítulo 12).** Mis pilotos no mueren, se quedan abiertos. Es una regla que adopto tal cual.
6. **El tope de pocas cosas a la vez (principio 3) y la regla de entrada (nivel 2 de madurez).** Útil para frenar a mis equipos, que quieren probar tres agentes a la vez. Ojo, la regla de entrada solo me sirve si la evaluación dura horas, como promete el texto.
7. **Coste por tarea completada y coste fuera de factura (capítulo 18).** Mi factura de modelos es pequeña; lo caro es la revisión humana y el retrabajo. Esta cuenta es la que no hacemos.
8. **Derecho a parar con respuesta en el día y tabla de quién decide qué (capítulo 18).** En una empresa sin jerarquía, que el soporte pueda decir "esto no lo usamos en este caso" sin pedir permiso es natural. Lo que me falta es la tabla de una página, que no tengo.
9. **Uso informal: consulta anónima y vía corta para herramientas generales (capítulo 18).** Es mi situación real. La garantía de no sanción por contar un uso es la pieza que me hace falta.

## 3. Lo que no usaría o me sobra

- **El comité de puertas con cuatro firmantes y nueve oídos (capítulo 18).** Es lo que más me chirría. Yo decido con dos o tres personas en media hora. Usaría la versión de programa acotado: firma del patrocinador y contrafirma de alguien ajeno al equipo. Aquí hay un detalle práctico: el método pide que la contrafirma venga de la "segunda línea o finanzas", y yo no tengo segunda línea de riesgos. Tendría que ser la persona de finanzas o el responsable de seguridad. Funciona, pero conviene decirlo, porque un texto escrito para una organización con tres líneas de defensa obliga a una scaleup a inventarlas.
- **Las cinco preguntas completas en cada iniciativa pequeña.** El propio método admite que no lo ha contrastado (pregunta abierta del capítulo 11). Yo haría la versión de media página y solo para lo que toque a clientes o a plantilla.
- **La escala de madurez de cuatro niveles aplicada a tres elementos más gobierno, y el anexo D.** Me suena a diagnóstico de consultora. Lo reduciría a: ¿hay alguien con nombre, una forma acordada y datos autorizados? Si sí, entra.
- **Los módulos de sistema obligatorios (aportaciones, tres necesidades, cinco puntas, huella y dependencia).** Por lo que leo en la tabla, para una iniciativa "de sistema" son siete líneas de anexo más nueve módulos obligatorios. No los he leído, así que no los descarto, pero no los pondría en marcha el primer año.
- **La representación legal oída antes (capítulo 18).** Probablemente no aplica en mi caso por tamaño y país, pero no estoy seguro de qué obliga en cada jurisdicción, y eso lo tendría que mirar un jurista, no yo.
- **El girasol (capítulo 7).** El propio texto reconoce que es una imagen y no un argumento. Para mí, adorno. No me molesta, pero tampoco lo voy a contar al equipo.

## 4. Cómo lo aplicaría yo: mi itinerario

### Nivel 1: una iniciativa completa, un agente de primer nivel en soporte (ejemplo inventado)

Alcance: de flujo, no de sistema. Tocamos un proceso de principio a fin (entrada de ticket, clasificación, respuesta, escalado), no el modelo de negocio.

**Antes de empezar (semana 0).** Yo, como patrocinadora, escribo el objetivo de negocio en tres líneas: bajar el coste por ticket resuelto sin bajar la satisfacción y absorber el crecimiento sin contratar al ritmo actual. Declaro por escrito que se vale reducir contratación futura y que no se prevé despedir (esto último es mi decisión como empresa; el método no me obliga a decirlo, y la síntesis de la ronda 1 propone una declaración de intención de plantilla, que yo aquí firmaría porque sin ella el equipo no hablaría).

**Fase 1, diagnóstico (unas semanas, a la vez estas cuatro cosas).**
- Una persona de operaciones observa el trabajo en el puesto de soporte y dibuja el flujo real. A la vez, esa misma persona levanta el mapa de lo que nadie escribió con las preguntas por las grietas (el propio método dice que salen de las mismas visitas). Hablaría con la persona a la que todos acuden y con la última que entró.
- Finanzas y datos miden la línea base: tiempo hasta primera respuesta, tickets reabiertos, coste por ticket cerrado, satisfacción, y para personas el indicador por defecto del capítulo 18 (casos fuera de patrón resueltos sin escalar) y la carga percibida. Con mínimo y máximo de los últimos meses.
- Consulta anónima de qué IA usa ya soporte, a la vez que lo anterior.
- Puerta: restricción nombrada (mi hipótesis, falsable: el cuello está en la clasificación y la búsqueda de contexto, no en escribir la respuesta), línea base, mapa con compromiso de uso firmado por mí.

**Fase 2, diseño.** Rediseño del trabajo antes de elegir modelo: qué decide cada rol y qué deja de hacer. Decisión de una página con las cinco preguntas. Dos opciones sobre la mesa: agente que responde las sencillas, o agente que clasifica y propone y la persona decide. El mapa dirá qué opción pierde menos. Criterios del piloto firmados: delta mínimo, guardas (satisfacción, reaperturas), criterio de parada, noventa días máximo, cómo se deshace. Casos de prueba preparados por el equipo de soporte, con los raros.

**Fase 3, piloto.** En un mercado o una cola con rotación alta y casos raros, no en la cola más fácil. Con una cola de comparación sin agente. Revisión a noventa días. Los casos de prueba se repiten cada vez que cambie el modelo.

**Fase 4, escala.** Por colas, con minipuerta cada etapa. Una persona responsable de adopción con tiempo y dos referentes por cola. Aquí cambiar evaluación e incentivos de soporte, que hoy se miden por tickets cerrados.

**Fase 5, sostenimiento.** Dueño operativo, presupuesto recurrente y dos periodos de medición sin el equipo del programa.

### Nivel 2: todo el programa con varios ámbitos a la vez (ejemplo inventado)

Cuatro ámbitos: soporte, onboarding de clientes nuevos, ingeniería (asistentes de código y revisión) y cobros internos. No arrancaría los cuatro a la vez. Haría esto:

- **Una sola oficina pequeña de medición y conocimiento,** de dos o tres personas a tiempo parcial, que sirva a todos los ámbitos. Es lo que el método llama programa amplio, y la parte que más se parece a mi realidad.
- **Un ciclo por ámbito, escalonados.** Soporte primero (más valor y más riesgo), onboarding después, aprovechando lo aprendido en el sostenimiento de soporte. Ingeniería la dejaría casi fuera del tronco: es herramienta del equipo y basta con la vía corta de herramientas de uso general. Cobros internos, en el tercer ciclo.
- **Un inventario único** desde el primer mes, que es lo que me falta hoy, y una tabla de quién decide qué de una página.
- **Tope de aceleradores por ciclo** respetado: en soporte, solo el agente. Nada más a la vez.
- **Un comité de puertas de tres o cuatro personas,** no de nueve oídas. Las objeciones por escrito, sí; el paseo por todas las áreas antes de cada puerta, no, salvo cuando toque a clientes o plantilla.

## 5. Lo que no entiendo o me suena a jerga

- **"Elemento" y "acelerador".** Hasta que lo leí dos veces no tuve claro que el elemento tecnología es una capacidad de la organización y el acelerador es una herramienta concreta. Es una distinción útil, pero el nombre despista.
- **"Las preguntas del comité" y "las preguntas por las grietas".** Dos juegos de preguntas con nombres casi iguales en el mismo capítulo 9.
- **"Delta" y las dos cifras (objetivo y palancas).** El concepto se entiende en un ejemplo. Dicho en abstracto suena a hoja de cálculo.
- **"Indicador de guarda".** Lo entiendo (un suelo que no se puede perforar), pero en mi equipo lo llamaríamos simplemente "límite" o "no romper".
- **"Dueño del beneficio", "dueño operativo", "dueño de los datos", "dueño de la solución".** Cuatro dueños. El texto avisa de que el dueño sin apellido es el operativo, pero en una empresa pequeña son la misma persona y la distinción cuesta explicarla.
- **"Segunda línea" y "tres líneas".** Es lenguaje de una organización grande y regulada. Aquí no tenemos nada que se llame así.
- **"Nivel" para madurez y "nivel" para autonomía.** La síntesis de ronda 1 ya lo señala; para mí es más grave de lo que parece, porque son números que se dicen en voz alta en la misma reunión.
- **"Marcha atrás", "extensión sin causa documentada".** Lo segundo es honesto, pero es lenguaje de método y no de empresa.
- **"Girasol" y "137,5 grados".** No lo necesito, y lo digo con respeto.

## 6. Los primeros noventa días

**El lunes.**
1. Escribo el objetivo de negocio en tres líneas y lo comparto.
2. Nombro a una persona de operaciones como responsable del diagnóstico de soporte, con tiempo reservado real, no "cuando pueda".
3. Lanzo la consulta anónima de uso de IA, con la promesa explícita de no sanción.
4. Pido a finanzas que dejen escrita la línea base de soporte con su variación normal. No cambio nada hasta tenerla.

**Qué me costaría (sin cifras).** El tiempo de una persona de operaciones y otra de datos durante buena parte del trimestre, algunas horas de la persona más sabia de soporte y de la más nueva (que es justo el recurso escaso), mi propio tiempo para firmar y para decir en voz alta que retirar es legítimo, y una persona de finanzas como contrafirma. No hay herramienta que comprar en estos noventa días, y eso en sí mismo me incomoda: mi cultura premia lanzar cosas. El método dice que los cien días se financian como gasto de diagnóstico, y lo creo.

**Señal de que va bien.** Que alguien del equipo de soporte me diga, sin que se lo pida, que el mapa recogió algo que ya sabía y nadie había apuntado. O que cancelemos o reorientemos una idea de IA antes de gastar en ella porque el mapa o la línea base la contradicen. Señal de que va mal: que el diagnóstico se alargue sin puerta, o que el equipo hable del programa como "lo de dirección".

## 7. Lo que falta para mi tipo de empresa

- **Una versión corta de verdad, hecha para ir rápido.** El método tiene el recorte por alcance, pero la tabla "Qué es obligatorio" ya son más de una veintena de filas para un alcance de flujo, y varias de las "obligatorias" arrastran un módulo entero. Necesito una página que diga: estas siete cosas, en este orden, y nada más durante el primer ciclo. La propia síntesis de la ronda 1 lo apunta desde otro rol (finanzas) y desde mi tipo de empresa lo sufro más: no tengo oficina de transformación.
- **Ritmo.** Cinco fases con puertas secuenciales suenan a ritmo de trimestres. Mis ciclos de producto son de semanas. El método dice que un piloto puede ser de noventa días como máximo, pero no hay una versión de ciclos de dos o cuatro semanas con un criterio de parada igual de exigente. No sé si el método aguanta ese ritmo; lo veo plausible pero sin probar.
- **IA dentro del producto que vendemos.** El método habla de transformar la organización y el servicio internos. Si el agente forma parte de lo que vendo (y para una empresa de software será pronto el caso), faltan clientes como parte de la puerta, contratos, responsabilidad frente a terceros y la gestión de cambios de modelo del proveedor frente a un SLA. El capítulo 18 toca el cambio de versión del modelo, pero desde dentro.
- **Ingeniería como ámbito propio.** Los asistentes de código son el mayor cambio de mi empresa y el método los trata de pasada (la vía corta de herramientas de uso general y algún estudio citado en el capítulo 18). No hay una ficha de qué medir en un equipo de producto (calidad, deuda, tiempos de revisión).
- **Equipos distribuidos y de varios países.** El método habla de visitas al puesto y conversaciones. No dice nada sobre cómo se levanta un mapa con equipos en remoto de distintas zonas horarias.
- **Quién lo dirige, sin oficina de transformación.** El método presupone un equipo del programa con siete funciones. En mi empresa esa función la haría una persona, quizá dos, que además tiene otro trabajo.
- **Coste del propio método.** Ya lo dijeron en la ronda 1 desde finanzas y lo mantengo con más fuerza: me cuesta decidir sin saber cuántas semanas de cuántas personas pide el primer ciclo. El propio método lo reconoce en el capítulo 18 ("no doy un orden de magnitud").

## Cómo pesan los hallazgos de la ronda 1 desde mi empresa

- **Más grave en mi caso:** que el método no se aplica a sí mismo y no da coste (propuesta 12). Para una scaleup es el primer filtro. Y el número de piezas obligatorias por alcance (propuesta 8 sobre alcance e importe): lo puntual no arrastra tanto como en una administración, pero lo de flujo arrastra demasiado.
- **Igual de grave:** el mapa ampliado y su protección (propuesta 6). Mi mapa de soporte va a tocar a cinco personas muy identificables, y el riesgo de exponerlas existe aunque no haya sindicato.
- **Menos grave:** la propuesta 11 (sector público), la 9 (cribado legal) en lo que no sea datos de clientes, y la propuesta 5 en lo jurídico. Una lista de piezas no retirables (propuesta 1) me parece razonable si es corta (cuatro cosas) y no la sentiría como burocracia. La contrafirma (propuesta 7) la resolvería con finanzas, no con una segunda línea que no tengo.
- **Donde no estoy seguro:** el delta como media que compensa (propuesta 2). Yo usaría pocos indicadores y los leería uno a uno, así que el problema me afecta menos; en un programa grande sí lo vería grave.

## 8. Veredicto

**Adoptaría una parte.** Me quedo con el diagnóstico (restricción, línea base con variación normal, mapa de lo que nadie escribió), la decisión de una página con criterios, criterio de parada y marcha atrás antes del piloto, el derecho a parar y la consulta anónima del uso informal. Dejo fuera, de entrada, el comité completo, la escala de madurez en cuatro niveles, los módulos obligatorios de sistema y la parte de gobierno que supone una organización con tres líneas de defensa. No lo adoptaría entero porque, tal como está, necesita más gente y más tiempo del que yo le puedo dar, y porque el propio método dice que nadie lo ha aplicado completo.

**Una frase para el comité de dirección:** "Vamos a usar de Synergós lo que nos obliga a entender el trabajo antes de comprar el agente y a poder retirarlo sin vergüenza si no funciona, y el resto lo probamos solo cuando el primer ciclo nos diga que lo necesitamos."

**Lo que más me aportaría:** una versión de una página con las siete piezas mínimas y un orden de magnitud de esfuerzo, aunque sea una horquilla ancha.
