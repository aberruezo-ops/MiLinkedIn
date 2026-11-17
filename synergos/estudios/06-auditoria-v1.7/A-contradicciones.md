# Auditoría A. Coherencia interna de "Synergós. El método" v1.7

Alcance: los catorce ficheros 01-por-que.md a 08-anexos.md de synergos/documentos/metodo/, leídos enteros y en orden. Solo lectura. Solo contradicciones e incoherencias con los dos sitios citados. No se valora estilo ni fondo. No se ha comprobado ningún dato contra fuentes externas.

Formato de cada hallazgo: sitios que chocan (fichero:línea aproximada), cita literal breve, por qué es un problema, corrección mínima.

Total: 57 hallazgos (12 de gravedad alta, 23 media, 22 baja).

Patrón general: casi todos los choques vienen de que las versiones 1.4 a 1.7 añadieron reglas en los capítulos 12 a 18 y en los módulos 23 y 24 sin actualizar cuatro sitios que resumen el método: la tabla de fases del capítulo 8, los principios del capítulo 6, las preguntas abiertas (recuadros y capítulo 21) y los anexos A, B, C y D.

---

## Gravedad alta

Un lector que aplique el método haría algo distinto según la página que lea.

### A1. La regla de entrada de los aceleradores tiene tres formulaciones incompatibles

- 02-arquitectura.md:44 (Principio 2): "Un acelerador entra en una fase solo si los tres elementos están, para esa fase, al menos en el nivel 2 de madurez."
- 05-orden.md:90 (cap. 18): "un acelerador se activa solo si sus condiciones están en nivel 2 o más. La IA en piloto dentro del servicio exige gobierno y personas en nivel 2 como mínimo."
- 05-orden.md:79: "La escala de madurez tiene cuatro niveles y se aplica a cada elemento y a cada acelerador." Frente a 08-anexos.md:68 (anexo D), que solo tiene columnas Personas, Conocimiento y Tecnología.
- 04-elementos.md:91: la IA es "Herramienta del equipo desde el primer día del diagnóstico". Frente a 08-anexos.md:73: Conocimiento en nivel 2 exige "Hay un mapa hecho", y el mapa es un entregable del diagnóstico.

Problema: (a) "los tres elementos" no es lo mismo que "sus condiciones", ni que "gobierno y personas"; el gobierno no es un elemento sino parte del orden, y no tiene escala en el anexo D. (b) El texto dice que la escala se aplica también a cada acelerador, pero no hay descripción de niveles para aceleradores. (c) Leído literalmente, el Principio 2 prohíbe usar IA en el diagnóstico, porque Conocimiento no puede estar en nivel 2 antes de hacer el mapa, y el capítulo 17 la recomienda desde el primer día.

Corrección mínima: dejar una sola redacción en el Principio 2 y en el capítulo 18 (por ejemplo, "las condiciones que ese acelerador necesita, en los elementos y en el gobierno, están en nivel 2"), decir que la regla se refiere a la IA dentro del servicio y no a la IA como herramienta del equipo, y añadir al anexo D una fila o columna de gobierno o quitar "y a cada acelerador".

### A2. Quién decide una retirada: cuatro respuestas distintas

- 03-tronco.md:123 (recuadro, cap. 12): "Propuesta provisional: la retirada la firman dos personas, el patrocinador y alguien sin interés en la iniciativa (por ejemplo, el responsable de medición)". Repetido como propuesta en 07-mejora.md:55.
- 05-orden.md:28 (tabla "Quién decide qué", 1.7): "Retirar una solución | Comité de puertas, con la firma de alguien sin interés en ella".
- 04-elementos.md:158: "La decisión la toma el comité de puertas".
- 06a-detalle-personas-trabajo.md:142: "la puerta del ciclo puede decidir bajar de nivel de autonomía o retirarla".
- 08-anexos.md:66 (anexo C): "Firma | Patrocinador y responsable de medición".
- 05-orden.md:96: en un programa acotado "las puertas las preside el patrocinador con el responsable" (no hay comité).

Problema: la misma decisión aparece como pregunta abierta sin resolver ("No resuelve el quién"), como regla cerrada en la tabla de 1.7 y con firmantes distintos en la plantilla. En un programa acotado la tabla de 1.7 remite a un comité que no existe.

Corrección mínima: elegir una regla, escribirla en la tabla del capítulo 18 con su variante para programa acotado, y convertir el recuadro del capítulo 12 y la entrada del capítulo 21 en referencia a esa regla (o marcar la fila de la tabla como provisional).

### A3. Sustituir una solución o cambiar de proveedor: comité o dueño

- 04-elementos.md:158: "se vuelve a decidir, para cada solución en uso, si se mantiene, se sustituye por otra comprada, se construye algo propio o se retira. La decisión la toma el comité de puertas [...] No la toma el proveedor ni el equipo que la construyó".
- 05-orden.md:30: "Cambiar de proveedor o de modelo | Dueño de la solución, con nueva evaluación antes de volver al servicio".

Problema: sustituir una solución por otra comprada es cambiar de proveedor. Un capítulo dice que lo decide el comité y que no lo decide quien tiene interés en mantenerla; el siguiente lo deja en el dueño.

Corrección mínima: distinguir en la tabla "cambiar de versión de modelo dentro de la misma solución" (dueño) de "sustituir la solución o el proveedor" (comité de puertas).

### A4. Casos de prueba y nueva evaluación: obligatorios siempre o solo desde ciertos niveles

- 03-tronco.md:119: "El sistema los pasa antes del piloto y vuelve a pasarlos en cada puerta. [...] vale para cualquier sistema de IA."
- 03-tronco.md:151: "volver a pasar los casos de prueba en cada ciclo y siempre que cambie el modelo".
- 06g-innovacion-agentes.md:99: "El agente lo pasa antes del piloto, en cada puerta y cada vez que cambia el modelo que hay debajo."
- 06g-innovacion-agentes.md:88-91 (tabla de controles): nivel 1 solo pide "Ficha e inventario; datos acotados a la finalidad"; el "conjunto de casos de prueba superado" entra en el nivel 2; la "nueva evaluación tras cada cambio de modelo, de herramientas o de permisos" entra en el nivel 4.

Problema: según la tabla, un sistema en nivel 1, 2 o 3 no necesita repetir la evaluación cuando cambia el modelo, y uno en nivel 1 puede entrar en piloto sin casos de prueba. Según el capítulo 12, el 14 y el mismo módulo 24, ambas cosas son obligatorias siempre.

Corrección mínima: mover "casos de prueba superados" y "nueva evaluación tras cada cambio de modelo" a la fila del nivel 1 de la tabla de controles (o decir que son previos a la tabla), y dejar en el nivel 4 solo lo que es propio de él.

### A5. El criterio de paso del piloto choca con la curva J que el propio método prevé en el piloto

- 05-orden.md:63: "el piloto pasa si el delta del ciclo supera el cuarenta por ciento y ningún indicador retrocede". Lo mismo en 08-anexos.md:61: "Delta mínimo del ciclo; ningún indicador retrocede".
- 06d-detalle-comunicacion-cartera.md:13: "Es el momento del piloto y de las primeras etapas de la escala. La productividad baja (la curva J)".
- 05-orden.md:47: "durante un tiempo la productividad medida baja antes de subir. Muchos programas se cancelan en ese valle".

Problema: un capítulo dice que en el piloto la productividad baja y que cancelar ahí es el error clásico; otro fija como criterio tipo de la puerta del piloto que ningún indicador retroceda. Aplicado tal cual, el criterio retira justo en el valle.

Corrección mínima: en el capítulo 18 y en el anexo C, precisar que "ningún indicador retrocede" excluye los indicadores para los que el modelo económico ha previsto valle, o sustituirlo por "ningún indicador retrocede más de lo previsto en el modelo económico".

### A6. Quién responde en una cadena de agentes: uno por cadena o uno por agente

- 06c-detalle-valor-riesgo.md:123 (recuadro, módulo 11): "Propuesta provisional: un responsable por cadena completa, no por pieza, con autoridad para pararla entera."
- 06g-innovacion-agentes.md:101 (módulo 24): "Cuando un agente encarga trabajo a otro, el fallo se propaga. Cada uno conserva su ficha y su dueño".

Problema: dos respuestas opuestas a la misma pregunta, una como propuesta provisional y otra como regla de 1.7.

Corrección mínima: en el módulo 24, añadir si además de un dueño por agente hay un responsable de la cadena, y actualizar el recuadro del módulo 11 para que remita a esa regla.

### A7. "Los seis entregables" del diagnóstico ya no son seis

- 03-tronco.md:23 y tabla de 03-tronco.md:13: "Los seis entregables": mapa del flujo, restricción, línea base, mapa de actores, madurez, mapa de lo que nadie escribió.
- 05-orden.md:11: el arranque a cien días incluye "el inventario de lo que ya se usa (también lo no autorizado), los derechos de decisión escritos".
- 05-orden.md:39: "averiguar en el diagnóstico qué se usa de verdad, con una consulta anónima".
- 06a-detalle-personas-trabajo.md:41: "En el diagnóstico, el inventario de aportaciones se levanta junto al mapa".
- 06c-detalle-valor-riesgo.md:89: "En el diagnóstico se mide la calidad de los datos".
- 06f-tres-miradas-b.md:51: "Un mapa del recorrido, junto al mapa de lo que nadie escribió. En el diagnóstico".
- 06e-tres-miradas-a.md:58 y 114: lectura de supuestos y representación legal en el diagnóstico.

Problema: quien lea el capítulo 9 entrega seis cosas; quien lea el capítulo 18 y los módulos entrega al menos once. La tabla de fases del capítulo 8 y la puerta del diagnóstico (03-tronco.md:71, "tres cosas") no recogen ninguna de las añadidas. Lo mismo ocurre en las filas de piloto, escala y sostenimiento de esa tabla, que no incluyen criterio de parada, registro de supuestos, casos de prueba, responsable de adopción ni normas de equipo (03-tronco.md:115-137).

Corrección mínima: en el capítulo 9, separar "seis entregables básicos" de "lo que añaden los módulos y el capítulo 18" con una lista de remisiones, y actualizar la tabla del capítulo 8.

### A8. La plantilla de decisión de puerta (anexo C) no recoge lo que los capítulos dicen que va en ella

- 08-anexos.md:50-66: la plantilla tiene Opción, Objetivo, las cinco preguntas, Criterios del piloto, Criterio de parada, Supuestos, Alcance, Cómo se deshace y Firma.
- 04-elementos.md:138: "en la puerta de diseño se fija por escrito el nivel máximo al que puede subir cada sistema y por qué". No hay campo.
- 06c-detalle-valor-riesgo.md:15: "Tres preguntas, una línea cada una, en la decisión de puerta" (autonomía, competencia, vínculo). No hay campo.
- 06e-tres-miradas-a.md:60: "La decisión de puerta incluye una línea por punta". No hay campo.
- 06f-tres-miradas-b.md:81: "que quede escrita en la decisión de puerta" (huella material). No hay campo.
- 06a-detalle-personas-trabajo.md:43: "cada opción dice qué aportaciones conserva, cuáles amplía y cuáles elimina". No hay campo.
- 06f-tres-miradas-b.md:9 y 90: roles que se reducen y separación escrita entre asistir y vigilar. No hay campo.

Problema: quien use la plantilla omite al menos seis cosas que el texto exige por escrito en la puerta. Además 03-tronco.md:89 la describe como "un documento de una página", que con esos añadidos no cabe.

Corrección mínima: añadir a la plantilla los campos que faltan (techo de autonomía, tres necesidades, cinco puntas, aportaciones, roles que se reducen, asistir o vigilar, huella) o decir en cada módulo que eso va en un anexo a la decisión y no en la plantilla.

### A9. La IA que ya se usa sin permiso: pregunta abierta y regla cerrada a la vez

- 04-elementos.md:174 (recuadro, cap. 17): "El método, tal como está, asume que la IA entra por las puertas. [...] Propuesta provisional: en el diagnóstico, preguntar sin castigo [...] Lo que no tengo resuelto es cómo hacerlo sin que la pregunta se convierta en una auditoría".
- 07-mejora.md:58: "¿Cómo se integra la IA que ya se usa sin permiso? Propuesta: preguntarlo en el diagnóstico sin castigo".
- 05-orden.md:39 (cap. 18, 1.7): "El método pide cuatro cosas: averiguar en el diagnóstico qué se usa de verdad, con una consulta anónima; ofrecer herramientas aprobadas [...]; un canal [...]; y la garantía de que contar un uso para que se evalúe no trae sanción".
- 06g-innovacion-agentes.md:29: "El método pide un cauce con dos garantías escritas".

Problema: un capítulo dice que el método no lo trata y que la propuesta es provisional; el siguiente lo da como exigencia con cuatro piezas. El lector no sabe si es obligatorio.

Corrección mínima: reescribir el recuadro del capítulo 17 y la entrada del capítulo 21 para que digan qué queda abierto después de 1.7, o retirarlos.

### A10. La dependencia silenciosa: tiene dos piezas y no tiene ninguna

- 06b-detalle-equipo-conocimiento.md:119 (módulo 6): "El método la trata con dos piezas: en el mapa se añade, para cada fila que pasa al sistema, quién mantiene la capacidad de hacerlo sin él; y en la supervisión trimestral se revisa qué capacidades se han perdido."
- 08-anexos.md:328 (anexo F, 1.1): "la dependencia silenciosa como pieza nueva".
- 07-mejora.md:72 (cap. 21, sin solución): "Es la dependencia silenciosa, y no tengo todavía una pieza para ella."

Problema: contradicción directa entre el módulo y el registro de versiones, por un lado, y el capítulo de preguntas abiertas, por otro.

Corrección mínima: en el capítulo 21, cambiar la frase por lo que de verdad sigue abierto (por ejemplo, que las dos piezas no están probadas) o mover la pregunta a "con propuesta provisional".

### A11. El programa acotado dura "menos de seis meses", pero sus fases suman más

- 05-orden.md:96: "Un programa acotado (un equipo, menos de seis meses)".
- 06e-tres-miradas-a.md:74-82 (módulo 17): "órdenes de magnitud orientativos para un programa acotado": diagnóstico de tres a seis semanas, diseño de cuatro a ocho, piloto de ocho a dieciséis, escala "De tres a nueve meses", sostenimiento "Dos ciclos de medición, al menos".

Problema: el mínimo de la tabla es de unos seis meses y medio sin contar el sostenimiento, y el máximo pasa de quince. Las dos definiciones de programa acotado no son compatibles.

Corrección mínima: cambiar el paréntesis del capítulo 18 (por ejemplo, "un equipo, menos de un año") o decir en el módulo 17 que la tabla llega más allá del programa acotado del capítulo 18.

### A12. Cuántos indicadores hay que llevar como mínimo

- 05-orden.md:65: "Tres indicadores como mínimo: uno por elemento."
- 05-orden.md:67: "el indicador de tecnología no puede ser solo el uso [...] El uso se empareja con un indicador de capacidad".
- 05-orden.md:69: "la medición de la tecnología se lee en tres niveles, y ninguno sustituye al siguiente".
- 06b-detalle-equipo-conocimiento.md:123: "Dos indicadores para el elemento conocimiento".
- 06e-tres-miradas-a.md:118: "Al indicador de personas se añade, en los pilotos con IA, una medida sencilla de carga y de intrusión".
- 06f-tres-miradas-b.md:59: "El indicador de tecnología (uso real) se completa con uno de quien recibe el servicio".
- 05-orden.md:61: "Pocos indicadores de resultado". 07-mejora.md:36: "Cinco fases, cinco preguntas, tres indicadores, un mapa."

Problema: la regla visible sigue siendo "tres", pero sumando lo que exigen las versiones 1.1 a 1.7 el mínimo real es de ocho o más (tres de tecnología, dos de conocimiento, personas más carga, receptor del servicio). Tampoco está dicho cuáles entran en el delta ponderado del ciclo.

Corrección mínima: reescribir la cuarta regla de medición como "al menos uno por elemento; en tecnología, uso, capacidad y resultado", listar en una tabla los indicadores obligatorios y los opcionales, y actualizar la crítica del capítulo 20.

---

## Gravedad media

### M1. Veinticuatro módulos, pero las dos tablas de encaje solo cubren veintidós

- 06a-detalle-personas-trabajo.md:3: "Son veinticuatro módulos".
- 06d-detalle-comunicacion-cartera.md:73-75: "Cómo encajan los catorce primeros módulos [...] Los ocho siguientes, nacidos de las tres miradas, se integran en las puertas con la tabla del final de esta parte."
- 06f-tres-miradas-b.md:83: la tabla "Lo que cambia en el método con las tres miradas" ya no está al final de la parte; después viene 06g-innovacion-agentes.md:1 con los módulos 23 y 24.

Problema: catorce más ocho son veintidós. Los módulos 23 y 24 no aparecen en ninguna tabla de encaje, y la referencia "tabla del final de esta parte" apunta a un sitio que ya no es el final.

Corrección mínima: cambiar "la tabla del final de esta parte" por el título de la tabla, y añadir una frase o dos filas que digan en qué fases pesan los módulos 23 y 24.

### M2. "Todos siguen la misma estructura" no se cumple

- 06a-detalle-personas-trabajo.md:3: "Todos siguen la misma estructura: qué es y por qué importa, lo que dicen las fuentes, cómo se hace, cómo se mide, las señales de que va mal y lo que todavía no está resuelto."
- Títulos reales: solo los módulos 6, 7 y 23 tienen "Cómo se mide" (06b:121, 06b:157, 06g:39). No tienen "Señales de que va mal" los módulos 3, 7, 11, 13, 16, 17, 19, 20, 21 y 22. No tienen recuadro de pregunta abierta los módulos 10, 12, 14 y 18. Los módulos 19, 20 y 22 no citan ninguna fuente.

Problema: promesa incumplida en la mayoría de los módulos; ninguno salvo el 6 y el 23 tiene las seis partes.

Corrección mínima: cambiar la frase por "La mayoría sigue un esquema parecido" o completar los apartados que faltan.

### M3. El mapa tiene "cuatro columnas", pero otros sitios le piden más

- 03-tronco.md:57: "Es una tabla de cuatro columnas: qué se sabe, quién lo sabe, dónde se usa y cuán concentrado está." Igual en 08-anexos.md:37.
- 06b-detalle-equipo-conocimiento.md:119: "en el mapa se añade, para cada fila que pasa al sistema, quién mantiene la capacidad de hacerlo sin él".
- 06b-detalle-equipo-conocimiento.md:123: "cuántas filas críticas del mapa siguen en una sola persona". Frente a 05-orden.md:65: "cuántas filas del mapa siguen en una sola persona". El mapa no tiene columna de criticidad y 03-tronco.md:65 deja abierto quién la fija.
- 03-tronco.md:63: el mapa "muestra el conocimiento, no a quien lo tiene". Frente a 03-tronco.md:42: el comité tiene que poder responder "En quién está".

Problema: la plantilla del anexo B no tiene la columna de quién mantiene la capacidad ni la de criticidad, el indicador de concentración se define de dos maneras y la regla de no mostrar a la persona choca con la segunda pregunta que el comité debe responder.

Corrección mínima: añadir al anexo B las dos columnas opcionales, unificar la definición del indicador y aclarar que "en quién está" se responde por perfil salvo consentimiento.

### M4. La tabla de 1.7 asigna todo al "comité de puertas", que no existe en todos los programas ni está definido

- 05-orden.md:25-28: aprobar un caso de uso, subir o bajar de nivel y retirar son del "Comité de puertas".
- 05-orden.md:96: en el programa acotado "las puertas las preside el patrocinador con el responsable"; el comité solo aparece en el programa amplio (05-orden.md:98).
- 08-anexos.md:17 (glosario): el patrocinador "preside sus puertas". 04-elementos.md:15: "presidir las puertas o delegarlas".
- Con voz en las puertas, según el sitio: quien hace el trabajo (06b:29), un mando intermedio "en cada puerta del diseño y del piloto" (06e:34), la segunda línea en diseño y piloto (05-orden.md:35), una persona que defiende a quien recibe el servicio (06f:91).

Problema: en ningún sitio se dice quién compone el comité; cada módulo añade un asiento. El glosario no tiene la entrada.

Corrección mínima: un párrafo en el capítulo 18 con la composición del comité y su equivalente en el programa acotado, y una entrada en el glosario.

### M5. La persona que defiende a quien recibe el servicio: provisional en el módulo, añadida en la tabla

- 06f-tres-miradas-b.md:65 (recuadro): "Propuesta provisional: que en cada puerta haya una persona con la función explícita de defender la mirada de quien recibe el servicio".
- 06f-tres-miradas-b.md:91 (tabla de lo que se añade a las puertas): "una persona que defiende su mirada en cada puerta".

Problema: la misma pieza es propuesta sin contrastar y parte del método veinte líneas después.

Corrección mínima: marcarla como provisional en la tabla o sacarla del recuadro.

### M6. Acelerador y elemento Tecnología se solapan, y no hay lista de aceleradores

- 01-por-que.md:25: "tres elementos que tienen que crecer a la vez, un cuarto componente que los ordena y un conjunto de aceleradores, entre los que hoy la inteligencia artificial pesa más".
- 02-arquitectura.md:23: el elemento Tecnología agrupa "La IA en sus dos papeles [...] las demás tecnologías (plataforma, automatización, entrega continua)".
- 08-anexos.md:7 (glosario): "Acelerador | [...] (la IA, una plataforma, la automatización). Solo entra si los elementos están preparados".
- 04-elementos.md:81: "La tecnología es la palanca del método. Hoy, sobre todo, la inteligencia artificial, que es el único acelerador que actúa en las cinco fases".

Problema: las mismas cosas (IA, plataforma, automatización) son a la vez contenido de un elemento y aceleradores. La regla "elemento antes que acelerador" exige que Tecnología esté en nivel 2 antes de que entre lo que la compone. El "conjunto de aceleradores" que anuncia el capítulo 1 no se enumera en ningún sitio, aunque el diseño debe entregar "Los aceleradores por fase" (03-tronco.md:83). "Palanca" es un tercer nombre.

Corrección mínima: una frase en el capítulo 5 que diga qué diferencia hay entre la tecnología como elemento (la capacidad de la organización para usarla) y un acelerador (una tecnología concreta que se activa), y una lista corta de aceleradores.

### M7. "Ciclo" significa dos cosas

- 03-tronco.md:5: "Un programa grande tiene varios ciclos en paralelo, cada uno en su fase" (ciclo como recorrido de las cinco fases).
- 03-tronco.md:17 y 153: "los indicadores aguantan dos ciclos sin el equipo". 06e-tres-miradas-a.md:82: "Dos ciclos de medición, al menos".
- 04-elementos.md:158: "al cierre de cada ciclo se vuelve a decidir". 05-orden.md:9: la dirección "recibe cada ciclo" el cuadro. 05-orden.md:49: "hay que repetirla cada ciclo".

Problema: si el ciclo es el recorrido de las cinco fases, la puerta del sostenimiento no puede exigir dos ciclos dentro de su propia fase. Si es un periodo de medición, no puede estar "en su fase". Afecta a cuándo se cierra el sostenimiento y a cada cuánto se revisan soluciones, costes y radar.

Corrección mínima: reservar "ciclo" para el recorrido de fases y usar "periodo de medición" (con su duración) en la puerta del sostenimiento y en las revisiones periódicas, o al revés.

### M8. Los verbos de la segunda pregunta: el glosario y el capítulo 9 siguen en dos

- 03-tronco.md:96: "Desde la versión 1.4 son tres." 01-por-que.md:61: "Synergós la amplía a tres: acelerar, automatizar o aumentar."
- 08-anexos.md:8 (glosario): solo existe la entrada "Automatizar o informar | La elección de diseño, formulada por Zuboff, entre quitar criterio a quien hace el trabajo o dárselo". No hay entradas para acelerar, automatizar ni aumentar.
- 03-tronco.md:45: "Conecta directamente con la pregunta de Zuboff: la misma tecnología puede automatizar o informar".
- Definición distinta de automatizar: glosario "quitar criterio"; 03-tronco.md:96 "sacar a la persona del circuito".
- El tercer verbo cambia de nombre: "informar" (Zuboff), "aumentar" (pregunta), "ampliar" y "la ampliación" (01-por-que.md:61, 04-elementos.md:107), "complementar" (04-elementos.md:109).

Problema: el glosario define la versión anterior de la pregunta y con otra definición de automatizar; el concepto central tiene cuatro nombres.

Corrección mínima: sustituir la entrada del glosario por "Acelerar, automatizar o aumentar" con las tres definiciones del capítulo 11, y mencionar una vez que "informar" y "ampliar" se usan como sinónimos de aumentar.

### M9. El inventario tiene cuatro descripciones con campos distintos

- 04-elementos.md:142: "un inventario de sistemas y de riesgos".
- 04-elementos.md:152: "añadir esa columna al inventario de sistemas y de casos de uso. Para cada uno se anotan seis cosas".
- 06c-detalle-valor-riesgo.md:121: "Registro. Inventario de sistemas de IA, con su nivel de riesgo, su responsable, sus datos, su nivel de autonomía y sus incidentes."
- 05-orden.md:33: "Un inventario único. [...] con dueño, nivel de autonomía, proveedor, datos y la columna de personas y conocimiento del capítulo 17."
- 06g-innovacion-agentes.md:68-80: ficha de once campos; el de personas y conocimiento recoge dos de las seis cosas ("Qué criterio gana o pierde [...] y quién enseña"), y 06g:82 dice "es la columna de Synergós llevada al agente".

Problema: el inventario "único" no tiene una lista única de campos: nivel de riesgo e incidentes solo están en el módulo 11, proveedor solo en el capítulo 18, y la columna de seis cosas se queda en dos en la ficha (faltan quién puede pararlo, vigilancia, incentivo y la fila del mapa). Además "registro" nombra el inventario, el registro de riesgos y decisiones (05-orden.md:17), el registro de decisiones del conocimiento (04-elementos.md:59) y el registro de acciones del agente (06g:77).

Corrección mínima: una sola tabla de campos del inventario en el capítulo 18, a la que remitan el capítulo 17, el módulo 11 y la ficha del módulo 24.

### M10. La regla "ninguna pieza entra sin causa y sin fuente fichada" no se cumple en las capas nuevas

- 01-por-que.md:49: "Quien proponga añadir una pieza al método tiene que decir a qué causa responde."
- 07-mejora.md:23: "Una pieza nueva entra solo si responde a una causa documentada y tiene una fuente fichada."
- 08-anexos.md:158, 229, 259 y 289: las fuentes de 1.1, 1.2, 1.5 y 1.7 están "pendientes de ficha propia".
- 04-elementos.md:109: la distinción de acelerar "no tiene una fuente que la respalde".
- 08-anexos.md:257: las cinco propuestas de 1.6 salen de publicaciones que "Ninguna se cita".
- La tabla de causas (01-por-que.md:33-47) tiene trece filas y no se ha ampliado: no hay causa para la exploración (módulo 23), los agentes (módulo 24), la huella material (módulo 22) ni la inclusión (módulo 20).

Problema: el control que el documento presenta como su defensa contra "engordar por acumulación" no se ha aplicado a las piezas añadidas desde 1.1.

Corrección mínima: añadir a la tabla de causas las filas que justifican los módulos nuevos, o rebajar la regla 1 a lo que de verdad se hace ("fuente identificada; ficha pendiente se marca").

### M11. El capítulo 21 dice que reúne las preguntas de los recuadros y recoge una cuarta parte

- 07-mejora.md:50: "Algunas preguntas ya aparecen en los recuadros de cada capítulo. Aquí están reunidas, junto con otras".
- En el texto hay 29 recuadros de pregunta abierta. El capítulo 21 lista 16 preguntas, de las que 8 no tienen recuadro; de los 29 recuadros solo aparecen 7 u 8. Faltan, entre otras, "¿Cinco preguntas son demasiadas?" (03-tronco.md:103), "¿El delta ponderado esconde más de lo que muestra?" (05-orden.md:75) y todas las de los módulos 1 a 24.

Problema: quien use el capítulo 21 como lista de lo no resuelto se deja fuera unas veinte preguntas.

Corrección mínima: completar la lista o cambiar la frase por "Aquí están las principales".

### M12. Propuestas que el capítulo 21 o un recuadro dan por provisionales y un módulo da como regla

- Retirar por la misma puerta: 07-mejora.md:60 "Propuesta: que la retirada de lo existente pase por la misma puerta" frente a 06d-detalle-comunicacion-cartera.md:65 (en "Lo que pide el método"): "Una iniciativa que sale pasa por las cinco preguntas".
- Una persona por agente: 06b-detalle-equipo-conocimiento.md:87 "Intuyo que la regla más importante es que siempre haya una persona que responda de lo que hace cada agente, con nombre, pero es una intuición" frente a 06c:115 "Para cada sistema de IA en el servicio, una persona responde de lo que hace" y 06g:70.
- Coste de la supervisión: 06a-detalle-personas-trabajo.md:144 "No tengo una forma estándar de medirlo [...] Propuesta: registrar durante el piloto" frente a 05-orden.md:49 (el coste por tarea incluye "la revisión humana que exige") y 06g:97 ("dos medidas de la propia supervisión").

Problema: el estado de cada pieza (obligatoria o provisional) depende de la página.

Corrección mínima: en cada recuadro, una línea que diga qué parte se ha convertido ya en regla y dónde.

### M13. La comunidad de práctica: antes del primer piloto o en la escala

- 04-elementos.md:142: "Antes del primer piloto con IA dentro del servicio [...] las piezas del entorno: [...] la formación por perfil; y una comunidad de práctica."
- 03-tronco.md:133 (fase de escala): "Desde la versión 1.6 [...] Se forma una comunidad de práctica con varios referentes por área".

Problema: la misma pieza es requisito previo al piloto y algo que se forma dos fases después.

Corrección mínima: decir en el capítulo 13 que la comunidad que existe desde el entorno se amplía con referentes por área en la escala.

### M14. "Un equipo de transformación Synergós tiene siete funciones", pero las versiones 1.2 a 1.7 añaden papeles que no están

- 06b-detalle-equipo-conocimiento.md:17: "tiene siete funciones".
- 03-tronco.md:135: "una persona responsable de la adopción, con nombre y con tiempo, distinta de quien despliega la herramienta".
- 05-orden.md:37: "Cada función que usa IA tiene una persona que responde de sus casos".
- 06g-innovacion-agentes.md:23: "Un laboratorio pequeño. Dos o tres personas con tiempo reconocido".
- 05-orden.md:98: "una oficina pequeña de medición y conocimiento". 03-tronco.md:133: referentes con horas reconocidas.

Problema: la tabla de funciones y la regla de dedicación (un tercio del tiempo) no dicen nada de estos papeles; no se sabe si son funciones del equipo, del equipo que opera o aparte.

Corrección mínima: una nota bajo la tabla del módulo 4 que sitúe cada papel nuevo.

### M15. Los derechos de decisión se describen de dos maneras y en dos momentos

- 06b-detalle-equipo-conocimiento.md:73: "Para cada tipo de decisión del programa, quién decide, a quién se consulta y a quién se informa. [...] diez o quince decisiones".
- 05-orden.md:21: "se escriben en una tabla de una página [...] Como mínimo responde a siete preguntas", con una sola columna "Quién la toma".
- Momento: 05-orden.md:11 los pone en los primeros cien días, antes de la primera puerta; 06d-detalle-comunicacion-cartera.md:83 los pone en la columna de Diseño.

Corrección mínima: remitir el módulo 5 a la tabla del capítulo 18 y decir si las columnas de consulta e información son parte de ella; unificar el momento.

### M16. El Reglamento de IA: fechas cerradas en dos sitios y difusas en otro

- 04-elementos.md:144: "sus obligaciones se aplican de forma escalonada, con fechas que se han discutido y que pueden haberse ajustado."
- 06c-detalle-valor-riesgo.md:111: "el calendario cambió en 2026 [...] al 2 de diciembre de 2027 para los usos del anexo III". Igual en 06e:106 y 08-anexos.md:133.
- 08-anexos.md:330 (1.3): "calendario del Reglamento de IA tras el Reglamento (UE) 2026/1744".

Problema: el capítulo 17 no se actualizó con la verificación de 1.3 y habla de un ajuste posible que otros tres sitios dan por hecho y fechado.

Corrección mínima: sustituir la frase del capítulo 17 por una remisión al módulo 11.

### M17. McKinsey figura como "revisada y no citada" y se cita en el módulo 24

- 08-anexos.md:285: "Revisadas y no citadas: McKinsey, BCG, Deloitte y Accenture. [...] Se usan como contexto en el cuaderno, no en el método."
- 06g-innovacion-agentes.md:60: "McKinsey publicó en 2025 las lecciones de un año de despliegues de agentes. Las que más pesan aquí [...]". Y 08-anexos.md:305 la lista como fuente de 1.7.
- 04-elementos.md:85: "Las consultoras lo ponen en la reinvención y el crecimiento, aunque sus propias encuestas reconocen [...]" (uso en el método sin cita).

Corrección mínima: acotar la nota a "en la versión 1.5" y añadir que 1.7 cita un texto de McKinsey como experiencia de práctica.

### M18. "Esta versión" apunta a cuatro versiones distintas

- 04-elementos.md:150: "Para esta versión revisé un esquema de gobierno de IA". Según 08-anexos.md:317 fue "Para la versión 1.4".
- 06e-tres-miradas-a.md:3: "dónde se trata a partir de esta versión" (es la 1.2).
- 06b-detalle-equipo-conocimiento.md:119: "el método trataba mal hasta esta versión" (es la 1.1).
- 07-mejora.md:19: "Una parte de las mejoras de esta versión" (por contenido, la 1.0).

Problema: el documento se presenta como versión 1.7 (01-por-que.md:3); el lector atribuye a 1.7 cambios de 1.0, 1.1, 1.2 y 1.4.

Corrección mínima: sustituir cada "esta versión" por el número.

### M19. Cuándo se escribe el destino del tiempo ganado

- 03-tronco.md:96 (puerta de diseño): "Si la respuesta es acelerar, se escribe a dónde va el tiempo que se gana."
- 06c-detalle-valor-riesgo.md:58: "El método exige que la capacidad liberada tenga un destino escrito antes de aprobar la escala". Y 06c:60: "el destino del tiempo se decide antes de la escala".

Problema: la misma decisión se exige en la puerta de diseño y en la de piloto a escala. Un lector del módulo 9 puede llegar al piloto sin haberla escrito.

Corrección mínima: en el módulo 9, "se escribe en el diseño y se confirma antes de aprobar la escala".

### M20. Revisar cada propuesta (nivel 2) frente a "revisar todo no funciona"

- 04-elementos.md:128: nivel 2, la persona "Revisa cada propuesta y decide". Nivel 1: "Decide y hace todo".
- 06g-innovacion-agentes.md:97: "Revisar todo lo que hace un agente no funciona [...] El método pide aprobación previa solo en lo irreversible o de alto impacto, revisión por muestreo en lo demás".

Problema: el módulo 24 formula como regla general lo que en la escala solo vale desde el nivel 3. Leído solo, autoriza muestreo en un agente de nivel 2.

Corrección mínima: añadir en el módulo 24 "en los niveles 3 y 4".

### M21. El indicador de criterio se usa como señal de retirada y a la vez se declara sin medida; la capacidad es de tecnología y de personas

- 06a-detalle-personas-trabajo.md:142: señal de retirada "que el indicador de criterio de las personas baje".
- 05-orden.md:73: "Es el indicador que más falta y el que peor sé medir. [...] no tiene una medida estándar." 07-mejora.md:64: "ningún indicador que me convenza".
- 05-orden.md:67: el indicador de capacidad, pareja del de tecnología, puede ser "la calidad de las correcciones que hace a lo que la herramienta produce". 05-orden.md:73: candidato a indicador de criterio de las personas, "la calidad de las correcciones que hacen a la IA".
- 04-elementos.md:158: los indicadores para decidir si se retira una solución son "el uso, la capacidad [...] y el coste por tarea completada", distintos de las cuatro señales de 06a:142.

Problema: una señal de retirada depende de un indicador que el método dice no tener; la misma medida aparece como indicador de tecnología y como candidato a indicador de personas; y las listas de señales para retirar no coinciden.

Corrección mínima: en el módulo 3, sustituir "indicador de criterio" por "indicador de capacidad" y remitir a la lista del capítulo 17; decir en el capítulo 18 a qué elemento se asigna la capacidad.

### M22. Tres clasificaciones distintas para la misma revisión de fin de ciclo

- 03-tronco.md:9: cada puerta tiene "tres salidas posibles: pasar, ajustar y repetir, o retirar".
- 06d-detalle-comunicacion-cartera.md:59 y 05-orden.md:100: "Mantener, acelerar, reorientar o retirar".
- 04-elementos.md:158: "si se mantiene, se sustituye por otra comprada, se construye algo propio o se retira".
- 04-elementos.md:168 (radar): "movimientos sin arrepentimiento [...] opciones pequeñas [...] apuestas".

Problema: al cierre de un ciclo se aplican cuatro esquemas de clasificación con categorías que se pisan (retirar está en tres), sin decir cómo se combinan. "Acelerar" significa aquí dar prioridad, no el verbo de la segunda pregunta.

Corrección mínima: un párrafo que diga qué clasificación se aplica a qué objeto (iniciativa, solución en uso, tecnología emergente) y cambiar "acelerar" por "priorizar" en la clasificación de cartera.

### M23. "La tercera pregunta del mapa" es dos preguntas distintas

- 04-elementos.md:45: "La tercera pregunta del mapa (qué le pasa a cada fila con cada opción)".
- 06b-detalle-equipo-conocimiento.md:69: "La tercera pregunta del mapa de lo que nadie escribió (a quién llamas cuando algo se atasca, y quién te llama a ti)".

Problema: el mapa tiene tres preguntas para el comité (03-tronco.md:41-43) y cinco preguntas por las grietas (08-anexos.md:27). "Las preguntas del mapa" (04-elementos.md:61, 06b:115) no dice cuáles. Además "las cinco preguntas" nombra también las de la puerta.

Corrección mínima: llamar siempre "preguntas por las grietas" a las de la entrevista y "preguntas del comité" a las otras.

---

## Gravedad baja

### B1. Tabla de fases: "ajustar, repetir o retirar"
03-tronco.md:15: "o la puerta decide ajustar, repetir o retirar" frente a 03-tronco.md:9 y 08-anexos.md:18: "pasar, ajustar y repetir, o retirar". La coma convierte tres salidas en cuatro. Corrección: "ajustar y repetir, o retirar".

### B2. Conocimiento explícito: cuatro piezas en el capítulo 16, tres en el capítulo 5
04-elementos.md:53: "Las piezas del método son cuatro" (incluye la captura del conocimiento de quien se va). 02-arquitectura.md:22: "El explícito (datos con dueño, base curada, registro de decisiones)". Corrección: añadir la cuarta a la tabla.

### B3. Qué agrupa el orden: tres listas, y las fases dentro o fuera
02-arquitectura.md:24: "Las cinco fases y sus puertas; estrategia; gobierno; modelo económico; medición y el delta; madurez y regla de entrada; dimensionamiento del programa; la marcha atrás". 05-orden.md:3: "Agrupa la estrategia, el gobierno, el modelo económico, la medición, la madurez y el dimensionamiento." 08-anexos.md:16: "fases, puertas, estrategia, gobierno, modelo económico, medición, madurez y dimensionamiento". Además 01-por-que.md:25 presenta el tronco de fases como pieza distinta del "cuarto componente que los ordena". Corrección: una sola lista.

### B4. Aceleradores "por fase" o "por ciclo"
02-arquitectura.md:50: "uno o dos aceleradores por fase". 05-orden.md:98: "la IA y hasta dos aceleradores más por ciclo"; 05-orden.md:96: "la IA y un acelerador más". Corrección: unificar la unidad.

### B5. Referentes, campeón, usuarios avanzados
03-tronco.md:133: "un solo campeón por equipo" y "varios referentes por área". 03-tronco.md:131: "los usuarios avanzados del piloto". 04-elementos.md:27: "un grupo estable de usuarios avanzados que prueban antes que nadie". No se dice si son las mismas personas. Tampoco coincide la unidad: "por equipo" y "por área". Corrección: una frase que relacione los tres términos.

### B6. Frontera dentada e irregular; "la frontera" como fenómeno y como clasificación
04-elementos.md:99 y 08-anexos.md:13 y 99: "frontera dentada". 08-anexos.md:277: "la frontera irregular". Además "la frontera" es el hallazgo de Dell'Acqua (04-elementos.md:99) y también la clasificación propia en cuatro categorías (06a:80: "Clasificar cada tarea en la frontera"). Corrección: "dentada" en la entrada de Mollick.

### B7. Daugherty y Wilson aparece dos veces en el anexo E con datos distintos
08-anexos.md:184: "Daugherty, P. y Wilson, J. (2018). Human + Machine. El medio que falta". 08-anexos.md:267: "Daugherty, P. y Wilson, H. J. (2018 y 2022). Human + Machine y Radically Human. [...] Evidencia de consultora, no auditable." Iniciales distintas y valoración distinta de la misma obra. Corrección: fusionar.

### B8. Citas del texto que no están en el anexo E
01-por-que.md:9: "todo lo que cito está en la lista de fuentes del final". No están: Deming (03-tronco.md:5: "el ciclo de mejora de Deming") ni la Ley 9/2017 (06d-detalle-comunicacion-cartera.md:41), que tampoco figura en "Normas citadas" (08-anexos.md:255). 04-elementos.md:71: "como advierte Davenport" no dice cuál de las dos entradas (Davenport y Prusak 1998 o Davenport y Kirby 2016). Corrección: añadir las dos entradas y precisar "Davenport y Kirby (2016)".

### B9. Entradas del anexo E que el texto no cita
Sin cita en el cuerpo: Gillespie y otros 2025 (08-anexos.md:271), Iansiti y Lakhani 2020 (273), Mollick 2024 (277), PwC 2026 (279), World Economic Forum 2025 (283), Ranganathan y Ye 2026 (313; 06c:60 usa su contenido como "Lo que se ha observado en organizaciones" sin nombrarla), Edmondson 1999 (105), y la Directiva (UE) 2024/2831, que está bajo el rótulo "Normas citadas" (255) y no se cita en ningún módulo. Corrección: citarlas donde se usan o moverlas a un apartado "revisadas".

### B10. Anexo E: orden de versiones y entradas sin contenido
Los bloques van 1.1, 1.2, 1.6, 1.5, 1.7 y 1.4 (08-anexos.md:158, 229, 257, 259, 287, 317). 08-anexos.md:79: "Cada fuente aparece con lo que aporta al método"; la entrada de Wenger (222) no tiene ninguna descripción, y las de Kellogg (243), Huy (239) y Wrzesniewski (226) tampoco. 01-por-que.md:9 promete "sobre todo, con lo que no dice", que la mayoría de entradas no trae. Corrección: ordenar y completar o rebajar la promesa.

### B11. Tecnoestrés: cuatro componentes en el texto, cinco en la fuente
06e-tres-miradas-a.md:98: "la sobrecarga, la invasión del tiempo personal, la complejidad y la inseguridad". 08-anexos.md:253: "Tecnosobrecarga, tecnoinvasión, tecnocomplejidad, tecnoinseguridad y tecnoincertidumbre." Corrección: añadir la quinta o decir "entre otras".

### B12. Anexo F, versión 1.7: "doce propuestas" y la lista enumera más de veinte
08-anexos.md:334: "doce propuestas: dos módulos nuevos [...]". La enumeración que sigue tiene más de veinte elementos y no dice cómo se agrupan en doce. En 1.6 sí cuadra ("cinco propuestas", cinco listadas). Corrección: numerar las doce o quitar la cifra.

### B13. Referencias a cosas que no están en el documento
06d-detalle-comunicacion-cartera.md:7: "El estudio de La bola negra que acompaña este documento" (no hay tal estudio en los anexos ni entrada en E). 08-anexos.md:333: "(axioma A23)" (no hay axiomas en el documento). 08-anexos.md:259 y 287: remisiones a "el cuaderno". Corrección: quitar o explicar en una línea.

### B14. "Las tres capas del párrafo anterior"
05-orden.md:35: "Las tres capas del párrafo anterior describen niveles de responsabilidad". Las tres capas están en 05-orden.md:19; entre medias hay la tabla de quién decide qué y el párrafo del inventario único. Corrección: "Las tres capas descritas más arriba".

### B15. Tres hipótesis o cinco diseños para enseñar el oficio
04-elementos.md:37: "Tengo tres hipótesis". 07-mejora.md:57: "Tres hipótesis". 06b-detalle-equipo-conocimiento.md:147: "Cinco diseños posibles". Corrección: remitir desde el recuadro al módulo 7 y decir "cinco".

### B16. "Nivel" nombra cinco escalas
Madurez (05-orden.md:79, niveles 1 a 4), autonomía (04-elementos.md:125, niveles 1 a 4), medición de tecnología (05-orden.md:69, "tres niveles"), árbol de impacto (06c:47, "cuatro niveles"), cultura (06e:48, "tres niveles"). El anexo D mezcla dos: Tecnología en nivel 4 de madurez incluye "se baja de nivel sin drama" (08-anexos.md:75). "Nivel 2" a secas es ambiguo en 05-orden.md:90. Corrección: "nivel de madurez" y "nivel de autonomía" siempre con apellido; el texto ya usa "peldaño" para autonomía en parte.

### B17. El glosario no recoge ningún término de las versiones 1.4 a 1.7 y usa uno que no está en el texto
08-anexos.md:12: "Elemento | Cada uno de los tres ejes" ("ejes" no aparece en ningún otro sitio; el texto usa "componente", 02-arquitectura.md:17). Faltan comité de puertas, inventario, ficha, referente, alcance, capa y línea, carril de exploración, coste por tarea completada. Corrección: añadir las entradas.

### B18. "En cada capítulo" hay preguntas abiertas
01-por-que.md:7: "lo digo en cada capítulo". 01-por-que.md:75: "preguntas abiertas que reconozco en cada capítulo". No tienen recuadro los capítulos 1 a 8, 10, 13, 14, 19, 20 y 22. Corrección: "en muchos capítulos".

### B19. La revisión trimestral de supuestos: para todos o solo para el programa amplio
04-elementos.md:77: "Synergós pide cuatro prácticas. [...] Y una revisión trimestral de supuestos". 05-orden.md:98: aparece solo en la lista del programa amplio. Además 06b:119 la llama "supervisión trimestral". Corrección: decir qué hace el programa acotado.

### B20. "Supervisión" nombra el aprendizaje del programa y la vigilancia humana de la IA
04-elementos.md:73: "El aprendizaje del propio programa: la supervisión"; 03-tronco.md:149: "calendario de supervisión". 06g-innovacion-agentes.md:97: "Supervisión que supervise" (revisión humana del agente); 06a:144: "coste de la supervisión"; 05-orden.md:51: "la supervisión humana". Corrección: "supervisión del programa" y "revisión humana".

### B21. El estudio del centro de atención se usa como ejemplo de aumentar con la definición de acelerar
04-elementos.md:107: "Acelerar es hacer la misma tarea más rápido, con la misma persona." 04-elementos.md:111: "Aumentar: con un asistente de IA, los agentes de atención al cliente resolvieron de media un 15 % más de casos por hora". Por la definición del propio texto, más casos por hora es acelerar. Corrección: una frase que diga por qué se clasifica como aumentar (la mejora de los menos expertos) o moverlo.

### B22. Regla 4 del capítulo 19 frente al anexo F
07-mejora.md:26: "Toda versión dice qué se ha cambiado y qué se ha aprendido." 08-anexos.md:323: la tabla solo tiene la columna "Qué cambia". Además 07-mejora.md:11 dice que el registro "dice qué cambió y por qué"; el porqué solo aparece en algunas filas. Corrección: añadir la columna o rebajar la regla.

Otros desajustes menores observados, sin número propio:
- 05-orden.md:27 ("Parar un sistema en uso | Su dueño y cualquier persona de la capa de uso, sin autorización previa") frente a 06g:76 y 04-elementos.md:152, que piden anotar por sistema "quién puede pararlo".
- 06e:80 (piloto "De ocho a dieciséis semanas") frente a 03-tronco.md:115 ("fecha de revisión a noventa días como máximo"): no se dice que la revisión no es el final del piloto.
- 07-mejora.md:46 ("las señales de fallo de cada pieza"): no todas las piezas tienen señal de fallo.
- 04-elementos.md:152: "Es el contenido de las cinco preguntas de la puerta, llevado al inventario"; tres de las seis cosas (quién puede pararlo, vigilancia, incentivo) no están en las cinco preguntas.

---

## Comprobaciones que salieron bien

- Todas las referencias "capítulo N" y "módulo N" del texto apuntan al sitio correcto (capítulos 2, 5, 7, 9, 13, 15, 17, 18; módulos 1, 2, 3, 4, 5, 7, 13, 14, 17, 19, 23, 24).
- Los recuentos internos cuadran en: seis principios, cinco preguntas de la puerta, cuatro categorías de la frontera, cuatro niveles de autonomía y de madurez, siete aportaciones, siete criterios de la matriz, siete funciones del equipo, siete filas de quién decide qué, cinco momentos del conocimiento, once campos de la ficha, catorce y ocho módulos, treinta y cuatro fuentes de 1.1 y trece de 1.7, tres campos nuevos de la plantilla en 1.7.
- Las etiquetas "desde la versión X" del cuerpo coinciden con el anexo F en todos los casos comprobados (1.4, 1.5, 1.6 y 1.7).
- Años y cifras de las fuentes repetidas coinciden entre texto y anexo E (Klarna, Commonwealth Bank, Brynjolfsson, Li y Raymond, el estudio de los canarios, Noy y Zhang, Dell'Acqua, Goodhart y Strathern, Kotter, Zuboff).
