# Recon map: Calendly (web)

Scope: scheduling core loop (event types, availability, public booking page, team round robin). Out: Notetaker, Callie, Contacts, Opportunities.
For: prueba de ejemplo, producto de nicho para equipos pequenos.
Date: 2026-11-28

Nota de fiabilidad: es una prueba con fuentes publicas solamente. Los articulos del centro de ayuda se cargan con JavaScript y no se pudieron leer, y no hay cuenta del usuario ni capturas. Por eso las pantallas y flujos son INFERIDOS (confianza media/baja), no observados. Con cuenta propia y capturas se cerraria el hueco.

## Sources

| # | source | URL | notes |
| --- | --- | --- | --- |
| 1 | pricing page | https://calendly.com/pricing | leida: planes, precios, funciones por plan |
| 2 | features page | https://calendly.com/features | leida: capacidades de scheduling y "how it works" en 4 pasos |
| 3 | help center home | https://help.calendly.com | leida: arbol de categorias (Event types, Availability, Sharing & booking, Routing forms, Automations...) |
| 4 | help articles | https://help.calendly.com/help/event-types (y otros) | NO leidos: render por JS |
| 5 | public API docs | developer docs (enlazado en la ayuda) | pendiente |

## Core loop

El anfitrion conecta su calendario, define disponibilidad y un tipo de evento, comparte un enlace, y el invitado (sin cuenta ni asiento) elige hora y la reserva queda en el calendario de ambos.

## Screens (inferidas)

| ID | screen | route / how to reach | purpose | key components | states seen |
| --- | --- | --- | --- | --- | --- |
| S01 | Alta / login | /login | entrar | form, SSO | por observar |
| S02 | Conectar calendario | Availability > Calendar settings (fuente: ayuda, 5 pasos) | evitar dobles reservas | selector de proveedor, lista de calendarios | por observar |
| S03 | Disponibilidad | Availability | horas semanales, buffers, limites diarios | editor semanal, buffers | por observar |
| S04 | Lista de tipos de evento | Event types | gestionar enlaces | cards, boton crear | vacio (plan Free: 1 tipo) |
| S05 | Editor de tipo de evento | Event types > crear | nombre, duracion, ubicacion, plantilla uno-a-uno o multi | form, selector de ubicacion | por observar |
| S06 | Pagina de reserva publica | enlace compartido | elegir dia | calendario, selector de zona horaria | por observar |
| S07 | Seleccion de hora | tras elegir dia | elegir slot | lista de slots | sin huecos, por observar |
| S08 | Formulario del invitado | tras elegir slot | datos del invitado | form | por observar |
| S09 | Confirmacion | tras enviar | cierre | resumen, anadir a calendario | por observar |
| S10 | Reuniones programadas | Scheduled events | ver/cancelar | tabla | por observar |
| S11 | Equipo y round robin | plan Teams | reparto entre miembros | selector de miembros | por observar |
| S12 | Routing forms | plan Teams | cualificar y enrutar leads | constructor de formulario | por observar |
| S13 | Automatizaciones y recordatorios | plan Standard | recordatorios y seguimientos | editor de reglas | por observar |

## Flows

```
F01 Invitado reserva una reunion
    S06 -> S07 -> S08 -> S09
    happy path clicks: por medir (estimado 3-4 sin contar el enlace)
    edge: sin huecos, zona horaria distinta, hueco ocupado mientras se rellena el formulario
F02 Anfitrion configura y comparte
    S01 -> S02 -> S03 -> S05 -> compartir enlace
    (fuente: features "How it works" 01-04: conectar, disponibilidad, plantilla, compartir)
F03 Anfitrion reparte reuniones en equipo (Teams)
    S11 -> S05 -> S06
F04 Lead cualificado y enrutado (Teams)
    S12 -> S06
```

## Components

| component | variants | states | used on |
| --- | --- | --- | --- |
| Button | primary, secondary | por observar | all |
| Calendario mensual | | dia con huecos, sin huecos, seleccionado | S06 |
| Selector de zona horaria | | | S06, S07 |
| Slot de hora | | libre, seleccionado | S07 |
| Form de invitado | | error, enviando | S08 |
| Editor semanal | | | S03 |

## Inferred data model

```
User          id, email, name, plan, timezone
              evidence: S01, pricing (asiento por usuario)   confidence: medium
CalendarAccount  id, user_id, provider (google|outlook|exchange), main (bool)
              evidence: ayuda "Connect your calendar" (5 pasos, calendario principal)   confidence: high
Availability  user_id, weekly_hours, buffers, daily_limit
              evidence: features (buffers, limites diarios, horarios)   confidence: medium
EventType     id, owner_id, name, duration, location, kind (one-on-one|group|collective|round-robin)
              evidence: features (plantillas de reunion), pricing (Free: 1 tipo)   confidence: medium
Booking       id, event_type_id, start_at, end_at, guest_name, guest_email, status, answers
              evidence: inferido del flujo F01   confidence: guess (campos exactos sin verificar)
Team          id, name, members   evidence: pricing Teams, round robin   confidence: medium
```

Relationships: User 1-n EventType, EventType 1-n Booking, User 1-n CalendarAccount, Team n-n User.

## Feature matrix

Ver `features.csv`.

## Out of scope (cannot or should not be cloned)

- Notetaker (grabacion y transcripcion) y Callie (asistente IA, beta): productos aparte.
- Integraciones con Salesforce, Marketo, Pardot, Dynamics: acuerdos de socio.
- SSO/SAML, SCIM, auditoria: solo Enterprise.
- Marca, textos e iconos de Calendly.

## Size

Screens 13 (inferidas), flows 4, entities 6. Hard parts: sincronizacion bidireccional con Google/Outlook, zonas horarias y cambios de hora, evitar doble reserva concurrente. Size: M (unas semanas) solo para el bucle central; L si se anaden equipos y routing.
