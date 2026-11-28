# Plan de pruebas (prueba de ejemplo)

Ejecutable: `./scripts/fresh-db.sh && node e2e/cases.js` (26 casos), mas test-api.js, test-backend.js y e2e.js. Todo contra el clon local; nada contra el original.

## F01 Invitado reserva una reunion
- H1 reserva feliz con confirmacion. Cubierto: F01-H1.
- E1 emoji y acentos (F01-E1). E2 nombre de 120 caracteres en movil (F01-E2). E3 XSS en el nombre (F01-E3).
- E4 doble clic (F01-E4). E5 dos pestanas, mismo hueco (F01-E5). E6 sin conexion (F01-E6). E7 recargar a mitad (F01-E7). E8 boton atras tras confirmar (F01-E8).
- E9 enlace inexistente (F01-E9). E10 zona UTC+14 a fin de mes (F01-E10). E11 caracter NUL (F01-E11). E12 saltos de linea en el nombre (F01-E12).
- DST1 y DST2 cambio de hora de primavera y otono (F01-DST1, F01-DST2).
- N1 correo invalido (F01-N1). N2 reserva cancelada (F01-N2). N3 token inexistente (F01-N3).
- No cubierto: sin huecos en 60 dias (probado a mano en la interfaz, sin caso automatico), conexion lenta, lector de pantalla real (solo axe).

## F02 Anfitrion configura y comparte
- H1 guardar horarios (F02-H1). N1 tramo invalido (F02-N1). E1 margen enorme (F02-E1). E2 duracion no numerica (F02-E2).
- No cubierto: conectar calendario y alta/login (no implementados), varios tipos de evento.

## Accesibilidad
- axe en administracion, reserva con formulario y confirmacion (A11Y-1 a 3). Foco visible por teclado (A11Y-4). Reserva completa solo con teclado (e2e.js).
- axe detecta una parte de los problemas; no sustituye una prueba con lector de pantalla.

## Seguridad y datos (test-backend.js y comprobaciones SQL)
- Doble reserva simultanea, RLS entre dos usuarios, tablas de servidor cerradas, limite de peticiones, JSON roto, cuerpo enorme, path traversal, token falso.

## Fuera de alcance de esta prueba
Emails reales, OAuth de calendarios, pagos, F03 y F04 (equipos, routing).
