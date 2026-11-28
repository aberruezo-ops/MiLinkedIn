# Escaner de documentos (referencia: Smart Printer App & Scan): analisis replica, 2026-11-28

## Fuentes y limites
- App Store: ficha oficial de Smart Printer App & Scan (id 1597439129): 4,20 estrellas, 85.339 valoraciones, puesto 13 en recaudacion de Negocios en EE. UU. Reseñas: no disponibles (feed oficial caido).
- Hacker News: 381 comentarios con "scanner app", "scanning app", CamScanner, Scanner Pro o Adobe Scan; 234 desde 2021. **La gran mayoria hablan de otra cosa** (escaneres de QR, 3D, radio). Los que hablan de escanear documentos son menos de 10. Senal muy fina y de publico tecnico.
- No he visto la app de referencia ni sus precios.

## Lo que se repite
1. **El sistema ya escanea, pero es incomodo.** "It’s a bit cumbersome to open the notes app or files app and make a new scan. And adobes app uploads everything to the cloud, which is an absolute no" (2023-02-17) https://news.ycombinator.com/item?id=34835467 . Tambien: "You don't need to purchase a \"scanning\" app." (2024-07-24) https://news.ycombinator.com/item?id=41060917
2. **Rechazo a subir documentos a la nube** (misma cita de arriba).
3. **Aprecio por el pago unico frente a la suscripcion.** "Genius Scan Enterprise is a non-subscription \"pay-up-front\" scanning app that I've used (on Android) for at least 3 years with complete satisfaction." (2023-08-16) https://news.ycombinator.com/item?id=37141881 . Y un desarrollador cuenta que su escaner de pago unico "still makes approximately this much a month after nearly 15 years on the store" (2025-12-18) https://news.ycombinator.com/item?id=46311938
4. **Ganas de alternativa abierta a CamScanner.** "I’m a longtime CamScanner user, but will happily move to something open source if it delivers on its promises." (2024-09-17) https://news.ycombinator.com/item?id=41570797

## Angulo posible
Escaner que no sube nada (todo en el dispositivo), guarda directo en Archivos, sin cuenta y con pago unico. Evidencia: 4 comentarios, 1 fuente.

## Lo que lo hace dificil
- **Competidor gratis dentro del sistema:** iOS escanea desde Notas y Archivos. La referencia vende igualmente (puesto 13 en recaudacion), pero no se por que: puede ser la impresion, el marketing o suscripciones agresivas. Sin reseñas no lo puedo saber.
- **Mercado lleno** de escaneres veteranos (Scanner Pro, Genius Scan, Adobe Scan, CamScanner).

## Tamaño de la replica (criterios de replica-recon)
Escaneo con deteccion de bordes y OCR usando las APIs nativas del sistema (VisionKit y Vision en iOS): **S a M**. Impresion por AirPrint: S. Nada que no se pueda clonar, salvo la marca y la base de usuarios.
