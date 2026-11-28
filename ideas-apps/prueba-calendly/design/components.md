# Componentes (del recon: S03 a S10). Textos propios, iconos abiertos (Lucide).

Aviso: medido de la web de marketing; los estados de la interfaz real de reservas no se han visto, asi que van como diseno propio y se marcan "por verificar contra capturas de la app".

Button
  variants  primary (bg text, on bg), secondary (borde text), accent, ghost, danger
  sizes     sm 32px, md 40px, lg 48px (medido: boton principal ~48px)
  states    default, hover, active, focus-visible (anillo 2px accent), disabled, loading
  tokens    radius md (12), font sm/600
  a11y      <button> real; loading conserva la etiqueta para lectores de pantalla
  used on   S01, S05, S08, S09

Input / Select
  states    default, focus (anillo accent), error (borde danger + mensaje), disabled
  tokens    borde border-input (4.37:1), radius md, altura control-md
  a11y      <label> asociado; el error se anuncia con aria-describedby
  used on   S01, S05, S08

CalendarMonth (selector de dia)
  states    dia libre, dia sin huecos (deshabilitado, no solo gris), hoy, seleccionado, fuera de mes
  a11y      rejilla con rol grid, flechas para moverse, dia seleccionado anunciado
  used on   S06

TimezoneSelect
  states    detectada, cambiada, buscando
  used on   S06, S07

TimeSlot
  states    libre, seleccionado, ocupado mientras se elige (se retira con aviso)
  tokens    borde accent, radius md, altura control-lg
  used on   S07

BookingForm
  states    vacio, error de campo, enviando (doble clic ignorado), hueco ya ocupado
  used on   S08

WeeklyHoursEditor
  states    dia sin horas, varios tramos, tramo invalido (fin antes de inicio)
  used on   S03

EventTypeCard
  states    activo, desactivado, limite del plan Free alcanzado
  used on   S04

Toast / Modal / Table
  Toast: exito, error, con deshacer; Modal: atrapa foco, Esc cierra; Table: vacia, cargando, filas
  used on   S10, S04
