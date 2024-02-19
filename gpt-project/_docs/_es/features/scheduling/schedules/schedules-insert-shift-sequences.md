---
title: Insertar rotaciones de turnos
product_label:
  - essential
  - advanced
  - enterprise
description: En Planificar puedes usar rotaciones de turnos para planificar repeticiones de turnos, actividades o disponibilidades.
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
---

Las rotaciones de turnos son patrones fijos y repetitivos de turnos, actividades o disponibilidades. Puedes insertar rotaciones de turnos para los empleados seleccionados, p.&nbsp;ej., para planificar tareas o disponibilidades regulares y recurrentes.

## Prerrequisitos

Antes de poder insertar rotaciones de turnos en tu horario, debes hacer lo siguiente:

- {% link_new Crear | features/administration/shift-sequences.md %} al menos una rotación de turnos
- {% link_new Asignar | features/administration/employee-overview.md | #asignar-una-rotación-de-turnos %} la rotación o rotaciones de turnos a un empleado

## Filtrar rotaciones de turnos

1. Ve a _Plan > Planificar_{:.breadcrumbs}.
2. En el menú desplegable **Acciones de planificación** a la derecha, selecciona _Insertar rotaciones de turnos_{:.doc-button}.
3. Selecciona una unidad de planificación.
4. (Opcional) Selecciona un grupo.
5. Establece un período de tiempo.

   > Puedes insertar rotaciones de turno para un máximo de dos años.


   La sección **Resumen** muestra rotaciones de turnos que coinciden con tu filtro. La tabla muestra los datos que se establecen cuando asignas una rotación de turnos existente a un empleado:

   | Opción                 | Descripción                                                                                                                                                                                                                                                                       |
   | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
   | Número personal       | Identificador inequívoco del empleado                                                                                                                                                                                                                                               |
   | Nombre                   | El nombre del empleado a quien se le asigna la rotación de turnos                                                                                                                                                                                                                                                                 |
   | Rotación de turnos         | El nombre de la rotación de turnos asignada                                                                                                                                                                                                                                                    |
   | Orden               | Define el orden en el que se insertan las rotaciones de turnos si un empleado tiene múltiples rotaciones de turnos asignadas. Las rotaciones de turnos con valores más bajos se insertan primero y pueden ser sobrescritas por rotaciones subsecuentes.                                                                  |
   | Fila de empleados           | Define qué fila de la rotación de turnos se usa para la persona.                                                                                                                                                                                                               |
   | Fecha de referencia         | Inicio de la rotación de turnos. Aprende más sobre la fecha de referencia. |
   | Válido desde<br>Válido hasta | Período durante el que la rotación de turnos ha sido asignada al empleado. Fuera del período de validez configurado, la rotación de turnos no se insertará en la planificación del empleado. Si el período de validez de la rotación de turnos se encuentra completamente dentro del período de tiempo seleccionado, no se mostrará. |

## Insertar rotaciones de turnos

1. Para seleccionar a un empleado, marca la casilla junto a su fila. Para seleccionar a todos los empleados, marca la casilla en el encabezado.
2. (Opcional) En el menú desplegable **Opciones** bajo la tabla, selecciona cómo gestionar las planificaciones existentes cuando insertas rotaciones de turnos.

   | Opción                           | Descripción                                                                                             |
   | -------------------------------- | --------------------------------------------------------------------------------------------------- |
   | Eliminar todas las actividades y turnos | Todas las actividades y turnos se eliminan del nivel de destino. Los periodos de disponibilidad se mantienen. |
   | Eliminar actividades de jornada completa       | Las actividades de jornada completa se eliminan. Las actividades que no sean de jornada completa no se eliminan.                              |
   | Eliminar periodos de disponibilidad      | Los periodos de disponibilidad se eliminan.                                                                   |

   <!-- {{ 2 | image: 'Options', '40%' }} -->

   > Las opciones seleccionadas solo se aplican al insertar la primera rotación de turnos de un empleado.

3. (Opcional) Modifica el nivel de destino. Por defecto, se selecciona el nivel Plan.
4. Haz clic en _Insertar rotaciones de turnos_{:.doc-button}.

> Atención  
>  
> Si una rotación de turnos incluye modelos de horario eliminados, estos serán insertados en la planificación (marcados con un borde punteado en Planificar y Centro de planificación).

## Acceder a los informes de resultados

En la sección **Histórico**, puedes ver informes de las ejecuciones de inserción de rotaciones de turnos actuales y anteriores. El enlace **Ver detalles** en la fila de cada ejecución abre un informe que contiene un mensaje de éxito o cualquier problema que haya ocurrido. El informe también muestra los IDs de las reglas de planificación y la razón por la cual no se pudieron insertar turnos o actividades.

Para eliminar ejecuciones de la sección **Histórico**, marca las casillas de verificación junto a una entrada o use la casilla de verificación en la parte superior para seleccionarlas todas y haz clic en _Eliminar entradas_{:.doc-button}.


## Gestión de planificaciones existentes

Una actividad de jornada completa de una rotación de turnos (p.&nbsp;ej., Enfermedad) sustituirá por defecto una actividad de jornada completa en la planificación (p.&nbsp;ej., Vacaciones).

Como resultado, las actividades más cortas y los modelos de horario pueden sobrescribir actividades de jornada completa y otras actividades de jornada parcial. Para evitar que esto ocurra con actividades de jornada completa, activa la regla de planificación _2645_{:.id-label}_. Para otras actividades de jornada parcial de los tipos Ausencia, Enfermedad, Vacaciones o Reunión, activa la regla de planificación _2648_{:.id-label}_.

## Periodos de validez

Cuando insertas rotaciones de turnos, los períodos de validez pueden influenciar los resultados.

Para determinar el período de tiempo durante el cual se puede planificar un modelo de horario, puedes limitar el período de validez de tus modelos de horario estableciendo una fecha de inicio y una fecha de finalización válidas. Después de insertar rotaciones de turno, es posible que veas el siguiente mensaje de error en el informe de resultados: [2151] Los modelos de horario para el turno «nombre del modelo de horario» no son válidos para el día dd/mm/yyyy.

En cada rotación de turnos puedes establecer un período de tiempo en el que se puede insertar la rotación de turnos. Por defecto, las rotaciones de turno son válidas todo el tiempo. Si limitas el período de tiempo, la rotación de turnos no se insertará fuera del período de tiempo definido. No verás ningún mensaje de error en ese caso.

Los períodos de validez en los modelos de horario personales (modelos de horario asignados a empleados) no afectan a las rotaciones de turnos. Estos modelos de horario incluidos en rotaciones de turnos seguirán siendo insertados

Atención: Los modelos de horario eliminados que aún forman parte de una rotación de turnos se insertan y se marcan con un borde punteado en el Centro de planificación y en Planificar. No verás ningún mensaje de error en ese caso.
