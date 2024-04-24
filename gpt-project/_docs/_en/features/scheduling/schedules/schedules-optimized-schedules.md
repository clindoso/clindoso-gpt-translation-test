---
title: Create an optimized schedule
description: Learn what an optimized schedule is, how to configure injixo for optimal results, and how to create an optimized schedule.
product_label:
  - advanced
  - enterprise
---

In this article, you will learn:

- what an optimized schedule is.
- how to configure your system in order to achieve the best optimization results.
- how to create an optimized schedule.

## What is an optimized schedule?

The feature _Create optimized schedule_ (also called AutoScheduler) automatically creates a full schedule with the best possible coverage for all activities with the lowest possible number of employees. The schedule is created based on the employee requirements for the different activities.

## Configure injixo for optimal results

For the _Create optimized schedule_ feature to produce the best results, you have to configure injixo properly:

- Configure your {% link_new employees | features/administration/employee-overview.md %}.
- Check the scheduling parameters and AutoScheduler parameters of your contracts under _WFM > Administration > Scheduling > Contracts_{:.breadcrumbs}. The optimization has to adhere to these settings.
- Add all day models to the planning unit that you want to use in the optimization. The optimization considers all day models of the planning unit.
- Make sure the planning unit has opening hours and that the shifts fit into the opening hours.
- The length of the available {% link_new day models | features/administration/daymodels/daymodel-creation.md %} must match the employees' contractual working hours.
- The activities which are scheduled by the optimization must be configured as _Plannable_. These activities will then replace activities configured as _Replaceable_ if necessary.
- Use {% link_new work time pattern models | features/administration/work-time-pattern-models.md %} for employees if you want to limit the possible working time combinations for the optimization.
- Check the {% link_new importance | best-practices/importance-for-activities.md %} and {% link_new priority | best-practices/priority-for-activities.md %} settings of your activities. They define which activities can overwrite other activities and which activities are prioritized during the optimization process.

## Create an optimized schedule

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling actions_{:.doc-button}.
3. Click **Create optimized schedule**.
4. Select the **Date range** for which you want to create schedules. The date range is pre-filled with the currently selected date range in _Schedules_.
5. Select a **Planning unit**.
6. Pick a **Selection** (optional) if you want to limit the optimization to a selection of employees.
7. Check the **Optimize again** checkbox if you have created an optimized schedule before that contains work time pattern models of type C and you want to allow the reshuffling of the order of the used week time patterns. Otherwise, injixo will use the same sequence of week time patterns as before. You have to delete the existing schedule first before creating a new one.
8. Click **Start full optimization**. A green success notification appears if the optimization job was started successfully. A red message appears when the job couldn't be started.

{{ 1 | image: 'Input dialog to create an optimized schedule', '70%' }}

The optimization job can take some time, depending on the amount of data and the selected period. During this time you can't make any changes to the schedule in the date range that is being optimized. After the job is finished, injixo saves the optimized schedule automatically.

Go to _WFM > Administration > System > JobProcessor_{:.breadcrumbs} to view the progress of a running optimization. There, you will also find a link to the {% link_new scheduling report | best-practices/resolve-optimization-issues.md %} when the process has been finished. It helps to find and resolve scheduling errors that occur during the optimization process.
