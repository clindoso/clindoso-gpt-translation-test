---
title: Gestión de horas extraordinarias
product_label:
  - advanced
  - enterprise
  - classic
description: Aprende el mejor modo de configurar las actividades para planificar horas extraordinarias y documentarlas de manera transparente.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

En ocasiones, es necesario que tus empleados trabajen horas extraordinarias para mantener unos niveles de servicio razonables. Las razones para planificar horas extraordinarias incluyen una carga de trabajo inesperadamente alta o falta de personal causada por altas tasas de ausencia por enfermedad o vacaciones.  
En muchos casos, los contratos de tus empleados estipulan que las horas extraordinarias tengan una retribución más elevada, o que las horas extraordinarias trabajadas se concedan como tiempo adicional de vacaciones. También es importante respetar otras restricciones contractuales cuando tus empleados trabajan horas extraordinarias, como el tiempo de descanso entre turnos. Si tu empresa es un proveedor de servicios, es posible que también estés obligado a informar a tus clientes sobre cualquier trabajo adicional programado. 

En este artículo, puedes encontrar consejos sobre cómo configurar actividades y multiactividades para poder planificar fácilmente horas extraordinarias y mostrarlas correctamente en tu mapa de calor de la cobertura y en tus informes.

Las horas extraordinarias deben planificarse manualmente en el Centro de planificación o en Planificar como una adición a la planificación existente.

## Crear actividades para horas extraordinarias

El ejemplo a continuación utiliza una actividad nueva llamada Llamadas. Sigue estos pasos para todas las actividades que quieras poder planificar como horas extraordinarias, es decir, para Llamadas o Correos electrónicos, pero no para Enfermedad o Vacaciones.

1. {% link_new Crea y configura la actividad | features/administration/activities.md %} **Llamadas**. 
2. Duplica la actividad **Llamadas** y nómbrala **Llamadas - horas extraordinarias**. No necesitas añadir cualificaciones a esta actividad.  
  - Marca la casilla **Trato especial en la planificación optimizada**.
  - Asegúrate de que la casilla **Se puede solicitar en Me**  no está marcada.
3. En **Llamadas - horas extraordinarias**, añade **Llamadas** como subactividad.  
  **Llamadas - horas extraordinarias** es ahora una multiactividad.
4. Añade ambas actividades a la unidad de planificación correspondiente. No añades la actividad de horas extraordinarias a ningún modelo de horario.

Con esta configuración, la actividad "Llamadas - horas extraordinarias" solo se puede planificar manualmente y no puede ser reemplazada durante la planificación optimizada. Tus empleados no podrán solicitar esta actividad en injixo Me.

Como has añadido "- horas extraordinarias" al nombre de la multiactividad, todos los empleados pueden ver claramente en la planificación cuándo alguien trabaja horas extraordinarias, durante cuánto tiempo y en qué tarea.

## Planificar horas extraordinarias

Puedes planificar horas extraordinarias manualmente tanto en _Plan > Centro de planificación_{:.breadcrumbs} como en _Plan > Planificación_{:.breadcrumbs}.

Para añadir actividades de horas extraordinarias en el Centro de planificación, sigue estos pasos:

1. Elige la unidad de planificación y, opcionalmente, la selección a la que pertenece el empleado a quien quieres planificar para horas extraordinarias.
2. Haz clic dos veces en la celda del empleado para el día en el que debe trabajar horas extraordinarias. Haz clic en la pestaña **Actividades múltiples** y selecciona **Llamadas - horas extraordinarias**.
3. Introduce una hora de inicio y finalización para la actividad.
4. Haz clic en _Aceptar_{:.doc-button}.

Las horas extraordinarias planificadas se reflejan inmediatamente en la ventana de planificación en la pestaña Actividades en la {% link_new ventana de parámetros | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %}. Si configuras la pestaña Actividades para mostrar la cobertura, el mapa de calor se actualizará y reflejará las horas extraordinarias planificadas.

Para añadir actividades de horas extraordinarias en _Plan > Planificar_{:.breadcrumbs}, sigue estos pasos:

1. Haz clic dos veces en una celda en la planificación para abrir el editor.
2. Haz clic en _Añadir una nueva actividad_{:.doc-button}.  
  Se añade una nueva fila a la derecha con la actividad.
3. En la nueva fila, selecciona **Llamadas - horas extraordinarias** en el menú desplegable.
4. Introduce una hora de inicio y finalización para la actividad.
5. Haz clic en _Guardar_{:.doc-button}.

## Informes

En el informe **Actividades en horas** se reflejará que el empleado trabajó horas extraordinarias, ya que el nombre de la actividad incluye dicha información. De este modo, todas las horas extraordinarias trabajadas quedan documentadas y pueden ser consultadas por todas las personas relevantes, como el departamento financiero, que gestiona la retribución adicional de estas horas.
