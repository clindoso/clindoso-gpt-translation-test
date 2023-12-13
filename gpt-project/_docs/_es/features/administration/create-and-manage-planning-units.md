---
title: Crear y gestionar unidades de planificación
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprende cómo crear, configurar y eliminar unidades de planificación.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-use-virtual-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
---

Las unidades de planificación agrupan empleados y datos de configuración que se usan durante la planificación. Las ubicaciones de tu organización no tienen por qué corresponder con tus unidades de planificación. Por ejemplo, si tienes empleados que trabajan en dos ubicaciones diferentes, puedes {% link_new asignarlos | features/administration/employee-overview.md | #configurar-los-ajustes-de-empleado %} a una única unidad de planificación. Recomendamos usar solo una unidad de planificación, excepto en los siguientes casos:

- Tienes empleados que trabajan en distintas zonas horarias. En este caso, usa una unidad de planificación para cada zona horaria.
- En tu organización, distintos planificadores coordinan distintos grupos de empleados, p.&nbsp;ej., empleados pertenecientes a distintas unidades de negocio.

injixo Advanced y Enterprise WFM ofrecen roles de usuario personalizables para limitar el acceso de los usuarios a las distintas unidades de planificación.

Si trabajas con varias unidades de planificación, puedes transferir temporalmente empleados de una unidad de planificación a otra. Aprende más sobre cómo {% link_new transferir empleados | features/administration/employee-overview.md | #transferir-empleados %}.

## Crear unidades de planificación

1. Ve a _Plan > Configuración > Unidades de planificación_{:.breadcrumbs}.
2. Haz clic en el icono Nuevo {% icon item-add | icon-only %} arriba a la izquierda.  
   Se abre un panel de configuración a la derecha.
3. Completa los siguientes campos:

   - **Nombre**: nombre único para la unidad de planificación (máximo 50 caracteres).
   - **Abreviatura**: abreviatura del nombre (máximo 25 caracteres).
   - **Color**: color opcional para la unidad de planificación. Verás el color en Planificar.
   - **Intervalo**: influencia el nivel de detalle con el que se muestran los datos en Planificar, como la cobertura y los requisitos de personal. El intervalo de la unidad de planificación no debe ser más largo que el intervalo de importación de tus datos de contacto y datos de los estados de los agentes. El menú desplegable muestra los intervalos de las unidades de planificación en minutos. Recomendamos usar **15 minutos**. No podrás modificar el intervalo una vez lo hayas guardado. Aprende más sobre la {% link_new importación de datos a través de integraciones | features/acd-integration/cloud/how-integrations-work.md %}.
   - **Unidad de planificación primaria**: unidad de planificación opcional que contiene la unidad de planificación que estás creando. Aprende más sobre las {% link_new unidades de planificación primarias | best-practices/how-to-use-virtual-planning-units.md %}.
   - **Zona horaria**: zona horaria de la unidad de planificación. No podrás modificar la zona horaria una vez hayas guardado la unidad de planificación. Aprende más sobre cómo {% link_new trabajar con zonas horarias | best-practices/working-with-timezones.md %}.

     > Atención
     >
     > La zona horaria seleccionada debe coincidir con la zona horaria de tus cargas de trabajo en Forecast. De lo contrario, no podrás transferir requisitos de personal para la planificación. Las integraciones ajustarán los datos importados según la zona horaria de tus cargas de trabajo.

4. Haz clic en _Aceptar_{:.doc-button}.  
   Ahora puedes añadir horarios de apertura y actividades, o [limitar los modelos de día](#limitar-los-modelos-de-horario).

### Añadir horarios de apertura

Para añadir horarios de apertura a una unidad de planificación, primero debes terminar de [crear la unidad de planificación](#crear-unidades-de-planificación).

Para poder crear planificaciones debes añadir horarios de apertura a tu unidad de planificación. Los horarios de apertura limitan las horas diarias para las que puedes {% link_new calcular requisitos de personal | features/forecast/injixo-forecast/staff-requirement.md %} y {% link_new crear planificaciones optimizadas | features/scheduling/schedules/schedules-optimized-schedules.md %}. <!-- special public holiday day types or part of the linked article? -->

1. En la sección **Horario de apertura** del panel de configuración de la unidad de planificación, haz clic en el icono Insertar {% icon item-add | icon-only %} para añadir los horarios de apertura para ciertos tipos de día.  
   Se abre una ventana de diálogo.
2. En la sección **Tipos de día**, selecciona uno o varios {% link_new tipos de día | features/administration/day-types.md %}.
3. Introduce la hora de inicio y fin en los campos **desde** y **hasta** (en formato de 24 horas). Si tu organización abre las 24 horas, introduce 00:00 en ambos campos.
4. (Opcional) Introduce en los campos **Válido desde** y **Válido hasta** el rango de fechas en el que las horas de apertura son válidas. Si el horario de apertura es válido de forma indefinida, deja los campos en blanco. Aprende más sobre los {% link_new períodos de validez | features/administration/set-a-validity-period.md %}.
5. Haz clic en _Aceptar_{:.doc-button}.

Para modificar o eliminar el horario de apertura, haz clic en el icono Editar {% icon item-edit | icon-only %} o en el icono Eliminar {% icon item-delete | icon-only %}.

### Añadir actividades

Para añadir actividades a una unidad de planificación, primero debes terminar de [crear la unidad de planificación](#crear-unidades-de-planificación).

Para poder crear planificaciones debes añadir actividades a las unidades de planificación. Solo puedes planificar empleados para actividades que hayas añadido a la unidad de planificación. Por defecto, todas las unidades de planificación incluyen la actividad Presente. La actividad Presente no puede ser eliminada.

Para añadir actividades a una unidad de planificación, sigue estos pasos:

1. En la sección **Actividades** del panel de configuración de la unidad de planificación, haz clic en el icono Insertar {% icon item-add | icon-only %}.  
   Se abre una ventana de diálogo.
2. Haz clic en la actividad que quieres añadir.
3. (Opcional) Introduce un periodo de tiempo en los campos **desde** y **hasta**. La funcionalidad {% link_new Crear horarios optimizados | features/scheduling/schedules/schedules-optimized-schedules.md %} tendrá en cuenta esta actividad solo durante el periodo de tiempo que has definido. Si ambos campos tienen el valor 00:00, injixo tendrá en cuenta las horas de apertura de la unidad de planificación. Los usuarios con acceso de administrador pueden cambiar este comportamiento predeterminado con el ajuste _48408_{:.id-label}.
4. (Opcional) Introduce en los campos **Válido desde** y **Válido hasta** el rango de fechas en el que la actividad está disponible para la planificación. Deja los campos **Válido desde** y **Válido hasta** en blanco si quieres que la actividad esté siempre disponible.
5. Haz clic en _Aceptar_{:.doc-button}.

Para editar o eliminar una actividad, haz clic en el icono Editar {% icon item-edit | icon-only %} o en el icono Eliminar {% icon item-delete | icon-only %}.

### Añadir multiactividades

Para añadir una {% link_new multiactividad | features/administration/activity-types-and-properties.md | #subactividades %} a una unidad de planificación, primero debes añadir todas sus subactividades. La multiactividad aparece en negrita en la lista de actividades. Las multiactividades no están disponibles en injixo Essential WFM.

### Limitar los modelos de horario

Los {% link_new modelos de horario | features/administration/daymodels/daymodel-creation.md %} son asignados por defecto a tus unidades de planificación. Si no quieres usar todos los modelos de horario en una unidad de planificación, puedes limitar la cantidad de modelos de horario usados para esa unidad de planificación.

Limitar los modelos de horario puede acelerar el proceso de planificación con la funcionalidad Crear horarios optimizados. Sin embargo, solo puedes utilizar los modelos de horario restantes para generar turnos, crear informes o crear planificaciones optimizadas. Esto puede requerir un mayor esfuerzo a la hora de mantener los otros datos de configuración, como los modelos semanales. Eliminar un modelo de horario en uso no afecta a las planificaciones y turnos creados con ese modelo de horario.

> Atención
> 
> Si eliminas todos los modelos de horario de la unidad de planificación, la única forma de planificar turnos será añadir manualmente actividades a la planificación, o bien {% link_new insertar actividades en las rotaciones de turnos | features/administration/shift-sequences.md %}. Los demás enfoques de planificación (Crear planificación optimizada o los modelos de planificación) dejarán de funcionar.

Para limitar el número de modelos de horario, sigue estos pasos:

1. Ve a _Plan > Configuración > Unidades de planificación_{:.breadcrumbs}.
2. Selecciona la unidad de planificación que quieres editar y desplázate a la sección **Modelos de horario**.
3. Haz clic en el icono Editar {% icon item-edit | icon-only %} junto a la opción de configuración predeterminada **[Todos]** y selecciona un modelo de horario. También puedes hacer clic en el icono Eliminar {% icon item-delete | icon-only %} para eliminar la opción **[Todos]**. Para limitar el número de modelos de horario tienes que sustituir o eliminar la opción **[Todos]**. No puedes añadir modelos de horario a una unidad de planificación más de una vez.
   Omite el paso 3 si quieres poder añadir más modelos de día más adelante.
4. Haz clic en el icono Insertar {% icon item-add | icon-only %} para añadir uno o varios modelos de horario.
5. Haz clic en _Aceptar_{:.doc-button}.

Para editar o eliminar un modelo de horario, haz clic en el icono Editar {% icon item-edit | icon-only %} o en el icono Eliminar {% icon item-delete | icon-only %}.

## Eliminar unidades de planificación

> Advertencia
> 
> Si eliminas una unidad de planificación, también se eliminarán las planificaciones asociadas.

1. Ve a _Plan > Configuración > Unidades de planificación_{:.breadcrumbs}.
2. En la lista, haz clic en la unidad de planificación que deseas eliminar.
3. Para asegurarte de que los datos de planificación siguen apareciendo correctamente, elimina las actividades y los modelos de horarios asignados de la unidad de planificación antes de eliminarla.
4. Haz clic en el icono Eliminar {% icon item-delete | icon-only %} arriba a la izquierda.
5. Para confirmar, haz clic en _Sí_{:.doc-button}.
