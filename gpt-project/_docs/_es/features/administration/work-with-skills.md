---
title: Usar las cualificaciones
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprende cómo reflejar las cualificaciones de tu equipo en injixo. Crea, edita y elimina cualificaciones y niveles de cualificación.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
redirect_from:
  - /es/skills/
redirect_reason: Updated filename on 24 July 2023
---

Las cualificaciones garantizan que los empleados solo sean planificados para trabajar en actividades para las que están cualificados. Las cualificaciones correlaciones las habilidades de tus empleados (conocimiento del producto, idiomas, canales de comunicación, etc.) con las actividades en las que pueden trabajar y que tú planificas en injixo.

Para configurar cualificaciones, ve a _Plan > Configuración > Cualificaciones_{:.breadcrumbs}.

## Crear cualificaciones

Crea un mínimo de una cualificación para cada actividad que requiera una habilidad particular. Cuando creas una cualificación, injixo crea por defecto un nivel de cualificación de 100&nbsp;%. Los niveles de habilidad reflejan cuán competentes deben ser los empleados para trabajar en una actividad, p.&nbsp;ej., 100&nbsp;% competentes en inglés pero solo 50&nbsp;% competentes en español. Puedes crear diferentes niveles de cualificación para una cualificación. 

> Si tus empleados no necesitan habilidades específicas para trabajar en una actividad, no es necesario que crees una cualificación para ella.

1. Haz clic en _Nueva cualificación_{:.doc-button}.
2. Introduce un **nombre**.
   La abreviatura se genera automáticamente, pero puedes modificarla.
3. (Opcional) Haz clic en _Añadir nivel de cualificación_{:.doc-button} para modificar la **calificación** predeterminada de un nivel de cualificación, o para añadir niveles de cualificación adicionales, si tienes empleados que son menos competentes en la actividad. Puedes leer más en [Calcular la idoneidad usando la calificación y la ponderación](#calcular-la-idoneidad-usando-la-calificación-y-la-ponderación)
4. Haz clic en _Crear nueva cualificación_{:.doc-button}.  

 A continuación, puedes [asignar un nivel de cualificación a un empleado](#asignar-niveles-de-cualificación-a-un-empleado) y [asignar la cualificación a una actividad](#añadir-cualificaciones-a-actividades).

## Duplicar cualificaciones

Para crear una nueva cualificación con los mismos niveles de cualificación que otra cualificación ya existente, sigue estos pasos:

1. En la lista de **Cualificaciones**, haz clic en la cualificación que quieres duplicar.
2. Haz clic en **Duplicar cualificación** bajo el nombre de la cualificación.  
   Se abre la ventana **Crear nueva cualificación** con los niveles de cualificación prellenados.
3. Introduce un **nombre** para la nueva cualificación.
4. (Opcional) Modifica los niveles de cualificación.
5. Haz clic en _Crear cualificación_{:.doc-button}.

## Editar cualificaciones y niveles de cualificación

1. Selecciona una cualificación de la lista.
2. Modifica la cualificación o los niveles de cualificación.
   Para eliminar un nivel de cualificación, haz clic en el {% icon trash %} a su derecha.
3. Haz clic en _Guardar cambios_{:.doc-button}.

## Eliminar cualificaciones

1. Selecciona una cualificación de la lista.
2. Haz clic en _Eliminar cualificación_{:.doc-button} y confirma la acción.

## Añadir cualificaciones a actividades

1. Ve a _Plan > Configuración > Actividades_{:.breadcrumbs}.
2. Selecciona una actividad de la lista y desplázate hasta la sección **Cualificaciones**.
3. Selecciona una cualificación en el menú desplegable.
4. (Opcional) Modifica la **ponderación**. Si solo vas a añadir una cualificación, mantén el valor predeterminado de 100.  
   Para actividades que requieren más de una cualificación, puedes [usar la ponderación](#calcular-la-idoneidad-usando-la-calificación-y-la-ponderación) para determinar qué cualificación es más importante.
7. Haz clic en _Guardar cambios_{:.doc-button}.

## Asignar niveles de cualificación a un empleado

1. Ve a _Plan > Configuración > Empleados_{:.breadcrumbs}.
2. Selecciona un empleado de la lista y desplázate a la sección **Grados de cualificación**.
3. Haz clic en el icono Insertar {% icon item-add | icon-only %} y selecciona uno o varios niveles de cualificación de la lista.
   Para seleccionar varios a la vez, mantén pulsada la tecla **Mayús** o **Ctrl** mientras haces clic.
4. (Opcional) Añade un {% link_new periodo de validez | features/administration/set-a-validity-period.md %} para el nivel de cualificación. Para ello, selecciona las fechas deseadas en los campos **Válido desde** y **Válido hasta**.
   No puedes asignar diferentes niveles de cualificación de una misma cualificación a un empleado para el mismo periodo de validez.
 5. Haz clic en _Aceptar_{:.doc-button}.  
   Las actividades que requieren la cualificación aparecerán en la sección **Actividades** en los datos de ese empleado.

Una actividad puede requerir una o varias cualificaciones. Para trabajar en una actividad que requiere varias cualificaciones, los empleados deben tener todas las cualificaciones necesarias.

Sugerencia: con la {% link_new función de modificación masiva | features/administration/employee-overview.md | #usar-la-modificación-masiva %} puedes asignar una cualificación a varios empleados a la vez. 

## Calcular la idoneidad usando la calificación y la ponderación

injixo puede calcular un valor de idoneidad basado en:

- la calificación del nivel de cualificación de un empleado;
- los valores de ponderación cuando una actividad requiere varias cualificaciones.

Pongamos por ejemplo que  tienes la actividad «Llamadas en español», que requiere dos cualificaciones, español y llamadas. La cualificación español es el doble de importante que la cualificación llamadas. Los valores de ponderación son 100 para español y 50 para llamadas.

- El empleado 1 tiene un nivel de cualificación de 50&nbsp;% en español y de 100&nbsp;% en llamadas.
- El empleado 2 tiene un nivel de cualificación de 100&nbsp;% en español y de 50&nbsp;% en llamadas.

Esto resulta en un valor de idoneidad del 66,66&nbsp;% para el empleado 1 y del 83,33&nbsp;% para el empleado 2.

El valor de idoneidad se calcula con esta fórmula: `(Suma(La ponderación de cada cualificación * el nivel de cualificación de cada empleado para esa cualificación) / (Suma de las ponderaciones de todas las cualificaciones)`

Si una actividad requiere solo una cualificación, el valor de idoneidad es igual al nivel de cualificación del empleado.

Para tener en cuenta el valor de idoneidad en la {% link_new planificación optimizada| features/scheduling/schedules/schedules-optimized-schedules.md %} (en lugar de usar el número de empleados), configure el ajuste _48069_{:.id-label}_. En el {% link_new Centro de planificación | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %} y en {% link_new Planificar | features/scheduling/schedules/schedules-activity-coverage.md %}, la cobertura y la ocupación no se pueden mostrar en función de la idoneidad de los empleados. En estos casos, la cobertura y la ocupación siempre aparecen al 100&nbsp;% para mostrar la cantidad de empleados.
