# Animación promocional de AR3 (3D con Three.js)

Escena 3D en HTML con Three.js: un diorama con bolas blancas y una bola negra, carteles dibujados dentro de la propia escena (texturas de canvas) y semillas en espiral de Vogel (137,5°). Texto y logo de cierre superpuestos en HTML. Nada de imágenes ni vídeo de la película.

Pipeline (el mismo que se usó en otro proyecto):
1. `scene.js` se empaqueta con esbuild: `NODE_PATH=<node_modules con three> esbuild scene.js --bundle --minify --format=iife --outfile=bundle.js` (three 0.160.0, esbuild 0.19.12; `bundle.js` no se versiona).
2. `capture.js` abre `index.html` con Playwright y Chromium (WebGL por software con SwiftShader), recorre el tiempo fotograma a fotograma y guarda JPG (720 x 1280, 25 fps). Una versión de 18,5 s tarda unos 80 s en este contenedor.
3. ffmpeg monta los fotogramas en H.264, calidad 28, sin audio: `../anim-promo-AR3.mp4`.

Textos de los carteles (en `scene.js`, objeto `signs`): La bola negra: quién decide quién cabe / Bola blanca: cabe. Bola negra: no cabe. / Nadie explica el voto. / Antes de votar: ¿a quién deja fuera esta opción? Cierre común: logo y "Crecer a la vez."
