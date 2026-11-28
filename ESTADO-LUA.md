# SERIE LÚA · Estado del proyecto (traspaso)

Cuentos para colorear de 4 a 8 años, firmados como Alex Berruezo. Descripción de la serie en `serie-lua.md`.

## Volumen I · «Lúa, la gatita gris» (`libro-lua/`)
- Interior 56 páginas y cubierta dibujada con código. Ficha en `libro-lua/ficha-amazon.md`.
- Pendiente: marcarlo como «Volumen I», añadir las 20 páginas de pasatiempos (módulo listo en `libro-lua2/pasatiempos.py`, función `build(cfg, tit)`) y hacerle cubierta en acuarela como el II para que la serie se vea igual.

## Volumen II · «Lúa y el jardín de todos» (`libro-lua2/`)
- Listo para KDP: `interior-KDP.pdf` (80 páginas, 8,5 x 11 in, sin sangrado) y cubierta en acuarela aplanada a 300 ppp: `cubierta-KDP-papel-blanco.pdf` (17,43 x 11,25 in) y `cubierta-KDP-papel-crema.pdf` (17,45 x 11,25 in). Arte en `libro-lua2/arte/`.
- Ficha completa en `libro-lua2/ficha-amazon.md` (subtítulo, descripción, 7 palabras clave, categorías, precio 8,99 €, declaración de IA). Contenido completo en `libro-lua2/contenido-libro.md` y `.pdf`.
- Raspi es gata (unificado). Regenerar: `python3 libro.py && node render.js && node aplanar_cubierta.js && python3 aplanar_cubierta.py`.
- Última incidencia en KDP: la miniatura de la cubierta salía recortada porque el tamaño de impresión seguía en 6 x 9. Solución indicada: elegir 8,5 x 11, papel blanco, volver a subir interior y cubierta de papel blanco.
- Pendiente de decisión del autor: cambiar «Texto e ilustraciones: Alex Berruezo» de la portadilla, porque las ilustraciones son de IA.

## Volumen III · «Lúa y el vecino nuevo» (`libro-lua3/`)
- Escrito y maquetado. Interior listo: `interior-KDP.pdf` (80 páginas, 8,5 x 11 in). Cubierta en acuarela (Higgsfield) aplanada a 300 ppp: `cubierta-KDP-papel-blanco.pdf` (17,43 x 11,25 in) y `cubierta-KDP-papel-crema.pdf` (17,45 x 11,25 in). Arte en `libro-lua3/arte/`.
- Personaje nuevo: Tilo, el erizo (`erizo.py`). Bicho escondido: Chispa, la luciérnaga. Texto completo en `contenido-libro.md`, ficha en `ficha-amazon.md`.
- Pendiente: que el autor lea y apruebe el cuento; decidir el crédito de la portadilla (ahora solo pone «Alex Berruezo»).
- Regenerar: `python3 libro.py && node render.js && node aplanar_cubierta.js && python3 aplanar_cubierta.py`.

## Preferencias del autor
Español, tono conversacional y directo, sin rayas «—» ni iconos. Decir siempre la verdad y avisar del coste en créditos. No afirmar que lo hecho con IA es humano.
