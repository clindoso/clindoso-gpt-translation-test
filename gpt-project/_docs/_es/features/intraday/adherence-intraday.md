---
title: Adherencia intradiaria
toc: true
product_label:
  - advanced
  - enterprise
description: Consulta de un vistazo el nivel de adherencia de tus empleados a sus turnos a lo largo del día.
archive_ref: 20210422-de-adherence
---

Con Adherencia intradiaria puedes comparar las actividades planificadas para un empleado con las actividades que realmente ha llevado a cabo, y así identificar periodos en los que esté fuera de adherencia durante el día laboral.

Para que Adherencia intradiaria muestre datos, debes configurar primero la importación de {% link_new estados de los agentes en tiempo real | features/acd-integration/cloud/import-agent-status-data.md %}.

¿Es la primera vez que trabajas con Adherencia en tiempo real? Consulta primero {% link_new la información básica | features/intraday/real-time-adherence.md %}.

## Mostrar y buscar datos

1. Ve a _Intraday > Adherencia Intradiaria_{:.breadcrumbs}
2. Para mostrar datos de los agentes, selecciona una **unidad de planificación** y/o un **grupo**.
3. Para cambiar el día mostrado, haz clic en _Hoy_{:.doc-button} o _Ayer_{:.doc-button} o usa el **selector de fechas**.

La tabla muestra detalles de períodos fuera de adherencia organizados por persona. En el encabezado de la tabla puedes identificar períodos con baja adherencia. Puedes ordenar la tabla o usar la búsqueda en la parte superior para filtrar la vista con las {% link_new opciones de filtrar y ordenar | features/intraday/real-time-adherence.md | #search-and-filter %}.

{{ 1 | image: 'Adherencia Intradiaria','100%' }}

> Limita el acceso a los datos de empleados concretos a usuarios relevantes
>
> Configura los permisos para ciertas unidades de planificación o grupos para {% link_new usuarios o roles de usuario específicos | getting-started/configure-user-roles.md | #establecer-permisos-para-wfm %}.

## Valor de adherencia

La adherencia muestra en un valor porcentual si hubo desviaciones entre las actividades planificadas y las actividades reales que el empleado llevó a cabo.

Puedes analizar la adherencia a lo largo del día con ayuda del gráfico. Si el día aún no ha terminado, el valor se calcula hasta la marca temporal de la última actualización, que puedes ver arriba del valor de adherencia.

injixo muestra el objetivo de adherencia con una línea de puntos. Puedes {% link_new modificar el objetivo de adherencia | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}.

{{ 2 | image: 'Valor de adherencia','100%' }}

## Tabla de adherencia del agente

La tabla muestra los detalles de adherencia de los empleados planificados hoy. Puedes ordenar la tabla por nombre de empleado y por valor de adherencia.

Cada fila de la tabla contiene la línea temporal de un empleado. Puedes ver las diferencias entre las actividades planificadas y las actividades reales que el empleado llevó a cabo. Cada persona tiene un valor de adherencia individual. Los valores individuales se suman al valor general de la unidad de planificación (mostrado en el encabezado de la tabla). Las desviaciones se resaltan cuando el valor cae por debajo del {% link_new objetivo de adherencia configurado | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}.

Los colores representan tres tipos de estados fuera de adherencia:

- No está presente (rojo)
- Actividad errónea (amarillo)
- No está planificado (azul)

Haz clic en un agente para ver la {% link_new adherencia intradiaria del agente | features/intraday/adherence-intraday.md | #adherencia-intradiaria-del-agente %}. Los {% link_new matches | features/intraday/adherence-matches.md %} y los {% link_new periodos de gracia | features/intraday/real-time-adherence.md | #buffer-time %} influyen en los cambios en el estado y los tipos de adherencia. Aprende más sobre los {% link_new estados y tipos de adherencia | features/intraday/real-time-adherence.md | #status %}.

{{ 3 | image: 'Tabla de adherencia del agente','100%' }}

## Adherencia intradiaria del agente

La vista de adherencia intradiaria del agente profundiza en los detalles de los incidentes de adherencia. Puedes ver, p.&nbsp;ej., cuándo alguien ha incumplido su horario. Para entender lo que un empleado ha hecho a lo largo del día, haz clic en una entrada de horario. La vista mostrará las actividades individuales con los colores configurados.

En la línea temporal puedes comparar las actividades planificadas con las actividades reales, y puedes ver los estados de fuera de adherencia resultantes. La tabla a continuación contiene una sola fila para cada período fuera de adherencia.

Para cambiar el día mostrado, puedes usar:

- el **selector de mes** en la parte superior y el **resumen diario** a la izquierda;
- las **flechas de navegación** junto a la fecha actual arriba de la tabla.

La vista diaria muestra el valor de adherencia para cada día del mes seleccionado. Arriba de la descripción diaria puedes ver distintas métricas clave para el mes seleccionado, como el valor de adherencia o la duración planificada.

{{ 4 | image: 'Detalles de adherencia intradiaria del agente','100%' }}

## Informe de adherencia (archivo CSV)

Puede ser que en ocasiones necesites analizar los datos de adherencia y cumplimiento de empleados concretos durante un período de tiempo más largo, p.&nbsp;ej., para calcular bonificaciones. El informe de adherencia es un archivo CSV que incluye datos agregados de adherencia y cumplimiento. Para descargarlo, sigue estos pasos:

1. Ve a _Intraday > Adherencia Intradiaria_{:.breadcrumbs}.
2. Selecciona al menos una unidad de planificación y/o grupo.
3. Haz clic en _Descargar informe_{:.doc-button}.  
   Se abre una ventana.
4. Selecciona un rango de fechas para el informe. Puedes seleccionar cualquier rango de fechas desde un día hasta seis meses en el pasado.
5. Haz clic en _Descargar informe_{:.doc-button}.

La tabla a continuación explica las columnas del informe:

| Columna             | Explicación                                                                     | Cálculo                                                                |
| ------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Minutes in adherence | Tiempo dedicado a actividades que corresponden a las actividades planificadas      | -- |
| Minutes out of adherence  | Tiempo dedicado a actividades que no corresponden a las actividades planificadas        | -- |                  
| Adherence in %   | Porcentaje del tiempo de trabajo dedicado a actividades que corresponden a las actividades planificadas       | Minutos en adherencia/minutos planificados * 100% |
| Minutes out of conformance   | La diferencia entre el tiempo de trabajo real y planificado             | Minutos de trabajo reales - minutos planificados |
| Conformance in % | Porcentaje del tiempo de trabajo en cumplimiento con el tiempo de trabajo planificado | Tiempo real/tiempo planificado * 100% |
| Scheduled in %  | El porcentaje de tiempo de trabajo planificado para una actividad de un cierto tipo | Tiempo planificado para el tipo de actividad relevante/tiempo total planificado * 100%              |
| Actual in %  | El porcentaje de tiempo de trabajo real invertido en una actividad de un cierto tipo | Tiempo real para el tipo de actividad relevante/tiempo total planificado * 100%              |

Cada fila de datos incluye un enlace para mostrar los datos relacionados en _Intraday > Adherencia Intradiaria_{:.breadcrumbs}.

## Preguntas frecuentes

| Pregunta                            | Respuesta                                                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ¿Por qué faltan algunos empleados o todos? | Prueba a borrar tu búsqueda. Comprueba si los empleados que estás buscando están planificados para el día de hoy en la unidad de planificación o en el grupo seleccionados.           |
| ¿Por qué no puedo seleccionar una fecha específica? | Puedes acceder a los datos históricos de adherencia del mes actual y de los seis meses anteriores (por ejemplo, si hoy es 15 de julio, puedes seleccionar fechas entre el 1 de enero y el 15 de julio). |
