---
title: Script para multiactividades
description: Calcula requisitos de personal para multiactividades.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

Usa el script para multiactividades para calcular requisitos de personal para tus multiactividades. El cálculo se basa en Erlang-C y usa un nivel de servicio.

## Prerrequisitos

- Crea al menos una {% link_new multiactividad | features/administration/activity-types-and-properties.md | #subactividades %} y asígnala a tu unidad de planificación
- Crea una {% link_new carga de trabajo | features/forecast/injixo-forecast/manage-workloads.md | #crear-cargas-de-trabajo %} para cada subactividad de la multiactividad.

## Exporta la previsión de todas las cargas de trabajo de las subactividades

Antes de ejecutar el script para multiactividades, exporta las previsiones de las cargas de trabajo de todas las subactividades:

1. En _Forecast > Workloads_{:.breadcrumbs} selecciona la carga de trabajo que creaste para una subactividad.
2. Selecciona el periodo de tiempo en el selector de fechas. Haz clic en el número de la semana para seleccionar una semana completa, o haz clic en un día cualquiera y arrastra para seleccionar un periodo más corto o más largo.
3. En el {% icon ellipsis_v %} arriba a la derecha, selecciona **Usar previsión**.
4. En la ventana que se abre, selecciona la previsión que quieres usar.
5. Haz clic en _Usar previsión_{:.doc-button}.
6. Haz clic en _Cerrar_{:.doc-button}.
7. Repite los pasos 1-6 para todas las cargas de trabajo creadas para tus subactividades.

injixo guarda los datos necesarios para el cálculo de los requisitos de personal en colas en _WFM > Gestión > Previsión > Datos en cola_{:.breadcrumbs}. Las colas tienen el nombre de la carga de trabajo correspondiente precedido por un asterisco, p.&nbsp;ej. *nombreDeTuCargaDeTrabajo.

## Configura el script

1. Ve a _Forecast > Scripts de requisito_{:.breadcrumbs}.
2. En el recuadro **Llamadas entrantes - Multi-actividad**, haz clic en _Abrir_{:.doc-button}.  
3. En la ventana de configuración del script, configura los siguientes ajustes:
   - En la sección **Fecha**:
     - **Fecha de inicio**:  introduce la fecha de inicio para el cálculo de los requisitos de personal.
     - **Número de días**: introduce el número de días tras la fecha de inicio para los que quieres calcular requisitos de personal.
   - En la sección **Parámetros de la unidad de planificación**:
     - **Unidad de planificación** y **Actividad múltiple**:<br>
     la ventana de configuración del script se actualiza y muestra los parámetros de cálculo para las subactividades relevantes.
   - En la sección **Subactividad** puedes configurar distintos parámetros de cálculo para cada subactividad. Comienza por los parámetros en la sección **Parámetros del archivo de datos en cola**:
    - **Calculation Method**: selecciona **Erlang-C**, **Linear** o **Chat**.<br>la ventana de configuración del script se actualiza y muestra los parámetros configurables relevantes. Consulta la [tabla a continuación](#parámetros-de-cálculo-en-la-sección-erlang-c) para ver qué parámetros puedes configurar para cada método de cálculo.
    - **Archivo de dato en cola**: selecciona la cola que contiene los datos que quieres usar para el cáculo.
    - **Operaciones**: selecciona el tipo de valor del volumen de contacto, p.&nbsp;ej. llamadas entrantes.
    - **Duración media de la operación**: si tienes una previsión de tiempo medio de operación (TMO) para tus cargas de trabajo, selecciona el tipo de valor correspondiente. En caso contrario, selecciona **[Ninguno]**.
    - **Versión**: selecciona **Auto-Forecast**. En injixo Enterprise on-premise, puedes seleccionar otra versión.

## Parámetros de cálculo en la sección Erlang C

| Parámetro                         | Descripción                                                                                                            | Configurable en Erlang-C | Configurable en Linear | Configurable en Chat |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |--------  | -------- |
| Nivel de servicio (%)             | Porcentaje de contactos que deben ser atendidos durante el tiempo configurado en el parámetro **Nivel de servicio (segundos)**.                                                                                                                                                                    | Sí | No | Sí |
| Nivel de servicio (segundos)            | Tiempo en el que el porcentaje de contactos especificado en el parámetro objetivo **Nivel de servicio (%)** debe ser atendido.                                                                                                                                                                                            | Sí | No | Sí |
| Suplemento (%)                         | El porcentaje en el que debes aumentar los requisitos de personal calculados. Aprende cómo [configurar este parámetro](#configurar-el-parámetro-suplemento--para-tener-en-cuenta-la-reducción) para tener en cuenta la reducción. | Sí | Sí | Sí |
| Ocupación mínima            | Introduce un valor para sobrescribir valores inferiores de requisitos de personal.                                                                                                                                                                                                                                                     | Sí | Sí | Sí |
| Ocupación máxima            | Introduce un valor para sobrescribir valores superiores de requisitos de personal.                              | Sí | Sí | Sí |
| Duración media constante de la operación | Si seleccionaste un tipo en el parámetro **Duración media de la operación** en la sección **Parámetros del archivo de datos en cola**, mantén aquí el valor predefinido.<br> Si seleccionaste **[Ninguno]** en el parámetro **Duración media de la operación**, introduce un valor en segundos.                                 | Sí | Sí | Sí |
| Sec. (%)                  | Porcentaje del TMO que los empleados ocupan con tareas que no pueden llevar a cabo en paralelo, como trabajo tras llamada.                                                                                                                                                                                                                                                                                   | No | No | Sí |
| Sesiones máx.                          | Número máximo de sesiones de chats paralelas que un empleado puede atender a la vez.                                                                                                                                             | No | No | Sí |

### Configurar el parámetro Suplemento (%) para tener en cuenta la reducción

Para configurar el parámetro **Suplemento (%)** para que tenga en cuenta la reducción, usa la siguiente fórmula, en la que s% es tu tasa de reducción: 1/(1-s%)-1. El resultado expresado como porcentaje es el valor que debes introducir en el parámetro **Suplemento (%)**. Por ejemplo, para considerar una reducción del 20%, el cálculo es 1/(1-0.2)-1, que resulta en 25%.

## Ejecutar el script

- Para comenzar el cálculo, haz clic en _Aceptar_{:.doc-button}.<br>Una ventana se abre y muestra los parámetros seleccionados y los resultados del script. <br>

## Ver los resultados del cálculo

Puedes ver los requisitos de personal actualizados para la unidad de planificación y la multiactividad en {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %} o en la ventana de parámetros en el {% link_new Centro de planificación | features/scheduling/edit-or-delete-staff-requirements.md %} o en {% link_new Planificar | features/scheduling/schedules/schedules-activity-coverage.md %}.
