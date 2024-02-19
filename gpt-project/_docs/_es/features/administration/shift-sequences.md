---
title: Crear rotaciones de turnos
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Usa las secuencias de turno para configurar planificaciones recurrentes.
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Insertar rotaciones de turnos
    filepath: features/scheduling/schedules/schedules-insert-shift-sequences.md
---

Una rotación de turnos es un patrón semanal de modelos de horario o actividades. Con las rotaciones de turnos puedes insertar rápidamente estos patrones recurrentes en tu planificación y dejar que injixo optimice el resto de la planificación.

Las rotaciones de turnos pueden ahorrarte muchas horas de trabajo, ya que no tienes que planificar los patrones recurrentes manualmente cada vez que los necesites.

Hay cuatro escenarios de uso para las rotaciones de turnos:

- Escenario 1: especificar los días en que se deben planificar ciertos turnos
- Escenario 2: planificar actividades recurrentes
- Escenario 3: especificar los días en que los empleados no trabajan
- Escenario 4: especificar cuándo se pueden planificar turnos en función de las disponibilidades de los empleados

Las rotaciones de turnos se componen de una o varias filas. Cada fila es un patrón individual que se puede insertar en la planificación.<br>
Cada fila contiene celdas que representan los días de la semana. En las celdas insertas los modelos de horario o actividades que quieras planificar con la rotación de turnos.<br>
Cada fila representa un patrón semanal para tu planificación, por lo que el número de celdas en una fila debe ser un múltiplo de siete. Una rotación de turnos puede tener un máximo de 53 filas porque no puede durar más de un año.

## Prerrequisitos

Para crear rotaciones de turnos, primero tienes que crear {% link_new actividades | features/administration/activities.md %} o {% link_new modelos de horario | features/administration/daymodels/daymodel-creation.md %}.<br>
Una vez hayas creado las rotaciones de turnos, tienes que {% link_new asignárselas a tus empleados | features/administration/employee-overview.md | #asignar-una-rotación-de-turnos %} antes de poder insertarlas en tu planificación.<br>
Cuando le asignas una rotación de turnos a un empleado, tienes que definir una fecha de referencia. La fecha de referencia es el primer día en el que se planificará la rotación de turnos. A partir de esa fecha, la rotación de turnos se repetirá continuamente mientras sea válida.<br>
Dado que las rotaciones de turnos son patrones semanales, configura como fecha de referencia un lunes, o el día en el que comience tu semana laboral.

>Atención
>
>Por defecto, la semana laboral comienza el lunes.
>
>Puedes cambiar el primer día de la semana con la configuración _48420_{:.id-label} _Inicio de la semana (planificación)_.

## Crear rotaciones de turnos

Antes de crear tu primera rotación de turnos, determina cuántas rotaciones de turnos necesitarás, así como el número de filas y celdas en cada una. Esto dependerá completamente de las necesidades de tu organización, p.&nbsp;ej., cuántos turnos diferentes planificas, si planificas reuniones recurrentes, etc.

Para crear rotaciones de turnos, ve a _Plan > Configuración > Rotaciones de turnos_{:.breadcrumbs} y sigue estos pasos:

1. Haz clic en el icono Nuevo {% icon item-add | icon-only %} arriba a la izquierda.
2. Configura la rotación de turnos:<br>
  **Nombre**: introduce un nombre inequívoco (máx. 50 caracteres).<br>
  **Abreviatura**: introduce el nombre o una versión más corta del mismo (máx. 25 caracteres).<br>
  **Fila(s) de empleado**: introduce el número de filas para la rotación de turnos (máximo 53).<br>A cada fila se le asignará un número. Haz doble clic en una fila para renombrarla. Necesitarás el número o nombre de la fila más adelante para asignársela a un empleado.<br>
  **Duración**: introduce un valor entre 7 y 371 días. La duración debe ser un múltiplo de siete.
6. Haz clic en _Aceptar_{:.doc-button}.

>Atención
>
>La duración de una rotación de turnos debe ser siempre un múltiplo de siete, incluso si su organización solo abre cinco o seis días a la semana. Las rotaciones de turnos se repiten automáticamente. Una secuencia de turnos de cinco días insertaría el turno del lunes en la celda del sábado, el turno del martes en la celda del domingo, etc.
>
>Si quieres planificar patrones con diferentes duraciones (p.&nbsp;ej., uno para reuniones semanales y otro para reuniones quincenales), debes crear rotaciones de turnos separadas.

Una vez hayas creado una rotación de turnos, puedes establecer {% link_new períodos de validez | features/administration/set-a-validity-period.md %} para la misma:

1. Haz clic en el {% icon item-edit %} encima de la tabla.
2. Introduce o selecciona las fechas en los campos **Válido desde** y **Válido hasta**.
3. Haz clic en _Aceptar_{:.doc-button}.

### Insertar modelos de horario

1. En el recuadro **Opciones**, selecciona **Insertar modelo de horario** en el menú desplegable a la izquierda.
2. Selecciona el modelo de horario que quieres insertar en el menú desplegable **Modelo de horario**.
3. Introduce un **número**. Este será el número de días consecutivos en los que insertas el modelo de horario.
4. En la tabla, haz clic en la primera celda en la que quieras insertar el modelo de horario.<br>
  Si has introducido un número mayor que uno, el modelo de horario se insertará en esa celda y en tantas celdas adicionales a la derecha como sea necesario hasta alcanzar ese número.

La rotación de turno se guarda automáticamente.

> Consejo
>
> Usa actividades o modelos de horario fijos. Si insertas modelos de horario variables en una rotación de turnos, el turno siempre comenzará a la hora más temprana posible.

### Insertar actividades

1. En el recuadro **Opciones**, selecciona **Insertar actividad** en el menú desplegable a la izquierda.
2. Elige la actividad que quieres insertar en el menú desplegable **Actividad**.
3. Introduce un **número**. Este será el número de días consecutivos en los que insertas la actividad.
4. Para especificar a qué hora está planificada la actividad, introduce un intervalo de tiempo (en formato 24 horas) en los campos **desde** y **hasta**, o marca la casilla **De jornada completa**.
5. En la tabla, haz clic en la primera celda en la que quieras insertar la actividad.<br>
  Si has introducido un número mayor que uno, la actividad se insertará en esa celda y en tantas celdas adicionales a la derecha como sea necesario hasta alcanzar ese número.

>Actividades que finalizan de madrugada
>
>Si quieres insertar actividades que finalizan de madrugada, suma 24 a la hora de fin, es decir, si la actividad debería finalizar a la 1 de la madrugada del día posterior, introduce 25:00.

## Editar rotaciones de turnos

1. En el recuadro **Rotación de turnos**, selecciona una rotación de turnos en el menú desplegable.
2. Haz clic en _Aplicar_{:.doc-button}.
3. Haz clic en el {% icon item-edit %} en la barra de acciones superior para editar el nombre, la abreviatura, el número de filas de empleado, o la duración.<br>Cuando hayas terminado, haz clic en _Aceptar_{:.doc-button}.
4. Haz clic en el {% icon item-edit %} en la barra de acciones sobre la tabla para editar los periodos de validez.<br>Cuando hayas terminado, haz clic en _Aceptar_{:.doc-button}.

### Eliminar elementos de una rotación de turnos

Si quieres eliminar uno o algunos elementos de la rotación de turnos, sigue estos pasos:
1. En el recuadro **Rotación de turnos**, selecciona una rotación de turnos en el menú desplegable.
2. Haz clic en _Aplicar_{:.doc-button}.
3. En el recuadro **Opciones**, selecciona **Eliminar** en el menú desplegable.
4. Haz clic en las celdas cuyos elementos quieres eliminar.<br>
  Los elementos se eliminan automáticamente.

Para eliminar todos los elementos de una rotación de turnos, sigue estos pasos:

1. En el recuadro **Rotación de turnos**, selecciona una rotación de turnos en el menú desplegable.
2. Haz clic en _Aplicar_{:.doc-button}.
3. En el recuadro **Opciones**, selecciona **Eliminar** en el menú desplegable.
4. Marca la casilla **Eliminar todos** y haz clic en _Aplicar_{:.doc-button}.

Los elementos se eliminan automáticamente.

## Eliminar una rotación de turnos

1. En el recuadro **Rotación de turnos**, selecciona una rotación de turnos en el menú desplegable.
2. Haz clic en _Aplicar_{:.doc-button}.
3. Haz clic en el {% icon item-delete %} en la barra de acciones superior.
4. En el diálogo de confirmación, haz clic en _Sí_{:.doc-button}.

## Escenarios de uso

Puedes usar las secuencias de turnos para varios escenarios.

### Escenario 1: especificar los días en que se deben planificar ciertos turnos

Este escenanario es relevante, por ejemplo, cuando tienes que planificar turnos de mañana y de tarde para diferentes grupos de empleados. O si tienes un empleado que no puede comenzar a trabajar antes de las 11&nbsp;a.&nbsp;m. los lunes, aunque el resto de la semana está disponible antes de esa hora.

Puedes aprender más sobre si este escenario es relevante para ti y sobre cómo configurar las rotaciones de turnos en el siguiente vídeo:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-1.vtt" kind="subtitles" srclang="en" label="English" default>
   </video>
</div>
<br>

### Escenario 2: planificar actividades recurrentes

Este escenario es relevante, por ejemplo, si tienes que planificar reuniones semanales o si quieres planificar que una persona haga una hora de back office todos los días a una hora concreta.

Puedes aprender más sobre si este escenario es relevante para ti y sobre cómo configurar las rotaciones de turnos en el siguiente vídeo:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-2.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-2.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

### Escenario 3: especificar los días en que los empleados no trabajan

Este escenario es relevante, por ejemplo, si tienes que definir patrones específicos de días libres para empleados concretos. 

Puedes aprender más sobre si este escenario es relevante para ti y sobre cómo configurar las rotaciones de turnos en el siguiente vídeo:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-3.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-3.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

### Escenario 4: Especificar cuándo se pueden planificar turnos en función de las disponibilidades de los empleados

Este escenario es relevante cuando quieres planificar a empleados con disponibilidad variable.

Puedes aprender más sobre si este escenario es relevante para ti y sobre cómo configurar las rotaciones de turnos en el siguiente vídeo:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-4.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-4.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

## Generar un informe

Puedes generar un informe en formato PDF que incluye todos los datos de una rotación de turnos. Para generar un informe, sigue estos pasos:

1. En el recuadro **Rotación de turnos**, selecciona la rotación de turnos para la que quieres generar un informe.
2. Haz clic en _Aplicar_{:.doc-button}.
3. Haz clic en _Informe_{:.doc-button} arriba de la tabla.
4. En el diálogo, puedes marcar la casilla para enviar el informe a la dirección de correo electrónico que usas para tu cuenta de injixo.

El informe muestra la hora de inicio y finalización de las actividades o modelos de horario incluidos en la rotación de turnos, así como su duración neta en horas. El informe está estructurado en semanas.
Además, el informe muestra los siguientes totales y promedios de la duración neta de las actividades y modelos de día:

- Fila Total: duración neta de todas las actividades y modelos de horario en la rotación de turnos.
- Columna de suma: duración neta total por semana de actividades y modelos de horario.
- Fila Promedio: valor promedio de todos los valores en la fila Total.
