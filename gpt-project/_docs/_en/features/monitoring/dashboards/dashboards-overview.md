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

_Analyze > Dashboards_{:.breadcrumbs} allows you to create dashboards with up to four different charts. Each chart can display graphs for multiple [time series](https://help.injixo.com/glossary/overview/#time-series)<!-- full url intended --> and date ranges.

To display a dashboard, select a dashboard from the drop-down menu, or type in the field to filter. If you don't have a dashboard yet, the page will show the edit mode, and you can [create a dashboard](#create-dashboards).

You can choose from the following key figures:

- **Workloads**: History, forecasts, or {% link_new forecast versions | features/forecast/injixo-forecast/store-forecast-versions.md %}
- **Planning units**: Staffing, requirement, and coverage for scheduled shifts and activities, plus shifts requested in Me
- **WFM Queues**: Workload data in queues in WFM. To see data, you need to click _Use Forecast_{:.doc-button} in your Forecast workloads.

Hint: Hover over a graph to display a tooltip showing the interval values for each graph.

## Create dashboards

1. Go to _Analyze > Dashboards_{:.menu-item} and click the {% icon ellipsis_v %} on the right.
2. To access the edit mode, click **Create New Dashboard**.
  - Enter a **Name** for the new dashboard.
  - In the **Layout** section at the top right, define the number of charts by selecting one of layouts.
  - In the **Untitled Chart** field, enter a name for the chart(s) to describe the purpose or content. The names don't have to be unique.
3. Select a **date range** for the chart(s).
4. (Optional) Activate the **Use Rolling Dates** option to shift the start date by one day every day.
5. In the tree view on the left, drag and drop time series into the chart(s).
    If workloads do not contain data for a period, you will see the {% icon circle_exclamation %} in the legend.
6. Click _Save_{:.doc-button}. To return to the view mode, click _Close Edit mode_{:.doc-button}.

### Copy a dashboard

To copy an existing dashboard, click the {% icon ellipsis_v %}, then click _Duplicate Dashboard_{:.doc-button}.

### Auto-refresh dashboards

You can automatically refresh dashboards every 15 minutes. After you have selected a dashboard, click _Auto-Refresh_{:.doc-button}. The bottom of the page will show when a dashboard was last updated.

### Activate full-screen mode

For a more detailed view, switch to full-screen mode. Click the {% icon maximize %} in the top right corner.

## Edit and delete dashboards

1. Select a dashboard and click the {% icon ellipsis_v %} on the right.
2. To access the edit mode, click **Edit**.
3. To edit the dashboard, {% link_new customize time series | features/monitoring/dashboards/work-with-charts.md | #customize-time-series %} or {% link_new delete | features/monitoring/dashboards/work-with-charts.md | #delete-time-series %} them.
4. Click _Save_{:.doc-button}. To return to the view mode, click _Close Edit mode_{:.doc-button}.


## Delete dashboards

1. Select a dashboard and click the {% icon ellipsis_v %}.
2. To access the edit mode, click **Edit**.
3. To delete the dashboard, click **Delete** on the bottom right.  
   You will see the following message: You are about to delete this Dashboard. Are you sure?
4. Click _Delete Dashboard_{:.doc-button}. To abort the deletion, click _Keep Dashboard_{:.doc-button}.

Note: If you delete the last remaining dashboard, the screen will show the edit mode until you [create a new dashboard](#create-dashboards).
