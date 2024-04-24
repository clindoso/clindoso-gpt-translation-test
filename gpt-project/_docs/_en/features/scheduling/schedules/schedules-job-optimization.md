---
title: Run a job optimization
description: Learn what the Job optimization is, when to use it, how to configure injixo for optimal results, and how to run the optimization.
product_label:
  - essential
  - advanced
  - enterprise
---

The job optimization can replace activities in the schedule that have been configured as Replaceable, e.g. the Present activity, with plannable activities with staff requirements. The job optimization does not change the start and end times of the shifts. The goal is to achieve the best possible coverage for all activities based on the staff requirements of the activities. Breaks are also optimized.

Use the Job optimization:

- When the employee requirements for one or more activities have changed and you want to optimize the coverage for the activities accordingly.
- When you have assigned shifts to your employees using the Shift Bidding features _Lottery_ or _Assign_. In that case, the shifts typically contain just the _Present_ activity which needs to be replaced with the actual activities based on the employee requirements.
- When you have inserted shift sequences for your employees using shifts with the _Present_ activity or any other _Replaceable_ activities, and you want to replace these activities with the actual activities based on the employee requirements.

The job optimization converts day models into individual activities, break corridors remain intact.

> Use the activity _Present_ in the day models used for shift bidding
>
> If you offer shifts to your employees via injixo Me, it makes sense to use only the default system activity called _Present_ with ID 1 as an activity in the day models. This way you avoid that employees initially request shifts with specific activities but are then assigned completely different activities by the Job optimization.

### Example

Some employees are skilled for an activity called _Travels_. Via Shift Bidding, they have received shifts with _Present_ as the base activity and a break around lunchtime. The activity _Present_ has been defined as replaceable. The optimization now checks at which times there is an employee requirement for the activity _Travels_. For those times, the activity _Present_ is replaced by the activity _Travels_ in the schedules of the employees.

## Configure injixo for optimal results

- Configure your {% link_new employees | features/administration/employee-overview.md %}. Employees can only be scheduled for activities they are skilled in.
- The _Job optimization_ only works with activities that are configured as _Plannable_. These activities replace other activities which are configured as _Replaceable_.
- Ensure that an employee requirement exists for all activities which can replace other activities. Activities without an employee requirement won't be considered by the optimization.
- Check the {% link_new importance | best-practices/importance-for-activities.md %} and {% link_new priority | best-practices/priority-for-activities.md %} settings of your activities. They define which activities can overwrite other activities and which activities are prioritized during the optimization process.

## Run a job optimization

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling Actions_{:.doc-button}.
3. Click **Job optimization**.
4. Select the **Date range** in which you want to optimize activities. The date range is pre-filled with the currently selected time range in Schedules.
5. Select a **Planning unit**.
6. (Optional) To limit the optimization to a selection of employees, pick a **Selection**.
7. Click **Start job optimization**. 
   The background process starts. You will see a green notification if it was started successfully. A red message appears when the job couldn't be started.

{{ 1 | image: 'Input dialog for job optimization', '70%' }}

The optimization process can take some time, depending on the amount of data and the selected period. During this time you can't make any changes in the date range that is being optimized. After the optimization has been finished, injixo saves the optimized schedule automatically.

Go to _WFM > Administration > System > JobProcessor_{:.breadcrumbs} to view the progress of a running optimization. There, you will also find a link to the {% link_new scheduling report | best-practices/resolve-optimization-issues.md %} when the process has been finished. It provides some basic information about the optimization process.
