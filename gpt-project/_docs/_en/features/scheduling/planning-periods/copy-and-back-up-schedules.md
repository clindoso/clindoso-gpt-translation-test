---
title: Copy or back up schedules
product_label:
  - classic
description: Copy or back up your schedules and other elements in the different scheduling levels of injixo (SchedulePro).
toc: false
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/what-are-planning-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/delete-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/batch-replace-an-activity.md
---

In this article, you will learn how to copy or back up your schedules and other elements in the different scheduling levels of injixo.

To do this, you will use planning periods. Read the article {% link_new What are Planning periods? | features/scheduling/planning-periods/what-are-planning-periods.md %} first.

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you are using injixo Advanced WFM or Enterprise WFM, use the function {% link_new Copy level content | features/scheduling/schedules/schedules-copy-level-content.md %} under _Plan > Schedules_{:.breadcrumbs} instead.

## Levels in injixo

In injixo you can use different levels for scheduling purposes. Levels can contain, among other elements, the activities or day models used for scheduling, shift requests or employee availability data. You can copy the data of a level, e.g. your complete schedule or parts of it, within the same level or to another level. This can be helpful to speed up your scheduling process.

You can create a backup by copying the complete schedule to another level. Backups are recommended from time to time, especially before you try out new scheduling methods.

## Select or create a planning period

1. Go to _WFM > Scheduling > SchedulePro > Planning Periods_{:.breadcrumbs}.
2. Choose a **Planning Unit**.
3. Choose the **Type** _Standard_.
4. For **Selection** choose **[All]**.
5. Click _Apply_{:.doc-button}.
6. Find a planning period that contains the date range for which you want to copy schedules. It doesn't have to match the date range exactly.
7. Click _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon}.
8. Select the **Status** _Locked_ to make sure that employees cannot access the schedule.
9. Click _Ok_{:.doc-button}.

If there is no suitable planning period in the list, create a new one:

1. Click the {% icon item-add %} in the action bar.
2. Use **Valid From** and **Valid To** to define the time period for which you want to copy schedules.
3. Select the **Status** _Locked_ to make sure that employees cannot access the schedule.
4. Click _Ok_{:.doc-button}.

## Copy or back up a schedule

Select a planning period with the date range in which you want to copy or back up schedules:

1. Click the planning period. A menu opens to the right.
2. Click _Copy_{:.doc-button} in the section _Level_.
3. Optional: Change the **Start Date** and **End Date** if you want to further limit the timeframe. If you don't change anything, it will use the time frame of the planning period.
4. Optional: Change the **Employee Selection** method if you want to run the process for certain employees only. Choose one or more of your selections or employees from the list. Press the _Shift_ or _CTRL_ key to select multiple entries at once.
5. For **Source Level**, select the scheduling level from which you want to copy or back up data.
6. Optional: Check **Clear contents after copying** to delete the existing content from the source level.
7. For **Target Level**, select the scheduling level to which you want to copy the data.
8. Change the **Start Date** for the _Target Level_ to copy data into a different time frame. For example, copy the data of an old schedule to a future period on the same level. In this case _source level_ and _target level_ are the same.
9. To start the copy or backup job, click _Ok_{:.doc-button}.

{{ 3 | image: 'Level copy dialog', '50%' }}
