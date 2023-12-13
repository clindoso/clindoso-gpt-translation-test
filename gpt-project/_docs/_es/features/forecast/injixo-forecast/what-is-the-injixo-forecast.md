---
title: ¿Qué es injixo Forecast?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Usa injixo Forecast para calcular automáticamente una previsión de volumen de contacto y TMO.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/store-forecast-versions.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/download-forecast.md
---

injixo Forecast combina tus datos históricos con algoritmos para generar previsiones de alta calidad. Los algoritmos reconocen tendencias, patrones y fluctuaciones en tus datos. injixo Forecast utiliza distintos tipos de algoritmos, como ARIMA, Holt-Winters, suavizamiento exponencial, regresión, o potenciación de gradiente. 

injixo Forecast selecciona automáticamente el algoritmo que mejor se ajusta a tus datos. injixo genera una previsión para 365 días que se puede consultar en vistas diarias, semanales, mensuales y anuales.

injixo Essential WFM usa un algoritmo básico que toma valores medios de los datos históricos para reconocer una tendencia lineal a largo plazo y patrones semanales.

## Generar una previsión

Consulta nuestra guía rápida para aprender a {% link_new generar una previsión | getting-started/calculate-a-forecast.md %}. Cada nueva importación de datos actualiza la previsión generada. injixo Essential WFM solo genera una nueva previsión una vez a la semana.

Si tu previsión generada solo muestra patrones semanales repetidos, ten en cuenta que esta puede ser la previsión óptima. En este caso, el algoritmo captura patrones a corto plazo (para fluctuaciones no repetitivas) y considera los patrones a largo plazo irrelevantes. Las fluctuaciones en los datos históricos no siempre son patrones.

## Requisitos de datos

injixo Forecast requiere que importes los contactos ofrecidos, el tiempo medio de operación (TMO) y los contactos atendidos.

Las cargas de trabajo Basic en injixo Classic requieren un mínimo de dos semanas de datos históricos. Las cargas de trabajo Smart pueden generar una previsión basada en datos históricos de un solo día. Si tienes datos para dos años o más, las cargas de trabajo Smart tienen en cuenta las fluctuaciones mensuales y anuales, como negocios estacionales.

El tipo de cargas de trabajo disponibles para ti depende de tu plan de WFM (Classic, Essential, Advanced o Enterprise WFM).

## Cómo lidiar con datos de baja calidad

Para generar una previsión precisa, los datos históricos deben estar completos (suficientes datos con la menor cantidad de brechas posible) y limpios (libres de patrones irrelevantes). Por ejemplo, los {% link_new eventos o festivos | features/forecast/injixo-forecast/events-and-holidays.md %} marcados incorrectamente afectarán a la calidad de la previsión.

Puede ocurrir que los datos históricos incluyan interrupciones prolongadas, o que falten datos de un periodo de tiempo específico. La calidad de la previsión se ve menos afectada cuanto más reciente sea la fecha cuyos datos faltan. 

Aquí ofrecemos algunos consejos para trabajar con datos de baja calidad, dependiendo de cuán largo sea el periodo con datos deficientes o faltantes:

| Periodo con datos de baja calidad     | Consejo                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Algunos días | Usa {% link_new eventos | features/forecast/injixo-forecast/events-and-holidays.md %} para marcar los días afectados como una interrupción y excluirlos del cálculo.                                  |
| Un par de semanas    | Sube datos adicionales sin brechas o patrones irrelevantes. |
| Varias semanas o meses  | Elimina los datos anteriores a la brecha. Importa solamente los datos posteriores a la brecha.                            |

Si no puedes subir datos adicionales o no tienes suficientes datos posteriores a una brecha, los algoritmos Smart automáticamente intentarán minimizar el impacto negativo de la falta de datos. 

> Verifica y limpia los datos antes de importarlos.
>
> No puedes eliminar datos históricos. En caso necesario, contacta con tu equipo de Customer Success.

## Previsión de volúmenes bajos

injixo Forecast puede generar previsiones para volúmenes de contacto bajos y altos. Cuando generas una previsión partiendo de volúmenes de contacto bajos, puede ser que injixo no reconozca los patrones diarios. Si bien es poco común, esto puede causar que no se genere ninguna previsión para días particulares. Puedes ajustar manualmente la previsión para días concretos. En una situación recurrente, puedes:

- añadir múltiples colas a la carga de trabajo (lo que resultará en volúmenes más altos);
- utilizar otro enfoque para generar los requisitos de personal para la programación, como {% link_new generar requisitos de personal constantes | features/forecast/requirement-scripts/requirement-constant.md %}.
