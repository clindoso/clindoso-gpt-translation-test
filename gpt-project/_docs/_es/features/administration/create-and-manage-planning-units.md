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
---

Las unidades de planificación agrupan empleados y datos de configuración que se usan durante la planificación. Las ubicaciones de tu organización no tienen por qué corresponder con tus unidades de planificación. Por ejemplo, si tienes empleados que trabajan en dos ubicaciones diferentes, puedes {% link_new asignarlos | features/administration/employee-overview.md | #configurar-los-ajustes-de-empleado %} a una única unidad de planificación.

## ¿Cuántas unidades de planificación debería usar?
	
Para reducir esfuerzos, puedes usar {% link_new grupos | features/administration/selections.md %} para planificar empleados que trabajan en sedes o equipos distintos en una unidad de planificación. Usa más de una unidad de planificación en los siguientes casos:
-  Los empleados trabajan en distintas zonas horarias. 
-  Los planificadores son responsables solamente de ciertos grupos de empleados, p.&nbsp;ej. unidades operacionales. En injixo Advanced y Enterprise WFM, los roles de usuario personalizados pueden {% link_new restringir el acceso a las unidades de planificación | getting-started/configure-user-roles.md | #gestionar-el-acceso-a-los-equipos-restringir-el-acceso-a-los-datos-de-configuración %}.
- Tienes requisitos de personal compartidos, p.&nbsp;ej. para escenarios de desbordamiento.
- Quieres crear informes que incluyan números totales de múltiples unidades de planificación.
	
	
> Consejos para trabajar con múltiples unidades de planificación
>
> - Para agrupar figuras pertenecientes a distintas unidades de planificación, añade una unidad de planificación primaria a todas las unidades de planificación relevantes.
> - Puedes transferir temporalmente empleados de una unidad de planificación a otra.<br>Aprende más sobre cómo {% link_new transferir empleados | features/administration/employee-overview.md | #transferir-empleados %}.
	
<!-- Typically, you assign one planning unit to a person at a time. Reassign a planning unit using valid from and valid to dates in the employee configuration. In rare cases, you will need to assign more than one planning unit to a person. The person's main planning unit is assigned with priority 1. The person is scheduled in this main planning unit. A person's schedule will be displayed in other planning units with lower priority. You can also manually reschedule people in other planning units if needed. -->

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
   Ahora puedes añadir horarios de apertura y actividades, o [limitar los modelos de horario](#limitar-los-modelos-de-horario).

### Añadir horarios de apertura

Para añadir horarios de apertura a una unidad de planificación, [crea la unidad de planificación](#crear-unidades-de-planificación).

Para crear planificaciones tienes que añadir horarios de apertura a los tipos de día incluidos en tu unidad de planificación. Los horarios de apertura limitan las horas diarias para las que puedes {% link_new calcular requisitos de personal | features/forecast/injixo-forecast/calculate-staff-requirements.md %} y {% link_new crear planificaciones optimizadas | features/scheduling/schedules/schedules-optimized-schedules.md %}. <!-- special public holiday day types or part of the linked article? -->

1. En la sección **Horario de apertura** del panel de configuración de la unidad de planificación, haz clic en el icono Insertar {% icon item-add | icon-only %}.
   Se abre una ventana.
2. En la sección **Tipos de día**, selecciona uno o varios {% link_new tipos de día | features/administration/day-types.md %}.
3. Introduce la hora de inicio y fin en los campos **desde** y **hasta** (en formato de 24 horas). Si tu organización abre las 24 horas, introduce 00:00 en ambos campos.
4. (Opcional) Introduce en los campos **Válido desde** y **Válido hasta** el rango de fechas en el que las horas de apertura son válidas. Si el horario de apertura es válido de forma indefinida, deja los campos en blanco. Aprende más sobre los {% link_new períodos de validez | features/administration/set-a-validity-period.md %}.
5. Haz clic en _Aceptar_{:.doc-button}.

Para modificar o eliminar el horario de apertura, haz clic en el icono Editar {% icon item-edit %} o en el icono Eliminar {% icon item-delete %}.

### Añadir actividades

Para añadir actividades a una unidad de planificación, [crea la unidad de planificación](#crear-unidades-de-planificación).

Antes de crear planificaciones, tienes que añadir todas las actividades relevantes de tipo Presencia a las unidades de planificación. Solo puedes planificar empleados para actividades que hayas añadido a su unidad de planificación. Por defecto, todas las unidades de planificación incluyen la actividad Presente, que no puede ser eliminada.
Para incluir actividades de cualquier tipo en tus informes, añade las actividades a las unidades de planificación relevantes.

Para añadir actividades a una unidad de planificación, sigue estos pasos:

1. En la sección **Actividades** del panel de configuración de la unidad de planificación, haz clic en el icono Insertar {% icon item-add | icon-only %}.  
   Se abre una ventana nueva.
2. Haz clic en la actividad que quieres añadir.
3. (Opcional) Introduce un periodo de tiempo en los campos **desde** y **hasta**. La funcionalidad {% link_new Crear planificación optimizada | features/scheduling/schedules/schedules-optimized-schedules.md %} tendrá en cuenta esta actividad solo durante el periodo de tiempo que has definido. Si ambos campos tienen el valor 00:00, injixo tendrá en cuenta las horas de apertura de la unidad de planificación. Los usuarios con acceso de administrador pueden cambiar este comportamiento predeterminado con el ajuste _48408_{:.id-label}.
4. (Opcional) Introduce un rango de fechas en los campos **Válido desde** y **Válido hasta** para limitar cuándo la actividad está disponible para la planificación.<br>Deja los campos **Válido desde** y **Válido hasta** en blanco si quieres que la actividad esté siempre disponible.
5. Haz clic en _Aceptar_{:.doc-button}.

Para editar o eliminar una actividad, haz clic en el icono Editar {% icon item-edit %} o en el icono Eliminar {% icon item-delete %}.

### Añadir multiactividades

Para añadir una {% link_new multiactividad | features/administration/activity-types-and-properties.md | #subactividades %} a una unidad de planificación, primero debes añadir todas sus subactividades. La multiactividad aparece en negrita en la lista de actividades. Las multiactividades no están disponibles en injixo Essential WFM.

### Limitar los modelos de horario

Los {% link_new modelos de horario | features/administration/daymodels/daymodel-creation.md %} son asignados por defecto a tus unidades de planificación. Si no quieres usar todos los modelos de horario en una unidad de planificación, puedes limitar la cantidad de modelos de horario usados para esa unidad de planificación.

Limitar los modelos de horario puede acelerar el proceso de planificación con la funcionalidad **Crear planificación optimizada**. Sin embargo, solo puedes utilizar los modelos de horario restantes para generar turnos, crear informes o crear planificaciones optimizadas. Esto puede requerir un mayor esfuerzo a la hora de mantener los otros datos de configuración, como los modelos semanales. Eliminar un modelo de horario en uso no afecta a las planificaciones y turnos creados con ese modelo de horario.

> Atención
> 
> Si eliminas todos los modelos de horario de la unidad de planificación, solo podrás planificar actividades manualmente, o bien {% link_new insertándolas en rotaciones de turnos | features/administration/shift-sequences.md %}. Ya no podrás usar la funcionalidad **Crear planificación optimizada**.

Para limitar el número de modelos de horario, sigue estos pasos:

1. Ve a _Plan > Configuración > Unidades de planificación_{:.breadcrumbs}.
2. Selecciona la unidad de planificación que quieres editar y desplázate a la sección **Modelos de horario**.
3. Para limitar el número de modelos de horario, sustituye o elimina la asignación de modelos de horario predefinada.
   - Haz clic en el {% icon item-edit %} junto a la opción **[Todos]** y selecciona un modelo de horario.
   - Haz clic en el {% icon item-delete %} para eliminar la opción **[Todos]**.
4. Haz clic en el icono Insertar {% icon item-add %} para añadir uno o varios modelos de horario. No puedes añadir el mismo modelo de horario dos veces. Para editar o eliminar un modelo de horario añadido, haz clic en el {% icon item-edit %} o en el {% icon item-delete %}.
5. Haz clic en _Aceptar_{:.doc-button}.

## Eliminar unidades de planificación

> Advertencia
> 
> Si eliminas una unidad de planificación, no podrás acceder a las planificaciones asociadas.

1. Ve a _Plan > Configuración > Unidades de planificación_{:.breadcrumbs}.
2. Selecciona la unidad de planificación que quieres eliminar.
3. Haz clic en el {% icon item-delete %} arriba a la izquierda.
4. Para confirmar, haz clic en _Sí_{:.doc-button}.
