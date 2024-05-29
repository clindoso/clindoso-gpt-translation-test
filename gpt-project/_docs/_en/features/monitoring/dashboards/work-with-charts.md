---
title: Work with charts
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to work with charts in a dashboard.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

In _Analyze > Dashboards_{:.breadcrumbs}, you can work with charts and time series to analyse your data. Start by selecting a dashboard from the drop-down menu at the top.

New to Dashboards? Learn {% link_new the basics | features/monitoring/dashboards/manage-dashboards.md %} first.

## Navigate charts

The following actions are available in **Dashboards**:

- To change the date range for which you display data, select a date range from the date picker in the upper right of each chart.
- To zoom in on a chart, click and drag to select your area of interest.
- To zoom out, click _Reset zoom_{:.doc-button}.
- To switch to the table view, click the Show table icon {% icon table-list | icon-only %} at the top right of a chart.
- To switch back to chart view, click the Show chart icon {% icon chart-view | icon-only %}.
- To copy data to the clipboard, click the Copy icon {% icon clone | icon-only %}.

> Note
>
> The date and time information is localized according to your injixo language settings. This could cause problems if you copy data from injixo into an Excel or Google Sheets document that uses another language.

## Work with time series

Time series are sequences of data points recorded over regular time intervals. The following subsections explain how you can use time series in **Dashboards** to use, customize and analyze your data and make informed decisions.

### Highlight time series

To temporarily highlight a specific time series in chart view, hover over the name of the time series in the legend. All other time series will fade into the background.

### Show and hide time series

Hide and show other time series by clicking the {% icon eye %} or the {% icon eye_slash %} next to the name in the legend.

### Customize time series

1. Go to _Analyze > Dashboards_{:.breadcrumbs}.
2. From the {% icon ellipsis_v %}, click **Edit**.
3. Hover over the time series name in the legend and click the Edit icon {% icon pencil | icon-only %}.
4. In the **Customize graph** window, edit the time series properties:
   - Edit the **Name** shown in the legend.
   - Choose between **Step** or **Histogram** (bar chart) in the **Type** drop-down menu.
   - Select another predefined **Color**.
   - Select how data is aggregated in the chart. Choose **By interval** (available for time ranges up to 8 days) to show interval values, or **By day** to show daily values.
   - Select whether to show the y-axis values on the **Left (default)** or the **Right**.
5. Click _Save_{:.doc-button}.<br>Click _Close Edit mode_{:.doc-button} to return to the view mode.

### Delete time series

1. Go to _Analyze > Dashboards_{:.breadcrumbs}.
2. From the {% icon ellipsis_v %}, click **Edit**.
3. Hover over the time series name in the legend and click the Edit icon {% icon pencil | icon-only %}.
4. In the **Customize graph** window, click _Delete_{:.doc-button}.
5. Click _Save_{:.doc-button}.<br>Click _Close Edit mode_{:.doc-button} to return to the view mode.
