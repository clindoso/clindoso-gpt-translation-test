---
title: Importar previsiones
description: Importar una previsión de una fuente externa a injixo Forecast.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Si quieres usar datos históricos generados por una fuente externa, como tus clientes o una aplicación externa, puedes importar previsiones externas a injixo Forecast. 

¿Estás empezando con injixo Forecast? Consulta primero {% link_new la información básica | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Preparar la importación

### Prerrequisitos

Para importar una previsión, necesitas al menos:

- una {% link_new integración | features/acd-integration/cloud/how-integrations-work.md %} que importe datos
- una carga de trabajo con una {% link_new cola | features/forecast/injixo-forecast/manage-workloads.md | #colas-y-canales %}
 
### Crear una cola

Para crear una cola, necesitas importar datos históricos de contacto mediante una integración. Las integraciones crean colas automáticamente.

Si no tienes ninguna integración que importe continuamente datos históricos, importa un archivo CSV para crear una cola:

1. {% link_new Añade una integración de archivos CSV | features/acd-integration/cloud/add-csv-integration.md | #configurar-una-nueva-integración-de-archivos-csv %}.
   - Omite la instalación de Cloud Link.
   - En la sección **Configuración**, selecciona **Datos de contacto**.
2. Crea un archivo CSV para los datos de contacto con al menos una fila para un solo intervalo, p.&nbsp;ej.:
   ```
   Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
ForecastImportQueue;22/02/2022;02:02;2;2;2
   ```
3. {% link_new Importa manualmente el archivo CSV | features/acd-integration/cloud/add-csv-integration.md | #importación-manual-de-archivos %}.  
   La cola se crea tras la importación.
   Usa esta cola para importar previsiones en todas tus cargas de trabajo.

### Asignar la cola a una carga de trabajo

Cuando creas una carga de trabajo, tienes que asignarle una cola. Esta es una parte integral del proceso de creación, además de un prerrequisito para [importar una previsión](#importar-una-previsión). Lee más sobre cómo crear una {% link_new carga de trabajo | features/forecast/injixo-forecast/manage-workloads.md | #crear-cargas-de-trabajo%}.

Puedes importar una previsión en una carga de trabajo existente, o añadir cualquiera de tus colas a una nueva carga de trabajo.

### Requisitos para los datos importados

Tus datos importados deben cumplir los siguientes requisitos:

| Requisitos                          | Detalles                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Formato de marca de tiempo                     | YYYY-MM-DD HH:MM                                                                                                                   |
| Datos de volumen                          | Números enteros                                                                                                           |
| Datos de TMO                             | Números enteros o números decimales (separados por punto)                                                                  |
| Formato de encabezado                   | `Timestamp;Offered;AHT` o un texto personalizado, (p.&nbsp;ej.&nbsp;`Timestamp;Offered_customtext;AHT_customtext`).                                 |
| Separadores                 | Punto y coma o coma (detección automática)                                                                                                 |
| Tamaño máximo del archivo                    | 20&nbsp;MB.<br>Los archivos no deben sobrepasar las 20.000 filas.                                                                         |
| Zona horaria                            | Debe corresponder con la zona horaria de la cola.                                                                                          |
| Duración del intervalo                      | Debe corresponder con el intervalo de la cola (15, 30 o 60 minutos).                                                               |


De modo alternativo, puedes {% link_new descargar una previsión (o una versión de la previsión) | features/forecast/injixo-forecast/download-forecast.md %} en formato CSV y usarla como plantilla para tu archivo de importación. La previsión solo lee las columnas `Timestamp`,`Offered` y `AHT`. Otras columnas, como `Offered_operational` y `AHT_operational` en el siguiente ejemplo, son ignoradas.

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
2020-05-17 16:30;40;180;50;170
```

### Gestionar los datos faltantes

Tus archivos de importación pueden tener intervalos sin datos. El gráfico de volumen o TMO resultante mostrará los valores importados como cero (0).  Las filas o valores vacíos no serán importados.

Si faltan datos para uno o varios intervalos, puedes editar tu archivo CSV como a continuación:

- Deja vacíos los campos de volumen y TMO:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:15;;
2020-05-17 15:30;40;180
  ```

- Importa las columnas con ceros:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:15;0;0
2020-05-17 15:30;40;180
  ```

- Omite la fila completa:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:30;40;180
  ```

## Importar una previsión

1. En _Forecast > Workloads_{:.breadcrumbs}, selecciona la carga de trabajo para la que quieres importar la previsión externa.
2. Del menú con tres puntos verticales {% icon ellipsis_v | icon-only %} arriba a la derecha, selecciona **Importar datos de previsión**.
3. Haz clic en _Elegir archivo_{:.doc-button} y selecciona el archivo CSV que quieres importar.
4. Haz clic en _Importar datos_{:.doc-button}.<br>
   La ventana se actualiza y muestra si la importación tuvo éxito.
5. Haz clic en _Finalizado_{:.doc-button}.<br>
Recarga la página para ver el gráfico actualizado del periodo de la importación. Los valores importados se muestran como una línea marrón en los gráficos en las secciones de volumen y AHT.
   Para ocultar la previsión importada en el gráfico, haz clic en icono Mostrar/ocultar {% icon eye | icon-only %} en la leyenda junto a **Importada**.
