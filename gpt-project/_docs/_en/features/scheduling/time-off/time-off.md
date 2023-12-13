---
title: Use Time Off
description: Learn how you can approve time off requests.
product_label:
  - essential
  - advanced
  - enterprise
beta-feature: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
---

In _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span> you can manage time-off requests and the time-off balances of your people.
All of your actions will be recorded for transparency and full traceability. Time Off will help you to plan the capacity of your {% link_new planning unit | features/administration/create-and-manage-planning-units.md %}.

This is how you can approve or reject time-off requests:

- A person requests time off in injixo Me <!-- add link later -->
- You approve or reject the request in _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span>
- If you approve the request, the time off is added to the schedule and the person's balance is updated

## Prerequisite
Before people can request time off in injixo Me, you need to [create time-off types](https://help.injixo.com/time-off-types#create-a-time-off-type) with an entitlement period, and at least one [time-off period](https://help.injixo.com/time-off-types#create-a-time-off-period) with the status Published.

## Approve or reject time-off requests

1. Go to the **Requested** tab.
2. Select the request you want to approve or reject.
3. (Optional) Add a comment.
4. Click *Approve time-off*{:.doc-button} or *Reject time-off*{:.doc-button}.  
   The person will be notified by email. Rejections are final.

## Cancel approved time-off requests

1. Go to the **Decided** tab.
2. Select the approved request you want to cancel.
3. Click *Cancel time off*{:.doc-button}.
4. If the person already had a schedule for the days for which you cancel the time off, select one of the following options:
      - **Restore history**: The person will remain scheduled for their shift on the selected day.
      - **Blank out shift**: The person will no longer be scheduled for their shift on the selected day. You may need to update their schedule manually in *Plan > Schedules*{:.breadcrumbs}.
5. Click **Cancel time off**.
4. If the person did not yet have a schedule for the timeframe, you may need to update their schedule manually in *Plan > Schedules*{:.breadcrumbs}. injixo does not update schedules automatically.

## Approve or reject a cancellation request

People cannot cancel their own time off. People can request to cancel an already approved time off.
You need to accept or reject the cancellation requests. 

1. Go to the **To be canceled** tab.
2. Select the cancellation request you want to approve or reject.
3. Click *Approve cancellation*{:.doc-button} or *Reject cancellation*{:.doc-button}.
4. If you approve a cancellation, select one of the following options:
      - **Restore history**: The person will remain scheduled for their shift on the selected day.
      - **Blank out shift**: The person will no longer be scheduled for their shift on the selected day. You may need to update their schedule manually in *Plan > Schedules*{:.breadcrumbs}.
5. Click **Approve cancellation**.
