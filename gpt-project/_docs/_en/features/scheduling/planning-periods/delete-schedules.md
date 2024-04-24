---
title: Delete schedules
product_label:
  - classic
description: Delete schedules from one or more scheduling levels for a specific date range (SchedulePro).
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/what-are-planning-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/batch-replace-an-activity.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/copy-and-back-up-schedules.md
---

In this article, you will learn how to

- Delete schedules (activities and day models) from one or more scheduling levels for a specific date range.
- Limit the deletion to specific employees.

To do this, you will use planning periods. Read the article {% link_new What are Planning Periods? | features/scheduling/planning-periods/what-are-planning-periods.md %} first.

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you are using injixo Advanced WFM or Enterprise WFM, use the function {% link_new Empty level | features/scheduling/schedules/schedules-empty-levels.md %} under _Plan > Schedules_{:.breadcrumbs} instead.

## Select or create a planning period

1. Go to _WFM > Scheduling > SchedulePro > Planning Periods_{:.breadcrumbs}.
2. Choose the **Planning Unit**.
3. Choose the **Type** _Standard_.
4. For **Selection** choose **[All]**.
5. Click _Apply_{:.doc-button}.
6. Find a planning period that contains the correct date range for which you want to delete schedules. It doesn't have to match the date range exactly.
7. Click _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon}.
8. Select the **Status** _Locked_ to make sure that employees cannot access the schedule.
9. Click _Ok_{:.doc-button}.

If there is no suitable planning period in the list, create a new one:

1. Click the {% icon item-add %} in the action bar.
2. Use **Valid From** and **Valid To** to define the time period for which you want to delete schedules.
3. Select the **Status** _Locked_ to make sure that employees cannot access the schedule.
4. Click _Ok_{:.doc-button}.

## Delete schedules for a specific date range

> Be careful when setting your parameters - you cannot undo a schedule deletion.

> Do not delete time-off requests
>
> Approved {% link_new time-off requests | features/scheduling/time-off/vacation-absences-management.md %} are only stored in the Schedule level. If you have approved time-off requests, don't delete your schedule as explained here. Because this would also delete the approved time-off requests in the chosen date range. Instead, delete the shifts manually.

1. Click a **planning period** of type _Standard_ that contains the data range in which you want to delete schedules. A menu opens to the right.
2. Click _Delete_{:.doc-button} in the section _Level_.
3. If needed, change the **Start Date** and **End Date** to further limit the timeframe that will be deleted.
4. Optional: Change the **Employee Selection** method if you want to delete only the data of certain employees. You can choose one or more of your selections or one or more employees from the list. Press the _Shift_ or _CTRL_ key to select multiple entries at once.
5. Select the **Level** from which you want to delete data.
6. To delete the data, click _Ok_{:.doc-button}. There is no further security prompt.

{{ 4 | image: 'Delete level dialog', '50%' }}
