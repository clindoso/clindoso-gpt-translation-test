---
title: Edit schedules
toc: true
redirect_from:
  - /schedules-history
redirect_reason: /schedules-history/ was deleted in May 2024 and its content moved to this article
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to manage activities and shifts in your schedule.
---

In _Plan > Schedules_{:.breadcrumbs}, you can add, edit, and delete activities in your schedule. You can also copy, cut, paste, and delete shifts.

New to Schedules? Learn {% link_new the basics | features/scheduling/schedules/schedules-overview.md %} first.

## Manage activities

### Add activities

1. In _Plan > Schedules_{:.breadcrumbs}, set the {% link_new filters | features/scheduling/schedules/schedules-overview.md | #filter-data %} and the {% link_new view options | features/scheduling/schedules/schedules-overview.md | #schedule-area %} for your schedule.
2. In a person's row, double-click the hour or day cell to which you want to add an activity.
3. (Optional) Filter the activities by type. In the page that opens, select an **Activity Type** from the drop-down menu. The default option is **All**.
4. Click _Add new Activity_{:.doc-button} to create a new activity for which you can define a start and end time or _Add new Full-Day Activity_{:.doc-button} to create a new {% link_new full-day activity | features/administration/activity-types-and-properties.md | #activity-properties %}.<br>
   injixo creates a row with the new activity. An <em class="multiactivity-icon"></em> icon marks the multiactivities. A <em class="daystatus-icon"></em> icon marks the activities with a full-day status.
5. In the new row, select an activity from the drop-down menu. If you selected an activity type in step 3, now you can only select activities of that type.
6. If your activity is not a full-day activity, enter the **Start Time** and **End Time** for the new activity.<br>If an activity starts the day before, or ends the day after, you can change the date of its start time or end time.<br>To add more activities, repeat steps 4 to 6.
7. At the bottom left, click _Save_{:.doc-button}.

### Edit activities

1. In _Plan > Schedules_{:.breadcrumbs}, set the {% link_new filters | features/scheduling/schedules/schedules-overview.md | #filter-data %} and the {% link_new view options | features/scheduling/schedules/schedules-overview.md | #schedule-area %} for your schedule.
2. In a person's row, double-click the hour or day cell with the activity or activities that you want to edit.
3. In the page that opens, edit the activity information.
4. At the bottom left, click _Save_{:.doc-button}.

### Delete activities

1. In _Plan > Schedules_{:.breadcrumbs}, set the {% link_new filters | features/scheduling/schedules/schedules-overview.md | #filter-data %} and the {% link_new view options | features/scheduling/schedules/schedules-overview.md | #schedule-area %} for your schedule.
2. In a person's row, double-click the hour or day cell with the activity or activities that you want to delete.
3. Click the {% icon x %} next to the activity or activities that you want to delete. Click the icon again to deselect the activity or activities. <br> To delete all activities currently displayed on the page, click _Delete all Activities_{:.doc-button}.
4. At the bottom left, click _Save_{:.doc-button}.

### Edit or delete individual days within a block of time-off activities

To edit or delete individual days within a block of approved time-off activities in the Schedule level, proceed as follows:

1. Delete the whole block of time off-time activities following the procedure above.
2. Restore individual days within the block in the **History** tab. Learn how to do it in the [dedicated section below](#see-and-restore-schedule-changes-in-the-history-tab).

## Manage shifts

Use keyboard shortcuts to edit the shifts directly in the schedule.

1. In _Plan > Schedules_{:.breadcrumbs}, set the {% link_new filters | features/scheduling/schedules/schedules-overview.md | #filter-data %} and the {% link_new view options | features/scheduling/schedules/schedules-overview.md | #schedule-area %} for your schedule.
2. Select a time frame between three and 32 days from the date picker.
3. In a person's row, click the hour or day cell with the shift that you want to edit.
4. Use the keyboard shortcuts listed in the table below.

| Shortcut      | Function                                                                             |
| ------------- | ------------------------------------------------------------------------------------ |
| **CTRL + C**  | Copies the shift in the selected cell. You can then paste the shift in other cells.  |
| **CTRL + X**  | Cuts the shift in the selected cell. You can then paste the shift in one other cell. |
| **CTRL + V**  | Pastes the copied shift into the selected cell.                                      |
| **CTRL + L**  | Deletes the content of the selected cell.                                            |
| **←**/**Del** | Deletes the content of the selected cell.                                            |
| **ESC**       | Deselects the selected cell.                                                         |

## See and restore schedule changes in the History tab

You can see and restore past changes to the schedule made by you or other people with the planner role. You can restore a schedule change for an individual person for one day at a time.

1. In _Plan > Schedules_{:.breadcrumbs}, set the {% link_new filters | features/scheduling/schedules/schedules-overview.md | #filter-data %} and the {% link_new view options | features/scheduling/schedules/schedules-overview.md | #schedule-area %} for your schedule.
2. In a person's row, double-click an hour or day cell.
3. In the page that opens, click the **History** tab.<br>At the top right of the page, you can see the person's current shift. Below, you see a table with five columns:
   - Checkbox column
   - **Name**: The name of the person who edited the shift
   - **Date and time**: The date and time of the changes
   - **Action**: A short description of the changes. In some cases, changes made by internal systems appear as **Unknown**.
   - Shift overview column: The effects of the changes on the shift
4. In the first column, check the checkbox next to the entry with the changes that you want to restore.
5. At the bottom left, click _Save_{:.doc-button}.

> Changes in the Edit and History tabs
>
> Save the changes you make in one tab before making changes in the other one. A yellow dot on the tab indicates unsaved changes. If you have unsaved changes in both tabs, and then save the changes in one of the tabs, the changes in the other tab will not be saved.
