# Panel ronda 2: director de transformación de un banco grande español

Evaluación de la versión 2.1 del método Synergós. Perfil inventado y plausible, no una persona real. Todo lo que cuento de "mi banco" es inventado. No he verificado en fuente ninguna norma ni práctica supervisora que menciono; donde las nombro es por orden de magnitud y lo marco como pendiente de un jurista o del área de cumplimiento normativo.

Qué he leído: capítulos 1 a 3 (por qué, arquitectura, principios), el tronco entero (capítulos 8 a 14), el capítulo 17 (tecnología) y el 18 (orden), el módulo 2, el módulo 11, los módulos 19 a 21, la tabla "Qué es obligatorio según alcance", los anexos B, C, D, G, H e I, el texto de la infografía y la síntesis de la ronda 1. No he leído los módulos 3 a 10 ni 12 a 16 enteros, ni el anexo E de fuentes, ni los capítulos 19 a 21. Si algo de lo que digo que "falta" está en esas partes, es culpa mía.

## 1. Mi empresa en tres frases

Banco Meridiano (inventado): unos veinte mil empleados, red de oficinas, banca digital, hipotecas, consumo, pymes y un centro de atención telefónica y digital subcontratado en parte. Tiene tres líneas de defensa asentadas, un área de validación de modelos, una auditoría interna que se toma en serio sus propios informes, representación sindical fuerte y un núcleo de sistemas con décadas de parches que nadie se atreve a tocar. La transformación que tengo entre manos: meter IA generativa en la tramitación de reclamaciones y de hipotecas, reducir coste por operación en el back-office y no perder a las tres o cuatro personas de cada mesa que saben qué expediente huele mal.

## 2. Lo que me aportaría el método

De lo más a lo menos valioso.

**1. El mapa de lo que nadie escribió (capítulo 9, anexo B).** Es lo mejor del método para mí. En un banco, el riesgo de persona clave está medido para directivos y para la sala de mercados, y no para la mesa de operaciones donde una señora de cincuenta y ocho años sabe qué cliente de qué oficina manda la documentación a medias y cuál es de fiar. La columna de concentración me da un papel que enseñar al comité. Y la tercera pregunta del comité (qué le pasa a cada fila con cada opción) convierte una intuición en un criterio de decisión. Con reservas: las de la ronda 1 sobre el compromiso de uso me parecen más graves en un banco (sección 7 de esta ronda).

**2. La puerta de diseño con criterios fijados antes y contrafirma (capítulos 11, 12, 18, anexo C).** No me enseña nada nuevo como forma: ya tengo comités de producto, de modelos y de cambios con criterios escritos. Lo que sí aporta es llevar esa disciplina al lado de las personas y del conocimiento, que mis comités no miran. La decisión de una página por opción es lo que más rápido adoptaría, porque cabe en mi gobierno sin crear otro. Y el criterio de "no se reescribe al ver el resultado" es una buena defensa contra el piloto que se justifica a posteriori, que aquí abunda.

**3. El inventario único y la ficha del agente (capítulo 18, módulo 24).** Mis modelos tienen inventario; mis casos de IA generativa no están a la altura. Los once campos de la ficha, el estado (en evaluación, en experimento, aprobado, retirado) y el techo de autonomía por función me dan una plantilla razonable para casar con el inventario de modelos en lugar de abrir otro. Lo marco como "cuadra con lo que ya hago, falta el puente" (ver sección 7).

**4. La escala de autonomía con techo y la regla "derechos de las personas, nivel 2 como máximo" (capítulo 17).** En crédito, en prevención de blanqueo y en reclamaciones esto es lo que mi segunda línea pediría igualmente. Tenerlo escrito como regla de partida con excepción por análisis jurídico me ahorra una discusión. Subir y bajar con criterios previos y sin que bajar sea un fracaso es sensato.

**5. Eliminar antes de acelerar (capítulo 11 pregunta 2, módulo 2).** En mi banco hay una capa enorme de deuda de proceso: controles que duplican otros controles, conciliaciones que nadie lee, informes que se mandan por costumbre. La pregunta "qué sostenía el paso" es la correcta, porque en un banco muchos pasos son un control que nació de una sanción o de un incidente. Es una buena norma para no automatizar un control zombi.

**6. Coste por tarea completada y coste que no está en la factura (capítulo 18, modelo económico).** Es la cuenta que mi director financiero me va a pedir. Integración, revisión humana, gobierno, vigilancia: están en presupuestos distintos y nadie los suma. La regla de compararlo en cada puerta con la línea base es útil.

**7. Casos de prueba que se repiten cuando cambia el modelo o los permisos (capítulos 12 y 14, módulo 24).** Con un proveedor externo de modelo que actualiza sin avisarme, es obligatorio. Es lo más parecido a la monitorización de modelos que contiene el método (más abajo digo por qué no basta).

**8. La marcha atrás como salida legítima y los casos Klarna y Commonwealth Bank (capítulo 18, cierre).** Para el comité de dirección el caso de un banco australiano que revirtió una decisión y pidió disculpas pesa más que cualquier argumento. Lo usaría tal cual, con la cautela del propio texto: la causa que se atribuye es lectura del autor.

**9. Las tres líneas, bien colocadas en el tiempo (capítulo 18).** La segunda línea en diseño y piloto, la tercera en sostenimiento. Es lo correcto. Por esto mi segunda línea lo leerá con buena disposición.

**10. El calendario de revisiones (anexo H) y el anexo de roles (anexo I).** El anexo I con "lo que no puede hacer" cada rol es de lo más útil del documento para quien tiene que casarlo con un organigrama de verdad. Las incompatibilidades (no contrafirmar la propia decisión, medición no firma) las entiende cualquier auditor.

## 3. Lo que no usaría o me sobra

- **El girasol y el ángulo de 137,5 grados (capítulo 7).** El texto ya dice que es una imagen y no un argumento. Para un comité de riesgos es ruido. Lo quitaría de cualquier material que llegue al comité de dirección.
- **Los 24 módulos como obligatorios en alcance de sistema (tabla de alcance).** En un banco un programa de sistema (por ejemplo, toda la tramitación de hipotecas) tendría que escribir 17 módulos más siete anexos de decisión. Es lo que mi oficina de transformación llama "el método que mata el programa". El propio texto reconoce el riesgo (la pregunta abierta de las cinco preguntas) pero la tabla lo contradice. Yo trabajaría con el núcleo de ocho filas más los condicionales y trataría los módulos como biblioteca consultable, no como lista de comprobación.
- **Módulo 23 (innovar con IA) y carril de exploración.** Útil en una startup. En un banco, la exploración ya vive en un laboratorio con su propio gobierno y no quiero que el método lo reabra.
- **Módulo 22 (huella material) y módulo 5 (colaboración) como obligatorios.** No son lo que me quita el sueño. Los dejaría en recomendados. (El texto marca el 5 como "extensión sin causa documentada"; estoy de acuerdo con la sospecha.)
- **Las cinco puntas (módulo 16) como anexo obligatorio.** Estrategia, estructura, procesos, recompensas y personas: ya lo cubre mi modelo operativo objetivo. Duplicaría trabajo.
- **El nombre de "referentes" y "comunidad de práctica".** Mi organización tiene "embajadores" y "champions" y no voy a renombrar nada. Es un asunto de vocabulario, pero el método dice "campeones" en otros textos y "referentes" aquí: si la gente tiene que traducir, se pierde.
- **La regla de "pocas cosas a la vez" (principio 3) tal como está.** Dos o tres aceleradores por ciclo suena bien en un programa acotado. En un banco hay doscientos proyectos en vuelo y cinco programas de IA. El límite tiene sentido por ámbito, pero hay que decir cómo se aplica a una cartera corporativa y quién la arbitra. Ahora mismo no lo dice.

## 4. Cómo lo aplicaría yo: mi itinerario

### Nivel 1: una iniciativa (asistente para la tramitación de reclamaciones, ejemplo inventado)

Ámbito: el servicio de reclamaciones de clientes de Banco Meridiano, unas ciento cuarenta personas en tres centros. Alcance: de flujo (no es puntual porque cambia el trabajo de un equipo entero y no es de sistema porque no toca todo el banco). Objetivo de negocio escrito por el director general de clientes: bajar el tiempo medio de resolución sin subir las reclamaciones que acaban en el organismo supervisor externo ni las sanciones.

**Antes de empezar (semana 0 a 2).** El patrocinador (directora general de clientes) firma el compromiso de uso del mapa. Nombro al dueño operativo (el responsable del servicio, no alguien de tecnología). Mi segunda línea de cumplimiento y de protección de datos entra ya, no al final. Consulta a la representación sindical: no es opcional en mi banco y la hago yo antes de que me la pidan. Paralelo: un cribado jurídico de una casilla (clasificación de riesgo del sistema, base jurídica de los datos, competencia), que el método no pide y yo sí.

**Fase 1, diagnóstico (unas semanas, a la vez varias cosas).**
- A la vez: mapa del flujo real observando en el puesto, mapa de lo que nadie escribió (sale de las mismas visitas), línea base con su variación normal (la oficina de datos extrae tiempos, reabiertas, escaladas al supervisor, satisfacción) y mapa de actores.
- A la vez, y fuera del equipo del servicio: inventario de lo que ya se usa con una consulta anónima (sé que hay gente pegando textos de reclamaciones en herramientas públicas; es mi mayor riesgo hoy y el método lo trata bien), y evaluación de madurez de la tabla del anexo D, que haré con seguridad en horas.
- La puerta solo exige tres cosas: restricción aceptada, línea base medida, mapa hecho. Contrafirma: alguien de control de gestión financiero, no de mi segunda línea (razón en la sección 7).

**Fase 2, diseño.** Cartera corta (dos o tres iniciativas). Para cada opción, la página del anexo C. Aquí se decide por tarea: eliminar (por ejemplo, el informe duplicado a la oficina del defensor interno), acelerar (la búsqueda de antecedentes), aumentar (propuesta de respuesta que el tramitador edita) y qué no se automatiza (reclamaciones con riesgo de sanción por conducta). Techo de autonomía: nivel 2 para toda respuesta que afecte a derechos del cliente. En paralelo, y es lo que más tiempo ahorra: casos de prueba escritos por los tramitadores, validación de modelos revisando proveedor y datos, evaluación de impacto de datos personales, y modelo económico con valle (el servicio tendrá un pico de reabiertas al empezar). Firma de umbrales de piloto por el patrocinador con contrafirma de finanzas.

**Fase 3, piloto.** En un centro con rotación alta y volumen alto (la regla de elegir el entorno difícil me gusta, mi tentación es el centro más ordenado). Comparación con otro centro. Criterio de parada y revisión a noventa días. Casos de prueba repetidos cada vez que el proveedor cambie el modelo. Derecho a parar de quien usa la herramienta, escrito.

**Fase 4, escala.** Por centros, con minipuerta en cada etapa. Responsable de adopción distinto de quien despliega. Al menos dos referentes por centro. Aquí cambio la evaluación y los incentivos del servicio: si sigo premiando el número de expedientes cerrados, la herramienta produce expedientes mal cerrados más rápido.

**Fase 5, sostenimiento.** Dueño operativo con presupuesto recurrente, cuadro de indicadores en régimen, volver a pasar casos de prueba cada trimestre. Mi auditoría interna comprueba una vez al año que el inventario coincide con lo que está en uso. La puerta se cierra con dos periodos de medición sin el equipo del programa.

Lo que se hace a la vez en todo el itinerario: consulta sindical, cribado jurídico, validación de modelos y evaluación de datos personales corren en paralelo al diagnóstico y al diseño, no en serie. El método lo dice a medias ("la segunda línea participa en el diseño y el piloto"); yo lo escribiría como calendario.

### Nivel 2: varios ámbitos a la vez (el programa de IA del banco)

Cinco ámbitos, cada uno con su ciclo: (a) reclamaciones y atención, (b) tramitación de hipotecas, (c) alertas de prevención de blanqueo y fraude, (d) análisis de crédito a pymes, (e) mantenimiento y modernización de código heredado en tecnología. Los cinco con riesgos distintos y con reguladores internos distintos.

- **Un solo gobierno, no cinco.** Un comité de puertas con el patrocinador (comité de dirección), los dueños operativos de cada ámbito, medición y la persona que contrafirma. Un único inventario que se case con el inventario de modelos que ya tengo, con la ficha del agente como ampliación, no como sustituto.
- **Escalonar la entrada de la IA dentro del servicio.** No cinco pilotos de IA generativa a la vez. Orden por riesgo: (e) primero, porque es IA como herramienta del equipo de tecnología con poco impacto en clientes; (a) segundo, con techo nivel 2; (b) tercero; (d) después, con validación de modelos plenamente implicada; (c) el último y solo con el supervisor al corriente, porque ahí el error cuesta más y el nivel 2 es el techo práctico. Es mi lectura del principio 3, no una regla del método.
- **Medición compartida.** Una oficina pequeña de medición (el método la prevé) con un único cuadro para el comité y el consejo. Un mismo indicador de conocimiento (concentración) y de personas (casos fuera de patrón) en los cinco ámbitos, para poder comparar.
- **El delta, por ámbito y por elemento.** No me fío de una media (ya lo dijo la ronda 1). Pediría para cada ámbito el vector de deltas por elemento y condicionaría el desembolso de cada fase a que ninguno caiga.
- **Dependencias.** La plataforma de datos y el entorno de modelos son comunes. Las pongo como habilitadores en la cartera (el método los permite) y las financio aparte para que no las pague el primero que llegue.
- **Presupuesto.** Horquilla por fase que cada puerta libera o devuelve: el método coincide con cómo mi director financiero ya quiere gastar en proyectos inciertos.

## 5. Lo que no entiendo o me suena a jerga

- **"Crecer a la vez".** Sé qué quiere decir, pero para un comité es una consigna. Lo que vale es la regla operativa que hay debajo (el vector de deltas). El propio ronda 1 ya pidió una definición operativa de "a la vez". La suscribo.
- **"Acelerador".** Entiendo la definición (una tecnología concreta que se activa en un ámbito). En mi organización "acelerador" significa programa de aceleración de startups. Habrá que renombrarlo en el glosario interno.
- **"Elemento" (personas, conocimiento, tecnología) y "palanca".** Los dos se usan como sinónimos. Para un banco, "elemento" no dice nada. "Palanca" tampoco.
- **"Delta".** Para mi gente de riesgos, delta es una sensibilidad de opciones. Hay que decir "avance hacia el objetivo".
- **"Nivel" para madurez y para autonomía.** El anexo D lo reconoce, y siguen chocando. Además mi banco usa nivel 1, 2 y 3 para el capital.
- **"Ámbito", "ciclo", "iniciativa", "programa", "cartera".** Los cinco se usan con precisión interna y yo tendría que casarlos con mis términos (línea de negocio, proceso, proyecto, programa, portfolio). Haría una tabla de equivalencias y la pondría al principio.
- **"Puerta".** Ya tengo puertas: comité de nuevos productos, de modelos, de cambios. Hay riesgo de que la gente no sepa si la puerta Synergós sustituye a la mía o se suma a ella. El método no lo dice.
- **"Frontera dentada", "centauro", "cíborg", "delegar/reservar".** Entiendo la clasificación y me parece útil, pero los nombres no los usaría con un comité. Diría "tareas que la IA hace sola, en pareja, o que se reservan".
- **"Dueño operativo", "dueño del beneficio", "dueño de los datos", "dueño del flujo".** Cuatro dueños. En mi banco ya tengo propietario del proceso, del dato, del modelo y de la aplicación. El anexo I ayuda, pero casarlos exige una tabla.
- **"Contrafirma".** Se entiende, pero en mi organización contrafirma tiene un uso jurídico concreto (apoderamientos). Lo llamaría "visto bueno independiente" y su rol tendría que casarse con mi segunda línea o con control interno financiero.
- **"Mapa de lo que nadie escribió".** Es un nombre bonito y lo uso con gusto, pero un auditor lo llamaría "inventario de conocimiento crítico no documentado". Me quedaría con los dos.
- **"Deuda de proceso".** Entendible; es un buen término.
- **"Supervisión del programa, de doble bucle".** No lo entiendo hasta que leo la nota: es revisar los supuestos, no solo los errores. La etiqueta sobra.

## 6. Los primeros noventa días

**Qué haría el lunes.** Elegir un único ámbito (reclamaciones, que combina volumen, regulación y poco riesgo sistémico) y pedir una reunión de una hora con la directora general de clientes con tres preguntas que el método obliga a plantear: qué resultado quiere cambiar, si el programa contempla o no reducir plantilla, y quién será su contrafirma. Con la respuesta a la segunda, que es la que el método deja abierta, decidiría si sigo adelante. Paralelo: llamar a mis tres interlocutores internos que no pueden enterarse al final (segunda línea de riesgo no financiero y cumplimiento, validación de modelos, relaciones laborales) para decirles que el método existe, que no sustituye a su proceso y que quiero su calendario.

**Qué costaría (sin cifras).**
- Tiempo: el de una persona dedicada del equipo de transformación a coordinar y otra de medición durante los noventa días. Un tramitador de cada centro cediendo parte de su semana para las visitas y los casos de prueba (el método pide horas reconocidas y yo las pondría por escrito). Horas de la segunda línea, de validación y de relaciones laborales más altas de lo que les gustaría.
- Personas: la que más escasea y no sale en el método es el analista de datos que extrae la línea base de sistemas heredados. Es el cuello de botella real.
- Político: una conversación incómoda con el comité de dirección sobre la declaración de intención de plantilla. No la evito, porque sin ella el mapa se pone en riesgo (más abajo).

**Qué señal diría que va bien.**
1. El patrocinador firma el compromiso de uso sin pedir cambios de fondo.
2. El mapa da filas concentradas que el responsable del servicio no esperaba y no se las discute.
3. La línea base se mide con su variación normal y alguien de finanzas la reconoce como cifra suya.
4. La segunda línea y validación objetan algo por escrito durante el diseño, no al final. Si nadie objeta, me preocupa.
5. Aparece en la consulta anónima un uso informal que no conocíamos y el banco responde con una herramienta aprobada en lugar de una circular.

Señal de que va mal: la primera puerta se pasa por calendario; los tramitadores contestan al mapa con respuestas de manual; el dueño operativo resulta ser alguien del equipo de transformación.

## 7. Lo que falta para mi tipo de empresa

Va de lo más a lo menos grave, y con la reserva de que algo puede estar en los módulos que no he leído.

1. **Gestión del riesgo de modelo y validación independiente.** El método tiene casos de prueba, vigilancia y volver a evaluar al cambiar el modelo. No tiene la figura de validación independiente del modelo antes de producción, con su inventario, su clasificación de materialidad y su revisión periódica, que en un banco existe (por práctica supervisora, aunque no puedo citar el texto exacto sin comprobarlo). El "responsable de medición" certifica datos, no valida modelos. Tal como está, mi validación de modelos lo vería como un proceso paralelo y ligero, y lo apartaría. Necesita un puente explícito: qué parte de la ficha del agente es el expediente de validación, quién valida y cómo se relaciona con la puerta de autonomía.
2. **Gobierno de terceros y resiliencia operativa digital.** El método dice "salida pactada con cada proveedor" y trata la contratación sobre todo en clave de sector público. En un banco, que un modelo de lenguaje de un proveedor concentrado soporte un proceso crítico es un asunto de resiliencia, de subcontratación y de plan de salida con ensayo, con obligaciones regulatorias que no me corresponde citar de memoria. Falta un apartado sobre procesos críticos, concentración y prueba de la salida. Lo que el método llama "construir, comprar o retirar" es un comienzo, no el tratamiento.
3. **Independencia de la segunda línea.** El método pone a "una persona ajena al equipo, de segunda línea o finanzas" como contrafirma. En mi banco, si la segunda línea contrafirma una decisión, deja de poder cuestionarla después: es coautora. La ronda 1 de cumplimiento ya lo dijo y para mí es más grave. Yo reservaría la contrafirma a finanzas o control interno de gestión, y dejaría a la segunda línea con el derecho a objetar por escrito (que el método ya le da) y la obligación de que su objeción conste. La auditoría interna, por el mismo motivo, no puede estar en el diseño, y el método ya la coloca en sostenimiento.
4. **Piezas no retirables.** La propuesta 1 de la ronda 1 me parece más grave aquí que para la mayoría. "Quitar una pieza obligatoria lo decide el patrocinador" es incompatible con mi modelo de gobierno: las políticas internas que derivan de la regulación no las dispensa el negocio, las dispensa la función que es propietaria de la política, con excepción formal. El texto dice que la ley se cumple "en cualquier alcance", bien, pero entre la ley y la sugerencia del método está mi normativa interna, y el método no la nombra. Necesito una lista de no retirables y una regla de que el patrocinador no puede dispensar lo que pertenece a una política corporativa.
5. **Conducta con el cliente y reclamaciones.** El módulo 21 trata la mirada del cliente y el canal humano. En banca de consumo hay obligaciones de transparencia, de adecuación y de trato del cliente vulnerable que condicionan qué puede decidir un sistema y qué se explica. El método debería permitir enganchar el criterio "cliente vulnerable" al mapa de lo que no encaja.
6. **Cambios en sistemas heredados.** Lo que se hace con un núcleo de sistemas antiguo (calendario de cambios, ventanas, congelaciones, entornos de pruebas, interfaces con terceros) no aparece, que yo haya visto, salvo como condición de elegir un piloto difícil. Mi cuello de botella para meter cualquier cosa no es la IA: es el calendario de cambios del núcleo. Un método que no dice nada sobre integrarse con eso queda en la capa de proceso y personas.
7. **Medición con datos regulatorios y calidad del dato.** El módulo 10 (datos) existe pero no lo he leído entero. Falta, si no está, la relación entre dato de gestión y dato regulatorio, la trazabilidad y la conservación de registros de las decisiones del sistema.
8. **Relación con el supervisor.** Cuándo se comunica a un supervisor externo que se va a introducir IA en un proceso material y cuándo no, y quién lo hace. No es un asunto del método, pero lo menciono porque mi comité de dirección lo va a preguntar el primer día.
9. **Tensión con la declaración de intención de plantilla (propuesta 5, ronda 1).** En un banco con representación sindical y precedentes de procesos de ajuste, escribir "se prevé" o "no se descarta" tiene efectos laborales y, si cotiza, posiblemente de información al mercado. No sé cuál es el tratamiento jurídico exacto y lo marco como pregunta a un jurista laboral. La propuesta protege a quien trabaja y es honesta, pero en mi caso no la podría emitir sin una redacción pactada con jurídico y relaciones laborales. El método debería decirlo y no dar por hecho que es un papel que firma un patrocinador.
10. **Mapa por observación y datos personales.** La propuesta 6 de la ronda 1 (levantar el mapa también por observación) en un banco choca con secreto bancario, con grabación de llamadas y con control de la actividad laboral. Observar el puesto o escuchar llamadas con ese fin exige una base y un pacto con la representación legal que el método solo menciona como "cuando toca condiciones de trabajo". Más grave aquí.
11. **Presupuesto anual y retribución.** El modelo económico por fases con horquilla que cada puerta libera o devuelve es sensato, pero mi presupuesto es anual, con objetivos individuales de dirección atados a él. Y la retribución variable de las redes comerciales está regulada en cuanto a incentivos y conducta. El capítulo 15 habla de rediseñar incentivos; no dice cómo hacerlo cuando el esquema retributivo tiene que pasar por un comité de remuneraciones y por la política de conducta.
12. **Cómo convive con lo que ya tengo.** Falta una tabla de equivalencias con marcos de gestión de proyectos a escala, con la oficina de transformación y con los marcos de riesgo existentes (la mención a NIST e ISO 42001 es un comienzo). Si no digo qué sustituye y qué se suma, el método es otro marco más, y los bancos están saturados de marcos.
13. **Escala del método a la cartera.** Qué pasa cuando hay cien iniciativas en paralelo con ámbitos que se solapan. Ya lo dije en la sección 3.

### Lo de la ronda 1 que, desde un banco, es más o menos grave

Resumen contra las quince propuestas de la síntesis:

| N.º | Propuesta | En mi banco |
|---|---|---|
| 1 | Lista de no retirables | Más grave: mi normativa interna la necesita |
| 2 | Mínimo por elemento en lugar de media | Igual de grave. Mi consejo de riesgos nunca aceptaría una media que compensa |
| 3 | Valle con tope | Menos grave: mi financiero ya pone topes por fase |
| 4 | Coste y beneficio neto en la puerta | Menos grave: es mi práctica habitual; me conviene que se escriba |
| 5 | Declaración de intención de plantilla | Más delicada: la necesito, pero con jurídico y relaciones laborales (punto 9) |
| 6 | Mapa ampliado y triangulado | Más grave por secreto bancario y control laboral (punto 10) |
| 7 | Medición independiente y contrafirma de finanzas | Más grave y la apoyo: encaja con validación y con control interno |
| 8 | Alcance con importe y reversibilidad | Más grave: mi banco clasifica por materialidad y el alcance "puntual/flujo/sistema" no lo reconozco como equivalente |
| 9 | Cribado legal de una casilla | Menos grave: ya lo hago. Una casilla me basta si la rellena jurídico |
| 10 | Definición de "a la vez" y refutación | Igual |
| 11 | Sector público | No me afecta |
| 12 | El método se aplica a sí mismo | Más grave: sin un primer programa real con coste, mi comité no va a entrar |
| 13 | Escala de evidencia | Menos grave para un banco que compra por resultados que por papers; me importa que esté claro qué está probado |
| 14 | Hoja de oficina y horas mínimas | Igual |
| 15 | Nombres que colisionan | Más grave: la colisión con términos propios es peor de lo que creían |

## 8. Veredicto

**Adoptaría solo una parte.** Las partes que tomaría: el diagnóstico con el mapa de lo que nadie escribió y la línea base, la decisión de puerta de una página, el inventario único casado con el de modelos, el techo de autonomía, el eliminar-antes-de-acelerar, el coste por tarea completada y la marcha atrás. Las dejaría fuera o aplazaría hasta que haya un programa real: los 24 módulos obligatorios en alcance de sistema, el girasol y el vocabulario propio, y cualquier cosa que el patrocinador pueda dispensar sin pasar por mi segunda línea. No lo adoptaría entero porque no habla de validación de modelos, de terceros críticos ni de calendario de cambios del núcleo, que es donde mi banco gana o pierde.

Frase para el comité de dirección: "Es un método para que la IA no nos haga perder lo que nuestra gente sabe y no escribió, con puertas que ya conocemos; lo encajamos con nuestro gobierno de modelos y de riesgos, y lo probamos en un solo servicio con un presupuesto máximo y un criterio de parada, antes de hablar de extenderlo."

Una última advertencia sobre mi propio informe: soy un perfil plausible. Las prácticas que atribuyo a "los bancos" son generales y no las he contrastado con fuente. Lo que toca a regulación, a derecho laboral y a información al mercado debe revisarlo un jurista antes de usarlo.
