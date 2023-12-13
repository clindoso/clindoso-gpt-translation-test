---
title: Schedule extra activities
product_label:
  - advanced
  - enterprise
permalink: /schedules-extra-activities/
permalink_reason: /schedules-extra-activities/ used in email and in Intercom message
description: Schedule a defined amount of time for storable activities, such as email and backoffice (Schedules feature).
---

In this article, you will learn:

- what the feature _Schedule extra activities_ is.
- how to schedule an extra activity.
- how to create, review, and apply scheduling suggestions for extra activities.
- how to clean up the scheduling history.

## What is the Schedule extra activities feature?

With the _Schedule extra activities_ feature, you can schedule a defined amount of person-hours for a storable activity (such as back office or email). Storable means that the workload can be stored and worked on whenever there is the time.

The _Schedule extra activities_ feature will schedule the storable activity by replacing other existing activities. Based on your inputs, an optimization process generates suggestions for suitable time slots which you can accept or decline. The optimization ensures that the impact on the coverage of your other activities is as little as possible.

You can also use the _Schedule extra activities_ feature to schedule activities that are not storable.

## Prerequisites

- The period to be scheduled must contain a schedule in the _Schedule_ level.
- You can only put extra activities in time slots that contain activities of type _Presence_ (configured as _Paid_ and _Replaceable_).

## Generate scheduling suggestions

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click **Scheduling actions** and select **Schedule extra activities**.
3. Click _Set up new extra activity_{:.doc-button} at the bottom.
   {{ 1 | image: 'overview page'}}
4. In the _Settings_ section, select the **Planning unit** in which you want to schedule the extra activity. You can type to filter the list.
   Once you have selected an entry, you will see how many activities of type _Presence_ are currently not configured as _Replaceable_ in the planning unit. The more activities you configure as _Replaceable_, the more suggestions you will receive for the placement of your extra activity.
5. Select an **Extra activity to schedule**. The list contains _Paid_ activities of type _Presence_.
6. Select a **Date range** in which you want the extra activity to be scheduled. By default, the date range is the next Monday-Sunday working week following the current date.
7. Select the **Minimum duration of slots**. The duration can range from 15 to 120 minutes (the default is 30 minutes). The selectable values depend on the defined interval of the selected planning unit.
8. Enter the **Total person-hours to be scheduled** for the extra activity.
9. To enforce that person-hours are distributed as evenly as possible, check the checkbox **Distribute person-hours evenly among people**. This can lead to a poorer coverage for your other activities. How evenly injixo can distribute the hours also depends on other constraints, such as agents not being scheduled for a replaceable activity.

   {{ 2 | image: 'Settings', '60%' }}

10. Under _Employees_, check the **Employees** who will be scheduled with the extra activity. Change all at once using the checkbox in the column header. You can only select employees from the selected planning unit who have the required skill(s) for the extra activity. You can also pick a selection or an employee filter from the drop-down menu above.
11. Click _Generate suggestions_{:.doc-button} at the bottom of the page.

This takes you back to the overview page. The _Scheduling history_ shows an entry for your request. The _Status_ column shows that the scheduling is in progress.

The generation of scheduling suggestions can take some time, depending on the number of employees and the chosen date range. Wait until the process has completed and the _Status_ changes. Learn more about the different statuses below.

## Check the status

Each scheduling process creates a row in the _Scheduling history_ section with the following information:

- date and time when the process was initiated
- the user who started it
- the chosen planning unit
- the extra activity which has been scheduled
- the chosen date range

When the scheduling is finished, the _Status_ column shows one of the following values:

- _Suggestions available_: The process was successful and scheduling suggestions have been generated for the chosen extra activity. Learn how to [review the suggestions](#review-and-apply-scheduling-suggestions).
- _Not possible_: The process failed, no suggestions have been created. Reasons for this may be that the selected employees don't have enough _Replaceable_ activities of type _Presence_ in their schedules or that the provided value for _Minimum duration of slots_ is too long. The status column also shows the text _View conflict_. Click it to display the reason for the conflict.<sup>1</sup>
- _Optimization failed. Please try again_: The process couldn't be started. Try starting the process again. If the problem persists, {% link_new create a ticket | support/create-ticket.md %} to get support.

<sup>1</sup> Message example: _"It was not possible to find slots for the selected employees. These employees do not have enough replaceable activities of type presence in their schedule or the provided minimum duration of slots is too long."_ This message appears if there is no schedule at all or if no _Replaceable_ activities exist in the schedule, or if no activity has been configured as _Replaceable_.

## Review and apply scheduling suggestions

If the scheduling suggestions have been successfully generated, the _Status_ column shows the text _Suggestions available_ and the link _View suggestions_:

1. To display details about the generated suggestions, click the **View suggestions** link.
   A table displays the following columns:
   - _Suggested time slot_: the time slot when the extra activity could be scheduled
   - _Extra activity to schedule_: the extra activity that will be scheduled
   - _Employee_: the employee who will receive the extra activity in the suggested time slot
   - _Replaced activity_: the activity which will be replaced by the extra activity
   - _Resulting coverage_: information about how the coverage will change for all affected activities if the scheduling suggestion for the extra activity is applied
2. (Optional) To exclude suggestions from being scheduled, uncheck one or more **checkboxes** on the left. At the top, you see the total number of person-hours which have been suggested and the total person-hours which will be scheduled based on your selection.
3. To write the suggestions into the schedule, click _Schedule extra activity_{:.doc-button} at the bottom of the page. This can take a moment.

   {{ 3 | image: 'View suggestions page'}}

## View the scheduling results

After the suggestions have been written into the schedule, you can click the **View results** link in the _Scheduling history_ section. The _Scheduled_, _Failed_, and _Excluded_ tabs on top allow you to review the scheduling results:

- The _Scheduled_ tab contains all scheduling suggestions that you wrote into the schedule.
- The _Failed_ tab contains all scheduling suggestions which could not be scheduled due to errors.
- The _Excluded_ tab contains all scheduling suggestions that you didn't select in the previous step and which therefore haven't been written into the schedule.

If one of the tabs is deactivated, there are no results in that category.

You can click the **View Schedule** link to go directly to your schedule.

{{ 4 | image: 'Results page'}}

## Remove Old Entries

You can remove entries from the _Scheduling History_ that are no longer needed:

1. Check the **checkbox** in front of an entry. Or check the checkbox on top to select all entries.
2. Click _Delete entries_{:.doc-button} to remove the selected rows. The extra activities that you already added to the schedule _won't_ be removed.
