---
title: Optimize breaks
product_label:
  - essential
  - advanced
  - enterprise
permalink: /break-optimization/
permalink_reason: /break-optimization/ used in email and in Intercom message
description: Optimize the distribution of breaks in your schedule to achieve a better coverage of your employee requirements for all activities.
promote-service: schedule-optimization-workshop
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
---

The **Optimize breaks** functionality can move breaks within your schedule to optimize the coverage of activities with staff requirements. The start and end times of shifts remain unchanged. The **Optimize breaks** functionality preserves the break corridors configured in day models. This allows you to run further break optimizations on already optimized periods if staff requirements change.

Example: Two employees have a shift on the same day with a scheduled break from noon to 1&nbsp;PM. Their breaks can start every 30&nbsp;minutes between noon and 3&nbsp;PM. To improve the low coverage for activities of type Presence around noon, injixo moves at least one of the breaks to a later time.

### Prerequisites

For the **Optimize breaks** functionality to work, the following needs to apply:
- There is a schedule in the Schedule level. 
- For the time periods to be optimized, there must be activities of type Presence where the breaks can be moved to.
- There are break corridors in your day models. 

## Run a break optimization

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling actions_{:.doc-button} and select **Optimize breaks**.
3. Select a **Planning unit**. The planning unit is pre-filled if a planning unit has been expanded in Schedules.
4. (Optional) Choose a **Selection** for which you want to perform the break optimization.
5. Select a **Date range**.<br>The pre-selected date range is the date range currently selected in Schedules. You can select the current or any future date.  <!-- do NOT explain feature-flag-based *Use Smart Optimization* checkbox-->
6. Click _Optimize breaks_{:.doc-button}. <!-- not handled as JobProcessor job -->

The maximum runtime of the optimization process is 60&nbsp;minutes and the functionality will use the best solution found during this time. The actual runtime depends on the number of people, the number of breaks in the schedule, and the length of the period to be optimized. While the optimization is running, you cannot edit the schedule for the affected timeframe. After the optimization is finished, injixo saves the optimized schedule automatically and updates the status in the **Break optimization history** section.

{{ 5 | image: 'Job optimization overview '}}

## Understand the optimization status

Each completed optimization creates an entry in the **Break optimization history** section with details such as start time, user, planning unit, selection, and the optimized period. 

The following optimization statuses are possible:

- Optimized schedule: The break optimization was successful and the result was saved to the Schedule level.
- Partly optimized schedule: The optimization could not optimize all breaks.
- Optimization failed: The optimization could not be started. Try restarting the optimization. If this status persists, create a ticket to contact our support team.

### Partly optimized schedule

<!-- Do not change this heading: /break-optimizations#partly-optimized-schedule is used within the break optimization UI -->

The status Partly optimized schedule is displayed when an optimization could not optimize all breaks in the selected period. There are three possible reasons:

- Some breaks have been skipped by the optimization, e.g. as they would otherwise overlay meeting activities, which is not allowed. These breaks are still in the position where they were at the start of the optimization.
- Some breaks were not included in the optimization because they are too short (below 5 minutes) or incompatible with the interval used by the planning unit.
- Some breaks could not be optimized due to certain {% link_new scheduling rule | features/administration/create-contracts.md | #scheduling-rules %} violations. For example, an employee may have been scheduled for an activity without having the required skill(s).

## Review the optimization results

In the **Break optimization history** section, a table shows previous optimizations. When an optimization's end date matches the current date, the entry is removed from the list.


To see the details for an entry, click _View results_{:.doc-button}. The status now shows how many breaks have been optimized. A diagram with two graphs shows the deviation from the coverage before and after the optimization for the optimization period.
<!-- From this sentence on, we need to change the information about coverage and the graph. "Perfect coverage" is not a term that has any meaning, see: https://ivx.slack.com/archives/C9Y6W10NS/p1691742308844969?thread_ts=1690371315.535319&cid=C9Y6W10NS. The graph label on the y-axis is also very confusing, "coverage - Total deviation from 0. It does not display clearly what is the value in the graph. The deviation is just the absolute value between the real coverage and the optimized coverage. -->
The diagram illustrates the deviation from the coverage before and after the optimization. It shows two graphs which sum up the coverage data of all scheduled activities over time:

- Yellow line: Original schedule (coverage) before optimization
- Green line: Optimized schedule (resulting coverage) after optimization

The numbers displayed in the graphs sum up the coverage data of all scheduled activities. The closer the green graph is to 0, the more the optimization improved the coverage. For example, a value of 5 for **Total deviation from 0** indicates an overstaffing of 5 employees at that time.

{{ 3 | image: 'Graph for the break optimization results', '70%' }}

### How the graphs are calculated

Assume your planning unit has two different activities of type _Presence_, each forecasted and scheduled with a 15-minute interval, resulting in four intervals per hour. For these four intervals, the table below shows the coverage for both activities, the deviation from the perfect coverage, as well as the total deviation which is the sum of the values of the deviation from the perfect coverage. A positive value shows overstaffing, a negative value understaffing.

| Queue            | Coverage            | Deviation from the coverage |
| ---------------- | ------------------- | ----------------------------------- |
| Customer Support | [0, -2, -1, 0]      | [0, 2, 1, 0]                        |
| Financial Issues | [3, 2, 2, 0]        | [3, 2, 2, 0]                        |
|                  | **Total deviation** | [3, 4, 3, 0]                        |

In the diagram, the green and yellow graphs are showing the _total deviation_ values.

### View the intervals of a day

For a date range of up to three days, the diagram displays the intervals for each day by default. For four days or more, the diagram only shows the total values for each day. However, you can display the individual intervals of a day if required:

1. Hover over a **day in the diagram** and click it. The view displays the intervals for the day now.
2. Click _Back to day-view_{:.doc-button} to return to the overview.

   {{ 4 | image: 'The view for the intervals of a day and a back button', '70%' }}
