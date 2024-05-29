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

_Plan > Time Off_{:.breadcrumbs} provides an overview of all time-off requests (activities of type Absence, Illness, or Vacation) that have been submitted by people in injixo Me. The page also shows activities that have been manually entered in the **Absence Request** level in Shift Center or Schedules.

People with the Planner or Supervisor (advanced) {% link_new role | getting-started/default-user-roles.md | #default-roles %} can do the following:

- View time-off requests (also available for Supervisor (basic))
- Approve or reject time-off requests
- Configure rules and quotas for automatic recommendations for approval or rejection

## View requests

You can view future and past time-off requests as follows:

1. To filter the results, select a planning unit, optionally a selection and a status, and a date range.
2. Click _Apply filters_{:.doc-button}.<br>
   By default, requests are sorted by their internal request ID.
3. (Optional) Search the results by activity or a person's name, or sort the table.<br>
   You can now view, approve, or reject time-off requests.

The page will show a table with filtered data that has the following columns:

| Column              | Description                                                                                                                                                                                                                                                                                                                                                  | Sortable                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- | --- |
| Status              | Open, rejected, and approved requests                                                                                                                                                                                                                                                                                                                        | Yes                                                     |
| Created             | Timestamp for all requests submitted in injixo Me. The timestamp shows when the request was entered by a person. Hover over a cell to see the exact time. Unknown for requests inserted in the **Absence Request** level in Shift Center or Schedules (or submitted in injixo Me before 2 November 2021). Hover over an Unknown value to see its request ID. | Yes                                                     |
| Name                | Name of the person requesting time-off                                                                                                                                                                                                                                                                                                                       | Yes                                                     |
| RD (Requested days) | Remaining vacation days based on people's {% link_new vacation entitlement                                                                                                                                                                                                                                                                                   | features/scheduling/time-off/vacation-entitlement.md %} | No  |
| AD (Available days) | Taken vacation days based on their {% link_new vacation entitlement                                                                                                                                                                                                                                                                                          | features/scheduling/time-off/vacation-entitlement.md %} | No  |
| Start               | Start date of the request                                                                                                                                                                                                                                                                                                                                    | Yes                                                     |
| End                 | Start date of the request                                                                                                                                                                                                                                                                                                                                    | Yes                                                     |
| Activity            | Requested activity                                                                                                                                                                                                                                                                                                                                           | Yes                                                     |
| Comment             | Comment submitted with the request                                                                                                                                                                                                                                                                                                                           | No                                                      |

## Approve or reject requests

Before you decide to approve or reject a request, you can click the Start or End cell to {% link_new check the quotas | features/scheduling/time-off/vacation-absences-management.md | #taken-quota-and-target-quota %} for the days requested at the bottom right of the calendar.

1. In the **Status** column, click **✓** to approve or **✗** to reject a request. Click again to deselect the entry.
   Click _Mark all as approved_{:.doc-button} or _Mark all as rejected_{:.doc-button} at the top of the list to select all pending requests.
2. Click _Apply n changes_{:.doc-button}.
3. (Optional) Add a comment for the approvals and rejections.
   injixo will notify people by email and include the comments. These email notifications cannot be deactivated. If you approve or reject multiple requests by different people at once, every person will see the same comment.
4. Click _Approve n requests_{:.doc-button} or _Reject n requests_{:.doc-button}. The button reflects the number of selected entries.
   By default, injixo checks whether approvals would violate rules, e.g. surpassing the remaining vacation entitlement. A red banner with the request ID indicates a rule violation. Click _Reject n requests_{:.doc-button} to deselect all requests marked for rejection.  
   Check the **Bypass approval rules** checkbox to approve or reject the requests even if they go against approval rules.

### Taken quota and Target quota

The footer of the calendar displays two rows with weekly quotas:

- **Taken quota**: Number or percentage of people with approved time off on this day.<br>The **Taken quota** value includes all activities of type holiday, absence, and sickness marked as **Requestable in Me**.
- **Target quota**: Number or percentage of people needed for the day as configured in the {% link_new base quota configuration | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md | #base-quota %}.

Use the radio buttons on the left of the footer to show the values as **Percentage** or as **Number of employees**/**Number of full-time employees** (depending on the base quota configuration).
To see a tooltip with the number of people and the number of pending requests, hover over a cell.

If **Full-time equivalent** is configured, the values reflect the duration of a time-off request in relation to a full-time contract. Without **Full-time equivalent**, each time-off request counts the same, regardless of its length.

## Configure approval suggestions

injixo can suggest requests for approval. Automatic suggestions consider the number of people, staff requirements, as well as planned absences, and configured target quotas for the planning unit. Learn how to configure {% link_new approval rules and quota settings | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md %}.

1. To display requests to approve, click _Suggest approvals_{:.doc-button}.<br>
   The process treats requests that were submitted earlier with a higher priority ("First come, first served").<br>
   Suggested approvals appear in green. You can still deselect rows using the **✗** icon.

   > Note
   >
   > You cannot click _Suggest approvals_{:.doc-button} if you search within the list of requests or haven't selected a planning unit or any requests before.

2. Click _Apply n changes_{:.doc-button}. The button name reflects the number of selected entries.
3. (Optional) Enter a comment for approval/rejection.
4. Click _Approve n requests_{:.doc-button}.
