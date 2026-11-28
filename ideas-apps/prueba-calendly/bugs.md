# Bugs (reproducidos con e2e/cases.js, contra Postgres local)

Sin S1 ni S2. Los 7 son S3: tienen solucion alternativa o afectan a entradas poco comunes. Estado al final del documento.

## B1 (S3) El calendario abre en un mes sin huecos para invitados con zona adelantada
Caso: F01-E10. Pasos: invitado con zona Pacific/Kiritimati (UTC+14) abre la pagina el 31-mar-2027 a las 09:30Z. Esperado: el calendario muestra abril, donde estan los huecos. Actual: abre en marzo sin ningun dia libre. Causa: el mes inicial se calcula en UTC, no en la zona del invitado. Evidencia: "el calendario abre en marzo de 2027 sin ningun dia libre". Solucion alternativa: pulsar la flecha del mes siguiente.

## B2 (S3) Un dia entero desaparece al consultar justo antes del cambio de hora de primavera
Caso: F01-DST1. Pasos: pedir huecos con `from` = 28-mar-2026 22:30Z para un anfitrion en Europe/Madrid con horario los domingos. Esperado: 2 huecos el domingo 29 (dia del cambio de hora). Actual: 0. Causa: el recorrido de dias avanza en bloques de 24 h UTC y salta un dia local cuando la hora local de partida esta entre las 23:00 y las 24:00 antes del cambio. Ventana estrecha (una hora al ano por zona), pero afecta a la disponibilidad real. Solucion alternativa: recargar mas tarde.

## B3 (S3) Un caracter NUL en el nombre provoca error 500
Caso: F01-E11. Peticion: POST /api/book con name "A\u0000B". Esperado: 201 o 422. Actual: 500 (`invalid byte sequence for encoding "UTF8": 0x00` de Postgres). Solo por API; el formulario no lo permite escribir. Solucion alternativa: no enviar ese caracter.

## B4 (S3) Saltos de linea en el nombre llegan al asunto del email
Caso: F01-E12. Peticion: name "Eva\r\nBcc: x@evil.com". Actual: el asunto de la cola de emails contiene CR/LF. Hoy el proveedor es simulado, pero con un proveedor SMTP seria inyeccion de cabeceras. Se registra como S3 porque no hay envio real; pasaria a S1 con SMTP si no se corrige.

## B5 (S3) Un margen enorme en el tipo de evento provoca error 500
Caso: F02-E1. Peticion: PUT /api/admin/event-type con buffer_after_min 99999999999. Actual: 500 (`out of range for type integer`). La ruta de admin esta abierta a todos (no hay auth), asi que cualquiera podria provocarlo.

## B6 (S3) Un nombre largo sin espacios desborda la confirmacion en movil
Caso: F01-E2. Nombre de 120 "W" a 390 px: scroll horizontal en /confirmacion. Causa: el texto del invitado no tiene `overflow-wrap`.

## B7 (S3) El calendario no es una rejilla ARIA valida
Caso: A11Y-2. axe: `aria-required-children` (critical): role="grid" con botones sin filas ni celdas. Los lectores de pantalla pueden anunciar mal el calendario.

## Por comprobar (no reproducido)
- El mapa de intentos del limite de peticiones crece sin purga (`hits` en server.js): no se pudo reproducir con varias IP desde localhost. Se arregla igualmente por ser trivial.
- Rutas de administracion sin autenticacion: ya documentado en backend.md; no es un bug nuevo sino una pieza pendiente.

## Estado
B1 a B7: corregidos. Cada uno tenia su caso fallando antes (e2e/cases.js) y ahora pasa. Suite completa en verde tras los arreglos: test-api (Postgres y memoria), test-backend, e2e.js y e2e/cases.js (26/26).
- B1: mes inicial calculado en la zona del invitado (public/book.html, initMonth).
- B2: slots.js recorre dias locales civiles en lugar de bloques de 24 h.
- B3 y B4: el nombre pierde caracteres de control y espacios repetidos antes de guardarse (server.js).
- B5: margenes limitados a 0..1440 minutos, 422 si se pasan.
- B6: overflow-wrap en las tarjetas (app.css).
- B7: role="group" con etiqueta en lugar de role="grid".
No hay commits: esto vive en el scratchpad de la prueba, no en un repositorio.
