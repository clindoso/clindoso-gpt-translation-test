---
title: Allow people to swap shifts
toc: false
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

To allow people to swap shifts with each other, use scheduling periods. New to scheduling periods? Learn {% link_new the basics | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} first.

To activate shift swaps, activate the option in injixo Me first. You need to have configure permission to Me. Click _Me_{:.breadcrumbs} in the main navigation and activate the option **Shift swap**.

Select the scheduling period for which you want to allow shift swap:

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling periods_{:.doc-button}.
3. Select the **planning unit** in which you want to activate shift swaps.
4. (Optional) Pick a **selection** if you want to allow only a certain group of people to swap shifts. If you want to allow all people in the planning unit to swap shifts with each other, leave the field empty.
5. Find an existing scheduling period with the date range for which you want to activate shift swaps. Click the **drop-down** menu in the Status column and change the status to published.

Note: The status shift bidding enabled allows your team members to swap shifts, and to request shifts in shift bidding. The status published only allows shift swaps.

If there is no scheduling period for the selected date range yet, create a new one:

1. Click _Create scheduling period_{:.doc-button}.
2. Select a **planning unit**.
3. (Optional) Pick a **selection** if you want to allow only a certain group of people to swap shifts. If you want to allow all people in the planning unit to swap shifts with each other, leave the field empty.
4. Set a **date range** to define the time period for which you want to activate shift swaps.
5. (Optional) Set a **deadline**. People can swap shifts until that date.
6. Select the status **Published**.
7. To confirm, click _Save_{:.doc-button}.

Your team members can now swap shifts in injixo Me for the time period defined by the scheduling period until the deadline. This is possible for the {% link_new activities | features/administration/activity-examples.md %} configured as {% link_new exchangeable with shift swap | features/administration/activity-types-and-properties.md | #activity-properties %}.
