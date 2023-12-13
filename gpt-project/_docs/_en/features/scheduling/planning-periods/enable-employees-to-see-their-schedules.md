---
title: Allow employees to see their schedules
toc: false
description: Allow employees to see their schedules in injixo Me (SchedulePro).
product_label:
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md
---

In this article, you will learn how to allow employees to see their schedules in injixo Me.

To do this, you will use planning periods. Read the article {% link_new What are planning periods? | features/scheduling/planning-periods/what-are-planning-periods.md %} first.

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you are using injixo Essential WFM, Advanced WFM, or Enterprise WFM, use {% link_new Scheduling Periods | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} under _Plan > Schedules_{:.breadcrumbs} instead.

## Allow employees to see their schedules

1. Go to _WFM > Scheduling > SchedulePro > Planning Periods_{:.breadcrumbs}.
2. Choose the **Planning Unit** you want to publish schedules for.
3. Choose the **Type** _Standard_.
4. Set the **Selection** to **[All]** unless you want to limit the publishing of the schedules to a certain group of agents. I you want to limit the publishing, choose the respective selection.
5. Click _Apply_{:.doc-button}.
6. Select the planning period with the date range for which you want to publish schedules and click _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon} in the action bar. If there is no planning period for that date range yet, create a new one. Click the {% icon item-add %}.

In both cases, the following dialog appears:

{{ 3 | image: 'Define Planning Period', '60%' }}

1. If you created a new planning period, use **Valid From** and **Valid To** to define the time period for which you want to publish the schedules.
2. Select the **Status** _Information_ if you want your employees to only see the schedules. If the planning period is also used for {% link_new shift bidding | features/scheduling/shift-bidding.md %} and {% link_new shift swaps | features/scheduling/planning-periods/enable-employees-to-swap-shifts.md %} between agents, choose _Enabled_.
3. Optional: Set a **Deadline** (only for shift bidding and shift swaps). Schedules will still be visible afterwards.
4. Confirm with _Ok_{:.doc-button}.

Your employees will now see their schedules in injixo Me for the time period defined by the planning period.
