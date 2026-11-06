# Parte II. La arquitectura

## 5. Tres elementos y un orden

Synergós se apoya en tres elementos: personas, conocimiento y tecnología. Y en un cuarto componente, el orden, que es lo que hace que los tres crezcan a la vez.

{{img:fig-arquitectura.png|15}}

### Por qué tres y no dos

La objeción más frecuente, y la primera que me hice yo, es que personas y conocimiento son lo mismo: el conocimiento está en las personas. Es verdad en parte, y por eso la respuesta importa.

El conocimiento vive en tres sitios. Vive en las personas, en lo que saben hacer y a menudo no saben explicar; es lo que Michael Polanyi resumió en 1966 con la frase "podemos saber más de lo que podemos decir". Vive en la organización, en sus rutinas, sus procedimientos y su manera de hacer las cosas, que es lo que Richard Nelson y Sidney Winter describieron en 1982 como la memoria de la organización. Y desde hace poco vive también en la tecnología: en los datos, en los modelos y en los sistemas que deciden o proponen.

La decisión central de cualquier transformación es a dónde va ese conocimiento. Si se queda en la persona y la tecnología la ayuda, si pasa al sistema de una forma que se pueda revisar, o si se pierde. Fundir conocimiento con personas borra esa decisión y devuelve el discurso al manido "personas y tecnología", en el que la tecnología acaba ganando siempre porque es la que tiene presupuesto. Separarlo obliga a mirarlo.

### Qué agrupa cada componente

| Componente | Qué agrupa |
|---|---|
| Personas | Liderazgo; roles, carreras e incentivos; seguridad psicológica; interacción con quien hace el trabajo y con quien recibe el servicio; quién enseña lo que la tarea enseñaba |
| Conocimiento | El explícito (datos con dueño, base curada, registro de decisiones); el tácito (el mapa de lo que nadie escribió); el aprendizaje del propio programa (supervisión de doble bucle) |
| Tecnología | La IA en sus dos papeles, la frontera, la escala de autonomía, el entorno que exige; las demás tecnologías (plataforma, automatización, entrega continua); el radar de lo emergente; la medida justa |
| El orden | Las cinco fases y sus puertas; estrategia; gobierno; modelo económico; medición y el delta; madurez y regla de entrada; dimensionamiento del programa; la marcha atrás |

### La regla que protege la arquitectura

No se compra un acelerador para tapar un elemento que falta. Un agente de IA que resuelve consultas acelera la escala de un servicio. Pero si nadie ha decidido quién responde de sus errores ni cómo cambia el trabajo de quienes resolvían antes esas consultas, se queda en piloto, y ninguna mejora del agente lo arregla. El fallo está en personas y en gobierno. Comprar una versión mejor del agente es pagar dos veces por no haber mirado.

## 6. Los seis principios

Los principios son las reglas que se aplican cuando el método no dice nada concreto. Son seis y cada uno tiene su fuente y su riesgo.

### Principio 1. Diagnóstico antes que solución

Nada entra en diseño sin una restricción nombrada y una línea base medida. Richard Rumelt lo explicó con precisión en 2011: una buena estrategia empieza por un diagnóstico que simplifica la realidad hasta encontrar el problema crítico. La mayoría de lo que se llama estrategia es una lista de objetivos sin diagnóstico. Eliyahu Goldratt añadió en 1984 la idea de restricción: en todo sistema hay un punto que limita el rendimiento del conjunto, y mejorar cualquier otro punto no mejora nada.

En la práctica, este principio choca con algo muy humano: casi todos los proyectos llegan con la solución ya decidida. En treinta años de trabajo, la mayoría de las conversaciones que he tenido sobre transformación empezaban con una herramienta en la mesa. El principio no prohíbe tener una idea de solución. Prohíbe aprobarla antes de saber qué problema resuelve.

*Riesgo del principio:* convertirse en una excusa para no actuar. Un diagnóstico que dura seis meses es otra forma de no decidir. Por eso el diagnóstico tiene entregables cerrados y una puerta, no un plazo indefinido.

### Principio 2. Elemento antes que acelerador

Un acelerador entra en una fase solo si los tres elementos están, para esa fase, al menos en el nivel 2 de madurez. La escala de madurez se explica en el capítulo 18. Lo importante aquí es la lógica: un acelerador multiplica lo que encuentra. Si encuentra un equipo que no sabe para qué sirve la herramienta, multiplica la confusión.

*Riesgo:* que la escala de madurez se convierta en un examen burocrático. La evaluación tiene que durar horas, no semanas, y hacerse con quien trabaja, no sobre quien trabaja.

### Principio 3. Pocas cosas a la vez

La IA se planifica en todas las fases. Además, uno o dos aceleradores por fase: los que atacan la restricción. Un programa que activa a la vez la IA, una plataforma nueva, un rediseño de procesos, un cambio de estructura y un nuevo modelo de medición no está transformando nada; está generando ruido que nadie puede atribuir.

### Principio 4. Puertas con criterios fijados antes

Los criterios de cada puerta se escriben al empezar la fase, no al terminarla. Es la diferencia entre decidir con evidencia y justificar lo que ya ha pasado. Robert Cooper formalizó en 1990 los procesos de puertas para el desarrollo de productos, y la lección central sigue valiendo: una puerta sin criterios previos es una reunión de seguimiento con otro nombre.

### Principio 5. Nada nuevo encima de lo no mirado

Es el principio del girasol, y se explica en el capítulo siguiente. Cada iniciativa se coloca donde no haga sombra a las personas ni a lo que ya funcionaba. Antes de poner algo nuevo encima, hay que haber mirado lo que hay debajo.

### Principio 6. El método se supervisa a sí mismo

Si una pieza del método no aporta en un programa, se retira de ese programa. Y si no aporta en varios, se retira del método. Este principio es el que da a Synergós su vocación de mejora continua, y tiene un capítulo propio al final.

## 7. El girasol: por qué 137,5 grados

El logo de Synergós lleva un acento girado 137,5 grados, y el verde de la marca es ese mismo ángulo trasladado al círculo cromático. No es decoración. Es el símil del método, y conviene explicar bien qué dice y qué no.

En la cabeza de un girasol, cada semilla nueva nace girada unos 137,5 grados respecto a la anterior. Es el llamado ángulo áureo: la vuelta completa dividida según la proporción áurea. Helmut Vogel propuso en 1979 un modelo matemático muy sencillo que reproduce la disposición: cada semilla se coloca a ese ángulo y a una distancia del centro que crece con la raíz cuadrada de su número de orden. El resultado es una cabeza llena, sin huecos y sin que ninguna semilla tape a otra. En 1992, Stéphane Douady e Yves Couder mostraron con un experimento físico, gotas de ferrofluido que caen a intervalos regulares en el centro de un plato con aceite, bajo un campo magnético, y se repelen entre sí, que el patrón emerge solo de una regla local: cada elemento nuevo se coloca donde menos le estorban los anteriores.

{{img:fig-girasol.png|10}}

De ahí salen tres lecturas que el método usa.

La primera: **el orden no lo pone nadie desde arriba**. Sale de cómo se coloca cada elemento nuevo respecto a los que ya están. En una transformación, la calidad del conjunto depende de la regla con la que entra cada iniciativa, no de un plan maestro que lo prevé todo.

La segunda: **nada tapa a nada**. Cada semilla encuentra su sitio sin quitarle el suyo a la anterior. En una organización, cada iniciativa nueva tiene que encontrar su sitio sin hacer sombra a las personas ni a lo que ya funcionaba. Cuando una iniciativa tapa a otra, el método pide que se diga, se mida y se decida a propósito.

La tercera: **crecer a la vez**. La cabeza del girasol no crece por zonas. Crece entera, desde el centro, manteniendo la proporción. Es la promesa de Synergós.

*Lo que el símil no dice.* La filotaxis no es una prueba de que las organizaciones funcionen así. Vogel y Douady y Couder describen plantas y gotas, no empresas. El girasol es una imagen que ayuda a pensar y a recordar, no un argumento. Y tiene un límite que conviene reconocer: en un girasol nada se retira, mientras que en una organización a veces lo correcto es quitar algo para que lo demás crezca. El método lo prevé (la marcha atrás, la retirada en la puerta), pero el símil no lo cuenta. Si algún día la metáfora empieza a pesar más que el contenido, habrá que soltarla.
