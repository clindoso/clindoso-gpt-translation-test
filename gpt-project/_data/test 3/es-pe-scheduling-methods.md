---
title: Métodos de planificación disponibles
promote-service: new-planner-training
description: Aprende sobre los distintos métodos de planificación en injixo.
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
  - overwrite_title: Configurar injixo Me
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

En este artículo, aprenderás:

- qué métodos de planificación puedes utilizar;
- qué método de planificación puedes utilizar para cada escenario.

Puedes usar un método de planificación individualmente o {% link_new combinar | features/scheduling/combined-scheduling-methods.md %} dos o más métodos.

Los métodos de planificación tienen en cuenta la información de los {% link_new contratos | features/administration/create-contracts.md %} asignados a los empleados. En los contratos se definen los días laborables semanales, las horas laborables diarias, semanales o mensuales, y otros parámetros de planificación.

## Planificación fija

La planificación fija es el método de planificación más rígido. Este método de planificación se basa en las {% link_new rotaciones de turnos | features/administration/shift-sequences.md %}.

Las rotaciones de turnos definen:

- los días de la semana en los que el empleado trabaja;
- el comienzo y el fin exacto de cada turno en cada jornada laboral.

Las planificaciones creadas con estas rotaciones de turnos pueden ser idénticas todas las semanas o cambiar en intervalos de 2 a 53 semanas.

Una vez creada la planificación, puedes optimizar los siguientes elementos:

- la posición de las pausas en los {% link_new pasillos | features/administration/daymodels/daymodel-basics.md | #elementos-fijos-vs-pasillos %};
- las {% link_new actividades sustituibles | features/administration/activity-types-and-properties.md | #propiedades-de-las-actividades %}.

## Planificación optimizada

La planificación optimizada es el método de planificación más flexible. Usa la funcionalidad {% link_new Crear planificación optimizada | features/scheduling/schedules/schedules-optimized-schedules.md %} para crear automáticamente una planificación completa. injixo asegura la mejor cobertura posible para las distintas actividades con el menor número de empleados posible.

Para definir qué turnos se pueden planificar, usa los {% link_new modelos de planificación | features/administration/work-time-pattern-models.md %}.

### Turnos completamente flexibles

Para planificar turnos completamente flexibles, asigna a tus empleados {% link_new modelos de planificación de tipo A | features/administration/work-time-pattern-models.md | #tipos-de-modelos-de-planificación %}.

Cualquier turno que esté disponible según el modelo de planificación y que respete el contrato del empleado puede ser planificado en cualquier día.

Para aumentar la satisfacción de los empleados con los turnos, puedes asignar modelos de planificación personales a los empleados o usar {% link_new disponibilidades | features/administration/availabilities.md %} para excluir ciertos turnos.

### Turnos alternos flexibles

Para planificar turnos alternos flexibles, asigna a tus empleados modelos de planificación de {% link_new tipo B, C o D | features/administration/work-time-pattern-models.md | #tipos-de-modelos-de-planificación %}.

Los turnos que estén disponibles según el modelo de planificación y que respeten el contrato del empleado se planificarán en un orden específico. Incluso pueden tener la misma hora de inicio cada día.

### Disponibilidades

Las {% link_new disponibilidades | features/administration/availabilities.md %} pueden complementar la planificación optimizada para limitar las opciones de turnos.

## Oferta de turnos

Con la {% link_new oferta de turnos | features/scheduling/schedules/schedules-shift-bidding.md %}, la planificación final se crea tras la participación de los empleados. Los empleados pueden solicitar sus turnos favoritos en injixo Me con anterioridad.

La oferta de turnos sigue el siguiente esquema:

1. Define cuántos turnos necesitas.
2. Genera turnos de acuerdo con los requisitos de personal calculados.
3. Cambia el estado del periodo de planificación a **Publicado**. Tus empleados pueden solicitar dos turnos por día (hasta un total de 10).
4. Inicia un {% link_new sorteo de turnos | features/scheduling/shift-bidding.md | #lottery-of-requested-shifts %} para los turnos solicitados.
5. Asigna los turnos restantes. Los empleados cuyas solicitudes no se asignaron durante el sorteo serán planificados en este paso.

## Resumen de los métodos de planificación y elementos de configuración

Cada método de planificación requiere configurar ciertos elementos en _Plan > Configuración_{:.breadcrumbs}. La siguiente tabla ofrece un resumen de los elementos de configuración obligatorios y opcionales para cada método de planificación.

|                          | Planificación fija | Planificación optimizada | Oferta de turnos |
|--------------------------| ----------------  | ---- ----------------| --------------|
| Cualificaciones          | Obligatorio          | Obligatorio             | Obligatorio      |
| Actividades              | Obligatorio          | Obligatorio             | Obligatorio      |
| Modelos de horario       | Obligatorio          | Obligatorio             | Obligatorio      |
| Unidades de planificación| Obligatorio          | Obligatorio             | Obligatorio      |
| Contratos                | Obligatorio          | Obligatorio             | Obligatorio      |
| Empleados                | Obligatorio          | Obligatorio             | Obligatorio      |
| Rotaciones de turnos         | Obligatorio          | --                   | Opcional      |
| Calendario de planificación    | Opcional          | Opcional             | Opcional      |  
| Grupos                   | Opcional          | Opcional             | Opcional      | 
| Modelos semanales        | --                | Opcional             | --            |
| Modelos de planificación | --                | Opcional             | --            |