---
title: Download forecasts
toc: true
product_label:
  - advanced
  - enterprise
  - classic
description: Download forecasts as CSV files from injixo Forecast. Learn how these files are formatted.
---

In _Forecast > Workloads_{:.breadcrumbs}, you can download your forecast data as a CSV file.

You can export data for up to one year. You can download the Forecast {% link_new version | features/forecast/injixo-forecast/save-forecast-versions.md | #save-a-forecast-version %} data by itself, or together with the Operational and/or Strategic versions.

## Download a forecast

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select the time frame using the date picker. Click on a week number to select the whole week, or click any day and drag to select a period shorter or longer than a week.
3. From the {% icon ellipsis_v %} at the top right, select **Download as CSV**.
4. Select the forecast data that you want to download.<br>To select all available versions, check the **All** checkbox.
5. Click _Download as CSV_{:.doc-button}.<br>
   The downloaded forecast versions are saved in one file.

## CSV file example

The CSV file name contains the workload name and the channel. For example, the CSV file for the calls workload Orders will be named `Orders-Calls.csv`. The column headers show the forecast version. The file contains timestamps (formatted as YYYY-MM-DD) and values for each forecast, and uses the time zone and interval of the workload. The file does not include information about public holidays, events added to the workload, or any historical data.

If you select **Forecast** and **Operational**, the file will look as follows:

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
...
2020-05-17 16:30;40;180;35;175
2020-05-17 16:45;41;181;37;183
2020-05-17 17:00;40;180;35;175
2020-05-17 17:15;41;181;37;183
...
```

> The download option is only available for Smart workloads in Live mode.
>
> Switch your workload to Live mode to access the download option. See {% link_new Create workloads | features/forecast/injixo-forecast/create-workloads.md %} for details about Live mode and Test mode. Smart workloads are only available for Enterprise and Advanced WFM plans.
