# Parte III. El tronco: cinco fases con puertas

## 8. Cómo funcionan las fases

El tronco del método son cinco fases: diagnóstico, diseño, piloto, escala y sostenimiento. Cada una tiene un propósito, unos entregables, una puerta y un error típico. Llamo ciclo al recorrido de las cinco fases en un ámbito. Un programa amplio tiene varios ciclos en paralelo, cada uno en su fase, y lo aprendido en el sostenimiento de uno alimenta el diagnóstico del siguiente. Es el ciclo de mejora de Deming llevado a escala de programa.

{{img:fig-fases.png|16}}

{{img:fig-estructura.png|16}}

**Qué recorre el tronco.** Un programa tiene uno o varios ámbitos. Un ámbito es el servicio o el flujo de trabajo que se va a transformar. Cada ámbito hace un diagnóstico y tiene una restricción. Del diagnóstico salen iniciativas, que forman la cartera. Cada iniciativa compara opciones en el diseño y recorre piloto, escala y sostenimiento. Hay, por tanto, un diagnóstico, un mapa y una puerta de diagnóstico por ámbito, y una puerta de diseño, de piloto, de escala y de sostenimiento por iniciativa.

Cada puerta tiene tres salidas posibles para la iniciativa que llega a ella: pasar, ajustar y repetir, o retirar. Retirar una iniciativa en la puerta del piloto es barato, y es una buena noticia: el método ha hecho su trabajo, que es equivocarse en pequeño antes de equivocarse en grande.

| Fase | Para qué | Entregables | Puerta: qué tiene que ser cierto | Quién escribe los criterios y cuándo | Quién decide | Error típico |
|---|---|---|---|---|---|---|
| 1. Diagnóstico | Entender dónde se pierden tiempo, calidad o dinero, y por qué | Los seis básicos, de los que la puerta solo exige tres (los de su columna): mapa del flujo real, restricción del ámbito, línea base, mapa de actores, madurez de los tres elementos, mapa de lo que nadie escribió. El capítulo 9 dice lo que añaden el capítulo 18 y los módulos | Restricción nombrada y aceptada por el patrocinador; línea base medida, no estimada; mapa de lo que nadie escribió hecho | Los fija el método. Quien dirige el programa los deja escritos al empezar, junto con el ámbito | El patrocinador, oído el comité de puertas | Un inventario de problemas sin jerarquía |
| 2. Diseño | Decidir qué se cambia, cómo y con qué aceleradores | Cartera priorizada, nuevo diseño del trabajo, aceleradores por fase, criterios del piloto con su criterio de parada, registro de supuestos, modelo económico, decisión escrita con las cinco preguntas por opción | Cada iniciativa ataca la restricción, o es un habilitador o una obligación legal; criterios del piloto firmados; cada opción dice qué le pasa al conocimiento y si acelera, automatiza o aumenta | Las cinco preguntas las fija el método. Quien dirige el programa las deja escritas al empezar la fase | El patrocinador, oído el comité de puertas | Diseñar la herramienta y dejar el trabajo como estaba |
| 3. Piloto | Probar en pequeño con gente y datos reales | Resultados contra la línea base y contra la comparación elegida, casos de prueba pasados, supuestos anotados, lecciones, ajustes, riesgos | Cumple sus criterios, o la puerta decide ajustar y repetir, o retirar | Medición propone los umbrales y el patrocinador los firma en el diseño, antes de empezar el piloto | El patrocinador, oído el comité de puertas | Elegir el entorno más fácil, que no representa al resto |
| 4. Escala | Extender lo que funciona | Despliegue por etapas, formación, responsable de adopción y referentes, normas de equipo, roles e incentivos, procedimientos | Los indicadores aguantan al ampliar, los elementos aguantan la carga y se ha comprobado si la restricción sigue siendo la misma | Medición los propone y el patrocinador los firma al pasar la puerta del piloto, antes de la primera etapa | El patrocinador, oído el comité de puertas. Cada etapa intermedia la decide el dueño operativo | Escalar la herramienta sin escalar roles e incentivos |
| 5. Sostenimiento | Que la mejora siga cuando el equipo se vaya | Dueño operativo, presupuesto recurrente, cuadro en régimen, calendario de supervisión del programa | El dueño acepta la responsabilidad y los indicadores aguantan dos periodos de medición sin el equipo del programa | Medición los propone con el dueño operativo y el patrocinador los firma al empezar la fase | El patrocinador, a convocatoria del dueño operativo | Cerrar sin dueño ni presupuesto |

Quién forma el comité de puertas, quién firma y quién contrafirma está en el capítulo 18. En un programa acotado no hay comité: firma el patrocinador con quien dirige el programa y contrafirma una persona ajena al equipo. El periodo de medición es el intervalo, fijado en el diseño, en que se leen los indicadores; por defecto, un trimestre.

## 9. Fase 1. Diagnóstico

En mi experiencia, el diagnóstico es la fase más importante y la que más se salta. Se salta porque parece lenta, porque el cliente interno ya sabe lo que quiere y porque nadie gana un premio por haber entendido bien un problema. Synergós la convierte en la condición de todo lo demás.

**Antes de empezar: el ámbito.** El ámbito que se diagnostica lo propone quien dirige el programa y lo decide el patrocinador, que deja escrito por qué ese y no otro.

### Los seis entregables

Son los seis entregables básicos. Lo que el capítulo 18 y los módulos añaden al diagnóstico está al final de este apartado.

{{img:fig-diagnostico.png|16}}

**El mapa del flujo de trabajo real.** Se dibuja el flujo que se hace, y la diferencia con el del procedimiento es la primera información útil del programa. Se construye observando en el puesto, no en una sala con los responsables. Las herramientas de minería de procesos ayudan cuando hay registros, pero solo ven lo que deja huella en el sistema, y lo más interesante suele ocurrir fuera.

**La restricción principal.** El punto que limita el resultado del conjunto. Tiene que ser una por ámbito diagnosticado, nombrada, y aceptada por el patrocinador. Una lista de diez problemas no es un diagnóstico. Si el equipo no consigue ponerse de acuerdo en cuál es la restricción, el programa todavía no sabe qué está transformando. Para nombrarla se hacen dos preguntas sobre el mapa del flujo: dónde se acumula la cola de trabajo, y qué pasaría con el resultado del conjunto si se duplicara la capacidad en ese punto. Si el resultado no cambiaría, la restricción está en otro sitio. Se escribe en una frase que diga el punto del flujo y lo que limita.

**La línea base.** Medida, no estimada. Sin línea base no hay forma de saber si el programa mejora algo, y cualquier resultado posterior se podrá defender o atacar según convenga. Es el entregable más aburrido y uno de los más decisivos. Lleva al menos un indicador por elemento (capítulo 18) y, para cada uno, su variación normal: el mínimo y el máximo de los últimos meses. Durante cuánto tiempo se mide lo fija el responsable de medición (anexo G).

**El mapa de actores.** Quién gana y quién pierde con cada posible cambio, quién decide, quién puede bloquear y quién sabe. La última columna es la que casi nunca se rellena.

**La madurez de los tres elementos.** Una evaluación rápida, con la escala del capítulo 18 y del anexo D, de dónde está la organización en personas, conocimiento y tecnología, y en gobierno, para el ámbito que se va a transformar. Sirve para aplicar la regla de entrada de los aceleradores.

**El mapa de lo que nadie escribió.** Es la aportación propia de Synergós al diagnóstico, y la desarrollo en el apartado siguiente.

**El diagnóstico paso a paso.** La tabla dice, para cada entregable, qué se hace, cuál de las siete funciones del equipo (módulo 4) lo hace, con quién y qué prueba que está terminado. El orden de las filas es el que propongo, con una salvedad: el mapa de lo que nadie escribió se levanta a la vez que el mapa del flujo, porque sale de las mismas visitas. No doy duraciones por fila. El módulo 17 da órdenes de magnitud para la fase entera, y el esfuerzo del equipo por fase sigue pendiente (capítulo 21).

| Entregable | Actividad | Función que lo hace | Con quién | Evidencia de terminado |
|---|---|---|---|---|
| Mapa del flujo real | Observar el trabajo en el puesto y compararlo con el procedimiento | Diseño del trabajo | Voz de quien hace el trabajo; Tecnología y datos si hay registros que analizar | El flujo está dibujado, quienes hacen el trabajo lo han repasado y las diferencias con el procedimiento están anotadas |
| Restricción principal | Hacer sobre el flujo las dos preguntas: dónde se acumula la cola y qué pasaría si se duplicara la capacidad en ese punto | Dirección del programa | Medición y Diseño del trabajo | Una frase que nombra la restricción del ámbito, aceptada por escrito por el patrocinador |
| Línea base | Medir los indicadores, al menos uno por elemento, con su variación normal | Medición | Tecnología y datos; el mando del ámbito | Valores medidos, con mínimo y máximo, que Medición certifica |
| Mapa de actores | Listar quién gana, quién pierde, quién decide, quién puede bloquear y quién sabe | Dirección del programa | Patrocinio | La tabla está rellena, también la columna de quién sabe |
| Madurez | Evaluar el ámbito con la escala del anexo D | Medición | El equipo afectado | Un nivel por elemento y uno de gobierno, cada uno con la evidencia en que se apoya |
| Mapa de lo que nadie escribió | Conversar con quienes hacen el trabajo usando las preguntas por las grietas (anexo B) | Conocimiento | Voz de quien hace el trabajo | El mapa de comité existe y el patrocinador ha firmado el compromiso de uso |

**Lo que añaden el capítulo 18 y los módulos.** Según el alcance del programa, el diagnóstico recoge también el inventario de lo que ya se usa, con consulta anónima, y los derechos de decisión (capítulo 18); el inventario de aportaciones (módulo 1); la calidad de los datos (módulo 10); la lectura de los supuestos de cultura (módulo 16); la información a la representación legal (módulo 18); y el mapa del recorrido de quien recibe el servicio (módulo 21). Cuáles son obligatorios lo dice la tabla "Qué es obligatorio según alcance", al cierre de la Parte V. La puerta del diagnóstico solo exige tres entregables, los que nombra su apartado más abajo.

### El mapa de lo que nadie escribió

El mapa recoge el conocimiento no escrito que sostiene hoy el trabajo que se va a cambiar, en quién está y qué le pasa a ese conocimiento con cada opción de diseño. La regla es sencilla: sin mapa no hay puerta. El comité que aprueba el diseño tiene que poder responder por escrito a tres preguntas. En todo el documento las llamo las preguntas del comité.

1. Qué conocimiento no escrito sostiene hoy el trabajo que se va a cambiar.
2. En quién está.
3. Qué le pasa a ese conocimiento con cada opción de diseño que hay sobre la mesa.

La segunda se responde ante el comité por perfil, y con nombre solo si la persona lo consiente. La tercera pregunta del comité es la que convierte el mapa en una herramienta de decisión y no en un ejercicio de antropología. Es la tercera pregunta de la puerta de diseño (capítulo 11) y alimenta también la segunda: el mapa permite responder a la de si acelera, automatiza o aumenta con datos en lugar de con intenciones.

**A quién se pregunta.** A quienes hacen el trabajo, no a los responsables del procedimiento, y en especial a dos perfiles: la persona a la que los demás acuden cuando algo se atasca, y la persona que lleva menos tiempo, porque todavía recuerda lo que nadie le explicó cuando llegó. Mi hipótesis es que entre los dos se dibuja casi todo el mapa. En una organización grande se pregunta por perfil y por centro, y se para cuando dos conversaciones seguidas no añaden filas nuevas.

**Qué se pregunta.** "Qué haces" no sirve, porque la respuesta es el procedimiento; se pregunta por las grietas. Son cinco, y en todo el documento las llamo las preguntas por las grietas:

- ¿Qué casos parecen iguales y no lo son? ¿Cómo los distingues?
- ¿Cuándo no sigues el procedimiento, y por qué?
- ¿A quién llamas cuando algo se atasca? ¿Y a quién te llaman a ti?
- ¿Qué sabes de un caso antes de leerlo entero?
- ¿Qué pasaría mañana si tú no vinieras?

**Cómo se dibuja.** Es una tabla de cuatro columnas básicas: qué se sabe, quién lo sabe, dónde se usa y cuán concentrado está. La última columna es la que asusta a los comités. Cuando una fila dice "una persona", se ve en un segundo dónde está el riesgo. El anexo B recoge la plantilla, con dos columnas opcionales (si la fila es crítica y quién mantiene la capacidad si pasa al sistema), y un ejemplo compuesto.

**Dos versiones.** Hay dos versiones del mapa. La de trabajo lleva nombres y solo la ve la función de conocimiento. La de comité va por perfiles, y es la que se enseña en la puerta. En un equipo pequeño el perfil puede bastar para saber quién es; en ese caso se le dice antes a la persona y decide ella si la fila se enseña.

**Qué se hace con él.** Se pone al lado de cada opción de diseño y se responde fila a fila: con esta opción, este conocimiento se queda en la persona y la tecnología la ayuda, pasa al sistema de forma revisable, o se pierde.

Va un caso compuesto. Una organización quiere usar IA para clasificar y responder las peticiones que le llegan por escrito; las atiende un equipo de doce personas. El mapa da diecinueve filas, cinco de ellas concentradas en una sola persona y dos que no se podían escribir aunque se quisiera (cifras ilustrativas, no medidas). La opción inicial, que la IA respondiera directamente las peticiones sencillas, perdía esas cinco filas, porque quien las sabía dejaba de ver las peticiones que la IA se quedaba. La opción que se aprobó fue otra: la IA clasifica y propone, la persona decide y el sistema le muestra lo que antes detectaba de oído. Con el mismo presupuesto y la misma tecnología, el resultado previsto en la tercera pregunta del comité era el opuesto. El coste del mapa en ese caso: dos semanas de una persona y unas veinte conversaciones. Es también una cifra ilustrativa, pensada para un equipo de ese tamaño, y no sirve para presupuestar un área grande.

**El límite del mapa.** No dice qué opción elegir; dice qué se pierde con cada una. Tampoco sustituye al análisis de costes, ni al de riesgos, ni al de la restricción. Y tiene un riesgo propio que todavía no he resuelto del todo: puede exponer. Si una persona esconde cómo trabaja por una razón legítima, ponerle nombre en una tabla es sacarla de detrás sin su permiso. La regla provisional es que el mapa es de la persona antes que del comité: se construye con su consentimiento, y la versión de comité muestra el conocimiento, no a quien lo tiene, hasta que ella decida otra cosa.

**Si alguien no consiente.** Su parte del mapa se anota como "conocimiento no descrito, concentrado en una persona", y la puerta de diseño lo trata como riesgo alto en la tercera de las cinco preguntas. El mapa se da por hecho con esa fila, de modo que nadie tiene un veto sobre el programa. Si quien no firma el compromiso de uso es el patrocinador, el mapa no se hace y la puerta del diagnóstico no se pasa.

!! Pregunta abierta. ¿Cuántas filas en una sola persona son demasiadas? | Un lector propuso un umbral práctico: más de tres filas críticas en una sola persona como señal para documentar y repartir antes de poner la IA en producción, midiendo además cuántas decisiones dependen de cada fila. Me parece mejor criterio que contar filas, porque pesa por consecuencias y no por volumen. Lo que no tengo resuelto es quién decide qué fila es crítica: si lo decide quien tiene el saber, se infla; si lo decide quien dirige, se infravalora. Propuesta provisional: la criticidad la fija quien usa el resultado de esa fila, no quien la sabe ni quien manda. No tengo un número probado y no lo voy a inventar.

!! Pregunta abierta. ¿Cómo se aplica el consentimiento cuando hay prisa? | La regla del consentimiento funciona cuando el programa tiene tiempo. Cuando la organización tiene prisa, la tentación es levantar el mapa sobre las personas en lugar de con ellas. No tengo una solución que no ralentice. La única defensa que conozco es que el patrocinador firme, antes de empezar, que el mapa no se usará para evaluar ni para decidir despidos individuales. Si no está dispuesto a firmarlo, el mapa no se hace, y eso también es información.

### La puerta del diagnóstico

Para pasar al diseño tienen que ser ciertas tres cosas: la restricción del ámbito está nombrada y el patrocinador la acepta; la línea base está medida; el mapa de lo que nadie escribió existe, con el compromiso de uso firmado por el patrocinador (anexo B). Si falta cualquiera, el programa no está listo para diseñar, por mucha prisa que haya. Hay dos casos en que la línea base no se puede medir como pide esta puerta: el programa que ya estaba en marcha, que se trata en el capítulo 18 (Dimensionamiento), y el servicio que todavía no existe, que se trata en el módulo 23.

## 10. Fase 2. Diseño

El diseño decide qué se cambia, cómo y con qué. Su error típico es el más caro del método: diseñar la herramienta y dejar el trabajo como estaba. Es lo que pasa cuando el diseño lo hace el equipo técnico solo, o cuando el rediseño del trabajo se deja para después.

### Lo que produce

**Una cartera priorizada.** Pocas iniciativas, ordenadas por cuánto atacan la restricción del ámbito; la regla de orden completa está en el módulo 14. Como partida, solo pueden no atacarla los habilitadores (módulo 14) y las obligaciones legales, y cada una de esas lleva su motivo escrito. La cartera no es una lista de deseos: crece solo si algo sale.

**El nuevo diseño del trabajo.** Antes de elegir la herramienta, se decide cómo va a trabajar la gente: qué decisiones toma cada rol, qué información necesita, qué deja de hacer y qué empieza a hacer. La herramienta se elige después, para ese trabajo.

**Los aceleradores por fase.** Qué aceleradores entran, cuándo, y cumpliendo la regla de entrada. Cuando el acelerador es un sistema de IA, en la puerta de diseño se fija también con qué nivel de autonomía entra en el piloto y hasta qué nivel puede subir (capítulo 17).

**Los criterios del piloto.** Escritos y firmados antes de empezar: qué tiene que mejorar, cuánto, en qué plazo y qué se hará si no ocurre. Se expresan como delta mínimo respecto a la línea base y, además, en la unidad de cada indicador. Los objetivos, los pesos y los umbrales se fijan y se firman aquí, como dice el capítulo 18. Desde la versión 1.6 el criterio escribe también qué decisión va a cambiar el resultado del piloto: qué se hará distinto si sale bien y qué se hará distinto si sale mal. Un piloto cuyo resultado no cambiaría ninguna decisión solo hace una demostración, no una prueba.

**El modelo económico.** Cuánto cuesta, cuándo llegan los beneficios y cómo se reparten. Tiene que prever el valle de la curva J, que se explica en el capítulo 18.

**La decisión escrita por opción.** Para cada opción de diseño que se considera seriamente, un documento de una página que responde a las cinco preguntas de la puerta. El anexo C recoge la plantilla, que es el núcleo de esa página. Lo que piden los módulos va aparte, en un anexo a la decisión, y solo las líneas que son obligatorias para el alcance de la iniciativa.

## 11. Las cinco preguntas de la puerta

La puerta de diseño es donde los tres elementos se protegen, y por eso tiene cinco preguntas en lugar de una.

{{img:fig-puerta.png|16}}

1. **¿Ataca la restricción?** La pregunta clásica de Goldratt y Rumelt. Si no la ataca, puede ser una buena idea, pero no es la prioridad.
2. **¿Acelera, automatiza o aumenta?** Zuboff formuló en 1988 la pregunta de fondo con dos verbos, automatizar o informar. Desde la versión 1.4 son tres. Acelerar es hacer la misma tarea más rápido con la misma persona; automatizar es sacar a la persona del circuito; aumentar, que ocupa el lugar del informar de Zuboff, es que la persona haga algo que antes no podía, o lo haga mejor, con la tecnología a su lado. Se responde por tarea, porque una misma opción suele mezclar los tres. Si la persona sale del circuito, automatiza. Si sigue y el resultado que se espera es solo tiempo, acelera. Si se espera mejor calidad o algo que antes no hacía, aumenta, y se dice con qué indicador se va a ver. Ninguno es bueno o malo por sí solo, y hay que elegir a propósito. Si la respuesta es acelerar, se escribe a dónde va el tiempo que se gana, y ese destino se confirma antes de aprobar la escala (módulo 9). Y en los tres casos se escribe qué tiene que ser cierto para que lo elegido dé el resultado que se espera (capítulo 17). Dentro de esta pregunta van dos más desde la versión 1.5: ¿crea tareas nuevas para las personas o solo desplaza las que había?, que es la distinción de Acemoglu y Restrepo (2019); y ¿qué pericia queda en el puesto después?, porque, como muestran Autor y Thompson (2025), el efecto sobre el puesto es distinto si la tecnología retira sus tareas sencillas o sus tareas expertas.
3. **¿Qué le pasa a cada fila del mapa de lo que nadie escribió?** Se queda en la persona y la tecnología la ayuda, pasa al sistema de forma revisable, o se pierde.
4. **¿Quién responde de los errores cuando el sistema se equivoque, y quién enseña lo que la tarea enseñaba?** La primera mitad es de gobierno. La segunda es de personas: si la tarea que desaparece era la que formaba a los nuevos, alguien tiene que asumir esa enseñanza.
5. **¿Hace crecer a la vez a los tres elementos, o abarata uno a costa de los otros?** La pregunta de síntesis.

Se puede aprobar una opción que pierde conocimiento, o una que automatiza y le quita criterio a alguien. Lo que el método no permite es aprobarlas sin saberlo.

!! Pregunta abierta. ¿Cinco preguntas son demasiadas? | Una crítica razonable es que cinco preguntas convierten la puerta en un trámite pesado. Mi respuesta provisional es que, para una iniciativa pequeña, las cinco se responden en media página, y que la que más se resiste a responderse suele ser la que más importa. Pero no lo he contrastado en programas grandes con decenas de iniciativas. Si se demuestra que la puerta se vuelve formulario, habrá que reducirla o graduarla por tamaño de la iniciativa.

## 12. Fase 3. Piloto

El piloto prueba en pequeño, con gente real y datos reales, lo que el diseño ha decidido. Su error típico es elegir el entorno más fácil, el equipo más motivado o el servicio más sencillo, que funciona muy bien y no representa al resto.

{{img:fig-piloto.png|16}}

>> Un piloto que no representa no prueba nada.

**Cómo elegir el entorno.** Con al menos una de las condiciones difíciles del resto de la organización: un equipo con rotación, un volumen alto, casos raros, sistemas antiguos. La pregunta útil es dónde va a fallar primero, si tiene que fallar.

**Con qué se compara.** Siempre que se pueda, con un equipo o un periodo de comparación que no tenga el cambio, además de con la línea base. La línea base trae la variación normal de cada indicador, y un cambio menor que esa variación no cuenta ni como mejora ni como retroceso. Si no hay con qué comparar, los resultados lo dicen por escrito.

**Qué produce.** Resultados contra la línea base y contra la comparación elegida, lecciones aprendidas, ajustes al diseño y riesgos descubiertos.

**La puerta.** Tres salidas: pasar si se cumplen los criterios; ajustar y repetir si el resultado es prometedor pero incompleto; retirar si no funciona. Los criterios se escribieron antes, en el diseño, y no se reescriben al ver el resultado. El criterio tipo, cuyas clases de indicador explica el capítulo 18, es este: el delta supera el mínimo firmado, ningún indicador de guarda baja de su suelo, y los indicadores para los que el modelo económico prevé valle no bajan más de lo previsto. Si el resultado queda dentro de la variación normal del indicador respecto al umbral, decide el patrocinador y lo motiva por escrito. La decisión se firma como todas las de puerta (capítulo 18): el patrocinador firma y alguien ajeno al equipo del programa contrafirma. Y antes de aprobar el piloto se comprueba lo que el criterio dejó escrito en el diseño (capítulo 10): qué decisión va a cambiar su evidencia y quién la toma. Si nadie sabe contestar, el piloto todavía no está listo para empezar.

**Repetir, una vez.** Un piloto se repite una vez como máximo y con los mismos criterios. La segunda vez que no los cumple, se retira o vuelve a diseño.

**Retirar.** Retirar en la puerta del piloto solo exige anotar qué pasa con las filas del mapa y con las personas, que son las preguntas 3 y 4 de la puerta de diseño. Las cinco preguntas completas se piden para retirar algo que ya está en escala o en sostenimiento. Quien propone la retirada queda protegido por escrito.

**Criterio de parada y revisión a noventa días.** Desde la versión 1.7, cada piloto nace con dos cosas escritas además de los criterios para pasar: qué resultado lo detiene antes de tiempo y una fecha de revisión a noventa días como máximo. Cuando el piloto dura más de noventa días, esa revisión es intermedia y la puerta sigue al final. En la revisión se decide con lo que haya si el piloto sigue, se ajusta o se para. Un piloto que sigue abierto sin que nadie haya decidido nada es la forma más común de no retirar.

**El registro de supuestos.** Toda opción de diseño descansa en supuestos: que la gente la usará, que los datos sirven, que el caso raro es poco frecuente. Se escriben en el diseño y en cada puerta se anota cuáles se han confirmado, cuáles han caído y cuáles siguen sin probar. Es la planificación guiada por el descubrimiento de McGrath y MacMillan aplicada a las puertas. Pasar una puerta con los supuestos principales sin probar es pasarla por fe.

**Los casos de prueba.** Antes de empezar, quien hace el trabajo prepara un conjunto de casos reales, con los difíciles incluidos, y dice qué cuenta como buen resultado en cada uno. El sistema los pasa antes del piloto, vuelve a pasarlos en cada puerta y también cada vez que cambian el modelo, las herramientas o los permisos, sea cual sea su nivel de autonomía. Si el proveedor cambia el modelo durante el piloto, los casos se repiten y el cambio se anota en los resultados. El módulo 24 lo desarrolla para los agentes, pero vale para cualquier sistema de IA.

**El espacio para fallar.** Amy Edmondson ha documentado que los equipos aprenden cuando creen que es seguro asumir riesgos interpersonales: preguntar, admitir un error, proponer algo que puede salir mal. Si el piloto castiga el fallo, la gente lo esconde, y el piloto deja de informar. El patrocinador tiene que decir, antes de empezar y en voz alta, que retirar es una salida legítima.

!! Pregunta abierta. ¿Funciona la regla de la retirada en una organización muy jerárquica? | El método dice cuándo se retira y quién lo firma: los criterios están firmados antes, la retirada la firma el patrocinador, la contrafirma una persona ajena al equipo del programa (sin interés en la iniciativa) y quien la propone queda protegido por escrito (capítulo 18). Lo que queda abierto es si eso basta cuando el piloto es de alguien con poder o ya se ha gastado mucho. La regla puede estar escrita y nadie atreverse a aplicarla. No sé si funciona en organizaciones muy jerárquicas. Es una de las preguntas que más necesita casos reales.

## 13. Fase 4. Escala

La escala extiende lo que ha funcionado. Su error típico es escalar la herramienta sin escalar los roles y los incentivos: la herramienta llega a toda la organización, pero el trabajo de cada persona sigue evaluándose como antes, y el resultado vuelve a donde estaba.

{{img:fig-escala.png|16}}

**Despliegue por etapas.** Nunca de golpe. Cada etapa tiene su propia mini puerta: los indicadores tienen que aguantar al ampliar. La decide el dueño operativo con los datos que certifica medición. Si la mejora del piloto se diluye al pasar a más equipos, para, lo lleva al comité de puertas y se entiende por qué antes de seguir.

**Formación en el puesto.** Se da acompañando mientras se trabaja; un curso de un día no basta. Lo que funciona en la escala casi siempre es lo que aprendieron quienes usaron la herramienta en el piloto, no lo que estaba en el manual. La tabla dice qué tiene que saber cada perfil y quién se lo enseña. Las horas las fija cada programa (anexo G), y cómo se comprueba que se sabe lo decide la persona responsable de la adopción.

| Perfil | Qué tiene que saber antes del piloto | Qué tiene que saber antes de la escala | Quién lo imparte |
|---|---|---|---|
| Dirección y mandos | Qué decide cada puerta y qué criterios se han firmado; qué puede y qué no puede hacer la herramienta en ese trabajo | Cómo cambian los roles, la evaluación y los incentivos de su equipo; cómo se leen el uso, la capacidad y el resultado | Dirección del programa, con medición |
| Quien usa la herramienta | Las reglas de uso y los datos permitidos; en qué tareas ayuda y en cuáles falla; cómo avisar de un error y cómo dejar de usarla en su caso | El trabajo rediseñado y las normas de su equipo | Diseño del trabajo y los referentes, en el puesto |
| Quien supervisa o es dueño | El nivel de autonomía y los criterios para cambiarlo; cómo se revisa lo que produce; cómo se para y cómo se reanuda; los casos de prueba | La ficha y el inventario; qué se hace cuando cambia el modelo; los indicadores que le toca leer | Tecnología y datos, con medición |

**Varios referentes por área.** Un referente es una persona que ya usa bien la herramienta, que se reconoce como tal y que tiene tiempo reconocido para ayudar a los demás. Los primeros salen de quienes la usaron en el piloto. En otros textos se les llama campeones; en este documento son siempre referentes. Los usuarios avanzados del capítulo 15 son el grupo que prueba antes que nadie, y de él pueden salir referentes. La comunidad de práctica existe desde antes del primer piloto, porque es una de las piezas del entorno (capítulo 17). Desde la versión 1.6, en la escala se amplía con varios referentes por área, para no descansar en uno solo. Llamo área a la unidad que tiene un mando directo; su tamaño en personas no lo fijo (anexo G). Así la formación en el puesto no depende de quien más usa la herramienta, y el saber de usarla bien no se concentra. Esto se cruza con la columna de concentración del mapa: si en un área solo una persona sabe usar bien la herramienta, esa fila vuelve a ser de una sola persona y el riesgo se ha movido de sitio, no ha desaparecido. Mi punto de partida es al menos dos referentes por área. No tengo una cifra mejor, y seguramente depende del tamaño del área.

**Quién lleva la adopción.** Desde la versión 1.7, la escala tiene una persona responsable de la adopción, con nombre y con tiempo, distinta de quien despliega la herramienta (módulo 4). Nombra a los referentes a propuesta de cada equipo, los coordina, recoge lo que no funciona y lo lleva al comité. Los referentes tienen horas reconocidas en su jornada, con un mínimo escrito que fija cada programa. Si la adopción es tarea de todos y de nadie en concreto, se queda en la formación inicial.

**Normas de equipo.** Que cada persona rinda más con IA no significa que el equipo rinda más. Cada equipo acuerda por escrito cuándo se usa la IA y cuándo no, cómo se avisa de que algo está hecho con ella, quién revisa qué, y qué no se entrega sin haberlo leído. Lo último importa: un trabajo generado deprisa y pasado sin revisar traslada el coste a quien lo recibe.

**El modelo operativo cambia con la fase.** En el diagnóstico, el diseño y el piloto conviene un equipo central, porque hay poco saber y hay que concentrarlo. En la escala, las áreas se hacen dueñas de sus casos y el centro conserva lo común: gobierno, plataforma, estándares y medición. En el sostenimiento el centro queda como apoyo. Es una regla de práctica; no conozco datos que comparen los modelos (módulo 4).

**Roles, carreras e incentivos.** Es la parte que más se olvida. Si el trabajo cambia y la evaluación no, la gente hace lo que se evalúa. Una señal clara de fallo es el uso alto de las herramientas nuevas con resultados iguales que antes.

**La puerta de escala.** Los indicadores aguantan al ampliar, y los tres elementos aguantan la carga: hay personas formadas, el conocimiento está donde tiene que estar y la tecnología soporta el volumen. En esta puerta se comprueba además si la restricción del ámbito sigue siendo la misma. Si se ha movido, que es lo esperable cuando una mejora funciona, se anota y el siguiente ciclo parte de la nueva. Los criterios los propone medición y los firma el patrocinador al pasar la puerta del piloto, antes de la primera etapa. Decide el patrocinador, oído el comité de puertas (capítulo 18).

## 14. Fase 5. Sostenimiento

El sostenimiento tiene que conseguir que la mejora siga cuando el equipo del programa se vaya. Es la fase que menos se planifica, porque el programa ya ha declarado su éxito. John Kotter lo identificó en 1995 como una de las causas clásicas del fracaso: declarar la victoria demasiado pronto.

{{img:fig-sostenimiento.png|16}}

**Lo que tiene que existir.** Un dueño operativo con nombre, que acepte la responsabilidad. Un presupuesto recurrente, no el del proyecto. Un cuadro de indicadores en régimen, que se mire sin que nadie del programa lo pida. Un calendario de supervisión del programa, con la revisión de supuestos incluida; el anexo H reúne las revisiones periódicas que pide el documento.

**Evaluación que no termina.** Un sistema de IA cambia aunque nadie lo toque: el proveedor actualiza el modelo, cambian los datos, cambia lo que la gente le pide. Desde la versión 1.7, el calendario incluye volver a pasar los casos de prueba en cada periodo de medición y siempre que cambien el modelo, las herramientas o los permisos, y la auditoría interna revisa una vez al año que el inventario y los registros se corresponden con lo que está en uso.

**La puerta.** El dueño acepta la responsabilidad por escrito y los indicadores aguantan dos periodos de medición sin el equipo del programa: los de avance mantienen su delta y los de guarda no bajan de su suelo (el periodo de medición se define en el capítulo 8). Sin el equipo significa que nadie del programa hace trabajo del servicio ni empuja los indicadores; el apoyo del centro, cuando el área lo pide, no cuenta. Si los indicadores caen al irse el equipo, la mejora era del equipo, no de la organización.

**Quién la convoca y quién decide.** La puerta de sostenimiento la convoca el dueño operativo ante el patrocinador, que decide y firma como en las demás puertas (capítulo 18). Pasarla cierra el programa para ese ámbito. Ajustar y repetir significa aquí que el equipo vuelve a lo que falló y los dos periodos empiezan a contar de nuevo. Retirar algo que ya está en sostenimiento pide las cinco preguntas completas (capítulo 12).

**El retorno al diagnóstico.** Lo aprendido en el sostenimiento alimenta el diagnóstico del siguiente ciclo. Aquí el tronco se cierra sobre sí mismo y pasa a ser un ciclo.
