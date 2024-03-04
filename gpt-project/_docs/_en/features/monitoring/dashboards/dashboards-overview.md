---
title: Manage dashboards
permalink: /dashboards-overview/
promote-service: team-leader-training
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Use dashboards to analyze your contact volume and staffing level data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/work-with-charts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

In _Analyze > Dashboards_{:.breadcrumbs} you can create and display dashboards with up to four different charts. Each chart can display graphs for multiple time series and date ranges. If you do not have a dashboard yet, the page shows the edit mode, and you can [create a dashboard](#create-dashboards).

- To display an existing dashboard, select a dashboard from the drop-down menu, or type in the field to filter.  
- To display the values for a specific interval, hover over a graph in the dashboard.
- To switch to full-screen mode, click the {% icon maximize %} at the top right.

You can also {% link_new switch between graph and table view | features/monitoring/dashboards/work-with-charts.md | #navigate-charts %} with the Show table icon {% icon table-list | icon-only %} and Show chart icon {% icon chart-view | icon-only %} at the top right of the view.

## Create dashboards

1. Go to _Analyze > Dashboards_{:.breadcrumbs}.
2. From the {% icon ellipsis_v %} on the right, select **Create New Dashboard**.
3. Configure the following fields:
  - **Name**: Unique name for your dashboard.
  - **Layout**: Select the number and layout of your charts.
  - **Untitled Chart**: Name for each chart. The names do not have to be unique.
4. Select a **date range** for each chart.
5. (Optional) Activate the **Use Rolling Dates** option to shift the start date by one day every day.
6. From the tree view on the left, drag and drop time series into the charts to visualize different key figures:
   - **Workloads**: History, Forecast, Import, and {% link_new forecast versions | features/forecast/injixo-forecast/store-forecast-versions.md %}. 
   - **Planning units**: Staffing, staff requirements, and coverage for scheduled shifts and activities, plus shifts requested in Me
   - **WFM Queues**: Workload data in WFM queues that you saved by clicking _Use forecast_{:.doc-button} in the workload page. The option may not be available, depending on your WFM plan. 

      > Note
      >
      > - The {% icon circle_exclamation %} in the legend of a chart is displayed if you have no data for a period.
      > - In workloads, you may see special key figures depending on your integration, e.g. if your workloads only contain queues from a [Genesys Cloud integration](/add-genesys-cloud-integration/), you will see information related to abandoned calls, average speed of answer, and calls answered within service level. 

7. Click _Save_{:.doc-button}.<br>To return to the view mode, click _Close Edit mode_{:.doc-button}.

### Duplicate a dashboard

To create a new dashboard with the same general properties as an existing dashboard, follow these steps:
1. Go to _Analyze > Dashboards_{:.breadcrumbs}.
2. From the drop-down menu, select a dashboard.
3. From the {% icon ellipsis_v %}, select **Duplicate Dashboard**.
4. Edit the name and configuration details, if needed.
5. Click _Save_{:.doc-button}.

### Auto-refresh dashboards

You can automatically refresh the selected dashboard. To do so, select an interval from the drop-down menu on the right and click _{% icon arrows-rotate | icon-only %} Auto-Refresh_{:.doc-button}.<br>In the lower left of the page, you can see when the dashboard was last updated.

## Edit dashboards

1. Go to _Analyze > Dashboards_{:.breadcrumbs}.
2. From the drop-down menu, select a dashboard.
3. From the {% icon ellipsis_v %} on the right, select **Edit**.
4. Edit the dashboard, {% link_new customize time series | features/monitoring/dashboards/work-with-charts.md | #customize-time-series %} or {% link_new delete | features/monitoring/dashboards/work-with-charts.md | #delete-time-series %} them.
5. Click _Save_{:.doc-button}. To return to the view mode, click _Close Edit mode_{:.doc-button}.

## Delete dashboards

1. Go to _Analyze > Dashboards_{:.breadcrumbs}.
2. From the drop-down menu, select a dashboard.
3. From the {% icon ellipsis_v %} on the right, select **Edit**.
4. Click _Delete_{:.doc-button} at the bottom right.  
5. In the confirmation window, click _Delete Dashboard_{:.doc-button}.<br> To cancel the deletion, click _Keep Dashboard_{:.doc-button}.

If you delete the last remaining dashboard, the page shows the edit mode until you [create a new dashboard](#create-dashboards).
