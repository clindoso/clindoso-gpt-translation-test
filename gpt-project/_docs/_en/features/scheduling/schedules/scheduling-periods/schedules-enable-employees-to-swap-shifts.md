---
title: Allow people to swap shifts
toc: true
description: Allow people to swap shifts with each other in injixo Me (Schedules).
product_label:
  - essential
  - advanced
  - enterprise
redirect_from: /schedules-enable-employees-to-exchange-shifts/
redirect_reason: file renamed in March 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
---

To allow people to swap shifts with each other in injixo Me, set up scheduling periods. A status, a time period, and a deadline date allow you to control the date range in which people can swap shifts.

New to scheduling periods? Start learning {% link_new the basics | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %}.

## Prerequisites

- Click _Me_{:.breadcrumbs} in the main navigation and activate the option **Shift swap** (requires admin access or user with a user role with Configure permission for Me).
- All activities in your day models must be configured as {% link_new Exchangeable with shift swap | features/administration/activity-types-and-properties.md | #activity-properties %}.
- Create a scheduling period and set a status other than Unpublished.

## Allow shift swaps for existing scheduling periods

Select the scheduling period for which you want to allow shift swap:

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling periods_{:.doc-button}.
3. Select the **planning unit** in which you want to activate shift swaps.
4. (Optional) Pick a **selection** if you want to allow only a certain group of people to swap shifts. If you want to allow all people in the planning unit to swap shifts with each other, leave the field empty.
5. Select a scheduling period with the date range for which you want to activate shift swaps. Note the date defined as deadline. People can swap shifts until that date.
6. Select the status **Published** from the drop-down menu in the Status column.<br>
   The status is saved automatically.<br>
   People can now {% link_new swap shifts in injixo Me | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md %}.

> Note
>
> Also status Finished allows shift swaps. The status Shift bidding enabled additionally allows to request shifts in {% link_new shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %}.

## Create a new scheduling period

If there is no scheduling period for the selected date range yet, create a new one:

1. Click _Create scheduling period_{:.doc-button}.
2. Select a **planning unit**.
3. (Optional) Pick a **selection** if you want to allow only a certain group of people to swap shifts. If you want to allow all people in the planning unit to swap shifts with each other, leave the field empty.
4. Set a **date range** to define the time period for which you want to activate shift swaps.
5. (Optional) Set a **deadline**. People can swap shifts until that date.
6. Select the status **Published**.
7. Click _Save_{:.doc-button}.<br>
   People can now {% link_new swap shifts in injixo Me | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md %}.
