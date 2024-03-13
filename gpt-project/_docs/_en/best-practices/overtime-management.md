---
title: Overtime management
product_label:
  - advanced
  - enterprise
  - classic
description: Learn how to best configure activities to schedule overtime work and document it in a transparent manner.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

Sometimes, people need to work overtime to keep reasonable service levels. The reasons for overtime include an unexpectedly high workload, or understaffing caused by high absence quotes due to illness or holiday.  
In many cases, your people's contracts stipulate that overtime hours are paid higher, or that any amount of overtime hours worked must be granted as additional vacation allowance. It is also important to respect other contractual constraints, such as rest time between shifts when people work overtime. If you are a service provider, you may also be obliged to inform customers about any additional work scheduled. 

In this article, you can find tips on how to configure activities and multiactivities to easily schedule overtime work and display it correctly on your coverage heat map and in your reports.

Overtime should be scheduled manually in Shift Center or Schedules as an addition to the existing schedule.

## Create activities for overtime

The example below uses a new activity named Calls. Follow these steps for all activities that you want to be able to schedule as overtime work, i.e. for Calls or Emails, but not for Illness or Holiday.

1. {% link_new Create and configure the activity | features/administration/activities.md %} **Calls**. 
2. Duplicate the activity **Calls** and name the new one **Calls overtime**. You do not need to add skills to this activity.  
  - Check the checkbox **Special handling in Schedule optimization**.
  - Make sure that the checkbox **Requestable in Me** is not checked.
3. In **Calls overtime**, add **Calls** as a subactivity.  
  **Calls overtime** is now a multiactivity.
4. Add both activities to the relevant planning unit. Do not add the overtime activity to any day model.

With this configuration, the activity Calls overtime can only be scheduled manually, and it cannot be replaced during schedule optimization. People will not be able to request this activity in injixo Me.

By adding "overtime" to the name of the multiactivity, you and your people can clearly see on their schedule when they are working overtime, for how long, and on which task.

## Schedule overtime

You can manually schedule overtime either in _Plan > Shift Center_{:.breadcrumbs} or in _Plan > Schedules_{:.breadcrumbs}.

To add overtime activities in Shift Center, follow these steps:

1. Choose the planning unit and, optionally, the selection to which the person you want to schedule for overtime work belongs.
2. Double-click that person's cell for the day on which they should work overtime. Click the **Multi-Activities** tab and select **Calls overtime**.
3. Set a start and end time for the activity.
4. Click _OK_{:.doc-button}.

The planned overtime is immediately reflected in the Schedule window and on the Activities tab in the {% link_new parameter window | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %}. If you configure the Activities tab to show the coverage, the heat map will update and reflect the overtime planned.

To add overtime activities in _Plan > Schedules_{:.breadcrumbs}, follow these steps:

1. Double-click a cell in the schedule to open the edit view.
2. Click _Add new Activity_{:.doc-button}.  
  A new row with the activity is added to the right.
3. In the new row, select **Calls overtime** from the drop-down menu.
4. Set a start and end time for the activity.
5. Click _Save_{:.doc-button}.

## Reporting

The report **Activities in hours** will reflect that the person worked overtime, thanks to the activity name including that information. This way, all worked overtime is documented and can be seen by all relevant people, e.g. the finance department who needs to handle the extra pay.
