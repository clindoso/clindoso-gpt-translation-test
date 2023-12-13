---
title: View and Approve Exchange Requests
description: View and approve or reject pending shift swap requests, as well as view past swaps.
archive_ref: 20210802-en-shift-exchange-overview
archived_date: 2021-08-02
---

In this article, you will learn:

- what a shift swap is and how it works.
- how to approve or reject shift swaps.
- how to generate a list of past swaps.
- which settings impact shift swaps.

## What is a shift swap?

With injixo Me, employees can swap their shifts or days off with each other, both on the same day and on different days.

At a high level, the swap process works as follows:

1. An employee offers a shift in injixo Me.
2. Other employees can see the posted shift and offer their own shift in exchange.
3. The offering employee selects the counter offer that best fits their needs.
4. injixo automatically confirms the selection and, if applicable, creates the approval request.
5. A user with _Admin access_ or the role _Planner_ reviews, approves or rejects the requested swap. To activate automatic approvals, you can use value 1 in setting _48152_{:.id-label} _Exchange Mode_.

For the employee perspective, read the article {% link_new Swap shifts with your colleagues | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #swap-shifts %}. Note: inviting colleagues to swap shifts is only possible in injixo Advanced and Enterprise WFM. Tip: The {% link_new Team Calendar | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} allows employees to see the working hours of colleagues and ask them to swap shifts.

## Prerequisites

Employees can offer a shift, if:

- the {% link_new shift swap feature is activated | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} in injixo Me.
- all activities in a shift are configured as {% link_new **Exchangeable with shift swap** | features/administration/activity-types-and-properties.md %}.
- a {% link_new planning period | features/scheduling/planning-periods/what-are-planning-periods.md %} with status _Enabled_, _Information_, or _Closed_ exists.
- the configured _Deadline_ for the planning period has not been reached yet.
- the value configured in setting _48151_{:.id-label} allows it. The setting value sets the number of days from today when a shift swap is no longer possible to avoid a risk to the current schedule.

## Approve or reject swaps

To review, approve or reject shift swap requests, you can follow the below steps:

1. Go to _WFM > Scheduling > SchedulePro > Exchange Overview_{:.breadcrumbs}.
2. Select a **Start Date** and an **End Date**. _Exchanges Barred Until_ shows the date until which no swaps can take place based on setting 48151.
3. Select a **Planning Unit**.
4. Select a **Selection** (optional).
5. Under _Options_, select the **Approval** option to approve/reject pending requests.
6. Click on _Create Employee List_{:.doc-button} to display the list. The message _No exchange pairs with exchange requests or other exchange data are available_ will appear, if there are no requests available for your selected parameters.
7. Check the checkbox before one or more entries you want to approve or reject.
8. Click _Approve_{:.doc-button} or _Reject_{:.doc-button}.

   {{ 3 | image: 'Exchange overview in SchedulePro', '80%' }}

The report _Exchange Statistics_ under _WFM > Monitoring > Reports_{:.breadcrumbs} lists the status of swaps (as _suggested_, _not yet started_, _rejected_, and _approved_) for a configurable period.

## Generate a list of past swaps

To understand which employee swapped which shift and when, you can review the list of past swaps as follows:

1. Go to _WFM > Scheduling > SchedulePro > Exchange Overview_{:.breadcrumbs}.
2. Select a **Start Date** and an **End Date**. The date under _Exchanges Barred Until_ shows the date based on setting 48151.
3. Select a **Planning Unit**.
4. Select a **Selection** (optional).
5. Under _Options_, select the **Information** option.
6. Click on _Create Employee List_{:.doc-button} to display the list of past swaps. The message _No exchange pairs with exchange requests or other exchange data are available._ will appear, if there are no requests available for your selected parameters.

The list will contain the following symbols in the _Status_ column:

{{ 1 | image: 'Overview of the different exchange symbols', '60%' }}

## Shift swap settings

Under _WFM > Administration > System > Settings_{:.breadcrumbs}, there are several settings to adapt the shift swap process to the needs of your business:

- _48151_{:.id-label} _Barred period for the Shift Exchange_: Number of days from the current date when a shift swap is no longer possible (Default: 3 days).
- _48152_{:.id-label} _Exchange Mode_: Configure whether a user with _Admin access_ or the role _Planner_ must approve shift swaps between employees (Defaults to 0 for approval, choose 1 for automatic swaps without approval).
- _48153_{:.id-label} _Exchange Entitlement_: Swaps between employees of one planning unit (value 0, default), a selection (value 1) or different planning units (value 2, not recommended).
- _48555_{:.id-label} _Exchanging workdays against free days_: Allow employees to swap shifts for days off (default: no).
- _48556_{:.id-label} _Exchanging different days_: Allow employees to swap shifts on different days of the week (default: no).
- _48999_{:.id-label} _Enable specific checks for subactivities of multiactivities in association with scheduling rule 2605_: injixo checks the skills for each subactivity when exchanging multiactivities (default: no check).

## When would shift swaps be blocked?

Employees can swap shifts if their request complies with the rules of the corresponding contracts (daily working hours, skills, weekday working hours, etc.). As an example, if an employee offered a shift in injixo Me, another employee will not see it if this shift falls outside their contractual working hours. Learn more about {% link_new scheduling rules | features/administration/create-contracts.md | #scheduling-rules %}.

If you are unsure why a swap cannot take place, simulate the swap in the _Shift Center_{:.menu-item} by copying and pasting the shifts. This way, you can see which scheduling rules prevent the swap, as a failing swap will show the scheduling rule and the exact reason for the violation here, for example wrong skills or working times.
