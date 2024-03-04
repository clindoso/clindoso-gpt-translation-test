---
title: Trabajar con gráficos
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprende cómo trabajar con los gráficos en un cuadro de mando.
related_articles:
  - overwrite_title: Ejemplos de cuadros de mando
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

En _Analyze > Dashboards_{:.breadcrumbs} puedes usar gráficos y series temporales para analizar tus datos. Para comenzar, selecciona un cuadro de mando del menú desplegable en la parte superior.

¿Es la primera vez que usas cuadros de mando? Consulta primero {% link_new la información básica | features/monitoring/dashboards/dashboards-overview.md %}.

## Navegar los gráficos

Las siguientes acciones están disponibles en **Dashboards**:

- Para modificar el rango de fechas para el que se muestran datos, selecciona un rango de fechas en el selector de fechas en la parte superior derecha de cada gráfico.
- Para ampliar un gráfico, haz clic y arrastra para seleccionar la zona que te interesa. 
- Para alejarte, haz clic en _Restablecer zoom_{:.doc-button}.
- Para cambiar a la vista de tabla, haz clic en el {% icon table-list %} en la parte superior derecha de cada gráfico.
- Para cambiar a la vista de gráfico, haz clic en el {% icon chart-view %}.
- Para copiar datos al portapapeles, haz clic en el {% icon clone %}.

> Atención
>
> La información de fecha y hora está localizada de acuerdo con tus ajustes de idioma en injixo. Esto podría causar problemas si copias datos de injixo a un documento de Excel o Google Sheets que use otro idioma.

## Trabajar con series temporales

Las series temporales son secuencias de puntos de datos registrados en intervalos de tiempo regulares. Las siguientes subsecciones explican cómo puedes usar las series temporales en **Dashboards** para personalizar y analizar tus datos y usarlos para tomar decisiones informadas.

### Resaltar series temporales

Para resaltar temporalmente una serie temporal en la vista de gráfico, mueve el ratón sobre el nombre de la serie temporal en la leyenda. Las demás series temporales se desvanecen en el fondo.

### Mostrar y esconder series temporales

Para esconder o mostrar otras series temporales, haz clic en el {% icon eye %} o el {% icon eye_slash %} junto al nombre relevante en la leyenda.

### Personalizar series temporales

1. Ve a _Analyze > Dashboards_{:.breadcrumbs}.
2. En el {% icon ellipsis_v %}, haz clic en **Editar**.
3. Mueve el ratón sobre el nombre de la serie temporal en la leyenda y haz clic en el {% icon pencil %}.
4. En la ventana **Personalizar gráfico**, edita las propiedades de la serie temporal:
   - Edita el **nombre** que aparece en la leyenda.
   - Escoge entre **Paso** e **Histograma** en el menú desplegable **Tipo**. 
   - Selecciona otro **color** predefinido.
   - Selecciona cómo agregar los datos en el gráfico. Escoge **Por intervalo** (disponible para rangos de fechas de hasta ocho días) para mostrar valores de intervalos, o **Por día** para mostrar valores diarios.
   - Selecciona si mostrar el eje y a la **izquierda (predeterminado)** o a la **derecha**.
5. Haz clic en _Guardar_{:.doc-button}.<br>Para volver al modo de vista, haz clic en _Cerrar modo de edición_{:.doc-button}.

### Eliminar series temporales

1. Ve a _Analyze > Dashboards_{:.breadcrumbs}.
2. En el {% icon ellipsis_v %}, haz clic en **Editar**.
3. Mueve el ratón sobre el nombre de la serie temporal en la leyenda y haz clic en el {% icon pencil %}.
4. En la ventana **Personalizar gráfico**, haz clic en _Eliminar_{:.doc-button}.
5. Haz clic en _Guardar_{:.doc-button}.<br>Para volver al modo de vista, haz clic en _Cerrar modo de edición_{:.doc-button}.

