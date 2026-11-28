# Marca (prueba de ejemplo)

Angulo: "Si ya te atraparon en una suscripcion, aqui se cancela en un clic y te contesta una persona" (fixes.md, opcion C, con plan gratuito claro). Ojo: ese angulo sale de una sola fuente sesgada hacia lo negativo (ver fixes.md).

## El nombre
Veinte candidatos pasados por el filtro de parecido (sonido, aspecto, significado) con el original y con nombres de la categoria que conozco. No incluyo ninguno acabado en "-ly" ni juegos con el nombre del original. Los cinco finalistas, **sin ninguna comprobacion hecha**:

| # | nombre | estilo | por que |
| --- | --- | --- | --- |
| 1 | **Citaclara** | compuesto | "cita" mas "clara": promete reservas y cobros sin letra pequena. Recomendado: es distintivo y encaja con el angulo. |
| 2 | Huecoabierto | compuesto | huecos disponibles, largo de escribir. |
| 3 | Quedamos | verbo | "quedar" es como se dice en España citarse con alguien; muy cercano, pero palabra comun: dificil de registrar y probablemente muy usada. |
| 4 | Abrehora | compuesto | acción de abrir un hueco; suena menos natural. |
| 5 | Tuhora | descriptivo | corto, pero generico y facil de confundir. |

### Comprobaciones: TODAS POR HACER
Desde este entorno no puedo consultar registros de marcas ni de dominios, asi que **no afirmo que ningun nombre este libre**. Para cada uno de los cinco:

| comprobacion | donde | estado |
| --- | --- | --- |
| Marca EE. UU. | tmsearch.uspto.gov, clases 9 y 42 | por hacer |
| Marca UE | euipo.europa.eu eSearch o TMview (incluye la OEPM) | por hacer |
| Marca España | sede.oepm.gob.es | por hacer |
| Global | WIPO Global Brand Database | por hacer |
| Dominio | .com, .es y .app en el registrador | por hacer |
| App Store y Google Play | buscar el nombre exacto | por hacer |
| Perfiles | X, Instagram, TikTok, GitHub | por hacer |
| La web | buscar "nombre + agenda/reservas" | por hacer |

Son comprobaciones de cribado, no autorizacion legal. Antes de gastar dinero en el nombre, conviene que un abogado de marcas haga una busqueda seria.

## Paleta
Roles identicos a replica-design, valores propios. Familia de color distinta de la del original (el suyo es azul marino sobre blanco roto; el nuestro, ciruela sobre hueso calido).

| rol | valor |
| --- | --- |
| bg | #f7f4ee |
| surface | #ece7dc |
| border | #d8d0bf |
| border-input | #7a7262 |
| text | #231b26 |
| text-muted | #58505b |
| accent | #7a2e74 |
| on-accent | #ffffff |
| danger / success / warning | #b42318 / #1a6b43 / #8a5a00 |

Contraste: 11 pares comprobados, 0 fallos AA (texto sobre fondo 15,2:1; acento sobre fondo 7,7:1; borde de campos 4,3:1 frente al minimo de 3:1).

Un detalle que corregi: en la primera version de los tokens use el fondo (#fcfbf8) y el azul marino de texto (#071a31) medidos de la web del original, y las sombras tambien llevaban ese marino en rgba(). El barrido lo detecto en el CSS pero **no detecta colores escritos como rgba()**, asi que las sombras las encontre a mano. Si añades colores, mira tambien ese formato.

## Brief del logo (no es un logo)
- Idea: una cita o hueco que se abre sin esfuerzo. Un monograma o simbolo sencillo que sugiera un "check" dentro de un hueco o un cuadrado de calendario con una esquina abierta.
- Tipo: simbolo mas wordmark "Citaclara".
- Debe funcionar a 16 px (favicon) y como icono de 1024 px.
- Entregables: SVG, icono de app 1024x1024 sin transparencia (iOS), juego de favicons, imagen social 1200x630.
- **No debe parecerse al original.** En mi captura de su web se ve un icono redondeado en azul con una letra C en el interior: nada de forma redondeada con una C dentro, nada de azul. Poner su logo al lado de los borradores antes de aprobar. No lo he copiado ni reproducido; lo describo solo de una captura de baja resolucion.

## Voz
Tres palabras: **directa** (sin rodeos, pero sin brusquedad), **cercana** (de tu a tu, sin cursileria), **clara** (cada cosa con su nombre, sin infantilizar).

| si | no |
| --- | --- |
| "Cancela aqui, sin escribir a nadie." | "Para gestionar tu reserva, contacta con nuestro equipo." |
| "Ese horario acaba de ocuparse." | "Se ha producido un error al procesar la solicitud." |
| "No quedan huecos en los proximos 60 dias." | "No hay disponibilidad." |
| "Dinos cuando estas libre." | "Configure su disponibilidad." |
| "Tu reserva esta confirmada." | "¡Genial! ¡Todo listo! 🎉" |

Cadenas reescritas en la app: subtitulo de la agenda, estado vacio sin huecos, aviso de cancelacion en la confirmacion, y titulos de pagina. El resto de cadenas ya eran de redaccion propia (las escribi desde cero en replica-build).

## Barrido
`python3 sweep.py . --config ../brand.json` sobre replica/app: **limpio**. Antes de cambiar la paleta encontro 2 colores del original. Pendiente de revisar a ojo: favicon (no hay), imagen social (no hay), plantillas de email (texto plano, sin marca), icono de app (no hay).
