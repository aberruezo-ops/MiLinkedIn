# Lúa, la gatita gris (volumen I de la serie)

Mismo formato que el volumen II (`libro-lua2/`): tipografía Fraunces, maquetación, pasatiempos y cubierta en acuarela.

Listos para KDP: `interior-KDP.pdf` (76 páginas, 8,5 x 11 in, sin sangrado) y cubierta aplanada a 300 ppp: `cubierta-KDP-papel-blanco.pdf` y `cubierta-KDP-papel-crema.pdf`. Datos de la ficha en `ficha-amazon.md`.

Regenerar todo:

    python3 libro.py && node render.js && node aplanar_cubierta.js && python3 aplanar_cubierta.py

`lib.py`, `animales.py`, `jardin.py`, `pasatiempos.py` y las fuentes son copias de las del volumen II (los cambios de uno conviene llevarlos al otro). `pasatiempos.py` admite `retos_titulo` en la configuración.

Cubierta: ilustraciones de Higgsfield (gpt_image_2_6, con la portada del volumen II como referencia) escaladas a 4k. Portada job 76bc23ce-43ef-4f50-a183-4dda75aa0337 (escalado cba2c918-6ab1-4860-bbfc-eec48930e1bb); contraportada job 571f1071-a73f-49ca-956a-dbe25b68fd67 (escalado 5772ae3d-551e-4ed2-b7f7-28c4a9de7114). En `arte/`.
