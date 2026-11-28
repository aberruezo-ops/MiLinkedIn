# Precios (hipotesis sin validar)

## Referencia: el original, leido de su pagina publica
Fuente: https://calendly.com/pricing, leida el 2026-11-28. El extracto de la pagina viene con el selector de facturacion anual; los precios de facturacion mensual no los pude ver, asi que los siguientes pueden ser los anuales.

| plan | precio mostrado | notas de la pagina |
| --- | --- | --- |
| Free | 0 | un tipo de evento, un calendario conectado |
| Standard | 10 USD por asiento y mes | tipos de evento ilimitados, varios calendarios, recordatorios y automatizaciones |
| Teams | 16 USD por asiento y mes | reparto entre el equipo (round robin), formularios de enrutado |
| Enterprise | desde 15.000 USD al año, desde 50 asientos | SSO, auditoria, soporte dedicado |

Alternativas: **no las he leido.** Ni he mirado las paginas de precios de ninguna alternativa; no incluyo cifras que no he visto. Pendiente de hacer: leer 2 o 3 antes de fijar precios.

## Lo que dicen los usuarios de precio y cobros (feedback.md, App Store EE. UU., 463 reseñas)
- Precio y plan gratuito: la herramienta cuenta 77, pero la cifra esta inflada (incluye reseñas que solo mencionan el precio). Lo verificado a mano: quejas por la retirada de un plan gratuito y por pagar sin tener soporte.
- Cobros y cancelar: 20 reseñas, media 1,9 estrellas. Quejas de baja dificil y de cobros tras pedir la cancelacion.
- Fuente unica y sesgada hacia lo negativo (media de la muestra 3,49 frente a 4,85 de la tienda). No es una encuesta de disposicion a pagar.

## El modelo propuesto
Precio plano, sin cobro por asiento: es la respuesta directa a las quejas de bajas dificiles y de saltos de precio. Mensual y anual (anual = 2 meses gratis).

| plan | para quien | precio | anual |
| --- | --- | --- | --- |
| Gratis | quien empieza | 0 EUR | |
| Para profesionales | una persona con varios tipos de reunion | 7 EUR al mes | 70 EUR |
| Para equipos pequeños | hasta 5 personas | 19 EUR al mes | 190 EUR |

**Esto es una hipotesis.** No sale de un modelo de costes ni de un estudio de precio: la referencia es la pagina del original y las quejas de la muestra. Antes de cobrar hay que calcular costes por usuario (base de datos, email, comisiones de pago) y probar con las primeras personas.

## Compromisos de cobro (se cumplen en el producto, no solo en la web)
- Darse de baja en un clic desde la cuenta. **No implementado:** hoy no hay cobros ni cuentas.
- Aviso por email antes de cada renovacion anual. No implementado.
- Sin saltos de precio por asiento: precio plano por plan. No implementado.
- Soporte humano con plazo de respuesta publicado. No existe ningun canal todavia.

## Productos y precios de Stripe a crear (los crea el usuario, en modo test primero)
- Producto "Para profesionales": precio mensual 7 EUR, precio anual 70 EUR.
- Producto "Para equipos pequeños": precio mensual 19 EUR, precio anual 190 EUR.
- Portal de cliente de Stripe activado para cambios y cancelacion.
