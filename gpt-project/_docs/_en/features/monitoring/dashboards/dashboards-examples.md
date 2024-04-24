---
title: Dashboard examples
description: "See some practical examples for Dashboards."
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn about some practical dashboards you might want to use in your planning.
---

In _Analyze > Dashboards_{:.breadcrumbs}, you can visualize and organize your data into charts to monitor, compare and analyze key metrics, and make informed decisions. The following examples describe useful dashboard configurations.

New to Dashboards? Learn the basics and {% link_new how to create dashboards | features/monitoring/dashboards/manage-dashboards.md | #create-dashboards %} first.

## Compare staff requirements and staffing per activity

To create a dashboard that compares calculated staff requirements for an activity with its actual staffing, proceed as follows:

1. In _Analyze > Dashboards_{:.breadcrumbs}, {% link_new create a new dashboard | features/monitoring/dashboards/manage-dashboards.md | #create-dashboards %}.
2. From the **Planning units** drop-down menu on the left, select a planning unit.
3. In the **Activities** list, select **Presence**.
4. Expand the activity for which you want to display data.
5. Drag and drop **Requirement** into an empty chart.
6. Drag and drop **Staffing** into the same chart.<br>Each scheduling level has its own Staffing and Coverage version. Pick the version that matches the level you are using.
7. Click _Save_{:.doc-button}.

## Compare total staff requirements and staffing

To create a dashboard that compares calculated staff requirements for an entire planning unit with its actual staffing, proceed as follows:

1. In _Analyze > Dashboards_{:.breadcrumbs}, {% link_new create a new dashboard | features/monitoring/dashboards/manage-dashboards.md | #create-dashboards %}.
2. From the **Planning units** drop-down menu on the left, select a planning unit.
3. In the **Activities** list, select **Presence**.
4. Expand the **Totals presence** metric.
5. Drag and drop **Requirement** into an empty chart.
6. Drag and drop **Staffing** into the chart.<br>Each scheduling level has its own Staffing and Coverage version. Pick the version that matches the level you are using.
7. Click _Save_{:.doc-button}.

## Compare forecasted and actual incoming calls

To create a dashboard that compares forecasted calls with actual incoming calls, proceed as follows:

1. In _Analyze > Dashboards_{:.breadcrumbs}, {% link_new create a new dashboard | features/monitoring/dashboards/manage-dashboards.md | #create-dashboards %}.
2. From the **Workloads** drop-down menu on the left, click a workload.
3. Drag and drop **Offered Calls Forecast** and **Offered Calls - Operational** into an empty chart.
4. From the **Planning units** drop-down menu on the left, select a planning unit.
5. From the **Activities** list, select **Presence** and expand the activity for which you want to display data.
6. Drag and drop **Coverage** into the chart.<br>Each scheduling level has its own Staffing and Coverage version. Pick the version that matches the level you are using.
7. Click _Save_{:.doc-button}.

To compare the forecasted and actual Average Handle Time (AHT), create a similar chart using **AHT** and **AHT - Operational** data. 

## Visualize absences per planning unit

To create a dashboard that displays absences, vacation, breaks, meetings, and illnesses per planning unit, proceed as follows:

1. In _Analyze > Dashboards_{:.breadcrumbs}, {% link_new create a new dashboard | features/monitoring/dashboards/manage-dashboards.md | #create-dashboards %}.
2. From the **Planning Units** drop-down menu on the left, select a planning unit.
3. From the **Activities** list, expand the activities for which you want to display data.
4. For each activity, select and drag and drop the **Staffing** metric into one chart.
5. Click _Save_{:.doc-button}.

Full-day activities and vacation are shown as horizontal lines, while shorter activities such as breaks or meetings are displayed as bars.

## Compare incoming and answered calls

To create a dashboard that displays incoming and answered calls for a specific workload, proceed as follows:

1. In _Analyze > Dashboards_{:.breadcrumbs}, {% link_new create a new dashboard | features/monitoring/dashboards/manage-dashboards.md | #create-dashboards %}.
2. From the **Workloads** drop-down menu on the left, click a workload.
3. Drag and drop **Offered Calls History** and **Answered Calls History** into an empty chart..
4. Click _Save_{:.doc-button}.
