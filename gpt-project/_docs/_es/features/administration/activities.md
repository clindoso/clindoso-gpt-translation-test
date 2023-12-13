---
title: Crear actividades
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
beta-feature: false
description: Crea actividades para representar las tareas planificadas y no planificadas de tu organización.
related_articles:
  - overwrite_title: Ejemplos de actividades
    filepath: features/administration/activity-examples.md
  - overwrite_title: Configurar actividades
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Para crear, editar y eliminar actividades, ve a _Plan > Configuración > Actividades_{:.breadcrumbs}.

Las actividades representan todas las actividades que se planifican e incluyen en informes en tu organización, como llamadas, pausas, permisos o reuniones. Puedes crear tantas actividades como quieras. El número de actividades dependerá de cuántas tareas quieras diferenciar y con qué nivel de detalle.

Las actividades son una parte esencial del proceso de planificación en injixo. Están vinculadas a otros elementos de configuración, como {% link_new unidades de planificación | features/administration/create-and-manage-planning-units.md | #añadir-actividades %} y {% link_new modelos de horario | features/administration/daymodels/daymodel-basics.md %}. También forman parte de las planificaciones gestionadas en el {% link_new Centro de planificación | features/scheduling/shiftcenter/add-and-delete-items.md %} o en {% link_new Planificar | features/scheduling/schedules/schedules-edit.md %}.

injixo incluye dos actividades preconfiguradas (no eliminables):

- Presente: Esta actividad se utiliza como marcador de posición en los modelos de horario. Durante la planificación, injixo reemplaza esta actividad por otras actividades que estén configuradas como planificables.
- Vacaciones: Esta actividad se utiliza para planificar vacaciones pagadas. Crea una actividad separada para permisos no remunerados.

## Crear una actividad

1. Haz clic en _Nueva actividad_{:.doc-button}.
2. Introduce la información general de tu actividad:
   - **Nombre**: un nombre inequívoco que describa la actividad. La abreviatura se genera automáticamente.
   - **Tipo**: el tipo determina cómo injixo usa las actividades en la planificación y cómo aparecen en otras partes de la aplicación y en los informes. Aprende más sobre los distintos {% link_new tipos de actividades | features/administration/activity-types-and-properties.md | #tipos-de-actividades %}.
   - **Color**: El color aparece en las páginas de planificación y de datos de configuración. Puede ayudar a identificar las distintas actividades.
   - **Atajo de teclado**: Atajo de teclado opcional para ayudarte a insertar la actividad más rápidamente en el Centro de planificación. Aprende más sobre los {% link_new atajos de teclado | best-practices/tips-on-shift-center-usage.md | #tip-2-shortcuts-for-a-quick-assignment-of-activities %}.
   - **Nombre oficial y abreviatura oficial**: Nombre alternativo que se puede utilizar para informes internos e integraciones. injixo Me siempre muestra el nombre definido en **Nombre**.
3. Marca una o varias casillas para definir las {% link_new propiedades de la actividad | features/administration/activity-types-and-properties.md | #propiedades-de-las-actividades %}.
  Si marcas Planificable, puedes editar el {% link_new valor de importancia | best-practices/importance-for-activities.md %}.
  Si marcas Reemplazable, puedes editar el {% link_new valor de prioridad | best-practices/priority-for-activities.md %}.
4. (Opcional) {% link_new Asigna cualificaciones | features/administration/work-with-skills.md | #añadir-cualificaciones-a-actividades %} a la actividad.
5. Haz clic en _Crear actividad_{:.doc-button}.

Aprende más sobre {% link_new tipos y propiedades de actividades | features/administration/activity-types-and-properties.md %}.

### Identificador (ID) de actividad

Para ver el ID de una actividad, puedes: 
- Haz clic en una actividad en la lista **Actividades**. La URL en la barra de tu navegador muestra el ID de la actividad seleccionada (p.&nbsp;ej., https://www.injixo.com/plan/configuration/activities/1234).
- Usa la API de injixo. Aprende cómo [gestionar actividades a través de la API de injixo](https://api.injixo.com/resources/activities/).

## Multiactividades y subactividades 


Las multiactividades te permiten planificar a empleados con múltiples cualificaciones cuando se requiera una de sus cualificaciones. Puedes convertir una actividad en una multiactividad {% link_new asignándole otras actividades | features/administration/activity-types-and-properties.md | #subactividades %}. Las actividades asignadas se convierten en sus subactividades.  En la lista de las actividades, las multiactividades están marcadas con el icono <em class="multiactivity-icon"></em>.

Si una actividad es una subactividad, al hacer clic en ella puedes ver la sección **Multiactividades**, que muestra todas las multiactividades a las que está asignada.

Si una actividad no es una subactividad, al hacer clic en ella puedes ver la sección **Subactividades**, donde puedes seleccionar otras actividades para convertirlas en subactividades de la actividad que estás editando. La actividad en sí se convierte en una multiactividad.
Solo puedes asignar subactividades a una actividad después de haberla creado.

## Sistemas externos

<!-- will be made obsolete by the new activity mapping page. Will require a separate article -->

Puedes asignar estados o actividades usados en sistemas externos a actividades en injixo.
1. Selecciona una actividad de la lista, desplázate hasta la sección **Sistemas externos** y haz clic en _Editar en WFM_{:.doc-button}.
2. Navega hasta la sección **Sistemas externos**.
3. Haz clic en el {% icon item-add %}.
4. Selecciona un **sistema externo**, un **nombre del sistema externo** y una **clasificación** en los menús desplegables.
5. Haz clic en _Aceptar_{:.doc-button}.

> Solo puedes asignar una actividad de un sistema externo a una sola actividad en injixo.

## Duplicar una actividad

Para crear una actividad nueva con las mismas propiedades generales que otra actividad ya existente, sigue estos pasos:

1. En la lista **Actividades**, selecciona una actividad.
2. Haz clic en **Duplicar actividad** bajo el nombre de la actividad.  
La ventana **Crear nueva actividad** se abre con casillas preseleccionadas. Las cualificaciones y subactividades asignadas no se duplican.
3. Introduce un **nombre** para la nueva actividad.
4. (Opcional) Modifica el color y las demás propiedades.
5. Haz clic en _Crear actividad_{:.doc-button}.

## Editar o eliminar una actividad

1. En la lista **Actividades**, selecciona una actividad.
  - Para editar la actividad, edita la información que deseas cambiar y haz clic en _Guardar cambios_{:.doc-button}.
  - Para eliminar la actividad, haz clic en _Eliminar actividad_{:.doc-button} abajo a la derecha.

Si la actividad eliminada estaba asignada a otros elementos de configuración, como unidades de planificación o modelos de horario, su nombre aparecerá en cursiva en estos elementos. Una actividad eliminada pierde sus asignaciones a otros elementos pero seguirá siendo visible en los datos de configuración. Puede que necesites volver a crear los modelos de horario existentes que utilizaban la actividad eliminada.

En el Centro de planificación las actividades eliminadas aparecen {% link_new rodeadas por una línea discontinua | features/scheduling/shiftcenter/shift-center-overview.md | #how-are-items-displayed %}. Planificar muestra las actividades eliminadas como un espacio gris y sin nombre. La información original de la planificación sigue estando disponible, excepto en la vista diaria.
