---
title: Import forecasts
description: Import a forecast from an external source into injixo Forecast.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

You can import external forecasts into injixo that have been generated in another application or by your own clients.

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first.

## Create at least one queue in your injixo instance

To {% link_new create a workload | features/forecast/injixo-forecast/manage-workloads.md | #create-workloads %} in which you can [import a forecast](#import-a-forecast), you need to add a queue to a workload. Queues are created when historical contact data is imported into injixo by an integration.

You can import a forecast into an existing workload, or add any of your queues to a new workload.

If you do not have an integration for historical data, you still need to import at least one data point to create a queue:

1. {% link_new Create a CSV integration | features/acd-integration/cloud/add-csv-integration.md | #configure-a-new-csv-integration %}
   - In the **CSV schema configuration** section, select **Contact data**.
   - Skip the Cloud Link installation step.
2. Create a CSV file for contact data with at least one line for a single interval, e.g.:
   ```
   Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
   ForecastImportQueue;22/02/2022;02:02;2;2;2
   ```
3. {% link_new Manually upload the file | features/acd-integration/cloud/add-csv-integration.md | #manual-file-import %}.  
   The queue is created after import.
   Use this queue to import forecasts into all your workloads.

## Import requirements

The time zone and interval length (15, 30, or 60 minutes) must correspond with the queue(s) in the workload.

| Requirement                          | Details                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Timestamp format                     | _YYYY-MM-DD HH:MM_                                                                                                                 |
| Volume data                          | Whole numbers (integers)                                                                                                           |
| AHT data                             | Whole numbers (integers) or decimal values (with point)                                                                            |
| Header line                          | `Timestamp;Offered;AHT` (standard format)<br>`Timestamp;Offered_customtext;AHT_customtext` (custom text with mandatory underscore) |
| Separator characters (auto-detected) | Semicolon or comma                                                                                                                 |
| Maximum file size                    | 20 MB<br>Create files with 20,000 lines or less (recommended).                                                                     |

## Create an import template

By {% link_new downloading a forecast (or version) | features/forecast/injixo-forecast/download-forecast.md %}, you can create a template for your own import file. The forecast only reads the **Timestamp**, **Offered**, and **AHT** columns. Other columns, such as `Offered_operational;AHT_operational` in the example below, are ignored.

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
2020-05-17 16:30;40;180;50;170
```

## Gaps handling in import data

There can be intervals with no data in your import files. The resulting graph will only show values that are imported as zero (0). Empty lines or values will not be imported.

If there is no data for one or more intervals, you can do the following:

- Leave volume and AHT blank:

  ```
  Timestamp;Offered;AHT
  2020-05-17 15:00;30;210
  2020-05-17 15:15;;
  2020-05-17 15:30;40;180
  ```

- Import columns filled with zeros:

  ```
  Timestamp;Offered;AHT
  2020-05-17 15:00;30;210
  2020-05-17 15:15;0;0
  2020-05-17 15:30;40;180
  ```

- Leave out the entire line:

  ```
  Timestamp;Offered;AHT
  2020-05-17 15:00;30;210
  2020-05-17 15:30;40;180
  ```

## Import a forecast

1. Go to _Forecast_{:.menu-item}.
2. From the drop-down menu on top, select the **Workload** in which you want to import the external forecast.
3. Click _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon}.
4. Select **Import Forecast Data**.
5. Click **Choose File** and select the CSV file you want to import.
6. Click _Start Import_{:.doc-button}.
   The page will update and display whether the import was successful or not.
7. Click _Done_{:.doc-button}.
   When you refresh the screen, the chart will display a new graph for the import period.
   To hide the imported forecast in the graph, click the {% icon eye %} in the legend next to **Import**.

{{ 2 | image: "Imported forecast", '90%' }}
