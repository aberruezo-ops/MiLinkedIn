# Arquitectura: clon de scheduling (prueba basada en el recon de Calendly)

Fuente: replica/recon.md y features.csv. Ojo: el recon tiene pantallas y campos inferidos, asi que lo marcado "por verificar" puede cambiar el esquema.

## Stack

| capa | eleccion | por que |
| --- | --- | --- |
| web | Next.js (App Router) + TypeScript | pagina publica de reserva con SSR y rutas de servidor en un solo repo |
| estilos | Tailwind, tokens de replica-design | |
| base de datos | Postgres en Supabase | la restriccion anti doble reserva es nativa de Postgres |
| ORM | Drizzle | tipos sin ocultar el SQL de la exclusion constraint |
| auth | Supabase Auth (email + Google) | RLS con auth.uid() |
| calendarios | Google Calendar API y Microsoft Graph, con claves propias | solo APIs oficiales |
| email | Resend | confirmaciones y recordatorios |
| pagos | Stripe (solo si se hace "could") | |
| jobs | Vercel Cron cada 5 min | recordatorios y renovacion de tokens |
| hosting | Vercel | |

Una base de datos, sin microservicios.

## Esquema

Ver `schema.sql`: 10 tablas (users, calendar_accounts, availability_rules, teams, team_members, event_types, event_type_hosts, bookings, reminders, webhook_events). Validado en Postgres 16: carga limpio, rechaza solapes del mismo anfitrion y acepta reservas contiguas.

Decisiones:
- `no_double_booking` (exclusion constraint con btree_gist) sobre `host_id` y rango de tiempo, solo para `status='confirmed'`. Es el cierre real de la carrera entre dos invitados.
- Tiempos en `timestamptz`; la disponibilidad semanal se guarda en hora local del anfitrion (`start_local`, `users.timezone`) y se convierte a UTC al calcular huecos, para que el cambio de hora no desplace los horarios.
- `bookings.on delete restrict` hacia event_types y users: no se borra historial por accidente; el borrado RGPD es un proceso explicito.
- Tokens de calendario cifrados en la app, nunca en claro.
- Acceso: RLS de Supabase para el anfitrion. El invitado no tiene cuenta: toda su interaccion pasa por rutas de servidor con service role y `manage_token` (hasta 24 bytes aleatorios) para ver, reprogramar o cancelar.

## API

| metodo ruta | que hace | quien | entrada | salida | flujo |
| --- | --- | --- | --- | --- | --- |
| GET /api/public/[slug]/[event]/slots?from&to&tz | calcula huecos libres | publico | rango y zona del invitado | lista de huecos UTC | F01 |
| POST /api/public/[slug]/[event]/book | crea la reserva | publico | hueco, nombre, email, tz, respuestas | booking + manage_token | F01 |
| GET /api/bookings/[token] | ver reserva | quien tenga el token | token | booking | F01 |
| POST /api/bookings/[token]/cancel | cancela | token | motivo opcional | ok | F01 (por verificar) |
| POST /api/bookings/[token]/reschedule | mueve la reserva | token | nuevo hueco | booking | F01 (por verificar) |
| GET/PUT /api/me/availability | lee y guarda reglas semanales | anfitrion | reglas, buffers, limite diario | reglas | F02 |
| GET/POST/PATCH /api/me/event-types | CRUD de tipos de evento | anfitrion | nombre, duracion, ubicacion | evento | F02 |
| POST /api/me/calendars/connect/[provider] | inicia OAuth | anfitrion | provider | redireccion | F02 |
| GET /api/oauth/[provider]/callback | guarda el calendario | anfitrion | code | ok | F02 |
| POST /api/teams y /api/teams/[id]/members | equipos | anfitrion Teams | | | F03 |
| POST /api/webhooks/google, /microsoft | cambios de calendario | proveedor | notificacion | 200 | F02 |

Jobs: enviar recordatorios (cada 5 min, `reminders.send_at <= now() and sent_at is null`), renovar canales de webhook de calendario, limpiar `webhook_events` de mas de 30 dias.

## Las partes que muerden

- Zonas horarias y cambio de hora: se calcula siempre en la zona del anfitrion y se muestra en la del invitado; probar con las dos fechas de cambio de hora.
- Carrera de reservas: la constraint es la autoridad; la API debe capturar el error y devolver "ese hueco acaba de ocuparse" con huecos nuevos.
- Idempotencia: los webhooks de Google y Microsoft llegan duplicados; `webhook_events` deduplica. El POST de reserva acepta una clave de idempotencia del cliente.
- Sincronizacion de calendarios: caducidad de tokens y de canales de webhook; si el calendario falla, no ofrecer huecos que no se pueden verificar.
- Conflictos con eventos externos: la constraint solo ve las reservas propias; los eventos del calendario externo se consultan al calcular huecos y se vuelven a comprobar justo antes de confirmar.
- Entregabilidad del email: SPF/DKIM antes de abrir a usuarios reales.
- Limites de tasa de Google y Microsoft: cachear lecturas de ocupado unos minutos.
- RGPD: borrado de invitado por email, con `bookings` anonimizadas, no borradas.

## Orden de construccion

1. **Rebanada vertical** (pantallas S06 a S09, S03, S05; tablas users, availability_rules, event_types, bookings; rutas slots, book): un anfitrion fijo con disponibilidad, un evento, y un invitado reserva sin calendario externo. Prueba la constraint y las zonas horarias.
2. **Imprescindibles**: auth y alta (S01), conectar calendario (S02, calendar_accounts, OAuth), email de confirmacion, reprogramar y cancelar (S10), aviso de zona horaria, ver reunion programadas.
3. **Recomendables**: buffers y limite diario, recordatorios (reminders + cron), embed, round robin (S11, event_type_hosts).
4. **Opcionales**: pagos, routing forms (S12), politica de cancelacion, app movil.
5. **Arreglos** que encuentre replica-entrepreneur.

## Siguiente paso

`/replica-design`. Necesita capturas de referencia en `replica/screens/` para medir colores y tipografia; ahora esa carpeta esta vacia, asi que sin ellas solo podria definir tokens genericos.
