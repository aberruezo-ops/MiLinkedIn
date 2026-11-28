# Backend (prueba): estado real

Verificado aqui, con Postgres 16 local. NO conectado: auth, calendarios externos, email real, pagos.

## Hecho y probado
- Migraciones versionadas (001 esquema, 002 cola de emails, 003 RLS restante) con script que aplica cada una una vez. Seed con datos ficticios.
- Persistencia en Postgres: las reservas sobreviven a un reinicio del servidor.
- Anti doble reserva en la base: 5 reservas simultaneas del mismo hueco = 1 confirmada y 4 rechazadas, contra la exclusion constraint.
- Acceso (RLS), probado con un rol sin privilegios y dos anfitriones: cada uno solo ve y modifica lo suyo; no puede insertar datos a nombre de otro; sin sesion no ve nada; las tablas de servidor (email_outbox, reminders, webhook_events) estan cerradas a clientes.
- Cola de emails: confirmacion al invitado y al anfitrion, sin duplicados (unique por reserva y tipo), reintentos con espera creciente, y "dead letter" tras 5 fallos. Proveedor SIMULADO: no se ha enviado ningun correo real.
- Limite de peticiones en /api/book (por IP, en memoria): a partir de la 4.ª en un minuto devuelve 429 (configurable con RATE_BOOK).
- Validacion en servidor de todas las entradas; JSON roto y cuerpos grandes rechazados; path traversal bloqueado.
- npm audit: 0 vulnerabilidades (unica dependencia: pg).

## Sin conectar (lo debe hacer el usuario con sus cuentas)
- Auth: sin registro, verificacion de email, recuperar clave ni sesiones. Las rutas /api/admin/* estan ABIERTAS: no usar fuera de pruebas.
- Google Calendar y Microsoft Graph: sin OAuth ni sincronizacion. Google exige verificacion de la app para scopes de Calendar antes del lanzamiento publico y tarda semanas: conviene empezarla pronto.
- Email real (Resend): falta implementar el envio con la clave del usuario y configurar SPF/DKIM en su dominio.
- Pagos (Stripe): no implementado; son funciones opcionales ("could").
- Recordatorios: la tabla existe, pero no hay trabajo programado que los genere.
- Reprogramar reserva: no implementado.
- Borrado de cuenta e invitado (RGPD): no implementado.

## Limites conocidos
- El limite de peticiones es en memoria y por instancia; con varias instancias hay que usar un almacen compartido, y detras de un proxy hay que tomar la IP real del proxy de confianza.
- El trabajo de la cola asume UN solo proceso; con varios habria que reclamar los trabajos dentro de una transaccion.
- Los tokens de calendario se guardan cifrados "en la app", pero ese cifrado no esta escrito todavia.

## Checklist de seguridad
- [x] secretos solo en variables de entorno, .env* en .gitignore (hay .env.example sin valores)
- [x] entrada validada en servidor en cada ruta
- [x] autorizacion en lectura y escritura, probada con un segundo usuario (a nivel de base de datos)
- [ ] autorizacion en las rutas de la API: no hay auth, las rutas de admin estan abiertas
- [x] limite de peticiones en la reserva (el registro y el login no existen todavia)
- [ ] webhooks con firma: no hay webhooks implementados
- [ ] subidas de archivos: no aplica por ahora
- [x] sin datos de usuario en URLs: el token de gestion si va en la URL de confirmacion (decision pendiente: es necesario para el enlace del email, pero hay que evitar registrarlo en logs)
- [x] dependencias auditadas
- [ ] politica de privacidad: pendiente

Nota: la pagina publica /confirmacion?t=TOKEN pone el token en la URL; es un secreto de acceso a esa reserva.
