---
title: What are planning periods?
description: Use planning periods to publish schedules, enable time-off requests, perform mass updates to your schedules, and more (SchedulePro).
product_label:
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-employees-to-see-their-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shift-bidding.md
---

In this article, you will learn:

- what planning periods are and what they are used for.
- how to display, edit and delete planning periods.

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you are using injixo Essential WFM, Advanced WFM, or Enterprise WFM, use {% link_new Scheduling Periods | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} under _Plan > Schedules_{:.breadcrumbs} and {% link_new Time-Off Periods | features/scheduling/time-off/time-off-periods.md %} under _Plan > Time Off_{:.breadcrumbs} instead.

## What are planning periods used for?

Planning periods are time periods of a few days, weeks or months up to one year. They are used for various planning purposes (see below), thus their name.

### Types

There are two types of planning periods: standard planning periods and activity-based planning periods.

{{ 2 | image: 'Different planning period types', '80%' }}

Use _standard planning_ periods if you want to:

- allow employees {% link_new to see their schedules | features/scheduling/planning-periods/enable-employees-to-see-their-schedules.md %}.
- allow employees {% link_new to exchange shifts | features/scheduling/planning-periods/enable-employees-to-swap-shifts.md %} with each other.
- activate {% link_new shift bidding | features/scheduling/shift-bidding.md %} for employees.
- edit or {% link_new calculate target work accounts | features/scheduling/planning-periods/target-work-accounts.md %} for employees.
- {% link_new batch replace one activity | features/scheduling/planning-periods/batch-replace-an-activity.md %} in your schedule with another.
- {% link_new copy or back up schedules | features/scheduling/planning-periods/copy-and-back-up-schedules.md %}.
- {% link_new delete schedules | features/scheduling/planning-periods/delete-schedules.md %}.

Use _activity-based planning periods_ if you want to allow employees to {% link_new request time off or to add sick leave | features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md %}. Activity-based planning periods use activities that have been configured as **Requestable in Me**. These are activities of the type _Absence_, _Vacation_, or _Illness_. You have to create a separate planning period for each activity, e.g. one for adding vacation requests and one for adding sick leave.

### Status

The status of a planning period determines how employees can interact with it. Typically, you will change the status of a planning period multiple times during the scheduling process, such as after you have finalized the schedule or once the shift bidding period is over.

| Status      | Explanation                                                                                                                                                                                                                            |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Locked      | Employees cannot see the published schedule, cannot participate in {% link_new shift bidding                                                                                                                                           | features/scheduling/shift-bidding.md %}, cannot exchange shifts with each other, and cannot request time off. Use this status if you don't want to release the schedule to your employees yet. |
| Enabled     | Employees can see the published schedule, can participate in shift bidding, can request time off, and can exchange shifts with each other. This status _cannot be set_ if the planning period has a deadline that has already expired. |
| Information | Employees can see the published schedule and can exchange shifts with each other. They _cannot_ participate in shift bidding and cannot request time off. This status is only relevant for planning periods of the type _Standard_.    |
| Closed      | Use this status to indicate that the schedule is final. Employees can still exchange shifts with each other.                                                                                                                           |

As you can see, planning periods are used in many different ways. Click one of the links in the list above to get detailed instructions for the different use cases.

## Filter and display planning periods

If you go to _WFM > Scheduling > SchedulePro > Planning Periods_{:.breadcrumbs}, you will initially see no planning periods. You first have to set a filter to choose the planning periods you want to display.

1. Choose a **Planning Unit**.
2. Choose a **Type**.
3. Choose a **Selection** (optional). The selection field is not available in injixo Essential WFM.
4. Click _Apply_{:.doc-button} to display the corresponding planning periods. If there are no matches with the filter criteria, nothing will be shown.

{{ 1 | image: 'Planning Periods', '80%' }}

The _inherited_ column flags planning periods of parent planning units. You can calculate time accounts and target work accounts on parent planning units for all child planning units or for each one individually. When you create a planning period for a parent planning unit, its status is inherited by any child planning units.

## Create a new planning period

To create a new planning period, use the _![add button](/assets/img/common/item-add.gif)_{:.doc-button-icon} button from the action bar. A dialog to set the time period and status of the new planning period appears. Since this information depends on what you want to achieve with the planning period, you can find more information in the articles at the top on the different use cases.

## Edit a planning period

The typical reason to edit a planning period is to update its status. To edit a planning period, select it. Then click the _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon} button from the action bar.

## Delete a planning period

To delete a planning period, use the _![delete button](/assets/img/common/item-delete.gif)_{:.doc-button-icon} button from the action bar.
