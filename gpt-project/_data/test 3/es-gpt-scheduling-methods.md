---
title: Métodos de planificación disponibles
promote-service: new-planner-training
description: Aprende acerca de los distintos métodos de planificación en injixo.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Combined scheduling methods
    filepath: features/scheduling/combined-scheduling-methods.md
  - overwrite_title: Configuración de los contratos
    filepath: features/administration/create-contracts.md
  - overwrite_title: Establecer un periodo de validez para los contratos
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Descripción general de los empleados
    filepath: features/administration/employee-overview.md
  - overwrite_title: Configurar injixo Me
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

En este artículo, te explicamos:

- qué métodos de planificación puedes utilizar,
- qué método de planificación puedes utilizar para cada caso de uso.

Puedes usar cada método de planificación individualmente o {% link_new combinar | features/scheduling/combined-scheduling-methods.md %} dos o más métodos.

Los métodos de planificación tienen en cuenta la información los {% link_new contratos | features/administration/create-contracts.md %} que están asignados a los empleados. En los contratos se definen la duración semanal de trabajo, las horas de trabajo diarias, semanales o mensuales, entre otros parámetros de planificación.

## Planificación fija

La planificación fija es el método de planificación más rígido. Se basa en las {% link_new secuencias de turnos | features/administration/shift-sequences.md %}.

Las secuencias de turnos definen:

- los días de la semana en los que el empleado trabaja
- el comienzo y el fin exacto de cada turno para cada jornada laboral

Las planificaciones creadas con estas secuencias pueden ser idénticas todas las semanas o cambiar en intervalos de 2 a 53 semanas.

Una vez creada la planificación, puedes optimizar los siguientes elementos:

- la posición de las pausas en los [bloques](fixed-elements-vs-corridors)
- las {% link_new actividades sustitutivas | features/administration/activity-types-and-properties.md | #propiedades-de-las-actividades %}

## Planificación optimizada

La planificación optimizada es el método de planificación más flexible. Puedes usar {% link_new Crear planificaciones optimizadas | features/scheduling/schedules/schedules-optimized-schedules.md %} para crear automáticamente una planificación completa. injixo garantizará la mejor cobertura posible para las distintas actividades con el menor número de empleados.

Para definir qué turnos se pueden planificar usaremos {% link_new plantillas de disponibilidad horaria | features/administration/work-time-pattern-models.md %}.

### Turnos completamente flexibles

Para turnos completamente flexibles, deberás asignar a tus empleados {% link_new plantillas de disponibilidad tipo A | features/administration/work-time-pattern-models.md | #tipos-de-plantillas-de-disponibilidad-horaria %}.

Puedes planificar cualquier turno disponible según la plantilla de disponibilidad horaria y que cumpla el contrato del empleado en cualquier día.

Para asegurarte de que tus empleados acepten las planificaciones, puedes excluir ciertos turnos añadiendo plantillas de disponibilidad específicas a los empleados o usar [disponibilidades](#Disponibilidades).

### Turnos rotativos flexibles

Para turnos rotativos flexibles, deberás asignar a tus empleados plantillas de disponibilidad {% link_new tipo B, C o D | features/administration/work-time-pattern-models.md | #tipos-de-plantillas-de-disponibilidad-horaria %}.

Los turnos que estén disponibles según la plantilla de acceso seleccionada y que cumplan con el contrato del empleado se planificarán en un orden específico, posiblemente incluso con la misma hora de inicio cada día.

### Plantillas de horarios de empleados

Al utilizar la {\% link_new planificación multipuestos | features/scheduling/schedules/schedules-employee-overview-multi-positions.md %} deben asignarse varias plantillas de disponibilidad a un empleado para cada función o ubicación.

### Disponibilidades

Las {% link_new disponibilidades | features/administration/availabilities.md %} pueden complementar las planificaciones optimizadas para limitar los turnos posibles.

## Rondas de planificación

{% link_new Rondas de planificación | features/scheduling/schedules/schedules-rounds.md %}, injixo genera automáticamente turnos para un periodo de planificación específico. Los empleados pueden coordinar los detalles finales con sus superiores.

Una ronda planificación consiste en los siguientes pasos:

1. Publicar una ronda de planificación.
2. Individualmente, los jefes y coordinadores de equipo planean los turnos para sus empleados basados en una plantilla generada por respiración.
3. Los jefes y coordinadores organizan el pedido del día con sus empleados.
4. Los empleados pueden, si lo desean, publicar cambios adicionales en la fase de planificación.
5. Cada ronda de planificación cuenta con una serie de fechas límite y fases, tales como planificación, pedido de día, evaluación y publicación de horarios.

## Método de planificación por turno

Con el método de planificación por turno, cada solicitud de turno se tiene en cuenta a la hora de crear un horario.

Visión general del método de planificación por turno:

1. Define cuántos turnos necesitas.
2. Genera turnos en base al cálculo de empleados previstos.
3. Establece el estado del periodo de planificación a **Planificado** o **Planificación cerrada**.
4. En la fase **Pedido de turno**, los empleados pueden solicitar hasta dos turnos por día (un máximo de 10 en total).
5. Los planificadores coordinan tu horario y crear una ronda de lotería de turnos, o automáticamente planifican los turnos.

## Descripción general de los distintos métodos de planificación

Para hacer posible el uso de los distintos métodos de planificación, es necesario configurar ciertos elementos en _Plan > Configuración_{:.breadcrumbs}. A continuación encontrarás una tabla que proporciona una descripción general de los elementos de configuración requeridos y opcionales para cada método de planificación.

|                          | Planificación fija  | Planificación optimizada | Rondas de planificación | Planificación por turno |
|--------------------------| ----------------  | ---- ----------------| --------------|--------------|
| Habilidades                   | Obligatorio          | Obligatorio             | Obligatorio      | Obligatorio      |
| Actividades               | Obligatorio          | Obligatorio             | Obligatorio      | Obligatorio      |
| Modelos de jornada           | Obligatorio          | Obligatorio             | --      | --      |
| Unidades de planificación           | Obligatorio          | Obligatorio             | --      | Obligatorio      |
| Contratos                | Obligatorio          | Obligatorio             | Obligatorio      | Obligatorio      |
| Empleados                | Obligatorio          | Obligatorio             | Obligatorio      | Obligatorio      |
| Secuencias de turno          | Obligatorio          | --                   | --      | --      |
| Planificar multiubicaciones  | No                | Sí             | Sí      | Sí      |
| Calendario de planificación        | Opcional          | Opcional             | Opcional      | Opcional      |  
| Últimas planificaciones               | Opcional          | Opcional             | Opcional      | Opcional      |
| Modelos semanales       | --                | Opcional             | --            | --            |
| Modelos de disponibilidad       | --                | Opcional             | --            | --            |