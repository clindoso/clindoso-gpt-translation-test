---
title: Modify items
product_label:
  - advanced
  - enterprise
  - classic
description: Copy, paste, move, expand, and shorten schedule items, undo your actions, convert day models to activities, and revoke full-day activities.
redirect_from: /changing-assignments/
redirect_reason: renamed file in March 2021
---

In this article, you will learn how to:

- copy and paste schedule items, i.e. activities and day models.
- move, expand, and shorten items.
- undo your actions.
- convert day models to activities.
- revoke full-day activities to restore schedules.

Typically, you won't build a schedule manually from scratch as the optimized scheduling feature takes care of that for you. But from time to time, you might need to edit your schedule. The Shift Center allows you to do that.

New to the Shift Center? Learn {% link_new the basics | features/scheduling/shiftcenter/shift-center-overview.md %} first.

## Copy and paste

You can cut, copy, and paste one or multiple day cells or single items in the Shift Center.

### Day cells

The entire day is copied if you copy one or more day cells. If you paste them, the content of the target day cell(s) is overwritten.

1. Select a cell or multiple cells by pressing **SHIFT**.
2. Right-click your selection to open the context menu. Then select **Copy** or **Cut**. You can also use the keyboard shortcuts **CTRL + C**, **CTRL + X**.
3. Select one or more other cells.
4. Right-click your selection and select **Paste**. You can also press **CTRL + V**.

### Single items

1. Expand a day by clicking on the column header of the day.
2. Right-click an item within the day that you want to copy, e.g. an activity and select **Copy**. You can also click the item and press **CTRL + C**.
3. Right-click one of the expanded day cells of an employee where you want to paste the activity and select **Paste**. You can also click an expanded day cell of an employee to select it and then press **CTRL + V**.

## Move, expand, and shorten elements

You can move, extent or shorten elements in the schedule using the mouse in an expanded day. First, open the cell where you want to change elements:

1. To expand a day, click a header of a day column.
2. To zoom in and out, click the tiny black arrow buttons in the column header.
3. Click the cell containing the activities or day models you want to modify.

### Variable day models

You can move day models of type _Variable Shift_ according the available starting positions. You can move breaks in day models if they are defined as a break corridor. Hover your mouse over an item until a **white double arrow** pointing left and right appears. Click, hold and then drag the item to move it.

### Activities

In case of activities, different options to edit an item exist:

- Move an item to the left or the right without changing its length:

  1. Hover your mouse over an item until a **white double arrow** pointing left and right appears.
  2. Click, hold and then drag. If there are neighboring items, they are shortened or extended accordingly.

- Shorten and expand the items to the left and the right:
  1. Hover your mouse over the end of an item or the contact point between two items. A **black double arrow** appears.
  2. Click, hold and then drag.

### Tips

- Press **CTRL** before moving an item to detach it from neighboring items.
- Press **Shift** to move all existing items together without changing them.
- When you move, extend or shorten items, a yellow tooltip appears below the item that shows the resulting start time, end time and length of the item. This allows you to position items precisely.

### Use the input dialog

Alternatively, you can use the input dialog to modify items. To open the input dialog, double-click a cell. Click one of the tabs called **Activities**, **Multiactivities**, **Day Models** or **Full-Day Activities**.

- To modify the _start or end time_, click a **time field**, type in the new time or change the time with the arrow buttons.
- Use **-/0/+** to specify if the start time or end time of the activity is on a different day. Keep **0** selected if the start or end time is on the selected day. Click **-** if the start or end time lies on the previous day. Use **+** if it lies on the following day.
- To change the _activity or day model_, click an **activity or day model name** to the left. Select the activity or day model you want to use from the drop-down menu.

## injixo automatically resolves editing conflicts

When you modify or add new activities or day models with the input dialog, the time ranges of new and old items may overlap at first. When you close the window with _OK_{:.doc-button}, injixo resolves these conflicts for you in the following way:

If you insert or edit a _single activity_ that creates an overlap, the activity will overwrite (parts of) other shifts within the overlap period.

If you are inserting or editing _several activities_, all activities including the ones that were scheduled previously will be re-inserted in the order of their start times. In the case of overlaps, any activities that start later will overwrite (parts of) those that start earlier. In this scenario, existing schedule content may (partly) overwrite newly inserted activities.

Open the input dialog again to check if the resulting schedule fits your needs. Here is an example:

Existing activities

- 08:00 to 09:00 `Sales`
- 09:00 to 11:00 `Service`

New activity

- 07:00 to 10:00 `Training`

Edited activity

- 09:00 to 12:00 `Service`

Resulting activities:

- 07:00 to 08:00 `Training`
- 08:00 to 09:00 `Sales`
- 09:00 to 12:00 `Service`

Moveable corridor elements, such as corridor elements for breaks in day models, stay on top of new or edited non-corridor items. Learn more about such {% link_new corridor elements | features/administration/daymodels/daymodel-basics.md | #fixed-elements-vs-corridors %}.

## Undo your actions

If you are using the {% link_new ActiveX-free Shift Center | features/scheduling/shiftcenter/shift-center-overview.md | #two-shift-center-versions %} under _Plan > Shift Center_{:.breadcrumbs}, you can undo your last change by pressing **CTRL + Z**.

If you are using the Shift Center with ActiveX under _WFM > Scheduling > SchedulePro > Shift Center_{:.breadcrumbs}, you can click the **button with the blue arrow** <!-- screenshot? --> in the action bar or press **CTRL + Z**. The option to undo a single action expires after logout or after opening another menu item.

### Display and revert previous actions

Double-click a **day cell** and click the tab **History**. The first row displays the current state of the employee schedule for the selected date. The other rows display previous versions of the day model or activities in descending time order.

{{ 1 | image: 'Reset previous planning status', '75%' }}

To restore a previous version for the chosen day and employee:

1. Click the **numbered button** to the left of an entry. You cannot restore rows with elements which have already been deleted in the administration.
2. Click _OK_{:.doc-button} to restore the data in the selected row.

You can only restore the history of a single employees and a single day at a time.

## Split day models into their activities

You can split a day model into the sequence of its individual activities. Afterwards, you can edit the activities of the day model separately. Automatic scheduling processes like the _Fully Optimized Plan_ always split shifts into their individual activities.

To split a day model into its activities:

1. Right-click a **day model**.
2. Choose **Dissociate Items from Shift Concept** in the context menu.

Note: The _Job Optimization_ and the _Create optimized schedules_ functionality also convert day models into activities. Movable corridor elements for flexible placement of breaks always remain corridor elements, when setting 48134 is activated (default).

## Revoke full-day activities to restore schedules

You can use full-day activities to add vacations and other full-day absences to the schedule. When inserted, the full-day activities replace the original employee schedule. However, you can revoke the manually added full-day activity to restore the original employee schedule:

1. Select **one or more cells** which contain full-day activities. Right-click the selected cells.
2. Select **Revoke Full-Day Activity** in the context menu. This restores the original employee schedules.
