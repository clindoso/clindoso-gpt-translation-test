---
title: Download forecast data as CSV
toc: false
product_label:
  - advanced
  - enterprise
  - classic
description: Download forecasts as CSV files from injixo Forecast. Learn how these files are formatted.
---

In _Forecast > Workloads_{:.breadcrumbs}, you can download your forecast data as a CSV file.

Values can be exported for up to one year. The time zone and interval correspond with those of the workload. You can download the Forecast version data by itself or together with the Operational and/or Strategic versions.

## Download a forecast

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select the time frame using the date picker.
3. From the three-dots menu _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} at the top right, select **Download as CSV**.
4. Select the forecast data that you want to download.  
5. Click _Download as CSV_{:.doc-button}.<br>
   The downloaded forecast versions will be saved in one file.

## CSV file example

The file contains the workload name and the channel. A download for the call workload Orders would result in a file named `Orders-Calls.csv`. The column headers show the forecast version. The file contains timestamps (formatted as YYYY-MM-DD) and the values per value type for each forecast, but does not include information about public holidays or events added to the workload, or any historical data.

If you select the Forecast and the Operational version, the file will look like the following example:

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
...
2020-05-17 16:30;40;180;35;175
2020-05-17 16:45;41;181;37;183
2020-05-17 17:00;40;180;35;175
2020-05-17 17:15;41;181;37;183
...
```

> The download option is available for Smart workloads in Live mode only.
>
> Switch the workload to Live mode to access the download option. See {% link_new Create workloads | features/forecast/injixo-forecast/manage-workloads.md %} for details about Live mode and Test mode.
