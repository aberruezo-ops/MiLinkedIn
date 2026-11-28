# Preflight de despliegue (prueba de ejemplo)

Fecha: 2026-11-28. **Veredicto: NO desplegar.** No se ha desplegado nada, ni se ha tocado ningun dominio, DNS, Stripe ni cuenta.

## Resultados
| comprobacion | resultado |
| --- | --- |
| Casos e2e (26, contra Postgres local) | pasan 26/26 |
| Pruebas de API y backend | pasan |
| Paridad de funciones | **52,6 / 100; imprescindibles 5 de 9. Falla.** |
| Barrido de marca, app y landing | limpio |
| Ficha de tienda (listing.py) | 0 errores, 0 avisos |
| Build de produccion | no hay paso de build (servidor Node sin compilar); `npm test` es un marcador sin pruebas, las pruebas se ejecutan con los scripts de e2e/ |
| npm audit | 0 vulnerabilidades |
| Bugs S1/S2 abiertos | ninguno (7 S3 corregidos, bugs.md) |
| Paginas de privacidad y terminos | **no existen** |
| Cookies | la app no usa cookies, pero no hay aviso ni politica escrita |
| Borrado de cuenta | **no existe** (tampoco hay cuentas) |
| Favicon e imagen social | **no existen** |
| Autenticacion del anfitrion | **ninguna: /api/admin/* abierto a cualquiera** |

## Lo que bloquea (en orden)
1. Faltan 4 funciones imprescindibles: calendario externo, reprogramar, varios tipos de evento (parcial), email real (parcial). Criterio de la skill: publicable solo con todas.
2. Las rutas de administracion no tienen autenticacion. Con cualquiera ya podria cambiar horarios o el evento. Es un bloqueo de seguridad, no cosmetico.
3. Sin politica de privacidad ni terminos, y se recogen nombre y correo de invitados.
4. Marca sin validar: ninguna comprobacion de nombre hecha (marcas, dominios, perfiles; brand.md).
5. La baja de suscripcion en un clic, que es el angulo del producto, no existe porque no hay cobros. Lanzar con ese titular seria enganoso.
6. El angulo sale de una sola fuente de resenas, sesgada hacia lo negativo (fixes.md).

## Servicios de produccion: pendiente, lo hace el usuario
- Proyecto de base de datos separado con copias de seguridad; migraciones 001 a 003 aplicadas por el despliegue (hoy se aplican con scripts/migrate.js).
- Variables de entorno de .env.example en el host. Claves reales solo ahi.
- Stripe: productos y precios de pricing.md; en modo test primero.
- OAuth de Google y Microsoft con dominio de produccion; Google exige verificar la app para los permisos de Calendar (tarda semanas).
- Email: dominio emisor verificado en el proveedor.

## Host y dominio (plantilla; no hay dominio elegido)
Host sugerido: Vercel u otro con soporte de Node. Con dominio ya comprado por el usuario:

| registro | nombre | valor |
| --- | --- | --- |
| A | @ | IP que indique el host |
| CNAME | www | destino que indique el host |
| TXT | @ | valor de verificacion, si lo pide |

Correo (los valores los da el proveedor de email): SPF (TXT), DKIM (CNAME o TXT) y DMARC empezando por `v=DMARC1; p=none; rua=mailto:tu-direccion` para endurecerlo despues. Sin esto, las confirmaciones irian a spam. Elegir host canonico (con o sin www) y redirigir el otro.

## Vigilancia en la primera semana (cuando se despliegue)
Seguimiento de errores, comprobacion de disponibilidad de la pagina de reserva y de /api/slots, registros conservados, analitica sin cookies, alerta al correo del propietario. Hacer una reserva completa en el sitio real y pedir a otra persona que la haga desde el movil.

## Movil
No hay app. La ficha de tienda de launch/listing.json es un borrador y lo dice.

## Que hay que decidir antes del siguiente intento
Hasta que los puntos 1 a 3 no esten resueltos no tiene sentido pedir el visto bueno para publicar.
