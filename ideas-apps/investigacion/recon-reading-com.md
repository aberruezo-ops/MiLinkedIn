# Recon map: Reading.com (iOS)

Alcance: el bucle central. Lecciones guionizadas adulto+niño, cuentos descodificables, videos de letras y juegos de practica. Fuera: portal web para profesores.
Para: version en español con metodo silabico, para España, Latinoamerica y familias hispanohablantes de EE. UU.
Fecha: 2026-11-28

Fiabilidad: solo fuentes publicas. Sin cuenta, sin reseñas (feed de Apple caido) y sin precios (el embudo de alta no se pudo abrir). Las pantallas salen de las 8 capturas oficiales y de los textos publicos; las que no aparecen en capturas van marcadas como inferidas.

## Fuentes
| # | fuente | URL | notas |
| --- | --- | --- | --- |
| 1 | ficha App Store (API oficial) | https://apps.apple.com/us/app/id1534938305 | 4,69 estrellas, 82.865 valoraciones, puesto 23 en recaudacion de Educacion EE. UU.; v5.13.43 del 2026-11-20; lanzada 2021-12-14; solo ingles; 4+; descripcion completa |
| 2 | 8 capturas oficiales | servidas por is1-ssl.mzstatic.com | en screens/app-0..7.jpg y screens/app-hoja.jpg. Solo referencia |
| 3 | portada | https://www.reading.com/ | metodo, etapas, publico, "2,5 millones de padres" (cifra suya) |
| 4 | edicion profesores | https://www.reading.com/teachers | portal web, gestion de clases, SSO con Google, Clever, ClassLink |
| 5 | ayuda | https://www.reading.com/support | temas: cuenta, suscripciones, reembolsos, lecciones, colegios |
| 6 | proximamente | https://www.reading.com/coming-soon | lista de espera para Chromebook y Windows |
| 7 | informe de eficacia | https://www.reading.com/efficacy-research.pdf | EdTech Recharge, marzo 2024, nivel ESSA Tier IV: modelo logico; **"It does not provide causal evidence of efficacy."** Habla de 99 lecciones (hoy anuncian 120) |
| 8 | precios | https://get.reading.com/welcome-p-hp | no legible desde aqui: **por verificar** |
| 9 | reseñas | feed oficial de Apple | no disponible |

## Bucle central
Cada dia, un adulto abre la leccion siguiente y la hace con el niño 15 a 20 minutos siguiendo un guion en pantalla ("tu dices / el niño hace"); al avanzar se desbloquean cuentos, videos y juegos que el niño puede usar solo.

## Metodo (de sus textos)
Instruccion Directa, fonetica sintetica explicita ("Science of Reading"). Cinco etapas: 1 letras, 2 unir letras, 3 leer libros, 4 descodificacion avanzada, 5 fluidez. Actividades por leccion: cancion del alfabeto, repaso, letra nueva, decir sonidos, unir sonidos, rimas, historia sonora, escribir letra o palabra, leer palabra o libro, comprension. Evita "adivinar por el dibujo" ("No guessing. Real reading only"). Contenido: 120 lecciones, 84 cuentos descodificables, 42 videos, 5 juegos, imprimibles.

## Pantallas
| ID | pantalla | como se llega | proposito | componentes | estados |
| --- | --- | --- | --- | --- | --- |
| S01 | Alta | primera apertura | cuenta del adulto | formulario | inferida |
| S02 | Suscripcion | tras el alta | pago familiar (hasta 3 perfiles) | muro de pago, control parental | inferida |
| S03 | Perfiles | inicio | elegir niño (max 3) | tarjetas de perfil | inferida (descripcion) |
| S04 | Mapa de lecciones | inicio del perfil | progreso 1 a 120 | camino con nodos, leccion actual | visto (captura 2) |
| S05 | Leccion guiada | nodo del mapa | el adulto guia, el niño responde | instruccion al adulto arriba, letras grandes con marcas de sonido (puntos y arcos), botones de audio, "tips", avanzar y retroceder, cerrar | visto (capturas 2 y 3) |
| S06 | Actividades de leccion | dentro de S05 | secuencia de 6 a 10 actividades | variantes de S05 | descrito en informe |
| S07 | Lector de cuento | leccion o biblioteca | leer un cuento descodificable | pagina con texto y dibujo, palabra en curso subrayada, puntos bajo letras, audio | visto (capturas 4 y 5) |
| S08 | Biblioteca de cuentos | inicio | 84 cuentos desbloqueables | rejilla con bloqueados | inferida |
| S09 | Videos de letras | inicio | 42 videos con niños reales y cancion | rejilla de videos | visto (captura 4) |
| S10 | Mundo de juegos | inicio | elegir juego | escena con personajes-letra | visto (captura 4) |
| S11 | Juego: trazar | S10 | escribir letras y palabras | trazo con guia | visto (captura 6) |
| S12 | Juego: palabras frecuentes | S10 | reconocer palabras | piezas que caen o se tocan | visto (captura 6) |
| S13 | Juego: deletrear | S10 | formar palabras con letras | huecos y letras moviles | visto (captura 6) |
| S14 | Imprimibles | inicio | fichas en papel | lista de PDF | visto (captura 8) |
| S15 | Ajustes y cuenta | menu del adulto | suscripcion, perfiles, borrar cuenta | lista | inferida (enlaces de la web) |

## Flujos
```
F01 Leccion diaria (el que se paga)
    S03 perfil -> S04 mapa -> S05/S06 leccion guiada -> fin -> desbloqueo
    clics del camino feliz: por medir (sin cuenta)
    borde: el niño se cansa a mitad, leccion a medias, dos niños en el mismo dispositivo
F02 Leer un cuento
    S04 o S08 -> S07 -> comprension
    borde: cuento aun bloqueado, sin conexion
F03 Juego autonomo del niño
    S10 -> S11 / S12 / S13
F04 Alta y suscripcion
    S01 -> S02 -> S03
    borde: pago cancelado, prueba gratuita, restaurar compra
F05 Imprimir actividad
    S14 -> PDF
```

## Componentes
Tarjeta de guion para el adulto ("tu dices" / "el niño hace"); fichas de letra con marcas de sonido (punto = sonido, arco = digrafo); nodo de mapa (hecho, actual, bloqueado); pagina de cuento con resaltado palabra a palabra; boton de audio; rejilla de videos; tarjetas de juego; control parental antes de compras y ajustes (obligatorio en la categoria Niños de Apple); muro de pago.

## Modelo de datos inferido
```
Account        id, email, subscription_status, created_at
               evidencia: enlaces de gestion y borrado de cuenta        confianza: alta
ChildProfile   id, account_id, name, birth_year o edad, avatar
               evidencia: "up to 3 profiles"                            confianza: alta
Lesson         number (1-120), stage (1-5), activities[]
               evidencia: descripcion, portada, informe                 confianza: alta
Activity       lesson_number, order, type (song|review|new_letter|sounds|blend|rhyme|sound_story|write|read|comprehension), content refs
               evidencia: informe de eficacia                           confianza: media
Book           id, title, unlock_lesson, pages[], word_list
               evidencia: "84 decodable storybooks"                     confianza: media
Video          id, letter, url                                          confianza: media
Game           id (5), skill                                            confianza: media
LessonProgress child_id, lesson_number, completed_at, activity_index    confianza: suposicion
GameProgress   child_id, game_id, level, stars                          confianza: suposicion
```
Relaciones: Account 1-n ChildProfile; ChildProfile 1-n LessonProgress; Lesson 1-n Activity; Lesson desbloquea Book.

## Adaptacion al español (lo que hace original la version)
La fonetica inglesa no se traduce: el español tiene una ortografia mucho mas transparente y se enseña habitualmente por silabas. Puntos a validar con una maestra de Infantil o una logopeda (no los he validado):
- Orden habitual: vocales, silabas directas (ma, me, mi), inversas (am, em), mixtas, trabadas (bra, pla), y despues los casos especiales: ch, ll, rr, qu, gu/gue/gui, c y g con varios sonidos, r suave y fuerte, h muda, y.
- Variantes regionales: seseo y ceceo (c, z, s) y yeismo (ll, y). Propuesta: paquetes de voz España y Latinoamerica.
- Las marcas visuales del original (puntos por sonido, arcos por digrafo) se adaptan bien a silabas: un arco por silaba.
- El guion "tu dices / el niño hace" funciona igual en español: es la parte mas valiosa y no depende del idioma.

## Matriz de funciones
Ver features.csv.

## No clonable
Las lecciones, cuentos, videos, canciones, personajes y marca de Reading.com y Teaching.com (contenido con derechos: hay que crearlo todo de nuevo), su certificacion kidSAFE y su informe de eficacia, y las integraciones escolares de EE. UU. (Clever, ClassLink).

## Tamaño
Pantallas 15, flujos 5, entidades 9. La app es M; el contenido es lo que la hace **L**: 100+ lecciones guionizadas, decenas de cuentos ilustrados, locuciones en dos variantes, videos. Partes dificiles: produccion de contenido con criterio pedagogico, cumplimiento de la categoria Niños de Apple y de proteccion de datos de menores, suscripcion con control parental. No hace falta reconocimiento de voz: quien corrige es el adulto.
