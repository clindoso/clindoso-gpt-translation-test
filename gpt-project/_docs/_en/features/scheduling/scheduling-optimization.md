---
title: Optimize your schedule
redirect_from: /schedule-optimization/
redirect_reason: renamed file in July 2020
description: Learn more about the three available optimization processes, the break, job, and full optimization.
product_label:
  - classic
promote-service: schedule-optimization-workshop
---

injixo offers three different optimization processes, which will influence your scheduling. In injixo Classic, the optimization page displays all past and current optimizations.

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you don't have the injixo Classic WFM plan, use the {% link_new Optimize breaks | features/scheduling/schedules/break-optimization.md %}, {% link_new Job optimization | features/scheduling/schedules/schedules-job-optimization.md %} and {% link_new Create optimized schedules | features/scheduling/schedules/schedules-optimized-schedules.md %} functionality under _Plan > Schedules_{:.breadcrumbs} instead.

## Three optimization types

- **Optimized scheduling:** Create an optimized schedule based on your configuration and staff requirements.
- **Job optimization:** Optimize activities and breaks in an existing schedule. The Job optimization functionality replaces replaceable activities with plannable activities and moves breaks that are placed in {% link_new corridors within day models | features/administration/daymodels/daymodel-basics.md | #fixed-elements-vs-corridors %}.
- **Break optimization:** Optimize the position of breaks after you have made changes to an existing schedule.

Depending on the amount of data and the selected time period, running an optimization may take longer. During this time, you cannot change the schedule for the optimization period. injixo will save the schedule automatically.

Under _WFM > Scheduling > SchedulePro > Optimization_{:.breadcrumbs}, finished optimizations display a report icon that links to the {% link_new scheduling report | best-practices/resolve-optimization-issues.md %}. The report helps you to understand any scheduling errors in case they occur.

## What are fully optimized schedules?

The Fully optimized schedules functionality (AutoScheduler) automatically creates a schedule with the best possible coverage for all activities with the lowest possible number of employees. The schedule is created based on the staff requirements for the different activities.

### Configure injixo for fully optimized schedules

- {% link_new Employees | features/administration/employee-overview.md %} are only scheduled for activities that they are skilled for (or for activities that do not require any skill).
- Make sure the Scheduling parameters and AutoScheduler parameters in the contracts are correct. The optimization has to adhere to configured values, e.g. Minimum Number of Working Days per Week or Maximum Number of Working Hours per Day.
- Make sure the configuration of the planning unit contains the business hours. Resulting shifts from day models must fit into the business hours of your planning unit.
- The length of available {% link_new day models | features/administration/daymodels/daymodel-creation.md %} must match the employees' contractual working hours.
- Activities that need to be scheduled must be configured as Plannable. Plannable activities can replace other activities configured as Replaceable, e.g. the Present activity.
- The optimization considers all day models assigned to a planning unit. You can remove all day models from your planning unit and add only specific day models.
- To limit working time combinations and set up rotations, you can use {% link_new work time pattern models | features/administration/work-time-pattern-models.md %}.
- The {% link_new importance | best-practices/importance-for-activities.md %} and {% link_new priority | best-practices/priority-for-activities.md %} values of your activities define which activities can overwrite other activities and which activities are prioritized.

### Create optimized schedules

1. Go to _WFM > Scheduling > SchedulePro > Optimization_{:.breadcrumbs}.
2. In the menu bar, select _Fully Optimized Schedule_{:.doc-button}.
3. Under **Time Period**, set a **Start date** and **End date**. The maximum period is 10 weeks.
4. Select a **Planning Unit**.
5. (Optional) Under **Selection**, use the default **[All]** or pick a selection from the drop-down menu.
   All employees are optimized but the results are saved only for the employees in the selection.
6. (Optional) Check **Optimize again** to run the optimization on an existing schedule that has been created based on work time pattern models of type C. This will reshuffle the order of weekdays previously used. In any other case, delete the existing schedule before you create a new one.
7. Click _Ok_{:.doc-button}.

## What is the Job optimization?

The job optimization exchanges activities in your employees' schedules without changing the start and end times of the shifts. The goal is to achieve the best possible coverage for all activities based on the staff requirements of the activities. Breaks are also optimized.

Example: Some people are skilled for the Travels activity. Via shift bidding, they have received shifts with the replaceable activity Present and a break around lunchtime. For periods with staff requirements, the Present activity is replaced by the Travels activity in the skilled peoples' schedule.

Use the Job optimization on an existing schedule:

- to optimize the coverage for activities when staff requirements have changed in the meantime.
- after the Lottery or Assign function in shift bidding or insert shift sequences to replace replaceable activities in day models with plannable activities based on staff requirements.

The Job optimization functionality converts day models into individual activities, while break corridors remain intact.

Tip: When you use shift bidding, only use the Present activity (ID 1) in your day models. This way, employees cannot request shifts with specific activities but only the shift start time and shift length. The Job optimization will replace the Present activity with other activities for which staff requirements exist. The Present activity needs to be configured as Replaceable and the other activities need to be configured as Plannable.

### Configure injixo for Job optimization

- {% link_new Employees | features/administration/employee-overview.md %} are only scheduled for activities they are skilled for (or activities that do not require a skill).
- Make sure to configure your activities with staff requirements as Plannable. The plannable activities will replace other replaceable activities.
- The {% link_new importance | best-practices/importance-for-activities.md %} and {% link_new priority | best-practices/priority-for-activities.md %} values of your activities define which activities can overwrite other activities and which activities are prioritized.

### Run the Job optimization

1. Go to _WFM > Scheduling > SchedulePro > Optimization_{:.breadcrumbs}.
2. In the menu bar, select _Job Optimization_{:.doc-button}.
3. Under **Time Period**, set a **Start date** and **End date**. The maximum period is 10 weeks.
4. Select a **Planning Unit**.
5. (Optional) Under **Selection**, use the default **[All]** or pick a selection from the drop-down menu.
   All employees are optimized but the results are saved only for the employees in the selection.
6. Click _Ok_{:.doc-button}.

## What is the Break optimization?

The Break optimization functionality redistributes breaks within your schedule to optimize the coverage of activities with staff requirements. The start and end times of shifts remain unchanged. Existing day models are converted into activities within the optimization period. Break corridors remain intact, so that you can run further break optimizations if necessary.

Example: Two employees have got a shift with a break from 12:00 to 13:00. The break can start every 30 minutes between 12:00 and 15:00. To improve the low coverage for the base activity of the shift between 12:00 and 13:00, injixo will move at least one of the breaks to a later time.

### Run the Break optimization

1. Go to _WFM > Scheduling > SchedulePro > Optimization_{:.breadcrumbs}.
2. In the menu bar, select _Break Optimization_{:.doc-button}.
3. Under **Time Period**, set a **Start date** and **End date**. The maximum period is 10 weeks.
4. Select a **Planning Unit**.
5. (Optional) Under **Selection**, use the default **[All]** or pick a selection from the drop-down menu. All employees are optimized but the results are saved only for the employees in the selection.
6. Click _Ok_{:.doc-button}.

## Optimizations in injixo Enterprise on-premise

In injixo Enterprise on-premise, the Fully optimized schedules functionality is called AutoScheduler. The AutoScheduler does not run via JobProcessor. To start the AutoScheduler, go to _WFM > Scheduling > SchedulePro > Shift Center_{:.breadcrumbs} and click the icons in the menu bar. The job and break optimization can also be started from the {% link_new planning periods | features/scheduling/planning-periods/what-are-planning-periods.md %} page. To write the optimization result into the schedule and show the scheduling report, click **Save**. Your changes are not saved automatically.
