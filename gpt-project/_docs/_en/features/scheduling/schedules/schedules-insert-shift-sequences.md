---
title: Insert shift sequences
product_label:
  - essential
  - advanced
  - enterprise
description: In Schedules, you can schedule repeating rotations of shifts, activities, or availabilities with shift sequences.
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
---

Shift sequences are fixed, repetitive sequences of shifts, activities, or availabilities. You can insert shift sequences for selected employees, e.g. to schedule regular recurring tasks or availabilities.

## Prerequisites

Before you can insert shift sequences into your schedule, you need to do the following:

- {% link_new Create | features/administration/shift-sequences.md %}  at least one shift sequence
- {% link_new Assign | features/administration/employee-overview.md | #assign-a-shift-sequence %} the shift sequence(s) to a person

## Filter shift sequences

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. From the **Scheduling Actions** drop-down menu on the right, select _Insert shift sequences_{:.doc-button}.
3. Select a planning unit.
4. (Optional) Pick a selection.
5. Set a time period.

   > You can insert shift sequences for up to two years.

   The **Overview** section shows shift sequences that match your filter. The table displays data that is set when you assign an existing shift sequence to a person:

   | Option                 | Description                                                                                                                                                                                                                                                                       |
   | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
   | Personnel number       | The person's unique identifier                                                                                                                                                                                                                                               |
   | Name                   | The name of the person to whom the shift sequence is assigned                                                                                                                                                                                                                                                                 |
   | Shift Sequence         | The name of the assigned shift sequence                                                                                                                                                                                                                                                    |
   | Sequence               | Defines the order in which shift sequences are inserted if a person has multiple shift sequences. Shift sequences with lower values are inserted first and may be overwritten by subsequent shift sequences.                                                                  |
   | Employee row           | Defines which row of the shift sequence is used for the person.                                                                                                                                                                                                               |
   | Reference date         | Start day of the shift sequence. If you use a shift sequence longer than seven days to plan several people, set different reference dates for them. This way, they are assigned the first week of the shift sequence for different weeks, and are not all assigned the same shift at the same time.
   | Valid from<br>Valid to | The period for which the shift sequence has been assigned to the person. Outside the configured validity period, the shift sequence is not inserted into the person's schedule. If the validity period of the shift sequence lies completely within the selected time period, it is not displayed. |

## Insert shift sequences

1. To select an employee, check the checkbox next to their row. To select all employees, check the checkbox in the header row.
2. (Optional) From the **Options** drop-down menu at the bottom of the overview table, select how existing schedules should be handled when inserting shift sequences.

   | Option                           | Description                                                                                         |
   | -------------------------------- | --------------------------------------------------------------------------------------------------- |
   | Delete full-day activities       | Full-day activities are deleted. Non full-day activities are retained.                              |
   | Delete availability periods      | Availability periods are deleted.                                                                   |
   | Delete all activities and shifts | All activities and and shifts are deleted from the target level. Availability periods are retained. |

   > The selected options are only applied while inserting a person's first shift sequence.

3. (Optional) Change the target level. By default, the Schedule level is selected.
4. Click _Insert shift sequences_{:.doc-button}.

> Note  
>  
> If deleted day models are still present in a shift sequence, they are still inserted into the schedule (marked with a dashed border in Schedules and Shift Center).

## Access result reports

In the **History** section, you can access reports for the current and previous runs of inserting shift sequences. Click the **View details** link to check why shifts or activities could not be inserted. A four-digit ID at the beginning of a row refers to a scheduling rule that blocks the shift sequence from being inserted.

To delete entries from the **History** section, check the checkboxes next to an entry and click _Delete entries_{:.doc-button}. To select all entries at once, check the checkbox at the top.

## Prevent overwriting of scheduled activities

By default, when you insert full-day activities into the schedule using shift sequences, injixo overwrites other full-day activities in the schedule, e.g. time off. To prevent this, activate scheduling rule _2645_{:.id-label} _Disallow overwriting of full-day activities with shifts or activities_.

To protect partial-day activities of the types Absence, Illness, Vacation, or Meeting from being overwritten, activate scheduling rule _2648_{:.id-label} _Write protection for activities in the Shift Center_.

> Note  
>
> Shift sequences are inserted with the currently logged-in user account. Scheduling rules can be configured differently per user. If you have several accounts, check whether you are logged in with the correct account.

## Validity periods

When you insert shift sequences, validity periods may have an impact on the results.

To determine the time period during which a day model can be scheduled, you can limit the validity period of your day models by setting a Valid from and Valid to date. After inserting shift sequences, you may see the following error message in the result report: \[2151\] The day models for the shift 'day model name' is invalid for the booking day dd/mm/yyyy.

In each shift sequence, you can set a time period in which the shift sequence can be inserted. By default, shift sequences are valid at any time. If you limit the time period, the shift sequence will not be inserted outside the defined time period. You will not receive an error message in that case.

Validity periods in personal day models (day models assigned to employees) do not affect shift sequences. Such day models in shift sequences are still inserted.

Note: Deleted day models that are still part of a shift sequence are inserted and marked with a dotted border in Shift Center and Schedules. You will not receive an error message in that case.
