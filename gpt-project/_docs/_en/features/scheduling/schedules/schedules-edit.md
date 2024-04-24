---
title: Edit your schedule
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Edit, add, and delete activities and shifts in your schedule (Schedules feature).
---

In this article, you will learn how to:

- edit, add, and delete activities in your schedule using _Plan > Schedules_{:.breadcrumbs}.
- copy, cut, paste, and delete complete shifts directly in the schedule.

New to Schedules? Learn {% link_new the basics | features/scheduling/schedules/schedules-overview.md %} first.

## Add activities

1. Double-click a cell in the schedule to open the edit view.
2. Optional: Select an **Activity Type** on the left to predetermine which type of activity you want to add. The default is set to _All_.
3. Click _Add new Activity_{:.doc-button} to create a new activity or click _Add new Full-Day Activity_{:.doc-button} to create a new full-day activity. A new row with the activity is added to the right. Multiactivities are marked by the _Symbol_{:.multiactivity-icon}, full-day activities with a day status are marked by the _Symbol_{:.daystatus-icon}.
4. In the row of the new activity, choose an activity from the **drop-down menu**. If you have selected an activity type in step 2, you will only be able to choose activities of that type.
5. Adjust the **Start Time** and **End Time** for the new activity. You can also change the date if you want to specify that the activity started the day before or ended the day after. Repeat the steps 2 to 5 to add more activities.
6. Click _Save_{:.doc-button}.

   {{ 1 | image: 'Add activities and multiactivities'}}

## Edit activities

1. Double-click a cell to open the edit view.
2. Change the values for **Activity**, **Start Time**, or **End Time** on the right.
3. Click _Save_{:.doc-button}.

   {{ 2 | image: 'Edit activity', '80%' }}

A small yellow dot next to the _Edit_ or _History_ tabs on the left indicates unsaved changes in the respective tab.

Sometimes it happens that you have unsaved changes in both tabs. If you now want to save the changes in one of the tabs, a warning message appears that indicates that in this case the changes in the other tab will be lost:

{{ 4 | image: 'Unsaved changes in other tabs modal', '50%'}}

> Edit or delete individual days within a multiday vacation block
>
> If you want to edit or delete individual days within a multiday block of approved vacation activities in the _Schedule_ level, you always need to delete the entire vacation activity block first. Afterwards, you can restore individual days via the {% link_new History | features/scheduling/schedules/schedules-history.md %} tab.

## Delete activities

1. Double-click a cell to open the edit view.
2. On the right, click the **X** button next to an activity to mark it for deletion. Click again if you want to revert this. You can also click _Delete all Activities_{:.doc-button} to mark all rows at once.
3. Click _Save_{:.doc-button}. This deletes all activities marked for deletion.

   {{ 3 | image: 'Delete activity', '80%'}}

## Modify shifts directly in the schedule

You can copy, cut, paste, and delete complete shifts directly in the schedule using keyboard shortcuts:

| Shortcut      | Function                                                                             |
| ------------- | ------------------------------------------------------------------------------------ |
| **CTRL + C**  | Copies the shift in the selected cell. You can now paste it in other cells.          |
| **CTRL + X**  | Cuts the shift in the selected cell. You can now paste it once in another cell once. |
| **CTRL + V**  | Pastes the copied shift into the selected cell.                                      |
| **CTRL + L**  | Deletes the content of the selected cell.                                            |
| **←**/**Del** | Deletes the content of the selected cell.                                            |
| **ESC**       | Removes the selection from the selected cell.                                        |

Note: The keyboard shortcuts don't work in the detailed view of a day.
