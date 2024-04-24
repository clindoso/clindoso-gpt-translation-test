---
title: Manage your people's unavailabilities
description: Learn how to use an activity of the Absence type to let your people define their unavailabilities.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
---

Create a requestable activity of the Absence type to let your people define the times when they are unavailable to work.

Manage your people's unavailabilities with time-off requests to achieve the following:

- Define the periods during which people can add their unavailabilities.
- Set a deadline for unavailability requests, and approve or reject them.
- Keep track of your people's requests over time. Assess if their contracts align with their time-off needs.
- Allow people to set an unlimited number of unavailabilities.
- Allow people to set unavailibities for partial days.

This article provides an overview of the process. You can use it as a checklist.

## 1. Create the activity Unavailable

1. In _Plan > Configuration_{:.breadcrumbs} create a {% link_new new activity | features/administration/activities.md | #create-an-activity %}.
2. Configure your activity as follows:
   - **Name**: Enter Unavailable. An abbreviation is generated automatically.
   - **Type**:  Select **Absence**.
   - Check the **Requestable in Me** checkbox.
   - (Optional) Check the **Allow as full-day activity** checkbox.
3. Click _Create activity_{:.doc-button}.

## 2. Create a time-off period

1. In _Plan > Time Off_{:.breadcrumbs}, create a {% link_new time-off period | features/scheduling/time-off/time-off-periods.md | #create-a-time-off-period %}.
2. Enter the general information for your time-off period:
   - **Planning unit**.
   - (Optional) **Selection**.
   - **Activity**: Select **Unavailable**.
   - (Optional): **Deadline**.
   - **Status**: Select **Published**.
3. Click _Create time-off period_{:.doc-button}.

## 3. People submit their requests

In _Me > Time Off_{:.breadcrumbs}, people can {% link_new submit requests | features/injixo-me/use-injixo-me/explore-injixo-me.md | #request-time-off %} for the activity Unavailable.

## 4. Approve or reject requests

In _Plan > Time Off_{:.breadcrumbs}, {% link_new approve or reject time-off requests | features/scheduling/time-off/vacation-absences-management.md %} for the activity Unavailable.<br>
After you approve a person's request, the Schedule window in Shift Center shows a red cell with the abbreviation of the Unavailability activity for the time slot of the approved request. If you use **Create optimized schedules** or **Job optimization**, injixo does not schedule the person during the blocked time slot.

## Keep track of the requests

In _Plan > Shift Center_{:.breadcrumbs}, you can see the details of approved time-off requests for the activity Unavailable.

1. Click the **Activities - Requirements** tab under the table. At the top, select a date range from the date picker and click _Apply_{:.doc-button}.
2. Expand the relevant planning unit in the top table.
3. Double-click a red cell labelled as Unavailable.  
4. Click the **History** tab.  
    You will see the details of the time-off request's approval:
    - Date/Time: Date and time of the approval.
    - Action: The action performed. In this case, Approve request.
    - User: The person who approved the request.
5. Click _OK_{:.doc-button}.
  
Go to _Plan > Time Off_{:.breadcrumbs} to {% link_new see approved, pending and rejected requests | features/scheduling/time-off/vacation-absences-management.md | #view-requests %}.
