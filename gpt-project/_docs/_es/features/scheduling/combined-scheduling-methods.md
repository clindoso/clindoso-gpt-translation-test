---
title: Combinar los métodos de planificación
product_label:
  - advanced
  - enterprise
  - classic
description: Combina los distintos métodos de planificación para adaptarte a las necesidades de tu negocio
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/availabilities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-time-pattern-models.md
---

Puedes combinar todos los {% link_new métodos de planificación | features/scheduling/scheduling-methods.md %} de distintas formas para crear planificaciones que se adapten tanto a las necesidades de tus empleados como a las de tu negocio.

Los siguientes ejemplos muestran algunos escenarios comunes en los que combinar métodos de planificación. También puedes usar otras combinaciones de métodos de planificación para satisfacer mejor las necesidades de tu organización.

## Escenario 1: empleados con turnos flexibles y empleados con horas o días laborables específicos  

Para este escenario, puedes combinar la planificación fija con turnos flexibles rotativos o turnos totalmente flexibles.

Para planificar a tus empleados con esta combinación, primero tienes que configurar los datos de configuración mostrados en la siguiente tabla, y asignárselos a los empleados pertinentes:


| Empleados con turnos flexibles            | Empleados con horas o días laborables específicos                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asígnales los modelos de planificación que deseas usar. | Crea rotaciones de turnos específicas que definan las horas o días en los que deben trabajar, y deja el resto de la semana en blanco.<br>Asígnales la rotación de turnos y los modelos de planificación pertinentes.                                    |

Para planificar a tus empleados, sigue estos pasos:

1. Inserta tus rotaciones de turnos.
2. Usa la funcionalidad **Crear planificación optimizada**.<br>injixo planificará tus turnos rotativos y totalmente flexibles de modo que complementen la cobertura proporcionada por las rotaciones de turnos.


## Escenario 2: empleados con turnos rotativos y empleados con turnos flexibles

Para este escenario, puedes combinar la planificación fija con turnos flexibles rotativos y turnos totalmente flexibles.

Para planificar a tus empleados con esta combinación, primero tienes que configurar los datos de configuración mostrados en la siguiente tabla, y asignárselos a los empleados pertinentes:

| Empleados con turnos flexibles rotativos           | Empleados con turnos totalmente flexibles                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asígnales modelos de planificación de tipo B o D. | Asígnales modelos de planificación de tipo A.                                   |


Usa la funcionalidad **Crear planificación optimizada**.<br>A los empleados con turnos flexibles rotativos se les asignará la rotación definida en sus modelos de planificación, y los empleados con turnos completamente flexibles completarán la planificación.

## Escenario 3: empleados con turnos rotativos y disponibilidad limitada

Este escenario se refiere a empleados que trabajan en turnos rotativos, pero no están disponibles durante ciertas horas, por ejemplo, no pueden trabajar más tarde de las 17:00&nbsp;h los miércoles.

Para este escenario, puedes combinar disponibilidades y turnos flexibles rotativos. 

1. Configura {% link_new disponibilidades | features/administration/availabilities.md %} para tus empleados para definir cuándo no pueden trabajar. En este ejemplo, los empleados está disponibles los miércoles solo hasta las 17:00&nbsp;h.
2. Asígnales los modelos de planificación pertinentes.

Para las semanas en las que trabajan el turno de mañana, se les planificará para el miércoles.<br>Para las semanas en las que trabajan el turno de tarde, no se les planificará para el miércoles y en cambio se les planificará para otros días de la semana.

## Escenario 4: empleados con turnos fijos y disponibilidad limitada puntualmente 

Este escenario se refiere a empleados que trabajan en turnos fijos, pero tienen una disponibilidad más restringida en algunos días particulares, por ejemplo, trabajan turnos de noche o durante el fin de semana, pero solo una de cada dos semanas.

Para este escenario, puedes añadir {% link_new modelos de horario de tipo Margen de disponibilidad | features/administration/daymodels/daymodel-basics.md | #tipos-de-modelos-de-horario %} a las {% link_new rotaciones de turnos | features/administration/shift-sequences.md %} para influenciar el resultado de la planificación en días particulares.<br>Consulta los dos ejemplos a continuación.

Para planificar a empleados de modo que trabajen uno de cada dos fines de semana, sigue estos pasos:

1. Crea un modelo de horario de tipo Margen de disponibilidad con un rango de tiempo desde la medianoche (0:00) hasta las 0:01 AM como bloqueador.
2. Añade el modelo de horario a un fin de semana en una rotación de turnos con 14 días. Deja el resto de días en blanco.
3. Asígnales la rotación de turnos a los empleados pertinentes.
4. Inserta la rotación de turnos en tu planificación.
5. Usa la funcionalidad **Crear planificación optimizada**.

injixo deja un fin de semana de cada dos libre y optimiza los días restantes.

Para planificar a empleados de modo que trabajen de noche una de cada dos semanas, sigue estos pasos:

1. Crea un modelo de horario de tipo Margen de disponibilidad con un rango de tiempo desde medianoche (0:00) a mediodía (12:00).
2. Añade el modelo de horario a todos los días de una semana en una rotación de turnos con 14 días. Deja el resto de días en blanco.
3. Asígnales la rotación de turnos a los empleados pertinentes.
4. Inserta la rotación de turnos en tu planificación.
5. Usa la funcionalidad **Crear planificación optimizada**.

injixo planifica el turno de noche para las semanas en las que los empleados están disponibles, siguiendo el modelo de planificación asignado a cada empleado. Para las otras semanas injixo puede planificar cualquier turno que sea compatible con el modelo de planificación.
