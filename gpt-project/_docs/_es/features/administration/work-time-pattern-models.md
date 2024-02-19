---
title: Crear modelos de planificación
redirect_from:
  - /wtpm_creating/
  - /week_time_patterns/
  - /wtpm_overview.md/
  - /understanding_wtpms/
product_label:
  - advanced
  - enterprise
  - classic
description: Usa modelos de planificación durante la optimización de tu planificación para asegurarte de que tus empleados no reciben turnos aleatorios.
related_articles:
  - overwrite_title: Planificación optimizada
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Configurar empleados
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Planificar turnos partidos
    filepath: best-practices/scheduling-split-shifts.md
---

Un modelo de planificación se compone de [modelos semanales](#crear-modelos-semanales) y define cómo asignar los {% link_new modelos de horario | features/administration/daymodels/daymodel-basics.md %} a tus empleados.

La siguiente imagen muestra la configuración de modelos de horario y modelos semanales en un modelo de planificación.

{{ 1 | image: 'Estructura de un modelo de planificación', '80%' }}

Con los modelos de planificación puedes crear patrones repetitivos de turnos y establecer restricciones de planificación para la funcionalidad **Crear planificación optimizada**.<br>
Los modelos de planificación ofrecen los siguientes beneficios:

- Definen qué modelos de horario se pueden usar para planificar a una persona.
- Tus empleados no reciben combinaciones aleatorias de turnos.
- Definen las horas de inicio de los turnos.
- Definen un orden para la asignación de los modelos de horario.

Como alternativa a los modelos de planificación puedes usar rotaciones de turnos o configurar {% link_new disponibilidades | features/administration/availabilities.md %} para tus empleados.

## Prerrequisitos

Para poder usar los modelos de planificación, asegúrate de cumplir las siguientes condiciones:
- Has creado {% link_new modelos de horario | features/administration/daymodels/daymodel-creation.md %} y [modelos semanales](#crear-modelos-semanales), y has asignado los modelos de horario a los modelos semanales.
- Cada modelo de planificación contiene al menos un modelo semanal.
- Cada modelo semanal contiene al menos un {% link_new modelo de horario | features/administration/daymodels/daymodel-basics.md %}.
- Has [asignado los modelo de planificación a tus empleados](#asignar-modelos-de-planificación-a-tus-empleados).

## Crear modelos semanales

Un modelo semanal es un grupo de modelos de horario. Puedes agrupar los modelos de horario siguiendo cualquier criterio, p.&nbsp;ej., duración del turno, actividades incluidas, hora de inicio, etc.<br>

Los modelos semanales solo pueden usarse como parte de un modelo de planificación. Para una semana laboral, injixo planifica a los empleados de acuerdo con los modelos de horario incluidos en el modelo semanal. De este modo, puedes garantizar que tus empleados tengan horarios de trabajo más justos y consistentes.

Para crear un modelo semanal, sigue estos pasos:

1. Ve a _Plan > Configuración > Modelos semanales_{:.breadcrumbs}.
2. Haz clic en el icono Nuevo {% icon item-add | icon-only %} en la barra de acciones.
    Se abre un panel de configuración a la derecha.
3. Configura el modelo semanal:<br>
  **Nombre**: introduce un nombre inequívoco (máx. 50 caracteres).<br>
  **Abreviatura**: introduce el nombre o una versión más corta del mismo (máx. 25 caracteres).<br>
  **Color**: el color puede ayudarte a identificar el modelo semanal en una lista.<br>
  **Máximo de días extraordinarios a la semana**: los [días extraordinarios](#días-extraordinarios) permiten que injixo rompa las reglas del modelo de planificación para cumplir mejor los requisitos de personal.
4. Haz clic en _Aceptar_{:.doc-button}.

Ahora puedes añadir modelos de horario a tu modelo semanal.

### Añadir modelos de horario a un modelo semanal

1. En el panel de configuración del modelo semanal, ve a la sección **Modelos de horario** y haz clic en el icono Insertar {% icon item-add | icon-only %}.
2. Selecciona uno o varios modelos de horario de la lista.
3. Haz clic en _Aceptar_{:.doc-button}.

Puedes añadir tanto modelos de horario fijos como variables a un modelo semanal. Si usas modelos de horario variables, la funcionalidad **Crear planificación optimizada** puede determinar la hora óptima de inicio de los turnos dentro de las restricciones establecidas por el modelo de horario.

> Atención
>
> injixo solo puede planificar modelos de horario que estén asignados a la unidad de planificación a la que pertenece el empleado. Si has {% link_new limitado los modelos de horario | features/administration/create-and-manage-planning-units.md | #limitar-los-modelos-de-horario %} en tu unidad de planificación, es posible que no se usen los modelos de horario que esperarías según tu modelo de planificación.
>
> injixo puede sustituir actividades sustituibles por actividades planificables en los turnos. Para ello, usa modelos de horario variables para cada duración de turno requerida por un contrato, y usa la actividad predeterminada {% link_new Presente (ID: 1) | features/administration/daymodels/daymodel-basics.md | #actividad-base-y-duración-del-turno %} como actividad base. No definas modelos de horario para cada actividad individual.

## Crear modelos de planificación

1. Ve a _Plan > Configuración > Modelos de planificación_{:.breadcrumbs}.
2. Haz clic en el icono Nuevo {% icon item-add | icon-only %} en la barra de acciones.
3. Configura el modelo de planificación:<br>
  **Nombre**: introduce un nombre inequívoco (máx. 50 caracteres).<br>
  **Abreviatura**: introduce el nombre o una versión más corta del mismo (máx. 25 caracteres).<br>
  **Color**: el color puede ayudarte a identificar el modelo de planificación en una lista.<br>
  **Tipo**: el [tipo](#tipos-de-modelos-de-planificación) determina cómo injixo usa el modelo de planificación.<br>
  **Modelo semanal para días extraordinarios**: selecciona el modelo semanal que injixo debe usar para planificar [días extraordinarios](#días-extraordinarios).
4. Haz clic en _Aceptar_{:.doc-button}.

Ahora puedes añadir modelos semanales a tu modelo de planificación.

### Añadir modelos semanales a un modelo de planificación

1. En el diálogo de configuración del modelo de planificación, haz clic en el icono Insertar {% icon item-add | icon-only %} en la sección **Modelos semanales**.
2. Escoge un **modelo semanal** de la lista.
3. Define una **posición**.<br>
  Si añades varios modelos semanales, haz clic en el {% icon down-arrow-blue %} y el {% icon up-arrow-blue %} para cambiar la posición.
4. Haz clic en _Aceptar_{:.doc-button}.

### Posición

La posición de los modelos semanales dentro de los modelos de planificación es relevante cuando se usan modelos de planificación de [tipo B o D](#tipos-de-modelos-de-planificación). injixo asignará los modelos semanales en el orden configurado aquí.

Usa el {% icon down-arrow-blue %} y el {% icon up-arrow-blue %} para definir la posición de los modelos semanales.

## Tipos de modelos de planificación

| Tipo | Nombre               | Uso de los modelos semanales                                                      | Asignación del modelo de horario | Hora de inicio del turno              | Efecto             |
| ---- | ------------------ | -------------------------------------------------------------------------- | -------------------- | ----------------------------- | --------------------------------- |
| A    | Selección flexible | injixo puede seleccionar cualquier modelo de horario de cualquiera de los modelos semanales incluidos para cada día de cada semana. | injixo puede usar cualquier modelo de horario de cualquier modelo semanal. | Flexible    | Dependiendo del horario de apertura de tu organización, el tipo A puede resultar en una distribución de turnos que a tus empleados les parezca aleatoria o estresante. Por ejemplo, un empleado podría trabajar el turno de mañana el lunes, de noche del martes, y de tarde el miércoles, etc. |
| B    | Alternancia fija     | injixo planifica los modelos semanales en el orden definido por sus posiciones. | Para cada semana, injixo elegirá el modelo de horario que mejor cubra los requisitos de personal. | Fijo    | Cuando asignas este tipo de modelo de planificación a tus empleados, debes establecer una fecha de referencia. La fecha de referencia define cuándo se usa por primera vez el modelo de planificación.<br> A cada empleado se le asigna un mismo modelo de horario toda la semana, p.&nbsp;ej., empezando a las 9&nbsp;a.&nbsp;m. de lunes a viernes. Define [días extraordinarios](#días-extraordinarios) si quieres planificar otro modelo de horario. Esta es la asignación de turnos más consistente de los cuatro tipos. |
| C    | Alternancia variable  | injixo no respeta la posición definida para los modelos semanales. | injixo elige un modelo de horario para toda la semana. | Fijo    | A los empleados se les puede asignar cualquier modelo semanal para cumplir mejor los requisito de personal. Dado que los turnos comienzan al mismo tiempo, tus empleados tienen un horario de trabajo consistente durante toda la semana. |
| D    | Alternancia combinada (A/B) | injixo respeta la posición definida para los modelos semanales. | injixo elige un modelo de horario para toda la semana.| Flexible (dentro de un rango de tiempo)    |  Dependiendo de los requisitos de personal, injixo puede planificar a empleados con turno temprano para comenzar a trabajar entre las 8&nbsp;a.&nbsp;m. y las 10&nbsp;a.&nbsp;m. Con el tipo D, injixo tiene más flexibilidad al planificar para cumplir mejor los requisitos de personal, a la vez que asigna horarios bastante consistentes a tus empleados. |


El siguiente gráfico muestra cómo los distintos tipos de modelos de planificación influencian tu planificación. Este ejemplo incluye un modelo de planificación con cuatro modelos semanales y tres modelos de horario en cada modelo semanal.

{{ 2 | image: 'Ejemplo de planificación con los distintos tipos de modelos de planificación' }}

## Días extraordinarios

Los días extraordinarios permiten a injixo incumplir las reglas del modelo de planificación para cumplir mejor los requisitos de personal. Por ejemplo, podrías usar días de excepción para planificar un turno nocturno en una semana en la que el empleado normalmente trabaja el turno de mañana.<br>

Los días extraordinarios priorizan los requisitos de personal y garantizan una mejor cobertura. Sin embargo, resultan en horarios menos consistentes para tus empleados.

Para planificar días extraordinarios, sigue estos pasos:

1. [Crea un modelo semanal adicional](#crear-modelos-semanales) y añádele los modelos de horario que quieras usar para los días extraordinarios.
2. En el diálogo de configuración de los modelos semanales que quieres usar para el turno estándar, define el número de días extraordinarios a la semana.
3. En el diálogo de configuración del modelo de planificación, selecciona el modelo semanal que quieres usar para los días extraordinarios.

A la hora de elegir un modelo de horario para la semana, injixo no puede usar los modelos de horario definidos para los días extraordinarios. Asegúrate de que todos los datos de configuración necesarios para la planificación (todos los modelos de horario usados, así como el modelo de planificación) cumplan con los {% link_new horarios laborales de referencia | features/administration/create-contracts.md | #horarios-laborales-de-referencia %} definidos en el contrato del empleado. Si el modelo de horario utilizado para la semana coincide con el contrato, injixo puede sustituir el modelo de horario original por uno definido para días extraordinarios para cumplir mejor los requisitos del personal.

## Asignar modelos de planificación a tus empleados

1. Ve a _Plan > Configuración > Empleados_{:.breadcrumbs}.
2. Selecciona un empleado de la lista.
3. Haz clic en el icono Insertar {% icon item-add | icon-only %} en la sección **Modelos de planificación**.<br>
   Se abre un panel de configuración a la derecha.
4. Configura los campos:<br>
  **Válido desde/Válido hasta**: establece un {% link_new periodo de validez| features/administration/set-a-validity-period.md %}.<br>
  **Modelo de planificación**<br>
  **Fecha de referencia**: establece una fecha de referencia en la que se comienza a usar el modelo de planificación.
5. Haz clic en _Aceptar_{:.doc-button}.

Usa la funcionalidad {% link_new actualización masiva | features/administration/mass-update.md %} para asignar un modelo de planificación a varios empleados a la vez.

> Precaución al usar la actualización masiva para asignar modelos de planificación de tipo B.
>
> Si usas la actualización masiva y estableces la misma fecha de referencia para todos los empleados, se planificará el mismo modelo semanal al mismo tiempo para todos.
>
> En su lugar, selecciona grupos más pequeños para la actualización masiva y establece lunes consecutivos como fechas de referencia para los distintos grupos. De esta manera, cada grupo comenzará su rotación en una semana diferente.

## Ejemplos:

### Ejemplo A: alternancia fija con turnos tempranos y tardíos

Configura un modelo de planificación de tipo B (alternancia fija) y asígnale tres modelos semanales diferentes. Recuerda definir la posición de los modelos semanales.

- El modelo semanal 1 (posición 1) contiene modelos de horario para turnos de mañana (los turnos comienzan entre las 7&nbsp;a.&nbsp;m. y las 9&nbsp;a.&nbsp;m.).
- El modelo semanal 2 (posición 2) contiene modelos de horario para turnos tardíos (los turnos terminan a las 11&nbsp;p.&nbsp;m.).
- El modelo semanal 3 (posición 3) contiene modelos de horario para turnos de tarde (los turnos comienzan entre las 11&nbsp;a.&nbsp;m. y el mediodía).

Con este modelo de planificación, los empleados alternan de forma consistente entre una semana con turnos de mañana, una semana con turnos tardíos y una semana con turnos de tarde. 

Si bien esto requiere cierta flexibilidad, los empleados tienen horarios consistentes durante toda la semana.

### Ejemplo B: días extraordinarios para turnos de noche

Configura un modelo de planificación con tres modelos semanales diferentes. Configura un máximo de dos días extraordinarios a la semana.

- El modelo semanal 1 contiene modelos de horario para turnos de mañana.
- El modelo semanal 2 contiene modelos de horario para turnos tardíos.
- El modelo semanal 3 contiene modelos de horario para turnos de noche (selecciona este modelo en el menú desplegable **Modelo semanal para días extraordinarios**).

Con este modelo de patrón de horario de trabajo, los empleados alternan entre turnos de mañana en la primera semana y turnos tardíos en la siguiente semana. Sin embargo, puesto que has definido dos días extraordinarios, a tus empleados también se les pueden asignar dos turnos de noche por semana, si esta es la mejor asignación para cumplir los requisitos del personal.

<!-- TODO: very special example, add some more context  -->
<!-- ### Example: Performance-Based Scheduling With WTPMs and Preferred Day Models

Use Work Time Pattern Models and preferred day models for Performance-Based Shift Assignment.

* Within the Week Time Patterns, assign the shifts according to agents' performance.
* Assign the Work Time Pattern Model to an agent with a validity period. Adjust it regularly according to performance scores.

For your high achievers you can pick some of the day models and assign them directly to these employees as personal day models. The AutoScheduler will only use these day models while generating schedules. This ensures that out-of-favor shifts are not assigned to high performing agents. -->

<!-- TODO: Example: normal use case scheduling different hours or working days in different weeks -->
<!-- ### Example: Scheduling Different Number of Working Days or Hours in Different Weeks -->
<!-- There is a bad German article /de/scheduling-different-wtm/ using WTPM Type B with two WTMs 4x10 and 5x8 hour shifts, with Autoscheduler contract parameter. minimum days per week with value 4 and scheduling parameter 2602 with value 10:00 -->
