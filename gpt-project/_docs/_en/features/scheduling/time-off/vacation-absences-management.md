---
title: Approve or reject time-off requests
redirect_from: /vacation-absences-management-new/
redirect_reason: Features in WFM section link to the article
description: Approve or reject pending time-off requests. Learn how injixo can suggest which requests to approve based on your needs.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-entitlement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md
---

The Time Off page provides an overview of all absence and vacation requests that people enter in injixo Me.

Users with the Planner or Supervisor (advanced) default role can:
-  accept or reject time-off requests
-  configure rules and quotas to get automatic suggestions to approve or reject a request

Users with the Supervisor (basic) default role can only see time-off requests.

To manage the time-off requests, go to _Plan > Time Off_{:.breadcrumbs}.

## Show pending, rejected, or approved requests

You can display future and past requests for all requestable absence and vacation activities, e.g. to approve them or to check when requests have been submitted. Filter by planning unit, selection, status, and date range at the top. To display time-off requests that match the filter, click _Apply filters_{:.doc-button}.

In the filter results, you can search for an activity or a person's name using the search field or click a column header to sort. You cannot sort by the columns Requested days (RD),  Available days (AD), and Comment (C).

The Status column displays open, rejected, and approved requests. The columns Requested days and Available days display people's taken and remaining vacation days based on their {% link_new vacation entitlement | features/scheduling/time-off/vacation-entitlement.md %}.

The Created column shows a timestamp for all requests submitted in injixo Me. The timestamp shows when the request was entered by a person. Hover over a cell to see the exact time.

The Created column displays the Unknown value for requests inserted in the Absence Request level in Shift Center or Schedules (or submitted in injixo Me before 2 November 2021). injixo sorts requests by request ID. Hover over an Unknown value to see its request ID.

## Approve or reject requests

Before you decide to approve or reject a request, you can click the Start or End cell to {% link_new check the quotas | features/scheduling/time-off/vacation-absences-management.md | #taken-quota-and-target-quota %}
quotas for the days requested at the bottom of the calendar on the right.

1. In the **Status** column, click **✓** to approve or **✗** to reject a request. Click again to deselect the entry.
  Click _Mark all as approved_{:.doc-button} or _Mark all as rejected_{:.doc-button} at the top of the list to select all pending requests.
2. Click _Apply n changes_{:.doc-button}.
3. (Optional) Add a comment for the approvals and rejections.
  injixo will notify people by email and include the comments. If you approve or reject multiple requests by different people at once, every person will see the same comment.
4. Click _Approve n requests_{:.doc-button} or _Reject n requests_{:.doc-button}. The button reflects the number of selected entries. 
    By default, injixo checks whether approvals would violate rules, e.g. surpassing the remaining vacation entitlement. A red banner with the request ID indicates a rule violation. Click _Reject n requests_{:.doc-button} to deselect all requests marked for rejection.     
    Check the **Bypass approval rules** checkbox to approve or reject the requests even if they go against approval rules.

### Taken quota and Target quota

The calendar footer displays two rows with weekly quotas:

- **Taken quota**: Number or percentage of people with approved time off on this day.<br>The **Taken quota** value includes all activities of type holiday, absence, and sickness marked as **Requestable in Me**.
- **Target quota**: Number or percentage of people needed for the day as configured in the {% link_new base quota configuration | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md | #base-quota %}.

Use the radio buttons on the left of the footer to show the values as **Percentage** or as **Number of employees**/**Number of full-time employees** (depending on the base quota configuration).
To see a tooltip with the number of people and the number of pending requests, hover over a cell.

If **Full-time equivalent** is configured, the values reflect the duration of a time-off request in relation to a full-time contract. Without **Full-time equivalent**, each time-off request counts the same, regardless of its length.

## Configure approval suggestions

injixo can suggest requests for approval. Automatic suggestions consider the number of people, staff requirements, as well as planned absences, and configured target quotas for the planning unit. Learn how to configure {% link_new approval rules and quota settings | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md %}.

1. Click _Suggest approvals_{:.doc-button} to display potential requests to approve. The process treats earlier requests with a higher priority ("First come, first served"). You'll see the result after a short loading time, showing: Loading Proposals.
2. Suggested approvals appear in green. You can still deselect rows using the **✗** icon.
3. Click _Apply n changes_{:.doc-button}. The button name reflects the number of selected entries (n).
4. (Optional) Enter a comment for approval/rejection.
5. Click _Approve n requests_{:.doc-button}.

Note: You cannot click _Suggest approvals_{:.doc-button} if you:

- search within the list of requests.
- haven't selected a planning unit or any requests for approval/rejection.

> Email notifications
>
> injixo always sends email notifications in all cloud versions. You cannot deactivate them. injixo Enterprise On-Premise sends email notifications when the field E-Mail 1 is configured for the people.
