---
title: Examples for dashboards
description: "See some practical examples for Dashboards."
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn about some practical dashboards you might want to use in your planning.
---

New to Dashboards? Learn the basics and {% link_new how to create Dashboards | features/monitoring/dashboards/dashboards-overview.md | #create-dashboards %} first.

## Staffing vs. requirement per activity

Do you want to know if the calculated requirement for an activity is sufficiently covered?

1. In the menu to the left, navigate to _Planning Units > Name of Your Planning Unit > Activities > Presence_{:.breadcrumbs}.
2. Click the **activity** you want to display data for.
3. Drag and drop **Requirement** and **Staffing** into the chart to the right. There is a separate version of the _Staffing_ metric for each level. Pick the one for the scheduling level you are using.

{{ 1 | image: 'requirement vs staffing weekly' }}

## Total staffing vs. requirement

Do you want to know how good your staffing is covering the requirement overall?

1. In the menu to the left, navigate to _Planning Units > Name of Your Planning Unit > Activities > Presence > Totals Presence_{:.breadcrumbs}.
2. Drag and drop **Requirement** and **Staffing** into the chart to the right. There is a separate version of the _Staffing_ metric for each scheduling level. Pick the one for the scheduling level you are using.
3. Optionally, you can also add the **Coverage** metric to the chart.

{{ 5 | image: 'Total Presences vs. Requirement with Coverage' }}

## Forecasted vs. actual incoming calls

Check how accurate your previously saved forecast was compared to the actual daily call volume. The metric _Coverage_ is also added in order to visualize whether you have enough employees available to handle any additional calls.

1. In the menu to the left, click **Workloads** and then click the workload you want to display data for.
2. Drag and drop **Incoming Calls** and **Incoming Calls - Operational Version** into the chart to the right.
3. Navigate to _Planning Units > Name of Your Planning Unit > Activities > Presence_{:.breadcrumbs} and click the call activity you want to display data for.
4. Drag and drop **Coverage** into the chart. There is a separate version of the _Coverage_ metric for each scheduling level. Pick the one for the scheduling level you are using.
5. Create the same graphs with **AHT** and **AHT - Operational Version** to also be able to compare the forecasted and actual Average Handling Time (AHT).

{{ 2 | image: 'Forecasted Calls', '50%' }}

## Absences per planning unit

Do you want to know how many employees are on vacation, in meetings, or on break?

The Dashboards feature provides values for absences, vacation, breaks, meetings and illness per planning unit. Full-day activities and vacation are shown as horizontal lines, while shorter activities such as breaks or meetings are displayed as bars.

1. In the menu to the left, navigate to _Planning Units > Name of Your Planning Unit > Activities_{:.breadcrumbs}.
2. Click the activities you like to display data for and find the _Staffing_ metric. There is a separate version of the _Staffing_ metric for each scheduling level. Drag and drop the metric for the scheduling level you are using into the chart to the right.
3. Add all **Staffing** metrics you want to display.

{{ 3 | image: 'Absences, breaks, vacation, illnesses', '50%' }}

## Incoming vs. answered calls

You can use this dashboard view to see how many calls you received and how many you were able to handle.

1. In the menu to the left, click **Workloads** and then click the workload you want to display data for.
2. Drag and drop **Incoming Calls** and **Answered Calls** into the chart to the right.

{{ 4 | image: 'Comparison incoming and answered calls', '50%' }}
