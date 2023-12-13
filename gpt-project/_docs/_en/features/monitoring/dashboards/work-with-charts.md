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

New to Dashboards? Learn {% link_new the basics | features/monitoring/dashboards/dashboards-overview.md %} first.

In the Dashboards feature, you can work with charts and time series after you have selected one of your dashboards.

## Change the date range

Select a fixed **date range** to display data in the upper right corner of each chart, or additionally activate **Use Rolling Dates**. In this mode, the start date is shifted by one day every day.

## Zoom in and out

View charts in more detail using the zoom function. For this, simply mark the area of interest in a chart using the mouse. Click _Reset zoom_{:.doc-button} to see the entire time frame again.

## Switch to the table view

As an alternative to the graph visualization, the table view displays timestamps and values for each chart. Switch between graph and table view with by clicking _![Table view](/assets/img/common/dashboards/table.png)_{:.doc-button-icon} above a chart.

### Copy data to the clipboard

The table view offers a copy function. Click _![Copy a table](/assets/img/common/dashboards/copy.png)_{:.doc-button-icon}, next paste the data into your spreadsheet program using copy & paste. The first column contains date and time, you need to use formulas in your spreadsheet to separate them.

Note: The date and time information is localized according to your injixo language settings, which could be problematic when copying the data from your tenant into your Excel or Google Sheets version using another language.

## Highlight time series

To temporarily highlight a specific time series, hover over the **name of the time series** in the legend. All other time series will fade into the background.

## Show and hide time series

Hide other time series by clicking _![Show and hide graphs](/assets/img/common/dashboards/view.png)_{:.doc-button-icon} next to the name in the legend.

## Customize time series

1. Click _![Context menu](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} next to the name of the currently selected dashboard.
2. Click **Edit** to access the edit mode for the dashboard.
3. Hover over the **time series name** in the legend, next click _![pencil icon](/assets/img/common/item-edit.gif)_{:.doc-button-icon}.
4. In the _Customize graph_ dialog window, change the time series properties. You can:
   - edit the **Name** shown in the legend.
   - change the diagram **Type**. Choose from **Step** or **Histogram** (bar chart).
   - select another predefined **Color**.
   - change how data is aggregated in the chart. Choose from **By interval** (available for time ranges up to 8 days) to show interval values or **By day** to show the values for the day.
   - change where the y-axis is shown. Choose from **Left (default)** or **Right**.
5. Click _Save_{:.doc-button}.
6. Click _Close Edit mode_{:.doc-button} to return to the view mode.

   {{ 3 | image: "Customize a Graph", '40%' }}

## Delete time series

1. Click _![Context menu](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} next to the name of the currently selected dashboard.
2. Click **Edit** to access the edit mode for the dashboard.
3. Hover over the **time series name** in the legend, next click _![pencil icon](/assets/img/common/item-edit.gif)_{:.doc-button-icon}.
4. In the _Customize graph_ dialog window, click _Delete_{:.doc-button} to delete the selected time series. This will close the editing dialog.
5. Click _Save_{:.doc-button}.
6. Click _Close Edit mode_{:.doc-button} to return to the view mode.
