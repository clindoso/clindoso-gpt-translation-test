---
title: Batch replace an activity
product_label:
  - classic
description: Replace all instances of an activity with another activity in an existing schedule (SchedulePro).
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/what-are-planning-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/copy-and-back-up-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/delete-schedules.md
---

In this article, you will learn how to batch replace an activity with another activity in an existing schedule.

To do this, you will use planning periods. Read the article {% link_new What are Planning Periods? | features/scheduling/planning-periods/what-are-planning-periods.md %} first.

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you are using injixo Advanced WFM or Enterprise WFM, use the function {% link_new Replace activities | features/scheduling/schedules/schedules-replace-activities.md %} under _Plan > Schedules_{:.breadcrumbs} instead.

## Select or create a planning period

1. Go to _WFM > Scheduling > SchedulePro > Planning Periods_{:.breadcrumbs}.
2. Choose a **Planning Unit**.
3. Choose the **Type** _Standard_.
4. For **Selection** choose **[All]**.
5. Click _Apply_{:.doc-button}.
6. Find a planning period that contains the date range for which you want to batch replace the activity. It doesn't have to match the date range exactly.
7. Click _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon}.
8. Select the **Status** _Locked_ to make sure that employees cannot access the schedule.
9. Click _Ok_{:.doc-button}.

If there is no suitable planning period in the list, create a new one:

1. Click the {% icon item-add %} in the action bar.
2. Use **Valid From** and **Valid To** to define the time period in which you want to replace an activity.
3. Select the **Status** _Locked_ to make sure that employees cannot access the schedule.
4. Click _Ok_{:.doc-button}.

## Batch replace an activity

Select a planning period with the date range for which you want to perform a batch replacement:

1. Click the planning period. A menu opens to the right.
2. Click _Exchange_{:.doc-button} in the section _Activity_.
3. Optional: Change the **Start Date** and **End Date** if you want to further limit the timeframe. If you don't change anything, it will use the time frame of the planning period.
4. Optional: Change the **Employee Selection** method if you want to run the process for certain employees only. Choose one or more of your selections or employees from the list. Press the _Shift_ or _CTRL_ key to select multiple entries at once.
5. For **Levels**, check one or more checkboxes to select the levels in which you want to perform the activity replacement.
6. For **Search**, select the activity you want to replace.
7. For **Replace**, select the activity that you want to replace the other activity with.
8. To start the replacement, click _Ok_{:.doc-button}.

{{ 2 | image: 'Exchange activities', '50%' }}
