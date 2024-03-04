---
title: Editar o eliminar requisitos de personal
toc: false
product_label:
  - advanced
  - enterprise
description: Aprende cómo editar o eliminar los valores de los requisitos de personal calculados por injixo.
archive_ref: 20210819-en-employee-requirement
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
redirect_from:
  - /es/employee-requirement/
redirect_reason: Updated filename on 28 February 2024
---

Los requisitos de personal definen cuántos empleados necesitas para una actividad en un momento específico. Necesitas requisitos de personal para crear planificaciones con la funcionalidad **Crear planificación optimizada** o para optimizarlas con **Optimizar las pausas** o la **Optimización de tareas**.

Generar los requisitos de personal es el último paso del proceso de previsión. En injixo Forecast puedes usar los requisitos de personal generados automáticamente o aplicar un método específico de cálculo de personal. Antes de crear una planificación, comprueba que se hayan creado requisitos de personal para todas las actividades relevantes.

## Ver y editar requisitos de personal

En injixo puedes ver los requisitos de personal en los siguientes cuatro lugares:

- _Forecast_{:.breadcrumbs}
- _Analyze > Dashboard_{:.breadcrumbs}
- _Plan > Planificar_{:.breadcrumbs}
- _Plan > Centro de planificación_{:.breadcrumbs} 

La siguiente tabla incluye detalles sobre las opciones disponibles en cada lugar:

<style>
table {
   margin-left: 0px;
}
</style>

| Dónde  | Ver | Editar | Eliminar |
| ------ |--------| -------- |-------- |
| _Forecast_ | Sí | Sí | Sí |
| _Analyze > Dashboard_{:.breadcrumbs} | Sí | No | No |
| _Plan > Planificar_{:.breadcrumbs}. | Sí | No | No |
| _Plan > Centro de planificación_{:.breadcrumbs} | Sí | Sí | No |

### Editar requisitos de personal en el Centro de planificación

1. Ve a _Plan > Centro de planificación_{:.breadcrumbs}.
2. Al final del panel, haz clic en la pestaña **Actividades - Necesidad** o en **Vista de actividades**.<br>
   > Mensaje Ningún registro en una celda
   >
   > Si una de las celdas de la tabla inferior muestra el mensaje Ningún registro, selecciona **Plan** o **Estado actual** en el menú desplegable **Levels** arriba a la derecha.

3. Para expandir una unidad de planificación, haz clic en el {% icon plus %} en el lado izquierdo de las tablas.
4. Haz clic con el botón derecho en cualquier celda de la tabla inferior y selecciona **Editar requisitos de personal**.
5. En la ventana **Editar necesidad de personal**, haz clic en una celda e introduce el nuevo valor.<br>
  No puedes editar celdas resaltadas en azul porque representan actividades eliminadas que todavía siguen asignadas a la unidad de planificación.<br>
  
6. (Opcional) Para editar varias celdas a la vez, copia una fila de valores de una hoja de cálculo. Haz clic en una celda y arrastra el ratón hacia la derecha. Pulsa Ctrl+V para pegar los valores.<br>
7.  Haz clic en _Aceptar_{:.doc-button}.

### Editar requisitos de personal en Forecast

Para editar requisitos de personal manualmente puedes ejecutar el script de requisitos constantes en _Forecast_{:.breadcrumbs}. El siguiente procedimiento explica cómo configurar el script específicamente para este escenario. Para más información sobre las distintas opciones de configuración consulta el artículo {% link_new Requisito constante | features/forecast/requirement-scripts/requirement-constant.md %}.

1. Ve a _Forecast > Scripts de requisito_{:.breadcrumbs}.
2. En el recuadro **Otros - Constante**, haz clic en _Abrir_{:.doc-button}.<br>
3. La ventana de configuración del script solo está disponible en inglés. Configura los siguientes ajustes:
   - En la sección **Date**:
     - **Start Date**: introduce la fecha de inicio para el cambio de los requisitos.
     - **Number of Days**: introduce el número de días consecutivos (empezando con la fecha de inicio) para los que quieres editar los requisitos.
     - **Consider Each Day of the Week**: selecciona **No**.
     - **Add to Existing Requirement**: deja la casilla desmarcada. 
     - **Number Of Days With Timespans**: para editar los requisitos de personal de todos los días en un periodo de tiempo, selecciona 1.
     - **Timespans Per Day**: selecciona el número de periodos dentro de un día para los que quieres editar los requisitos de personal (p.&nbsp;ej. 1 si quieres editar los requisitos de personal para el día completo, pero 3 si quieres configurar requisitos de personal distintos para la mañana, la tarde y la noche).
     - **Number of Activities**: selecciona el número de actividades para las que quieres editar los requisitos de personal.
   - En la sección **Data**:
     - **Planning unit** y **Activity**: selecciona la unidad de planificación y actividad relevantes para cada actividad cuyos requisitos de personal quieras editar.
     - **Agents**: introduce el número de empleados que quieres usar como requisitos de personal.
     - **Start** y **End**: selecciona el periodo o periodos de tiempo para los que quieres editar los requisitos de personal.
4. Haz clic en _OK_{:.doc-button}.

## Eliminar requisitos de personal

injixo no ofrece ninguna opción para eliminar requisitos de personal. Puedes editar los requisitos de personal para que sean 0, lo que tiene el mismo efecto que eliminarlos.

 Tienes dos opciones para establecer requisitos de personal con valor 0:
 - Sigue los pasos para [editar requisitos de personal en el Centro de planificación](#editar-requisitos-de-personal-en-el-centro-de-planificación) e introduce 0 en las celdas pertinentes.
 
 - Sigue los pasos para [editar requisitos de personal en Forecast](#editar-requisitos-de-personal-en-forecast) e introduce 0 en el campo **Agents**.

La siguiente imagen muestra el script de requisitos constantes configurado para eliminar requisitos de personal en Forecast para un día completo (en este ejemplo Day 1):

{{ 3 | image: 'Ejemplo del script de requisitos constantes con una actividad de 00:00 a 00:00 y requisitos 0', '80%' }}
