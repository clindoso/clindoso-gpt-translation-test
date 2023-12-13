---
title: Allow employees to swap shifts
toc: false
description: Allow employees to swap shifts with each other in injixo Me (SchedulePro).
product_label:
  - classic
redirect_from: /enable-employees-to-exchange-shifts/
redirect_reason: file renamed in March 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shift-bidding.md
---

In this article, you will learn how to allow employees to swap (exchange) shifts with each other.

To do this, you will use planning periods. Read the article {% link_new What are planning periods? | features/scheduling/planning-periods/what-are-planning-periods.md %} first.

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you are using injixo Essential WFM, Advanced WFM, or Enterprise WFM, use {% link_new Scheduling Periods | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} under _Plan > Schedules_{:.breadcrumbs} instead.

## Allow employees to swap shifts

To allow shift swaps, you first have to activate the option in injixo Me. Click _Me_{:.breadcrumbs} in the main navigation and turn on **Shift swap**.

1. Go to _WFM > Scheduling > SchedulePro > Planning Periods_{:.breadcrumbs}.
2. Select the **Planning Unit** for which you want to allow shift swaps among employees.
3. Select the **Type** _Standard_.
4. Pick a **Selection** if you want to limit the option to swap shifts to a certain group of agents. Otherwise, keep **[All]**.
5. Click _Apply_{:.doc-button}.
6. Select the planning period with the date range for which you want to allow shift swaps and click _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon} in the action bar. If there is no suitable planning period in the list, create a new one by clicking the {% icon item-add %}.

In both cases, the following dialog appears:

{{ 3 | image: 'Define Planning Period', '60%' }}

1. Use **Valid From** and **Valid To** to define the time period for which you want to allow shift swaps.
2. Select the **Status** _Enabled_.
3. Optional: Set a **Deadline**. Until that date, employees can swap shifts.
4. Confirm with _Ok_{:.doc-button}.

Your employees can swap shifts in injixo Me for the time period defined by the planning period. This is possible for all {% link_new activities | features/administration/activity-examples.md %} which are configured as **Exchangeable with shift swap**.
