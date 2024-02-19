---
title: Métodos de planificación
promote-service: new-planner-training
description: Aprende sobre los distintos métodos de planificación de injixo.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Combinar métodos de planificación
    filepath: features/scheduling/combined-scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

injixo ofrece distintos métodos de planificación, que puedes usar por separado o en {% link_new combinación | features/scheduling/combined-scheduling-methods.md %}.

Los distintos métodos de planificación están diseñados para adaptarse a diferentes escenarios. Todos los métodos de planificación tienen en cuenta la información configurada en los {% link_new contratos | features/administration/create-contracts.md %} de tus empleados, como el número de días laborables, las horas laborables diarias, semanales o mensuales, y otros parámetros de programación.

## Prerrequisitos

Antes de comenzar a usar los métodos de planificación, asegúrate de haber configurado los siguientes datos de configuración en _Plan > Configuración_{:.breadcrumbs}:

- Cualificaciones
- Actividades
- Modelos de horario
- Unidades de planificación
- Contratos
- Empleados

Algunos métodos de planificación pueden requerir que configures otros datos de configuración, como rotaciones de turnos o modelos de planificación.

## Planificación fija

El método planificación fija se basa en las {% link_new rotaciones de turnos | features/administration/shift-sequences.md %}. Una rotación de turnos es un patrón semanal de modelos de horario o actividades que define en qué días trabaja un empleado, así como la hora exacta de inicio y finalización de su turno. Como consecuencia, la planificación fija es el método de planificación más consistente, pero ofrece la menor flexibilidad.

Las planificaciones creadas con rotaciones de turnos pueden ser iguales todas las semanas o cambiar en intervalos de 2 a 53 semanas.

Una vez se haya creado la planificación, puedes usar {% link_new Optimizar las pausas | features/scheduling/schedules/break-optimization.md %} o la {% link_new Optimización de tareas | features/scheduling/schedules/schedules-job-optimization.md %} para optimizar aún más tu planificación.

**Optimizar las pausas** mueve los descansos planificados al intervalo de tiempo donde tengan el menor impacto en tu cobertura. injixo solo puede mover los descansos configurados dentro de un {% link_new pasillo en un modelo de horario | features/administration/daymodels/daymodel-basics.md | #elementos-fijos-vs-pasillos %}.

La **Optimización de tareas** puede sustituir las actividades configuradas como sustituibles con otras actividades planificables para lograr la mejor cobertura posible para todas las actividades, basándose en tus requisitos de personal. Los horarios de inicio y fin de los turnos no se modifican. La **Optimización de tareas** también puede modificar los descansos dentro de un turno, del mismo modo que **Optimizar las pausas**.

## Planificación optimizada

El método planificación optimizada ofrece la mayor flexibilidad. En este método, usas la funcionalidad {% link_new Crear planificación optimizada | features/scheduling/schedules/schedules-optimized-schedules.md %} para crear automáticamente una planificación completa. injixo asegura la mejor cobertura posible para todas las actividades con el menor número posible de empleados.

Por defecto, la funcionalidad **Crear planificación optimizada** puede planificar a los empleados con cualquier {% link_new modelo de horario | features/administration/daymodels/daymodel-basics.md %} asignado a su unidad de planificación y compatible con sus contratos. 

Dependiendo de tu configuración, el uso de distintos modelos de horario durante la planificación puede resultar en horarios muy inconsistentes, p.&nbsp;ej., injixo podría planificar a tus empleados para trabajar el turno de noche un lunes, el turno de tarde el martes y el turno de mañana el miércoles.

Para definir qué modelos de horario pueden usarse para crear una planificación, configura los {% link_new modelos de planificación | features/administration/work-time-pattern-models.md %}. Un modelo de planificación se compone de {% link_new modelos semanales | features/administration/work-time-pattern-models.md | #crear-modelos-semanales %} y define cómo asignar los modelos de horario a tus empleados. Con los modelos de planificación puedes crear patrones repetitivos de turnos y establecer restricciones de planificación para la funcionalidad **Crear planificación optimizada**.

Para planificar a tus empleados usando modelos de planificación, asigna un modelo de planificación a cada empleado. No puedes asignar varios modelos de planificación con el mismo periodo de validez a un mismo empleado.

### Turnos totalmente flexibles

Para crear planificaciones con turnos totalmente flexibles, crea modelos de planificación de {% link_new tipo A | features/administration/work-time-pattern-models.md | #tipos-de-modelos-de-planificación %}, y asígnaselos a tus empleados.

Con el tipo A, injixo puede seleccionar cualquier modelo de horario incluido en el modelo de planificación para cada día de cada semana, siempre y cuando sea compatible con el contrato del empleado.

Este método crea las mejores planificaciones que tus necesidades operativas. Al mismo tiempo, puede crear planificaciones muy inconsistentes que afecten negativamente a tus empleados. Para reducir este impacto negativo, puedes excluir ciertos turnos para algunos empleados asignándoles modelos de horario individuales o usando las [disponibilidades](#disponibilidades).

### Turnos flexibles rotativos

Para crear planificaciones con turnos flexibles rotativos, crea modelos de planificación de {% link_new tipo B, C o D | features/administration/work-time-pattern-models.md | #tipos-de-modelos-de-planificación %}, y asígnaselos a tus empleados.

Con los tipos B, C y D defines un orden específico que injixo sigue al seleccionar los modelos de horario de entre los disponibles en el modelo de planificación que sean compatibles con el contrato de cada empleado. También puedes definir una hora de inicio fija para los turnos, o un marco de tiempo dentro del cual comienzan los turnos.

### Disponibilidades

Puedes usar las {% link_new disponibilidades | features/administration/availabilities.md %} para configurar que algunos empleados no están disponibles para trabajar un día concreto o durante algunas horas. Las disponibilidades añaden restricciones de planificación adicionales a las definidas por los contratos y los horarios de apertura de las unidades de planificación.

Cuando las personas tienen disponibilidades asignadas, solo pueden ser planificadas para turnos dentro de los marcos de tiempo en los que están disponibles.

## Oferta de turnos

Si usas la {% link_new oferta de turnos | features/scheduling/schedules/schedules-shift-bidding.md %}, la planificación definitiva se crea una vez tus empleados hayan tenido la oportunidad de solicitar sus turnos preferidos en injixo Me.

Para crear una planificación usando la oferta de turnos, sigue estos pasos:

1. Define cuántos turnos necesitas para un {% link_new período de planificación | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %}.
2. {% link_new Genera turnos | features/scheduling/schedules/schedules-shift-bidding.md | #generate-shifts %} basados en los requisitos de personal calculados.
3. Cambia el estado de tu período de planificación a **Publicado**. Tus empleados pueden solicitar dos turnos por día (hasta un total de 10).
4. Inicia una {% link_new lotería de turnos | features/scheduling/shift-bidding.md | #lottery-of-requested-shifts %} para los turnos que han sido solicitados.
5. Asigna los turnos restantes. Los empleados cuyas solicitudes no se cumplieron durante la lotería serán planificados en este paso.

Una vez se haya creado la planificación, puedes usar la {% link_new Optimización de tareas | features/scheduling/schedules/schedules-job-optimization.md %} para optimizar aún más tu planificación.

> Usa la actividad Presente si combinas la oferta de turnos y la **Optimización de tareas**
>
> Si los empleados pueden solicitar turnos en injixo Me, pero quieres usar la **Optimización de tareas** más tarde, usa solo la actividad predeterminada Presente (ID de actividad: 1) como actividad en los modelos de horario. De esta manera evitas que los empleados soliciten turnos con actividades específicas y luego la **Optimización de tareas** les asigne actividades completamente diferentes.
