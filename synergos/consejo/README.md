# Consejo de seis perspectivas

Para decisiones de verdad (precio, contratar o automatizar, aceptar un cliente, abrir una línea, elegir un socio) en las que un solo punto de vista tiende a darte la razón. En vez de preguntar a uno, se pregunta a seis con miradas distintas y se pide un único veredicto. Idea tomada de una infografía ajena que Alejandro compartió el 25 nov 2026; los roles, los nombres y el formato son propios (A21: no se reutilizan diseños ni imágenes ajenos).

## Los seis (agentes en `.claude/agents/`)

| Agente | Mira |
|---|---|
| consejo-abogado-del-diablo | Qué sale mal, y qué supuesto lo hundiría |
| consejo-desde-cero | Si la pregunta está bien planteada |
| consejo-numeros | Cuánto cuesta, cuánto deja y qué dato falta |
| consejo-oportunidad | Qué se pierde por ir a lo seguro |
| consejo-mirada-externa | Lo que quien llega de fuera ve y tú ya no |
| consejo-ejecucion | Si se puede hacer y cuál es el primer paso |

## Cómo se usa

Escribir en la conversación: «Consulta al Consejo:» y la decisión, con el contexto mínimo (qué se decide, plazo, qué hay en juego). Claude lanza los seis agentes en paralelo con el mismo texto y sintetiza un veredicto con cuatro bloques:

1. Donde coinciden.
2. Donde chocan.
3. Lo que nadie miró.
4. La recomendación, con la condición que la haría cambiar.

## Cuándo no usarlo

Datos sueltos, resúmenes, redactar un correo o decisiones pequeñas y reversibles: no compensa. Cada consejero es corto (unas 150 palabras), pero son seis lanzamientos más la síntesis. Para una consulta más barata, pedir solo tres miradas (por ejemplo abogado del diablo, números y ejecución).

## Límites

El consejo son seis voces simuladas por el mismo modelo: sirven para encontrar lo que no se ha mirado, no para validar la decisión ni sustituir a personas reales. Ninguna recomendación se ejecuta sin aprobación de Alejandro.
