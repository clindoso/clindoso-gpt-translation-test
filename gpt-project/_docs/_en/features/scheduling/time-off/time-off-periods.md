---
title: Time-off periods
description: Learn what time-off periods are and how to work with them.
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-entitlement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-absences-management.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md
---

Time-off periods are time ranges for which people can request time off in injixo Me, e.g. January 2023-December 2024. 

Time-off periods only support the activity types Absence, Vacation, and Illness. The activities must be configured as {% link_new Requestable in Me | features/administration/activities.md %} and {% link_new assigned to your planning unit | features/administration/create-and-manage-planning-units.md %}. Create a separate time-off period for each activity that people can use to request time off.

In injixo Me, people can request time off for different reasons, e.g. vacation or illness. People can only create time-off requests for time ranges that are included in a time-off period with the status Published. 

Note: To allow people to request time off, go to _Me_{:.breadcrumbs} in the main navigation and activate the **Time Off Requests** option.

Use {% link_new scheduling periods | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} to allow people {% link_new to see their schedules | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %}, {% link_new exchange shifts | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}, and {% link_new bid on shifts | features/scheduling/schedules/schedules-shift-bidding.md %}.

### Status

Every time-off period has a status that determines whether it is available for people in injixo Me. You set a status when you create the time-off period, but you can change the status as often as you want to.

| Status      | Explanation                                                                                                                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unpublished | People cannot see the time-off period or use it to submit time-off requests. Use this status until you are ready for people to see the time-off period and submit time-off requests.                                                                                |
| Published   | People can see the time-off period in injixo Me and use it to submit time-off requests. The time-off period appears in injixo Me with a white background. You cannot set this status if the time-off period has an expired deadline. |

## Manage time-off periods

1. Go to _Plan > Time Off_{:.breadcrumbs}.
2. Click _Time-off periods_{:.doc-button} on the top right.
3. Select a **Planning unit** to filter the list.
4. Optional: Choose a selection and/or an activity.

The list will show the relevant time-off periods divided into two tabs:

- Ongoing: Time-off periods whose date range lies partly or completely in the future.
- Expired: Time-off periods whose date range lies completely in the past.

Both tabs show a table with six columns. The **Inherited from** column is only relevant when a time-off period was created for a parent planning unit. In that case, all child planning units inherit the time-off period and the column shows the name of the parent planning unit.

To sort a column, click the table header. To reverse the sorting order, click again.

## Create a time-off period

1. Go to _Plan > Time Off_{:.breadcrumbs}.
2. Click _Time-off periods_{:.doc-button} on the top right.
3. Click _Create time-off period_{:.doc-button} on the top right.
4. Fill in the fields. 
  Remember that people can only request time off if you select the status Published.
5. Click _Save_{:.doc-button}.

## Edit a time-off period

If you want to change the status of a time-off period

1. Go to _Plan > Time Off_{:.breadcrumbs}.
2. Click _Time-off periods_{:.doc-button} on the top right. 
3. To change the status, use the drop-down in the **Status** column. The changed status will be saved automatically.  
  To edit other data, hover over the list item that you want to edit and click the {% icon pencil %} on the right.
4. Edit the relevant data.
5. Click _Save_{:.doc-button}.

## Delete a time-off period

1. Go to _Plan > Time Off_{:.breadcrumbs}.
2. Click _Time-off periods_{:.doc-button} on the top right. 
3. Check one or more checkboxes on the left. The checkbox on the header selects all items.
4. Click _Delete entries_{:.doc-button}.
