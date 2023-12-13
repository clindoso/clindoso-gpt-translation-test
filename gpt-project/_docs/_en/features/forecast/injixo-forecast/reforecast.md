---
title: Reforecast
product_label:
  - advanced
  - enterprise
description: Trigger a reforecast to recalculate your forecast when required to by an unexpected event.
---

During your Intraday planning you may notice some unforeseen events in your Forecast. To react on these events, we offer the option to trigger a Reforecast.

This feature is available in injixo Advanced WFM or higher. <!-- currently not live, beta was canceled a few years ago -->

## How does the Reforecast work?

The Reforecast adapts your forecast data based on the differences between the **operational** or **strategic** {% link_new version | features/forecast/injixo-forecast/store-forecast-versions.md %} and the historical data. The adapted forecast data will be shown as manual adjustments in the graph.

## Trigger a Reforecast

The following steps are necessary to carry out a Reforecast of the Auto-Forecast:

1. Open the desired Workload.
2. Use the time navigation and switch to the daily view and click _Today_{:.doc-button-icon}.
3. Click _{{ 1 | image: "Context Menu in injixo Forecast", '100%', 'svg'}}_{:.doc-button-icon} within the Volume and AHT section.
4. Select _Start a Reforecast_{:.doc-button}.
5. Determine whether the Reforecast should be calculated based on data from the **operational** or **strategic** version. The Reforecast will be shown as manual adjustments in the graph.
6. a) If you are satisfied with the displayed Reforecast, confirm your selection with _Save_{:.doc-button}.
7. b) If you want to make manual adjustments to the forecast, confirm your selection with _Save and adjust_{:.doc-button}.

> Note
>
> Existing manual adjustments for the selected period will be overwritten.

## Displaying a Reforecast

The Reforecast is automatically displayed in the volume graph as manual adjustments. You have the possibility to revise or remove the Reforecast using the manual adjustments function. You can also save the revised auto forecast from the reforecast in a version as usual.

{{ 2 | image: 'Adjusted Forecast after applying the Reforecast'}}
