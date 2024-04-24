---
title: Request time off
description: Learn how you can request time off and request cancellation of already approved time off in injixo Me.
product_label:
  - essential
  - advanced
  - enterprise
beta-feature: true
---

> Beta feature
>
> This article documents a beta feature. The documentation may not be up to date with feature behavior.

Time off represents absences from the workplace. The amount and types of time off that you can take depend on your organization's regulations and on your contract.

Go to _Me > Time Off_{:.breadcrumbs} to do the following:
- Request time off
- See the time-off types available to you (e.g. Sickness or Vacation)
- Check your personal balance, i.e. how much paid time off you have left.
- View existing time-off requests
- Request cancellation of approved time off

If you request time off for a day on which you are scheduled to work or would regularly work according to your contract, you will be compensated for your time off and the respective amount of days or hours will be deducted from your entitlement. If you want to know how much paid time off you can still take, [view your personal balance](#view-your-personal-balance). You can also request unpaid time off by choosing an unpaid time-off type in your time-off request. You will not be compensated for unpaid time off but you can use it to ensure you do not get scheduled, e.g. if you have an important appointment outside of work.

In your time-off calendar, you can see the days with approved time off (in green) or requested time off (in dark gray). Rejected time-off requests are highlighted in brown.<br>
On days that are highlighted in light gray, you cannot request time off, e.g. because your organization has not published a time-off period for those days yet.
If there is already a published schedule, the days on which you are scheduled to work are highlighted in bold formatting.

## View your personal balance

1. Select a time-off type from the drop-down menu in the top left. 
2. The sections **Pending**, **Remaining** and **Taken** show the current status for the selected time-off type:<br>
   - **Pending**: time off you have requested that has not yet been approved or rejected
   - **Remaining**: time off that you can still request within the entitlement period
   - **Taken**: time off that you have requested and that has already been approved

## Request time off for full days

1. Select a time-off type from the drop-down menu in the top left.
2. Click _Request time off_{:.doc-button}.
3. Define the length of your time off:<br>
**Start date**/**End date**: If you only want to take one day off, select the same date in both date range pickers.
4. (Optional) Enter a comment.
5. Click _Request time-off_{:.doc-button}.

You cannot edit a time-off request after submitting it. If you need to edit your time-off request, delete the pending time-off request and create a new one.

## Request time off for partial days

1. Select a time-off type from the drop-down menu in the top left.
2. Click _Request time off_{:.doc-button}.
3. Select the day for your time off:<br>
**Start date**/**End date**: Select the same date in both date range pickers or two consecutive dates if your requested time off starts before and ends after midnight.
4. Activate the **Request a part of the day** option.
5. Define the length of your time off:<br>
**Start time**/**End time**: Depending on your organization's settings, time-off requests for a partial day might be rounded to half a day or a full day.
6. (Optional) Enter a comment.
7. Click _Request time-off_{:.doc-button}.

You cannot edit a submitted time-off request. If you need to edit details of your time-off request, delete the pending time-off request and create a new one.

## Time-off requests for night shifts

By default, when you request a full day off and it is approved, injixo will insert an absence of one calendar day into your schedule. For example, if you request to be off on 25&nbsp;June, your absence in injixo starts at midnight on 25&nbsp;June and ends at midnight on 26&nbsp;June. This default behavior applies to time-off requests for days without night shifts or if you have not been scheduled yet for the day.

If you are scheduled to work a night shift that starts before midnight of one day and ends after midnight of the following day, and you want to take a day off, injixo handles your time-off request differently based on your schedule. For example, if you want to take a day off on 26&nbsp;June and you are scheduled to work from 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM, your day off does not begin at midnight but after the end of your scheduled shift, i.e. at 6&nbsp;AM. It ends at midnight of 26&nbsp;June, covering a total absence of 18&nbsp;hours.
If you want to take a day off on 25&nbsp;June and you are scheduled to work from 25&nbsp;June, 10PM until 26&nbsp;June, 6AM, your day off does not end at midnight but after the end of your scheduled shift, i.e. at 6AM, covering a total absence of 30&nbsp;hours.

injixo can also combine these two variants: If the time period of your requested time off includes a night shift at the beginning as well as at the end, your time off starts after the end of the first night shift and ends after the end of the last night shift.

For a quick overview of the different scenarios, see this table:

| Scheduled night shift | Time-off request |   Time off in schedule |
|--------------------|--------------------|--------------------|--------------------|
| 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM | 26&nbsp;June | 26&nbsp;June, 6&nbsp;AM until 27&nbsp;June midnight (18&nbsp;hours) |
| 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM | 25&nbsp;June | 25&nbsp;June, midnight until 26&nbsp;June 6&nbsp;AM (30&nbsp;hours) |
| 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM and 28&nbsp;June, 10&nbsp;PM until 29&nbsp;June, 6&nbsp;AM, not scheduled on 27&nbsp;June | 25&nbsp;June until 29&nbsp;June | 25&nbsp;June, midnight until 29&nbsp;June, 6&nbsp;AM |
| no scheduled night shift | 26&nbsp;June |  26&nbsp;June, midnight until 27&nbsp;June, midnight |

If you want to take specific hours off instead of a full day, use a [partial-day time-off request](#request-time-off-for-partial-days).

## Cancel approved time-off

If the time-off request has not been approved yet, you can cancel your pending time-off request by clicking the {% icon rotate_left %}.

If your requested time off has already been approved, you cannot cancel it yourself. Instead, request a cancellation that your planner or team lead can approve or reject.

1. In the **Time-off requests** section, click the {% icon circle_xmark %} under the approved request you want to cancel.
2. (Optional) Enter a **Reason for cancellation**.
3. Click _Request cancellation_{:.doc-button}.

To withdraw a cancellation request for an already approved time off, click the {% icon rotate_left %}.
