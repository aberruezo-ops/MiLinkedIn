# Parte V. El detalle: cómo se hace

Hasta aquí el documento ha descrito la arquitectura: los elementos, el orden, las fases, las puertas. Esta parte entra en lo que hay dentro. Son veinticuatro módulos, cada uno sobre un tema que el método toca en varias fases y que necesita desarrollo propio. Casi todos siguen esta estructura: qué es y por qué importa, lo que dicen las fuentes, cómo se hace, cómo se mide, las señales de que va mal y lo que todavía no está resuelto. Donde falta un apartado es porque no lo tengo. No todos los módulos hacen falta en todos los programas: la tabla "Qué es obligatorio según alcance", al cierre de esta parte, dice qué es obligatorio, qué es recomendado y qué no aplica en una iniciativa puntual, en una de flujo y en una de sistema.

El hilo que los une es una pregunta que la arquitectura plantea y no responde: en un trabajo en el que la tecnología puede hacer cada vez más cosas, ¿cuál es el lugar de las personas, y cómo se diseña para que la tecnología lo amplíe en lugar de ocuparlo?

## Módulo 1. Lo que aporta una persona

### Por qué empezar por aquí

Casi todos los proyectos de IA empiezan preguntando qué puede hacer la máquina. Synergós empieza al revés: qué aporta hoy la persona que hace el trabajo, y qué parte de eso no debería perderse. No lo hago por romanticismo: la evidencia sobre tecnología y productividad dice, una y otra vez, que el valor sale de combinar a las personas con la máquina más que de sustituirlas.

### Lo que dicen las fuentes

Ajay Agrawal, Joshua Gans y Avi Goldfarb propusieron en 2018 una forma muy útil de mirar la IA: es una tecnología que abarata la predicción. Predecir qué cliente va a reclamar, qué expediente tiene un error, qué palabra viene después. Cuando algo se abarata, lo que lo complementa gana valor. Y el complemento de la predicción es el juicio: decidir qué hacer con ella, qué riesgo se acepta, qué importa en este caso concreto. La IA no elimina la necesidad de juicio; la aumenta, porque genera más predicciones sobre las que alguien tiene que decidir.

Daron Acemoglu y Pascual Restrepo mostraron en 2019 que la historia de la automatización tiene dos fuerzas. Una desplaza a las personas de tareas que pasan a hacer las máquinas. La otra crea tareas nuevas en las que las personas tienen ventaja, y devuelve trabajo. Cuando solo opera la primera, el empleo y los salarios se resienten. El resultado depende de cuántas tareas nuevas se crean, y eso no ocurre solo: es en gran parte una decisión de diseño.

Paul Daugherty y James Wilson describieron en 2018 lo que llamaron el medio que falta: el espacio en el que personas y máquinas trabajan juntas. Las personas entrenan a los sistemas, explican sus resultados y vigilan que se usen bien. Las máquinas amplían la capacidad de las personas, interactúan a escala y hacen trabajo físico o repetitivo. Las organizaciones que más ganaban no eran las que más automatizaban, sino las que rediseñaban los procesos alrededor de esa colaboración.

David Autor, David Mindell y Elisabeth Reynolds llegaron a una conclusión parecida en el estudio del MIT sobre el futuro del trabajo, publicado como libro en 2022: el resultado de la tecnología depende de las instituciones y de las decisiones que la rodean.

### Qué aporta una persona: un inventario

En el trabajo real, lo que una persona aporta y una máquina hoy no aporta, o aporta mal, se agrupa en siete cosas.

| Aportación | Qué es | Ejemplo en un servicio |
|---|---|---|
| Juicio en el caso difícil | Decidir cuando las reglas no bastan o se contradicen | Un expediente que cumple todos los requisitos y aun así huele mal |
| Contexto | Saber lo que no está en los datos: historia, intenciones, relaciones | Saber que ese proveedor siempre entrega tarde en diciembre |
| Responsabilidad | Alguien que responde, da la cara y puede rendir cuentas | Explicar a un ciudadano por qué se le ha denegado algo |
| Relación y confianza | La conversación, la empatía, la lectura de lo que no se dice | Calmar a un cliente antes de resolver su problema |
| Lo nuevo y la excepción | Reconocer que algo no encaja en ningún patrón conocido | Detectar un fraude que no se parece a los anteriores |
| Sentido | Saber para qué se hace algo y cuándo deja de tener sentido | Proponer eliminar un trámite que ya no sirve a nadie |
| Enseñar | Transmitir el oficio a quien llega | El veterano que explica por qué ese caso es distinto |

La tabla es una plantilla de diagnóstico. En la fase 1, para cada rol que va a cambiar, se pregunta cuáles de estas siete aportaciones hace hoy esa persona, con qué frecuencia y qué pasaría si dejara de hacerlas. Se cruza con el mapa de lo que nadie escribió, porque buena parte de esas aportaciones viven en lo tácito.

### Cómo se usa en el método

**En el diagnóstico**, el inventario de aportaciones se levanta junto al mapa, con las mismas personas. En una organización grande se pregunta por perfil, con la misma regla de parada que el mapa (capítulo 9).

**En el diseño**, cada opción dice qué aportaciones conserva, cuáles amplía y cuáles elimina. Esa línea va en el anexo a la decisión de puerta (anexo C), cuando la tabla "Qué es obligatorio según alcance" la marca como obligatoria para ese alcance. La quinta pregunta de la puerta (¿crecen los tres elementos?) se responde con datos: si una opción elimina el juicio, el contexto y la relación de un rol y le deja solo la vigilancia de lo que hace la máquina, no está haciendo crecer a las personas aunque mantenga el empleo.

**En la escala**, los roles se describen por aportaciones, no por tareas. Es la forma más directa de que las carreras y los incentivos se rediseñen con sentido.

### Señales de que va mal

- Los roles nuevos se describen solo por lo que la persona ya no hace.
- La persona que queda "en el bucle" no tiene poder real para cambiar lo que hace el sistema.
- Las aportaciones de relación y de enseñanza no aparecen en ningún indicador.

!! Pregunta abierta. ¿Y si una aportación humana deja de ser necesaria de verdad? | El inventario puede volverse una defensa de todo lo que hacen hoy las personas, y no todo merece defenderse. A veces la máquina hace algo mejor y conviene aceptarlo. Mi criterio provisional: una aportación se puede retirar si se dice a propósito, si se mide que el resultado no empeora y si la persona pasa a una tarea con al menos el mismo valor. Lo difícil es el tercer requisito, porque las tareas nuevas no aparecen solas.

## Módulo 2. Rediseñar el trabajo sin sustituir

### El problema

Hay tres formas de meter tecnología en un trabajo: sustituir a la persona, ponerla a vigilar a la máquina, o cambiar el trabajo para que persona y máquina hagan cada una lo que mejor hacen. La primera es la que más se vende. La segunda es la que más se hace sin darse cuenta. La tercera es la que defiende Synergós, y es la más difícil.

### Las ironías de la automatización

Lisanne Bainbridge publicó en 1983 un artículo breve que sigue siendo de lo más lúcido que se ha escrito sobre el tema. Lo llamó las ironías de la automatización. La primera ironía: cuanto más se automatiza un sistema, más importante y más difícil se vuelve la intervención humana, porque la persona solo interviene cuando algo ha fallado y el caso es raro. La segunda: la persona que ya no hace el trabajo deja de practicarlo y pierde la destreza justo cuando más la necesita. La tercera: vigilar un sistema que casi nunca falla es una tarea para la que los humanos están especialmente mal dotados; la atención se apaga.

Raja Parasuraman y Victor Riley distinguieron en 1997 cuatro maneras de relacionarse con la automatización. El uso, que es activarla cuando conviene, y tres problemas: el mal uso, que es confiar demasiado en ella (el llamado sesgo de automatización); el desuso, que es desconfiar tanto que se ignora cuando acierta; y el abuso, que es automatizar sin pensar en las consecuencias para quien tiene que convivir con ella, una decisión de quien diseña y dirige, no del operador. Los tres problemas aparecen hoy con la IA generativa. El estudio de la frontera dentada de 2023 encontró que, en las tareas que quedaban fuera de la frontera, los consultores con IA lo hacían peor que sin ella. Mi lectura es que confiaban en la IA justo donde se equivocaba, y por eso lo tomo como ejemplo del primero.

Para Synergós, la consecuencia es concreta: "poner a una persona en el bucle" es el punto de partida de un problema de diseño, y por sí misma no resuelve nada.

### El diseño del trabajo

J. Richard Hackman y Greg Oldham propusieron en 1976 el modelo de las características del puesto, uno de los más contrastados de la psicología del trabajo. Un puesto motiva y rinde cuando tiene cinco cosas: variedad de habilidades, identidad de la tarea (hacer algo completo y reconocible, no una pieza suelta), significado (que importe a alguien), autonomía y retroalimentación sobre el resultado.

El modelo sirve para evaluar un rediseño con IA. Si la IA hace las partes variadas y deja a la persona las repetitivas, baja la variedad. Si fragmenta el trabajo y la persona ya no ve el caso completo, baja la identidad. Si la persona solo valida lo que propone la máquina, baja la autonomía. Un rediseño que empeora las cinco características producirá peores resultados aunque la herramienta sea excelente, porque la gente dejará de implicarse.

Amy Wrzesniewski y Jane Dutton describieron en 2001 algo complementario: las personas rediseñan su propio trabajo desde dentro, cambiando tareas, relaciones y la manera de entenderlo. Lo llamaron *job crafting*. Un rediseño que deja margen para eso aprovecha lo que la gente sabe de su trabajo. Uno que lo cierra todo lo desperdicia.

### Cómo se hace: cinco pasos

1. **Descomponer el trabajo en tareas.** No en funciones ni en procesos, sino en tareas concretas que alguien hace. Es el enfoque que usan los economistas del trabajo desde Autor, y es el único que permite ver qué cambia de verdad.
2. **Clasificar cada tarea con las cuatro categorías.** Delegar, centauro, cíborg o reservar, según el capítulo 17. Para cada una, la pregunta es a qué lado de la frontera dentada cae: dónde mejora la IA el resultado y dónde lo empeora. Se responde probando con casos reales, no con la ficha del proveedor. La frontera se mueve con cada modelo, así que la clasificación se revisa con los casos de prueba cada vez que cambia el modelo.
3. **Recomponer el puesto.** Con las tareas reasignadas, se vuelve a montar el puesto y se evalúa con las cinco características de Hackman y Oldham. Si alguna cae mucho, se rediseña (cuánto es mucho lo fija cada programa en el diseño; anexo G): se devuelve a la persona una tarea completa, se le da la decisión final, se le muestra el resultado de su trabajo.
4. **Diseñar la intervención humana.** Para cada tarea en la que la persona vigila o corrige a la IA: cuándo interviene, con qué información, cada cuánto practica el caso difícil y qué poder tiene para cambiar el sistema. Es la respuesta directa a Bainbridge.
5. **Crear las tareas nuevas.** Qué hará la persona con el tiempo que libera. Si la respuesta es "más de lo mismo", no se han creado tareas nuevas; se ha aumentado la carga. Las tareas nuevas con más valor suelen estar en las aportaciones del módulo 1: más tiempo para el caso difícil, para la relación, para mejorar el proceso y para enseñar.

**El flujo entero, antes que la tarea suelta.** Desde la versión 1.7, los cinco pasos se aplican al flujo de principio a fin: desde que entra la petición hasta que alguien recibe el resultado. Mejorar una tarea deja intactas las esperas, los traspasos y las revisiones duplicadas que hay alrededor, y la ganancia se pierde en la siguiente cola. Antes de poner IA en un paso conviene preguntar si ese paso tiene que existir. A lo que se arrastra sin motivo lo llamo deuda de proceso: aprobaciones que nadie recuerda por qué se pusieron, datos que se piden dos veces, controles que duplican otro control. Automatizarla la hace más rápida y más difícil de quitar.

### Un caso compuesto

Un equipo de tramitación incorpora un asistente que lee la documentación y propone una resolución. La primera versión del diseño dejaba a los tramitadores validando propuestas en pantalla, una tras otra. En el piloto, la productividad subió las dos primeras semanas y luego se estancó; los errores que se colaban eran justo los casos raros, que nadie miraba con atención porque el noventa por ciento de las propuestas eran correctas (cifras ilustrativas, no medidas). El rediseño cambió tres cosas: el asistente señalaba su nivel de confianza y los casos fuera de patrón iban directos a la persona sin propuesta previa; cada tramitador llevaba sus expedientes completos de principio a fin; y una parte de la jornada se reservó para revisar a fondo una muestra y mejorar las reglas del asistente. Es un caso compuesto: lo construyo para ilustrar el rediseño, y ni sus cifras ni su desenlace son un resultado medido.

### Señales de que va mal

- La persona pasa la mayor parte del día validando lo que propone la máquina.
- Los errores que se escapan son siempre los casos raros.
- Nadie sabe qué se hace con el tiempo liberado.
- Se ha puesto IA en un paso que el flujo no necesitaba.

!! Pregunta abierta. ¿Cuánta práctica del caso difícil necesita alguien para no perder la destreza? | Bainbridge planteó el problema hace cuarenta años y sigue sin una respuesta general. En aviación se resolvió con simuladores y horas obligatorias de vuelo manual. En el trabajo de oficina no hay nada equivalente. Propuesta provisional: reservar a propósito una proporción de casos para que se resuelvan sin asistencia, y medir la calidad de esas resoluciones, leída por equipo y no por persona (capítulo 18). No sé qué proporción es la adecuada.

## Módulo 3. La IA: cuándo sí, cuándo no y cuándo quitarla

### Por qué hace falta un criterio

La pregunta "¿dónde ponemos IA?" se responde casi siempre por disponibilidad: hay una herramienta, hay un caso que se le parece, se pone. Synergós pide un criterio previo, porque la misma herramienta puede ser una gran idea en una tarea y un error caro en la de al lado.

### Lo que dicen las fuentes

La evidencia experimental sobre IA generativa en el trabajo ha crecido rápido y apunta en una dirección bastante clara, con matices. Shakked Noy y Whitney Zhang publicaron en 2023 un experimento con tareas de redacción profesional: la IA redujo el tiempo y mejoró la calidad, y la mejora fue mayor para quienes peor lo hacían al principio. Brynjolfsson, Li y Raymond encontraron algo parecido en un centro de atención al cliente, con una mejora media del 15 % y en torno al 30 % para los menos expertos. Dell'Acqua y sus coautores mostraron el reverso: en las tareas fuera de la frontera, los consultores con IA lo hacían peor que sin ella.

Daniel Kahneman, Olivier Sibony y Cass Sunstein publicaron en 2021 un libro sobre el ruido: la variabilidad no deseada en los juicios de personas expertas que deberían coincidir. Dos tramitadores ante el mismo expediente deciden distinto; el mismo tramitador decide distinto un lunes y un viernes. Un sistema bien diseñado puede reducir ese ruido. Es un argumento a favor de la IA que, en mi experiencia, casi nunca se usa, y que me parece más sólido que el ahorro de tiempo.

### La matriz de decisión

Para cada tarea candidata se responden siete preguntas. No hay una puntuación mágica; la matriz sirve para que la decisión sea explícita.

| Criterio | Inclina hacia sí | Inclina hacia no, o hacia reservar |
|---|---|---|
| Coste del error | Bajo, detectable | Alto, difícil de detectar |
| Reversibilidad | El error se deshace fácil | El error no tiene vuelta atrás |
| Datos | Hay datos suficientes y representativos | Pocos datos, o sesgados |
| Frecuencia | Tarea frecuente y parecida | Tarea rara y distinta cada vez |
| Valor formativo | La tarea no enseña nada a nadie | La tarea es la que forma a los nuevos |
| Explicación | Nadie necesita saber por qué | Hay que poder explicar la decisión a un tercero |
| Relación | La tarea no depende de la confianza | La tarea es la relación |

Una tarea con coste de error alto y difícil de detectar no está prohibida para la IA. Pero exige subir muy despacio por la escala de autonomía y diseñar con cuidado la intervención humana del módulo 2. Si además la decisión afecta a derechos de las personas, no se puede deshacer o hay que poder explicarla a quien la recibe, vale el techo de autonomía del capítulo 17. Una tarea que es la que forma a los nuevos se puede automatizar, pero solo después de decidir quién enseña lo que enseñaba.

### Cuándo no

Hay cuatro situaciones en las que el método recomienda no poner IA, al menos todavía.

**Cuando el problema no es de predicción.** Si la restricción es que dos departamentos no se hablan, ninguna IA lo arregla. Es el error del capítulo 5: comprar un acelerador para tapar un elemento que falta. Si el diagnóstico no justifica la IA dentro del servicio, el programa sigue sin ella.

**Cuando no se sabe qué es un buen resultado.** Si el equipo no se pone de acuerdo en qué es una resolución correcta, la IA reproducirá ese desacuerdo a escala.

**Cuando el entorno no está.** Es la regla de entrada del capítulo 18: si las condiciones que la IA necesita no están en el nivel 2 de madurez en el ámbito, por ejemplo porque nadie sabe quién responde de los errores, la IA en el servicio tiene que esperar.

**Cuando la tarea es la relación.** Hay servicios en los que lo que la persona recibe es, precisamente, que otra persona la atienda. Automatizar esa parte puede ahorrar coste y destruir lo que daba valor al servicio.

### Cuándo quitarla

Retirar una IA que ya funciona es más difícil que no ponerla, porque alguien la defendió y alguien la pagó. El método fija señales de retirada desde el diseño: que la tasa de corrección vuelva a subir o se estanque por encima del valor fijado en el diseño; que aparezcan errores en los casos raros que antes resolvían las personas; que el indicador de capacidad baje (capítulo 18); que el coste por tarea completada, incluida la revisión humana, supere al ahorro. Son los mismos indicadores con los que el capítulo 17 revisa cada solución en uso (el uso, la capacidad y el coste por tarea completada), mirados desde la tarea. Una tasa de corrección baja solo tranquiliza si una muestra revisada a ciegas por otra persona confirma la tasa de error, porque también puede querer decir que quien revisa ha dejado de mirar.

Ante cualquiera de esas señales, el dueño de la solución propone bajar de nivel de autonomía o retirarla. Bajar de nivel se decide en una puerta de autonomía, que puede convocarse en cualquier momento. La retirada se firma como cualquier decisión de puerta, y quien la propone queda protegido por escrito (módulo 14 y capítulo 18).

!! Pregunta abierta. ¿Cómo se mide el coste de la revisión humana? | Casi ningún caso de negocio de IA incluye el tiempo que las personas dedican a revisar, corregir y vigilar lo que hace el sistema. Ese tiempo es real y, según Bainbridge, crece con la automatización. Una parte ya es regla: el coste por tarea completada incluye la revisión humana (capítulo 18) y el módulo 24 pide dos medidas de esa revisión. Lo que sigue abierto es cómo medir ese tiempo sin que la medición se vuelva intrusiva. Propuesta: registrarlo durante el piloto por muestreo, con el acuerdo del equipo y leído por equipo y no por persona, y llevarlo al modelo económico.
