---
title: What are scheduling periods?
description: Learn what scheduling periods are used for and how to display, edit and delete them (Schedules).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
---

Scheduling periods are time spans of a few days, weeks, or months. Use them if you want to:

- allow employees to {% link_new see their schedules | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %}.
- allow employees to {% link_new swap shifts | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} with each other.
- allow {% link_new shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %} for employees.

To allow employees to request time off, use {% link_new time off periods | features/scheduling/time-off/time-off-periods.md %}.

## Status

Every scheduling period has a status. The status unlocks or restricts certain options for employees for the date range of the scheduling period. Typically, you will change the status of a scheduling period multiple times during the scheduling process, for example after you have finalized the schedule or when the time period for submitting shift requests has expired.

| Status                | Explanation                                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unpublished           | Employees cannot see the published schedule, cannot participate in {% link_new shift bidding                                                                                            | features/scheduling/schedules/schedules-shift-bidding.md %}, and cannot swap shifts with each other. Use this status if you don't want to release the schedule to your employees yet. |
| Shift bidding enabled | Employees can see the published schedule, participate in shift bidding, swap shifts with each other, and see {% link_new comments                                                       | features/scheduling/shiftcenter/add-and-delete-items.md                                                                                                                               | #add-comments %} that have been entered in the Schedule level. This status cannot be set if the scheduling period has a deadline that has already expired. |
| Published             | Employees can see the published schedule, can swap shifts with each other, and can see comments that have been entered in the Schedule level. They cannot participate in shift bidding. |
| Finished              | This status indicates that the schedule is final. Employees can still swap shifts with each other.                                                                                      |

## Display scheduling periods

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling periods_{:.doc-button}.
3. Select a **planning unit** from the first drop-down menu. Start typing to filter the list.
4. (Optional) To filter scheduling periods, pick a **Selection** from the second drop-down menu. Start typing to filter the list.  
   If there are scheduling periods for your selected planning unit (and selection), they will be displayed. Learn more about the tabs and table columns below.

### Ongoing and Expired tabs

All scheduling periods of the chosen planning unit and/or selection will appear in the tabs below:

- **Ongoing**: Scheduling periods that lie partly or completely in the future.
- **Expired**: scheduling periods that lie completely in the past.

Both tabs will be empty if you have not created a scheduling period yet, or if the filter criteria do not match existing scheduling periods.

### Table columns

The table of scheduling periods has six columns:

- **Status**: the status of the scheduling period
- **Selection**: the selection of employees who are affected by the scheduling period
- **Valid from**: the start date of the scheduling period
- **Valid to**: the end date of the scheduling period
- **Deadline**: the date by which employees can participate in shift bidding and swap shifts
- **Inherited from**: when you create a scheduling period for a parent planning unit, its status is inherited by all child planning units. The column shows the name of the parent planning unit if applicable.

You can sort the list by any column by clicking on the respective **column header**. To reverse the sort order, click again.

## Create scheduling periods

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling periods_{:.doc-button}.
3. Click _Create scheduling period_{:.doc-button} in the upper right.
4. Select a planning unit, a selection, a date range, a deadline (optional), and a [status](#status) for the scheduling period.
5. To save the scheduling period, click _Save_{:.doc-button}.

## Edit scheduling periods

To update the status of a scheduling period, select a new status from the drop-down menu in the **Status** column. The new status is automatically saved.

To edit all settings of a scheduling period (including the status), hover over it and click the {% icon pencil %} on the right.

## Delete scheduling periods

To delete one or more scheduling periods, check the **checkboxes** to the left of the list entries. The checkbox on top selects all displayed entries. Click _Delete selected_{:.doc-button} below the list.
