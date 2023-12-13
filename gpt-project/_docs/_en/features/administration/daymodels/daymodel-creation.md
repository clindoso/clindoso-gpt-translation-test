---
title: Configure day models
redirect_from:
  - /day-models-overview/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to create day models of the types fixed shift, variable shift and availability period, and how to add activities to day models.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-basics.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
---

New to day models? Learn the {% link_new basics | features/administration/daymodels/daymodel-basics.md %} first.

## Create day models

You can create and edit day models under _Plan > Configuration > Day Models_{:.breadcrumbs}.

> Note
> 
> - Day models of type Fixed Shift are also called fixed day models.<br> 
> - Day models of type Variable Shift are also called variable day models.

1. To add a new day model, click the {% icon item-add %}.
2. From the **Type** drop-down menu, select the day model type you want to configure.
3. Configure your day model.<br>To find out more about the configuration options for each day model type, see the following sections.
4. To save the day model, click _OK_{:.doc-button}.

Now, you can {% link_new add activities | features/administration/daymodels/daymodel-creation.md | #add-activities-to-day-models %} to the new day model. 

> Note
> 
> If you work with a {% link_new limited number of day models in your planning unit | features/administration/create-and-manage-planning-units.md | #limit-day-models %}, you may need to assign new day models to your planning unit. If you use work time pattern models, update the week time pattern(s).

### Fixed Shift
   
| **Parameter** | **Description** |
|:-----|:-----|
| Name | Unique name to describe the day model. We recommend specifying the day model type and its start and end times, e.g. 8-16:30-fix. |
| Abbreviation | This version of the name is displayed in reports and in Schedules. We recommend using the specified name or a shorter version of it. |
| Shortcut | Optional keyboard shortcut to help you insert the day model more quickly in Shift Center. Learn more about {% link_new shortcuts | best-practices/tips-on-shift-center-usage.md %}. |
| Color |  The color appears in the schedule and on configuration data pages.<br>It can help you quickly identify the length, day model type, or included activities. |
| Valid to/Valid from | Optional period during which the day model can be used.<br>Learn more about {% link_new valid from/to dates | features/administration/set-a-validity-period.md %}. |
| Start | Time at which the fixed shift begins. |
| End | Time at which the fixed shift ends. |
| Total Shift Duration | Duration of the shift in hours.<br>If you configure this value, it will replace the configured end time.<br>Note: Day models of type Fixed Shift can span up to two days. To create a night shift, add up to 24 hours to the end time when creating the day model, or use the total shift duration. The maximum value is 48:00&nbsp;(h). |
| Activity | The first activity is the {% link_new base activity | features/administration/daymodels/daymodel-basics.md | #base-activity-and-shift-duration %}.<br>Note: You cannot change the base activity after saving the day model. |


### Variable Shift
   
| **Parameter** | **Description** |
|:---------------------|:---------------------|
| Name | Unique name to describe the day model. We recommend specifying the day model type and its start and end times, e.g. var-8-20-8. |
| Abbreviation | This version of the name is displayed in reports and in Schedules. We recommend using the specified name or a shorter version of it. |
| Color |  The color appears in the schedule and on configuration data pages<br>It can help you quickly identify the length, day model type, or included activities. |
| Valid to/Valid from | Optional period during which the day model can be used.<br>Learn more about {% link_new valid from/to dates | features/administration/set-a-validity-period.md %}. |
| Time Frame Start | Earliest possible time at which the shift can start. |
| Time Frame End | Latest possible time at which the shift can end. |
| Time Frame Duration | Number of hours between the earliest start and latest end time of the shift.<br>This will replace the Time Frame End. |
| Total Shift Duration | Total shift duration including breaks. The duration must be shorter than the time frame. If the shift duration equals the time frame, the day model automatically becomes a day model of type Fixed Shift. |
| Interval | Interval in which a shift can start within the defined time frame. For example, with an interval of 30, the shift can begin every 30&nbsp;minutes within the defined time frame. |
| Activity | The first activity is the {% link_new base activity | features/administration/daymodels/daymodel-basics.md | #base-activity-and-shift-duration %}.<br>Note: You cannot change the base activity after saving the day model. |

### Availability Period

Use this day model type e.g. in shift sequences to configure availabilities for several people at once. Note that day model availabilities overwrite availabilities entered by people in injixo Me as well as availabilities that have been manually added in Shift Center. Learn more about {% link_new availabilities | features/administration/availabilities.md %}.

| **Parameter** | **Description** |
|:---------------------|:---------------------|
| Name | Unique name to describe the day model. We recommend specifying the day model type and its start and end times, e.g. avail-8-16. |
| Abbreviation | This version of the name is displayed in reports and in Schedules. We recommend using the specified name or a shorter version of it. |
| Color |  The color appears in the schedule and on configuration data pages<br>It can be helpful when setting up shift sequences, for example. |
| Valid to/Valid from | Optional period during which the day model can be used.<br>Learn more about {% link_new valid from/to dates | features/administration/set-a-validity-period.md %}. |
| Availability Period Start | Earliest possible time at which the shift can start. |
| Availability Period End | Latest possible time at which the shift can end. |
| Availability Period Duration | Number of hours between the earliest start and latest end time of the shift. The maximum value is 48&nbsp;hours.<br>This will replace the Availability Period End. |

## Add activities to day models

To further define an existing day model, you can add breaks or other activities to it. Configure other activities if you need to represent specific tasks people should work on at a given time in a shift. These special activities can be, for example, checking the organization's social media channels or back-office tasks. 

To add activities, you need to {% link_new create the day model | features/administration/daymodels/daymodel-creation.md | #create-day-models %} first.

The schedule optimization can replace activities of type Presence that are configured as Replaceable. If you do not want to schedule people to work on any special activities, the base activity is the only activity of type Presence in your day model. Keep in mind that configuring activities in day models will limit the flexibility of optimization features (e.g. full optimization, extra activities, meetings). To keep the optimization as flexible as possible and to avoid scheduling errors, we recommend keeping the configuration of activities of type Presence in day models to a minimum.

> Note
> 
> The first activity you add to a day model is automatically the base activity. You cannot change or delete a base activity after saving the day model.
> We recommend using the activity Present as base activity. Find out more about the {% link_new base activity | features/administration/daymodels/daymodel-basics.md | #base-activity-and-shift-duration %}.

### Add a presence or absence activity

To add a presence or absence activity to an existing day model, proceed as follows:

1. Select a day model.
2. In the **Presences and Absences** section, click the {% icon item-add %}.<br>A dialog window opens.
3. Configure the activity:
- **Start** and **End**:<br>If the **Relative to Start of Shift** checkbox is checked: Define the number of hours/minutes after the start of the shift at which you want the activity to start and end (e.g. for 1.5 hours, enter 1:30).<br>If the **Relative to Start of Shift** checkbox is unchecked: Define the exact time after the start of the shift at which you want the activity to start and end (e.g. for 2pm, enter 14:00).
- **Duration**: If you configure a duration that is longer than the time between the configured start and end times, you create a {% link_new corridor | features/administration/daymodels/daymodel-basics.md | #fixed-elements-vs-corridors %} within which the activity can be moved.
- **Interval**: We recommend using the same interval as your ACD. Note that the activity length must be divisible by the selected interval.<br>If you enter 0, the start time of the activity is fixed and the activity cannot be moved within a corridor.
- **Relative to Start of Shift**:<br>If checked (default), the activity starts at the defined number of hours/minutes after the shift start. If the shift is moved, the activity is moved as well.<br>If unchecked, the activity starts at the exact configured time. When you move a variable shift, the activities will not move. This can be useful, e.g. when employees with different shifts need to attend a team meeting at the same time.
4. Select an **Activity** from the drop-down menu.
5. Click _OK_{:.doc-button}.

### Add a break activity

In both variable and fixed day models, you can add breaks for optimized scheduling and shift bidding.  
To add a break activity to an existing day model, proceed as follows:

1. Select a day model.
2. In the **Breaks (Shift Generation)** section, click the {% icon item-add %}.<br>A dialog window opens.
3. Configure the break:
- **Start** and **End**:<br>If the **Relative to Start of Shift** checkbox is checked: Define the number of hours/minutes after the start of the shift at which you want the break to start and end (e.g. for 4.5 hours, enter 4:30). By default, breaks are entered relative to the start of the shift, because they usually start after a certain time at work.<br>If the **Relative to Start of Shift** checkbox is unchecked: Define the exact time after the start of the shift at which you want the break to start and end (e.g. for 1pm, enter 13:00).
- **Duration**: If you configure a duration that is longer than the time between the configured start and end times, you create a {% link_new corridor | features/administration/daymodels/daymodel-basics.md | #fixed-elements-vs-corridors %} within which the break can be moved.
- **Interval**: We recommend using the same interval as your ACD. Note that the break length must be divisible by the selected interval.<br>If you enter 0, the start time of the break is fixed and the break cannot be moved within a corridor.
- **Relative to Start of Shift**:<br>If checked (default), the break starts at the defined number of hours/minutes after the start of the shift. If the shift is moved, the break is moved as well.<br>If unchecked, the break starts at the exact configured time. When you move a variable shift, the breaks will not move. This can be useful, e.g. if the cafeteria in your contact center is only open for a limited time.
4. Select a break option from the **Break** drop-down menu.
5. Click _OK_{:.doc-button}.

Note: In injixo Enterprise WFM on-premise, setting _48134_{:.id-label} _Treatment of shiftable presences and absences or breaks in time corridors when solving the shift reference in day models_ determines if break corridors remain or if these are converted to fixed elements.

## Effects of changing day models in use

Changing day models that are already used in your schedules can have different effects. You can safely change configuration data that is not relevant for scheduling, such as the name, abbreviation, or color.

However, we recommend you only make changes to scheduling-relevant data, such as start and end times, total shift duration, presences, and absences or breaks, before creating your next schedule. When you change an existing day model, injixo internally creates a copy of the original day model. This way, shifts that are already scheduled are retained and will still be displayed.

After changing an existing day model or adding a new one, we recommend running the scheduling process from the beginning so that new or modified day models are used correctly.

Affected day models are exchanged in shift sequences and week time patterns. Already scheduled day models will be displayed with a dotted line at the bottom in Shift Center and in Schedules. Shifts with this day model can no longer be scheduled or edited. They can only be deleted from the schedule.

If you have generated shifts from a day model and people have already requested such shifts in injixo Me as part of the shift bidding process, your people can no longer see or request shifts with that day model.
Already requested shifts will not be used in the subsequent lottery or assignment runs.

Note: The minimum and maximum values entered as shift requirements still apply for the changed day model.
