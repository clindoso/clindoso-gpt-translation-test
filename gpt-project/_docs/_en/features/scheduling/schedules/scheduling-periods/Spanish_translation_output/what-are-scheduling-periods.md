---
title: ¿Qué son los periodos de planificación?
description: Aprende cómo se utilizan los periodos de planificación y cómo mostrar, editar y borrar periodos de planificación (Planificación).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
---

Los periodos de planificación son periodos de tiempo de varios días, semanas o meses. Utilízalos para:

- permitir a los empleados {% link_new consultar los horarios | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %}.
- permitir a los empleados {% link_new intercambiar turnos | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.
- permitir a los empleados {% link_new marcar turnos | features/scheduling/schedules/schedules-shift-bidding.md %}.

Para permitir a los empleados solicitar ausencias, utiliza los {% link_new periodos de ausencia | features/scheduling/time-off/time-off-periods.md %}.

## Estado

Todos los periodos de planificación tienen un estado, que desbloquea o restringe determinadas acciones para los empleados para el periodo de tiempo del periodo de planificación. Normalmente cambiarás el estado de un periodo de planificación varias veces durante el proceso de planificación, por ejemplo una vez hayas finalizado la planificación o una vez haya expirado el plazo para participar en el periodo de planificación.

| Estado                | Descripción                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sin publicar           | Los empleados no pueden ver el horario publicado, no pueden participar en la {% link_new adjudicación                                                                                                                 | features/scheduling/schedules/scheduling-periods/schedules-shift-bidding.md %} de turnos y no pueden intercambiar turnos. Utiliza este estado si todavía no quieres publicar el horario a tus empleados. |
| Adjudicación de turnos activada | Los empleados pueden ver el horario publicado, participar en la adjudicación de turnos, intercambiar turnos con otros empleados y ver los {% link_new comentarios | features/scheduling/shiftcenter/add-and-delete-items.md | #añadir-comentarios %} introducidos en el horario. Este estado no se puede marcar si el periodo de planificación tiene un plazo que ya ha expirado. |
| Publicado             | Los empleados pueden ver el horario publicado, intercambiar turnos con otros empleados y ver los comentarios introducidos. No pueden participar en la adjudicación de turnos.                                                                                      |
| Finalizado              | Este estado indica que el horario es definitivo. Los empleados todavía pueden intercambiar turnos entre ellos.                                                                                                           |

## Mostrar periodos de planificación

1. Ve a _Plan > Planificación_{:.breadcrumbs}.
2. Haz clic en _Periodos de planificación_{:.doc-button}.
3. Selecciona una **unidad de planificación** en el primer menú desplegable. Empieza a escribir para filtrar la lista.
4. (Opcional) Para filtrar los periodos de planificación, escoge una **selección** en el segundo menú desplegable. Empieza a escribir para filtrar la lista.  
   Si hay periodos de planificación para la unidad de planificación y selección seleccionadas, se mostrarán. Aprende más sobre las pestañas y las columnas de la tabla a continuación.

### Pestañas «En curso» y «Expirado»

Todos los periodos de planificación de la unidad de planificación y/o selección escogidas se muestran en las siguientes pestañas:

- **En curso**: Periodos de planificación que comienzan parcial o totalmente en el futuro.
- **Expirado**: peridos de planificación completamente en el pasado.

Ambas pestañas estarán vacías si no has creado un periodo de planificación todavía, o si los criterios de filtrado no coinciden con un periodo de planificación existente.

### Columnas de la tabla

La tabla de periodos de planificación tiene seis columnas:

- **Estado**: el estado del periodo de planificación
- **Selección**: qué selección de empleados está afectada por el periodo de planificación
- **Válido desde**: la fecha de inicio del periodo de planificación
- **Válido hasta**: la fecha de fin del periodo de planificación
- **Plazo**: la fecha antes de la cual los empleados pueden participar en la adjudicación de turnos o intercambiar turnos
- **Heredado de**: si creas un periodo de planificación para una unidad de planificación superior, todos los periodos de planificación para sus unidades hijas heredarán su estado. La columna muestra el nombre de la unidad de planificación superior si aplica.

Puedes ordenar la lista haciendo clic en la **encabezado** de la columna respectiva. Para cambiar el orden de clasificación, haz clic de nuevo en el encabezado de la columna.

### Crear periodos de planificación

1. Ve a _Plan > Planificación_{:.breadcrumbs}.
2. Haz clic en _Periodos de planificación_{:.doc-button}.
3. Haz clic en _Crear un periodo de planificación_{:.doc-button} arriba a la derecha.
4. Selecciona una unidad de planificación, una selección, un rango de fechas, un plazo (opcional) y un [estado](#estado) para el periodo de planificación.
5. Para guardar el periodo de planificación, haz clic en _Guardar_{:.doc-button}.

### Editar periodos de planificación

Para actualizar el estado de un periodo de planificación, selecciona un nuevo estado en el menú desplegable de la columna **Estado**. El nuevo estado se guardará automáticamente.

Para editar la configuración de un periodo de planificación (incluido el estado), sitúa el ratón sobre él y haz clic en el {% icon pencil %} a la derecha.

### Borrar periodos de planificación

Para borrar uno o más periodos de planificación, marca las **casillas de verificación** a la izquierda de los periodos. La casilla de verificación en la parte superior marca o desmarca todas las casillas de la lista. Haz clic en _Borrar los elementos seleccionados_{:.doc-button} debajo de la lista.
