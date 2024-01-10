---
title: Qué son los periodos de planificación
description: Aprende para qué se usan los periodos de planificación y como mostrarlos, editarlos y eliminarlos (Planificación).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Permitir que los empleados consulten su planificación
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
  - overwrite_title: Permitir que los empleados intercambien turnos
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Configurar la oferta de turnos
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Periodos de permisos
    filepath: features/scheduling/time-off/time-off-periods.md
---

Los periodos de planificación son periodos de tiempo de varios días, semanas o meses. Úsalos para:

- permitir que los empleados {% link_new consulten su planificación | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %};
- permitir que los empleados {% link_new intercambien turnos | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} entre sí;
- activar la {% link_new oferta de turnos | features/scheduling/schedules/schedules-shift-bidding.md %} para tus empleados.

Para permitir que los empleados soliciten permisos, usa los {% link_new periodos de permisos | features/scheduling/time-off/time-off-periods.md %}.

## Estado

Todos los periodos de planificación tienen un estado. El estado desbloquea o restringe determinadas acciones para los empleados en el periodo de tiempo que abarca el periodo de planificación. Por regla general, cambiarás el estado de un periodo de planificación varias veces durante el proceso de planificación, p.&nbsp;ej., cuando finalices la planificación o cuando expire el plazo para solicitar turnos.

| Estado                | Descripción                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No publicado           | Los empleados no pueden ver la planificación publicada, no pueden participar en la {% link_new oferta de turnos                                                                                                            | features/scheduling/schedules/schedules-shift-bidding.md %} y no pueden intercambiar turnos. Usa este estado si todavía no quieres que tus empleados accedan a la planificación. |
| Oferta de turnos habilitada | Los empleados pueden consultar la planificación publicada, participar en la oferta de turnos, intercambiar turnos con otros empleados y ver los {% link_new comentarios | features/scheduling/shiftcenter/add-and-delete-items.md | #add-comments %} guardados en el nivel Plan. No puedes usar este estado si el plazo del periodo de planificación ya ha expirado. |
| Publicado             | Los empleados pueden consultar la planificación publicada, intercambiar turnos con otros empleados y ver los comentarios. No pueden participar en la oferta de turnos.                                                                                      |
| Finalizado              | Este estado indica que la planificación es definitiva. Los empleados todavía pueden intercambiar turnos entre sí.                                                                                                           |

## Mostrar los periodos de planificación

1. Ve a _Plan > Planificar_{:.breadcrumbs}.
2. Haz clic en _Periodos de planificación_{:.doc-button}.
3. Selecciona una **unidad de planificación** en el primer menú desplegable. Empieza a escribir para filtrar la lista.
4. (Opcional) Para filtrar los periodos de planificación, escoge un **grupo** en el segundo menú desplegable. Empieza a escribir para filtrar la lista.  
   Verás los periodos de planificación de la unidad de planificación y el grupo seleccionadas, si los hay. Aprende más sobre las pestañas y las columnas de la tabla a continuación.

### Pestañas En marcha y Caducado

Todos los periodos de planificación disponibles para la unidad de planificación y el grupo seleccionados se muestran en las siguientes pestañas:

- **En marcha**: periodos de planificación parcial o totalmente en el futuro.
- **Caducado**: periodos de planificación completamente en el pasado.

Ambas pestañas estarán vacías si todavía no has creado ningún periodo de planificación, o si los criterios de filtrado no coinciden con ningún periodo de planificación existente.

### Columnas de la tabla

La tabla de los periodos de planificación tiene seis columnas:

- **Estado**: el estado del periodo de planificación.
- **Grupo**: qué grupo de empleados se ve afectado por el periodo de planificación.
- **Válido desde**: la fecha de inicio del periodo de planificación.
- **Válido hasta**: la fecha de fin del periodo de planificación.
- **Fecha tope**: la fecha hasta la cual los empleados pueden participar en la oferta de turnos o intercambiar turnos.
- **Heredado de**: si creas un periodo de planificación para una unidad de planificación primaria, todos los periodos de planificación para sus unidades secundarias heredarán su estado. En este caso, la columna muestra el nombre de la unidad de planificación primaria.

Puedes ordenar la lista haciendo clic en el encabezado de la columna respectiva. Para cambiar el orden de clasificación, vuelve a hacer clic en el encabezado.

### Crear periodos de planificación

1. Ve a _Plan > Planificar_{:.breadcrumbs}.
2. Haz clic en _Periodos de planificación_{:.doc-button}.
3. Haz clic en _Crear periodo de planificación_{:.doc-button} arriba a la derecha.
4. Selecciona una unidad de planificación, un grupo, un rango de fechas, una fecha tope (opcional) y un [estado](#estado) para el periodo de planificación.
5. Para guardar el periodo de planificación, haz clic en _Guardar_{:.doc-button}.

### Editar periodos de planificación

Para actualizar el estado de un periodo de planificación, selecciona un nuevo estado en el menú desplegable de la columna **Estado**. El nuevo estado se guardará automáticamente.

Para editar la configuración de un periodo de planificación (incluido el estado), sitúa el ratón sobre él y haz clic en el {% icon pencil %} a la derecha.

### Borrar periodos de planificación

Para borrar uno o varios periodos de planificación, marca las casillas de verificación a la izquierda de los periodos. La casilla en el encabezado marca o desmarca todas las casillas de la tabla. Haz clic en _Eliminar seleccionado_{:.doc-button} debajo de la tabla.