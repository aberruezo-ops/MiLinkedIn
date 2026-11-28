# Splitwise: que odian, que falta y por donde entrar (analisis replica, 2026-11-28)

## Fuentes y limites
- App Store: ficha oficial (4,03 estrellas, 29.893 valoraciones, puesto 29 en recaudacion de Finanzas en EE. UU.). Reseñas: **no disponibles**, el feed oficial no devuelve datos.
- Web publica de Splitwise (portada y pagina Pro), leida hoy.
- Hacker News: 171 comentarios que mencionan Splitwise (2012 a 2026), 76 desde 2020. Unica fuente de opinion. Audiencia muy tecnica, y **muchos de los criticos son autores de alternativas**: tienen interes en hablar mal. Todo lo que sigue es senal fina, no tendencia.
- El clasificador automatico de temas no sirvio (confundia menciones neutras con quejas); la lectura es a mano.

## Lo que dice la propia Splitwise
Gratis en iPhone, Android y web. Pro incluye: gastos ilimitados ("Add as many expenses as you like each day"), sin anuncios, escaneo de tickets con desglose por articulo, conversion de divisas, graficas, busqueda, reparto por defecto e importacion de transacciones (solo EE. UU.). O sea: el plan gratuito tiene **anuncios y un limite diario de gastos**. El precio de Pro no aparece en la web.

## 1. Lo que odian
1. **Limite diario de gastos en el plan gratis.** "they at some point throttled the free accounts to 4 transactions/day, which is painful" (2024-09-06) https://news.ycombinator.com/item?id=41468132 . La cifra de 4 es de ese comentario; no la he verificado en Splitwise.
2. **Suscripcion para un uso a rachas.** "Paying a monthly subscription isn't worthwhile if I only use it in bursts a couple times a year, so its back to spreadsheets." (mismo comentario).
3. **Muro de pago creciente.** "Splitwise has been paywalling very hard recently and I was personally frustrated with this." (2025-08-09, autor de una alternativa) https://news.ycombinator.com/item?id=44849142
4. **Anuncios y ruido.** "I made Spliit because I was sick of Splitwise, of all the ads on the app and all the features I never use that just add noise to my user experience." (2022-07-01, autor de una alternativa) https://news.ycombinator.com/item?id=31947032

## 2. Lo que falta
- **Apuntar y pagar en el mismo sitio.** "We were tired of juggling Splitwise for tracking and Venmo for paying." (2025-08-09) https://news.ycombinator.com/item?id=44849142
- **Varias fotos de ticket por gasto.** "Splitwise only lets you upload one receipt photo" (2026-11-03) https://news.ycombinator.com/item?id=50352679
- **Privacidad / autoalojado.** "Actually I was looking for something self-hostable that avoids sending receipts to another server." (mismo comentario)

## 3. El problema de verdad: la competencia
Ya hay alternativas gratuitas y abiertas. "Spliit is a free, open source Splitwise alternative; donations cover hosting (~$150/month)" (2026-08-26) https://news.ycombinator.com/item?id=49451331 . Y otras de pago o nuevas: Chipp ("Since our March launch, 1,650 users have moved $54K through Chipp.", 2025-08-09), PeanutSplit, SplitMate, sharebucks (todas citadas en Hacker News en 2026). Un clon que solo sea "Splitwise sin limites" compite con lo gratis.

## Por donde entrar (tres opciones)
**A. Pago por viaje, sin suscripcion.** Para quien solo reparte gastos en viajes o eventos un par de veces al año: grupos gratis, y un pago unico por viaje para lo avanzado (tickets, divisas). Evidencia: queja de uso a rachas y limite diario (1 comentario, mas la pagina Pro). Es la unica idea que ataca el modelo de negocio y no solo las funciones.
**B. Apuntar y saldar en un paso.** Para quien vive saltando entre la app de gastos y la de pagos. En España el pago real seria Bizum o transferencia: integrarlo exige un banco o entidad de pago, asi que en la practica serian enlaces de pago, no pagos dentro de la app. Evidencia: 2 comentarios.
**C. Privado y sin cuenta.** Ya lo cubre Spliit gratis y en abierto. Poco hueco.

**Recomendacion: A**, con la cautela de que la evidencia es muy fina (una fuente sesgada). Antes de construir: leer reseñas de la App Store y Google Play cuando sea posible, mirar alternativas fuertes en España (no las he comprobado aqui) y hablar con 5 a 10 personas que hayan organizado un viaje en grupo este año.

## Tamaño de la replica (criterios de replica-recon)
Nucleo (grupos, gastos con reparto igual, desigual, por porcentaje o partes, saldos, simplificar deudas, divisas, gastos recurrentes, modo sin conexion): **M**, unas semanas. Lo dificil: sincronizacion sin conexion, divisas, y apps nativas. No clonable: Splitwise Pay y la tarjeta (financieros regulados), importar transacciones bancarias (requiere agregador y licencias) y su red de grupos ya creados.
