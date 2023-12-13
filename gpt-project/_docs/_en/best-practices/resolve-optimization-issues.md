---
title: Resolve scheduling errors
toc: true
promote-service: schedule-optimization-workshop
redirect_from:
  - /optimization-issues/
  - /autoscheduler-scheduling-report-and-errors/
redirect_reason: renamed/deleted files in March 2020
product_label:
  - advanced
  - enterprise
  - classic
description: Identify and resolve common errors when using automatic scheduling processes.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
---

## Analyze issues with the Scheduling report

The Scheduling report is available for {% link_new schedule optimization | features/scheduling/scheduling-optimization.md %}. The report contains information about scheduling steps, warnings, and error messages.

Use the scheduling report to check the optimization result and to get an idea on how to resolve scheduling errors.

In injixo Advanced WFM and Enterprise WFM, you will find the scheduling report under _WFM > Administration > System > JobProcessor_{:.breadcrumbs} after you have created {% link_new optimized schedules | features/scheduling/schedules/schedules-optimized-schedules.md %}.

In injixo Classic, you can also access the reports under _WFM > Scheduling > SchedulePro > Optimization_{:.breadcrumbs}.  
In injixo Enterprise on-premise, the report is shown after saving the schedule in the Auto Scheduler.

Errors in the {% link_new scheduling report | best-practices/resolve-optimization-issues.md %} appear with the respective scheduling rule ID, e.g.:

```
Saving the activities ...
failed: [2622] 'The employee 'Ashman, Christian' is allowed to have 2 workdays on Sundays. With the assignment from 28.10.2012 the employee has 3 working days on Sundays.''
```

### Text colors in the Scheduling report

- Black text: Describes the scheduling steps performed by the automatic scheduling process.
- Blue text: Indicates that the target working time for an employee could not be met. This can be a problem, but is not always one. Flexible contracts allow flexible weekly working times by setting minimum, target, and maximum working time values for the week. If you use flexible hours, and the working time of the employee is between the defined minimum and target values, that may just indicate a lower requirement.
  {{ 4 | image: 'Report with blue warning messages'}}
- Red text: Indicates that a problem prevented an employee from receiving a schedule. Continue reading below for more details.
  {{ 1 | image: 'Report with red employee errors'}}

## Analyze issues in the message window in Shift Center

If a day model was not assigned, or an employee was left out from schedule optimization, you can use the message window in Shift Center to find the underlying cause:

1. Press **CTRL + K** to open the Shift Center message window at the bottom of the screen.
2. In the schedule window at the top, insert the day model that has been left out of Schedule optimization according to the Scheduling report. A pop-up or message in the message window may appear showing which rule prevents the shift from being added. In many cases, this is also the rule that has prevented the addition of the day model during the automatic scheduling process.

Note: The automatic schedule generation may work differently than the manual insertion of shifts as the {% link_new scheduling rule configuration | features/administration/create-contracts.md %} can differ per user.

{{ 2 | image: "Shift Center with Hint to Scheduling Rules" }}

## Resolve configuration errors

Scheduling errors often relate to the way you have configured injixo. Check the following settings:

### Employee settings

Go to _Administration > Scheduling > Employees_{:.breadcrumbs} and select the employee whose settings you want to check:

- In the **Staff Membership** section, make sure the **Leave Date** is not in the past.
- In the section **Miscellaneous**, check the **Shift Assignment** checkbox.
- Check that the correct activities appear in the **Activities** section. If not, assign further skills in the **Skill Levels** section. The associated activities are created automatically.
- Check if employees have personal day models assigned in the **Day Models** section. These limit the optimization to only using those day models for the employee. Remove personal day models to let the optimization use all day models that have been assigned to the planning unit.
- Make sure that available day models fit the availability restrictions of the employee defined in Availability.

### Contract and day model settings

- Assign all day models to your planning unit by adding **[All]** to the **Day Models** section of the planning unit.
- Make sure that you have calculated and saved {% link_new staff requirements | features/forecast/injixo-forecast/staff-requirement.md %} for the activity you want to schedule.
- Check if you have created the right {% link_new day models | features/administration/daymodels/daymodel-creation.md %}. Their length must suit the work time guidelines defined in the {% link_new contract | features/administration/create-contracts.md %}. Day models specify a gross total working time, while contracts only count net working time. To get the correct net working time, you may need to subtract breaks or other unpaid activities from the gross working time.
- Check other contract parameters.

### Other things to check

> Potential risk of scheduling errors
>
> Changes to scheduling rules are complex and can result in scheduling errors if done incorrectly. We do not recommend changing them yourself. If you need to change a scheduling rule, contact your consultant.

- Check your scheduling rule configurations under _WFM > Administration > System > Scheduling Rules_{:.breadcrumbs}.
- Make sure that no activities have been added that might be blocking slots in the schedule. Unpaid full-day activities used as blockers for certain days might be intended.
- Make sure that the work time pattern models of your employees contain the correct day models. Check this in _WFM > Administration > Scheduling > Work Time Pattern Models_{:.breadcrumbs}.
- Check if the value for working days per week in the contract matches the actual number of working days. You may need to specify a lower value for Minimum Number of Working Days per Week in the contract.
- Check that the rotation defined for the employee's work time pattern model does not prevent the use of the correct day models. This can happen with {% link_new work time pattern models | features/administration/work-time-pattern-models.md %} of type B, C, and D.

## Resolve common error messages

- **The employee does not have a valid contract.**<br>Make sure the right contract has been assigned to the employee and that the contract has been configured properly.<br><br>

- **No shifts available that comply with this contract.**<br>There is no combination of shifts that fits the values defined in the _Work Time Guidelines_ section of the contract. This could be due to wrong day model lengths, availabilities, skills, or employee requirements.<br><br>

- **The number of working days per week cannot be met.**<br>The resulting schedule conflicts with the allowed maximum number of days. Reasons can be a prescheduled day within the week, shifts conflicting with a person's configured availability, or a day model that has not been assigned to the planning unit or week time patterns (in case the non-scheduled person has a work time pattern model assigned).

- **The employee is locked from scheduling or is not yet/no longer part of the company.**<br>Check if the employee is barred from scheduling in the **Barred From Scheduling** section in the employee settings. Also, check that the leave date in the **Staff Membership** section is not in the past.<br><br>

- **Shift distribution is not activated.**<br>Go to _WFM > Administration > Scheduling > Employees_{:.breadcrumbs}. Click the employees, navigate to the **Miscellaneous** section, and make sure to check the **Shift Assignment** checkbox.<br><br>

- **The existing scheduling content cannot be optimised.**<br>Check if there are pre-scheduled activities in the employee's schedule which could block the automatic scheduling.<br><br>

- **This day is a holiday that does not allow the placing of activities or shifts.**<br>Deactivate the holiday mode in the settings of the respective {% link_new day type | features/administration/day-types.md %} or remove the day from the planning calendar, if you want to schedule your employees to work during a public holiday.<br><br>

- **The employee was given a scheduling model with no week models.**<br>Check the employee's work time pattern model. Assign at least one {% link_new week time pattern | features/administration/work-time-pattern-models.md %}.<br><br>

- **The day cannot be scheduled due to an existing full-day activity.**<br>Typically just a warning. The employee has a _Day Off_, _Vacation_ or another unpaid full-day activity in their schedule.<br><br>

- **The contract does not contain a value that would guarantee the week working hours.**<br>Weekly working hours and available day models must fit together. The employee must be able to meet their weekly working hours using the day models assigned to the planning unit and the number of working days in the employee's contract. Normally you can just multiply the net working hours for the day model by the maximum working days per week in the contract.<br><br>

- **You are not allowed to enter an incomplete specification of the working hours for each day of the week.**<br>If you use Working hours for each day of the week in the contract, enter a value for each day. Use 00:00 for days on which the employee should not work.<br><br>

- **The weekly working hours do not allow keeping the quota of minimum or maximum weekly working hours.**<br>Adjust the Working hours for each day of the week or the minimum or maximum work time per week in the employee's contract.<br><br>

- **One or more days cannot be scheduled due to there being no shifts with the necessary duration.**<br>Check the expected shift lengths in the contract. Create another day model that corresponds to the needed duration.<br><br> <!-- net vs. gros times? -->

- **No valid target working hours have been defined.**<br>Define valid target working times in the employee's contract.<br><br>

- **The maximum number of successive working days (not limited to the days within a week) has not been specified in the contract.**<br>Check the contract and adjust the Maximum Number of Successive Working Days (2624).<br><br>

- **The free time between shifts cannot be observed.**<br>Free time refers to the rest period between two shifts. Check the contract and adjust the value for _Rest Period Between Two Working Days_ (2601).<br><br>
