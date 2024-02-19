---
title: Filtrar con grupos
description: Aprende a usar los grupos como filtro.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
---

¿Es la primera vez que trabajas con grupos? Consulta primero {% link_new la información básica | features/administration/selections.md %}.

Cuando gestionas tu equipo, a menudo necesitas agrupar a empleados con condiciones laborales similares, p.&nbsp;ej. empleados con hijos en edad preescolar, o empleados que comparten un mismo supervisor. Con los grupos puedes crear tus propios criterios de agrupación. Esto es útil si necesitas opciones de agrupación más allá del alcance de las {% link_new unidades de planificación | features/administration/create-and-manage-planning-units.md %} y los {% link_new filtros avanzados | features/administration/employee-filter.md %}.

Las unidades de planificación te ayudan a agrupar empleados según la estructura de tu organización, p.&nbsp;ej., si asignas empleados en diferentes zonas horarias a diferentes unidades de planificación; y los filtros avanzados funcionan de acuerdo con los elementos de configuración de injixo, como contratos y actividades. Los grupos te ayudan a agrupar personas para satisfacer las necesidades específicas de tu organización.

Puedes crear un grupo para refinar los filtros dentro de una unidad de planificación o para gestionar empleados en varias unidades de planificación. Puedes, p.&nbsp;ej. crear un grupo para asegurarte de que las planificaciones de los empleados con hijos en edad preescolar se gestionen por separado; o para filtrar las planificaciones de empleados de diferentes unidades de planificación para una campaña de marketing en diferentes zonas horarias.

## Usar grupos para filtrar empleados dentro de una unidad de planificación

injixo ofrece filtros por unidad de planificación y grupo en **Plan** e **Intraday**. Después de seleccionar la unidad de planificación, también puedes filtrar los empleados por grupo.

Por ejemplo, si tienes tres unidades de planificación y una de las unidades de planificación incluye empleados que están participando en un programa de formación, puedes usar los grupos para agrupar a estos empleados y gestionar sus planificaciones por separado, p.&nbsp;ej., para planificar reuniones específicas.

## Usar grupos para gestionar empleados en distintas unidades de planificación

En injixo, hay tres formas de filtrar por grupos abarcando todas las unidades de planificación. Puedes encontrar ejemplos sobre cómo filtrar por grupos bajo esta sección.

La siguiente tabla ofrece un resumen de las tres opciones para filtrar por grupo en todas las unidades de planificación. Puedes encontrar estas opciones en los componentes o funcionalidades de injixo.

| Componente/funcionalidad | Opción de filtrado |
|-------------------------|----------------------------|
| Planificar               | Todas las unidades de planificación y un grupo. |
| Vacaciones/Ausencias                | Todas las unidades de planificación y un grupo. |
| Adherencia en tiempo real     | Un grupo y ninguna unidad de planificación. |
| Adherencia intradiaria      | Un grupo y ninguna unidad de planificación. |
| Centro de planificación            | Un grupo (no hay filtro de unidad de planificación disponible). |
| Notificar empleados           | Una unidad de planificación y un grupo. Repítelo por cada unidad de planificación que quieras filtrar. |
| Períodos de planificación  | Una unidad de planificación y un grupo. Repítelo por cada unidad de planificación que quieras filtrar. |
| Reuniones                | Una unidad de planificación y un grupo. Repítelo por cada unidad de planificación que quieras filtrar. |
| Períodos de permiso        | Una unidad de planificación y un grupo. Repítelo por cada unidad de planificación que quieras filtrar. |
| Derecho de vacaciones    | Una unidad de planificación y un grupo. Repítelo por cada unidad de planificación que quieras filtrar. |

Para todas las funcionalidades en _Plan > Planificar > Acciones de planificación_{:.breadcrumbs} tienes que seleccionar una unidad de planificación y un grupo y aplicar la acción de planificación a cada unidad de planificación que quieras filtrar.

Los siguientes ejemplos dan más detalles sobre las tres opciones de filtrado para grupos descritas en la tabla anterior.

## Ejemplos

Los ejemplos a continuación usan un grupo llamado Onboarding. El grupo Onboarding tiene como objetivo agrupar a los empleados que se han incorporado recientemente a tu organización, independientemente de su unidad de planificación. Usar el grupo Onboarding facilita la gestión de sus planificaciones y el seguimiento de sus necesidades.

Con la siguiente configuración, puedes usar el grupo Onboarding como filtro en todas las unidades de planificación:

1. {% link_new Crea y configura un grupo | features/administration/selections.md | #crear-grupos %} con el nombre Onboarding.
2. {% link_new Asigna a los empleados | features/administration/selections.md | #asignar-empleados-a-grupos %} que están en la fase de incorporación al grupo Onboarding.

### Opción de filtrado 1: todas las unidades de planificación y un grupo

En _Plan > Planificar_{:.breadcrumbs} puedes filtrar las planificaciones de los empleados en el grupo Onboarding con los siguientes menús desplegables:

- **Unidad de planificación**: selecciona **Todas las unidades de planificación**.
- **Elige Grupo**: selecciona Onboarding.  
   Si no ves el menú desplegable **Elige Grupo**, haz clic en el icono {% icon selection-filter-u %} arriba a la izquierda.

### Opción de filtrado 2: un grupo y ninguna unidad de planificación

En _Intraday > Adherencia en tiempo real_{:.breadcrumbs} puedes filtrar las actividades planificadas para los empleados en el grupo Onboarding y compararlas con el estado actual de los empleados en tiempo real. Esto es útil para verificar, p.&nbsp;ej., si un empleado está llevando a cabo las actividades planificadas para su fase de incorporación.

Para filtrar por grupo, usa los siguientes menús desplegables:

- **Unidad de planificación**: asegúrate de no haber seleccionado ninguna unidad de planificación.
- **Grupo**: selecciona **Onboarding**.

### Opción de filtrado 3: un grupo y una unidad de planificación

Si tienes condiciones específicas de permisos para los empleados en la fase de incorporación, puedes crear períodos de permiso específicos para el grupo Onboarding. Imagina que tienes las siguientes unidades de planificación para tres oficinas diferentes: Oficina 1, Oficina 2 y Oficina 3. Estas tres oficinas tienen empleados en fase de incorporación que están asignadas al grupo Onboarding.

Para crear períodos de permiso específicos para el grupo Onboarding, sigue estos pasos:

1. En _Plan > Ausencias/Permisos_{:.breadcrumbs}, haz clic en _Períodos para permisos_{:.doc-button}.  
   injixo te redirige a la página **Períodos para permisos**.
2. Haz clic en _Nuevo periodo de disfrute_{:.doc-button}.  
   Se abre una ventana de diálogo.
3. Para filtrar por grupo, usa los siguientes menús desplegables:  
   - **Unidad de planificación**: selecciona **Oficina 1**.
   - **Grupo**: selecciona **Onboarding**.
4. Completa los campos restantes.  
   Aprende más información sobre cómo configuración los {% link_new períodos para permisos | features/scheduling/time-off/time-off-periods.md %}.
5. Haz clic en _Guardar_{:.doc-button}.
6. Repite los pasos 1 al 5 para las unidades de planificación Oficina 2 y Oficina 3.
