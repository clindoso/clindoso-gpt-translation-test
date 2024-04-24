---
title: Save forecast versions
description: Use forecast versions to save forecasts for comparison against actual volume for short and long-term forecasting.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
redirect_from:
  - /versions/
redirect_reason: Updated filename on 29 March 2023
---

Forecast versions allow you to save forecast values for specific periods. Use forecast versions to compare the original forecast with the current values, and to see how other factors, such as events, influence your forecasts. You can also {% link_new calculate staff requirements | features/forecast/injixo-forecast/calculate-staff-requirements.md %} based on a forecast version, or display forecast version data in {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %}.

## Save a forecast version

injixo offers two forecast versions:

- Operational: Use it for short-term forecasts to calculate staff requirements.
- Strategic: Use it for long-term forecasts to plan your organization's capacity.

To save the default Forecast data in a forecast version, proceed as follows:

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select the time frame for which you want to save the forecast version. Click on a week number to select the whole week, or click any day and drag to select a period shorter or longer than a week.
3. From the {% icon ellipsis_v %} at the top right, select _Save forecast in version_{:.doc-button}.
4. In the configuration window, select the forecast version into which you want to save the data.
   > Note
   >
   > There can only be one Operational and one Strategic forecast version for a period in a workload. Saving data for the same period in the same forecast version overwrites the existing data.

5. Click _Save_{:.doc-button}.
 
The volume and AHT graphs show the forecast version data as colored lines. The Operational version data is displayed as a purple line. The Strategic version data is displayed as a green line.