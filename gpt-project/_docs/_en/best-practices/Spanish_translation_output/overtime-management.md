---
title: Gestión de horas extraordinarias <!-- GPT translation -->
product_label:
  - advanced
  - enterprise
  - classic
description: Aprende a configurar de la mejor manera las actividades para planificar horas extras y documentarlas de forma transparente. <!-- GPT translation -->
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

A veces, necesitamos hacer horas extra para mantener niveles de servicio razonables. Las razones para hacer horas extra incluyen una carga de trabajo inesperadamente alta, o tener menos personal por altos índices de ausencia por enfermedad o vacaciones. <!-- GPT translation -->
En muchos casos, los contratos de tus colaboradores establecen que las horas extras se paguen a una tarifa más alta, o que cualquier cantidad de horas extraordinarias trabajadas se conceda como tiempo de vacaciones adicional. También es importante respetar otras limitaciones contractuales, como el tiempo de descanso entre turnos cuando tus colaboradores trabajan horas extras. Si proporcionas servicios, es posible que estés obligado a informar a tus clientes de cualquier trabajo adicional planificado. <!-- GPT translation -->

En este artículo, puedes encontrar consejos sobre cómo configurar actividades y multiactividades para poder planificar fácilmente horas extraordinarias y mostrarlas correctamente en tu mapa de calor de la cobertura y en tus informes. <!-- TM 100 -->

Las horas extraordinarias deben planificarse manualmente en el Centro de planificación o en Planificar como una adición a la planificación existente. <!-- TM 100 -->

## Crear actividades para horas extraordinarias <!-- TM 100 -->

El ejemplo a continuación utiliza una actividad nueva llamada Llamadas. Sigue estos pasos para todas las actividades que quieras poder planificar como horas extraordinarias, es decir, para Llamadas o Correos electrónicos, pero no para Enfermedad o Vacaciones. <!-- TM 100 -->

- {% link_new Crear actividades | features/administration/activities.md %} <!-- TM 66 -->
2. Duplica la actividad **Llamadas** y pon el nombre **Llamadas extra**. No es necesario añadir habilidades a esta actividad. <!-- GPT translation -->
  - Marca la casilla **Trato especial en la planificación optimizada**. <!-- TM 100 -->
  - Asegúrate de que la casilla **Se puede solicitar en Me**  no está marcada. <!-- TM 100 -->
3. En **Llamadas extra a horas** agrega **Llamadas** como subactividad.   <!-- GPT translation -->
  **Llamadas - horas extraordinarias** es ahora una multiactividad. <!-- TM 100 -->
4. Añade ambas actividades a la unidad de planificación correspondiente. No añades la actividad de horas extraordinarias a ningún modelo de horario. <!-- TM 100 -->

Con esta configuración, la actividad "Llamadas - horas extraordinarias" solo se puede planificar manualmente y no puede ser reemplazada durante la planificación optimizada. Tus empleados no podrán solicitar esta actividad en injixo Me. <!-- TM 100 -->

Como has añadido "- horas extraordinarias" al nombre de la multiactividad, todos los empleados pueden ver claramente en la planificación cuándo alguien trabaja horas extraordinarias, durante cuánto tiempo y en qué tarea. <!-- TM 100 -->

## Planificar horas extraordinarias <!-- TM 100 -->

Puedes planificar horas extraordinarias manualmente tanto en _Plan > Centro de planificación_{:.breadcrumbs} como en _Plan > Planificación_{:.breadcrumbs}. <!-- TM 100 -->

Para añadir actividades de horas extraordinarias en el Centro de planificación, sigue estos pasos: <!-- TM 100 -->

1. Elige la unidad de planificación y, opcionalmente, la selección a la que pertenece el empleado a quien quieres planificar para horas extraordinarias. <!-- TM 100 -->
2. Haz clic dos veces en la celda del empleado para el día en el que debe trabajar horas extraordinarias. Haz clic en la pestaña **Actividades múltiples** y selecciona **Llamadas - horas extraordinarias**. <!-- TM 100 -->
3. Introduce una hora de inicio y finalización para la actividad. <!-- TM 100 -->
4. Haz clic en _Aceptar_{:.doc-button}. <!-- TM 100 -->

Las horas extraordinarias planificadas se reflejan inmediatamente en la ventana de planificación en la pestaña Actividades en la {% link_new ventana de parámetros | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %}. Si configuras la pestaña Actividades para mostrar la cobertura, el mapa de calor se actualizará y reflejará las horas extraordinarias planificadas. <!-- TM 100 -->

Para añadir actividades de horas extraordinarias en _Plan > Planificar_{:.breadcrumbs}, sigue estos pasos: <!-- TM 100 -->

1. Haz clic dos veces en una celda en la planificación para abrir el editor. <!-- TM 100 -->
5. Haz clic en _Crear carga de trabajo_{:.doc-button}. <!-- TM 61 -->
  Se añade una nueva fila a la derecha con la actividad. <!-- TM 100 -->
3. En la nueva fila, selecciona **Llamadas - horas extraordinarias** en el menú desplegable. <!-- TM 100 -->
4. Introduce una hora de inicio y finalización para la actividad. <!-- TM 100 -->
5. Haz clic en _Guardar_{:.doc-button}. <!-- TM 100 -->

## Informes <!-- TM 100 -->

En el informe **Actividades en horas** se reflejará que el empleado trabajó horas extraordinarias, ya que el nombre de la actividad incluye dicha información. De este modo, todas las horas extraordinarias trabajadas quedan documentadas y pueden ser consultadas por todas las personas relevantes, como el departamento financiero, que gestiona la retribución adicional de estas horas. <!-- TM 100 -->