---
title: Create a schedule
description: Follow the basic steps required to create a schedule.
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/resolve-optimization-issues.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/why-level-copy.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/meetings-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-extra-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-replace-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-public-holidays.md
redirect_from:
  - /quickstart-scheduling/
redirect_reason: Updated filename on 27 July 2023
---

Creating schedules is an essential part of the {% link_new WFM cycle | getting-started/the-wfm-cycle-in-injixo.md %}. Schedules contain the shifts and activities planned for your people.  

Use this article as a checklist to support your onboarding.

Note: In injixo Essential WFM, you cannot back up your time-off requests or the final schedule.

## Prerequisites

Before you create a schedule, make sure you have correctly {% link_new set up your base configuration | getting-started/set-up-base-configuration.md %} and {% link_new generated a forecast | getting-started/calculate-a-forecast.md %}. 

## Configuration order

We recommend setting up the configuration items in the order presented in this article. No configuration setup is the same, which is why the optimal order might be different for your organization. Contact your consultant if you have any questions.

## Configure time off

People can request time off using injixo Me. To configure time off, go to _Plan > Time Off_{:.breadcrumbs}:

1. Enter your people's {% link_new vacation entitlement | features/scheduling/time-off/vacation-entitlement.md %} for the current year.
2. Create a {% link_new time-off period | features/scheduling/time-off/time-off-periods.md %} and publish it. A time-off period defines the time frame in which people can request vacation and other absences. People will receive a notification in injixo Me and can start creating time-off requests for that period.

## Enter Illness or Absence activities

In {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %} and {% link_new Shift Center | features/scheduling/shiftcenter/shift-center-overview.md %}, you can manage your team's schedule. Enter any known {% link_new activities | features/administration/activity-types-and-properties.md | #activity-types %} of the types Absence or Illness into the schedule.

## Manage time-off requests

In _Plan > Time Off_{:.breadcrumbs}, approve or reject any {% link_new pending requests | features/scheduling/time-off/vacation-absences-management.md %}.

> Create a backup of the current schedule in another level
>
> Use {% link_new Copy level content | features/scheduling/schedules/schedules-copy-level-content.md %} to save a copy of your schedule. This ensures that you do not lose any approved time-off requests or previously entered absences if you delete the schedule and start over.

## Create the schedule

In {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %}, {% link_new Shift Center | features/scheduling/shiftcenter/shift-center-overview.md %} or {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %}, check if {% link_new staff requirements | features/forecast/injixo-forecast/calculate-staff-requirements.md %} are correctly set up for your activities.

1. Insert {% link_new shift sequences | features/scheduling/schedules/schedules-insert-shift-sequences.md %} for your people.
2. Configure and apply additional {% link_new scheduling methods | features/scheduling/scheduling-methods.md %} to complete the schedule.
3. Run the {% link_new job optimization | features/scheduling/schedules/schedules-job-optimization.md %}. You can skip this step if you {% link_new create an optimized schedule | features/scheduling/schedules/schedules-optimized-schedules.md %}.

Tip: If you are creating a schedule for testing purposes, you can use {% link_new empty levels | features/scheduling/schedules/schedules-empty-levels.md %}. Copy the saved absences and time-off requests back to the Schedule level before each test run.

## Back up your final schedule

Before applying any {% link_new manual changes | features/scheduling/shiftcenter/modify-items.md %} to your original schedule, {% link_new save a backup | features/scheduling/schedules/schedules-copy-level-content.md %} in the Actual level. This allows you to assess the quality of your original schedule compared to later versions.

## Publish the schedule and allow shift swaps

1. Create a scheduling period to {% link_new allow people to see their schedule | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} in injixo Me.
2. (Optional) {% link_new Allow people to swap shifts | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.  
    By default, you need to {% link_new view and approve any pending shift swaps | features/scheduling/view-approve-shift-swap-requests.md %}, but you can also allow automatic swaps between people with the _48152_{:.id-label} **Exchange Mode** setting.
3. Share the article {% link_new Explore injixo Me | features/injixo-me/use-injixo-me/explore-injixo-me.md %} with your people.
