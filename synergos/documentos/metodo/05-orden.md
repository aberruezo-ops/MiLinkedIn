## 18. El orden: crecer a la vez

El orden es lo que hace que los tres elementos avancen al mismo compás. Además de las fases y sus puertas, que ocupan la Parte III, agrupa la estrategia, el gobierno, el modelo económico, la medición, la madurez y el dimensionamiento. El capítulo explica con ellos el delta, la regla de entrada y la marcha atrás. Es la parte menos vistosa del método y la que decide si todo lo demás llega a algún sitio.

### Estrategia

Rumelt describió en 2011 el núcleo de una buena estrategia en tres partes: un diagnóstico que nombra el problema crítico, una política guía que dice cómo se va a abordar y un conjunto de acciones coherentes entre sí. A. G. Lafley y Roger Martin lo formularon en 2013 como dos elecciones: dónde jugar y cómo ganar. Lo que tienen en común es que una estrategia es, sobre todo, lo que se decide no hacer.

**El papel de la dirección.** Desde la versión 1.7, la estrategia de IA tiene dueño en el órgano que dirige la organización. Ese órgano hace tres cosas que nadie más puede hacer: decide para qué se quiere la IA (capítulo 17), fija cuánto riesgo se acepta y recibe cada periodo de medición el mismo cuadro de indicadores que ve el comité de puertas. Delegar la estrategia de IA entera en el área de tecnología es una forma de no tenerla.

**Un arranque a cien días.** Un programa nuevo se compromete solo a lo que cabe en ese plazo: el diagnóstico con su mapa, el inventario de lo que ya se usa (también lo no autorizado), los derechos de decisión escritos, la línea base de los indicadores y la primera puerta. Los cien días se financian como gasto de diagnóstico, porque todavía no existe modelo económico. A partir de ahí se compromete el resultado de la siguiente puerta y se reserva, sin comprometer resultados, una horquilla de presupuesto para las fases siguientes, que cada puerta libera o devuelve. La razón es la misma que el módulo 17 da para los plazos. No doy un orden de magnitud del esfuerzo del equipo en esos cien días porque no tengo uno que pueda defender: lo estima cada programa y lo anota como supuesto.

*Señal de fallo:* la cartera crece sin que nadie retire nada. Un programa que solo suma iniciativas no tiene estrategia; tiene una lista.

### Gobierno

Un comité de puertas con criterios previos, derechos de decisión escritos y un registro de riesgos y de decisiones. Peter Weill y Jeanne Ross mostraron en 2004 que las organizaciones que deciden con claridad quién decide qué sobre la tecnología obtienen más valor de ella. La claridad importa más que el modelo concreto.

{{img:fig-comite.png|16}}

**Tres capas de responsabilidad.** El gobierno fija los criterios, los derechos de decisión y las puertas. La gestión los aplica, los mide y los corrige. El uso es de quien trabaja con la herramienta cada día, que es quien primero ve cuándo falla. Propuesta de la versión 1.4: la capa de uso tiene derecho a parar, por escrito y sin represalias, y ese derecho se anota en la misma tabla que los demás derechos de decisión. Sin él, que la persona decida se queda en una frase.

**El comité de puertas.** Desde la versión 1.8 su composición está escrita. Intervienen cuatro personas y otras son oídas antes, por escrito.

| Quién | Papel en la puerta |
|---|---|
| El patrocinador | Decide y firma |
| El dueño operativo | Decide con el patrocinador |
| El responsable de medición | Certifica los datos, no la decisión |
| Una persona ajena al equipo del programa (sin interés en la iniciativa: segunda línea o finanzas) | Contrafirma |
| Quien hace el trabajo | Oído antes, por escrito |
| El mando intermedio del ámbito | Oído antes, por escrito |
| Quien defiende a quien recibe el servicio | Oído antes, por escrito |
| El área de tecnología | Oída antes, por escrito |
| La representación legal | Oída antes, por escrito, cuando la decisión toca condiciones de trabajo |

La regla de decisión es una: decide el patrocinador oído el comité, y las objeciones quedan escritas. Toda decisión de puerta se firma así: firma el patrocinador y contrafirma la persona ajena al equipo del programa. La plantilla del anexo C lo recoge. En el programa acotado no hay comité: firma el patrocinador con quien dirige el programa y contrafirma alguien ajeno. Donde este documento dice "comité de puertas", el programa acotado lee esa firma.

**Quién decide qué.** Los derechos de decisión se escriben en una tabla de una página durante los primeros cien días, antes de la primera puerta, y se revisan en cada puerta. Es la única tabla de derechos de decisión del método, y el módulo 5 remite a ella. Como mínimo responde a estas decisiones. Cada organización añade las suyas y dos columnas más: a quién se consulta y a quién se informa.

| Decisión | Quién la toma |
|---|---|
| Aprobar un caso de uso o un agente nuevo | Comité de puertas |
| Subir o bajar un nivel de autonomía | Comité de puertas, a propuesta del dueño y con los criterios escritos antes |
| Parar un sistema en uso y reanudarlo | Cualquier persona de la capa de uso puede dejar de usarlo en su caso y pedir la parada al dueño, que responde en el día. El dueño puede parar el servicio entero. Reanudar lo decide el dueño y lo anota |
| Retirar una solución | El patrocinador, que firma, con la contrafirma de alguien sin interés en la iniciativa |
| Aceptar un riesgo que queda por encima de lo fijado | El órgano de dirección |
| Cambiar de versión de modelo dentro de la misma solución | El dueño, con nueva evaluación antes de volver al servicio |
| Sustituir la solución o el proveedor | Comité de puertas |
| Elegir plataforma y arquitectura | El área de tecnología, con el comité de puertas como consultado |
| Aceptar una solución en producción y operarla | El área de tecnología, con el comité de puertas como consultado |
| Responder ante quien recibe el servicio cuando algo falla | El dueño, que es la persona con nombre que figura en el inventario |
| Gestionar un incidente con un sistema de IA | El dueño, que lo anota en el inventario. La segunda línea lo revisa y puede objetar, y el análisis posterior, sin culpables, entra en la supervisión del programa |
| Vigilar un sistema en servicio y volver a pasar sus casos de prueba | El dueño, con el responsable de medición, que certifica los datos de los indicadores. La auditoría interna comprueba una vez al año que el inventario se corresponde con lo que está en uso |
| Buscar sesgos y casos que no encajan antes de pasar a producción | Quien hace el trabajo escribe los casos de prueba, incluidos los raros, con el mapa de lo que nadie escribió como punto de partida. La segunda línea revisa y puede objetar |
| Decidir qué datos pueden usarse con qué herramienta | El dueño de los datos, con la segunda línea. Los datos personales tienen además su propio paso (módulo 11) |

Las cuatro últimas filas, sobre incidentes, vigilancia, sesgos y datos, son una propuesta de la versión 1.8 sin probar. No traen reglas nuevas: reúnen lo que dicen otros capítulos para que cada una tenga responsable en la misma tabla.

El dueño de la solución es el dueño operativo, el del agente y quien figura en el inventario: una sola persona. Cuando el documento habla de otro dueño (de los datos, del beneficio, de la estrategia), lo nombra con su apellido.

**Un inventario único.** Casos de uso, sistemas y agentes están en un solo inventario, y esta es su única definición: el capítulo 17, el módulo 11 y el módulo 24 remiten aquí. Cada entrada lleva los campos de la ficha del módulo 24 (dueño, finalidad y flujo, acciones permitidas, datos, nivel y techo de autonomía, aprobación humana, condiciones de parada, registro de acciones, coste, personas y conocimiento, y revisión) y cuatro cosas más: el nivel de riesgo, el proveedor, los incidentes y un campo de estado. El campo de personas y conocimiento se rellena con las seis anotaciones del capítulo 17. El estado tiene cuatro valores: en evaluación, en experimento, aprobado y retirado. Solo lo que figura como aprobado está aprobado para el servicio. Lo que prueba el carril de exploración (módulo 23) figura como experimento. Un uso contado puede seguir en estado "en evaluación", con las reglas generales de datos, hasta que haya respuesta.

**Quien usa, quien controla y quien audita.** El Instituto de Auditores Internos llama a este reparto las tres líneas. La primera es quien posee y opera el sistema. La segunda la forman riesgos, seguridad, protección de datos y cumplimiento, que revisan y pueden objetar. La tercera es la auditoría interna, que comprueba que las otras dos funcionan. En Synergós la segunda línea participa en el diseño y en el piloto, y no se la convoca al final para firmar. La tercera entra en el sostenimiento. Las tres capas descritas más arriba son niveles de responsabilidad; las tres líneas dicen quién vigila a quién. Hacen falta las dos cosas.

**Gobierno dentro de cada función.** Un comité central no ve lo que pasa en compras, en atención o en recursos humanos. Cada función que usa IA tiene una persona que responde de sus casos, que conoce el inventario de su área y que trae al comité lo que el comité no puede ver. Sin esa persona, el gobierno es un documento que la función no ha leído.

**El uso informal.** En casi todas las organizaciones hay gente usando herramientas de IA que nadie ha aprobado. Prohibirlo sin ofrecer alternativa lo esconde. Desde la versión 1.8 esto es regla; solo sigue abierto cómo preguntar sin que la consulta parezca una auditoría (capítulo 17). El método pide cuatro cosas: averiguar en el diagnóstico qué se usa de verdad, con una consulta anónima; ofrecer herramientas aprobadas que sirvan para lo que la gente hace con las otras; un canal para pedir herramientas nuevas con respuesta en plazo; y la garantía de que contar un uso para que se evalúe no trae sanción (módulo 23). La garantía cubre haber probado la herramienta; no exime de comunicar y tratar una posible fuga de datos. Qué datos pueden usarse con cada herramienta lo dice el módulo 11.

{{img:fig-uso-informal.png|16}}

>> Lo que la gente usa a escondidas dice dónde está la necesidad.

**Herramientas de uso general.** Un asistente para toda la plantilla no ataca una restricción concreta ni tiene un flujo que mapear, así que no puede recorrer el tronco. Se aprueba por una vía corta, con cuatro condiciones escritas: reglas de uso, datos permitidos, formación mínima e indicadores de uso y de capacidad. Cada uso que entre en un servicio pasa después por el tronco.

*Señal de fallo:* las puertas se aprueban por calendario y no por evidencias. Otra señal: hay sistemas o agentes en uso que no están en el inventario.

>> Cuando la puerta se pasa porque toca, deja de ser una puerta.

### Modelo económico

Presupuesto por fases, con la horquilla que cada puerta libera o devuelve, reparto pactado de las ganancias e hitos de recuperación. Y una previsión explícita del valle.

Brynjolfsson, Daniel Rock y Chad Syverson describieron en 2021 la curva J de la productividad: cuando una organización adopta una tecnología de propósito general, primero tiene que invertir en cosas que no se ven en la contabilidad (rediseño del trabajo, formación, procesos nuevos), y durante un tiempo la productividad medida baja antes de subir. La fuente describe el efecto a nivel de empresa y de economía; aplicarlo a un programa es una analogía mía. En mi experiencia, muchos programas se cancelan en ese valle, justo antes de dar resultado. El modelo económico de Synergós lo prevé: dice cuánto dura el valle esperado, cuánto cuesta, qué indicadores bajarán y cuánto, y qué indicadores tempranos muestran que se va por buen camino aunque el resultado todavía no llegue. La duración del valle se estima con la clase de referencia del módulo 17 y, si no hay, se declara como supuesto.

{{img:fig-curva.png|16}}

**Coste por tarea completada.** Desde la versión 1.6, el modelo no se queda en lo que cuesta tener la herramienta. Calcula cuánto cuesta cerrar una tarea de principio a fin con ella: licencias o consumo, la revisión humana que exige, el retrabajo cuando falla y el soporte. Se compara con lo que costaba la misma tarea en la línea base. Es una cuenta incómoda, porque la herramienta puede ser barata por uso y cara por tarea cerrada si casi todo hay que revisarlo. Y hay que repetirla cada periodo de medición, porque el uso y el coste cambian.

**El coste que no está en la factura.** Desde la versión 1.7, la cuenta incluye lo que no cobra el proveedor del modelo: integrar la solución con los sistemas, preparar los datos, evaluarla, vigilarla, la revisión humana y el gobierno. Suelen estar en presupuestos distintos, con dueños distintos, y por eso el caso de negocio solo cuenta lo que se ve. La FinOps Foundation propone leer el gasto en IA por unidad de trabajo y no por consumo. En Synergós esa unidad es la que entiende el negocio: el expediente resuelto, la consulta atendida, el caso cerrado. El coste por tarea completada, con todo eso dentro, se compara con el de la línea base en cada puerta.

*Señal de fallo:* la revisión de cada periodo de medición reabre la financiación, o el único coste que se presenta es el de las licencias y no el de cerrar la tarea.

### Medición y el delta

Las reglas de medición de Synergós están todas en este apartado.

{{img:fig-medicion.png|16}}

**Línea base antes de cambiar nada.** Sin ella, ningún resultado posterior significa nada. La línea base recoge también la variación normal de cada indicador, es decir, entre qué valores se movía antes de cambiar nada. Un indicador que no existía antes de la herramienta, como el uso, parte de cero, y se dice así.

**Pocos indicadores de resultado, en pareja.** Velocidad con calidad, coste con satisfacción. Douglas Hubbard defendió en 2007 que casi todo lo que importa se puede medir de forma útil si se acepta medir con incertidumbre. Y la ley de Goodhart avisa del riesgo contrario. Charles Goodhart la formuló en 1975 pensando en la política monetaria; la versión que se cita hoy, "cuando una medida se convierte en objetivo, deja de ser una buena medida", es de la antropóloga Marilyn Strathern, de 1997. Medir en pareja es la defensa más barata: es difícil mejorar la velocidad a costa de la calidad si las dos se miran juntas.

**Dos clases de indicador.** Desde la versión 1.8 hay dos clases. Los de avance tienen objetivo y entran en el delta. Los de guarda solo tienen un suelo y no entran en la media: se cumplen o no. La calidad que acompaña a una mejora de velocidad, o una capacidad que solo se quiere conservar, son indicadores de guarda. El suelo se fija mirando la variación normal de la línea base.

**Una sola unidad para la mejora: el delta.** El delta de un indicador de avance es lo que ha avanzado desde su línea base hacia su objetivo, en porcentaje. Si el tiempo medio de respuesta estaba en diez días, el objetivo es cuatro y ahora está en siete, el delta es del cincuenta por ciento: se ha recorrido la mitad del camino. El objetivo de cada indicador de avance se fija y se firma en el diseño junto con los pesos, con su justificación, y no cambia hasta el siguiente ciclo. El delta de un indicador tiene un máximo del cien por cien, para que uno que se pasa de su objetivo no tape a otro. Si un indicador queda peor que su línea base, su delta es negativo y entra así en la media. El delta de un ciclo es la media ponderada de sus indicadores de avance.

**Cómo se escribe un criterio de puerta.** Como delta mínimo y, además, en la unidad del indicador: "el tiempo medio de respuesta pasa de diez días a siete o menos". El criterio tipo del piloto es este: el delta del ciclo supera el umbral firmado, ningún indicador de guarda baja de su suelo, y los indicadores para los que el modelo económico prevé valle no bajan más de lo previsto. Sustituye a "ningún indicador retrocede", que retiraba una iniciativa justo en el valle que el propio método espera.

**Quién fija los umbrales.** Los propone medición, con dos referencias: la variación normal del indicador en la línea base y el mínimo que haría rentable la escala según el modelo económico. Los firma el patrocinador. Un cambio menor que la variación normal no cuenta ni como mejora ni como retroceso. Si el resultado queda dentro de esa variación respecto al umbral, decide el patrocinador y lo motiva por escrito. El método no da un valor de partida para ningún umbral, porque no tengo uno contrastado.

**Al menos un indicador por elemento.** Es la regla que conecta la medición con la promesa. En tecnología son dos, el uso y el resultado. Si solo mejora la tecnología, la transformación está rota aunque sus números sean excelentes. La tabla dice cuáles son obligatorios, de qué clase es cada uno y a qué elemento pertenece.

| Indicador | Elemento | Clase | Obligatorio u opcional |
|---|---|---|---|
| Proporción de casos fuera de patrón que el equipo resuelve sin escalar, medida por muestreo antes y durante el piloto | Personas | De avance si el diseño espera que mejore; de guarda, con suelo en su línea base, si se pide que se conserve | Obligatorio. Es el indicador de personas por defecto, provisional mientras la pregunta sigue abierta |
| Carga percibida | Personas | De guarda | Obligatorio, junto al anterior |
| Capacidad: qué sabe hacer la gente con la herramienta y sin ella | Personas | De guarda, salvo que el diseño le ponga objetivo | Obligatorio cuando hay una herramienta dentro del servicio. Se lee en pareja con el uso |
| Concentración: cuántas filas críticas del mapa siguen en una sola persona | Conocimiento | De avance | Obligatorio |
| Revisabilidad y vigencia de la base (módulo 6) | Conocimiento | De avance | Opcional |
| Uso real, no el de la demo | Tecnología | De avance. Su línea base es cero | Obligatorio |
| Resultado en el servicio o en el negocio: tiempo de ciclo, coste por unidad, errores | Tecnología | De avance, con su pareja como indicador de guarda | Obligatorio |
| Lo que vive quien recibe el servicio (módulo 21) | Tecnología | La fija el diseño | Opcional |
| Autonomía de las personas, rotación | Personas | De guarda | Opcional. La rotación llega tarde |
| Tiempo que tarda alguien nuevo en resolver solo los casos difíciles (módulo 7) | Personas | De guarda: su suelo es no empeorar respecto a la línea base y no entra en el delta, porque tarda más que el piloto en dar dato | Opcional. Se lee en el sostenimiento |

Con una herramienta dentro del servicio, el mínimo real son seis lecturas: las tres de personas, una de conocimiento y las dos de tecnología. Lo digo así porque "tres indicadores", que era la cifra de versiones anteriores, se quedaba corta.

**El uso, en pareja con la capacidad.** El uso engaña: un uso alto con resultados iguales que antes es la señal clásica de que la adopción es aparente. Por eso se lee junto a la capacidad, que es un indicador de personas: qué ha pasado con lo que la gente sabe hacer con la herramienta y sin ella. Por ejemplo, la proporción de tareas que alguien del área resuelve bien sin ayuda de la herramienta cuando hace falta, o la calidad de las correcciones que hace a lo que la herramienta produce. El uso tiene su propia escalera: la persona tiene acceso, la usa cada semana, la usa en varias tareas distintas. El resultado es lo que cambió en el servicio o en el negocio. El uso es condición para que haya resultado y no lo demuestra.

**Lectura agregada.** Las medidas de capacidad y de supervisión se leen agregadas por equipo. Una lectura individual se pacta antes con el equipo y con la representación legal y se anota como vigilancia en el inventario.

**Dos cautelas.** El tiempo ahorrado que declara la gente es evidencia débil y no se acepta como prueba de valor; vale como indicio para saber dónde medir. Y las cifras de retorno que publican los informes del sector se contradicen entre sí, de modo que la única vara fiable es la propia: la línea base de la organización, medida antes del piloto con el mismo método que se usará después.

!! Pregunta abierta. ¿Cómo se mide el criterio de las personas? | Es el indicador que más falta y el que peor sé medir. Medir la rotación es fácil, pero llega tarde. Medir el uso es fácil, pero engaña. Lo que de verdad importa (si la gente conserva y amplía su capacidad de juzgar casos difíciles) no tiene una medida estándar. Desde la versión 1.8 hay un indicador por defecto para que las puertas se puedan aplicar: la proporción de casos fuera de patrón que el equipo resuelve sin escalar, con la carga percibida como guarda. Es provisional. Sigue abierto si mide de verdad el criterio, cuántos casos hay que muestrear y si una evaluación periódica con casos difíciles preparados lo haría mejor.

!! Pregunta abierta. ¿El delta ponderado esconde más de lo que muestra? | Un delta medio del sesenta por ciento puede ocultar un indicador que ha empeorado. Los indicadores de guarda, el máximo del cien por cien y la firma de objetivos y pesos en el diseño reducen el problema y no lo quitan: quien fija los objetivos y los pesos fija el resultado. Sigue siendo una decisión política disfrazada de número, y conviene decirlo.

### Madurez y regla de entrada

La escala de madurez tiene cuatro niveles y se aplica a cada uno de los tres elementos y al gobierno. Se evalúa en el diagnóstico y se revisa en cada puerta.

{{img:fig-madurez.png|16}}

| Nivel | Nombre | Qué significa |
|---|---|---|
| 1 | Puntual | Ocurre cuando alguien se acuerda o tiene buena voluntad; depende de personas concretas |
| 2 | Repetible | Hay una forma acordada de hacerlo y se repite, aunque no esté integrada en la gestión |
| 3 | Integrado | Forma parte de cómo se gestiona el área: tiene dueño, presupuesto y revisión |
| 4 | Sistemático | Se mide, se mejora y se usa para decidir; sobrevive a los cambios de personas |

El anexo D desarrolla qué significa cada nivel para cada uno de los tres elementos y para el gobierno.

**La regla de entrada.** Un acelerador entra en el servicio solo si las condiciones que necesita, en los tres elementos y en el gobierno, están en nivel 2 de madurez en el ámbito. La regla se aplica a la tecnología dentro del servicio. La IA como herramienta del equipo que transforma solo exige reglas de uso y datos autorizados. La exigencia es baja: el nivel 2 solo pide que algo se haga de forma acordada y repetible. Pero sin eso, el acelerador multiplica lo que encuentra.

### Dimensionamiento

El método se adapta al tamaño del programa.

**Un programa acotado** (un equipo, hasta la puerta del piloto en menos de seis meses): no hay comité de puertas, y cada puerta la firma el patrocinador con quien dirige el programa y la contrafirma alguien ajeno; un solo ciclo; como máximo dos aceleradores por ciclo, contando la IA dentro del servicio si el diagnóstico la justifica.

**Un programa amplio** (varias áreas, de uno a tres años): comité de puertas; varios ciclos en paralelo, uno por ámbito; como máximo tres aceleradores por ciclo, contando la IA; una oficina pequeña de medición y conocimiento.

La revisión de supuestos del capítulo 16 vale para los dos tamaños y se hace cada periodo de medición. En el programa acotado puede coincidir con la puerta.

**Un programa en marcha** no se reinicia. Se hace un diagnóstico rápido, con tres entregables: la restricción nombrada, la línea base y el mapa del trabajo afectado. Si no hay línea base anterior, se mide la situación actual, se declara como línea base tardía y se dice qué mejora anterior queda sin poder atribuirse. Después cada iniciativa se clasifica en mantener, priorizar, reorientar o retirar, y se instalan las puertas a partir de la siguiente fase.

### La marcha atrás como opción legítima

Klarna anunció en febrero de 2024 que su asistente de IA hacía el trabajo equivalente a setecientos agentes de atención al cliente a tiempo completo, buena parte de ellos de proveedores externos. En mayo de 2025 su consejero delegado reconoció que se habían fijado demasiado en el coste y que la calidad había bajado, y anunció un piloto para volver a incorporar personas y garantizar que el cliente pueda hablar siempre con una. Commonwealth Bank of Australia declaró prescindibles en julio de 2025 cuarenta y cinco puestos de atención telefónica porque un bot de voz reducía las llamadas; el sindicato sostuvo que las llamadas habían subido, y el 21 de agosto el banco revirtió la decisión y pidió disculpas. En los dos casos la decisión se tomó mirando el coste o el volumen, y hubo que rectificar. Mi lectura, que las fuentes no confirman, es que no se midió lo que hacían las personas.

Un método serio prevé la marcha atrás antes de necesitarla y la hace barata. En Synergós eso significa tres cosas: la retirada es una de las tres salidas de cada puerta; el diseño dice, para cada opción, cómo se deshace; y la escala de autonomía permite bajar de nivel sin que nadie tenga que justificar un fracaso.

**Lo que cuesta retirar.** La retirada se firma como cualquier decisión de puerta: firma el patrocinador y contrafirma alguien sin interés en la iniciativa. Quien la propone queda protegido por escrito. Cuánto hay que justificar depende de la fase y está en el capítulo 12. Queda abierto si esta regla funciona en organizaciones muy jerárquicas.
