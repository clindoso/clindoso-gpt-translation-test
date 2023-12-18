---
title: Crear modelos de turno
redirect_from:
  - /es/wtpm_creating/
  - /es/week_time_patterns/
  - /es/wtpm_overview.md/
  - /es/understanding_wtpms/
product_label:
  - advanced
  - enterprise
  - classic
description: Usa modelos de turno en la optimización de la planificación para asegurarte de que las planificaciones de turnos no son aleatorias.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/reference-date.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Scheduling split shifts
    filepath: best-practices/scheduling-split-shifts.md
---

Un modelo de turno se compone de {% link week time patterns | features/administration/create-work-time-pattern-models.md %} y define cómo se asignan los {% link modelos de turno y días festivos | features/administration/daymodels/daymodel-basics.md %} a tus empleados.

La siguiente imagen muestra la configuración de los modelos de turno y los patrones de trabajo semanales en un modelo de turno.

{{ 1 | image: 'Estructura de un diseño de turno' }}

Con los modelos de turno puedes crear patrones de turnos y estableces restricciones de planificación para la funcionalidad **Planificar optimización de la planificación**<br>
Los modelos de turno tienen las siguientes ventajas:

- Definen qué modelos de turno pueden usarse para planificar a un(a) empleado/a.
- evitan asignar turnos de forma aleatoria.
- definen horarios de inicio para turnos.
- definen un orden para la asignación de modelos de turno.

Como alternativa a los modelos de turno, puedes usar secuencias de turnos o configurar las {% link_new disponibilidad | features/administration/availabilities.md %} para tu equipo.

## Requisitos previos

Para poder usar los modelos de turno, asegúrate de que se cumplen los siguientes requisitos previos:
- has creado [modelos de turno](#create-week-time-patterns) y [patrones de trabajo semanales](#patrones-de-trabajo-semanales), y has asignado modelos de turno a los patrones de trabajo semanales.
- cada modelo de turno contiene al menos un patrón de trabajo semanal.
- cada patrón de trabajo semanal contiene al menos un {% link_new modelo de turno | features/administration/daymodels/daymodel-basics.md %}.
- has asignado los modelos de turno a tus empleados.

## Crear patrones de trabajo semanales

Un patrón de trabajo semanal es un grupo de modelos de turno. Puedes agrupar los modelos de turno según esos criterios, p.ej. duración del turno o actividad, si es un turno de mañana, tarde o noche, etc.<br>

Solo puedes usar los patrones de trabajo semanales en un modelo de turno. Para una semana laboral, injixo planificará a los empleados según los modelos de turno incluidos en el patrón de trabajo semanal junto con los patrones de trabajo semanales.

Para crear un patrón de trabajo semanal, sigue estos pasos:

1. Ve a _Plan > Configuración > Patrones de trabajo semanales_{:.breadcrumbs}.
2. Haz clic en el icono Nuevo  {% icon item-add | icon-only %} en la esquina superior izquierda.
    Se abre un panel de configuración a la derecha.
3. Configura los ajustes del patrón de trabajo semanal:<br>
  **Nombre**: Introduce un nombre exclusivo (máx. 50 caracteres).<br>
  **Abreviatura**: Introduce el nombre o una manera abreviada del nombre (máx. 25 caracteres).<br>
  **Color**: El color te ayudará a identificar el patrón de trabajo semanal en una lista.<br>
  **Máximo de días de excepción por semana**: [Días de excepción](#días-de-excepción) te permiten a ti y a injixo saltarse las reglas del modelo de turno para adaptarte mejor a las necesidades de tu plantilla.
4. Haz clic en _Guardar_{:.doc-button}.

Puedes añadir ahora modelos de turno a tu patrón de trabajo semanal.

### Añadir modelos de turno a un patrón de trabajo semanal

1. En el panel de configuración del  patrón de trabajo semanal, ve a la sección **Modelos de turno** y haz clic en el icono Añadir  {% icon item-add | icon-only %}.
2. Selecciona uno o varios modelos de turno en la lista.
3. Haz clic en _Guardar_{:.doc-button}.

Puedes usar tanto los {% link_new modelos de turno fijos y variables | features/administration/daymodels/daymodel-basics.md | #types-of-day-models %} en un patrón de trabajo semanal. Si usas modelos de turno variables, la funcionalidad **Planificar optimización de la planificación** puede calcular la mejor hora de inicio de los turnos en los límites definidos por el modelo de turno.

> Atención
>
> Para planificar modelos de turno, asegúrate de que has asignado los modelos de turno al modelo de empleado o a la unidad de planificación a la que el empleado está asignado.  Si has [limitado los modelos de turno](features/administration/create-and-manage-planning-units.md#create-and-manage-planning-units), los modelos de turno que esperas que injixo utilice en planificación pueden no ser usados.
>
> Injixo puede sustituir actividades sustituibles por actividades planificables en un turno. Para hacerlo, explícita modelos de turno variables para cada duración de turno requerida en un contrato, y usa la actividad del sistema Presente (ID: 1) como {% link_new actividad base | features/administration/daymodels/daymodel-basics.md | #actividad-base-y-duración-del-turno %}. No definas modelos de turno para cada actividad individual.

## Crear modelos de turno

1. Ve a _Plan > Configuración > Modelos de turno_{:.breadcrumbs}.
2. Haz clic en el icono Nuevo  {% icon item-add | icon-only %} en la parte superior izquierda.
3. Configura los ajustes del modelo de turno:<br>
  **Nombre**: Introduce un nombre exclusivo (máx. 50 caracteres).<br>
  **Abreviatura**: Introduce el nombre o una manera abreviada del nombre (máx. 25 caracteres).<br>
  **Color**: El color te ayudará a identificar el modelo de turno en una lista.<br>
  **Tipo**: El [tipo](#tipos-de-modelos-de-turno) determina cómo injixo utiliza el modelo de turno.<br>
  **Patrón de trabajo semanal - máximo de días de excepción por semana**: Selecciona el patrón de trabajo semanal que injixo debería usar para planificar los [días de excepción](#días-de-excepción).
4. Haz clic en _Guardar_{:.doc-button}.

Puedes ahora añadir patrones de trabajo semanales a tu modelo de turno.

### Añadir patrones de trabajo semanales a un modelo de turno

1. En el diálogo de configuración del modelo de turno, haz clic en el icono Añadir  {% icon item-add | icon-only %} en la sección **Patrones de trabajo semanales**.
2. Escoge un **Patrón de trabajo semanal** de la lista.
3. Introduce una **Posición**.<br>
  Si añades varios patrones de trabajo semanales, haz clic en la {% icon up-arrow-blue %} y la {% icon down-arrow-blue %} para cambiar la posición.
4. Haz clic en _Guardar_{:.doc-button}.

### Posición

La posición de un patrón de trabajo semanal dentro de un modelo de turno es importante cuando uses modelos de turno de [tipo B o D](#tipos-de-modelos-de-turno). Injixo asigna los patrones de trabajo semanales en el orden configurado aquí.

Usa la {% icon up-arrow-blue %} y la {% icon down-arrow-blue %} para definir la posición de los patrones de trabajo semanales.

## Tipos de modelos de turno

| Tipo | Nombre               | Uso de los patrones de trabajo semanales                                                      | Asignación de modelos de turno | Hora de inicio del turno              | Efecto             |
| ---- | ------------------ | -------------------------------------------------------------------------- | -------------------- | ----------------------------- | --------------------------------- |
| A    | Selección flexible | injixo puede elegir cualquier modelo de turno de cualquier patrón de trabajo semanal para cualquier día de la semana. | injixo puede usar cualquier modelo de turno de cualquier patrón de trabajo semanal.| Flexible    | Dependiendo del horario de apertura de tu organización, el tipo A puede resultar en una distribución de turnos que parece aleatoria o estresante para tus empleados. P.ej., una persona tendría que trabajar temprano el lunes,  por la noche el martes, y tarde el miércoles, etc. |
| B    | Rotación fija     | injixo planifica los patrones de trabajo semanales en el orden definido por sus posiciones. | Para cada semana, injixo selecciona el modelo de turno que mejor cubra las necesidades de personal.| Fijada   | Cuando asignes este tipo de modelo de turno a un empleado, debes fijar una {% link fecha de referencia | features/administration/reference-date.md %}. La fecha de referencia define a partir de cuándo se usa el modelo de turno.<br> Cada empleado tendrá asignado el mismo modelo de turno para la semana entera, p.&nbsp;ej., un turno que empieza a las 9&nbsp;a.&nbsp;m., de lunes a viernes. Esta regla únicamente puede ser incumplida definiendo días de excepción. Esta es la asignación de turnos más consistente de los cuatro tipos. |
| C    | Rotación variable  | injixo no respeta la posición definida para los patrones de trabajo semanales. | injixo selecciona un modelo de turno para toda la semana.| Fijada   | Puedes asignar cualquier patrón de trabajo semanal a tus empleados para cubrir mejor las necesidades de tu equipo. Dado que los turnos empiezan a la misma hora, las horas de trabajo son consistentes durante toda la semana. |
| D    | Rotación combinada (A/B) | injixo respeta la posición definida para los patrones de trabajo semanales. | injixo selecciona un modelo de turno para toda la semana.| Flexible (dentro de un marco de tiempo)    |  Basándose en las necesidades de tu plantilla, injixo puede planificar a empleados&mdash;para comenzar su turno entre las 8&nbsp;a.&nbsp;m. y las 10&nbsp;a.&nbsp;m. Con el tipo D, injixo asigna horarios consistentes a tus empleados,  mientras al mismo tiempo planifica más accesiblemente para reunir y  satisfacer mejor las necesidades de tu plantilla. |



## Días de excepción

Los días de excepción permiten a injixo y a ti saltarte las reglas definidas por el [tipo de modelo de turno](#tipos-de-modelos-de-turno) en uso.<br>

Por ejemplo, podrías usar días de excepción para planificar un turno de noche en una semana en la que normalmente el empleado trabaja un turno de mañana.<br>

Los días de excepción priorizan las necesidades de tu plantilla y aseguran una mejor cobertura en la planificación. Sin embargo, resultan en horarios menos consistentes para tus empleados.

Para planificar días de excepción, sigue estos pasos:

1. [Crea un patrón de trabajo semanal separado](#crear-patrones-de-trabajo-semanales) y añade los modelos de turno que se usarán como excepción.
2. En el diálogo de configuración de los patrones de trabajo semanales que quieres usar para la planificación estándar, define el máximo número de días de excepción por semana.
3. En el diálogo de configuración del modelo de turno, selecciona el patrón de trabajo semanal que quieras usar para los días de excepción.

Cuando selecciones un modelo de turno para la semana, injixo no puede usar los modelos de turno definidos para los días de excepción. Asegúrate de que todos los datos de configuración requeridos para la planificación (es decir, los modelos de turno utilizados y el modelo de turno) cumplen las [normas de planificación de turnos](features/administration/create-contracts.md#modificación-de-horarios-predefinidos-definidos-en-un-modelo-de-trabajo) definidas en el contrato de trabajo del empleado. Si el modelo de turno para la semana coincide con el contrato de trabajo, injixo puede sustituir el modelo de turno original con uno definido para los días de excepción, para reunir y satisfacer mejor las necesidades de tu plantilla.

## Asignar modelos de turno a tus empleados

1. Ve a _Plan > Configuración > Empleados_{:.breadcrumbs}.
2. Selecciona un empleado en la lista.
3. Haz clic en el icono Añadir  {% icon item-add | icon-only %} en la sección **Modelos de trabajo**.<br>
   Se abre un panel de configuración a la derecha.
4. Configura los ajustes:<br>
  **Válido desde/hasta**: Introduce un {% link nuevo período de validez | features/administration/set-a-validity-period.md %}.<br>
  **Modelo de turno**<br>
  **Fecha de referencia**: Establece una {% link nueva fecha de referencia | features/administration/reference-date.md %} para que un modelo de turno empiece a usarse.
5. Haz clic en _Guardar_{:.doc-button}.

Usa la funcionalidad de {% link nuevo actualización masiva | features/administration/mass-update.md %} para asignar un modelo de turno a varias personas al mismo tiempo.

> Atención al usar la actualización masiva para asignar modelos de turno de tipo B
>
> Si usas la funcionalidad de actualización masiva y estableces la misma fecha de referencia para todas las personas, todas las personas tendrán asignado el mismo patrón de trabajo semanal en la misma semana.
>
> En su lugar, elige grupos más pequeños para la actualización masiva, y establece lunes futuros como fecha de referencia para ellos. De esta manera, cada grupo comenzará la rotación de modelos de turno en una semana distinta.
