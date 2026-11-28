# Lúa y el vecino nuevo (libro 3 de la serie)

Interior listo para KDP: `interior-KDP.pdf` (80 páginas, 8,5 x 11 in, sin sangrado). Cubierta provisional dibujada con código: `cubierta-KDP.pdf` (17,43 x 11,25 in, aplanada a 300 ppp) y `portada-frontal.jpg`.

Textos de las escenas en `escenas.py` (TEXTOS); Tilo y los decorados nuevos en `erizo.py`; portadilla, guía, actividades, pasatiempos y cubierta en `libro.py`. Regenerar:

    python3 libro.py && node render.js && node aplanar_cubierta.js && python3 aplanar_cubierta.py

## Cubierta en acuarela (pendiente)
Si se guardan `arte/portada-acuarela.jpg` y `arte/contraportada-acuarela.jpg`, `libro.py` usa `cubierta_acuarela()` con la misma maqueta que el volumen II. Sin esas imágenes usa la cubierta dibujada con código.
