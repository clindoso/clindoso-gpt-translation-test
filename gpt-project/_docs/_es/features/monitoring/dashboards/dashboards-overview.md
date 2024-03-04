---
title: Gestionar los cuadros de mando
permalink: /es/dashboards-overview/
promote-service: team-leader-training
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Usa los cuadros de mando para analizar tus datos de volumen de contacto y nivel de ocupación.
related_articles:
  - overwrite_title: Navegar los gráficos
    filepath: features/monitoring/dashboards/work-with-charts.md
  - overwrite_title: Ejemplos de cuadros de mando
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

En _Analyze > Dashboards_{:.breadcrumbs} puedes crear y visualizar cuadros de mando con hasta cuatro gráficos. Cada gráfico puede mostrar diagramas con diversas series temporales y periodos de tiempo. Si no tienes ningún cuadro de mando, la página muestra el modo de edición y puedes [crear un cuadro de mando](#crear-cuadros-de-mando).

- Para mostrar un cuadro de mando ya existente, selecciónalo en el menú desplegable, o introduce el nombre en el campo para filtrar los resultados.  
- Para ver los valores de un intervalo específico, mueve el ratón sobre un gráfico en el cuadro de mando.
- Para cambiar al modo de pantalla completa, haz clic en el {% icon maximize %} arriba a la derecha.

También puedes {% link_new cambiar entre vista de gráfico y de tabla | features/monitoring/dashboards/work-with-charts.md | #navegar-los-gráficos %} con los iconos Mostrar tabla {% icon table-list | icon-only %} y Mostrar gráfico {% icon chart-view | icon-only %} arriba a la derecha de la vista.

## Crear cuadros de mando

1. Ve a _Analyze > Dashboards_{:.breadcrumbs}.
2. En el {% icon ellipsis_v %} a la derecha, selecciona **Crear nuevo cuadro de mando**.
3. Completa los siguientes campos:
  - **Nombre**: nombre único para tu cuadro de mando.
  - **Diseño**: selecciona el número y diseño de tus gráficos.
  - **Gráfico sin título**: nombre para cada gráfico. Los nombres no tienen que ser únicos.
4. Selecciona un **rango de fechas** para cada gráfico.
5. (Opcional) Activa la opción **Usar fechas revolventes** para posponer la fecha de inicio por un día cada día.
6. En la vista de árbol a la izquierda, selecciona series temporales y arrástralas a los gráficos para visualizar distintas figuras clave:
   - **Cargas de trabajo**: histórico, previsión, importación, y {% link_new versiones de la previsión | features/forecast/injixo-forecast/store-forecast-versions.md %}. 
   - **Unidad de planificación**: ocupación, requisitos de personal y cobertura para los turnos y actividades planificados, además de turnos solicitados en Me.
   - **Colas de WFM**: datos de cargas de trabajo en colas de WFM que guardaste mediante la opción _Usar previsión_{:.doc-button} en la página de la carga de trabajo. Esta opción puede no estar disponible, dependiendo de tu plan WFM. 

      > Atención
      >
      > - El {% icon circle_exclamation %} en la leyenda de un gráfico aparece cuando no tienes datos para un periodo.
      > - En las cargas de trabajo puedes ver figuras clave según tu integración, p.&nbsp;ej. si tus cargas de trabajo solo incluyen colas de una {% link_new integración de Genesys Cloud | features/acd-integration/cloud/add-genesys-cloud-integration.md %} ves información sobre llamadas abandonadas, velocidad media de respuesta y llamadas atendidas dentro del nivel de servicio. 

7. Haz clic en _Guardar_{:.doc-button}.<br>Para volver al modo de vista, haz clic en _Cerrar modo de edición_{:.doc-button}.

### Duplicar un cuadro de mando

Para crear un cuadro de mando nuevo con las mismas propiedades generales que otro cuadro de mando ya existente, sigue estos pasos:
1. Ve a _Analyze > Dashboards_{:.breadcrumbs}.
2. En el menú desplegable, selecciona un cuadro de mando.
3. En el {% icon ellipsis_v %}, selecciona _Duplicar cuadro de mando_{:.doc-button}.
4. Edita el nombre y los detalles de configuración, en caso necesario.
5. Haz clic en _Guardar_{:.doc-button}.

### Recargar cuadros de mando automáticamente

Puedes recargar automáticamente el cuadro de mando seleccionado. Para hacerlo, seleccione un intervalo del menú desplegable a la derecha y haga clic en _{% icon arrows-rotate | icon-only %}Recargar automát._{:.doc-button}.<br>En la parte inferior izquierda de la página puedes ver cuándo se actualizó el cuadro de mando por última vez.

## Editar cuadros de mando

1. Ve a _Analyze > Dashboards_{:.breadcrumbs}.
2. En el menú desplegable, selecciona un cuadro de mando.
3. En el {% icon ellipsis_v %} a la derecha, selecciona **Editar**.
4. Edita el cuadro de mando, {% link_new personaliza las series temporales | features/monitoring/dashboards/work-with-charts.md | #personalizar-series-temporales %} o {% link_new elimínalas | features/monitoring/dashboards/work-with-charts.md | #eliminar-series-temporales %}.
5. Haz clic en _Guardar_{:.doc-button}. Para volver al modo de vista, haz clic en _Cerrar modo de edición_{:.doc-button}.

## Eliminar cuadros de mando

1. Ve a _Analyze > Dashboards_{:.breadcrumbs}.
2. En el menú desplegable, selecciona un cuadro de mando.
3. En el {% icon ellipsis_v %} a la derecha, selecciona **Editar**.
4. Haz clic en _Eliminar_{:.doc-button} en la parte inferior derecha.  
5. En la ventana de confirmación, haz clic en _Eliminar cuadro de mando_{:.doc-button}.<br> Para cancelar la eliminación, haz clic en _Mantener cuadro de mando_{:.doc-button}.

Si eliminas el último cuadro de mando restante, la página muestra el modo de edición hasta que [crees un nuevo cuadro de mando](#crear-cuadros-de-mando).
