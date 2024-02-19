---
title: Configurar empleados
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Crea y configura empleados que quieras incluir en la planificación.
related_articles:
  - overwrite_title: Panorámica del Centro de planificación
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Requisitos de personal
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Optimización de tareas
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Planificación optimizada
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

injixo ofrece tres lugares donde puedes crear y editar empleados, dependiendo del contexto de uso. La tabla a continuación te ofrece una visión general de dónde puedes configurar empleados en injixo y describe qué puedes hacer en cada lugar.

| Dónde                                           | Qué puedes hacer              |
| ----------------------------------------------- | ------------------------ |
| _Plan > Configuración > Empleados_{:.breadcrumbs}   | {% link_new Configurar un empleado para la planificación | features/administration/employee-overview.md | #panorámica-de-los-ajustes-de-empleado %}. Los empleados que no estén asignados a ninguna unidad de planificación no aparecerán en la lista.      |
| _Account > Usuarios_{:.breadcrumbs}                                 | Gestiona los permisos de acceso de los usuarios mediante {% link_new roles de usuario | getting-started/configure-user-roles.md | #crear-un-nuevo-rol-de-usuario %}, {% link_new desbloquear usuarios bloqueados | getting-started/manage-user-accounts.md | #desbloquear-usuarios %}, {% link_new establecer contraseñas nuevas para los usuarios | getting-started/manage-user-accounts.md | #establecer-una-contraseña-nueva-para-un-usuario %}, y {% link_new comprobar qué usuarios se incluyen en la facturación | getting-started/how-does-billing-work.md | #consultar-los-usuarios-facturados-y-no-facturados %} y cuáles no. También puedes {% link_new eliminar usuarios | getting-started/manage-user-accounts.md | #eliminar-una-cuenta-de-usuario %} para que sean excluidos de la facturación. |
| **People**                                                           | {% link_new Crear y gestionar | features/people/manage-people.md %} cuentas de empleados y gestionar la información de contacto y dirección. |

En _Plan > Configuración > Empleados_{:.breadcrumbs}, los usuarios sin acceso de administrador solo pueden ver a los empleados asignados a las unidades de planificación para las que tienen permisos. Los empleados que no están asignados a ninguna unidad de planificación no aparecen en la lista, incluso si seleccionas Todas/Todos en los menús desplegables de unidad de planificación y selección. Los usuarios con acceso de administrador pueden ver todos los empleados.

Los empleados y usuarios están sincronizados, por lo que solo tienes que crear cada empleado una única vez y también se facturará una sola vez.

> A tu organización se le {% link_new facturará | getting-started/how-does-billing-work.md %} cada empleado o usuario que crees en una de las tres secciones hasta que los {% link_new desactives o elimines | features/administration/deactivate-employees.md %}.

## Crear un empleado

Para crear un empleado con la configuración básica, injixo requiere que completes todos los campos obligatorios. Antes de configurar al empleado para la planificación, debes [configurar](#configurar-los-ajustes-de-empleado) diversos otros [ajustes del empleado](#panorámica-de-los-ajustes-de-empleado).
Para crear un empleado con la configuración básica, sigue estos pasos:

1. Ve a _Plan > Configuración > Empleados_{:.breadcrumbs}.
2. En la barra de acciones, haz clic en el {% icon item-add %}.
3. En la sección **General**, añade un **número personal** único.
4. En la sección **Datos personales**, añade los **apellidos** del empleado.
5. En el campo de **injixo Inicio de sesión (Correo electrónico)**, introduce la dirección de correo electrónico que el empleado va a utilizar para injixo. La dirección de correo funciona automáticamente también para iniciar sesión en injixo Me. 
6. {% link_new Establece una contraseña | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %} para que el empleado pueda iniciar sesión en injixo.<br>Puedes hacerlo tras terminar la configuración básica del empleado.
7. Haz clic en _Aceptar_{:.doc-button}.<br>injixo establece automáticamente la fecha actual como fecha de entrada. Puedes cambiarla manualmente más tarde en la sección [Pertenencia a la empresa](#otros-ajustes).

Cuando creas un empleado, injixo crea automáticamente un usuario con el rol Agente.

<!-- In injixo Enterprise on-premise, you need to set the correct join date for the employee in the Employment Period section manually. To automatically create a linked user in the Users section, you need to add a User name and a Password in the Employee section. The injixo Login (Email) field is called Email 1 here and is not mandatory. --->

## Configurar los ajustes de empleado

Después de haber creado un empleado con la configuración básica obligatoria, puedes configurar los ajustes para la planificación. Para ello, sigue los pasos a continuación:

Prerrequisito: Has configurado {% link_new todos los elementos requeridos para la planificación | getting-started/set-up-base-configuration.md | #elementos-de-configuración-requeridos %}.

1. Haz clic en un empleado de la lista.<br>
Puedes usar los enlaces rápidos en azul en la parte superior derecha para navegar rápidamente a una sección.
2. Haz clic en el {% icon item-add %} en una sección para añadir un nuevo ajuste. Para editar un ajuste ya existente, haz clic en el {% icon item-edit %}.<br>Aprende más sobre las [opciones individuales de configuración](#panorámica-de-los-ajustes-de-empleado).
3. (Opcional) En algunas secciones, puedes configurar las fechas {% link_new Válido desde y Válido hasta | features/administration/set-a-validity-period.md %}, que limitan el período de validez de un ajuste.
4. Para guardar tus cambios, haz clic en _Aceptar_{:.doc-button}.

## Panorámica de los ajustes de empleado

En las siguientes secciones, puedes encontrar información sobre los ajustes obligatorios y opcionales para configurar a un empleado para la planificación.

### Ajustes de planificación obligatorios

La siguiente lista muestra los ajustes obligatorios que debes asignar a tus empleados para poder incluirlos en la planificación. Para aprender más sobre cada ajuste, sigue los enlaces.

> Atención
>
> No puedes asignar elementos con {% link_new períodos de validez | features/administration/set-a-validity-period.md %} superpuestos.
> Las asignaciones pasadas y futuras están ocultas por defecto. Para mostrarlas, haz clic en el icono Mostrar todo {% icon assignment-history | icon-only %}.


- {% link_new Contratos | features/administration/create-contracts.md %}: el menú desplegable muestra todos los contratos disponibles. Elige el contrato adecuado para tu empleado y asígnaselo.
- {% link_new Niveles de cualificación | features/administration/work-with-skills.md %}: los niveles de cualificación reflejan la capacidad de un empleado para trabajar en una tarea específica. Selecciona uno o varios niveles de cualificación en el menú desplegable.
- {% link_new Actividades | features/administration/activities.md %}: las actividades son las tareas en las que un empleado puede trabajar según sus cualificaciones. La sección de actividades se completa automáticamente después de asignar un nivel de cualificación a un empleado. Las actividades en las que todos los empleados pueden trabajar no requieren cualificaciones, p.&nbsp;ej., las actividades predefinidas Presente y Vacaciones.
- {% link_new Unidades de planificación | features/administration/create-and-manage-planning-units.md %}: las unidades de planificación agrupan empleados. Un empleado puede ser asignado a más de una unidad de planificación, pero necesita al menos una unidad de planificación con prioridad 1. Se le pueden asignar otras unidades de planificación con un valor entre 1 y 100 para cada empleado, siendo 1 la prioridad más alta.

### Ajustes de planificación opcionales

Los siguientes ajustes no son obligatorios, pero también pueden usarse para la planificación. Para aprender más sobre cada ajuste, sigue los enlaces.

- {% link_new Disponibilidad | features/administration/availabilities.md %}: define en qué días y a qué horas un empleado está disponible para ser planificado. Si deseas excluir siempre a un empleado de la planificación en un día específico de la semana, establece una disponibilidad de un minuto para el {% link_new tipo de día | features/administration/day-types.md %} en cuestión. Para establecer la misma disponibilidad para múltiples empleados a la vez, usa modelos de horario de {% link_new tipo márgenes de disponibilidad | features/administration/daymodels/daymodel-creation.md | #margen-de-disponibilidad %} en las rotaciones de turnos. Si un empleado está disponible sin limitaciones, no es necesario añadir ninguna disponibilidad.

- {% link_new Modelos de horario | features/administration/daymodels/daymodel-creation.md %}: por defecto, injixo usa todos los modelos de horario asignados a la unidad de planificación para crear horarios para tus empleados. Si asignas modelos de horario personales a un empleado, la planificación optimizada solo usará estos modelos de horario específicos para el empleado. Si quieres que injixo solo planifique empleados que hayan sido asignados a modelos de horario personales, puedes activar la regla de planificación 2661.

- {% link_new Rotaciones de turnos | features/administration/shift-sequences.md %}: las rotaciones de turnos contienen modelos de horarios o actividades con un patrón semanal repetitivo. Si quieres usar rotaciones de turnos para crear horarios para tus empleados, primero debes crear y [asignar rotaciones de turnos a un empleado](#asignar-una-rotación-de-turnos). También puedes asignar varias rotaciones de turnos a un empleado, p.&nbsp;ej. si quieres usar una rotación de turnos para los fines de semana y otra para los días laborables. 

- {% link_new Grupos | features/administration/selections.md %}: los grupos funcionan como una especie de filtro para mostrar una selección de empleados en una vista general o para realizar una acción simultáneamente para un grupo específico de empleados. Puedes crear uno o varios grupos desde el menú desplegable Grupos. Ejemplos de grupos son empleados que siempre tienen el mismo horario, tienen el mismo contrato, trabajan en rotaciones de turnos, comparten coche para ir al trabajo, o que son planificados primero porque trabajan a jornada completa.

- {% link_new Modelos de planificación | features/administration/work-time-pattern-models.md %}: usa los modelos de planificación para limitar la planificación automática a un subconjunto de los modelos de horario disponibles. Solo puedes asignar varios modelos de planificación a un mismo empleado si sus periodos de validez no coinciden. Define una fecha de referencia para marcar cuándo se usa por primera vez el modelo de planificación.

- Sistemas externos: asigna a tus empleados {% link_new identificadores de usuarios externos | features/acd-integration/cloud/import-agent-status-data.md | #asignar-identificadores-de-usuarios-externos-a-los-empleados-en-injixo %}, que son necesarios para importar estados de los agentes de tu distribuidor de llamadas.

### Otros ajustes

Esta sección proporciona una descripción general de los ajustes restantes en la configuración del empleado. La mayoría de ellos no son relevantes para la planificación. Para obtener más información sobre estos ajustes, puedes pasar el cursor sobre ellas en la interfaz de usuario para ver los detalles de cada ajuste.

- Pertenencia a la empresa: cuando [creas un empleado con la configuración básica](#crear-un-empleado), la fecha de entrada se establece automáticamente. Aquí puedes editar la fecha de entrada y establecer una fecha de salida, en caso necesario.

- Datos personales: introduce los datos personales de tu empleado, como la dirección, el número de teléfono y el país.

- Números de identificación: introduce el número de la tarjeta de identificación corporativa de tu empleado o cualquier otra tarjeta de identificación personal.

- Otros datos

Algunas informaciones en la sección Otros datos son relevantes para la planificación, mientras que otras no lo son. La siguiente tabla ofrece una panorámica con los detalles de los ajustes

| Ajuste        | Relevante para la planificación | Descripción                |
|----------------| ------------------------|----------------------------|
|Color       | No                      | Elige un color para identificar rápidamente al empleado en la planificación.  |
|Fecha y lugar de nacimiento  |       No |  Añade la fecha y lugar de nacimiento del empleado.  |
|Posición en el plan  | Sí | Define el orden de clasificación para la funcionalidad {% link_new Ordenar según la posición en el plan | features/scheduling/shiftcenter/sort-and-filter-items.md | #sort-the-items-of-a-level %} en el Centro de planificación. El valor predeterminado es 0 y el Centro de planificación ordena de forma ascendente.  |
|Asignar turnos | Sí | La casilla está marcada por defecto y es obligatoria si deseas planificar a los empleados automáticamente. Si no quieres que esto ocurra, desmarca la casilla. Todavía puedes asignar turnos manualmente e insertar rotaciones de turnos para este empleado.  |

## Usar la modificación masiva

En injixo Advanced y Enterprise WFM, puedes usar la {% link_new funcionalidad de modificación masiva | features/administration/mass-update.md %} para modifcar varios empleados a la vez.

## Asignar una rotación de turnos

Una rotación de turnos es un conjunto de modelos de horario o actividades que se repite con regularidad. Aprende cómo {% link_new crear rotaciones de turnos | features/administration/shift-sequences.md %} e insertarlas en tu planificación.

Para asignar una rotación de turnos, sigue los pasos a continuación:

1. En la sección **Rotaciones de turnos** haz clic en el {% icon item-add %}.
2. Selecciona una rotación de turnos
3. Desde el menú desplegable de la fila de empleados, selecciona la fila de la {% link_new rotación de turnos | features/administration/shift-sequences.md %} que corresponda al empleado.
4. Especifica el orden.<br>Este ajuste solo es relevante si necesitas asignar más de una rotación de turnos a un empleado. Las rotaciones de turnos con valores más bajos se insertan primero y pueden ser sobrescritas por las siguientes.
5. Establece una fecha de referencia que marque el primer día de la rotación de turnos.
6. Haz clic en _Aceptar_{:.doc-button}.  
   Ahora puedes {% link_new insertar rotaciones de turnos | features/scheduling/schedules/schedules-insert-shift-sequences.md %} en la planificación.

## Transferir empleados

Si tus empleados trabajan a menudo en otras unidades de planificación durante un tiempo limitado, puedes usar la funcionalidad Transferir empleado para asignar a los empleados temporalmente a otra unidad de planificación.

Durante el período de transferencia, la nueva unidad de planificación tiene automáticamente prioridad durante la planificación. Cuando el período definido acaba, el empleado automáticamente vuelve a ser planificado en su antigua unidad de planificación. La funcionalidad Transferir empleado ahorra tiempo en comparación con reasignar manualmente la unidad de planificación.

Para transferir un empleado, sigue los siguientes pasos.

1. Selecciona un empleado
2. Ve a la sección **Unidades de planificación**.
3. En el encabezado de la sección, haz clic en el {% icon delegate-employees %}.
4. Selecciona la unidad de planificación a la que quieres transferir el empleado.
5. Introduce una fecha de inicio y una fecha de finalización para la transferencia.
6. Haz clic en _Aceptar_{:.doc-button}.

> Atención
>
> Si un empleado está asignado a múltiples unidades de planificación al mismo tiempo, siempre será delegado desde la unidad de planificación con la mayor prioridad.
