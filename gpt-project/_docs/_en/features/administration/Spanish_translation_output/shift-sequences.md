---
title: Crear secuencias de turnos
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Usa las secuencias de turnos para gestionar planificaciones periódicas.
redirect_from:
  - /es/shift-sequence-overview/
redirect_reason: filename used in old product onboarding
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Añadir una secuencia de turnos
    filepath: features/scheduling/capacity/capacity-insert-shift-sequences.md
---

Una secuencia de turnos es un patrón semanal de modelos de días o actividades. Con las secuencias de turnos puedes insertar estos patrones repetitivos rápidamente en tu planificación y dejar que injixo optimice el resto de la planificación.

Las secuencias de turnos pueden ahorrarte una gran cantidad de tiempo ya que no tienes que planificar manualmente los patrones repetitivos una y otra vez.

Hay cuatro casos de uso para las secuencias de turnos:

1. Definir días en los que deben planificarse ciertos turnos
2. Planificar actividades periódicas
3. Definir días en los que el personal no trabaja
4. Definir cuándo pueden planificarse turnos basándose en la disponibilidad del personal

Las secuencias de turnos se componen de una o varias filas. Cada fila es un patrón individual que puede insertarse en la planificación.<br>
Cada fila contiene celdas que representan los días de la semana. En las celdas insertas los modelos de día o las actividades que quieres planificar con la secuencia de turnos.<br>
Cada fila representa un patrón semanal para tu planificación, por eso el número de celdas en una fila tiene que ser un múltiplo de siete. Una secuencia de turnos puede tener un máximo de 53 filas porque no puede durar más de un año.

## Prerrequisitos

Para crear secuencias de turnos, primero debes haber {% link_new creado | features/administration/activities.md %} modelos de días o actividades.<br>
Tras crear las secuencias de turnos, debes {% link_new asignarlas al personal | features/administration/employee-overview.md | #asignar-una-secuencia-de-turnos %} antes de poder insertarlas en tu planificación.

>Ten en cuenta
>
>La semana laboral empieza por defecto el lunes.
>
Puedes modificar el primer día de la semana con el ajuste _48420_{:.id-label} _Primero del rango de fechas_.

## Crear secuencias de turnos

Antes de crear tu primera secuencia de turnos, determina cuántas secuencias de turnos necesitarás y cuántas filas y celdas tiene que tener cada una. Esto dependerá completamente de las necesidades de tu organización: cómo sean los turnos que planifiques, si planificas reuniones recurrentes, etc.

Para crear secuencias de turnos, ve a _Planificar > Configuración > Secuencias de turnos_{:.breadcrumbs} y sigue estos pasos:

1. Haz clic en el icono de Crear {% icon item-add | icon-only %} arriba a la izquierda.
2. Configura los ajustes de la secuencia de turnos:<br>
  **Nombre**: Introduce un nombre inequívoco (máx. 50 caracteres).<br>
  **Abreviatura**: Introduce el nombre o una versión abreviada del mismo (máx. 25 caracteres).<br>
  **(Filas de) empleado**: Introduce el número de filas para la secuencia de turno (máx. 53).<br>A cada fila se le asigna un número. Haz doble clic en una fila para renombrarla. Necesitarás el número de la fila para asignársela a un empleado más tarde.<br>
  **Duración**: Introduce un valor entre 1 y 371 días.
3. Haz clic en _Aceptar_{:.doc-button}.

>Ten en cuenta
>
>La duración de una secuencia de turnos siempre tiene que ser un múltiplo de siete, incluso si tu organización opera únicamente cinco o seis días a la semana. Las secuencias de turnos tienen ciclos automáticos. Una secuencia de 5 días insertaría el turno del lunes en una celda de sábado, el turno del martes en una celda de domingo, etc.
>
>Si quieres planificar patrones con distintas duraciones (por ejemplo, uno para reuniones semanales y uno para reuniones quincenales), necesitas crear secuencias de turnos separadas.

Una vez hayas creado una secuencia de turnos, puedes {% link_new definir un rango de fechas | features/administration/set-a-validity-period.md %}:

1. Haz clic en el icono de Editar encima de la tabla.
2. Introduce o selecciona las fechas en los campos **Válido desde** y **Válido hasta**.
3. Haz clic en _Aceptar_{:.doc-button}.

### Insertar modelos de día

1. En el recuadro **Opciones**, selecciona **Insertar modelo de día** en el menú desplegable a la izquierda.
2. Selecciona el modelo de día que quieres insertar en el menú desplegable **Modelo de día**.
3. Introduce un **número**. Este será el número de turnos consecutivos en los cuales insertas el modelo de día.
4. En la tabla, haz clic en la primera celda en la que quieres insertar el modelo de día.<br>
  Si has introducido un número mayor que uno, el modelo de día se insertará en esa celda y en celdas adicionales a la derecha hasta alcanzar ese número.

La secuencia de turno se guarda automáticamente.

> Consejo
>
> Usa actividades o modelos fijos. Si insertas modelos de días variables en una secuencia de turnos, el turno siempre comenzará a la hora más temprana posible.

### Insertar actividades

1. En el recuadro **Opciones**, selecciona **Insertar actividad** en el menú desplegable a la izquierda.
2. Elige la actividad que quieres insertar del menú desplegable **Actividad**.
3. Introduce un **número**. Este será el número de días consecutivos en los cuales insertas la actividad.
4. Para especificar a qué hora está planificada la actividad, introduce un intervalo de tiempo (en formato horario 24 horas) en los campos **desde** y **hasta**, o marca la casilla **Día completo**.
5. En la tabla, haz clic en la primera celda en la que quieres insertar la actividad.<br>
  Si has introducido un número mayor que uno, la actividad se insertará en esa celda y en celdas adicionales a la derecha hasta alcanzar ese número.

>Actividades que terminan pasada la medianoche
>
>Si quieres insertar actividades que finalizan pasada la medianoche, añade 24 a la hora de finalización, es decir, si la actividad debería finalizar a la 1 de la madrugada del día posterior, introduce 25:00.

## Editar secuencias de turnos

1. En el recuadro **Secuencias de turnos**, selecciona una secuencua de turnos en el menú desplegable.
2. Haz clic en _Aplicar_{:.doc-button}.
3. Haz clic en el icono de Editar {% icon item-edit | icon-only %} en la barra de acciones arriba.<br>Renombra la secuencia de turnos, modifica la abreviatura, el número de filas de empleados o la duración.<br>Cuando hayas terminado, haz clic en _Aceptar_{:.doc-button}.
4. Haz clic en el icono de Editar en la barra de acciones arriba para editar el rango de fechas.<br>Cuando hayas terminado, haz clic en _Aceptar_{:.doc-button}.

### Eliminar elementos de una secuencia de turnos

Si quieres eliminar uno o unos pocos elementos de la secuencia de turnos, sigue estos pasos:
1. En el recuadro **Secuencias de turnos**, selecciona una secuencia de turnos en el menú desplegable.
2. Haz clic en _Aplicar_{:.doc-button}.
3. En el recuadro **Opciones**, selecciona **Eliminar** en el menú desplegable.
4. Haz clic en las celdas cuyos elementos quieres eliminar.<br>
  Los elementos se eliminan automáticamente.

Para eliminar todos los elementos de una secuencia de turnos, sigue estos pasos:

1. En el recuadro **Secuencias de turnos**, selecciona una secuencia de turnos en el menú desplegable.
2. Haz clic en _Aplicar_{:.doc-button}.
3. En el recuadro **Opciones**, marca la casilla **Eliminar todos** y haz clic en _Aplicar_{:.doc-button}.

Los elementos se eliminan automáticamente.

## Eliminar una secuencia de turnos

1. En el recuadro **Secuencias de turnos**, selecciona una secuencia de turnos en el menú desplegable.
2. Haz clic en _Aplicar_{:.doc-button}.
3. Haz clic en el icono de Eliminar {% icon item-delete | icon-only %} en la barra de acciones arriba.
4. En el cuadro de diálogo de confirmación, haz clic en _Sí_{:.doc-button}.

## Casos de uso

Puedes usar las secuencias de turnos para varios escenarios.

### Caso de uso 1: planificar turnos en días específicos

Este caso de uso se aplica, por ejemplo, cuando tienes que planificar turnos de mañana y de tarde para diferentes grupos de empleados. O si tienes un empleado al que no se le puede planificar trabajo antes de cierta hora, aunque esté disponible antes de esa hora el resto de la semana.

Puedes aprender en qu casos se aplica este caso de uso y cómo configurar las secuencias de turnos en nuestras vídeo-clases a continuación:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-1.vtt" kind="subtitles" srclang="en" label="English" default>
   </video>
</div>
<br>

### Caso de uso 2: planificar actividades periódicas

Este caso de uso se aplica, por ejemplo, cuando tienes que planificar reuniones semanales o si quieres insertar la actividad de hacer trabajo de back office durante una hora todos los días a la misma hora.
</script>

Puedes aprender en qu casos se aplica este caso de uso y cómo configurar las secuencias de turnos en nuestras vídeo-clases a continuación:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-2.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-2.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

### Caso de uso 3: planificar ausencias

Este caso de uso se aplica, por ejemplo, si tienes que definir patrones específicos de días libres para empleados concretos. 

Puedes aprender en qu casos se aplica este caso de uso y cómo configurar las secuencias de turnos en nuestras vídeo-clases a continuación:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-3.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-3.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

### Caso de uso 4: planificar turnos basándose en la disponibilidad del personal

Este caso de uso se aplica cuando quieres planificar personal con disponibilidad variable.

Puedes aprender en qu casos se aplica este caso de uso y cómo configurar las secuencias de turnos en nuestras vídeo-clases a continuación:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-4.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-4.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

## Generar un informe

Puedes generar un informe en formato PDF que incluye todos los datos de una secuencia de turnos. Sigue estos pasos:

1. En el recuadro **Secuencias de turnos**, selecciona la secuencia para la que quieres generar un informe.
2. Haz clic en _Aplicar_{:.doc-button}.
3. En _Informe_{:.doc-button}, puedes seleccionar la casilla para enviar el informe a la dirección de correo electrónico que usas para tu cuenta de injixo.

El informe muestra la hora de inicio y finalización de las actividades o modelos de día asociados a la secuencia de turnos, así como su duración neta en horas. El informe está estructurado en semanas.
Además, el informe muestra los siguientes totales y promedios de la duración neta de las actividades y modelos de día:

- Total por fila: duración neta de todas las actividades y modelos de día en la secuencia de turnos
- Suma de columnas: duración neta total por semana de actividades y modelos de día
- Promedio por fila: valor promedio de todas las duraciones de acciones y modelos de días en la columna de Totales
