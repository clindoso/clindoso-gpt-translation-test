---
title: View and approve shift swap requests
product_label:
  - essential
  - advanced
  - enterprise
description: View and approve or reject pending shift swap requests, as well as view past swaps.
archive_ref: 20210802-en-shift-exchange-overview
redirect_from:
  - /shift-exchange-overview/
redirect_reason: Updated filename on 19 April 2023
---

In injixo Me, users with the agent role can {% link_new swap their shifts | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #swap-shifts %} or days off with each other, both on the same day and on different days.

This is how shift swap works:

1. A person offers a shift in injixo Me.
2. Other people can see the posted shift and offer their own shift in exchange.
3. The person who offers the shift selects the counter offer that best fits their needs.
4. injixo automatically confirms the selection and creates the approval request if applicable.
5. A user with admin access or the planner role reviews, approves, or rejects the requested swap. To allow automatic approvals, change the setting _48152_{:.id-label} _Exchange Mode_ from 0 to 1.

To see how people can swap shifts in injixo Me, read {% link_new Swap shifts with your colleagues | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #swap-shifts %}.

Tip: In the {% link_new Team Calendar | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %}, people can see their colleagues' working hours and ask for shift swaps.

## Prerequisites

A person with the agent role can offer a shift if:

- {% link_new Shift swap is activated | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} in injixo Me.
- all activities in a shift are {% link_new exchangeable with shift swap | features/administration/activity-types-and-properties.md %}.
- a {% link_new scheduling period | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} with status Shift bidding enabled, Published, or Finished exists.
- the configured deadline for the planning period has not been reached yet.
- the value configured in setting _48151_{:.id-label} allows shift swaps. The setting value sets the number of days from the current date until which a shift swap is possible without creating a risk to the current schedule.
- they have view access to injixo Me.

## Approve or reject swaps

To review, approve, or reject shift swap requests in _Plan > Schedules_{:.breadcrumbs}, proceed as follows:

1. Click _Scheduling actions_{:.doc-button}.
2. Select **Approve shift swaps**.
3. Select a **planning unit**.
4. (Optional) Select a **selection**.
5. Select a **date range**. If you have not already selected a date range in Schedules, the date range defaults to today + seven days.
6. Check the **checkboxes** next to one or more entries you want to approve or reject. Use the checkbox at the top to select all entries at once.
7. Click _Approve selected_{:.doc-button} or _Reject selected_{:.doc-button}.  
   After pending requests have been approved or rejected, they will move to the Information tab.

The Exchange Statistics report under _WFM > Monitoring > Reports_{:.breadcrumbs} lists the status of swaps (as _Offered_, _Not edited_, _Rejected_, and _Approved_) for a configurable period.

## Generate a list of past swaps

On the **Approve shift swaps** page, the Information tab shows which person has swapped which shift and at what time. The list shows approved, rejected and cancelled requests. For more information on cancelled requests, hover over the {% icon info_circle %}.

## Shift swap settings

Under _WFM > Administration > System > Settings_{:.breadcrumbs}, there are several settings to adapt the shift swap process to the needs of your business:

- _48151_{:.id-label} _Barred period for the Shift Exchange_: Number of days from the current date when a swap is no longer possible (default: 3 days).
- _48152_{:.id-label} _Exchange Mode_: Configure whether a user with admin access or the planner role must approve shift swaps between people (Defaults to 0 for approval, choose 1 for automatic swaps without approval).
- _48153_{:.id-label} _Exchange Entitlement_: Swaps between people of one planning unit (value 0, default), a selection (value 1) or different planning units (value 2, not recommended).
- _48555_{:.id-label} _Exchanging workdays against free days_: Allow people to swap shifts for days off (default: 0, no).
- _48556_{:.id-label} _Exchanging different days_: Allow people to swap shifts on different days of the week (default: 0, no).
- _48999_{:.id-label} _Enable specific checks for subactivities of multi-activities in association with scheduling rule 2605_: injixo checks the skills for each subactivity when exchanging multiactivities (default: 0, no check).

## When shift swaps are blocked

People can see and swap shifts offered in injixo Me if the swap request complies with the rules of their contract (contractual working hours) and if they have the necessary skills.

To find out why the swap is prevented in injixo Me, simulate the swap in the _Shift Center_{:.menu-item}. When copying and pasting the shifts, the {% link_new message window | features/scheduling/shiftcenter/shift-center-overview.md | #message-window %} at the bottom of the screen will display the {% link_new scheduling rule | features/administration/create-contracts.md | #scheduling-rules %} and the reason, e.g. wrong skills or other contractual constraints.
