---
title: Use Time Off
description: Learn how you can manage time-off and cancellation requests.
product_label:
  - essential
  - advanced
  - enterprise
beta-feature: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
---

> Beta feature
>
> This article documents a beta feature. The documentation may not be up to date with feature behavior.

In _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span>, you can manage your people's time-off and cancellation requests:
- Approve and reject time-off requests
- Approve and reject requests to cancel already approved time off

If your organization works with [recommendations](#recommendations), you may only be able to recommend approval or rejection of pending time-off or cancellation requests, depending on your role or permissions.

On the Time Off page, you can also configure the following:
- View the personal balances and edit the time-off entitlements of your people
- Create new and edit existing time-off types
- Create new and edit existing time-off periods<br>
Learn more about the additional configuration options in [this article](https://help.injixo.com/time-off-types).

All of your actions related to time-off requests and personal balances are recorded for transparency and full traceability.

## Prerequisite
Before your people can request time off in injixo Me, you need to create [time-off types](https://help.injixo.com/time-off-types#create-a-time-off-type) with an entitlement period, and at least one [time-off period](https://help.injixo.com/time-off-types#create-a-time-off-period) with the status Published.

## Recommendations
Depending on your organization's setup and preferences, you may only be able to recommend approval or rejection for pending time-off or cancellation requests instead of being able to approve or reject them yourself. Optionally, if your role is to approve or reject requests, you may only see requests with a recommendation by another person in your organization. You can still decide against the recommendation.

By default, Time Off <span class="beta-icon">Beta</span> is set up without recommendations, and planners can view and edit all incoming requests. If your organization does not work with recommendations yet and you would like to implement a multi-layered approval process for time-off and cancellation requests, contact your injixo consultant.
If your organization does not use recommendations, you will always see all requests and can approve or reject them according to your organization's and your people's needs.
 <!-- Add information about smart recommendations when they are available on the UI -->

## Approve or reject time-off requests

1. In _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span>, go to the **Time off requested** tab.<br>To limit the displayed results, you can filter the list by selections, planning units, and time-off types.
2. In the entry with the pending request, click _Show coverage and time off_{:.doc-button} to make a better-informed decision. [Learn more](#show-coverage-and-time-off) about this functionality.
3. Click _Approve time off_{:.doc-button} or _Reject_{:.doc-button}.<br>A confirmation window opens.
4. (Optional) Add a comment.
5. Click _Confirm_{:.doc-button} or _Reject time off_{:.doc-button}.  
   The person is notified by email. Rejections are final.<br>
   injixo automatically adds approved time off to the person's schedule.

> Time off without valuation not added to schedule
>
> If you approve a time-off request for which there is no valuation, injixo does not add the approved time off to the schedule. [Learn more](https://help.injixo.com/understand-valuation) about the valuation of people's time off.

When you approve a person's time-off request, injixo adds the time off to the person's schedule. 
Depending on what the [time-off valuation is based on](https://help.injixo.com/understand-valuation), there may be differences in how injixo displays time off in the schedule.

For valuation based on a person's schedule, injixo replaces all paid activities with a paid absence activity, corresponding to the selected time-off type. This applies to the entire requested time range.

If the time-off valuation is based on a person's contract, by default, injixo uses the beginning of your planning unit's business hours as the start of the time off in the schedule, e.g. at 8&nbsp;AM on the day of the person's time-off request. This allows you to see the effect of your approval on the coverage in your planning unit. If your planning unit does not have opening hours, injixo sets the start time of the time off to midnight on the requested day.

### Show coverage and time off

To understand how approving a time-off request affects the schedule, you can use the **Show coverage and time off** functionality. When you click the _Show coverage and time off_{:.doc-button} button in a time-off request, injixo displays a view of the person's schedule for the requested time-off range, the coverage for their scheduled activities and the total number of people off during that time. The scheduled activities are highlighted in the same color that is used to highlight them in Shift Center.

The coverage indicates whether the activities are overstaffed or understaffed during the requested time. The displayed coverage is based on the current schedule and does not reflect staffing after approving the time-off request.

The number of people off is based on the approved time-off requests in Time Off <span class="beta-icon">Beta</span>. Absences that you or another planner manually entered into the schedule in Shift Center are not considered.

### Time-off requests for night shifts

By default, when people request a full day off and you approve it, injixo inserts an absence of one calendar day into their schedule if the requested [time-off type](https://help.injixo.com/time-off-types) is configured as unpaid or if it is configured as paid and you have activated the [option to replace unpaid activities and fill up non-working hours](https://help.injixo.com/#replace-unpaid-activities-and-fill-up-non-working-hours). For example, if a person requests to be off on 25&nbsp;June, their absence in injixo starts at midnight on 25&nbsp;June and ends at midnight on 26&nbsp;June, covering a total absence of 24&nbsp;hours. This default behavior applies to time-off requests for full days without night shifts or if the person has not yet been scheduled for the day.

If a person is scheduled to work a night shift that starts before midnight of one day and ends after midnight of the following day, and they want to take a day off, injixo handles their time-off request differently based on their schedule. 

The following table provides different scenarios for requested time off including a night shift:

| Scheduled night shift | Time-off request |   Time off in schedule |
|--------------------|--------------------|--------------------|--------------------|
| 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM | 26&nbsp;June | 26&nbsp;June, 6&nbsp;AM until 27&nbsp;June midnight (18&nbsp;hours) |
| 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM | 25&nbsp;June | 25&nbsp;June, midnight until 26&nbsp;June 6&nbsp;AM (30&nbsp;hours) |
| 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM and 28&nbsp;June, 10&nbsp;PM until 29&nbsp;June, 6&nbsp;AM, not scheduled on 27&nbsp;June | 25&nbsp;June until 29&nbsp;June | 25&nbsp;June, midnight until 29&nbsp;June, 6&nbsp;AM |

As shown in row&nbsp;3 of the above table, injixo can also combine the variants from rows&nbsp;1&nbsp;and&nbsp;2: If the requested time off includes a night shift at the beginning as well as at the end, the person's time off starts after the end of the first night shift and ends after the end of the last night shift.

## Cancel approved time-off requests

If you have approved a person's time off but need to cancel it again, for example, because they have already been scheduled or need to be scheduled for the respective time frame, proceed as follows:

1. Go to the **Decided** tab.<br>To limit the displayed results, you can filter the list by selections, planning units, and time-off types.
2. In the entry with the approved time off you want to cancel, click _Cancel time off_{:.doc-button}.<br>A confirmation window opens.
3. If the person has already been scheduled for the days for which you want to cancel the time off, select one of the following options:
      - **Restore history**: If a person was originally scheduled to work on the day for which their requested time off was approved, this functionality schedules them again for that shift after the time off is canceled.
      - **Blank out shift**:  If a person was originally scheduled to work on the day for which their requested time off was approved, this functionality does not restore their scheduled shift from the schedule after the time off is canceled. Instead, their shift is blanked out.
4. Click _Cancel time off_{:.doc-button}.

> injixo does not update schedules automatically
> 
> If the person has not yet been scheduled for the respective time frame, you may need to update their schedule manually in _Plan > Schedules_{:.breadcrumbs} if you want them to work on that day.

## Approve or reject a cancellation request

People cannot cancel their own time off. Instead, they can request to cancel an already approved time off.
You need to accept or reject the cancellation requests. 

1. Go to the **Cancellation requested** tab.
2. In the the cancellation request you want to approve or reject, click _Cancel time off_{:.doc-button} or _Reject_{:.doc-button}.<br>A confirmation window opens.
3. If you approve a cancellation and if the person has already been scheduled for the days for which they want you to cancel their time off, select one of the following options:
      - **Restore history**: The person remains scheduled for their shift on the selected day.
      - **Blank out shift**: The person is no longer scheduled for their shift on the selected day. You may need to update their schedule manually in _Plan > Schedules_{:.breadcrumbs}.
4. Click _Approve cancellation_{:.doc-button} or _Reject cancellation_{:.doc-button}.

> Manual update of schedule required if the person's shift cannot be restored
> 
> In some cases, injixo cannot restore a shift for a person after their time off is canceled:<br>
> - The time off was originally requested and approved in Time Off instead of Time Off <span class="beta-icon">Beta</span>.
> - The time off was valuated with 0 and was not added to the schedule.<br>
> If the shift cannot be restored or if the person has not yet been scheduled for the respective time frame, you need to update their schedule manually in _Plan > Schedules_{:.breadcrumbs} if you want them to work on that day.

## How does approved time off appear in the schedule?

There are different factors that determine how approved time off is displayed in the schedule in Shift Center and in Schedules. The following table provides an overview of the different scenarios.

| Time-off type | Requested time off | [ Fill-up functionality](https://help.injixo.com/time-off-types#replace-unpaid-activities-and-fill-up-non-working-hours) activated | Time off displayed in schedule |
|--------------------|--------------------|--------------------|--------------------|
| Paid | One full day | Yes | Equals requested time off. Here: one calendar day (from midnight until midnight) |
| Paid | One full day | No | According to [valuation](https://help.injixo.com/understand-valuation) |
| Paid | Only a part of the day, e.g. 4 hours | No | According to valuation |
| Paid | Only a part of the day, e.g. 4 hours | Yes | Equals requested time off. Here: 4 hours  |
| Paid | Several days, e.g. from 25&nbsp;June until 28&nbsp;June | Yes | Equals requested time off. Here: 25&nbsp;June, midnight until 28&nbsp;June, midnight |
| Paid | Several days, e.g. from 25&nbsp;June until 28&nbsp;June | No | According to valuation |
| Unpaid | One full day | -- | Equals requested time off. Here: one calendar day (from midnight until midnight) |
| Unpaid | Only a part of the day, e.g. 4&nbsp;hours | -- | Equals requested time off. Here: 4&nbsp;hours |
| Unpaid | Several days, e.g. from 25&nbsp;June until 28&nbsp;June | -- | Equals requested time off. Here: 25&nbsp;June, midnight until 28&nbsp;June, midnight |

If the time-off type is paid but the fill-up functionality is not activated, the schedule displays the approved time off according to the valuation. Depending on whether the valuation is based on the schedule or the contract, the following applies:

- Valuation is based on the schedule: The time off displayed in the schedule equals the scheduled paid activities. 
- Valuation is based on the contract: The time off displayed in the schedule corresponds to the person's target working hours for the requested time frame. The starting time equals the start of the planning unit's opening hours.
