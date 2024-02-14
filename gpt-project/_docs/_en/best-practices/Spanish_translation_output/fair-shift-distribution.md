---
title: Garantizar la equidad en la planificación. <!-- Repetition of GPT translation -->
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Asegurar una distribución más equitativa de los turnos y lograr una mayor percepción de equidad en el horario. <!-- Repetition of GPT translation -->
---

Independientemente del {% link_new método de planificación | features/scheduling/scheduling-methods.md %} que uses, es probable que haya empleados que reciban más a menudo turnos impopulares debido a su disponibilidad o porque poseen habilidades especializadas. Esto puede hacer que se sientan insatisfechos, reducir la moral y aumentar la rotación de empleados. <!-- GPT translation -->

Este artículo te proporciona consejos sobre prácticas recomendadas para garantizar una distribución más equitativa de los turnos y una mayor percepción de equidad. <!-- GPT translation -->

## Secuencias de desplazamiento para distribuciones uniformes <!-- GPT translation -->

Usa secuencias de turnos para asegurar una distribución más equitativa de las tareas o turnos. Con las secuencias de turnos, creas horarios que se repiten regularmente. <!-- GPT translation -->

{{ 1 | image: 'Sequences Shift'}} <!-- GPT translation -->

Se recomienda crear secuencias para los turnos, en especial para los de fin de semana. Los turnos de los fines de semana se distribuyen equitativamente entre tus empleados. Tus empleados pueden incluso prever cuándo trabajarán los fines de semana. <!-- GPT translation -->

### Combinar secuencias de turno con la optimización de horarios <!-- GPT translation -->

Si quieres usar la Optimización de horarios pero también quieres distribuir de manera equitativa algunos turnos, puedes combinar el uso de secuencias de turnos con la Optimización de horarios. <!-- GPT translation -->

Si quieres alternar los turnos de fin de semana, realiza lo siguiente. <!-- GPT translation -->

1. Crea una {% link_new disponibilidad de modelo de día | features/administration/availabilities.md %} con una duración de 1 minuto que marca el día como completamente no disponible. <!-- GPT translation -->
2. Inserta el modelo de disponibilidad de este día en una secuencia de turnos de dos semanas, alternando cada fin de semana, y dejando los demás días en blanco. <!-- GPT translation -->

Antes de ejecutar la optimización del horario, inserta la secuencia del turno en el horario. <!-- GPT translation -->

- En las semanas con el periodode disponibilidad de franjas horarias, no planificaremos al empleado para el fin de semana, y optimizaremos su horario la semana laboral. <!-- GPT translation -->
- En semanas en las que el fin de semana no esté bloqueado, el empleado puede trabajar durante esos días. Se optimizará tanto el horario para el fin de semana como el resto de la semana. <!-- GPT translation -->

## Crear modelos de planificación <!-- TM 64 -->

Si deseas optimizar los turnos mientras aplicas pautas de rotación, usa _modelos de calendario_{:.menu-item}. <!-- GPT translation -->

Los modelos de patrones horarios te permiten programar a tus empleados para que trabajen turnos tempranos, intermedios y tardíos en un patrón rotativo semanal fijo. En cada semana, los turnos que se pueden trabajar se eligen de una lista de **modelos diarios** que especificas en un **patrón horario semanal**. La optimización está limitada por el **tipo** que especifiques en el modelo de patrón horario: Rotación flexible (por ejemplo), Rotación fija, etc. <!-- GPT translation -->

## Cambios impopulares: días de excepción <!-- GPT translation -->

En el caso de que no quieras asignar turnos impopulares o tareas para toda la semana, sino que solo quieras programar uno o dos por semana para cada empleado, puedes utilizar _patrones semanales_{:.menu-item} con las **excepciones**: <!-- GPT translation -->

1. Crea un **patrón de horario semanal** con tus turnos habituales. <!-- GPT translation -->
Por favor, entrega el diseño dos semanas antes del 02.10.20. <!-- GPT translation -->
En el patrón de tiempo semanal, introduce un valor de 1 (o más) en el campo de **Núm. máx. de días de descanso consecutivos por semana** para definir cuántos turnos impopulares puede recibir un empleado en una semana. <!-- GPT translation -->
{{ 'El modelo del patrón temporal semanal' | imagenes: 'Week Time Pattern Model', '50%' }} <!-- GPT translation -->
Crea un segundo **patrón de turnos semanales** con tus turnos impopulares. <!-- GPT translation -->
En un modelo de patrón de trabajo, agrega los programas semanal(es) con los turnos estándares. <!-- GPT translation -->
El modelo incluye 5 patrones estándar por turnos semanales. <!-- GPT translation -->
5. Selecciona el modelo de asignación del período semanal con turnos impopulares en el menú desplegable **Week Time Pattern - Exception Days**.

Translation: Select the weekly time pattern with unpopular shifts from the **Week Time Pattern - Exception Days** drop-down menu. <!-- GPT translation -->
{ 2 | image: 'work time pattern model', '50%' }
The scale of the differences between working patterns. <!-- GPT translation -->

## Subasta de turnos más justa <!-- GPT translation -->

En el corto plazo en la planificación de turnos es posible que a algunos empleados no se les asignen los turnos que solicitaron. Para conseguir una asignación más justa, puedes dar prioridad a ciertas selecciones. Así lograrás, a largo plazo, un sorteo equitativo, algo que el puro principio aleatorio quizás no consiga. <!-- GPT translation -->

Para ello, asigna a los empleados a las distintas selecciones y rota la selección que oritas para hacer las asignaciones en cada ciclo de planificación. <!-- GPT translation -->

Ejemplos: <!-- TM 89 -->

- En junio, la selección A será la primera en ofertar, seguida por B y después por C. <!-- GPT translation -->
- En julio, la selección B hace la primera puja, seguida de C y, finalmente, A. <!-- GPT translation -->
- En agosto, la selección C lanza la primera oferta, seguida por A, y por último B. <!-- GPT translation -->
- Etc. <!-- GPT translation -->