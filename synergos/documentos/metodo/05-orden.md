## 18. El orden: crecer a la vez

El orden es lo que hace que los tres elementos avancen al mismo compás. Agrupa la estrategia, el gobierno, el modelo económico, la medición, la madurez y el dimensionamiento. Es la parte menos vistosa del método y la que decide si todo lo demás llega a algún sitio.

### Estrategia

Rumelt describió en 2011 el núcleo de una buena estrategia en tres partes: un diagnóstico que nombra el problema crítico, una política guía que dice cómo se va a abordar y un conjunto de acciones coherentes entre sí. A. G. Lafley y Roger Martin lo formularon en 2013 como dos elecciones: dónde jugar y cómo ganar. Lo que tienen en común es que una estrategia es, sobre todo, lo que se decide no hacer.

**El papel de la dirección.** Desde la versión 1.7, la estrategia de IA tiene dueño en el órgano que dirige la organización. Ese órgano hace tres cosas que nadie más puede hacer: decide para qué se quiere la IA (capítulo 17), fija cuánto riesgo se acepta y recibe cada ciclo el mismo cuadro de indicadores que ve el comité de puertas. Delegar la estrategia de IA entera en el área de tecnología es una forma de no tenerla.

**Un arranque a cien días.** Un programa nuevo se compromete solo a lo que cabe en ese plazo: el diagnóstico con su mapa, el inventario de lo que ya se usa (también lo no autorizado), los derechos de decisión escritos, la línea base de los indicadores y la primera puerta. Más allá de la primera puerta no se promete nada, por la misma razón que el módulo 17 da para los plazos.

*Señal de fallo:* la cartera crece sin que nadie retire nada. Un programa que solo suma iniciativas no tiene estrategia; tiene una lista.

### Gobierno

Un comité de puertas con criterios previos, derechos de decisión escritos y un registro de riesgos y de decisiones. Peter Weill y Jeanne Ross mostraron en 2004 que las organizaciones que deciden con claridad quién decide qué sobre la tecnología obtienen más valor de ella. La claridad importa más que el modelo concreto.

**Tres capas de responsabilidad.** El gobierno fija los criterios, los derechos de decisión y las puertas. La gestión los aplica, los mide y los corrige. El uso es de quien trabaja con la herramienta cada día, que es quien primero ve cuándo falla. Propuesta de la versión 1.4: la capa de uso tiene derecho a parar, por escrito y sin represalias, y ese derecho se anota en la misma tabla que los demás derechos de decisión. Sin él, que la persona decida se queda en una frase.

**Quién decide qué.** Desde la versión 1.7, los derechos de decisión se escriben en una tabla de una página, que se revisa en cada puerta. Como mínimo responde a siete preguntas.

| Decisión | Quién la toma |
|---|---|
| Aprobar un caso de uso o un agente nuevo | Comité de puertas |
| Subir o bajar un nivel de autonomía | Comité de puertas, a propuesta del dueño |
| Parar un sistema en uso | Su dueño y cualquier persona de la capa de uso, sin autorización previa |
| Retirar una solución | Comité de puertas, con la firma de alguien sin interés en ella |
| Aceptar un riesgo que queda por encima de lo fijado | El órgano de dirección |
| Cambiar de proveedor o de modelo | Dueño de la solución, con nueva evaluación antes de volver al servicio |
| Responder ante quien recibe el servicio cuando algo falla | Una persona con nombre, la misma que figura en el inventario |

**Un inventario único.** Casos de uso, sistemas y agentes están en un solo registro, con dueño, nivel de autonomía, proveedor, datos y la columna de personas y conocimiento del capítulo 17. Lo que no está en el inventario no está aprobado. La ficha de cada agente se describe en el módulo 24.

**Quien usa, quien controla y quien audita.** El Instituto de Auditores Internos llama a este reparto las tres líneas. La primera es quien posee y opera el sistema. La segunda la forman riesgos, seguridad, protección de datos y cumplimiento, que revisan y pueden objetar. La tercera es la auditoría interna, que comprueba que las otras dos funcionan. En Synergós la segunda línea participa en el diseño y en el piloto, y no se la convoca al final para firmar. La tercera entra en el sostenimiento. Las tres capas del párrafo anterior describen niveles de responsabilidad; las tres líneas describen quién vigila a quién. Hacen falta las dos cosas.

**Gobierno dentro de cada función.** Un comité central no ve lo que pasa en compras, en atención o en recursos humanos. Cada función que usa IA tiene una persona que responde de sus casos, que conoce el inventario de su área y que trae al comité lo que el comité no puede ver. Sin esa persona, el gobierno es un documento que la función no ha leído.

**El uso informal.** En casi todas las organizaciones hay gente usando herramientas de IA que nadie ha aprobado. Prohibirlo sin ofrecer alternativa lo esconde. El método pide cuatro cosas: averiguar en el diagnóstico qué se usa de verdad, con una consulta anónima; ofrecer herramientas aprobadas que sirvan para lo que la gente hace con las otras; un canal para pedir herramientas nuevas con respuesta en plazo; y la garantía de que contar un uso para que se evalúe no trae sanción (módulo 23). Lo que la gente usa a escondidas dice dónde está la necesidad.

*Señal de fallo:* las puertas se aprueban por calendario y no por evidencias. Cuando la puerta se pasa porque toca, deja de ser una puerta. Otra señal: hay sistemas o agentes en uso que no están en el inventario.

### Modelo económico

Presupuesto por fases, reparto pactado de las ganancias e hitos de recuperación. Y una previsión explícita del valle.

Brynjolfsson, Daniel Rock y Chad Syverson describieron en 2021 la curva J de la productividad: cuando una organización adopta una tecnología de propósito general, primero tiene que invertir en cosas que no se ven en la contabilidad (rediseño del trabajo, formación, procesos nuevos), y durante un tiempo la productividad medida baja antes de subir. Muchos programas se cancelan en ese valle, justo antes de dar resultado. El modelo económico de Synergós lo prevé: dice cuánto dura el valle esperado, cuánto cuesta y qué indicadores tempranos muestran que se va por buen camino aunque el resultado todavía no llegue.

**Coste por tarea completada.** Desde la versión 1.6, el modelo no se queda en lo que cuesta tener la herramienta. Calcula cuánto cuesta cerrar una tarea de principio a fin con ella: licencias o consumo, la revisión humana que exige, el retrabajo cuando falla y el soporte. Se compara con lo que costaba la misma tarea en la línea base. Es una cuenta incómoda, porque la herramienta puede ser barata por uso y cara por tarea cerrada si casi todo hay que revisarlo. Y hay que repetirla cada ciclo, porque el uso y el coste cambian.

**El coste que no está en la factura.** Desde la versión 1.7, la cuenta incluye lo que no cobra el proveedor del modelo: integrar la solución con los sistemas, preparar los datos, evaluarla, vigilarla, la supervisión humana y el gobierno. Suelen estar en presupuestos distintos, con dueños distintos, y por eso el caso de negocio solo cuenta lo que se ve. La FinOps Foundation propone leer el gasto en IA por unidad de trabajo y no por consumo. En Synergós esa unidad es la que entiende el negocio: el expediente resuelto, la consulta atendida, el caso cerrado. El coste completo por unidad se compara con el de la línea base en cada puerta.

*Señal de fallo:* cada revisión trimestral reabre la financiación, o el único coste que se presenta es el de las licencias y no el de cerrar la tarea.

### Medición y el delta

La medición en Synergós tiene cuatro reglas.

**Línea base antes de cambiar nada.** Sin ella, ningún resultado posterior significa nada.

**Pocos indicadores de resultado, en pareja.** Velocidad con calidad, coste con satisfacción. Douglas Hubbard defendió en 2007 que casi todo lo que importa se puede medir de forma útil si se acepta medir con incertidumbre. Y la ley de Goodhart avisa del riesgo contrario. Charles Goodhart la formuló en 1975 pensando en la política monetaria; la versión que se cita hoy, "cuando una medida se convierte en objetivo, deja de ser una buena medida", es de la antropóloga Marilyn Strathern, de 1997. Medir en pareja es la defensa más barata: es difícil mejorar la velocidad a costa de la calidad si las dos se miran juntas.

**Una sola unidad para la mejora: el delta.** El delta de un indicador es lo que ha avanzado desde su línea base hacia su objetivo, en porcentaje. Si el tiempo medio de respuesta estaba en diez días, el objetivo es cuatro y ahora está en siete, el delta es del cincuenta por ciento: se ha recorrido la mitad del camino. El delta de un ciclo es la media ponderada de sus indicadores, con pesos pactados en el diseño. Los criterios de las puertas se escriben como delta mínimo: "el piloto pasa si el delta del ciclo supera el cuarenta por ciento y ningún indicador retrocede".

**Tres indicadores como mínimo: uno por elemento.** Es la regla que conecta la medición con la promesa. Para personas, algo como el criterio que conserva la gente, su autonomía o la rotación. Para conocimiento, la concentración (cuántas filas del mapa siguen en una sola persona) o lo que ha pasado al sistema de forma revisable. Para tecnología, el uso real, no el de la demo. Si solo mejora el tercero, la transformación está rota aunque los números de la tecnología sean excelentes.

**El uso, en pareja con la capacidad.** Desde la versión 1.6, el indicador de tecnología no puede ser solo el uso, porque el uso engaña: un uso alto con resultados iguales que antes es la señal clásica de que la adopción es aparente. El uso se empareja con un indicador de capacidad: qué ha pasado con lo que la gente sabe hacer con la herramienta y sin ella. Por ejemplo, la proporción de tareas que alguien del área resuelve bien sin ayuda de la herramienta cuando hace falta, o la calidad de las correcciones que hace a lo que la herramienta produce. El uso dice cuánto se toca la herramienta; la capacidad dice si la gente sabe más o menos que antes.

**Tres niveles: uso, capacidad y resultado.** Desde la versión 1.7 la medición de la tecnología se lee en tres niveles, y ninguno sustituye al siguiente. El uso tiene su propia escalera: la persona tiene acceso, la usa cada semana, la usa en varias tareas distintas. La capacidad es la del párrafo anterior. El resultado es lo que cambió en el servicio o en el negocio: tiempo de ciclo, coste por unidad, errores, satisfacción de quien lo recibe. El uso es condición para que haya resultado y no lo demuestra.

**Dos cautelas.** El tiempo ahorrado que declara la gente es evidencia débil y no se acepta como prueba de valor; vale como indicio para saber dónde medir. Y las cifras de retorno que publican los informes del sector se contradicen entre sí, de modo que la única vara fiable es la propia: la línea base de la organización, medida antes del piloto con el mismo método que se usará después.

!! Pregunta abierta. ¿Cómo se mide el criterio de las personas? | Es el indicador que más falta y el que peor sé medir. Medir la rotación es fácil, pero llega tarde. Medir el uso es fácil, pero engaña. Lo que de verdad importa (si la gente conserva y amplía su capacidad de juzgar casos difíciles) no tiene una medida estándar. Candidatos que estoy considerando: la proporción de casos fuera de patrón que resuelve el equipo sin escalar; la calidad de las correcciones que hacen a la IA; una evaluación periódica con casos difíciles preparados. Ninguno me convence del todo. El indicador de capacidad en pareja con el de uso, que se añade en la versión 1.6, no resuelve esta pregunta, pero evita que el uso sea el único indicador de adopción mientras se resuelve.

!! Pregunta abierta. ¿El delta ponderado esconde más de lo que muestra? | Un delta medio del sesenta por ciento puede ocultar un indicador que ha retrocedido. Por eso los criterios de puerta añaden "ningún indicador retrocede", pero eso tampoco resuelve el problema de los pesos: quien fija los pesos fija el resultado. Propuesta: los pesos se pactan en el diseño, se escriben, y no se cambian hasta el siguiente ciclo. Sigue siendo una decisión política disfrazada de número, y conviene decirlo.

### Madurez y regla de entrada

La escala de madurez tiene cuatro niveles y se aplica a cada elemento y a cada acelerador. Se evalúa en el diagnóstico y se revisa en cada puerta.

| Nivel | Nombre | Qué significa |
|---|---|---|
| 1 | Puntual | Ocurre cuando alguien se acuerda o tiene buena voluntad; depende de personas concretas |
| 2 | Repetible | Hay una forma acordada de hacerlo y se repite, aunque no esté integrada en la gestión |
| 3 | Integrado | Forma parte de cómo se gestiona el área: tiene dueño, presupuesto y revisión |
| 4 | Sistemático | Se mide, se mejora y se usa para decidir; sobrevive a los cambios de personas |

El anexo D desarrolla qué significa cada nivel para cada uno de los tres elementos.

**La regla de entrada:** un acelerador se activa solo si sus condiciones están en nivel 2 o más. La IA en piloto dentro del servicio exige gobierno y personas en nivel 2 como mínimo. No es una regla de perfección: el nivel 2 solo pide que algo se haga de forma acordada y repetible. Pero sin eso, el acelerador multiplica lo que encuentra.

### Dimensionamiento

El método se adapta al tamaño del programa.

**Un programa acotado** (un equipo, menos de seis meses): las puertas las preside el patrocinador con el responsable; un solo ciclo; la IA y un acelerador más.

**Un programa amplio** (varias áreas, de uno a tres años): comité de puertas; varios ciclos en paralelo; la IA y hasta dos aceleradores más por ciclo; revisión trimestral de supuestos; una oficina pequeña de medición y conocimiento.

**Un programa en marcha** no se reinicia. Se hace un diagnóstico rápido, cada iniciativa se clasifica en mantener, acelerar, reorientar o retirar, y se instalan las puertas a partir de la siguiente fase.

### La marcha atrás como opción legítima

Klarna anunció en febrero de 2024 que su asistente de IA hacía el trabajo equivalente a setecientos agentes de atención al cliente a tiempo completo, buena parte de ellos de proveedores externos. En mayo de 2025 su consejero delegado reconoció que se habían fijado demasiado en el coste y que la calidad había bajado, y anunció un piloto para volver a incorporar personas y garantizar que el cliente pueda hablar siempre con una. Commonwealth Bank of Australia declaró prescindibles en julio de 2025 cuarenta y cinco puestos de atención telefónica porque un bot de voz reducía las llamadas; el sindicato sostuvo que las llamadas habían subido, y el 21 de agosto el banco revirtió la decisión y pidió disculpas. En ninguno de los dos casos falló la tecnología. Falló la medición de lo que hacían las personas, que se descubrió cuando ya no estaban.

Un método serio prevé la marcha atrás antes de necesitarla y la hace barata. En Synergós eso significa tres cosas: la retirada es una de las tres salidas de cada puerta; el diseño dice, para cada opción, cómo se deshace; y la escala de autonomía permite bajar de nivel sin que nadie tenga que justificar un fracaso.
