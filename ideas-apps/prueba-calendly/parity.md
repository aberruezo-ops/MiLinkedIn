# Paridad: clon de scheduling frente a Calendly (prueba de ejemplo)

Veredicto: **no es publicable**. Faltan 4 funciones imprescindibles y la ruta de administracion no tiene autenticacion. No hay bugs S1 ni S2 abiertos.

## Cifras
- Paridad de funciones: **52,6 / 100** (17 funciones contadas, 4 descartadas por no clonables). Imprescindibles hechas: **5 de 9**.
- Paridad de diseno: **sin cifra, a proposito.** Las unicas capturas de referencia son de la web de marketing de Calendly (/features y /pricing; la de precios salio casi en blanco). No se puede comparar con sentido con la pagina de reserva del clon. Forzar una puntuacion seria inventarla. Para medirla hacen falta capturas de la app real de reservas (pagina publica de un anfitrion, o la cuenta del propio usuario).
- Ojo con las propias cifras de funciones: parten de un recon con partes inferidas (ver recon.md). Una funcion "hecha" lo esta respecto a lo que supusimos, no respecto a lo que el original hace de verdad.

## Informe de la herramienta
## Parity: 52.6 / 100

features 52.6  (17 counted, must-haves 5 of 9 done)

Not shippable yet: 4 must-have features are not done.

## By area, weakest first
- onboarding                     0.0  (1 features)
- payments                       0.0  (1 features)
- teams                          0.0  (2 features)
- sharing                        0.0  (1 features)
- platform                       0.0  (1 features)
- notifications                 30.0  (2 features)
- bookings                      37.5  (2 features)
- event types                   50.0  (1 features)
- availability                  80.0  (2 features)
- booking page                 100.0  (4 features)

## Missing, in build order
- [must] onboarding: Conectar calendario (Google/Outlook) para leer ocupado, no  (fuente ayuda)
- [must] bookings: Reprogramar y cancelar, partial  (por verificar; cancelar si; reprogramar no)
- [must] event types: Tipos de evento (nombre duracion ubicacion), partial  (Free limita a 1; un solo tipo editable (nombre, duracion, margenes); sin ubicacion ni varios tipos)
- [must] notifications: Email de confirmacion a ambos, partial  (cola con reintentos y dead letter; proveedor simulado, sin envio real)
- [should] notifications: Recordatorios automaticos, no  (plan Standard)
- [should] sharing: Embed en web, no  (ayuda)
- [should] teams: Round robin y reuniones de equipo, no  (plan Teams)
- [should] availability: Buffers y limites diarios, partial  (features page; buffers si; limite diario solo en el modelo, sin interfaz)
- [could] bookings: Politica de cancelacion, no  (pricing)
- [could] payments: Cobros (Stripe/PayPal), no  (plan Standard)
- [could] platform: App movil y extension de navegador, no
- [could] teams: Routing forms, no  (plan Teams)

## Left out on purpose (not scored)
- Notetaker: producto aparte
- Callie asistente IA: beta producto aparte
- Integracion Salesforce/Marketo/Pardot: acuerdos de socio
- SSO SAML SCIM auditoria: solo Enterprise

## Diferencias de comportamiento
Solo conozco el comportamiento del clon. Del original no he observado ningun flujo (no hay cuenta ni walkthroughs leidos), asi que no hay filas "el original hace" fiables.
- Clon, reservar: elegir dia, elegir hora, escribir nombre y correo, confirmar. Son 3 pulsaciones mas dos campos de texto. El numero del original esta por medir.
- Clon, conflicto: si el hueco se ocupa mientras se rellena, aviso y lista actualizada. Original: sin verificar.
- Clon, recordatorios, reprogramar y emails reales: no existen.

## Las 5 cosas a construir despues
1. Conectar calendario externo (OAuth de Google y Microsoft). Es lo que hace util al producto, y Google exige verificar la app antes del lanzamiento publico: empezar ya.
2. Autenticacion del anfitrion y cerrar las rutas /api/admin/*, que hoy estan abiertas.
3. Email real con la clave del usuario (Resend) y dominio con SPF/DKIM.
4. Reprogramar una reserva.
5. Varios tipos de evento con ubicacion, y limite diario en la interfaz.
