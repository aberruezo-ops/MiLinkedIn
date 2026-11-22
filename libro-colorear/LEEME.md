# Libro para colorear: Teo y las pelotas de colores

Archivos listos para KDP: `interior-KDP.pdf` (40 paginas, 8,5 x 11 in) y `cubierta-KDP.pdf` (tapa completa con lomo).

Para cambiar algo: editar `libro.py` (titulo, autor, anio), `escenas.py` (dibujos y textos de cada escena) y ejecutar:

    python3 libro.py && node render.js

El grosor del lomo se calcula en `libro.py` (GROSOR_PAPEL). Verificalo con la calculadora de portadas de KDP al elegir papel.
