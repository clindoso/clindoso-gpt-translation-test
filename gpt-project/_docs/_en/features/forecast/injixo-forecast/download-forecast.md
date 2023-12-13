---
title: Download forecast data as CSV
toc: false
product_label:
  - advanced
  - enterprise
  - classic
description: Download forecasts as CSV files from injixo Forecast. Learn how these files are formatted.
---

In this article, you will learn:

- how you can export forecasts and versions of a workload to a CSV file.
- how the export is formatted.

Values can be exported for up to one year. The time zone and interval correspond with the workload. You can download the Auto-Forecast data by itself or with the Operational and/or Strategic Versions.

## How to download forecasts

1. Open a **Workload**.
2. Select the download range using the **time navigation**.
3. Click the context menu _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} (to the right of the _Use Forecast_ button).
4. Select **Download as CSV**.
5. Check the time frame again and **select the desired forecasts**. Choose from the Auto-Forecast, the Operational version, and the Strategic version. The forecast and versions will be saved in a single file.
6. Confirm your selection with _Start Download_{:.doc-button}.

## CSV file example

The file contains the workload name and the channel. A download for the call workload _Orders_ would result in a file named `Orders-Calls.csv`. The column headers show the forecast version. The file contains time stamps (formatted as YYYY-MM-DD) and the values per value type for each forecast, but does not include information about holidays or events added to the workload, or any historical data.

If you select the Auto-Forecast and the Operational version, the file will look like this:

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
...
2020-05-17 16:30;40;180;35;175
2020-05-17 16:45;41;181;37;183
2020-05-17 17:00;40;180;35;175
2020-05-17 17:15;41;181;37;183
...
```

> The download option is available for _Smart_ workloads in _Live_ mode only.
>
> Switch the workload plan to _Live_ in order to access the download option, see {% link_new Managing Workloads | features/forecast/injixo-forecast/manage-workloads.md %} for details about _Live/Test_ plans.
