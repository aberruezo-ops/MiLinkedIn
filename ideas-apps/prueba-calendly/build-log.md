# Build log (rebanada vertical, prueba)

Datos en memoria, sin auth ni calendario externo. Codigo en replica/app/ (Node sin dependencias). Capturas en replica/clone-screens/.

- S03 disponibilidad: hecho. Editor de tramos semanales con validacion (fin posterior a inicio). Falta: varios dias a la vez, excepciones por fecha.
- S05 tipo de evento: parcial. Un solo tipo editable. Falta: crear varios, ubicacion, limite diario en la interfaz.
- S06 pagina de reserva (calendario): hecho. Estados: cargando (esqueletos), sin huecos, enlace invalido, error de carga con reintento.
- S07 seleccion de hora: hecho. Muestra horas en la zona del invitado.
- S08 formulario: hecho. Errores por campo (se limpian al escribir), doble envio ignorado, conflicto 409 con aviso.
- S09 confirmacion: hecho. Incluye cancelar.

Mas dificil de lo esperado: el margen antes/despues entre reuniones (mi primera version solo bloqueaba en un sentido; la prueba lo cazo). Dos fallos de interfaz encontrados por el recorrido en navegador: el aviso de conflicto se borraba al recargar huecos, y los errores no se quitaban al escribir.

Pendiente, no hecho: email de confirmacion, reprogramar, calendario externo, Postgres real, autenticacion. Algunos textos tienen tamaños de fuente en px fijos (14px) en lugar de token.
