# Synergós: estructura del método

**Versión 0.2 (31 oct 2026), validada por Alejandro el mismo día.** Alejandro compartió en la conversación el documento base (su método de transformación acelerada por IA, escrito en su tiempo y con medios propios, ver `09-propiedad.md`). Esta versión reorganiza esa arquitectura en clave Synergós. El documento base no se copia en el repositorio ni se cita en público; aquí queda su estructura traducida, sin referencias a ningún empleador, estudio interno ni cliente. Lo que Synergós cambia respecto al documento base está marcado así: **[cambio]**.

---

## 1. La promesa

**Crecer a la vez.** Una transformación sale bien cuando las personas, el conocimiento y la tecnología avanzan en el mismo orden y ninguna crece a costa de las otras. Cuando la tecnología va dos años por delante no es una transformación rápida: es una transformación rota que todavía no lo sabe.

Synergós es un método para dirigir cualquier programa de transformación, de un servicio, de un área o de una organización entera. Tiene un tronco (cinco fases con entregables y puertas), tres elementos que crecen a la vez y un conjunto de aceleradores, entre los que la IA pesa más que los demás. Cada pieza existe porque responde a una causa documentada de fracaso; si una pieza no responde a ninguna, sobra.

## 2. Por qué un método: las causas del fracaso y qué pieza responde a cada una

La cifra de que el 70 % de las transformaciones fracasan no tiene base empírica (Hughes, 2011). Lo que sí está documentado son los motivos por los que se atascan.

| Causa | Quién la documenta | Pieza de Synergós que responde |
|---|---|---|
| Se elige la solución antes de entender el problema | Rumelt 2011 | Fase 1, diagnóstico; su puerta exige nombrar la restricción |
| La tecnología llega antes que el cambio en la forma de trabajar | Westerman, Bonnet y McAfee 2014; Trist y Bamforth 1951 | Regla "elemento antes que acelerador"; fase 2 rediseña el trabajo antes de elegir la herramienta |
| Se sustituye a quien sabía sin haberlo mirado | Polanyi 1966; casos Klarna y Commonwealth Bank 2025 | **[cambio]** El mapa de lo que nadie escribió, entregable de la fase 1; pregunta 3 de la puerta |
| Los pilotos de IA no llegan al proceso real | MIT NANDA 2025; Whitelane 2025 (ambas por verificar en primaria) | La IA se planifica en todas las fases, cada caso nace de la restricción y la autonomía sube por puertas |
| Falta urgencia y una coalición con poder real | Kotter 1995 | Liderazgo: obligaciones explícitas del patrocinador |
| Se escala lo que nadie ha probado | Ries 2011; Cooper 1990 | Fase 3, piloto con criterios fijados antes y puerta que decide |
| Se mide tarde o se mide lo que no importa | Forsgren, Humble y Kim 2018; ley de Goodhart | Línea base en el diagnóstico; indicadores de resultado, en pareja; el delta |
| Los costes llegan antes que los beneficios y el programa se cancela en el valle | Brynjolfsson, Rock y Syverson 2021 (curva J) | Modelo económico pactado antes de invertir, que prevé el valle |
| La gente no cambia porque sus incentivos siguen igual o equivocarse sale caro | Edmondson 2018 | Personas: roles, carreras e incentivos rediseñados; espacio para fallar en el piloto |
| Se corrigen errores sin cuestionar los supuestos | Argyris y Schön 1978 | Supervisión de doble bucle, con calendario |
| Se diseña de espaldas a quien usa el servicio | Von Hippel 2005; Christensen 2016 | Interacción: visitas al puesto, cocreación, canal de propuestas |
| Se declara la victoria demasiado pronto | Kotter 1995 | Fase 5, sostenimiento, con dueño y presupuesto propios |
| La balanza está inclinada hacia sustituir en vez de ampliar | Brynjolfsson 2022 (trampa de Turing); Zuboff 1988 | **[cambio]** Pregunta 2 de la puerta: ¿automatiza o informa? |

La tabla también sirve de control: quien proponga añadir una pieza tiene que decir a qué causa responde.

## 3. Arquitectura

El documento base separaba tres capas: el tronco (fases), los habilitadores (condiciones sin las que ninguna fase avanza: estrategia, gobierno, liderazgo, personas y cambio, modelo económico) y los aceleradores (lo que hace que una fase vaya más rápido o llegue más lejos: IA, tecnologías, datos y conocimiento, medición, supervisión, interacción).

**[cambio] Synergós conserva el tronco y reordena lo demás alrededor de los tres elementos.** Personas deja de ser un habilitador entre cinco y conocimiento deja de ser un acelerador entre seis: pasan a ser ejes al mismo nivel que la tecnología. Las condiciones de gobierno, estrategia y modelo económico, junto con la medición, pasan a formar el cuarto componente, el orden, que es lo que hace que los tres crezcan a la vez.

| Componente | Qué agrupa | De dónde viene en el documento base |
|---|---|---|
| **Personas** | Liderazgo; personas y cambio (roles, carreras, incentivos, seguridad psicológica); interacción con quien hace el trabajo y con quien recibe el servicio | Habilitadores liderazgo y personas y cambio; acelerador interacción |
| **Conocimiento** | El explícito (datos con dueño, base curada, registro de decisiones) y el tácito (el mapa de lo que nadie escribió); el aprendizaje del propio programa (supervisión de doble bucle) | Acelerador datos y conocimiento; acelerador supervisión; **[cambio]** mapa tácito nuevo |
| **Tecnología** | La IA en sus dos papeles (para transformar y dentro del servicio), la frontera, la escala de autonomía, el entorno que exige; las demás tecnologías (plataforma, automatización, entrega continua); el radar de lo emergente | Aceleradores IA y tecnologías; sección 7 |
| **El orden (crecer a la vez)** | Las cinco fases y sus puertas; estrategia; gobierno; modelo económico; medición y el delta; la escala de madurez y la regla de entrada; el dimensionamiento del programa | Tronco; habilitadores estrategia, gobierno y modelo económico; acelerador medición; secciones 8 y 9 |

La regla que protege la arquitectura no cambia: no se compra un acelerador para tapar un elemento que falta. Un agente de IA que resuelve consultas acelera la escala, pero si nadie ha decidido quién responde de sus errores ni cómo cambia el trabajo de los técnicos, se queda en piloto; el fallo está en personas y en gobierno, y ninguna mejora del agente lo resuelve.

### Principios

1. **Diagnóstico antes que solución.** Nada entra en diseño sin una restricción nombrada y una línea base medida.
2. **Elemento antes que acelerador.** **[cambio, antes "habilitador antes que acelerador"]** Un acelerador entra en una fase solo si los tres elementos están, para esa fase, al menos en nivel 2 de madurez.
3. **Pocas cosas a la vez.** La IA se planifica en todas las fases; además, uno o dos aceleradores por fase, los que atacan la restricción (Goldratt 1984).
4. **Puertas con criterios fijados antes.** Se escriben al empezar la fase, no al terminarla.
5. **Nada nuevo encima de lo no mirado.** **[cambio]** La regla del girasol: cada iniciativa se coloca donde no haga sombra a las personas ni a lo que ya funcionaba (Vogel 1979; Douady y Couder 1992).
6. **El método se supervisa a sí mismo.** Si una pieza no aporta en un programa, se retira de ese programa.

## 4. El tronco: cinco fases con puertas

Un programa grande tiene varios ciclos en paralelo, cada uno en su fase; lo aprendido en el sostenimiento de uno alimenta el diagnóstico del siguiente (ciclo de Deming a escala de programa). Cada puerta tiene tres salidas: pasar, ajustar y repetir, o retirar. Retirar en la puerta del piloto es barato y es buena noticia.

| Fase | Para qué | Entregables | Puerta: qué tiene que ser cierto | Error típico |
|---|---|---|---|---|
| 1. Diagnóstico | Entender dónde se pierden tiempo, calidad o dinero, y por qué | Mapa del flujo de trabajo real, restricción principal, línea base, mapa de actores, madurez de los tres elementos, **[cambio] mapa de lo que nadie escribió** | La restricción está nombrada y aceptada por el patrocinador; la línea base está medida, no estimada; **[cambio] el mapa tácito existe** | Un inventario de problemas sin jerarquía |
| 2. Diseño | Decidir qué se cambia, cómo y con qué aceleradores | Cartera priorizada, nuevo diseño del trabajo, aceleradores por fase, criterios del piloto, modelo económico pactado, **[cambio] decisión escrita con las cinco preguntas de la puerta por opción** | Cada iniciativa ataca la restricción o tiene motivo escrito; criterios del piloto firmados; **[cambio] cada opción dice qué le pasa al conocimiento y si automatiza o informa** | Diseñar la herramienta y dejar el trabajo como estaba |
| 3. Piloto | Probar en pequeño con gente y datos reales | Resultados contra la línea base, lecciones, ajustes, riesgos | Cumple sus criterios, o la puerta decide ajustar, repetir o retirar | Elegir el entorno más fácil, que no representa al resto |
| 4. Escala | Extender lo que funciona | Despliegue por etapas, formación, roles e incentivos, procedimientos | Los indicadores aguantan al ampliar y los elementos aguantan la carga | Escalar la herramienta sin escalar roles e incentivos |
| 5. Sostenimiento | Que la mejora siga cuando el equipo se vaya | Dueño operativo, presupuesto recurrente, cuadro en régimen, calendario de supervisión | El dueño acepta la responsabilidad y los indicadores aguantan dos ciclos sin el equipo | Cerrar sin dueño ni presupuesto |

### Las cinco preguntas de la puerta **[cambio]**

El documento base tenía una pregunta de puerta: ¿ataca la restricción? Synergós la mantiene y añade cuatro, porque es ahí donde los tres elementos se protegen:

1. ¿Ataca la restricción?
2. ¿Automatiza o informa a quien hace el trabajo? (Zuboff)
3. ¿Qué le pasa a cada fila del mapa de lo que nadie escribió: se queda en la persona y la tecnología la ayuda, pasa al sistema de forma revisable, o se pierde?
4. ¿Quién responde de los errores cuando el sistema se equivoque, y quién enseña lo que la tarea enseñaba?
5. ¿Hace crecer a la vez a los tres elementos, o abarata uno a costa de los otros?

Se puede aprobar una opción que pierde conocimiento. Lo que no se puede es aprobarla sin saberlo.

## 5. Los tres elementos, en detalle

### 5.1 Personas

Condición, no destinataria. Entran en el diagnóstico, no en la formación de cierre.

- **Liderazgo.** Patrocinador con tiempo asignado, coalición con poder real, comunicación continua, retirada de obstáculos (Kotter). Distinguir problemas técnicos, que se delegan, de problemas adaptativos, que obligan a cambiar hábitos y lealtades y no se pueden delegar (Heifetz y Linsky 2002). Casi todo lo difícil de una transformación es adaptativo. Señal de fallo: el patrocinador delega todas las conversaciones difíciles.
- **Personas y cambio.** Roles y carreras rediseñados, incentivos alineados con los indicadores del programa, formación en el puesto, espacio para fallar en el piloto (Edmondson 2018). Señal de fallo: uso alto de las herramientas nuevas y resultados iguales que antes.
- **Interacción.** Visitas al puesto donde se hace el trabajo, entrevistas sobre el trabajo que el cliente intenta resolver, canal permanente de propuestas con respuesta en plazo, cocreación por ciclo, grupo estable de usuarios avanzados (Von Hippel 2005; Christensen 2016). Señal de madurez: una parte relevante de la cartera nace de empleados y clientes.
- **[cambio] Quién enseña.** Si la tarea que desaparece era la que formaba a los nuevos, la puerta exige decidir quién enseña ahora lo que esa tarea enseñaba (Brynjolfsson, Chandar y Chen 2025).

### 5.2 Conocimiento

Tiene nombre propio porque vive en tres sitios: en las personas, en la organización y en la tecnología. Lo que decide una transformación es a dónde va.

- **El explícito.** Datos con dueño y calidad medida, base de conocimiento curada y versionada, registro de decisiones y de sus motivos, captura del conocimiento de quien se va (Nonaka y Takeuchi 1995). En madurez 4 lo consumen personas y agentes.
- **[cambio] El tácito: el mapa de lo que nadie escribió.** Dónde está, en quién, dónde se usa y cuán concentrado está. Se levanta con quien hace el trabajo y con quien acaba de llegar, preguntando por las grietas (qué parece igual y no lo es, cuándo no sigues el procedimiento, a quién llamas, qué sabes antes de leer, qué pasaría mañana si tú no vinieras). Tabla de cuatro columnas; la columna de concentración es la que asusta. Sin mapa no hay puerta.
- **El aprendizaje del programa: supervisión.** Bucle simple corrige el error; doble bucle revisa la regla que lo produjo (Argyris y Schön 1978). Revisión tras cada puerta con cuatro preguntas (qué esperábamos, qué pasó, por qué, qué cambiamos), retrospectiva por ciclo, análisis de incidentes sin culpables, revisión trimestral de supuestos.

### 5.3 Tecnología

La palanca. Hoy, sobre todo, la IA, que es el único acelerador que actúa en las cinco fases, cambia el trabajo del propio equipo que transforma, trae su propia regulación y cambia en meses.

- **Los dos papeles de la IA.** Para transformar (herramienta del equipo desde el primer día del diagnóstico: minería de procesos, análisis de documentación, síntesis de entrevistas, prototipos, medición automática; riesgo bajo, beneficio pronto) y dentro del servicio (asistentes y agentes en los procesos transformados, desde el piloto; mayor mejora y mayor riesgo).
- **La frontera.** Cada tarea se clasifica según dónde la IA ayuda y dónde empeora el resultado: delegar, centauro, cíborg, reservar (Dell'Acqua y otros 2023). Brynjolfsson, Li y Raymond 2023: la ayuda es mayor para quien empieza.
- **La escala de autonomía.** Cuatro niveles; cada subida se gana en una puerta con evaluaciones superadas. Protege lo que más cuesta recuperar: la confianza de quien trabaja y de quien recibe el servicio.
- **El entorno que exige.** Antes del primer piloto con IA hay que poder responder: quién decide y responde, con qué reglas se usa, quién sabe usarla. Gobierno de la IA integrado en el comité de puertas (no paralelo), inventario de sistemas y riesgos, gestión de riesgos alineada con el reglamento europeo de IA, uso seguro y acceso controlado, gobierno del dato, formación por perfil, comunidad de práctica. Necesario, no suficiente: dónde aplicar la IA lo decide el diagnóstico.
- **Las demás tecnologías.** Plataforma común antes que soluciones a medida, pruebas y despliegues automatizados, arquitectura modular, salida pactada con cada proveedor (Forsgren, Humble y Kim 2018; Ross, Beath y Mocker 2019).
- **El radar.** Lo emergente se revisa al cierre de cada ciclo y se clasifica en movimiento sin arrepentimiento, opción pequeña o apuesta que espera señal. Nada entra por fuera de las puertas.
- **La medida justa [cambio].** Cuánta IA necesita cada caso: la misma pregunta vale para no poner ninguna y para no poner de menos.

## 6. El orden: crecer a la vez

Es lo que hace que los tres elementos avancen en el mismo compás. Agrupa lo que en el documento base eran los habilitadores de dirección y la medición.

- **Estrategia.** Diagnóstico, política guía y acciones coherentes; elegir dónde jugar y cómo ganar (Rumelt 2011; Lafley y Martin 2013). Señal de fallo: la cartera crece sin que nadie retire nada.
- **Gobierno.** Comité de puertas con criterios previos, derechos de decisión escritos, registro de riesgos y decisiones (Weill y Ross 2004). Señal de fallo: las puertas se aprueban por calendario y no por evidencias.
- **Modelo económico.** Presupuesto por fases, reparto pactado de las ganancias, hitos de recuperación; prevé el valle de la curva J (Brynjolfsson, Rock y Syverson 2021). Señal de fallo: cada revisión trimestral reabre la financiación.
- **Medición y el delta.** Línea base antes de cambiar nada, pocos indicadores de resultado, en pareja (velocidad con calidad, coste con satisfacción), revisión mensual con el patrocinador (Hubbard 2007; ley de Goodhart). La mejora se expresa en una sola unidad, el delta: lo que ha avanzado un indicador desde su línea base hacia su objetivo, en porcentaje; el delta de un ciclo es la media ponderada de sus indicadores, con pesos pactados en el diseño; los criterios de puerta se escriben como delta mínimo. **[cambio] Tres indicadores, no uno:** al menos uno por elemento (personas: criterio, autonomía, rotación; conocimiento: concentración, lo que ha pasado al sistema y es revisable; tecnología: uso real, no demo). Si solo mejora el tercero, la transformación está rota.
- **Madurez y regla de entrada.** Escala de cuatro niveles (puntual, repetible, integrado, sistemático) para elementos y aceleradores, evaluada en el diagnóstico y revisada en cada puerta. Un acelerador se activa solo con sus condiciones en nivel 2 o más; la IA en piloto exige gobierno y personas en nivel 2.
- **Dimensionamiento.** Un programa acotado (un equipo, menos de seis meses): puertas del patrocinador con el responsable, un ciclo, la IA y un acelerador más. Un programa amplio (varias áreas, uno a tres años): comité de puertas, varios ciclos, la IA y hasta dos más por ciclo, revisión trimestral de supuestos, oficina pequeña de medición y conocimiento. Un programa en marcha no se reinicia: diagnóstico rápido, cada iniciativa se clasifica en mantener, acelerar, reorientar o retirar, y se instalan las puertas a partir de la siguiente fase.
- **La marcha atrás como opción legítima [cambio].** Un método serio la prevé antes y la hace barata.

## 7. Qué se publica y qué se guarda

Siguiendo `09-propiedad.md`: en LinkedIn se publica el porqué y el qué (esta arquitectura, las causas y sus respuestas, los tres elementos, las cinco preguntas, el delta como idea). Se guarda para el libro, el curso o la consultoría futura el cómo operativo: las fichas completas de cada acelerador, la escala de madurez detallada, las trece actuaciones del entorno de la IA, la herramienta de seguimiento, las plantillas de mapa y de puerta. El artículo "el método en una página" del final de la vuelta 3 será el índice, no el kit.

## 8. Mapa de la serie: qué casilla cubre cada artículo

| Casilla | Vuelta 1 (nov) | Vuelta 2 (dic) | Vuelta 3 (ene) | Vuelta 4 (feb) |
|---|---|---|---|---|
| Conocimiento | 2 nov. El mapa de lo que nadie escribió (5.2 tácito) | 30 nov. El conocimiento que vive en los equipos: Trist y Bamforth (5.2, causa 2) | El conocimiento que vive en la tecnología: qué tiene de nuevo la IA generativa (5.2, 5.3) | Aprender en doble bucle: la supervisión que revisa los supuestos (5.2) |
| Personas | 9 nov. Las personas no son la fase final: criterio de diseño desde el diagnóstico (5.1, fase 1) | 7 dic. Lo que preguntasteis: participar, liderar, el miedo (5.1 liderazgo, interacción, Edmondson) | Quién enseña lo que la tarea enseñaba (5.1, Canaries) | Problemas técnicos y adaptativos: lo que el patrocinador no puede delegar (5.1, Heifetz) |
| Tecnología | 16 nov. Automatiza o informa (puerta, pregunta 2) | 14 dic. De la demo al uso: los dos papeles de la IA y la escala de autonomía (5.3) | La medida justa y la frontera: delegar, centauro, cíborg, reservar (5.3) | El radar: incorporar lo nuevo sin perseguirlo (5.3) |
| El orden | 23 nov. Diagnóstico antes que solución: la restricción y la puerta (fase 1, 6 estrategia) | 21 dic. El orden importa: 137,5 grados, nada nuevo encima de lo no mirado (principio 5) | Medir el crecimiento, no la actividad: el delta y los tres indicadores (6) | El método en una página: las cinco fases, las cinco preguntas, el valle de la curva J (todo) |

Con cuatro vueltas queda descrito el método entero en público, al nivel de índice y porqué. Cada semana, los dos posts hijos y la pregunta de comunidad salen de la casilla del lunes.

## 9. Decisiones tomadas y pendientes

**Tomadas con el documento base a la vista (31 oct):**
- Las fases se llaman como en el documento base: diagnóstico, diseño, piloto, escala, sostenimiento. Se descarta la propuesta Mirar, Decidir, Hacer, Sostener.
- La pregunta "¿ataca la restricción?" se hereda tal cual, con Goldratt y Rumelt como fuentes.
- Los habilitadores y aceleradores del documento base se reparten entre los tres elementos y el orden según la tabla de la sección 3. Ninguno desaparece.
- La sección de la IA del documento base entra como núcleo del elemento tecnología (dos papeles, frontera, autonomía, entorno, radar).
- El delta se adopta como unidad de medida, con la regla nueva de un indicador por elemento como mínimo.

**Cerradas por Alejandro (31 oct 2026):**
1. La tabla de la sección 3 vale: la supervisión vive en conocimiento y la medición en el orden.
2. La escala de autonomía de la IA y la clasificación de la frontera se publican con sus nombres (delegar, centauro, cíborg, reservar), citando a Dell'Acqua y otros 2023 cuando se nombre la frontera.
3. Las cifras de mercado (MIT NANDA, Whitelane) no se usan en público hasta verificarlas en fuente primaria.
4. Las fuentes del documento base se fichan una a una en `02-fuentes.md` antes de citarlas en un post.

Con esto la versión 0.2 queda validada como índice del método y de la serie.
