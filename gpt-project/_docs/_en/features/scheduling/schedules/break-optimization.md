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

In this article, you will learn:

- how the _Optimize breaks_ feature improves your schedule.
- how to run the break optimization.
- how to view and analyze the results of the optimization.

## What is the Optimize breaks feature?

The goal of the _Optimize breaks_ feature is to redistribute breaks within your schedule in order to optimize the coverage of activities for which staff requirements exist. Shift start and end times remain unchanged. The _Optimize breaks_ feature converts existing day models into activities in the optimization period but it preserves the break corridors in day models, so that you can perform further break optimizations if necessary.

Example: Two employees have got a shift with a break from 12:00 to 13:00. The break can start every 30 minutes between 12:00 and 15:00. To improve the low coverage for the base activity of the shift between 12:00 and 13:00, injixo will move at least one of the breaks to a later time.

### Limitations

The _Optimize breaks_ feature requires an existing schedule in the _Schedule_ level. It can only place breaks in time periods which contain activities of type _Presence_. Also, it can only optimize moveable breaks in break corridors. It can't optimize fixed breaks. _Optimize breaks_ runs for a maximum of 60 minutes and uses the best solution found during this time.

## Run a break optimization

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling actions_{:.doc-button} and select **Optimize breaks**.
3. Select a **Planning unit**. The planning unit is pre-filled if a planning unit has been expanded in the _Schedules_ feature.
4. Choose a **Selection** (optional) of employees for which you want to perform the break optimization.
5. Select a **Date range** for the break optimization. You can select today and any future date. The date range is pre-selected by the date range currently selected in _Schedules_. <!-- do NOT explain feature-flag-based *Use Smart Optimization* checkbox-->
6. Click _Optimize breaks_{:.doc-button} to start the break optimization. You will see a green notification message if it was started successfully. Otherwise, a red notification appears. You can view the progress of a running optimization in _WFM > Administration > System > JobProcessor_{:.breadcrumbs}.

The optimization process can take some time, depending on the number of employees, the number of breaks in the schedule, and the length of the optimization period. While the optimization is running, you can't make any changes in the date range that is being optimized. After the optimization has been finished, injixo saves the optimized schedule automatically. The status in the _Break optimization history_ section below updates automatically after completion.

{{ 5 | image: 'Job optimization overview '}}

## Understand the optimization status

Each completed optimization leads to an entry in the _Break optimization history_ section with some details, such as start time, user, planning unit, selection, and the optimization period. The _Status_ column shows one of the following values:

- _Optimized schedule_: The break optimization was successful. The result was saved to the _Schedule_ level.
- _Partly optimized schedule_: The optimization couldn't optimize some of the breaks. Learn more about [this status](#partly-optimized-schedule) below.
- _Optimization failed_: The optimization could not be started. Try starting the optimization again. If the notification _Optimization failed. Please try again._ persists, {% link_new create a ticket | support/create-ticket.md %} to get support.

### Partly optimized schedule

<!-- Do not change this heading: /break-optimizations#partly-optimized-schedule is used within the break optimization UI -->

The status _Partly optimized schedule_ appears when the optimization couldn't optimize some of the breaks. There are three possible reasons for this:

- Some breaks have been skipped by the optimization, e.g. as they would otherwise overlay meeting activities, which is not allowed. These breaks are still in the place where they have been at the start of the optimization.
- Some breaks were left out as they are too short (< 5 minutes) or incompatible with the interval used by the planning unit.
- Some breaks could not be optimized due to certain {% link_new scheduling rule | features/administration/create-contracts.md | #scheduling-rules %} violations. For example, an employee might have been scheduled for an activity without having the required skill(s).

## Review the optimization results

To view the details of an optimization, click **View results** in the _Status_ column of the _Break optimization history_ section.

{{ 2 | image: 'Break optimization history' }}

For the selected optimization, you will see some details and how many breaks have been optimized (only in the case of a {% link_new partly optimized schedule | features/scheduling/schedules/break-optimization.md | #partly-optimized-schedule %}).

The diagram illustrates the deviation from perfect coverage before and after the optimization. It shows two graphs which sum up the coverage data of all scheduled activities over time:

- Yellow line: The coverage of the schedule _before_ the optimization
- Green line: The coverage of the schedule _after_ the optimization

The closer the green graph is to 0, the more the optimization improved the coverage. A value of e.g. 5 for _Total deviation from 0_ means that there is an overstaffing of 5 employees at that time.

{{ 3 | image: 'Graph for the break optimization results', '70%' }}

### How the graphs are calculated

Assume your planning unit has two different activities of type _Presence_, each forecasted and scheduled with a 15-minute interval, resulting in four intervals per hour. For these four intervals, the table below shows the coverage for both activities, the deviation from the perfect coverage, as well as the total deviation which is the sum of the values of the deviation from the perfect coverage. A positive value shows overstaffing, a negative value understaffing.

| Queue            | Coverage            | Deviation from the perfect coverage |
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
