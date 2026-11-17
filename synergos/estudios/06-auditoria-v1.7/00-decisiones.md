# Decisiones de consolidación para la versión 1.8 (17 nov 2026)

Alejandro pide corregir todo lo que encontró la auditoría (A-contradicciones.md y B-huecos-ambiguedades.md). Donde los hallazgos tocan varios ficheros hay que elegir una sola respuesta. Estas son las elegidas. Son la referencia única: cualquier frase del documento que diga otra cosa se cambia para que coincida. La versión 1.8 no añade temas nuevos; cierra, unifica y aligera.

## Reglas generales de la 1.8

- No se inventa experiencia ni datos. Si una corrección pide una cifra o una experiencia del autor que no está ya en el documento, no se pone: se deja la regla sin número y se dice quién lo fija.
- Las propuestas sin probar se llaman propuestas. A la fecha ningún programa ha aplicado el método completo, y el documento lo dice.
- Estilo del documento: primera persona del autor, frases llanas, sin rayas largas (no usar el carácter —), sin contrastes del tipo «no es X, sino Y», sin iconos. Los recuadros de pregunta abierta empiezan por `!! Pregunta abierta. Pregunta | texto` en una sola línea.
- Cuando una regla cambia se anota «Desde la versión 1.8» solo si hace falta para que el lector no se pierda. No se multiplican esas etiquetas.
- Se quita o se fusiona antes que añadir. Si dos sitios dicen lo mismo, uno manda y el otro remite.

## Dónde vive cada cosa (el sitio que manda)

| Tema | Sitio que manda | Los demás remiten |
|---|---|---|
| Qué recorre el tronco, tabla de fases, diagnóstico paso a paso, comparación y repetición del piloto, formación | 03-tronco.md | |
| Regla de entrada, comité de puertas, quién firma, quién decide qué, inventario único, uso informal y herramientas de uso general, medición (delta, clases de indicador, umbrales, indicadores obligatorios), dimensionamiento | 05-orden.md, capítulo 18 | cap. 6, cap. 17, módulos 3, 5, 11, 23, 24 |
| Escala de autonomía y su techo | 04-elementos.md, capítulo 17 | módulo 24 |
| Ficha del agente y controles por nivel | 06g, módulo 24 | cap. 17 |
| Funciones del equipo y otros papeles | 06b, módulo 4 | |
| Seguridad y datos personales | 06c, módulo 11 | cap. 18 |
| Administración pública | 06d, módulo 13 | |
| Qué es obligatorio según alcance (núcleo), encaje de los 24 módulos y causa a la que responde cada uno | final de 06g (cierre de la Parte V) | 06d, 06f |
| Glosario, plantillas, madurez, fuentes, versiones, valores de partida y calendario de revisiones | 08-anexos.md | |
| Estado real del método, reglas para cambiarlo, preguntas abiertas | 01-por-que.md y 07-mejora.md | |

## Decisiones

**D1. Regla de entrada.** Una sola redacción: «Un acelerador entra en el servicio solo si las condiciones que necesita, en los tres elementos y en el gobierno, están en nivel 2 en el ámbito». Se aplica a la tecnología dentro del servicio. La IA como herramienta del equipo que transforma solo exige reglas de uso y datos autorizados. El anexo D añade una fila de gobierno y deja de decir que la escala se aplica «a cada acelerador». El nivel 2 de conocimiento se redacta sin nombrar piezas del método.

**D2. Elemento y acelerador.** El elemento tecnología es la capacidad de la organización para gobernar y usar tecnología. Un acelerador es una tecnología concreta que se activa en un ámbito. El glosario lleva la lista de aceleradores que el documento reconoce (se extrae del texto, no se amplía). El límite de «pocas cosas a la vez» se refiere a aceleradores; lo que el método pide siempre (rediseño del trabajo, medición, gobierno) no cuenta en ese límite. Se unifica «por ciclo».

**D3. La IA y el diagnóstico.** La IA como herramienta del equipo que transforma se considera en todas las fases. La IA dentro del servicio entra solo si el diagnóstico lo justifica, y un programa Synergós puede terminar sin ella.

**D4. Qué recorre el tronco.** Un programa tiene uno o varios ámbitos. Cada ámbito hace un diagnóstico. Del diagnóstico salen iniciativas, que forman la cartera. Cada iniciativa compara opciones en el diseño y recorre piloto, escala y sostenimiento. Hay una restricción por ámbito. Como partida, solo los habilitadores (módulo 14) y las obligaciones legales pueden no atacarla. En cada puerta de escala se comprueba si la restricción sigue siendo la misma.

**D5. Ciclo y periodo de medición.** «Ciclo» queda reservado para el recorrido de las cinco fases en un ámbito. «Periodo de medición» es el intervalo, fijado en el diseño, en que se leen los indicadores (por defecto, un trimestre). La puerta de sostenimiento pide «dos periodos de medición sin el equipo del programa»; «sin el equipo» significa sin nadie del programa haciendo trabajo del servicio ni empujando los indicadores. Las revisiones periódicas se expresan en periodos de medición. Las dos entradas van al glosario.

**D6. Comité de puertas.** Deciden cuatro: el patrocinador, que firma; el dueño operativo; el responsable de medición, que certifica los datos y no la decisión; y una persona ajena al equipo del programa (segunda línea o finanzas), que contrafirma. Son oídos antes, por escrito: quien hace el trabajo, el mando intermedio del ámbito, quien defiende a quien recibe el servicio, el área de tecnología y, cuando la decisión toca condiciones de trabajo, la representación legal. Regla: decide el patrocinador oído el comité, y las objeciones quedan escritas. En el programa acotado no hay comité: firma el patrocinador con quien dirige el programa y contrafirma alguien ajeno. Toda decisión de puerta se firma así; el anexo C lo refleja.

**D7. Retirada.** Sigue la regla de D6: firma del patrocinador y contrafirma de alguien sin interés en la iniciativa. Quien la propone queda protegido por escrito. Retirar en la puerta del piloto solo exige anotar qué pasa con las filas del mapa y con las personas (preguntas 3 y 4). Las cinco preguntas completas se piden para retirar algo que ya está en escala o en sostenimiento. El recuadro del capítulo 12 y la entrada del capítulo 21 dejan de proponer una regla y dicen qué queda abierto: si funciona en organizaciones muy jerárquicas.

**D8. Quién decide qué (tabla del capítulo 18).** Se parte la fila del proveedor: cambiar de versión de modelo dentro de la misma solución lo decide el dueño, con nueva evaluación; sustituir la solución o el proveedor lo decide el comité. Se añaden dos filas: elegir plataforma y arquitectura, y aceptar una solución en producción y operarla, que decide el área de tecnología con el comité como consultado. Parar: cualquier persona de la capa de uso puede dejar de usarlo en su caso y pedir la parada al dueño, que responde en el día; el dueño puede parar el servicio entero; reanudar lo decide el dueño y lo anota. El módulo 5 remite a esta tabla.

**D9. Dueño.** El dueño de la solución es el dueño operativo, el del agente y quien figura en el inventario: una sola persona. Otros dueños distintos (de los datos, del beneficio, de la estrategia) se nombran con su apellido. Entrada en el glosario.

**D10. Cadenas de agentes.** Cada agente tiene su dueño. El dueño del flujo responde de la cadena entera ante quien recibe el servicio. El recuadro del módulo 11 remite a esta regla y deja abierto solo lo que sigue sin resolver.

**D11. Inventario único.** Una sola definición, en el capítulo 18: los campos de la ficha del módulo 24 más riesgo, proveedor, incidentes, las seis anotaciones de personas y conocimiento del capítulo 17 y un campo de estado (en evaluación, en experimento, aprobado, retirado). El capítulo 17, el módulo 11 y el módulo 24 remiten. Un uso contado puede seguir en estado «en evaluación», con las reglas generales de datos, hasta que haya respuesta.

**D12. Uso informal y herramientas de uso general.** Es regla (capítulo 18), ya no pregunta abierta. Los recuadros del capítulo 17 y del capítulo 21 dicen solo lo que queda abierto. Se añade la vía corta para herramientas de uso general (un asistente para toda la plantilla): se aprueban con cuatro condiciones escritas (reglas de uso, datos permitidos, formación mínima, indicadores de uso y capacidad) y cada uso que entre en un servicio pasa después por el tronco. La garantía de no sanción cubre haber probado la herramienta; no exime de comunicar y tratar una posible fuga de datos.

**D13. Controles por nivel (módulo 24).** Casos de prueba superados y nueva evaluación tras cada cambio de modelo, de herramientas o de permisos son previos a la tabla y valen para todos los niveles. La cabecera pasa a «Controles que tienen que existir para operar en este nivel». El nivel de entrada al piloto se fija en la puerta de diseño. «Revisar todo no funciona» se refiere a los niveles 3 y 4; en el nivel 2 la persona revisa cada propuesta. «Puerta de autonomía» entra en el glosario: decisión de subir o bajar un nivel, que puede tomarse en cualquier momento con los criterios escritos.

**D14. Techo de autonomía.** Las decisiones que afectan a derechos de las personas, que no se pueden deshacer o que hay que poder explicar a quien las recibe se quedan como máximo en el nivel 2, salvo que el análisis jurídico del caso permita otra cosa.

**D15. Tasa de corrección.** Para subir del nivel 2: la tasa es baja y estable y una muestra revisada a ciegas por otra persona confirma la tasa de error. Señal de retirada (módulo 3): la tasa vuelve a subir o se estanca por encima del valor fijado. En el módulo 3 se habla de «indicador de capacidad», no de «indicador de criterio».

**D16. Medición.** Hay dos clases de indicador. Los de avance tienen objetivo y entran en el delta. Los de guarda solo tienen un suelo y no entran en la media: se cumplen o no. El objetivo de cada indicador de avance se fija y se firma en el diseño junto con los pesos, con su justificación, y no cambia hasta el siguiente ciclo. El delta de un indicador tiene un máximo del cien por cien. Los criterios de puerta se escriben además en la unidad del indicador. Umbrales: los propone medición, con dos referencias (la variación normal del indicador en la línea base y el mínimo que haría rentable la escala según el modelo económico), y los firma el patrocinador. Un cambio menor que la variación normal no cuenta ni como mejora ni como retroceso. Si el resultado queda dentro de esa variación respecto al umbral, decide el patrocinador y lo motiva por escrito.

**D17. Criterio tipo del piloto.** Sustituye a «ningún indicador retrocede»: ningún indicador de guarda baja de su suelo, y los indicadores para los que el modelo económico prevé valle no bajan más de lo previsto.

**D18. Indicadores obligatorios.** Al menos uno por elemento. En tecnología, el uso y el resultado. La capacidad es un indicador de personas que se lee en pareja con el uso. Indicador de personas por defecto, provisional mientras la pregunta sigue abierta: proporción de casos fuera de patrón que el equipo resuelve sin escalar, medida por muestreo antes y durante el piloto, más la carga percibida como indicador de guarda. Una tabla en el capítulo 18 lista los obligatorios y los opcionales y dice de qué clase es cada uno. Las medidas de capacidad y de supervisión se leen agregadas por equipo; una lectura individual se pacta antes con el equipo y con la representación legal y se anota como vigilancia en el inventario. El texto dice cuántas reglas de medición hay de verdad, o deja de contarlas.

**D19. Tres verbos.** Se responde por tarea. Si la persona sale del circuito, automatiza. Si sigue y el resultado esperado es solo tiempo, acelera. Si se espera mejor calidad o algo que antes no hacía, aumenta, y se dice con qué indicador. El glosario se actualiza a los tres verbos. El ejemplo del centro de atención se presenta como lo que es.

**D20. Duraciones.** Programa acotado: un equipo, hasta la puerta del piloto en menos de seis meses. La revisión a noventa días es intermedia cuando el piloto dura más; la puerta sigue al final. Un piloto se repite una vez como máximo con los mismos criterios; la segunda vez que no los cumple, se retira o vuelve a diseño. Un cambio de modelo durante el piloto obliga a repetir los casos de prueba. Se compromete el resultado de la siguiente puerta y se reserva, sin comprometer resultados, una horquilla de presupuesto para las fases siguientes, que cada puerta libera o devuelve. Los cien días se financian como gasto de diagnóstico.

**D21. Entregables y plantilla de puerta.** El capítulo 9 habla de seis entregables básicos y remite a lo que añaden el capítulo 18 y los módulos. La plantilla del anexo C es el núcleo de una página. Lo que piden los módulos (techo de autonomía, tres necesidades, cinco puntas, aportaciones, roles que se reducen, asistir o vigilar, huella) va en un «anexo a la decisión», y solo las líneas que la tabla del núcleo marque como obligatorias para ese alcance.

**D22. Núcleo mínimo.** Tabla «Qué es obligatorio según alcance» al cierre de la Parte V, con columnas puntual, de flujo y de sistema, y valores obligatorio, recomendado o no aplica. Siempre obligatorio: restricción nombrada, línea base, mapa del trabajo afectado, decisión de puerta de una página, un indicador por elemento, criterio de parada, cómo se deshace y dueño. Se añade en una iniciativa de flujo: rediseño del trabajo (módulo 2), casos de prueba, registro de supuestos, responsable de adopción y referentes, destino del tiempo. Se añade en una de sistema: modelo económico con valle, las tres miradas y gobierno completo. La ficha del agente es obligatoria siempre que haya un agente. Quitar una pieza lo decide el patrocinador y se anota en el registro de decisiones. La misma tabla, o una contigua, dice en qué fases pesan los 24 módulos y a qué causa del capítulo 2 responde cada uno; los que no respondan a ninguna se marcan como extensión sin causa documentada.

**D23. Estado real del método.** «Cómo leer» dice que a la fecha ningún programa ha aplicado el método completo. Se quitan o matizan las frases que suenan a método ya aplicado («he visto funcionar», «cada trimestre reviso» pasa a futuro). La regla 1 para cambiar el método se rebaja a lo que de verdad se hace: fuente identificada, y la ficha pendiente se marca. No se inventa una tabla de piezas probadas: eso lo tiene que decir el autor.

**D24. Afirmaciones y fuentes.** Se aplican las correcciones F2 a F15 de la auditoría B tal como están propuestas: rebajar lo que dice más que su fuente, marcar como lectura propia o como experiencia propia lo que lo es, y marcar las cifras de los casos compuestos como ilustrativas.

**D25. Administración pública.** Tabla breve en el módulo 13, «Qué cambia en una administración», con cinco filas (incentivos y carrera, representación del personal, decisiones automatizadas sobre ciudadanos, seguridad, presupuesto) y las columnas qué pide el método, qué puede limitarlo y qué se hace en su lugar. Sin citar artículos ni fechas, y con la frase «a comprobar con asesoría jurídica».

**D26. Anexos nuevos.** Anexo G, «Valores que fija cada programa»: una fila por expresión sin número del documento (suficiente, baja y estable, pocos, área, etc.), quién la fija y con qué referencia; solo lleva valor donde el documento ya da uno. Anexo H, «Calendario de revisiones»: una fila por revisión periódica que pide el documento, frecuencia y responsable, fusionando las que coinciden.

**D27. Lo que no se corrige porque depende del autor.** Esfuerzo orientativo del equipo por fase (H10), tamaño de «área» en personas (A9), valores numéricos de partida (A10) y qué piezas usó el autor en programas reales (F1). Se anotan como pendientes en el capítulo 21 o donde corresponda, sin inventar.
