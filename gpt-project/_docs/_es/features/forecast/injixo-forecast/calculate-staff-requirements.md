---
title: Calcular requisitos de personal
redirect_from:
  - es/staff-requirement/
  - /es/staff-requirement/
redirect_reason: Updated filename on 04 March 2024
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Calcula requisitos de personal para llamadas, chats, correos electrónicos y más.
related_articles:
  - overwrite_title: Script para multiactividad
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
  - overwrite_title: Script para llamadas salientes
    filepath: features/forecast/requirement-scripts/requirement-outbound.md
  - overwrite_title: Script para requisitos constantes
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: Add title for untranslated source.
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
---

Después de haber generado una previsión puedes calcular requisitos de personal. Puedes escoger entre distintos scripts de requisitos y métodos de cálculo disponibles en injixo. También puedes escribir requisitos de personal constantes sin una previsión, si fuera necesario.

¿Estás empezando con injixo Forecast? Consulta primero {% link_new la información básica | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Métodos de cálculo y scripts de requisitos

injixo ofrece distintos métodos de cálculo y scripts de requisitos.
Descubre qué {% link_new script de requisitos o método de cálculo es el más adecuado | best-practices/requirement-scripts.md %} para tu escenario de uso.<br>
Aprende cómo configurar los [métodos de cálculo](#configurar-los-métodos-de-cálculo) en la siguiente sección:<br>
Para aprender cómo configurar los scripts de requisitos, haz clic en los siguientes enlaces:

- {% link_new Script para multiactividad | features/forecast/requirement-scripts/requirement-multiactivity.md %}
- {% link_new Script para llamadas salientes | features/forecast/requirement-scripts/requirement-outbound.md %}
- {% link_new Script para requisitos constantes | features/forecast/requirement-scripts/requirement-constant.md %}

## Configurar los métodos de cálculo

Los métodos de cálculo calculan requisitos de personal con base en nuevas importaciones de datos, modificaciones a los parámetros de cálculo o {% link_new ajustes manuales | features/forecast/injixo-forecast/manual-adjustments.md %}.
Puedes cambiar de método de cálculo en cualquier momento.

1. En _Forecast > Workloads_{:.breadcrumbs}, selecciona una carga de trabajo.
2. En la sección **Requisitos de personal**, haz clic en _Editar requisitos de personal_{:.doc-button}.
3. En el menú desplegable **Método de cálculo**, selecciona una opción:
   - **Erlang-C**
   - **Chat**
   - **Linear**
4. En la sección **Parámetros de cálculo**, configura los [parámetros de cálculo](#parámetros-de-cálculo).
5. En la sección **Unidad de planificación y actividad asociadas**, selecciona la unidad de planificación y la actividad para las que quieres usar los requisitos de personal.  
   Aprende más sobre cómo [usar los requisitos de personal para la planificación](#usar-requisitos-de-personal-para-la-planificación).
6. Haz clic en _Guardar_{:.doc-button}.

El gráfico en la sección **Requisitos de personal** muestra los requisitos de personal calculados.<br> Bajo el gráfico puedes ver los valores configurados para los parámetros y el total de horas persona necesarias para el periodo seleccionado.<br> Pasa el ratón sobre el gráfico para ver información detallada para cada intervalo sobre volumen, TMO, requisitos de personal, cualquier ajuste manual y eventos añadidos.

### Parámetros de cálculo

La siguiente tabla incluye los parámetros que puedes configurar para cada método de cálculo:

| Parámetro                         | Descripción                                                                                                                                                                                                                                                                                                           | Configurable en Erlang-C | Configurable en Chat | Configurable en Linear |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |--------  | -------- |
| Objetivo de nivel de servicio              | Porcentaje de llamadas o chats entrantes que deben ser atendidos dentro del tiempo especificado en el parámetro objetivo de tiempo de respuesta.                                                                                                                                                                                                                                                                          | Sí | Sí | No |
| Objetivo de tiempo de respuesta                | Tiempo en el que el porcentaje de llamadas o chats especificado en el parámetro objetivo de nivel de servicio debe ser atendido.                                                                                                                                                                                            | Sí | Sí | No |
| Reducción                         | El porcentaje de tiempo remunerado durante el que los empleados no pueden trabajar, sea por p.&nbsp;ej. descansos para ir al baño, retrasos, bajas por enfermedad no planificadas, o problemas técnicos. | Sí | Sí | Sí |
| Personal mínimo requerido            | Introduce un valor para sobrescribir intervalos con valores inferiores de requisitos de personal.                                                                                                                                                                                                                                                     | Sí | Sí | Sí |
| Personal máximo requerido            | Introduce un valor para sobrescribir intervalos con valores superiores de requisitos de personal.                              | Sí | Sí | Sí |
| Tiempo medio de operación (TMO) fijo | Introduce un valor para sobrescribir el TMO calculado en la previsión.<br>Marca la casilla **Aplicar el TMO fijo solo cuando no haya valores de TMO disponibles** para usar el valor de TMO fijo solo en periodos sin datos de TMO. Por defecto, el cálculo de los requisitos de personal usa los valores de TMO de la previsión.                                  | Sí | Sí | Sí |
| Sesiones máximas                  | Número máximo de sesiones de chats paralelas que un empleado puede atender al mismo tiempo.                                                                                                                                                                                                                                                                                   | No | Sí | No |
| Sobrecarga                          | Porcentaje del TMO que los empleados deben dedicar a tareas que no pueden hacer en paralelo, como añadir notas post llamada al sistema CRM. Este parámetro no se toma en consideración si introduces 1 en el campo **Sesiones máximas**.                                                                                                                                             | No | Sí | No |

## Usar requisitos de personal para la planificación

Para crear una planificación con base en requisitos de personal, primero tienes que guardarlos. Para guardar requisitos de personal, sigue los pasos a continuación.

Solo puedes usar los requisitos de personal calculados para las versiones de la previsión o las previsiones importadas que has guardado para el periodo seleccionado.<br>
Aprende más sobre {% link_new versiones de la previsión | features/forecast/injixo-forecast/store-forecast-versions.md %} o sobre cómo {% link_new importar una previsión | features/forecast/injixo-forecast/import-forecast.md %}.

1. En _Forecast > Workloads_{:.breadcrumbs}, selecciona una carga de trabajo.
2. Selecciona el periodo para el que quieres usar los requisitos de personal.
3. En la sección **Requisitos de personal**, selecciona una versión de la previsión del menú desplegable a la izquierda.
4. Haz clic en _Guardar requisitos de personal_{:.doc-button}.
5. En la ventana **Guardar requisitos de personal**, haz clic en _Guardar_{:.doc-button}.

injixo guarda los requisitos de personal para la unidad de planificación y la actividad que seleccionaste cuando configuraste el método de cálculo.

> Atención
>
> Puedes usar los requisitos de personal para otra unidad de planificación o actividad. <br> Para ello, repite el procedimiento para [configurar el método de cálculo](#configurar-los-métodos-de-cálculo) y selecciona una unidad de planificación o actividad distintas. A continuación, sigue el procedimiento para [usar los requisitos de personal para la planificación](#usar-requisitos-de-personal-para-la-planificación).
