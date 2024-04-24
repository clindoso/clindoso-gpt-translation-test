---
title: Allow time-off requests and sick leave
toc: false
description: Allow employees to request time off or add sick leave in injixo Me.
product_label:
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shift-bidding.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/target-work-accounts.md
---

In this article, you will learn how to allow employees to request time off or add sick leave.

To do this, you will use planning periods. Read the article {% link_new What are planning periods? | features/scheduling/planning-periods/what-are-planning-periods.md %} first.

> This article is about _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> If you are using injixo Essential WFM, Advanced WFM, or Enterprise WFM, use {% link_new Scheduling Periods | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} under _Plan > Schedules_{:.breadcrumbs} and {% link_new Time-Off Periods | features/scheduling/time-off/time-off-periods.md %} under _Plan > Time Off_{:.breadcrumbs} instead.

## Allow time-off requests and sick leave

To allow _time-off requests_ or sick leave, you first have to activate the option in injixo Me. Click _Me_{:.breadcrumbs} in the main navigation and turn on **Time Off Requests**.

1. Go to _WFM > Scheduling > SchedulePro > Planning Periods_{:.breadcrumbs}.
2. Choose the **Planning Unit** you want to allow time-off requests for.
3. As **Type**, choose one of your requestable activities. Learn how to configure an {% link_new activity as **Requestable in Me** | features/administration/activities.md %}. Then add the activity to the {% link_new planning unit | features/administration/create-and-manage-planning-units.md %}.
4. Choose a **Selection** if you want to limit time-off requests to a certain group of agents. Otherwise, keep **[All]**.
5. Click _Apply_{:.doc-button}.
6. If a matching planning period exists, select it and click the _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon} button in the action bar. If there is no suitable planning period in the list, create a new one by clicking the {% icon item-add %} button in the action bar.

In both cases, the following dialog appears:

{{ 3 | image: 'Define Planning Period', '60%' }}

1. Use **Valid From** and **Valid To** to define a time period, e.g. three months or the entire year. A planning period for vacation or other absences is usually longer than just a week.
2. Select the **Status** _Enabled_.
3. Optional: Set a **Deadline**. Until that date, employees can request time off.

Your employees will now see the option to request time off in injixo Me for the time period defined by the planning period. As a planner, you can then {% link_new approve or reject | features/scheduling/time-off/vacation-absences-management.md %} time-off requests.
