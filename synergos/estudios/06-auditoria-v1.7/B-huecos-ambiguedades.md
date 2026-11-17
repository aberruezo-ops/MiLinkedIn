# Auditoría B de "Synergós. El método", versión 1.7

Punto de vista: una directora de transformación que tiene que aplicarlo el lunes y un revisor metodológico.

Alcance: los catorce ficheros `0*.md` de `/home/user/MiLinkedIn/synergos/documentos/metodo/`, leídos enteros y en orden (37.325 palabras). No se ha editado ningún fichero. No se ha mirado el .docx ni el cuaderno de estudios.

Reglas seguidas: cada hallazgo lleva cita literal o la constatación de que algo no aparece, con lo que se buscó. Las 29 preguntas abiertas en recuadro no cuentan como hallazgo, salvo cuando tapan un hueco mayor (se indica). No se comenta el estilo.

Total: 67 hallazgos. Huecos 19, ambigüedades 14, problemas de lógica o de método 19, afirmaciones más fuertes que su respaldo 15. Por gravedad: 23 altas, 38 medias, 6 bajas. Al final, los cinco puntos por donde un crítico lo desmontaría.

Cómo leer cada hallazgo: Dónde, Cita, Problema, Gravedad, Corrección mínima.

---

## Bloque 1. Huecos

### H1. No hay núcleo mínimo: no se sabe qué es obligatorio y qué se puede quitar

- Dónde: `06g-innovacion-agentes.md`, Módulo 23, "Lo que pide el método"; `02-arquitectura.md`, "Principio 6"; `01-por-que.md`, cap. 4.
- Cita: "una mejora puntual no necesita los veinticuatro módulos". "Si una pieza del método no aporta en un programa, se retira de ese programa". "Si un programa usa Synergós y las personas aparecen por primera vez en la formación de cierre, no está usando Synergós".
- Problema: se dice que no todo hace falta, pero en ningún fichero se dice cuáles módulos, entregables o preguntas son irrenunciables y cuáles dependen del alcance (puntual, de flujo, de sistema) o del tamaño (acotado, amplio). Tampoco quién decide retirar una pieza. Quien aplica tiene que decidirlo sola y no puede saber si "está usando Synergós".
- Gravedad: alta.
- Corrección: añadir al final de la Parte V una tabla de una página, "Qué es obligatorio según alcance y tamaño", con filas = entregables y módulos, columnas = puntual, de flujo, de sistema, y tres valores: obligatorio, recomendado, no aplica. Añadir una frase: "Retirar una pieza de un programa lo decide el patrocinador y se anota en el registro de decisiones".

### H2. El comité de puertas no está definido

- Dónde: `05-orden.md`, cap. 18, "Gobierno" y "Dimensionamiento"; `03-tronco.md`, cap. 9.
- Cita: "Un comité de puertas con criterios previos, derechos de decisión escritos y un registro de riesgos y de decisiones". "El comité que aprueba el diseño tiene que poder responder por escrito a tres preguntas".
- Problema: el comité toma casi todas las decisiones (aprobar casos, subir autonomía, retirar, construir o comprar), pero no se dice quién lo forma, cuántos son, quién tiene voto y quién solo voz, cómo decide (consenso, mayoría, decide el patrocinador), cada cuánto se reúne ni quién lo convoca. La composición hay que reconstruirla de ocho sitios: patrocinador que preside (cap. 15), mando intermedio "con voz" (módulo 15), personas que hacen el trabajo que "tienen voz en las puertas" (módulo 4), segunda línea que "participa en el diseño y en el piloto" (cap. 18), una persona que defiende a quien recibe el servicio (módulo 21, provisional), la persona de cada función (cap. 18), el responsable de medición que firma (anexo C) y alguien "sin interés" para las retiradas. Busqué "quórum", "vota", "RACI": no aparecen.
- Gravedad: alta.
- Corrección: añadir en "Gobierno" una tabla "Composición del comité de puertas": miembro, voz o voto, en qué puertas es obligatorio. Y una frase de regla de decisión, por ejemplo: "Decide el patrocinador oído el comité; la objeción de la segunda línea y la del responsable de medición quedan escritas".

### H3. El caso más frecuente no tiene camino: dar un asistente general a toda la plantilla

- Dónde: `05-orden.md`, cap. 18, "El uso informal"; `04-elementos.md`, cap. 17, "El radar".
- Cita: "ofrecer herramientas aprobadas que sirvan para lo que la gente hace con las otras". "Nada entra por fuera de las puertas, por muy prometedor que parezca".
- Problema: el método pide ofrecer herramientas aprobadas, pero su único camino de aprobación es el tronco (restricción, línea base, mapa, piloto con delta). Un asistente de uso general para miles de personas no ataca una restricción concreta ni tiene un flujo ni un mapa. No se dice por qué puerta entra, con qué criterios ni quién lo decide. Es probablemente lo primero que le pedirán a una directora de transformación. Busqué "asistente general", "propósito general", "licencia": solo aparece "licencias" como coste.
- Gravedad: alta.
- Corrección: añadir en "El uso informal" un párrafo "Herramientas de uso general": se aprueban por una vía corta con cuatro condiciones escritas (reglas de uso, datos permitidos, formación mínima, indicadores de uso y capacidad), y cada uso que entre en un servicio pasa después por el tronco.

### H4. No se dice cómo se fija ningún umbral

- Dónde: `05-orden.md`, "Medición y el delta"; `04-elementos.md`, "La escala de autonomía"; `03-tronco.md`, cap. 13.
- Cita: "el piloto pasa si el delta del ciclo supera el cuarenta por ciento y ningún indicador retrocede". "La tasa de corrección es baja y estable en casos reales". "Los errores detectados son pocos, conocidos y reversibles". "Los indicadores aguantan al ampliar".
- Problema: todas las puertas dependen de un umbral y el documento no da ni un número de partida ni un procedimiento para elegirlo (por referencia a qué, quién lo propone, quién lo aprueba). El cuarenta por ciento del ejemplo no se justifica. Dos equipos aplicando el método pondrán umbrales incomparables. La palabra "umbral" solo aparece dos veces, las dos en la pregunta abierta de las filas críticas.
- Gravedad: alta.
- Corrección: añadir en "Medición y el delta" una regla de tres líneas: quién propone el umbral (medición), con qué referencia (variación normal del indicador en la línea base y el mínimo que haría rentable la escala según el modelo económico) y quién lo firma. Y una nota en la tabla de autonomía: "cada organización escribe el número; como partida, X".

### H5. El diagnóstico no se puede ejecutar paso a paso: cinco de seis entregables no tienen procedimiento ni plantilla

- Dónde: `03-tronco.md`, cap. 9, "Los seis entregables"; `08-anexos.md`, anexos B, C y D.
- Cita: "**La restricción principal.** El punto que limita el resultado del conjunto. Tiene que ser una, nombrada, y aceptada por el patrocinador". "Si el equipo no consigue ponerse de acuerdo en cuál es la restricción, el programa todavía no sabe qué está transformando".
- Problema: el mapa de lo que nadie escribió tiene preguntas, tabla y plantilla. Los otros cinco entregables tienen un párrafo cada uno. No se dice cómo se encuentra la restricción (ningún procedimiento), qué indicadores forman la línea base ni durante cuánto tiempo se miden, cómo se observa "en el puesto" (cuántos puestos, cuántas horas), qué columnas tiene el mapa de actores ni con qué instrumento se evalúa la madurez. Tampoco el orden entre ellos ni quién hace cada uno. Y falta el paso cero: cómo se elige el ámbito que se diagnostica (la palabra "ámbito" aparece dos veces, sin criterio de elección).
- Gravedad: alta.
- Corrección: añadir al cap. 9 una tabla "El diagnóstico semana a semana" con seis filas (una por entregable): actividad, quién de las siete funciones la hace, con quién, duración y evidencia de terminado. Añadir tres líneas sobre cómo se nombra la restricción (por ejemplo: dónde se acumula la cola, qué pasa si se duplica la capacidad en ese punto) y una frase sobre quién elige el ámbito y con qué criterio.

### H6. La adaptación a la administración pública se queda en la contratación

- Dónde: `06d-detalle-comunicacion-cartera.md`, Módulo 13, "El caso del sector público"; `06e-tres-miradas-a.md`, Módulo 18, "El marco legal en España".
- Cita: "La propuesta del método es modesta: que el diagnóstico (fase 1) se haga con medios propios o con un contrato separado antes del pliego de la solución".
- Problema: el público objetivo incluye la administración y el método exige cosas que allí funcionan de otra manera y no se tratan: "roles, carreras e incentivos rediseñados" con retribuciones y puestos fijados por norma; representación del personal funcionario (el módulo 18 solo cita el Estatuto de los Trabajadores); la actuación administrativa automatizada y la motivación de los actos; el Esquema Nacional de Seguridad; el presupuesto anual frente a "presupuesto recurrente". Busqué "EBEP", "Estatuto Básico", "junta de personal", "Ley 40/2015", "Ley 39/2015", "actuación administrativa", "Esquema Nacional", "relación de puestos": cero apariciones. "Funcionari" aparece una vez, en la cita de Lipsky.
- Gravedad: alta para ese público.
- Corrección: añadir al módulo 13 una tabla "Qué cambia en una administración" de cinco filas (incentivos y carrera, representación del personal, decisiones automatizadas sobre ciudadanos, seguridad, presupuesto), cada una con "qué pide el método", "qué limita la norma" y "qué se hace en su lugar", y la frase "a comprobar con asesoría jurídica".

### H7. El piloto no tiene ninguna regla que haga creíble su resultado

- Dónde: `03-tronco.md`, cap. 12; `05-orden.md`, "Medición y el delta".
- Cita: "Resultados contra la línea base, lecciones aprendidas, ajustes al diseño y riesgos descubiertos".
- Problema: el piloto compara antes y después en un solo entorno durante ocho a dieciséis semanas. No se pide grupo de comparación, ni tamaño mínimo, ni se tiene en cuenta la variación normal del indicador, la estacionalidad o el efecto de sentirse observado. Con eso, un delta del cuarenta por ciento puede ser ruido, y la regla "ningún indicador retrocede" puede fallar por azar. Busqué "grupo de control", "tamaño de la muestra", "tolerancia", "estadístic": cero apariciones.
- Gravedad: alta.
- Corrección: añadir al cap. 12 un párrafo "Con qué se compara": siempre que se pueda, un equipo o periodo de comparación sin el cambio; la línea base incluye la variación normal del indicador (mínimo y máximo de los últimos meses) y un cambio menor que esa variación no cuenta ni como mejora ni como retroceso.

### H8. Las cinco fases no tienen el mismo nivel de detalle: escala y sostenimiento no dicen quién escribe sus criterios ni quién decide

- Dónde: `03-tronco.md`, caps. 13 y 14, y tabla del cap. 8; `02-arquitectura.md`, "Principio 4".
- Cita: "Los criterios de cada puerta se escriben al empezar la fase". "**La puerta de escala.** Los indicadores aguantan al ampliar, y los tres elementos aguantan la carga". "Cada etapa tiene su propia mini puerta".
- Problema: comparación entre fases. Diagnóstico: seis entregables y puerta con tres condiciones cerradas. Diseño: seis productos, plantilla y cinco preguntas. Piloto: criterios firmados, parada, revisión a noventa días. Escala: actividades descritas, pero la puerta es una frase sin medida, no se dice quién escribe sus criterios ni cuándo, ni quién decide las "mini puertas" de cada etapa. Sostenimiento: cuatro párrafos; no se dice quién convoca la puerta cuando el equipo ya no está, qué significa aquí "ajustar y repetir" o "retirar", ni qué pasa después de pasarla (¿el programa se cierra?). Ninguna fase tiene responsables por entregable.
- Gravedad: alta.
- Corrección: añadir a la tabla del cap. 8 dos columnas: "Quién escribe los criterios y cuándo" y "Quién decide". En el cap. 14, una frase: "La puerta de sostenimiento la convoca el dueño operativo ante el patrocinador; pasarla cierra el programa para ese ámbito".

### H9. Seguridad de la información y protección de datos no tienen pieza propia

- Dónde: `04-elementos.md`, cap. 17, "El entorno que exige la IA"; `05-orden.md`, "El uso informal".
- Cita: "el uso seguro y el acceso controlado; el gobierno del dato; la formación por perfil". "la garantía de que contar un uso para que se evalúe no trae sanción".
- Problema: la seguridad es media línea en una lista y la segunda línea "puede objetar", pero no hay nada sobre qué datos pueden salir a una herramienta externa, clasificación de la información, fugas o ataques a sistemas con IA. La evaluación de impacto en protección de datos no se menciona. Y la garantía de no sanción no dice qué pasa si el uso confesado supuso sacar datos personales o confidenciales, que puede generar obligaciones que la organización no puede perdonar. Busqué "cibersegur", "confidencial", "fuga", "evaluación de impacto", "EIPD": cero. "Protección de datos" aparece como miembro de la segunda línea y como nombre del Reglamento.
- Gravedad: media.
- Corrección: añadir al módulo 11 un apartado de cinco líneas "Seguridad y datos personales" (qué datos pueden usarse con qué herramienta, quién lo decide, evaluación de impacto cuando proceda según el delegado de protección de datos) y, en "El uso informal", la frase: "La garantía cubre haber probado la herramienta, no exime de comunicar y tratar una posible fuga de datos".

### H10. No se dice cuánto cuesta aplicar el método ni cómo se financia el diagnóstico

- Dónde: `05-orden.md`, "Un arranque a cien días" y "Modelo económico"; `06b-detalle-equipo-conocimiento.md`, Módulo 4, "Dedicación".
- Cita: "Presupuesto por fases, reparto pactado de las ganancias e hitos de recuperación". "ninguna función crítica puede estar cubierta por alguien con menos de un tercio de su tiempo".
- Problema: el modelo económico es un producto del diseño (fase 2), así que el diagnóstico se hace sin él. No hay orden de magnitud del coste del equipo de siete funciones, de liberar a quien hace el trabajo ni del propio diagnóstico. El único dato de coste de todo el documento es el del mapa en un caso compuesto ("dos semanas de una persona y unas veinte conversaciones"). Una directora no puede pedir presupuesto con esto.
- Gravedad: media.
- Corrección: añadir a la tabla del módulo 17 una columna "Esfuerzo orientativo del equipo" (personas a tiempo equivalente por fase, marcada como experiencia del autor) y una frase en "Un arranque a cien días": "Los cien días se financian como gasto de diagnóstico, antes de que exista modelo económico".

### H11. La formación se nombra y no se desarrolla

- Dónde: `04-elementos.md`, cap. 17, "El entorno que exige la IA"; `03-tronco.md`, cap. 13, "Formación en el puesto".
- Cita: "la formación por perfil". "No un curso de un día, sino acompañamiento mientras se trabaja".
- Problema: no hay módulo de formación entre los veinticuatro. No se dice qué tiene que saber cada perfil antes del piloto, quién forma, cuántas horas ni cómo se comprueba. El módulo 7 trata de aprender el oficio, que es otra cosa. Busqué "alfabetización": cero. "Formación" aparece ocho veces, siempre de pasada.
- Gravedad: media.
- Corrección: añadir en el cap. 13 una tabla de tres filas (dirección y mandos, quien usa, quien supervisa o es dueño) con "qué tiene que saber antes de" piloto y escala, y quién lo imparte.

### H12. La relación con el área de tecnología no se trata

- Dónde: `05-orden.md`, "El papel de la dirección"; `06b-detalle-equipo-conocimiento.md`, Módulo 4.
- Cita: "Delegar la estrategia de IA entera en el área de tecnología es una forma de no tenerla". Función "Tecnología y datos | Elige, integra y opera la tecnología".
- Problema: el área de tecnología aparece una vez, como advertencia. No se dice qué decide ella y qué el programa, quién es dueño de la plataforma, cómo entra la arquitectura corporativa en las puertas ni quién paga la integración. "Integrar" aparece dos veces. Para una gran empresa es la relación que más conflictos da.
- Gravedad: media.
- Corrección: añadir dos filas a la tabla "Quién decide qué": "Elegir plataforma y arquitectura" y "Aceptar una solución en producción y operarla", con el área de tecnología como decisora y el comité como consultado.

### H13. No se dice cómo escala el mapa a una organización grande

- Dónde: `03-tronco.md`, cap. 9, "El mapa de lo que nadie escribió".
- Cita: "El coste del mapa en ese caso: dos semanas de una persona y unas veinte conversaciones".
- Problema: el único tamaño de referencia es un equipo de doce personas, y es un caso compuesto. Para un área de quinientas personas o varios centros no hay regla de muestreo (a cuántos se pregunta, cuándo se para). Lo mismo vale para el inventario de aportaciones "para cada rol" y el plan de transición "por persona".
- Gravedad: media.
- Corrección: añadir una frase de parada: "Se pregunta por perfil y por centro hasta que dos conversaciones seguidas no añaden filas nuevas", y decir que el coste citado vale para equipos de ese tamaño.

### H14. No se dice qué hacer cuando un elemento está en nivel 1

- Dónde: `05-orden.md`, "Madurez y regla de entrada"; `08-anexos.md`, anexo D.
- Cita: "un acelerador se activa solo si sus condiciones están en nivel 2 o más".
- Problema: la regla bloquea, pero no hay camino para pasar de nivel 1 a nivel 2, ni quién evalúa, ni con qué evidencia, ni qué se hace si los niveles difieren dentro de un elemento (hay patrocinador con tiempo, pero no "una forma acordada de implicar a quien hace el trabajo"). El anexo D da una celda por nivel y elemento.
- Gravedad: media.
- Corrección: añadir bajo la tabla del anexo D una línea por elemento: "Para pasar de 1 a 2 hace falta, como mínimo: ..." y la frase "Evalúa la función de medición con el equipo afectado; vale el nivel más bajo de los rasgos de la celda".

### H15. Una innovación de sistema no puede pasar la puerta del diagnóstico tal como está escrita

- Dónde: `06g-innovacion-agentes.md`, Módulo 23, "Del experimento a la cartera"; `03-tronco.md`, "La puerta del diagnóstico".
- Cita: "entra en la cartera como candidata y recorre el tronco desde el diagnóstico". "la línea base está medida; el mapa de lo que nadie escribió existe".
- Problema: un servicio que todavía no existe no tiene línea base ni trabajo actual que mapear, y el delta no se puede calcular sin línea base. El propio módulo reconoce que el tronco "sirve mal" para lo nuevo, pero manda lo nuevo al tronco sin adaptar la puerta.
- Gravedad: media.
- Corrección: añadir en el módulo 23 una frase: "Para una apuesta de sistema, la línea base es la del servicio o la necesidad más parecida que hoy se atiende, y el mapa se hace sobre el trabajo que cambiaría; si no existe ninguno, la puerta lo dice por escrito".

### H16. No se dice qué pasa entre puertas ni cuántas veces se puede repetir

- Dónde: `03-tronco.md`, cap. 12, "La puerta".
- Cita: "ajustar y repetir si el resultado es prometedor pero incompleto". "Los criterios se escribieron antes, en el diseño, y no se reescriben al ver el resultado".
- Problema: no hay regla para el resultado que no llega por poco (busqué "por poco" y "tolerancia": cero). "Prometedor pero incompleto" queda a juicio. No hay límite de repeticiones ni se dice si al repetir valen los mismos criterios. Tampoco qué se hace si a mitad del piloto cambia algo que no depende del equipo (el proveedor actualiza el modelo, cambia el volumen): ¿se reinicia, se anota, se sigue?
- Gravedad: media.
- Corrección: añadir tres frases: "Un piloto se repite una vez como máximo con los mismos criterios; la segunda vez que no los cumple, se retira o vuelve a diseño". "Si el resultado queda dentro de la variación normal del indicador respecto al umbral, decide el patrocinador y lo motiva por escrito". "Un cambio de modelo durante el piloto obliga a repetir los casos de prueba y se anota en los resultados".

### H17. Hay al menos diecinueve roles u órganos mencionados que no están en la tabla de funciones

- Dónde: `06b-detalle-equipo-conocimiento.md`, Módulo 4, "La composición" (siete funciones); menciones en `03-tronco.md`, `05-orden.md`, `06c`, `06f`, `06g`.
- Cita: "la escala tiene una persona responsable de la adopción, con nombre y con tiempo, distinta de quien despliega la herramienta". "una oficina pequeña de medición y conocimiento". "las puertas las preside el patrocinador con el responsable".
- Problema: fuera de las siete funciones aparecen, sin definición ni encaje: comité de puertas, órgano de dirección, dueño operativo, dueño de la solución, dueño del agente, dueño de los datos, dueño de cada beneficio, responsable de adopción, referentes, persona que responde en cada función, persona que defiende a quien recibe el servicio, mando intermedio en puertas, segunda línea, auditoría interna, laboratorio, oficina de medición y conocimiento, usuarios avanzados, firmante "sin interés", responsable por cadena de agentes. La tabla del módulo 4 es de la versión 1.1 y no recoge lo añadido después. "El responsable" del programa acotado no se sabe quién es.
- Gravedad: media.
- Corrección: añadir al módulo 4 una segunda tabla "Otros papeles que el método nombra": papel, quién suele serlo, en qué fase aparece, de cuál de las siete funciones depende. Sustituir "con el responsable" por "con quien dirige el programa".

### H18. Un programa en marcha recibe puertas sin línea base

- Dónde: `05-orden.md`, "Dimensionamiento".
- Cita: "Se hace un diagnóstico rápido, cada iniciativa se clasifica en mantener, acelerar, reorientar o retirar, y se instalan las puertas a partir de la siguiente fase".
- Problema: "diagnóstico rápido" no se define (qué entregables de los seis se hacen) y, si ya se cambió algo, la línea base "antes de cambiar nada" ya no se puede medir, con lo que los criterios como delta no se pueden escribir. Es el caso de casi todos los clientes del autor.
- Gravedad: media.
- Corrección: añadir dos frases: qué tres entregables forman el diagnóstico rápido y "si no hay línea base anterior, se mide la situación actual, se declara como línea base tardía y se dice qué mejora anterior queda sin poder atribuirse".

### H19. Solo tres de los veinticuatro módulos dicen cómo se miden

- Dónde: `06a-detalle-personas-trabajo.md`, introducción de la Parte V.
- Cita: "Todos siguen la misma estructura: qué es y por qué importa, lo que dicen las fuentes, cómo se hace, cómo se mide, las señales de que va mal y lo que todavía no está resuelto".
- Problema: comprobado con los encabezados: "Cómo se mide" solo existe en los módulos 6, 7 y 23. Los módulos 10, 13, 19 y 22 no tienen apartado de fuentes. Los módulos 3, 7, 11, 16, 17, 19, 20, 21 y 22 no tienen señales de que va mal. Los módulos 10, 12, 14 y 18 no tienen pregunta abierta. Quien busque el indicador de un módulo no lo encuentra en veintiuno de ellos.
- Gravedad: baja.
- Corrección: cambiar la frase por "Casi todos siguen esta estructura; donde falta un apartado es porque no lo tengo" o añadir una línea "Cómo se mide" a cada módulo que hoy no la tiene.

---

## Bloque 2. Ambigüedades

### A1. "Ciclo" significa al menos tres cosas y no está en el glosario

- Dónde: `03-tronco.md`, caps. 8 y 14; `05-orden.md`, "Medición y el delta" y "Dimensionamiento"; `06e`, Módulo 17; `08-anexos.md`, anexo A.
- Cita: "Un programa grande tiene varios ciclos en paralelo, cada uno en su fase". "los indicadores aguantan dos ciclos sin el equipo del programa". "Dos ciclos de medición, al menos". "al cierre de cada ciclo se vuelve a decidir, para cada solución en uso".
- Problema: unas veces ciclo es el recorrido completo de las cinco fases, otras un periodo de medición, otras un periodo de gestión (se revisa el radar, la cartera, el coste por tarea "cada ciclo"). Con la primera lectura, la puerta de sostenimiento es circular: la fase 5 de un ciclo no puede esperar a que pasen "dos ciclos". Con la segunda, no se sabe cuánto dura (¿un mes, un trimestre?). El programa acotado tiene "un solo ciclo" y aun así debe aguantar "dos ciclos". El glosario no define el término (comprobado: no hay entrada).
- Gravedad: alta.
- Corrección: añadir al glosario dos entradas distintas: "Vuelta: el recorrido de las cinco fases para un ámbito" y "Periodo de medición: el intervalo, fijado en el diseño, en que se leen los indicadores (por defecto, un trimestre)". Sustituir "dos ciclos" por "dos periodos de medición" en los caps. 8 y 14.

### A2. No se sabe qué recorre el tronco: el programa, el ciclo, la iniciativa o la opción

- Dónde: `03-tronco.md`, cap. 10, "Una cartera priorizada"; `06g`, Módulo 23, "Del experimento a la cartera"; `06d`, Módulo 14.
- Cita: "**Una cartera priorizada.** Pocas iniciativas, ordenadas por cuánto atacan la restricción" (producto de la fase de diseño). "entra en la cartera como candidata y recorre el tronco desde el diagnóstico".
- Problema: la cartera es un producto del diseño, que viene después del diagnóstico, pero una candidata entra en la cartera y entonces empieza su diagnóstico. No queda claro si hay un diagnóstico por ámbito del que salen varias iniciativas que se pilotan, o un diagnóstico por iniciativa. Programa, ciclo, iniciativa, opción de diseño, caso de uso, solución, sistema y agente se usan sin relación declarada. De eso depende cuántos diagnósticos, mapas y puertas hay que hacer.
- Gravedad: alta.
- Corrección: añadir al cap. 8 un esquema de cuatro líneas: "Un programa tiene uno o varios ámbitos. Cada ámbito hace un diagnóstico. Del diagnóstico salen iniciativas, que forman la cartera. Cada iniciativa compara opciones en el diseño y recorre piloto, escala y sostenimiento". Y ajustar la frase del módulo 23 a "vuelve al diagnóstico de su ámbito".

### A3. Elemento y acelerador se solapan, y la regla de entrada está escrita de tres formas

- Dónde: `02-arquitectura.md`, "Principio 2" y tabla "Qué agrupa cada componente"; `05-orden.md`, "Madurez y regla de entrada"; `08-anexos.md`, anexo A.
- Cita: "Un acelerador entra en una fase solo si los tres elementos están, para esa fase, al menos en el nivel 2". "un acelerador se activa solo si sus condiciones están en nivel 2 o más. La IA en piloto dentro del servicio exige gobierno y personas en nivel 2 como mínimo". "La escala de madurez tiene cuatro niveles y se aplica a cada elemento y a cada acelerador". Glosario: "Acelerador | [...] (la IA, una plataforma, la automatización)". Elemento tecnología: "La IA en sus dos papeles [...] las demás tecnologías (plataforma, automatización, entrega continua)".
- Problema: la IA, la plataforma y la automatización son a la vez el elemento tecnología y los aceleradores, de modo que "elemento antes que acelerador" pide que la tecnología esté madura antes de que entre la tecnología. La regla aparece con tres condiciones distintas: los tres elementos; "sus condiciones"; gobierno y personas (el gobierno no es un elemento y el conocimiento desaparece). El anexo D solo da escala para los elementos, no para los aceleradores ni para el gobierno. No hay lista cerrada de qué cuenta como acelerador, y de ella depende el límite de "uno o dos".
- Gravedad: alta.
- Corrección: una sola redacción en los dos sitios: "Un acelerador entra en una fase si personas, conocimiento y tecnología están en nivel 2 en el ámbito". Añadir al glosario la lista de aceleradores que el método reconoce y la frase "El elemento tecnología es la capacidad de la organización para gobernar y usar tecnología; el acelerador es la herramienta concreta que entra".

### A4. Acelerar, automatizar y aumentar no se pueden distinguir con las definiciones dadas

- Dónde: `03-tronco.md`, cap. 11, pregunta 2; `04-elementos.md`, cap. 17, "Acelerar, automatizar o aumentar".
- Cita: "Acelerar es hacer la misma tarea más rápido con la misma persona [...] aumentar es que la persona haga algo que antes no podía, o lo haga mejor". "**Aumentar:** con un asistente de IA, los agentes de atención al cliente resolvieron de media un 15 % más de casos por hora". "**Acelerar:** [...] tardaron un 40 % menos y su trabajo salió con una calidad un 18 % mayor".
- Problema: el propio documento pone como ejemplo de aumentar un resultado de más casos por hora (más rápido, misma tarea, misma persona: su definición de acelerar) y como ejemplo de acelerar uno que también mejora la calidad (su definición de aumentar). Si el autor los cruza, dos comités también. Además la mayoría de las opciones reales mezclan los tres verbos por tareas, y el texto reconoce que la distinción "no tiene una fuente que la respalde". La puerta obliga a elegir uno.
- Gravedad: alta.
- Corrección: añadir una regla de decisión de tres líneas en la pregunta 2: "Se responde por tarea, no por opción. Si la persona sale del circuito, automatiza. Si sigue y el resultado esperado es solo tiempo, acelera. Si se espera mejor calidad o algo que antes no hacía, aumenta, y se dice con qué indicador". Y mover el ejemplo de los agentes de atención al cliente al verbo que corresponda con esa regla.

### A5. "Puerta" se usa para cuatro cosas distintas

- Dónde: `08-anexos.md`, anexo A; `04-elementos.md`, "La escala de autonomía"; `03-tronco.md`, cap. 13; `06a`, Módulo 3; `06g`, Módulo 24.
- Cita: Glosario: "El punto de decisión al final de cada fase". "cada subida se gana en una puerta con evaluaciones superadas". "Cada etapa tiene su propia mini puerta". "la puerta del ciclo puede decidir bajar de nivel". Tabla de controles: "Controles que tienen que existir antes de subir".
- Problema: hay puertas de fase, mini puertas de etapa, puertas de subida de autonomía y una "puerta del ciclo". Solo la primera está definida. No se sabe si una subida de autonomía tiene que esperar al final de una fase, quién la decide en un programa acotado sin comité, ni si un sistema puede empezar el piloto en nivel 2 o 3 o debe empezar siempre en el 1. En la tabla de controles, "antes de subir" no aclara si los controles de la fila son para estar en ese nivel o para pasar al siguiente.
- Gravedad: media.
- Corrección: añadir al glosario "Puerta de autonomía: decisión de subir o bajar un nivel, que puede tomarse en cualquier momento con los criterios escritos". En la tabla de controles, cambiar la cabecera a "Controles que tienen que existir para operar en este nivel". Añadir: "El nivel de entrada al piloto se fija en la puerta de diseño".

### A6. "Dueño" tiene nueve usos y no se dice si son la misma persona

- Dónde: `03-tronco.md`, cap. 14; `05-orden.md`, tabla "Quién decide qué"; `06c`, Módulos 9, 10 y 11; `06g`, Módulo 24; `06b`, Módulo 4.
- Cita: "Un dueño operativo con nombre". "Dueño de la solución, con nueva evaluación". "Su dueño y cualquier persona de la capa de uso". "Una persona con nombre, la misma que figura en el inventario". "cada pieza tiene un dueño en el equipo que opera". "cada beneficio tiene un dueño en el negocio".
- Problema: dueño operativo, dueño de la solución, dueño del sistema, dueño del agente, dueño de la pieza en el equipo que opera, dueño de los datos, dueño del beneficio, dueño del documento y dueño de la estrategia. No se dice cuáles coinciden. Para un mismo agente puede haber cuatro personas distintas que "responden", que es lo que el método quiere evitar ("Una persona, que puede apoyarse en un comité").
- Gravedad: media.
- Corrección: añadir al glosario la entrada "Dueño" con una tabla de cuatro filas (del servicio o solución, de los datos, del beneficio, de la estrategia) y la frase "El dueño de la solución es el dueño operativo, el del agente y quien figura en el inventario: una sola persona".

### A7. El derecho a parar no dice qué se para ni quién vuelve a arrancar

- Dónde: `05-orden.md`, tabla "Quién decide qué" y "Tres capas de responsabilidad".
- Cita: "Parar un sistema en uso | Su dueño y cualquier persona de la capa de uso, sin autorización previa".
- Problema: en una gran empresa, leído literalmente, cualquier usuario puede detener un sistema en producción para todos. No se dice si para solo su caso, su puesto o el servicio entero, a quién avisa, quién decide reanudar ni en qué plazo. Sin eso, seguridad y operaciones lo vetarán o quedará en el papel.
- Gravedad: media.
- Corrección: cambiar la celda por: "Cualquier persona de la capa de uso puede dejar de usarlo en su caso y pedir la parada al dueño, que responde en el día; el dueño puede parar el servicio entero. Reanudar lo decide el dueño y lo anota".

### A8. "Restricción": una, pero no se dice por qué unidad, y la excepción lo admite todo

- Dónde: `03-tronco.md`, cap. 9 y tabla del cap. 8.
- Cita: "Tiene que ser una, nombrada". "Cada iniciativa ataca la restricción o tiene motivo escrito".
- Problema: en un programa de "una organización entera" con varios ciclos en paralelo no se sabe si hay una restricción por programa o una por ámbito. "Motivo escrito" no tiene requisito alguno: cualquier iniciativa pasa con una frase. Tampoco se dice qué ocurre cuando la restricción se mueve tras una mejora, que es lo esperable según la fuente que se cita.
- Gravedad: media.
- Corrección: añadir "una por ámbito diagnosticado" y limitar la excepción: "Como máximo una de cada tres iniciativas de la cartera puede no atacar la restricción, y solo si es un habilitador (módulo 14) o una obligación legal". Añadir: "En cada puerta de escala se comprueba si la restricción sigue siendo la misma".

### A9. "Área", "función", "referente", "centro" y "equipo del programa" no se delimitan

- Dónde: `03-tronco.md`, cap. 13, "Varios referentes por área" y "El modelo operativo cambia con la fase"; cap. 14, "La puerta".
- Cita: "Mi punto de partida es al menos dos referentes por área". "personas que ya usan bien la herramienta, que se reconocen como tales". "En el sostenimiento el centro queda como apoyo". "los indicadores aguantan dos ciclos sin el equipo del programa".
- Problema: no se dice qué es un área (¿un equipo de ocho, una dirección de cuatrocientos?), quién reconoce a un referente ni cuántas horas tiene. Y si el centro "queda como apoyo" con gobierno, plataforma, estándares y medición, no se sabe si la condición "sin el equipo del programa" se cumple o no mientras el centro sigue ahí.
- Gravedad: media.
- Corrección: añadir "área: la unidad con un mando directo, normalmente de 10 a 40 personas" (o la cifra que el autor use), "los referentes los nombra el responsable de adopción a propuesta del equipo, con un mínimo de horas escrito", y en el cap. 14: "sin el equipo significa sin nadie del programa haciendo trabajo del servicio ni empujando los indicadores; el apoyo del centro a petición no cuenta".

### A10. Criterios cualitativos sin número ni forma de fijarlo

- Dónde: varios. `04-elementos.md` (tabla de autonomía, "Interacción"); `06a`, Módulo 2, paso 3; `04-elementos.md`, cap. 15; `06g`, Módulo 23; `03-tronco.md`, cap. 10.
- Cita: "baja y estable". "pocos, conocidos y reversibles". "Si alguna cae mucho, se rediseña". "una parte relevante de la cartera nace de empleados y de usuarios". "dedicar un tiempo fijo cada semana". "Pocas iniciativas". "un presupuesto pequeño y fijado de antemano". "respuesta en plazo".
- Problema: son las expresiones de las que dependen decisiones y niveles de madurez, y ninguna tiene valor de partida ni responsable de fijarlo. (Las cifras que el autor declara no tener en recuadros no se cuentan aquí.)
- Gravedad: media.
- Corrección: añadir un anexo G de media página, "Valores de partida", con una fila por expresión, un valor orientativo marcado como tal y quién lo fija en cada programa.

### A11. "Función crítica" y la regla del tercio de jornada

- Dónde: `06b`, Módulo 4, "Dedicación" y "La composición".
- Cita: "ninguna función crítica puede estar cubierta por alguien con menos de un tercio de su tiempo". "En un programa acotado, varias recaen en la misma persona".
- Problema: no se dice cuáles de las siete funciones son críticas. Si lo son las seis que no son patrocinio y tres recaen en una persona, esa persona ya está al cien por cien. Dos lectores calcularán equipos muy distintos.
- Gravedad: media.
- Corrección: añadir a la tabla de funciones una columna "Dedicación mínima" con valores para programa acotado y amplio, y decir cuáles se pueden acumular en una persona.

### A12. La plantilla del mapa no coincide con lo que el texto le pide al mapa, y el anonimato choca con sus usos

- Dónde: `03-tronco.md`, cap. 9, "Cómo se dibuja" y "El límite del mapa"; `06b`, Módulo 6, "La dependencia silenciosa" y "Cómo se mide"; `08-anexos.md`, anexo B.
- Cita: "Es una tabla de cuatro columnas: qué se sabe, quién lo sabe, dónde se usa y cuán concentrado está". "muestra el conocimiento, no a quien lo tiene, hasta que ella decida otra cosa". "en el mapa se añade, para cada fila que pasa al sistema, quién mantiene la capacidad de hacerlo sin él". "cuántas filas críticas del mapa siguen en una sola persona".
- Problema: el indicador de conocimiento necesita una columna de criticidad y el módulo 6 añade otra (quién mantiene la capacidad); ninguna está en el anexo B. Por otro lado, el mapa no debe mostrar a quien sabe, pero tiene una columna "Quién lo sabe", en un equipo de doce "Perfil A" identifica a la persona, y otras piezas necesitan el nombre: el plan de transición por persona, la red de conectores (señal de fallo: "El programa no sabe quiénes son los conectores centrales") y la columna del inventario "qué sabe hoy quien hace ese trabajo".
- Gravedad: media.
- Corrección: añadir al anexo B las columnas "Crítica (sí o no, la fija quien usa el resultado)" y "Quién mantiene la capacidad si pasa al sistema". Añadir una frase: "Hay dos versiones del mapa: la de trabajo, con nombres, que solo ve la función de conocimiento, y la de comité, por perfiles".

### A13. Quién firma una puerta: tres respuestas

- Dónde: `08-anexos.md`, anexo C; `05-orden.md`, tabla "Quién decide qué"; `03-tronco.md`, cap. 12.
- Cita: "Firma | Patrocinador y responsable de medición". "Retirar una solución | Comité de puertas, con la firma de alguien sin interés en ella". "alguien sin interés en la iniciativa (por ejemplo, el responsable de medición)".
- Problema: unas veces firma el patrocinador con medición, otras el comité con un tercero. Y el responsable de medición es una de las siete funciones del equipo del programa: su trabajo depende de que el programa siga, así que presentarlo como persona "sin interés" es discutible.
- Gravedad: media.
- Corrección: una línea en "Gobierno": "Toda decisión de puerta la firma el patrocinador. La contrafirma alguien de fuera del equipo del programa (segunda línea o finanzas). Medición certifica los datos, no la decisión".

### A14. "La tercera pregunta del mapa" son dos preguntas distintas, y "cuatro reglas" son seis

- Dónde: `04-elementos.md`, cap. 15, "Lo que no encaja en el patrón"; `06b`, Módulo 5, "El mapa como red"; `05-orden.md`, "Medición y el delta".
- Cita: "La tercera pregunta del mapa (qué le pasa a cada fila con cada opción)". "La tercera pregunta del mapa de lo que nadie escribió (a quién llamas cuando algo se atasca, y quién te llama a ti)". "La medición en Synergós tiene cuatro reglas".
- Problema: el mapa tiene tres preguntas para el comité y cinco para las entrevistas, y se cita "la tercera" de ambas listas con el mismo nombre. En medición, tras anunciar cuatro reglas hay seis apartados en negrita (línea base; pocos indicadores en pareja; el delta; tres indicadores como mínimo; uso con capacidad; tres niveles) más dos cautelas. Quien haga una lista de comprobación no sabe cuáles son las cuatro.
- Gravedad: baja.
- Corrección: llamar "preguntas del comité" y "preguntas de las grietas" a cada lista, y cambiar "cuatro reglas" por "seis reglas y dos cautelas".

---

## Bloque 3. Problemas de lógica o de método

### P1. El delta depende de un objetivo que nadie regula: quien fija el objetivo fija el resultado

- Dónde: `05-orden.md`, "Medición y el delta"; `03-tronco.md`, cap. 10, "Los criterios del piloto"; `08-anexos.md`, anexo A.
- Cita: "El delta de un indicador es lo que ha avanzado desde su línea base hacia su objetivo, en porcentaje. Si el tiempo medio de respuesta estaba en diez días, el objetivo es cuatro y ahora está en siete, el delta es del cincuenta por ciento". "Se expresan como delta mínimo respecto a la línea base".
- Problema: la aritmética del ejemplo es correcta: (10 - 7) / (10 - 4) = 3 / 6 = 50 %. El fallo es otro. El delta necesita un objetivo por indicador y el documento no dice quién lo fija, cuándo ni con qué criterio (solo habla de los pesos). Con los mismos datos, si el objetivo fuera seis días en vez de cuatro, el delta sería (10 - 7) / (10 - 6) = 75 %. Un piloto mediocre pasa la puerta bajando el objetivo. La pregunta abierta sobre el delta habla de los pesos y no de esto, que es un hueco mayor. Tampoco se dice si el delta se topa en 100 % (un indicador que se pasa del objetivo puede tapar a otro en la media) ni cómo cuenta un delta negativo.
- Gravedad: alta.
- Corrección: añadir tras la definición: "El objetivo de cada indicador se fija y se firma en el diseño junto con los pesos, con su justificación (de dónde sale), y no cambia hasta la siguiente vuelta. El delta de un indicador se topa en 100 %. Los criterios de puerta se escriben además en la unidad del indicador (de diez días a siete), no solo como porcentaje".

### P2. El delta no se puede calcular para varios de los indicadores que el propio método obliga a usar

- Dónde: `05-orden.md`, "Tres indicadores como mínimo: uno por elemento", "El uso, en pareja con la capacidad"; `06b`, Módulo 7, "Cómo se mide".
- Cita: "Para personas, algo como el criterio que conserva la gente". "Para tecnología, el uso real". "la proporción de tareas que alguien del área resuelve bien sin ayuda de la herramienta". "El indicador es el tiempo que tarda alguien nuevo en resolver solo los casos difíciles".
- Problema: tres casos. (a) Indicadores que solo deben conservarse (el criterio que se conserva, la calidad cuando se mejora la velocidad): objetivo igual a línea base, y la fórmula divide por cero. (b) Indicadores que no existen antes de la herramienta (uso, capacidad "con la herramienta y sin ella", tasa de corrección): no tienen línea base "antes de cambiar nada"; el uso parte de cero y su delta es simplemente uso dividido por objetivo. (c) Indicadores que tardan años (el tiempo de un nuevo hasta resolver solo los casos difíciles) no dan dato en un piloto de ocho a dieciséis semanas. Con eso, "una sola unidad para la mejora" no cubre los tres indicadores mínimos.
- Gravedad: alta.
- Corrección: añadir una frase: "Hay dos clases de indicador. Los de avance tienen objetivo y entran en el delta. Los de guarda solo tienen un suelo (no bajar de X) y no entran en la media: se cumplen o no". Y decir de cada indicador obligatorio de qué clase es y cuál es su línea base cuando no existía antes.

### P3. "Ningún indicador retrocede" contradice la curva J que el método dice esperar en el piloto

- Dónde: `05-orden.md`, "Medición y el delta" y "Modelo económico"; `06d`, Módulo 12, "Cuidar la zona neutra"; `08-anexos.md`, anexo C.
- Cita: "el piloto pasa si el delta del ciclo supera el cuarenta por ciento y ningún indicador retrocede". "durante un tiempo la productividad medida baja antes de subir". "Es el momento del piloto y de las primeras etapas de la escala. La productividad baja (la curva J)".
- Problema: el método afirma que en el piloto la productividad baja y a la vez pone como criterio tipo de puerta (está en la plantilla del anexo C) que ningún indicador retroceda. Las dos cosas no pueden ser ciertas a la vez. Además, sin margen de tolerancia, un indicador que baje una décima por variación normal bloquea la puerta.
- Gravedad: alta.
- Corrección: cambiar el criterio tipo por: "ningún indicador de guarda baja de su suelo, y los indicadores para los que el modelo económico prevé valle no bajan más de lo previsto". Añadir que el suelo se fija con la variación normal de la línea base.

### P4. La regla que sostiene la promesa no se puede aplicar: el indicador de personas es obligatorio y no tiene medida

- Dónde: `05-orden.md`, "Tres indicadores como mínimo" y pregunta abierta "¿Cómo se mide el criterio de las personas?"; `03-tronco.md`, "La puerta del diagnóstico".
- Cita: "Si solo mejora el tercero, la transformación está rota aunque los números de la tecnología sean excelentes". "Es el indicador que más falta y el que peor sé medir". "la línea base está medida".
- Problema: el recuadro reconoce la duda, pero tapa un hueco mayor: la puerta del diagnóstico exige línea base medida, la del piloto exige un indicador por elemento dentro del delta, y la regla que define el fracaso ("solo mejora el tercero") necesita el de personas. Sin medida operativa para el lunes, las tres reglas quedan a juicio. Los sustitutos que sí se pueden medir (rotación, carga percibida) el propio texto los descarta o los deja como añadidos.
- Gravedad: alta.
- Corrección: declarar un indicador de personas por defecto mientras la pregunta sigue abierta, por ejemplo: "proporción de casos fuera de patrón resueltos por el equipo sin escalar, medida por muestreo antes y durante el piloto, más carga percibida como indicador de guarda". Decir que es provisional.

### P5. La carga documental antes de un piloto no cabe en los plazos ni en los principios del método

- Dónde: suma de `03-tronco.md` (caps. 9, 10 y 12), `04-elementos.md`, `05-orden.md`, módulos 1 a 24 y anexos B y C; frente a `02-arquitectura.md`, "Principio 3" y "Principio 2", y `06e`, Módulo 17.
- Cita: "Pocas cosas a la vez". "La evaluación tiene que durar horas, no semanas". "Diagnóstico | De tres a seis semanas". "Diseño | De cuatro a ocho semanas". "un documento de una página que responde a las cinco preguntas de la puerta".
- Problema: he contado lo que alguien tiene que dejar escrito antes de empezar un piloto. Son unas 44 piezas distintas.
  - Diagnóstico, cap. 9 (6): mapa del flujo real, restricción, línea base, mapa de actores, madurez, mapa de lo que nadie escribió.
  - Diagnóstico, añadidas en otros sitios (16): compromiso firmado sobre el uso del mapa (anexo B); obligaciones del patrocinador por escrito (cap. 15); inventario de aportaciones por rol (módulo 1); descomposición en tareas (módulo 2); tareas candidatas (módulo 3); red de a quién se acude (módulo 5); línea base del aprendizaje del oficio (módulo 7); árbol de la restricción al efecto económico (módulo 9); calidad de los datos con cuatro indicadores (módulo 10); inventario de sistemas y de uso informal con consulta anónima (cap. 18 y módulo 11); tabla de derechos de decisión (cap. 18); lectura de supuestos de cultura (módulo 16); clase de referencia de tres programas (módulo 17); información a la representación legal (módulo 18); soltura digital real (módulo 20); mapa del recorrido de quien recibe el servicio (módulo 21).
  - Diseño, cap. 10 (6): cartera, diseño del trabajo, aceleradores por fase, criterios del piloto, modelo económico, decisión escrita por opción.
  - Diseño, añadidas (16): criterio de parada y fecha de revisión; registro de supuestos; casos de prueba (cap. 12); techo de autonomía; criterio, responsable y registro por peldaño (cap. 17); ficha del agente con once campos y columna de seis anotaciones (módulo 24 y cap. 17); matriz de siete criterios por tarea; señales de retirada (módulo 3); límite de iniciativas, etiqueta de alcance y lista de habilitadores (módulo 14); objetivos y pesos del delta (cap. 18); diseño elegido para aprender el oficio (módulo 7); dueños de los datos y salida pactada (módulos 10 y 13); clasificación de riesgo y responsable con nombre (módulo 11); dueño de cada pieza en el equipo que opera (módulo 4); separación escrita entre asistir y vigilar (módulo 18); plan de transición por persona si un rol se reduce (módulo 19).
  - La "una página" por opción tiene 13 campos en el anexo C, y los módulos le añaden al menos 11 líneas que el anexo no recoge: tres de las necesidades (módulo 8, "una línea cada una, en la decisión de puerta"), cinco de la estrella (módulo 16, "una línea por punta"), huella y dependencia (módulo 22), aportaciones que conserva, amplía y elimina (módulo 1) y accesibilidad "como criterio de puerta" (módulo 21). Y es una página por cada opción.
  - Después hay al menos 17 revisiones periódicas distintas repartidas por el texto (semanal de cartera, quincenal de pruebas, tras cada puerta, retrospectiva por ciclo, trimestral de supuestos, trimestral de capacidades perdidas, construir, comprar o retirar, radar, coste por tarea, casos de prueba, inventario, derechos de decisión, madurez, supuestos en cada puerta, clasificación de cartera, cuadro a la dirección, auditoría anual) y más de veinte indicadores pedidos en nueve sitios, frente a "pocos indicadores".
  - No es realista para "un equipo" en siete a catorce semanas de diagnóstico y diseño, cuando solo el mapa cuesta, según el propio texto, dos semanas de una persona. Choca con "pocas cosas a la vez", con "la medida justa" y con la crítica que el cap. 20 reconoce ("Puede convertirse en burocracia") sin dar el remedio.
- Gravedad: alta.
- Corrección: la tabla de H1 resuelve la mayor parte. Además: actualizar el anexo C para que contenga todas las líneas que los módulos le añaden y decir cuántas páginas son de verdad; y añadir un anexo "Calendario de revisiones" con una fila por revisión, frecuencia y responsable, fusionando las que coinciden.

### P6. La tasa de corrección sirve a la vez para subir de autonomía, para retirar y como señal de supervisión vacía

- Dónde: `04-elementos.md`, tabla de la escala de autonomía; `06a`, Módulo 3, "Cuándo quitarla"; `06g`, Módulo 24, "Supervisión que supervise".
- Cita: Para subir del nivel 2: "La tasa de corrección es baja y estable en casos reales". Señal de retirada: "que la tasa de corrección deje de bajar o vuelva a subir". "Si aprueba todo en segundos, la supervisión existe solo en el papel".
- Problema: una tasa "estable" es condición para subir y "que deje de bajar" es señal de retirada: es el mismo hecho. Y una tasa baja puede significar que el sistema acierta o que la persona ha dejado de mirar, que es el sesgo que el módulo 2 describe. El indicador elegido como llave de la autonomía no distingue los dos casos.
- Gravedad: alta.
- Corrección: en la tabla de autonomía, cambiar el criterio del nivel 2 por: "la tasa de corrección es baja y estable y una muestra revisada a ciegas por otra persona confirma la tasa de error". En el módulo 3, cambiar "deje de bajar o vuelva a subir" por "vuelva a subir, o se estanque por encima del valor fijado".

### P7. El techo de nivel 3 para decisiones sobre derechos permite decidir sin revisión humana de cada caso

- Dónde: `04-elementos.md`, cap. 17, "Un techo explícito" y tabla de autonomía; `06e`, Módulo 18, "Las decisiones automatizadas".
- Cita: "las decisiones que afectan a derechos de las personas, que no se pueden deshacer o que la organización tiene que poder explicar a quien las recibe se quedan como máximo en el nivel 3, con revisión humana". Nivel 3: "Decide en los casos tipo" y la persona "Revisa por muestreo y todos los casos fuera de patrón".
- Problema: en el nivel 3 el sistema decide los casos tipo y la persona solo ve una muestra. Para los casos no muestreados, la decisión es solo automática. El propio módulo 18 recuerda el derecho a no ser objeto de una decisión basada únicamente en un tratamiento automatizado. Una administración que tramite prestaciones siguiendo esta regla de partida puede estar incumpliendo. La frase "con revisión humana" da a entender una garantía que el nivel 3 no da.
- Gravedad: alta.
- Corrección: cambiar la regla de partida a "se quedan como máximo en el nivel 2 (la persona revisa cada propuesta y decide), salvo que el análisis jurídico del caso permita otra cosa".

### P8. Las duraciones no cuadran entre sí

- Dónde: `05-orden.md`, "Dimensionamiento"; `06e`, Módulo 17, "Órdenes de magnitud"; `03-tronco.md`, cap. 12.
- Cita: "**Un programa acotado** (un equipo, menos de seis meses)". Tabla para "un programa acotado (un equipo, un servicio)": "De tres a seis semanas", "De cuatro a ocho semanas", "De ocho a dieciséis semanas", "De tres a nueve meses", "Dos ciclos de medición, al menos". "una fecha de revisión a noventa días como máximo".
- Problema: aritmética. Mínimo de las tres primeras fases: 3 + 4 + 8 = 15 semanas, unos tres meses y medio. Más el mínimo de escala, tres meses: seis meses y medio antes de empezar el sostenimiento. El máximo: 6 + 8 + 16 = 30 semanas más nueve meses, unos dieciséis meses. El programa acotado de "menos de seis meses" no cabe ni en el mejor caso de la tabla que el propio documento da para ese mismo tipo de programa. Además, el piloto dura hasta dieciséis semanas (112 días) y la revisión obligatoria es a noventa días como máximo: o la revisión no es la puerta, o el piloto no puede durar más de trece semanas.
- Gravedad: media.
- Corrección: cambiar "menos de seis meses" por "hasta la puerta del piloto en menos de seis meses" o ajustar la tabla. En el cap. 12, añadir: "La revisión a noventa días es una revisión intermedia cuando el piloto dura más; la puerta sigue siendo al final".

### P9. "Diagnóstico antes que solución" convive con una solución que ya está decidida antes del diagnóstico: la IA

- Dónde: `02-arquitectura.md`, "Principio 1" y "Principio 3"; `05-orden.md`, "Dimensionamiento"; `06a`, Módulo 3, "Cuándo no".
- Cita: "Prohíbe aprobarla antes de saber qué problema resuelve". "La IA se planifica en todas las fases". "un solo ciclo; la IA y un acelerador más". "Si la restricción es que dos departamentos no se hablan, ninguna IA lo arregla".
- Problema: el método critica llegar con la herramienta decidida y a la vez da por hecho que todo programa lleva IA en todas las fases, también el más pequeño. Si el diagnóstico concluye que la restricción no es de las que la IA resuelve, no se dice qué queda del programa. Un crítico dirá que es un método con la solución puesta.
- Gravedad: media.
- Corrección: cambiar la frase del principio 3 por: "La IA como herramienta del equipo que transforma se considera en todas las fases. La IA dentro del servicio entra solo si el diagnóstico lo justifica, y un programa Synergós puede terminar sin ella".

### P10. "Pocas cosas a la vez" prohíbe lo que el resto del método obliga a hacer a la vez

- Dónde: `02-arquitectura.md`, "Principio 3"; frente a `03-tronco.md`, cap. 10 y 13, `05-orden.md`, "Medición", `06c`, Módulo 10.
- Cita: "Un programa que activa a la vez la IA, una plataforma nueva, un rediseño de procesos, un cambio de estructura y un nuevo modelo de medición no está transformando nada; está generando ruido que nadie puede atribuir".
- Problema: el método exige, en todo programa, IA, rediseño del trabajo antes de elegir herramienta, roles, carreras e incentivos rediseñados, un modelo de medición nuevo (el delta), gobierno nuevo e inventario, y "plataforma antes que piezas". Es casi literalmente la lista que el principio condena. Además el límite es "uno o dos aceleradores por fase" en el principio y "por ciclo" en el dimensionamiento.
- Gravedad: media.
- Corrección: reescribir la frase para que el límite se refiera solo a aceleradores (herramientas) y decir: "Lo que el método pide siempre (rediseño del trabajo, medición, gobierno) no cuenta en ese límite". Unificar "por ciclo" o "por fase".

### P11. Gobierno: tres sitios, tres listas de campos para el "inventario único", dos tablas de derechos y una contradicción

- Dónde: `04-elementos.md`, cap. 17, "Qué se gobierna" y "Construir, comprar o retirar"; `05-orden.md`, cap. 18, "Gobierno"; `06c`, Módulo 11, "Registro"; `06g`, Módulo 24, "La ficha del agente"; `06b`, Módulo 5.
- Cita: "con dueño, nivel de autonomía, proveedor, datos y la columna de personas y conocimiento". "con su nivel de riesgo, su responsable, sus datos, su nivel de autonomía y sus incidentes". Ficha: once campos. "Cambiar de proveedor o de modelo | Dueño de la solución". "La decisión la toma el comité de puertas [...] No la toma el proveedor ni el equipo que la construyó".
- Problema: el inventario se describe tres veces con campos distintos. La columna de Synergós tiene seis anotaciones en el cap. 17 y dos en la ficha del agente (se pierden, entre otras, vigilancia e incentivo). Los derechos de decisión son una tabla de siete filas en el cap. 18 y "diez o quince decisiones" con consulta e información en el módulo 5. Y sustituir una solución por otra comprada lo decide el comité según el cap. 17 y el dueño según la tabla del cap. 18. No se dice cuál manda. Añadido: el comité acumula aprobar cada caso, cada peldaño, cada retirada y la revisión de cada solución en cada ciclo, que es el cuello de botella que el módulo 4 advierte ("Un centro que lo decide todo").
- Gravedad: media.
- Corrección: dejar una sola definición del inventario (la ficha del módulo 24, ampliada con riesgo, proveedor, incidentes y las seis anotaciones) y remitir a ella desde los otros dos sitios. En la tabla de derechos, partir la fila: "Cambiar de versión de modelo: dueño, con nueva evaluación. Cambiar de proveedor o de solución: comité".

### P12. Cartera: tres sitios con reglas de orden distintas

- Dónde: `03-tronco.md`, cap. 10; `06d`, Módulo 14; `06g`, Módulo 23; `04-elementos.md`, "El radar".
- Cita: "ordenadas por cuánto atacan la restricción". "Priorizar por la restricción y por el coste del retraso". "Se aprueban por las iniciativas que desbloquean". "movimientos sin arrepentimiento, que se adoptan".
- Problema: el cap. 10 ordena por un criterio, el módulo 14 por dos sin decir cómo se combinan, los habilitadores entran por un tercero, y el radar "adopta" movimientos sin decir si pasan por la cartera y su límite. El límite de iniciativas "se fija en el diseño, según la capacidad del equipo" sin forma de calcularlo; la única referencia es una señal de fallo ("más iniciativas que personas en el equipo").
- Gravedad: media.
- Corrección: en el módulo 14, una regla de orden única: "Primero las que atacan la restricción, ordenadas por coste del retraso; después los habilitadores que estas necesitan; el resto espera". Y en el radar: "se adoptan pasando por la cartera".

### P13. La escala de madurez mide cuánto Synergós se ha aplicado, y la IA entra en el diagnóstico antes de que la regla lo permita

- Dónde: `08-anexos.md`, anexo D; `04-elementos.md`, cap. 17, "Los dos papeles de la IA"; `02-arquitectura.md`, "Principio 2".
- Cita: Conocimiento, nivel 2: "Hay un mapa hecho y un registro de decisiones que se usa". Tecnología, nivel 3: "La tecnología entra por las puertas; la autonomía sube por niveles". "Herramienta del equipo desde el primer día del diagnóstico: minería de procesos, análisis de documentación, síntesis de entrevistas".
- Problema: los niveles se definen con las piezas del propio método, así que una organización "madura" al aplicarlo: es circular y no dice nada de su capacidad real. Y hay un orden imposible: el conocimiento solo llega a nivel 2 cuando el mapa está hecho, que es al final del diagnóstico, pero la IA (un acelerador) se usa desde el primer día del diagnóstico, antes de evaluar la madurez. Lo mismo con "la evaluación tiene que durar horas" si la evidencia del nivel 2 es un mapa que cuesta dos semanas.
- Gravedad: media.
- Corrección: añadir una frase en la regla de entrada: "La regla se aplica a la IA dentro del servicio. La IA como herramienta del equipo que transforma solo exige reglas de uso y datos autorizados". Y redactar el nivel 2 de conocimiento sin nombrar piezas del método ("se sabe por escrito qué conocimiento crítico está en una sola persona").

### P14. Los asistentes obligados a una puerta superan el límite que el método da para decidir

- Dónde: `06b`, Módulo 5, "Señales de que va mal"; más las fuentes de H2.
- Cita: "Las decisiones se toman en reuniones con más de diez personas".
- Problema: sumando a quienes el texto sienta en una puerta de diseño o de piloto: patrocinador, dirección del programa, medición, un mando intermedio, al menos una persona que hace el trabajo, quien defiende a quien recibe el servicio, la segunda línea (riesgos, seguridad, protección de datos, cumplimiento: hasta cuatro), la persona de la función afectada y el dueño que propone. Son entre nueve y trece. Es una inferencia, porque la composición no está definida (H2), pero con la lectura natural el método incumple su propia señal de fallo.
- Gravedad: media.
- Corrección: la tabla de composición de H2, distinguiendo "deciden" (tres o cuatro) de "son oídos antes por escrito".

### P15. Medir a las personas choca con no evaluarlas ni vigilarlas

- Dónde: `06g`, Módulo 24, "Supervisión que supervise"; `06b`, Módulo 6, pregunta abierta final; `03-tronco.md`, cap. 9; `06e`, Módulo 18.
- Cita: "dos medidas de la propia supervisión: cuántas veces la persona corrige o anula, y cuánto tarda en revisar". "registrar quién ha enseñado al sistema y reconocerlo en la evaluación". "el mapa no se usará para evaluar". "Separar asistir de vigilar".
- Problema: el método pide medir por persona cuánto corrige, cuánto tarda en revisar, cómo resuelve casos sin asistencia y quién enseñó al sistema, y llevar parte de eso a la evaluación. A la vez promete que el mapa no evalúa y pide separar asistir de vigilar. Esas medidas son, en la práctica, un sistema que mide a quien trabaja, justo lo que el módulo 18 dice que hay que declarar a la representación legal. No se dice si son individuales o agregadas.
- Gravedad: media.
- Corrección: añadir en el módulo 24 y en "Medición": "Las medidas de supervisión y de capacidad se leen agregadas por equipo. Cualquier lectura individual se pacta antes con el equipo y con la representación legal y se anota como vigilancia en el inventario".

### P16. Retirar es "barato" y a la vez pasa por más trámites que entrar

- Dónde: `03-tronco.md`, cap. 8; `06d`, Módulo 14; `05-orden.md`, tabla "Quién decide qué" y "La marcha atrás".
- Cita: "Retirar una iniciativa en la puerta del piloto es barato". "Una iniciativa que sale pasa por las cinco preguntas". "Comité de puertas, con la firma de alguien sin interés en ella". "bajar de nivel sin que nadie tenga que justificar un fracaso".
- Problema: para retirar hacen falta las cinco preguntas, el comité y una firma independiente; para bajar de nivel, propuesta del dueño y comité. Eso encarece justo lo que el método quiere abaratar, y contradice "sin que nadie tenga que justificar".
- Gravedad: media.
- Corrección: una frase: "Retirar en la puerta del piloto solo exige anotar qué pasa con las filas del mapa y con las personas (preguntas 3 y 4). Las cinco preguntas completas se piden para retirar algo que ya está en escala o en sostenimiento".

### P17. "Más allá de la primera puerta no se promete nada" choca con el modelo económico y con la contratación

- Dónde: `05-orden.md`, "Un arranque a cien días" y "Modelo económico"; `06d`, Módulo 13.
- Cita: "Más allá de la primera puerta no se promete nada". "Presupuesto por fases, reparto pactado de las ganancias e hitos de recuperación". "*Señal de fallo:* cada revisión trimestral reabre la financiación".
- Problema: una dirección financiera o una intervención no aprueban un programa sin horizonte, y el propio método considera fallo que la financiación se reabra cada trimestre. No se explica cómo se concilia un compromiso solo hasta la siguiente puerta con un presupuesto por fases y, en lo público, con un expediente de gasto plurianual.
- Gravedad: media.
- Corrección: añadir: "Se compromete el resultado de la siguiente puerta y se reserva, sin comprometer resultados, una horquilla de presupuesto para las fases siguientes, que cada puerta libera o devuelve".

### P18. El consentimiento del mapa puede bloquear la puerta y no se dice qué pasa entonces

- Dónde: `03-tronco.md`, cap. 9, "El límite del mapa" y regla "sin mapa no hay puerta".
- Cita: "se construye con su consentimiento". "sin mapa no hay puerta".
- Problema: si la persona que concentra las filas críticas no consiente, o el patrocinador no firma el compromiso ("el mapa no se hace"), la puerta del diagnóstico no se puede pasar nunca. El recuadro trata la prisa, no la negativa. Se da a una persona un veto sobre el programa sin decirlo.
- Gravedad: media.
- Corrección: añadir: "Si alguien no consiente, su parte del mapa se anota como 'conocimiento no descrito, concentrado en una persona' y la puerta lo trata como riesgo alto en la pregunta 3; el mapa se da por hecho con esa fila".

### P19. La regla "nada entra sin puerta" y "lo que no está en el inventario no está aprobado" no encajan con el laboratorio ni con el uso informal

- Dónde: `05-orden.md`, "Un inventario único" y "El uso informal"; `06g`, Módulo 23.
- Cita: "Lo que no está en el inventario no está aprobado". "El laboratorio trabaja con herramientas y datos autorizados, en un entorno separado del servicio". "quien cuenta un uso no autorizado para que se evalúe no es sancionado".
- Problema: no se dice si los experimentos del laboratorio y los usos informales confesados están en el inventario, ni qué pasa con un uso informal entre que se cuenta y se evalúa (¿se sigue usando, se para?). Tampoco cómo prueba el laboratorio algo útil sin datos reales del servicio.
- Gravedad: baja.
- Corrección: añadir al inventario un campo "Estado: en evaluación, en experimento, aprobado, retirado" y la frase "Un uso contado puede seguir en estado 'en evaluación' con las reglas generales de datos hasta que haya respuesta".

---

## Bloque 4. Afirmaciones más fuertes que su respaldo

### F1. El documento habla como si el método se hubiera aplicado, y su propio registro dice que tiene seis semanas

- Dónde: `01-por-que.md`, "Cómo leer este documento"; `07-mejora.md`, cap. 19; `03-tronco.md`, cap. 9; `08-anexos.md`, anexo F.
- Cita: "Donde tengo una herramienta que he visto funcionar, la explico". "Cada trimestre reviso no solo si las piezas funcionan". "Entre los dos suelen dibujar casi todo el mapa". "El mapa funciona en los comités por eso". Anexo F: "0.1 | Octubre de 2026"; "1.0 | 6 de noviembre de 2026"; versiones 1.0 a 1.3 el mismo día; "1.7 | 17 de noviembre de 2026".
- Problema: el método tiene unas seis semanas y ocho versiones, cuatro de ellas en un día. No puede haberse revisado "cada trimestre", ni una pieza haberse retirado "si en dos programas seguidos no aporta". El cap. 20 admite que no hay ningún programa aplicado ("La única forma de responderla es aplicar el método"). Sin embargo varias frases describen cómo "suele" comportarse el mapa. El lector no puede distinguir qué viene de treinta años de oficio con herramientas parecidas y qué es diseño nuevo sin probar, que es lo que el propio "Cómo leer" promete marcar.
- Gravedad: alta.
- Corrección: añadir al anexo F o al cap. 19 una tabla "Estado de cada pieza" con tres valores: usada por el autor en programas reales antes de Synergós, propuesta sin probar, tomada de una fuente. Cambiar "Cada trimestre reviso" por "Cada trimestre revisaré". Decir en "Cómo leer" que a la fecha ningún programa ha aplicado el método completo.

### F2. La tabla de causas se presenta como documentada "con bastante solidez" y varias filas dicen más que sus fuentes

- Dónde: `01-por-que.md`, cap. 2, tabla; `08-anexos.md`, anexo E.
- Cita: "Lo que sí está documentado, y con bastante solidez, son los motivos por los que las transformaciones se atascan". Filas: "Se sustituye a quien sabía sin haberlo mirado | Polanyi 1966; casos Klarna y Commonwealth Bank 2025". "Los costes llegan antes que los beneficios y el programa se cancela en el valle | Brynjolfsson, Rock y Syverson 2021". "La gente no cambia porque sus incentivos siguen igual o equivocarse sale caro | Edmondson 2018". Anexo E sobre Polanyi: "No habla de organizaciones ni de tecnología". Sobre Goodhart: "referida a la política monetaria".
- Problema: la columna "Quién la documenta" atribuye a las fuentes causas de fracaso de transformaciones que, según el propio anexo, no estudian: Polanyi no habla de organizaciones; Goodhart habla de política monetaria; la curva J describe productividad medida y no cancelaciones de programas; Edmondson estudia la seguridad psicológica y no los incentivos; varias filas se apoyan en libros de práctica (Kotter, Ries, Rumelt, Westerman, Christensen), que son experiencia y no medición. El capítulo empieza desmontando la cifra del setenta por ciento por falta de base y luego pide para su tabla una solidez del mismo tipo. Además ninguna fuente respalda la tercera columna: que la pieza de Synergós resuelva la causa.
- Gravedad: alta.
- Corrección: cambiar la frase por "Lo que sí está descrito, con distinto grado de solidez". Añadir a la tabla una columna "Tipo de respaldo" (estudio empírico, libro de práctica, caso, concepto trasladado por analogía). Y una línea bajo la tabla: "La tercera columna es diseño del autor; ninguna fuente prueba que la pieza resuelva la causa".

### F3. El método incumple su propio control de entrada de piezas

- Dónde: `01-por-que.md`, cap. 2; `07-mejora.md`, "Las reglas para cambiar el método"; `08-anexos.md`, anexo E, bloques de las versiones 1.1, 1.2, 1.5 y 1.7.
- Cita: "Quien proponga añadir una pieza al método tiene que decir a qué causa responde". "Una pieza nueva entra solo si responde a una causa documentada y tiene una fuente fichada". "Verificadas por conocimiento general de la literatura; pendientes de ficha propia en el cuaderno antes de citarlas en público". "Los temarios se usaron como lista de comprobación de lo que el método no cubría".
- Problema: la tabla de causas tiene trece filas y no se ha ampliado, pero han entrado veinticuatro módulos y, en la 1.7, doce propuestas. Varios módulos no responden a ninguna de las trece causas (huella material, inclusión, innovar con IA, agentes). Las fuentes de los módulos están, según el anexo, sin fichar. Y la 1.7 declara que creció comparándose con temarios de programas para directivos y publicaciones de LinkedIn, que es crecer por acumulación, lo que el control dice evitar ("Así se evita que el método engorde"). Un crítico solo necesita citar las dos frases juntas.
- Gravedad: alta.
- Corrección: añadir a la tabla del final del módulo 14 (o a una nueva) una columna "Causa de la tabla del cap. 2 a la que responde" para los veinticuatro módulos, y ampliar la tabla de causas con las que falten, con su fuente. Los módulos que no puedan rellenarla se marcan como "extensión sin causa documentada".

### F4. "Evidencia económica de veinticinco años" no sostiene la promesa tal como está formulada

- Dónde: `06c`, Módulo 9, "Lo que dicen las fuentes".
- Cita: "la tecnología solo rinde cuando crece a la vez que las personas y el conocimiento. Es la promesa de Synergós, sostenida por evidencia económica de veinticinco años, no por una intuición". "es la base empírica más sólida de Synergós".
- Problema: los tres estudios citados encuentran que la tecnología de la información rinde más en empresas con ciertas prácticas de organización y de gestión de personas. Son correlaciones a nivel de empresa, anteriores a la IA generativa, y no miden el "conocimiento" como tercer elemento ni nada parecido al mapa. De "son complementarios" a "solo rinde cuando crecen a la vez los tres" hay un salto. El anexo E lista las tres fuentes como "pendientes de ficha propia". Y el cap. 19 admite que el supuesto central "es también el que más necesita evidencia", lo contrario de "sostenida por evidencia".
- Gravedad: alta.
- Corrección: sustituir por: "La evidencia económica de veinticinco años apoya la mitad de la promesa: la tecnología rinde más cuando cambia a la vez la organización del trabajo. Que el conocimiento no escrito sea el tercer factor es la hipótesis de Synergós".

### F5. De Klarna y Commonwealth Bank se afirma una causa que el anexo no recoge

- Dónde: `05-orden.md`, "La marcha atrás como opción legítima"; `01-por-que.md`, tabla del cap. 2; `08-anexos.md`, anexo E.
- Cita: "En ninguno de los dos casos falló la tecnología. Falló la medición de lo que hacían las personas, que se descubrió cuando ya no estaban". Anexo: "admitió que se habían fijado demasiado en el coste y que la calidad había bajado". "No se ha confirmado si el bot sigue en uso". "(no fueron setecientos despidos)".
- Problema: lo que el anexo documenta es que en Klarna bajó la calidad del servicio que daba el asistente (eso es, como mínimo, un fallo del conjunto con la tecnología dentro) y que en el banco hubo una disputa sobre si las llamadas bajaban. Ninguna de las dos fichas dice que la causa fuera no haber medido lo que hacían las personas, ni conocimiento tácito. En Klarna buena parte eran agentes externos, así que "cuando ya no estaban" tampoco se ajusta. Son los dos únicos casos reales del documento y sostienen la fila más propia de la tabla.
- Gravedad: media.
- Corrección: cambiar por: "En los dos casos la decisión se tomó mirando el coste o el volumen, y hubo que rectificar. Mi lectura, que las fuentes no confirman, es que no se midió lo que hacían las personas".

### F6. Una empresa observada se convierte en "organizaciones que ya trabajan con IA"

- Dónde: `06c`, Módulo 9, "El tiempo no se libera solo"; `08-anexos.md`, anexo E, Ranganathan y Ye (2026).
- Cita: "Lo que se ha observado en organizaciones que ya trabajan con IA es que la carga tiende a subir". Anexo: "Una empresa tecnológica observada durante meses. Conocido por resúmenes; autoría por confirmar".
- Problema: el texto generaliza en plural y sin citar; el anexo dice que es una empresa, conocida por resúmenes y con la autoría sin confirmar. De ahí sale una comprobación obligatoria nueva.
- Gravedad: media.
- Corrección: cambiar por: "En una empresa tecnológica observada durante meses (Ranganathan y Ye, 2026, que conozco por resúmenes), la carga subió". Mantener la comprobación como propuesta.

### F7. Los casos compuestos aportan cifras que se usan como dato

- Dónde: `03-tronco.md`, cap. 9; `06a`, Módulo 2, "Un caso compuesto".
- Cita: "El mapa da diecinueve filas, cinco de ellas concentradas en una sola persona [...] Mismo presupuesto, misma tecnología, resultado opuesto. El coste del mapa en ese caso: dos semanas de una persona y unas veinte conversaciones". "la productividad subió las dos primeras semanas y luego se estancó".
- Problema: un caso compuesto no tiene resultado ni coste: son construidos. "Resultado opuesto" afirma un desenlace que no ocurrió en ningún sitio, y el coste del mapa es el único dato de esfuerzo de todo el documento. Un lector lo tomará como referencia para presupuestar.
- Gravedad: media.
- Corrección: añadir tras cada cifra "(cifra ilustrativa, no medida)" y cambiar "resultado opuesto" por "resultado previsto opuesto en la tercera pregunta del mapa".

### F8. El estudio sobre empleo joven se presenta como descriptivo y se usa como prueba

- Dónde: `04-elementos.md`, cap. 15, "Quién enseña lo que la tarea enseñaba"; `06b`, Módulo 7.
- Cita: "está claramente por debajo de lo que habría estado sin ella". "Son datos descriptivos, no prueban la causa y son de otro país, pero la señal es clara". "es la primera señal de que esto ya está pasando". "dentro de diez años no habrá expertos". Anexo: "Descriptivo, no causal [...] Verificada por fuentes secundarias".
- Problema: "lo que habría estado sin ella" es lenguaje causal para un dato que el propio texto llama descriptivo. El estudio habla de menos contratación; no dice nada de que las tareas de entrada formaran a los nuevos ni de que falten expertos en diez años. Esa cadena es del autor, y sobre ella se monta la cuarta pregunta de la puerta. La fuente, además, no se ha leído en original.
- Gravedad: media.
- Corrección: cambiar "por debajo de lo que habría estado sin ella" por "por debajo del de otros grupos de edad y de ocupaciones menos expuestas", y "es la primera señal de que esto ya está pasando" por "es compatible con esta hipótesis, sin probarla".

### F9. La curva J se traslada del nivel de economía y empresa al de un piloto

- Dónde: `05-orden.md`, "Modelo económico"; `06d`, Módulo 12; `06e`, Módulo 17.
- Cita: "Muchos programas se cancelan en ese valle, justo antes de dar resultado". "dice cuánto dura el valle esperado, cuánto cuesta". "La curva J tiene una duración. El plan la incluye".
- Problema: el anexo solo dice "La curva J". El trabajo citado explica un efecto de medición de la productividad cuando hay inversión que la contabilidad no ve; no da la forma ni la duración del valle de un programa concreto ni dice que muchos se cancelen ahí. El método exige escribir cuánto dura el valle sin dar forma de estimarlo, y la frase de las cancelaciones no tiene fuente.
- Gravedad: media.
- Corrección: añadir: "La fuente describe el efecto a nivel de empresa y de economía; aplicarlo a un programa es una analogía mía. La duración del valle se estima con la clase de referencia del módulo 17 y, si no hay, se declara como supuesto". Marcar la frase de las cancelaciones como experiencia del autor.

### F10. Las consultoras "no se usan en el método" y sí se usan

- Dónde: `08-anexos.md`, anexo E, "Revisadas y no citadas"; `06g`, Módulo 24, "Lo que dicen las fuentes"; `04-elementos.md`, cap. 17, "Para qué: el objetivo".
- Cita: "**Revisadas y no citadas:** McKinsey, BCG, Deloitte y Accenture [...] Se usan como contexto en el cuaderno, no en el método". "McKinsey publicó en 2025 las lecciones de un año de despliegues de agentes. Las que más pesan aquí". "sus propias encuestas reconocen que hoy la mayoría de las organizaciones solo obtiene productividad".
- Problema: el anexo dice dos cosas incompatibles sobre la misma firma, y el cap. 17 apoya un argumento en encuestas de consultora sin decir cuál. El informe de McKinsey se conoce "por resúmenes" y aun así se dice cuáles de sus lecciones "pesan".
- Gravedad: media.
- Corrección: cambiar la nota del anexo a "Sus encuestas con cifras no se citan. Se cita un texto de práctica de McKinsey (2025) como lista de comprobación". En el cap. 17, nombrar la encuesta o quitar la frase.

### F11. La regla "primero las personas, después la IA" se presenta como mostrada por un estudio que no la estudia

- Dónde: `06g`, Módulo 23, "Lo que pide el método"; `08-anexos.md`, anexo E, Doshi y Hauser.
- Cita: "El orden importa por lo que mostraron Doshi y Hauser". "la IA ayuda a quien tiene una idea y empobrece el abanico si todo el mundo parte de ella". Anexo: "Hecho con relatos breves; el método lo extiende por analogía a las sesiones de ideas, y eso es una inferencia propia".
- Problema: el anexo lo dice bien y el texto no: el estudio no prueba que escribir primero sin IA conserve la variedad, ni trata de sesiones de ideas en organizaciones.
- Gravedad: media.
- Corrección: cambiar por: "El orden es una precaución mía a partir de Doshi y Hauser, que trabajaron con relatos breves y no probaron este orden".

### F12. Las fechas regulatorias se dan como hecho en un sitio, como duda en otro, y la revisión legal "se dejó fuera"

- Dónde: `04-elementos.md`, cap. 17, "El entorno que exige la IA"; `06c`, Módulo 11, "Las referencias"; `06e`, Módulo 18; `08-anexos.md`, anexo E.
- Cita: Cap. 17: "con fechas que se han discutido y que pueden haberse ajustado". Módulo 11: "El Reglamento (UE) 2026/1744, el llamado ómnibus digital, en vigor desde el 27 de julio de 2026, retrasó las de alto riesgo: al 2 de diciembre de 2027". Anexo: "La parte legal de la revisión (calendarios y normas) se dejó fuera".
- Problema: el cap. 17 no se actualizó y contradice en tono al módulo 11. El documento no indica con qué fuente primaria se comprobó el reglamento de 2026 ni sus fechas; yo no he podido verificarlo en esta auditoría y no afirmo que sea incorrecto. En el anexo aparece además una directiva (2024/2831, trabajo en plataformas) que el texto no cita en ningún sitio (comprobado). Para un cliente público, una fecha legal errónea en el método es un riesgo de credibilidad.
- Gravedad: media.
- Corrección: alinear el cap. 17 con el módulo 11, y añadir a la ficha del anexo la referencia del Diario Oficial y la fecha en que se consultó. Quitar del anexo la norma que no se cita o citarla donde corresponda.

### F13. Superlativos y frecuencias sin fuente

- Dónde: `04-elementos.md`, cap. 15, "Liderazgo"; `06c`, Módulo 8; `06a`, Módulo 3; `03-tronco.md`, cap. 9.
- Cita: "Treinta años después siguen siendo las que más se incumplen". "Es la causa de fracaso de la tabla del capítulo 2 que más se repite en la práctica". "Es un argumento a favor de la IA [...] que es más sólido que el ahorro de tiempo". "El diagnóstico es la fase más importante y la que más se salta".
- Problema: son afirmaciones de frecuencia o de comparación sin dato. El cap. 2 pide que "cualquiera que dé una cifra exacta" explique cómo la midió; "la que más" es una cifra implícita.
- Gravedad: baja.
- Corrección: anteponer "en mi experiencia" a cada una.

### F14. La frontera de un experimento de 2023 se convierte en la clasificación general de tareas

- Dónde: `04-elementos.md`, cap. 17, "La frontera"; `06a`, Módulo 2.
- Cita: "lo empeoraba, porque los consultores confiaban en ella donde no debían". "Synergós usa esa idea para clasificar cada tarea en cuatro categorías". "el estudio de la frontera dentada de 2023 mostró el primero con claridad".
- Problema: es un experimento con consultores de una firma y con un modelo de 2023. El propio cap. 17 dice que la IA "cambia en meses, no en años", así que la frontera de cada tarea se mueve con cada versión de modelo, y no se dice cada cuánto hay que reclasificar. La explicación causal ("porque confiaban") y el vínculo con el sesgo de automatización son lectura del autor; el anexo solo recoge "La frontera dentada; centauros y cíborgs".
- Gravedad: baja.
- Corrección: añadir: "La clasificación de cada tarea se revisa con los casos de prueba cada vez que cambia el modelo". Y "según interpretan los autores" tras la explicación causal, si es así, o "a mi juicio".

### F15. El anexo E no cumple lo que "Cómo leer" promete de él

- Dónde: `01-por-que.md`, "Cómo leer este documento"; `08-anexos.md`, anexo E; `03-tronco.md`, cap. 8.
- Cita: "todo lo que cito está en la lista de fuentes del final, con lo que cada autor dice y, sobre todo, con lo que no dice". "Es el ciclo de mejora de Deming llevado a escala de programa".
- Problema: de unas 107 entradas con año en el anexo, unas 23 llevan alguna nota de límite; el resto solo dice qué aportan. Deming se cita en el cap. 8 y no está en el anexo (comprobado: una sola aparición en todo el documento). Hay entradas del anexo que el texto no cita (Gillespie y otros, Iansiti y Lakhani, PwC, World Economic Forum). Once entradas se declaran conocidas solo por resúmenes o fuentes secundarias.
- Gravedad: baja.
- Corrección: cambiar la frase por "con lo que cada autor aporta y, en las que más pesan, con lo que no dice". Añadir Deming o quitar la mención. Mover las no citadas a un apartado "Leídas, no usadas".

---

## Bloque 5. Lo más débil si un crítico quisiera desmontarlo

1. **No se ha aplicado nunca y habla a ratos como si sí.** El registro de versiones muestra ocho versiones en seis semanas, cuatro en un día, y el cap. 20 reconoce que no hay ningún programa hecho con el método. Los dos únicos casos reales cuentan fracasos ajenos y los demás son compuestos con cifras inventadas a propósito. Sin embargo el texto dice "he visto funcionar", "suelen", "cada trimestre reviso". Un crítico empezará por ahí (F1, F7, F5).

2. **La promesa no se puede comprobar con las herramientas del método.** "Crecer a la vez" se verifica con tres indicadores y el delta. El indicador de personas no tiene medida, el delta depende de un objetivo que nadie regula y no sirve para indicadores que solo deben conservarse, los umbrales no tienen forma de fijarse, y el criterio tipo de puerta contradice la curva J. En la práctica, cada puerta se decide a juicio y el número lo acompaña (P1, P2, P3, P4, H4, H7).

3. **Pesa demasiado y no tiene núcleo.** Unas 44 piezas escritas antes de un piloto, una "página" de decisión con al menos 24 líneas, más de diecinueve papeles además de las siete funciones, diecisiete revisiones periódicas y más de veinte indicadores, para un programa que el propio texto sitúa en "un equipo". No hay versión mínima ni regla para quitar piezas. Contradice sus principios 3 y 6 y la medida justa (P5, H1, P10, P14).

4. **La base de evidencia es más débil de lo que el texto dice, y el método ha crecido en contra de su propio control.** La tabla de causas se declara sólida y se apoya en parte en libros de práctica y en conceptos trasladados desde otros campos. La mayoría de las fuentes de los módulos están, según el anexo, sin fichar o leídas por resúmenes. La frase "evidencia económica de veinticinco años" cubre solo media promesa. Y la versión 1.7 creció comparándose con temarios y publicaciones de LinkedIn, sin ampliar la tabla de causas (F2, F3, F4, F6, F10).

5. **Los conceptos centrales no están cerrados, así que dos personas aplicarán dos métodos distintos.** Ciclo significa tres cosas; no se sabe si el tronco lo recorre el programa o la iniciativa; elemento y acelerador se solapan y la regla de entrada tiene tres redacciones; acelerar, automatizar y aumentar se cruzan en los propios ejemplos; puerta y dueño tienen varios sentidos; la escala de madurez mide cuánto Synergós se ha aplicado; el comité que decide casi todo no está definido. Para un método que se vende por su orden, es el flanco más fácil (A1, A2, A3, A4, A5, A6, H2, P13).

Fuera de los cinco, pero decisivo para la mitad del público objetivo: la adaptación a la administración pública se limita a la contratación, y la regla de partida del nivel 3 para decisiones sobre derechos puede llevar a un cliente público a decidir de forma solo automática (H6, P7).

---

## Lo que he comprobado y sale bien

- Aritmética del ejemplo del delta: (10 - 7) / (10 - 4) = 50 %. Correcta.
- Ejemplo de volumen o conversión: 2 de 10 y 20 de 100 son el 20 % los dos; 5 de 10 es el 50 %. Correcto.
- Recuentos internos que cuadran: siete aportaciones, siete criterios de la matriz, cinco formas de interacción, siete funciones, cinco preguntas de las grietas, treinta y cuatro fuentes de la versión 1.1, veinticuatro módulos, once campos de la ficha.
- El documento ya reconoce, fuera de los recuadros, varias debilidades que aquí aparecen (evidencia anecdótica, peso para organizaciones pequeñas, dependencia del patrocinador, riesgo de burocracia). No las he contado como hallazgo por sí mismas; sí cuando el reconocimiento no viene con una regla que permita aplicar el método.

## Lo que no he hecho

- No he contrastado las fuentes con sus originales ni el calendario regulatorio de 2026 con el Diario Oficial.
- No he revisado el .docx generado, las figuras ni el cuaderno de estudios al que remite el anexo E.
