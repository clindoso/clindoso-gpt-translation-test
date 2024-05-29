---
title: Insert shift sequences
description: Schedule repeating rotations of shifts, activities, or availabilities with Shift Sequences (SchedulePro).
promote-service: new-planner-training
product_label:
  - classic
---

Shift sequences are fixed, repetitive sequences of shifts, activities, or availabilities. They are used to schedule regular recurring tasks or availabilities of your employees. Before inserting them, you need to {% link_new create shift sequences | features/administration/shift-sequences.md %} and {% link_new assign to your employees | features/administration/employee-overview.md | #optional-scheduling-settings %}.

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you are using injixo Essential WFM, Advanced WFM or Enterprise WFM, use the function {% link_new Insert Shift Sequences | features/scheduling/schedules/schedules-insert-shift-sequences.md %} under _Plan > Schedules_{:.breadcrumbs}.

## Set parameters

Using the following dialog in _WFM > Scheduling > SchedulePro > Insert Shift Sequences_{:.breadcrumbs} you can insert shift sequences:

{{ 1 | image: 'Insert shift sequences', '75%' }}

1. Select **a start and end date** (maximum: 2 years), a planning unit, a selection if necessary, and the target level.
2. Confirm your parameters with _Create Employee List_{:.doc-button}. The [employee list](#employee-list) appears.
3. Select individual employees with the **checkbox in front of the personnel number** or use the first checkbox in the upper left corner to select all employees.
4. Click the _Insert Shift Sequences_{:.doc-button}.

The shift sequences are inserted. At the end, another window appears, this may contain messages detailing errors during the insertion process.

## Options

In the _Options_{:.menu-item} section there are various options for deleting existing schedule content:

| Option                           | Explanation                                                                                                                                                     |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Delete full-day activities       | Existing full-day activities of employees are deleted from the target level before insertion and replaced by the selected shift sequence.                       |
| Delete availability periods      | Existing availability periods of employees are overwritten by the selected shift sequence.                                                                      |
| Delete all activities and shifts | Existing activities and all shifts of employees on the target level are deleted and replaced by the selected shift sequence; availability periods are retained. |

The options are only considered when inserting the first shift sequence of an employee, i.e. if this option is activated, the schedule content is only deleted when inserting the first shift sequence.

Existing full-day activities are generally replaced by full-day activities from a shift sequence if the existing entries are not of the type `Absence`, `Illness`, `Vacation`, or `Meeting`. To prevent full-day activities (for example, vacation) from being overwritten by partial-day activities or shifts from a shift sequence, activate scheduling rule _2645_{:.id-label}_Disallow overwriting of full-day activities with shifts or activities_.

Other scheduling rules can influence the result:

- _2602_{:.id-label} _Check maximum duration of each activity as specified in the employee's contract_
- _2611_{:.id-label} _Check employee availability_
- _2613_{:.id-label} _Check maximum number of shifts on one day as specified in the employee's contract_
- _2648_{:.id-label} _Write protection for activities in the Shift Center_

## Employee list

The employee list, which appears after clicking on _Create Employee List_{:.doc-button}, contains information about every shift sequence of your employees.

{{ 2 | image: 'Employee Shift sequences' }}

Besides the personnel number and the name of the employee, the list also contains information about the shift sequence itself (name, length, validity). The sequence, employee line, and reference date information comes from the employee's assignment. Deleted shift sequences that are still assigned to employees appear in italics.

### Order

When inserting several shift sequences per employee, these are inserted in ascending order in the schedule.
Whether the content of a shift sequence is actually replaced by the content of another shift sequence depends on the data to be inserted, on the existing schedule content, on the selected options, and on the check using scheduling rules.

### Reference date

For each day of the week, injixo needs to choose between the pattern for week 1, week 2, etc. The reference date provides a fixed point for this. The first day of the shift sequence is always inserted relative to the reference date. This is defined when the shift sequence is assigned to the employee and should always be on the first day of the week. By default, the start of the week is set to either Sunday or Monday, depending on your region. If you need to set it to another day, contact your consultant.

Example: The period you wish to insert a 3-week shift sequence for is 9th - 29th July. The shift sequence starts on 9th July, but the reference date is set to 2nd July. On July 9th, the 8th day of the shift sequence is inserted, which is the start of week 2 of the sequence. Week 3 of the shift sequence will start on July 23rd.
