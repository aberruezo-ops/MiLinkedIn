# Lúa y el jardín de todos (libro 2 de la serie)

Listos para KDP: `interior-KDP.pdf` (56 paginas, 8,5 x 11 in) y `cubierta-KDP.pdf` (tapa completa con lomo).
Textos en `escenas.py` (TEXTOS), autor y titulo en `libro.py`. Regenerar:

    python3 libro.py && node render.js

## Cubierta en acuarela
Ilustraciones generadas con Higgsfield (gpt_image_2_6) y escaladas a 4k: portada job e3703650-0e83-40fc-a570-1513e3d025c1 (escalado 6de4208d-eb45-4a90-8bf0-05abb6cd2ed3), contraportada job f90406c4-53ad-4547-b3e0-d9c613ca4c77 (escalado 9a9da9ce-82b2-43f4-b184-de9df1f0925c). Están en `arte/`. Si existe `arte/portada-acuarela.jpg`, `libro.py` usa `cubierta_acuarela()`; si no, la cubierta dibujada con código.
Datos para KDP en `ficha-amazon.md`.

## Cubierta aplanada (la que se sube a KDP)
Tras `python3 libro.py && node render.js`, ejecutar `node aplanar_cubierta.js && python3 aplanar_cubierta.py`. Genera `cubierta-KDP.pdf` como una sola imagen a 300 ppp (17,43 x 11,25 in para 80 páginas) y `portada-frontal.jpg`. Todo el texto queda al menos a 0,25 in del corte.
