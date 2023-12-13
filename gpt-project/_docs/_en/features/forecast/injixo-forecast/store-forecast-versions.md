---
title: Store forecast versions
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
    filepath: features/forecast/injixo-forecast/manage-workloads.md
redirect_from:
  - /versions/
redirect_reason: Updated filename on 29 March 2023
---

In your workloads, forecast versions allow you to store forecast values for specific time periods. With forecast versions, you can compare the original forecast (Auto-Forecast) with the actual numbers or how other factors, such as events, would influence your forecasts.

## Two forecast versions

Workloads display forecast version data as a colored line in all views (daily, weekly, monthly, and yearly) in the **Volume and AHT** section (if forecast version data has been stored for the selected period).

- Operational (purple): For short-term forecasts for scheduling to calculate staff requirements
- Strategic (green): For long-term forecasts that you can use for capacity planning

{{ 1 | image: 'Offered and AHT Forecast with operational forecast version', '80%' }}

Tip: To hide or show a graph, click the {% icon eye %} in the legend.

## <a name="store-the-auto-forecast-in-a-forecast-version"> Store data in a forecast version

To store the actual Auto-Forecast data in a forecast version, proceed as follows:

1. Go to _Forecast_{:.menu-item}.
2. Select a **workload**.
3. Select a **time period** using the time navigation on top, for which you want to store the forecast version.
4. In the **Volume and AHT** section, click {% icon ellipsis_v %}.
5. In the context menu, click **Store forecast in version**.
   In the dialog window, verify the previously selected period.

   > There can only be one operational and one strategic forecast version for a period in a workload.
   >
   > If you store the same time period again, forecast version data will be overwritten.

6. Select **Operational** or **Strategic**.
7. Click _Save_{:.doc-button}.

## Calculate staff requirements with forecast version data

You can {% link_new calculate staff requirements | features/forecast/injixo-forecast/staff-requirement.md %} based on the Auto-Forecast or a forecast version, for which data has been stored. Forecast version data is also transferred to the Auto-Forecast version in WFM.

For an integrated calculation method, e.g. Erlang-C, proceed as follows in the same workload:

1. Double-check the **time period** in the time navigation on top.
2. In the **Staff Requirements** section, select a stored forecast version from the drop-down menu.
3. To store the staff requirements for scheduling, click _Use Requirements_{:.doc-button}.
4. To save staff requirements for the selected period in the planning unit and activity configured in your workload, click _Save_{:.doc-button}.

For an alternative calculation method, proceed as follows in the same workload:

1. Double-check the **time period** in the time navigation on top.
2. In the **Volume and AHT** section, click _Use Forecast_{:.doc-button}.
3. In the **Prepare Forecast for staff requirement calculation** window, select a forecast version.
4. To transfer forecast version data into WFM, click _Use this Forecast_{:.doc-button}.
To run scripts for {% link_new alternative calculation methods | features/forecast/injixo-forecast/staff-requirement.md | #additional-calculation-methods %} based on forecast version data, select the following values for the Queue and Version parameters:
   - Queue parameter: The queue that has the same name as the workload starting with an asterisk (\*)
   - Version parameter: The Auto-Forecast version
