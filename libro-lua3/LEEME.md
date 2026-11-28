# Lúa y el vecino nuevo (libro 3 de la serie)

Listos para KDP: `interior-KDP.pdf` (80 páginas, 8,5 x 11 in, sin sangrado) y cubierta en acuarela aplanada a 300 ppp: `cubierta-KDP-papel-blanco.pdf` (17,43 x 11,25 in; `cubierta-KDP.pdf` es la misma) y `cubierta-KDP-papel-crema.pdf` (17,45 x 11,25 in). `portada-frontal.jpg` es la portada sola.

Textos de las escenas en `escenas.py` (TEXTOS); Tilo y los decorados nuevos en `erizo.py`; portadilla, guía, actividades, pasatiempos y cubierta en `libro.py`. Regenerar:

    python3 libro.py && node render.js && node aplanar_cubierta.js && python3 aplanar_cubierta.py

## Cubierta en acuarela
Ilustraciones generadas con Higgsfield (gpt_image_2_6, con la portada del volumen II como referencia de estilo) y escaladas a 4K: portada job d56841dc-a4f3-45c2-abd4-85219cb89b1a (escalado a7f2fc93-b2f6-4c19-a33c-b11913124dc2), contraportada job 19c43ab9-a3ef-41e3-a9c1-c6abf31de8cb (escalado 5f10b97c-182a-49c8-b10a-9a93b61d5cc4). Coste: 0,75 + 0,75 + 2 + 2 = 5,5 créditos. Están en `arte/`. Si se borran, `libro.py` vuelve a la cubierta dibujada con código.
