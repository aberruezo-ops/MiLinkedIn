# Cuaderno de trabajo de Synergós

Synergós (del griego συνεργός, "el que trabaja junto a otro") es el framework que Alejandro Berruezo está construyendo sobre cuatro ejes al mismo nivel: transformación, innovación, inteligencia artificial, y personas y su conocimiento. Su base de partida es un documento interno de método (nombre de trabajo CAUDEX, que no se usa en público).

Este cuaderno es la memoria viva del pensamiento. No es el método terminado: es donde se discute, se verifica y se decide qué entra y qué no. De aquí salen las publicaciones de LinkedIn.

## Archivos

| Archivo | Qué contiene | Cuándo se toca |
|---|---|---|
| `00-tesis.md` | Las tesis centrales de Synergós, numeradas y versionadas. Cada una con su argumento, su evidencia y sus objeciones. | Cuando una idea madura lo suficiente para defenderla en público. |
| `01-preguntas-abiertas.md` | Lo que todavía no sabemos o no hemos decidido. | Cada vez que aparece una duda real. Se cierra cuando se convierte en tesis o se descarta. |
| `02-fuentes.md` | Referencias verificadas: qué dice cada una, qué aporta a Synergós, y qué no dice (para no citarla de más). | Al verificar una fuente. Nada entra sin verificación. |
| `03-backlog-posts.md` | Ideas de publicación derivadas de las tesis, con pilar, ángulo y estado. | Al cerrar un hilo de pensamiento. La rutina de contenido lo lee antes de redactar. |
| `07-perfil.md`, `08-colores.md`, `09-propiedad.md` | Perfil de LinkedIn, estudio de color y precauciones de propiedad y separación del empleo. | Cuando cambian. |
| `04-bitacora.md` | Registro cronológico de cómo evoluciona la idea: qué se discutió, qué cambió y por qué. | Al final de cada sesión de trabajo. |

## Axiomas (no se discuten en cada post; se cumplen)

- **A1. Español de España.** Todos los posts y todo el trabajo del cuaderno se escriben en español peninsular: tú y vosotros, nunca voseo ("tú imaginas", no "vos imaginá"; "pensad", no "piensen"). Léxico de España ("ordenador", "móvil", "vale"). Fijado por Alejandro el 24 oct 2026.
- **A2. Lo humano es la base de la transformación.** Cualquier tesis, post o frase de Synergós tiene que ser coherente con esto.
- **A3. Synergós habla a quien dirige la transformación dentro de la organización**, no a quien la vende.
- **A4. Nada inventado presentado como real.** Los casos compuestos se etiquetan como tales. Las cifras solo si están verificadas en `02-fuentes.md`.
- **A5. En público, siempre Synergós.** Nunca el nombre de trabajo interno.
- **A7. La frase de Synergós (definitiva, 26 oct 2026).** Eslogan: "Crecer a la vez." Subtítulo: "Synergós: personas, conocimiento y tecnología avanzando en el mismo orden." Idea de fondo: la sincronía y la armonía del girasol (cada semilla encuentra su sitio y todas crecen a la vez), que es también el significado del nombre, trabajar junto a otro. Descartados antes: "La transformación es humana. La tecnología solo la acelera." (manido) y "Nada tapa a nada." (críptico). Frases de fondo para los posts: "lo que no está escrito es lo que sostiene todo"; "la transformación es humana". Hashtag de tema principal: #TransformaciónHumana por ahora.
- **A8. Pieza visual por defecto (desde el 3 nov 2026, decisión de Alejandro del 30 oct).** Martes y jueves (Synergós): infografía animada en vídeo MP4 vertical (1080x1350), con la animación de semillas y logo al principio, una escena por idea con sus cifras y fuentes, y cierre con el eslogan; plantilla `imagenes/anim-infografia-B12.html` y generador `imagenes/anim-render.js`. Miércoles (Comunidad): vídeo corto cuadrado (1080x1080, unos 8 s) sobre fondo verde con la animación del logo y la pregunta; plantilla `imagenes/anim-comunidad-C11.html`. Enlaces, si los hay, en el primer comentario. Publora sube MP4 por el mismo circuito que las imágenes (get_upload_url con type video y contentType video/mp4, PUT, complete_media, update_post). LinkedIn no reproduce GIF animados: siempre MP4. Las tarjetas estáticas y el carrusel PDF quedan como alternativa manual.
- **A9. Paleta de Synergós (definitiva, 26 oct 2026).** Paleta "Ángulo áureo" del estudio `08-colores.md`: tinta cálida #1F1D1A para texto y tinta del logo; verde #2C6D3F para el acento (el "gó", el arco, la franja), que es el matiz de 137,5 grados en el círculo cromático, el mismo ángulo del acento; sobre fondo de tinta el verde se aclara a #7CC090; fondo claro #F4F6F6. Segundo acento, solo para gráficos: el complementario #943879. Se probaron y descartaron antes magenta, azul marino, ciruela, marrón de girasol, verde oscuro y albero, granate y aguamarina. Tipografía: Fraunces (OFL) vectorizada para el logo; textos de apoyo en DejaVu Serif y DejaVu Sans.
- **A10. Separación del empleo.** Synergós se trabaja en tiempo, medios y cuentas propios; no usa material, nombres ni clientes de la empresa; es divulgación y posicionamiento, no un servicio en venta mientras dure el empleo. Detalle y precauciones en `09-propiedad.md`. Fijado el 26 oct 2026.
- **A11. Los tres elementos de Synergós: personas, conocimiento y tecnología.** Son tres y no dos porque el conocimiento no vive solo en las personas: vive en ellas (tácito, Polanyi), en la organización (procesos, rutinas, documentos; Nelson y Winter) y en la tecnología misma (un modelo de IA es conocimiento codificado sin nadie que lo sepa). La pregunta central de toda transformación es qué pasa con el conocimiento: si sale de las personas hacia los sistemas (automatizar), si se queda y crece en ellas con ayuda de la tecnología (informar, Zuboff) o si se pierde por el camino. Esa pregunta solo existe si el conocimiento tiene nombre propio. Nunca se habla de "gestionar" el conocimiento, sino de dónde vive y a dónde va. Fijado por Alejandro el 26 oct 2026 tras objetar que personas y conocimiento son uno.
- **A6. Hashtags.** Al final del post, nunca dentro de las frases. Cinco como máximo. Dos fijos en todos los posts: `#Synergos` (sin tilde, para que coincida con cómo lo escribirá la gente) y `#TransformaciónDigital` (añadido por Alejandro el 30 oct 2026 para atraer a quien busca ese tema), más dos o tres de tema. En el texto, la grafía sigue siendo Synergós con tilde.

## Reglas del cuaderno

1. Ninguna cifra ni cita entra sin estar verificada en `02-fuentes.md`. Si no se pudo verificar, se marca así.
2. Las tesis se numeran y no se borran: se versionan. Si una cambia, queda el rastro de por qué.
3. Cada tesis lleva sus objeciones. Una tesis sin objeción escrita no está lista.
4. El caso ilustrativo del operador logístico del documento base es inventado. Si se usa, se dice.
5. En público, siempre Synergós. Nunca el nombre de trabajo interno.
