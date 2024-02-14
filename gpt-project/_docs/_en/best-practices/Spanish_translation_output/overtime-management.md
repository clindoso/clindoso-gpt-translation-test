---
title: Gestión del tiempo extra <!-- GPT translation -->
product_label:
  - advanced
  - enterprise
  - classic
description: Aprenda cómo configurar actividades para planificar horas extraordinarias y documentarlo de manera transparente.
 <!-- GPT translation -->
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

A veces, es necesario trabajar horas extras para mantener niveles de servicio razonables. Las razones para hacer horas extras pueden ser una carga de trabajo inesperadamente alta, o una falta de personal causada por un elevado número de ausencias debido a enfermedad o vacaciones. <!-- GPT translation -->
En muchos casos, los contratos de tus empleados estipulan que las horas extraordinarias se pagan a un tipo superior, o que cualquier cantidad de horas extraordinarias trabajadas se debe convertir en días adicionales de vacaciones. También es importante respetar otras limitaciones contractuales, como los períodos mínimos de descanso entre turnos cuando los empleados trabajan horas extraordinarias. Si prestas servicios, también es posible que estés obligado a informar a los clientes sobre cualquier labor adicional programada. <!-- GPT translation -->

En este artículo, puedes encontrar consejos sobre cómo configurar actividades y multiactividades para poder planificar fácilmente horas extraordinarias y mostrarlas correctamente en tu mapa de calor de la cobertura y en tus informes. <!-- TM 100 -->

Las horas extraordinarias deben planificarse manualmente en el Centro de planificación o en Planificar como una adición a la planificación existente. <!-- TM 100 -->

## Crear actividades para horas extraordinarias <!-- TM 100 -->

El ejemplo a continuación utiliza una actividad nueva llamada Llamadas. Sigue estos pasos para todas las actividades que quieras poder planificar como horas extraordinarias, es decir, para Llamadas o Correos electrónicos, pero no para Enfermedad o Vacaciones. <!-- TM 100 -->

- {% link_new Crear actividades | features/administration/activities.md %} <!-- TM 66 -->
Duplica la actividad **Calls** y denomina la nueva actividad **Calls overtime**. No es necesario añadir habilidades a esta actividad. <!-- GPT translation -->
- **Marcar la casilla** Especificar manejo en optimización horaria. <!-- GPT translation -->
- Asegúrate de que la casilla **Disponible para mi** no esté marcada. <!-- GPT translation -->
3. En **Llamadas extra**, añade **Llamadas** como subactividad. <!-- GPT translation -->
**Las llamadas por tiempo extra** son ahora una multiactividad.

Translate words and phrases in the same style and tone. <!-- GPT translation -->
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
Se añade una nueva fila con la actividad a la derecha. <!-- GPT translation -->
3. En la nueva fila, selecciona **Llamadas - horas extraordinarias** en el menú desplegable. <!-- TM 100 -->
4. Introduce una hora de inicio y finalización para la actividad. <!-- TM 100 -->
5. Haz clic en _Guardar_{:.doc-button}. <!-- TM 100 -->

## Informes <!-- TM 100 -->

En el informe **Actividades en horas** se reflejará que el empleado trabajó horas extraordinarias, ya que el nombre de la actividad incluye dicha información. De este modo, todas las horas extraordinarias trabajadas quedan documentadas y pueden ser consultadas por todas las personas relevantes, como el departamento financiero, que gestiona la retribución adicional de estas horas. <!-- TM 100 -->