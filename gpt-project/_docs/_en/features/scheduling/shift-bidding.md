---
title: Set up shift bidding
description: Use the shift generation, lottery, and shift assignment processes to engage your employees in the scheduling process for increased user satisfaction (SchedulePro).
promote-service: new-planner-training
product_label:
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/what-are-planning-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/employee-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shift-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/view-approve-shift-swap-requests.md
---

Shift bidding allows your employees to actively participate in the scheduling process.

The important facts in brief:

- You create shifts based on the {% link_new employee requirements | features/scheduling/employee-requirement.md %} and the {% link_new shift requirements | features/scheduling/shift-requirement.md %}.
- Your employees can request the generated shifts via _injixo Me_{:.menu-item}.
- You can lottery the requested shifts.
- You can assign the remaining shifts (like those that are unpopular).

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you are using injixo Advanced WFM or Enterprise WFM, use scheduling periods under _Plan > Schedules_{:.breadcrumbs} for {% link_new shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %} instead.

Take note:

- The process requires a planning period of the type Standard.
- The status of the planning period influences the visibility of the schedules.
- (Optional) You can combine the shift lottery with the Create optimized schedules functionality.

Complete process:

- [Workflow Shift Bidding](/assets/img/en/features/shift-bidding/image-1.png)

## Generate, lottery, assign shifts with planning periods

In _WFM > Scheduling > SchedulePro > Planning Periods_{:.breadcrumbs}, when you select a planning period you are presented the **Shifts** navigation block on the right side:

{{ 2 | image: 'Planning Periods with Shift Functions'}}

## Preparation

All relevant menu items are in _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.

1. Check if {% link_new employee requirements | features/scheduling/employee-requirement.md %} exist. They are the basis for shift generation (in combination with the shift requirement).

2. (Optional) If you use shift sequences for all or some employees, insert them.

3. You need a {% link_new planning period | features/scheduling/planning-periods/what-are-planning-periods.md %} of type Standard with status Locked. The scheduling data is not (yet) visible to your employees. In this way, you can also prepare the planning periods for several future schedules in advance.

4. You need a {% link_new shift requirement | features/scheduling/shift-requirement.md %} to create shifts. Check vacations and other absences in the schedule for the upcoming planning period and update the table before each shift generation. Otherwise, you would create an oversupply of shifts.

Remark on the shift requirement:

- If the shift requirements is created incorrectly, or not at all, some employees may be not scheduled. With no restrictions, injixo could e.g. only generate part-time shifts as these are best suited to cover the requirement curve.
- To limit the generation of shifts to the opening hours of the planning unit, make sure that there is no employee requirement outside the business hours. Enter zeros for days when the planning unit is closed (e.g. holidays).
- The more flexible your employees' contracts are, the more time-consuming it is to enter shift requirements. Therefore, our recommendation - possibly at the expense of your scheduling flexibility - is to use only a limited number of day models for full-time and part-time employees. The optimal would be a mix of short and long flexible shifts to achieve the contractually agreed working time.
- To ensure the maximum possible flexibility in the schedule, use Present as {% link_new base activity of your day models | features/administration/daymodels/daymodel-creation.md | #add-a-presence-or-absence-activity %}.

## Create shifts for bidding

Shift generation generates shifts for each day of the planning period and tries to achieve the best possible coverage of the requirement curve. Shifts that already exist in the schedule are taken into account.

1. Select a **planning period** of the type Standard in the overview.
2. Click _Generate_{:.doc-button} in the **Shifts** section.
3. The shift generation parameter window opens:
   {{ 3 | image: 'Parameter window for shift generation', '50%' }}
4. Optionally adjust the following parameters:
   - The **start date**/**end date** of the planning period.
   - The value for the **shift generation requirement**. A value above 100% generates more shifts than specified by the requirement. A value below 100% may be required if the personnel capacity is too low to cover the requirement.
   - The options **of the employee requirement** and **of the contractual hours**. These determine whether the requirement is to be met based on employee requirements or based on the contract hours.
5. Click _OK_{:.doc-button} to start the shift generation.

Activate the option _Display job results_{:.menu-item} to generate the **result report**. This report contains information, warnings, and errors concerning the configuration data and the shift generation itself (run time, writing of requirement data, violations of scheduling rules). If you click _Close Dialog_{:.doc-button}, the shift generation continues in the background. While the process is running, the scheduling data is protected during the optimization period. You cannot make any changes to the schedule during this time.

## Shift request of your agents

Change the status of the {% link_new planning period | features/scheduling/planning-periods/what-are-planning-periods.md %} to Enabled so that the created shifts are visible and requestable for your employees.

The employees can make an initial request and an alternative request. Several employees can bid on the same shift. They can see how many shifts are needed and how often a certain shift has already been requested. This way they can estimate the probability of getting a shift and, if necessary, find alternative shifts.
During the lottery, the initial check is whether the normal request can be fulfilled or not.
Define a deadline in your planning period to determine the time in which your employees can enter their bids.
The submitted bids appear in the levels Request and Alternative Request in _Schedules_{:.menu-item} or in the _Shift Center_{:.menu-item}.

## Schedule generated shifts

After the deadline, set the planning period back to the status Locked. You can edit the schedule without your employees already having access to it.

### Lottery of requested shifts

With the lottery, the requested shifts are distributed among the employees. Successful requests from the levels Request and Alternative Request are copied into the level Schedule.

Start the lottery:

1. Select the **planning period** in the overview.
2. Click _Lottery_{:.doc-button} in the shifts section.
3. Select the [relevant parameters](#parameters-for-lottery-and-assignment) in the pop-up window.
4. Click _OK_{:.doc-button} to start the lottery.

If necessary, check the **Create Lottery Log** checkbox. This report contains the selected parameters (user name, planning unit, start date and end date), information about employees (personnel number, target time account, work time account) and raffled shifts and reasons for refusal of normal requests/alternative requests. Also, the results of the lottery for normal/alternative requests and the daily and total quotas per employee in % and the total quota in % for all employees are included.

> Note
>
> A new shift generation deletes already submitted requests.

For a fair distribution, employees' requests can be drawn by selections. If you rotate over the selections in each planning period, you ensure that one group is always preferred and has a higher chance to get the requested shifts.

### Assignment of remaining shifts

Start the assignment:

1. Select the **planning period** in the overview.
2. Click _Assign_{:.doc-button} in the shifts section.
3. Select the [relevant parameters](#parameters-for-lottery-and-assignment) in the pop-up window.
4. Click _OK_{:.doc-button} to start the assignment.

If required, check the **Create Assignment Log** checkbox. The report contains the selected parameters (user name, planning unit, start date and end date), information about employees (personnel number, time account, working time account) and assigned shifts and reasons for rejection.

The assignment randomly assigns shifts to employees for which there were no or too few requests in _injixo Me_{:.menu-item}.
These shifts remain unoccupied if there are too few employees. If employees cannot perform certain shifts due to skills or shift length, the schedule may remain incomplete. Therefore, check the assignment log and the schedule after the assignment.

### Parameters for lottery and assignment

Both the lottery and assignment parameter windows contain the same fields. Here is an example for the lottery:

{{ 4 | image: 'Parameter window lottery', '65%' }}

You have the following options:

- Choose all employees, individual employees, or selections.
- Change the start or end date.
- Create a protocol in PDF format.
- Activate the consideration of an average start time for other shifts. Enter the **Tolerance** in HH:MM format. In this range, the shifts may deviate from the average shift start.

The time corridor for the **Tolerance** behaves differently, depending on whether shifts are already present in the schedule or not:

| Case           | Calculation                                                                                                                                                                                                                                                                                                 |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Without Shifts | The time corridor is observed for all further shifts after the first shift is assigned.<br> If the first shift starts at 9 o'clock and you set a tolerance of 1 hour, all further shifts start between 8 and 10 o'clock.                                                                                    |
| With Shifts    | An average shift start is determined. This is crucial for the assignment of shifts within the time corridor.<br> If shifts are already scheduled to start at 8 and 12 o'clock, 10 o'clock is used as the average value. All other shifts have to start with a tolerance of 1 hour between 9 and 11 o'clock. |

## Replace present in shifts with the job optimization

Run the {% link_new Job Optimization | features/scheduling/scheduling-optimization.md | #what-is-the-job-optimization %} if your shifts do not contain the final activities. This will replace the placeholder activity Present (but also other replaceable activities) with plannable activities with existing employee requirements.

## Publish the schedule and allow your agents to swap shifts

Set the status of the {% link_new planning period | features/scheduling/planning-periods/what-are-planning-periods.md %} to Information so that your employees can view their shifts. Your employees can swap shifts if you have configured the {% link_new shift swap | features/scheduling/view-approve-shift-swap-requests.md %}.
