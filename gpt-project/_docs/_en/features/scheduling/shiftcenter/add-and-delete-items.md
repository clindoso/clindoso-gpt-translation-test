---
title: Add and delete items
product_label:
  - advanced
  - enterprise
  - classic
description: Manually add or delete activities, day models, and other items in your employees' schedules in the Shift Center.
reddirect_from:
  - /working-with-availabilities/
  - /creating-assignments/
redirect_reason: renamed file in March 2021
---

In this article, you will learn:

- how to add activities, multiactivities, full-day activities, day models, availabilities, and comments to your schedule.
- how to add items to multiple employees at once.
- how to delete items.

Typically, you won't build a schedule manually from scratch as the optimized scheduling feature takes care of that for you. But from time to time, you might need to edit your schedule. The Shift Center allows you to do that.

New to the Shift Center? Learn {% link_new the basics | features/scheduling/shiftcenter/shift-center-overview.md %} first.

## Add an activity

You can insert one or more activities for an employee on a specific day. Your options to open the input dialog for activities in the schedule view are:

- Right-click a cell and click **Insert Activity...** in the context menu.
- Select a cell and press **CTRL + N** on your keyboard.
- Double-click a cell and click the **Activities** tab.

If you are using the {% link_new Shift Center with ActiveX | features/scheduling/shiftcenter/shift-center-overview.md | #two-shift-center-versions %} under _WFM > Scheduling > SchedulePro > Shift Center_{:.breadcrumbs}, you can also use the shortcuts **ALT + 1** to **ALT + 8** to switch between the tabs of the input dialog.

To add an activity on the _Activities_ tab, do this:

1. Choose an activity type using the **Type** field at the bottom left.
2. Click _Add_{:.doc-button} to add a new activity. A new row with the activity appears on the left. If you want to delete it again, select it and click _Delete_{:.doc-button}.
3. In the drop-down menu to the left, select an **activity**.
4. Define a **Start Time** and an **End Time**. Click a **time field**, type in the time or change the time with the arrow buttons.
5. Click _OK_{:.doc-button}.

{{ 1 | image: 'Adding Activities', '70%' }}

### Booking date and _-/0/+_ columns

The _Booking Date_ column can't be changed. Use **-/0/+** to specify if the start time or end time is on a different day. Keep **0** selected if the start or end time is on the selected day. Click **-** if the start or end time lies on the previous day. Use **+** if it lies on the following day.

## Add a multiactivity

You can insert a multiactivity for an employee on a specific day. Your options to open the input dialog for multiactivities in the schedule view are:

- Right-click a cell and click **Insert Multiactivity...** in the context menu.
- Double-click a cell and click the **Multiactivities** tab.

To add a multiactivity using the _Multiactivities_ tab, do this:

1. Click the {% icon plus %} to **expand a category** on the right.
2. Double-click a **multiactivity**. You can also select it and click the appearing **small black arrow** to the right. A new row with the multiactivity appears on the left. If you want to delete it again, select it and click _Delete_{:.doc-button}.
3. Click the {% icon plus %} on the new line to display details for the multiactivity.
4. Set a **Start time** and an **End time**. Click a **time field**, type in the time or change the time with the arrow buttons. Use **-/0/+** if needed ([see above](#booking-date-and--0-columns)).
5. Click _OK_{:.doc-button}.

{{ 3 | image: 'Adding Multiactivities', '70%' }}

## Add a day model

You can insert day models for an employee on a specific day. Your options to open the input dialog for day models in the schedule view are:

- Right-click a cell and click **Insert Day Model...** in the context menu.
- Double-click a cell and click the **Day Models** tab.

To add a day model using the _Day Models_ tab, do this:

1. To the right, you can choose between day models assigned to the planning unit (PU) and day models assigned to the employee (Emp.). Some filters on the right, such as _Sorted by Name_, _Sorted by Time_, help you quickly find the right day model. Click the {% icon plus %} to **expand a category**. The sections _Understaffed Shifts_ and _Generated Shifts_ contain day models if you work with {% link_new shift bidding | features/scheduling/shift-bidding.md %}.
2. Click the {% icon plus %} to display the individual day model.
3. Double-click the **day model**. You can also select it and click the appearing **small black arrow** to the right (or directly use a double click). A new row appears on the left. If you want to delete it again, select it and click _Delete_{:.doc-button}.
4. Click the {% icon plus %} on the new line to display details for the day model.
5. Select a **Start Time** (for variable day models only). Use **-/0/+** if needed ([see above](#booking-date-and--0-columns)).
6. Click _OK_{:.doc-button}.

{{ 2 | image: 'Adding Day Models', '70%' }}

## Add a full-day activity

Full-day activities are activities for which the option _Allow as Full-Day Activity_ has been activated. You can insert a full-day activity for an employee for one or more days. Your options to open the input dialog for full-day activities in the schedule view are:

- Right-click a cell and click **Insert Full-Day Activity...** in the context menu.
- Double-click a cell and click the **Full-Day Activities** tab.

To add a full-day activity using the _Full-Day Activities_ tab, do this:

1. Click _Add_{:.doc-button}. A new row with the full-day activity appears on the left. If you want to delete it again, select it and click _Delete_{:.doc-button}.
2. In the drop-down menu to the left, select an **activity**.
3. Set a **Start Date** and an **End Date** (maximum one year).
4. Click _OK_{:.doc-button}.

{{ 4 | image: 'Adding Full-Day Activities', '75%' }}

Check **Display All Full-Day Activities of the Year** to display all full-day activities of the selected employee for the year.

## Add an availability

You can insert an availability for an employee on a specific day. An availability specifies certain time slots on a day where an employee is available for work. If no availability has been defined, the employee is considered as _available_ for the whole day.

Adding an availability is only possible in the _Availability_ level. To show this level, click {% icon shift-center-params | icon-only %} in the action bar at the upper left and select the _Availability_ level.

{{ 5 | image: 'Availabilities in Shift Center', '80%' }}

Your options to open the input dialog for availabilities in the schedule view are:

- Right-click a cell in the _Availability_ level and click **Insert Availabilities...** in the context menu.
- Double-click a cell in the _Availability_ level and click the **Availability** tab.

You can add a standard availability using the _Availability_ tab as follows:

1. Click _Add_{:.doc-button} in the lower left to create an availability entry for the day.
2. Enter a **Start Time** and **End Time** above and click _OK_{:.doc-button} to save it.

You can also insert day model availabilities:

1. Click the {% icon plus %} in the _Sorted by Name_ or _Sorted by Time_ sections on the right. An empty list indicates that no day models of the type _Availability Period_ exist or that they are not assigned to your planning unit. Learn how to {% link_new create day model availabilities | features/administration/availabilities.md | #create-day-model-availabilities %}.
2. Double-click a multiactivity. You can also select it and click the small black arrow that appears on the right. A new row with the multiactivity appears on the left. If you want to delete it again, select it and click _Delete_{:.doc-button}.
3. Click the {% icon plus %} on the new line to display the details for the Availability.

   {{ 7 | image: 'Shift Center Availabilities Input Dialog', '70%' }}

4. Set a **Start Date** and an **End Date**. Use **-/0/+** if needed ([see above](#booking-date-and--0-columns)).
5. Click _OK_{:.doc-button}.

> Day models of type _Availability Period_ overwrite other availabilities
>
> If you use day models of the type _Availability Period_ in Shift Center or via shift sequences, they will overwrite any availabilities that have been assigned in the employee configuration under _WFM > Administration > Scheduling > Employees_{:.breadcrumbs} and also availabilities which have been entered in injixo Me by the agent.

## Add comments

You can add comments with a maximum length of 250 characters on each level for each person. You cannot copy comments but you can [add the same comment for multiple employees](#add-items-to-multiple-employees-at-once). Add a single comment as follows:

1. Double-click a cell and switch to the **Comment** tab.
2. Enter a **comment**.
3. Click _OK_{:.doc-button}.  
   The commented day cell is highlighted by a black border.  
   To display the comment in a tooltip, move your mouse over the cell.  
   To edit or remove the comment, double-click a commented cell.

Comments entered in the Schedule level will be visible in injixo Me if there is a scheduling period with the status Published or Shift bidding enabled.



## Add items to multiple employees at once

You can add identical items (activities, multiactivities, full-day activities, day models, and even comments) for several employees on the same day at once:

1. Double-click a **day cell**.
2. Click the **Employees** tab.
3. Check the **checkboxes** of the employees that you want to add the item for. Choose _All_{:.doc-button} or _None_{:.doc-button} to select or deselect all.
   {{ 11 | image: 'select employees', '75%' }}
4. Click the **tab** where you want to enter data, i.e. _Activities_, _Multiactivities_, _Day Models_, _Full-Day Activities_, or _Comments_.
5. Add the **items** you want to assign.
6. Click _OK_{:.doc-button}. The items are now added to the schedule of each selected employee.
   {{ 12 | image: 'Reset previous planning status', '75%' }}

Note: You cannot use the option to restore previous schedule states on the _History_ tab for several employees at once.

> Look out for scheduling rule violations
>
> As a user with _Admin access_ or the role _Planner_, your schedules are updated regardless of any scheduling rule violations. Check the {% link_new **message window** | features/scheduling/shiftcenter/shift-center-overview.md | #message-window %} at the bottom for errors. For other user roles, changes violating rules are not processed at all.

## Delete items

> Data is immediately deleted without prior confirmation. The previous state can only be restored individually per employee and day on the _History_ tab.

To delete a _single activity or day model_:

- Right-click it and select **Delete Entry**. You can also click the item and press **CTRL + E**. Or double-click a cell to open the input dialog, select the data row of the item you want to delete and press _Delete_{:.doc-button}.
- Click the **day cell** and press **Del** or **CTRL + L**.

To delete all data for a _single day_:

- Right-click the day cell and select **Delete ALL Entries**.
- Click the **day cell** and press **Del** or **CTRL + L**.

To delete all activities and day models for _multiple days and employees_ at once:

1. Tip: Configure the {% link_new display parameters | features/scheduling/shiftcenter/shift-center-overview.md | #choose-the-time-range-and-levels %} to only show the time period and levels where you want to delete data.
2. Select the **cells** you want to delete.
3. Right-click **the selected cells** and select **Delete All Entries**. Or press **Del** or **CTRL + L** on your keyboard.
