---
title: Optimize breaks
product_label:
  - essential
  - advanced
  - enterprise
permalink: /break-optimization/
permalink_reason: /break-optimization/ used in email and in Intercom message
description: Learn how to optimize the distribution of breaks in your schedule to improve coverage.
promote-service: schedule-optimization-workshop
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-activity-coverage.md
---

The **Optimize breaks** functionality moves breaks within your schedule to optimize the coverage of activities with staff requirements.<br>
The start and end times of shifts do not change. The **Optimize breaks** functionality does not change the break corridors that you configured in day models but moves breaks within those corridors. You can run further break optimizations if staff requirements change.

### When should I optimize breaks?

Consider the following example:

Two people are scheduled on the same day with a break from 12&nbsp;PM to 1&nbsp;PM. Their breaks can start every 30&nbsp;minutes between noon and 3&nbsp;PM.<br>
Use the break optimization to improve coverage for the activities of type Presence around noon. The break optimization moves at least one of the breaks to a later time, between 12&nbsp;PM and 3&nbsp;PM.

### Prerequisites

To use the **Optimize breaks** functionality, the following conditions need to apply:

- There is a schedule in the Schedule [level](/glossary/overview/#level). <!-- add link to levels once it's been reworked https://help.injixo.com/tips-on-shift-center-usage#tip-9-working-with-different-levels -->
- Your schedule includes activities of type Presence for the time periods that you want to optimize. The break optimization will replace such activities with breaks.
- Your day models include {% link_new break corridors | features/administration/daymodels/daymodel-creation.md | #add-a-break-activity %}.

## Run a break optimization

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. From the _Scheduling actions_{:.doc-button} drop-down menu, select _Optimize breaks_{:.menu-item}.
3. In the **Set up break optimization** section, configure the break optimization:

   - **Planning unit**: The planning unit for which you want to perform the break optimization.
   - (Optional) **Selection**
   - **Date range**: You can select from one day up to two months in the future.
   <!-- do NOT explain feature-flag-based *Use Smart Optimization* checkbox-->

4. Click _Optimize breaks_{:.doc-button}. <!-- not handled as JobProcessor job -->

The optimization process can take up to 60&nbsp;minutes. The process duration is influenced by factors such as the number of people, the number of breaks in the schedule, and the length of the period to be optimized. <!--  The **Optimize breaks** functionality uses the best solution found during the optimization process - how else would it work? is this necessary? -->
During the optimization process, you cannot edit the schedule for the affected date range.<br>After the optimization is finished, injixo saves the optimized schedule in the Schedule level<!-- add link to the Levels article https://help.injixo.com/tips-on-shift-center-usage#tip-9-working-with-different-levels after it's been updated --> and updates the status in the **Break optimization history** section.

## Understand the optimization status

Each break optimization creates an entry in the table in the **Break optimization history** section. The table includes details about the optimization start date, the person who ran the optimization, the planning unit, the selection, the period, and the status. When an optimization's end date matches the current date, the entry is removed from the list.

The table below gives you more details about the possible optimization statuses:

| Status                    | Description                                     | Effect/Next step                                                                                       |
| ------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Optimized schedule        | The break optimization was successful.          | The resulting schedule was saved to the Schedule level.                                                |
| Partly optimized schedule | The optimization could not optimize all breaks. | Learn more about this status in the [dedicated section below](#partly-optimized-schedule).             |
| Optimization failed       | The optimization could not be started.          | Try restarting the optimization. If this status persists, create a ticket to contact our support team. |

### Partly optimized schedule

<!-- Do not change this heading: /break-optimizations#partly-optimized-schedule is used within the break optimization UI -->

The status Partly optimized schedule is displayed when the break optimization could not optimize all breaks in the selected period. There are three possible causes:

- The optimization did not move some breaks because, for example, they would overlay activities of type Meeting. The breaks keep the positions they had before the start of the optimization.
- The optimization did not include some breaks because, for example, they are shorter than 5 minutes, or because they do not match the {% link_new interval used by the planning unit | features/administration/create-and-manage-planning-units.md | #create-planning-units %}.
- The optimization ignored some breaks to prevent {% link_new scheduling rule | features/administration/create-contracts.md | #scheduling-rules %} violations, such as scheduling a person for an activity for which they do not have the required skill(s).

## See the optimization results

To see the details for a completed break optimization, click _View results_{:.doc-button}.
In the window that opens, the **Status** tile shows the number of optimized breaks.<br>
A diagram with two graphs shows the difference between the coverage before the break optimization (represented by a yellow line) and the coverage after the break optimization (represented by a green line).<br>
The horizontal axis represents the dates of the selected period.<br>
The vertical axis represents the total coverage for all planned activities in the selected planning unit and/or selection in the selected period, expressed in absolute values. For example, a value of 5 can represent either understaffing (5 people scheduled less than required) or overstaffing (5 people scheduled more than expected). To find out more about coverage, {% link_new check your schedule in the Schedule level | features/scheduling/schedules/schedules-activity-coverage.md %}.<br>

<!-- From this sentence on, we need to change the information about coverage and the graph. "Perfect coverage" is not a term that has any meaning, see: https://ivx.slack.com/archives/C9Y6W10NS/p1691742308844969?thread_ts=1690371315.535319&cid=C9Y6W10NS. The graph label on the y-axis is also very confusing, "coverage - Total deviation from 0. It does not display clearly what is the value in the graph. The deviation is just the absolute value between the real coverage and the optimized coverage. -->

The closer the green line is to 0, the more the break optimization improved the coverage.

### How are the graph values calculated?

Consider the following example:

You schedule two activities in your planning unit: Customer Support and Financial Issues. Your planning unit uses an interval of 15&nbsp;minutes, which results in four intervals per hour.<br>The following table shows the coverage values and the coverage expressed in absolute values:

<!-- left-align table -->
<style>
table {
   margin-left: 0px;
}
</style>

| Activity name    | Coverage values per interval | Coverage absolute values per interval |
| ---------------- | ---------------------------- | ------------------------------------- |
| Customer Support | [0, -2, -1, 0]               | [0, 2, 1, 0]                          |
| Financial Issues | [3, 2, -2, 0]                | [3, 2, 2, 0]                          |

For this example, the resulting total coverage values on the vertical axis are 3, 4, 3, and 0.

### Display the intervals of a day

If you select a period of up to three days, the diagram displays the intervals for each day by default.<br>
If you select a period of four days or more, the diagram displays the total values for each day. To display the intervals of a day, proceed as follows:

1. Hover over a day in the diagram and click it.
2. Click _Back to day-view_{:.doc-button} to return to the daily overview.
