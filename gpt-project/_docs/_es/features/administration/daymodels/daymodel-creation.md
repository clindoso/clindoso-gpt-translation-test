---
title: Configurar modelos de horario
redirect_from:
  - /es/day-models-overview/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprende cómo crear modelos de horario de los tipos turno fijo, turno variable y margen de disponibilidad, y cómo añadir actividades a los modelos de horario.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-basics.md
  - overwrite_title: Establecer un periodo de validez
    filepath: features/administration/set-a-validity-period.md
---

¿Los modelos de horario son nuevos para ti? Consulta primero {% link_new la información básica | features/administration/daymodels/daymodel-basics.md %}.

## Crear modelos de horario

Puedes crear y editar modelos de horario en _Plan > Configuración > Modelos de horario_{:.breadcrumbs}.

> Atención
> 
> - A los modelos de horario de tipo turno fijo también se les llama modelos de horario fijos.<br> 
> - A los modelos de horario de tipo turno variable también se les llama modelos de horario variables.

1. Para añadir un nuevo modelo de horario, haz clic en el {% icon item-add %}.
2. En el menú desplegable **Tipo**, selecciona el tipo de modelo de horario que quieres configurar.
3. Configura tu modelo de horario.<br>Para aprender más sobre las opciones de configuración de cada tipo de modelo de horario, consulta las siguientes secciones.
4. Para guardar el modelo de horario, haz clic en _Aceptar_{:.doc-button}.

Ahora puedes [añadir actividades](#añadir-actividades-a-modelos-de-horario) al modelo de horario nuevo. 

> Atención
> 
> Si trabajas con un {% link_new número limitado de modelos de horario en tu unidad de planificación | features/administration/create-and-manage-planning-units.md | #limitar-los-modelos-de-horario %}, puede que tengas que añadir los modelos de horario nuevos a tu unidad de planificación. Si usas modelos de planificación, actualiza el modelo o modelos semanales.

### Turno fijo
   
| **Parámetro** | **Descripción** |
|:-----|:-----|
| Nombre | Un nombre inequívoco que describa el modelo de horario. Recomendamos especificar el tipo de modelo de horario y sus horas de inicio y fin, p.&nbsp;ej., 8-16:30-fijo. |
| Abreviatura | Esta versión del nombre aparece en los informes y en Planificar. Recomendamos usar el nombre especificado o una versión más corta del mismo. |
| Atajo de teclado | Atajo de teclado opcional para ayudarte a insertar la actividad más rápidamente en el Centro de planificación. Aprende más sobre los {% link_new atajos de teclado | best-practices/tips-on-shift-center-usage.md %}. |
| Color |  El color aparece en la planificación y en las páginas de datos de configuración.<br>Puede ayudarte a identificar rápidamente la duración, el tipo de modelo de horario o las actividades incluidas. |
| Válido desde/Válido hasta | Período opcional durante el cual se puede utilizar el modelo de horario.<br>Aprende más sobre las {% link_new fechas de validez | features/administration/set-a-validity-period.md %}. |
| Inicio | Hora a la que comienza el turno fijo. |
| Fin | Hora a la que termina el turno fijo. |
| Duración del turno en bruto | Duración del turno en horas.<br>Si configuras este valor, este reemplazará la hora de fin configurada.<br>Ten en cuenta que los modelos de horario de tipo turno fijo pueden abarcar hasta dos días. Para crear un turno nocturno, añade hasta 24 horas a la fecha de fin al crear el modelo de horario, o utiliza la duración total del turno. El valor máximo es 48:00 (horas). |
| Actividad | La primera actividad es la {% link_new actividad base | features/administration/daymodels/daymodel-basics.md | #actividad-base-y-duración-del-turno %}.<br>Ten en cuenta que no puedes cambiar la actividad base una vez hayas guardado el modelo de horario. |


### Turno variable
   
| **Parámetro** | **Descripción** |
|:---------------------|:---------------------|
| Nombre | Un nombre inequívoco que describa el modelo de horario. Recomendamos especificar el tipo de modelo de horario y sus horas de inicio y fin, p.&nbsp;ej., fijo-8-20-8. |
| Abreviatura | Esta versión del nombre aparece en los informes y en Planificar. Recomendamos usar el nombre especificado. |
| Color |  El color aparece en la planificación y en las páginas de datos de configuración.<br>Puede ayudarte a identificar rápidamente la duración, el tipo de modelo de horario o las actividades incluidas. |
| Válido desde/Válido hasta | Período opcional durante el cual se puede utilizar el modelo de horario.<br>Aprende más sobre las {% link_new fechas de validez | features/administration/set-a-validity-period.md %}. |
| Inicio margen temporal | La hora más temprana a la que puede comenzar el turno. |
| Fin del margen temporal | La hora más tardía a la que puede comenzar el turno. |
| Duración margen temporal | Número de horas entre la hora de inicio más temprana y la hora de finalización más tardía del turno.<br>Esto reemplazará el Fin del margen temporal. |
| Duración del turno en bruto | Duración total del turno incluyendo pausas. La duración debe ser más corta que el margen temporal. Si la duración del turno es igual al margen temporal, el modelo de horario se convierte automáticamente en un modelo de horario de tipo turno fijo. |
| Intervalo | Intervalo en el que un turno puede comenzar dentro del margen temporal definido. Por ejemplo, un intervalo de 30 significa que el turno puede empezar cada media hora dentro del margen temporal. |
| Actividad | La primera actividad que añadas será la {% link_new actividad base | features/administration/daymodels/daymodel-basics.md | #actividad-base-y-duración-del-turno %}.<br>Ten en cuenta que no puedes cambiar la actividad base una vez hayas guardado el modelo de horario. |

### Margen de disponibilidad

Usa este tipo de modelo de horario p.&nbsp;ej., en rotaciones de turnos para configurar la disponibilidad de varias personas a la vez. Ten en cuenta que las disponibilidades provenientes de un modelo de horario sobrescriben cualquier disponibilidad introducida por los empleados en injixo Me, así como las disponibilidades añadidas manualmente al Centro de planificación. Aprende más sobre las {% link_new disponibilidades | features/administration/availabilities.md %}.

| **Parámetro** | **Descripción** |
|:---------------------|:---------------------|
| Nombre | Un nombre inequívoco que describa el modelo de horario. Recomendamos especificar el tipo de modelo de horario y sus horas de inicio y fin, p.&nbsp;ej., dispo-8-16. |
| Abreviatura | Esta versión del nombre aparece en los informes y en Planificar. Recomendamos usar el nombre especificado o una versión más corta del mismo. |
| Color |  El color aparece en la planificación y en las páginas de datos de configuración.<br>Puede ser útil cuando configures rotaciones de turnos. |
| Válido desde/Válido hasta | Período opcional durante el cual se puede utilizar el modelo de horario.<br>Aprende más sobre las {% link_new fechas de validez | features/administration/set-a-validity-period.md %}. |
| Inicio margen de disponibilidad | La hora más temprana a la que puede comenzar el turno. |
| Fin margen de disponibilidad | La hora más tardía a la que puede comenzar el turno. |
| Duración margen de disponibilidad | Número de horas entre la hora de inicio más temprana y la hora de finalización más tardía del turno. El valor máximo es 48 horas.<br>Esto reemplazará el fin del margen de disponibilidad. |

## Añadir actividades a modelos de horario

Para hacer un modelo de horario existente aún más específico, puedes añadirle pausas u otras actividades. Configura otras actividades si necesitas representar tareas específicas en las que tus empleados deben trabajar en un momento determinado durante un turno. Estas actividades especiales pueden ser, p.&nbsp;ej., revisar los canales de redes sociales de la organización o tareas de back-office. 

Para poder añadir actividades primero tienes que [crear el modelo de horario](#crear-modelos-de-horario).

La planificación optimizada puede reemplazar actividades de tipo presencia que estén configuradas como reemplazables. Si no quieres planificar actividades especiales para tus empleados, la actividad base será la única actividad de tipo presencia en tu modelo de horario. Ten en cuenta que configurar actividades en modelos de horario limitará la flexibilidad de las funcionalidades de optimización (p.&nbsp;ej., optimización completa, actividades adicionales, reuniones). Para mantener la optimización lo más flexible posible y evitar errores de planificación, recomendamos que solo incluyas actividades de tipo presencia en los modelos de horario si es estrictamente necesario.

> Atención
> 
> La primera actividad que añades a un modelo de horario es automáticamente la actividad base. No puedes cambiar la actividad base una vez hayas guardado el modelo de horario.
> Recomendamos utilizar la actividad Presente como actividad base. Puedes leer más sobre la {% link_new actividad base | features/administration/daymodels/daymodel-basics.md | #actividad-base-y-duración-del-turno %}.

### Añadir una actividad de presencia o ausencia

Para añadir una actividad de presencia o ausencia a un modelo de horario ya existente, sigue estos pasos:

1. Selecciona un modelo de horario.
2. En la sección **Presencias y ausencias**, haz clic en el {% icon item-add %}.<br>Se abre una ventana de diálogo.
3. Configura la actividad:
- **Inicio** y **Fin**:<br>Si la casilla **Relativo al inicio del turno** está marcada: introduce el número de horas y minutos tras el inicio del turno cuando quieres que la actividad comience y termine (p.&nbsp;ej., para una hora y media, introduce 1:30).<br>Si la casilla **Relativo al inicio del turno** no está marcada: introduce la hora exacta (en formato de 24 horas) tras el inicio del turno cuando quieres que que la actividad comience y termine (p.&nbsp;ej., para las 2 de la tarde, introduce 14:00).
- **Duración**: si configuras una duración más larga que el tiempo entre el inicio y fin introducidos, creas un {% link_new pasillo | features/administration/daymodels/daymodel-basics.md | #elementos-fijos-vs-pasillos %} dentro del cual se puede mover la actividad.
- **Intervalo**: recomendamos usar el mismo intervalo que tu ACD. Ten en cuenta que la duración de la actividad tiene que ser divisible por el intervalo seleccionado.<br>Si introduces 0, el tiempo de inicio de la actividad queda fijo y no puede ser movida en el pasillo.
- **Relativo al inicio del turno**:<br>Si está marcada (por defecto), la actividad comienza a la hora y minutos definidos tras el inicio del turno. Si se mueve el turno, la actividad también se mueve.<br>Si no está marcada, la actividad comienza a la hora configurada exacta. Cuando mueves un turno variable, las actividades no se mueven. Esto puede ser útil, p.&nbsp;ej., cuando empleados con diferentes turnos necesitan asistir a una reunión de equipo al mismo tiempo.
4. Selecciona una actividad del menú desplegable.
5. Haz clic en _Aceptar_{:.doc-button}.

### Añadir una actividad de pausa

Tanto en los modelos de horario flexibles como fijos puedes añadir pausas para la planificación optimizada y la oferta de turnos.  
Para añadir una actividad de pausa a un modelo de horario ya existente, sigue estos pasos:

1. Selecciona un modelo de horario.
2. En la sección de **Pausas para la planificación**, haz clic en el {% icon item-add %}.<br>Se abre una ventana de diálogo.
3. Configura la actividad de pausa:
- **Inicio** y **Fin**:<br>Si la casilla **Relativo al inicio del turno** está marcada: introduce el número de horas y minutos tras el inicio del turno cuando quieres que la pausa comience y termine (p.&nbsp;ej., para cuatro horas y media, introduce 4:30). Por defecto, las pausas se introducen en relación al inicio del turno, ya que generalmente comienzan tras un cierto tiempo de trabajo.<br>Si la casilla **Relativo al inicio del turno** no está marcada: introduce la hora exacta (en formato de 24 horas) tras el inicio del turno cuando quieres que que la pausa comience y termine (p.&nbsp;ej., para las 1 de la tarde, introduce 13:00).
- **Duración**: si configuras una duración más larga que el tiempo entre el inicio y fin introducidos, creas un {% link_new pasillo | features/administration/daymodels/daymodel-basics.md | #elementos-fijos-vs-pasillos %} dentro del cual la pausa puede ser movida.
- **Intervalo**: recomendamos usar el mismo intervalo que tu ACD. Ten en cuenta que la duración de la pausa tiene que ser divisible por el intervalo seleccionado.<br>Si introduces 0, el tiempo de inicio de la pausa queda fijado y no puede ser movida en el pasillo.
- **Relativo al inicio del turno**:<br>Si está marcada (por defecto), la pausa comienza a la hora y minutos definidos tras el inicio del turno. Si se mueve el turno, la pausa también se mueve.<br>Si no está marcada, la actividad comienza a la hora configurada exacta. Cuando mueves un turno variable, las pausas no se mueven. Esto puede ser útil si, p.&nbsp;ej., la cafetería de tu organización solo está abierta durante un tiempo limitado.
4. Selecciona una opción de pausa en el menú **Pausa**.
5. Haz clic en _Aceptar_{:.doc-button}.

Ten en cuenta que en injixo Enterprise WFM on-premise, el ajuste 48134 determina si los pasillos de pausa se mantienen o si son convertidos en elementos fijos.

## Efectos de modificar modelos de horario en uso

Modificar modelos de horario que se usan en tu planificación puede tener diferentes efectos. Puedes cambiar sin preocuparte los datos de configuración que no son relevantes para la planificación, como el nombre, la abreviatura o el color.

Sin embargo, recomendamos que solo hagas cambios en los datos relevantes para la planificación, como las horas de inicio y finalización, la duración total del turno, las presencias y ausencias o pausas, antes de crear tu próxima planificación. Cuando cambias un modelo de horario existente, injixo crea una copia interna del modelo de horario original. De esta manera, los turnos que ya están planificados se mantienen y siguen siendo mostrados.

Tras cambiar un modelo de horario existente o tras crear uno nuevo, recomendamos empezar de nuevo el proceso de planificación para que los nuevos modelos de horario nuevos o modificados sean usados correctamente.

Los modelos de horario afectados serán cambiados en las rotaciones de turnos y modelos semanales. Los modelos de horario ya planificados se mostrarán con una línea de puntos en la parte inferior en el Centro de planificación y en Planificar. Los turnos con este modelo de horario ya no pueden ser planificados o editados. Solo pueden ser eliminados de la planificación.

Si has creado turnos a partir de un modelo de horario y tus empleados ya han solicitado estos turnos en injixo Me durante el proceso de oferta de turnos, tus empleados ya no podrán ver o solicitar los turnos de ese modelo de horario.
Las turnos ya solicitados no serán utilizados en sorteos o asignaciones posteriores.

Ten en cuenta que los valores mínimos y máximos introducidos como requisitos de turno aún se aplican al modelo de horario modificado.
