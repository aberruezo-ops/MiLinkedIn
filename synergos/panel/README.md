# Panel de agentes del método

Cuatro agentes con roles distintos leen el método Synergós y devuelven críticas y propuestas para evolucionarlo. Nada se cambia en el método sin que lo apruebe Alejandro.

## Roles

Cada rol es un agente de proyecto en `.claude/agents/`:

| Agente | Mira el método desde |
|---|---|
| panel-direccion-finanzas | Dirección general y finanzas: valor, plazos, retorno |
| panel-quien-hace-el-trabajo | Responsable de equipo y primera línea: aplicabilidad y respeto |
| panel-sector-publico-cumplimiento | Administración, jurídico y riesgos: normativa, contratación, auditoría |
| panel-academico-metodologo | Academia y método: coherencia, evidencia, huecos |

## Cómo se lanza una ronda

1. Se lanza cada agente con el encargo "evalúa la versión X del método" y la ruta de salida `synergos/panel/ronda-N/<agente>.md`. Se pueden lanzar los cuatro en paralelo.
2. Cuando vuelven, se sintetizan en `synergos/panel/ronda-N/00-sintesis.md`: qué coincide entre roles, qué choca, y propuestas ordenadas por aporte, marcadas como CAMBIO, AÑADIDO o ACLARACIÓN.
3. Alejandro decide qué entra. Lo aprobado se incorpora a la versión siguiente y se anota en el anexo F.

## Coste

Cada agente lee entre 150.000 y 250.000 caracteres del método. Una ronda de cuatro cuesta unas cuatro veces eso. Para una revisión más barata, pedir a cada agente que lea solo los capítulos de su rol y el anexo F.

## Reglas

- Los agentes solo leen. Escriben únicamente su informe.
- Un agente no sustituye a una persona del perfil: da una lectura plausible desde ese rol y sirve para encontrar huecos, no para validar.
- Ninguna cifra de un informe entra en el método sin leerse en la fuente.
- Es conveniente contrastar las críticas más duras con alguien real de cada perfil.
