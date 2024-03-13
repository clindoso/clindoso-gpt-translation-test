---
title: What is injixo Forecast?
redirect_from:
  - /forecast_overview/
  - /general-functionality/
redirect_reason: redirect for intercom forecast tour, 2nd link, renamed article in june 2021
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Use injixo Forecast to automatically calculate a forecast for contact volume and AHT.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manual-adjustments.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/store-forecast-versions.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/download-forecast.md
---

injixo Forecast combines your historical data with algorithms to generate high-quality forecasts. The algorithms recognize trends, patterns, and fluctuations included in your data. injixo Forecast uses many types of algorithms, such as ARIMA, Holt-Winters, exponential smoothing, regression, or gradient boosting. 

injixo Forecast automatically selects the algorithm best suited to your data. The forecast is generated for 365 days and can be displayed in daily, weekly, monthly, and yearly views.

injixo Essential WFM uses a basic algorithm that uses simple average values in the historical data to recognize a long-term linear trend and weekly patterns.

## Generate a forecast

Check our quick start guide to learn how to {% link_new generate a forecast | getting-started/calculate-a-forecast.md %}. Each new data import updates the generated forecast. injixo Essential WFM only generates a new forecast once a week.

Note: If your generated forecast only shows repeated weekly patterns, it still may be the optimal forecast. In this case, the algorithm captures short-term patterns (for non-repeating fluctuations) and rates long-term patterns as irrelevant. Fluctuations in the historical data are not always patterns.

## Data requirements

injixo Forecast requires that you import offered contacts, average handling time (AHT), and handled contacts.

Basic workloads in injixo Classic require at least two weeks of historical data. Smart workloads can generate a forecast based on just one day of historical data. If you have two or more years worth of data, Smart workloads consider monthly and annual fluctuations, such as seasonal business.

Which kind of workloads are available to you depends on your WFM plan (Classic, Essential, Advanced or Enterprise WFM).

## How to deal with low data quality

To generate an accurate forecast, historical data must be both complete (enough data with as few gaps as possible) and clean (free of irrelevant patterns). For example, incorrectly marked {% link_new events or holidays | features/forecast/injixo-forecast/events-and-holidays.md %} will impact forecast quality.

Historical data may include prolonged outages, or it may miss data for a particular timeframe. The closer that missing data is to the current day, the less the forecast quality is affected. 

Here are some tips on managing low data quality depending on how long the period with poor or missing data is:

| Timeframe with poor quality data     | Tip                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| A few days | Use {% link_new events | features/forecast/injixo-forecast/events-and-holidays.md %} to mark the affected days as an outage and exclude them from the calculation.                                  |
| A couple of weeks    | Upload additional data without gaps or irrelevant patterns. |
| Several weeks or months  | Remove the data that predates the gap. Import only the data from after the gap.                            |

Note: If you cannot upload additional data or you do not have enough data after a gap, the Smart Forecast algorithms will automatically try to minimize the negative impact of missing data.

> Check and clean up data before you import it
>
> You cannot remove historical data. Contact your Customer Success team if needed.

## Forecast low volumes

injixo Forecast can generate forecasts for low and high contact volumes. When generating a forecast based on data from low contact volumes, injixo may not recognize the daily patterns. While rare, this may result in no forecast being generated for particular days. For single days, adjust the forecast manually. In a recurring situation, you can:

- Add multiple queues to the workload (resulting in higher volumes).
- Use another approach to generate staff requirements for scheduling, e.g. {% link_new generate constant staff requirements | features/forecast/requirement-scripts/requirement-constant.md %}.
