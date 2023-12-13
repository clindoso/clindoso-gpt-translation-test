---
title: Tips on Shift Center usage
product_label:
  - advanced
  - enterprise
  - classic
description: Learn some best practices for using the Shift Center.
redirect_from:
  - /best-practice-tips-on-shift-center-usuage/
---

In this article, you will receive useful tips to work with the Shift Center more efficiently in your daily work.

## Tip 1: Adjust the view of the hour scale

Limit the hour scale to the opening hours of your planning unit by hiding irrelevant time periods:

1. Go to _WFM > Administration > System > Settings_{:.breadcrumbs}.
2. Scroll to the _SchedulePro_ section (or use the search).
3. Adjust the default value for the settings below according to your needs:
   - _48077_{:.id-label} _Start time of the Shift Center hour scale_
   - _48078_{:.id-label} _End time of the Shift Center hour scale_

## Tip 2: Shortcuts for a quick assignment of activities

Shortcuts offer simple and quick way to add full-day activities or fixed day models to employees manually. No need to select the corresponding activity from a dialog window first. This is especially useful when managing absences during intraday management.

The two available shortcuts types allow letters, numbers, and spaces (max. 5 characters):

- Default shortcuts: require to press the _Enter_ key after you entered the defined sequence on your keyboard to insert the related day model or activity.
- Instant shortcuts: No need to press _Enter_. Add a _#_ character at the end when creating the shortcut definition.

### Create shortcuts

1. Go to _Plan > Configuration_{:.breadcrumbs} and select **Activities**. For day models, go to _WFM > Administration > Scheduling > Day Models_{:.breadcrumbs}.
2. Select an **activity** or **day model**.
3. Enter the shortcut into the **Shortcut** field, e.g. **s** for _sickness_ (default shortcut) or **s#** (instant shortcut).
4. Click _Ok_{:.doc-button} to save the shortcut.

Note: Shortcuts require that activities and day models are assigned to the planning unit.

### Use a default shortcut

1. Select one or more **day cells** for an employee in the scheduling window.
2. Press **s**. The new element is directly added. To enter an element for multiple consecutive days, select **several cells at once**, before pressing **s**. This action overwrites existing elements in the schedule.

### Use an instant shortcut

1. Select a **day cell** for an employee in the scheduling window.
2. Press **s** followed by **Enter**. To enter the element for several consecutive days, press a **number key** after the shortcut, e.g. **s** + **3** + **Enter**. This action overwrites existing elements in the schedule.

Tip: The space bar is perfectly suitable as an instant shortcut (e.g. for the activity sickness), because this key is reached fastest. Simply, press space followed by #.

{{ 1 | image: 'Instant-Shortcut', '50%' }}

## Tip 3: Copy the original schedule as reference

Even the best schedule will only last until the first necessary change in day-to-day business. To keep track of the necessary schedule variances and, if necessary, draw conclusions for the next scheduling period, it is a good idea to save the original schedule before changing it.

For this purpose, injixo offers various [scheduling levels](#tip-9-working-with-different-levels), and you can copy your final schedule from the _Schedule_ level to the _Actual_ level using the {% link_new copy level content | features/scheduling/schedules/schedules-copy-level-content.md %} feature to obtain a reference.

Use the levels contrary to their names:

- _Schedule_: for all changes concerning short-term illnesses, vacations, delays, or unexpected team meetings etc. Optimize jobs and breaks at any time, if you need to react to changed requirements.
- _Actual_: Use the level for comparison purposes. It serves as a reference to the original schedule.

## Tip 4: Sort shifts within the day view

When you open the _Shift Center_{:.menu-item}, the day view is always sorted alphabetically by employee name by default. You can {% link_new change the sort order | features/scheduling/shiftcenter/sort-and-filter-items.md | #sort-the-items-of-a-level %}, e.g. ascending or descending by shift start time. When you reopen the _Shift Center_{:.menu-item}, click the **arrow pointing down** to call up the sorting previously used.

## Tip 5: Change the view of the day cell

The day cell offers short information on the day in both closed and open day views. By default, it displays the short name of the first activity of the day, but depending on how you work, it may be useful to adjust the view.

To show the actual working hours (gross working time) or shift start/end times instead of the abbreviation of the first element, right-click a **day cell**, select **Display**, and then choose one of the **options**.

{{ 4 | image: 'Setting the day cell display', '50%' }}

## Tip 6: Display the modification history for a day

The _History_ tab gives displays the current and previous employee assignments for the selected day. You can see who made the respective change, which may be helpful when collaborating with several people on a schedule. Learn how to {% link_new display and revert previous actions | features/scheduling/shiftcenter/modify-items.md | #display-and-revert-previous-actions %}.

## Tip 7: Add activities to multiple employees at once

If you need to quickly insert the same (meeting) activity for multiple employees, adding it manually can be way more faster than using an automated process. You still have a direct view of the schedule and the parameter window. Learn how to {% link_new insert an activity for multiple employees at once | features/scheduling/shiftcenter/add-and-delete-items.md | #add-items-to-multiple-employees-at-once %}.

## Tip 8: Adjust the parameter view

The _Activities_ tab within the parameter window allows you to recognize over- or understaffed activities, indicated by colors.

To get a better overview, remove various activities from the view and {% link_new display only certain activity types | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md | #hide-activities-of-certain-types %}. If you only select the _Presence_ type, it will be easier to make adjustments and see their effects in the schedule, e.g. during intraday management when you enter sick leave requests, to be able to initiate requirement-oriented countermeasures, if necessary.

## Tip 9: Working with different levels

Display and use different levels to carry out your scheduling even more precisely:

- _Schedule_{:.menu-item}: displays manually or automatically scheduled activities and shifts. {% link_new Shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %} and {% link_new Optimized schedules | features/scheduling/schedules/schedules-optimized-schedules.md %} write to this level. Job and break optimizations change the content, employees see it in injixo Me.
- _Actual_{:.menu-item}: contains the actual schedule. [Copy your final schedule](#tip-3-copy-the-original-schedule-as-reference) to this level and make any last-minute changes for the day here.
- _External System_{:.menu-item}: displays {% link_new agent status data | features/acd-integration/cloud/import-agent-status-data.md %} imported using an integration (if configured). You can add/edit entries manually if needed.
- _Request_{:.menu-item}: displays all normal shift requests that employees enter in injixo Me. You can add day models manually, but no individual activities.
- _Alternative Request_{:.menu-item}: shows all alternative requests employees enter in injixo Me. You can add day models manually, but no individual activities.
- _Vacation Request/Absence Request_{:.menu-item}: displays any time-off requests employees enter in injixo Me. You can add day models manually, but no individual activities.
- _Availability_{:.menu-item}: displays employee availabilities. You can also add them manually.
- _Version 1_{:.menu-item} and _Version 2_{:.menu-item}: can contain schedule backups or approved time-off requests. Use this level for comparison purposes, e.g. for schedules compared to the actual day or for testing/comparing different scheduling scenarios.

Note: injixo Advanced and Enterprise WFM include all levels. You can configure the access to levels via {% link_new user roles | getting-started/configure-user-roles.md %}. injixo Essential WFM only provides access to the _Schedule_ level.
