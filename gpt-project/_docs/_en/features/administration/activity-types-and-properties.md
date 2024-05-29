---
title: Activity types and properties
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn about the different types of activities and the purpose of each activity configuration option.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-schedule-multiskill-agents.md
redirect_from:
  - /activity-properties/
redirect_reason: Updated filename on 11 October 2023
---

When {% link_new creating and editing activities | features/administration/activities.md %}, the different configuration options influence how activities are used and displayed in your schedules and reports.

## Activity types

The activity type influences your scheduling and determines:

- how optimized scheduling handles the activity.
- where you can use the activity.
- how the activity is displayed in Schedules and in Shift Center.
- whether reports include the activity. <!-- illness, absences, vacation -->

The following table provides more details about each activity type:

| Type     | Description                                                                                                                                                                    |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Presence | All activities on which people work.<br>Activities of the type Presence are scheduled by injixo based on staff requirements.                                                   |
| Break    | Paid or unpaid breaks within a shift.<br>Only activities of the type Break can be configured in day models as break activities. You can use the {% link_new break optimization | features/scheduling/schedules/break-optimization.md %} functionality to distribute breaks within the schedules so that you achieve optimal coverage for activities with staff requirements. |
| Illness  | Paid or unpaid absences such as a sick day or a doctor's appointment.<br>Only activities of the type Illness appear in the Illness reports.                                    |
| Vacation | Paid or unpaid vacation, company leave, etc.<br> Only activities of the type Vacation appear in the vacation reports.                                                          |
| Absence  | Other absences that affect the schedule, for example, offsite training, overtime leave, etc.<br>Absence reports only show activities of the type Absence.                      |
| Meeting  | Activity type to {% link_new schedule meetings                                                                                                                                 | features/scheduling/meetings/meetings-overview.md %}.                                                                                                                                       |

## Activity properties

Activity properties impact your schedule and how you can use the activity.
You can set activity properties with the following checkboxes.

| Property                                          | Effect                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Paid                                              | Activates the working time calculation for scheduled activities. If breaks or absences are paid, they are calculated as working time. If they are unpaid, they are not included in the net working time calculation.                                                                                                                                                                                     |
| Comply with rest period                           | Prevents violations of the rest period configured in the contract. injixo only checks the rest period if scheduling rule _2601_{:.id-label} is activated.                                                                                                                                                                                                                                                |
| Plannable                                         | injixo can schedule the activity if you use the Create optimized schedules functionality, or can optimize it during job optimization. We recommend using this property for activities with staff requirements. It is typically not used for activities of the types Absence, Vacation, and Illness.                                                                                                      |
| Requestable in Me                                 | Allows people to request time off (absences, vacation, and illness) in injixo Me (if there is a {% link_new Time-off period                                                                                                                                                                                                                                                                              | features/scheduling/time-off/time-off-periods.md %} with status Published). In shift bidding, shifts with activities of the types Presence and Break are automatically requestable.                                                       |
| Exchangeable with shift swap                      | Allows people to {% link_new swap the activity with each other                                                                                                                                                                                                                                                                                                                                           | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} in injixo Me. For this, all activities (including breaks) included in day models must be configured as **Exchangeable with shift swap**. |
| Allow overstaffing if shift requirements are zero | injixo can schedule the activity even during times with no staff requirements. By default, intervals with 0 requirements will not be covered.                                                                                                                                                                                                                                                            |
| Replaceable                                       | injixo can replace the activity with plannable activities with staff requirements. This is required to {% link_new schedule meetings                                                                                                                                                                                                                                                                     | features/scheduling/meetings/meetings-overview.md %} on this activity.                                                                                                                                                                    |
| Allow as full-day activity                        | You can schedule the activity for a full day in Schedules or on the Full-Day Activities tab in the day view in Shift Center. If the activity is also configured as Paid, the employee is credited with the corresponding daily target according to the contract.<br>Required to allow employees to request the activity as full-day activity in injixo Me.                                               |
| Can be a day status                               | Only available for full-day activities. Day status allows you to manually schedule the activity in the Shift Center as a day status on the Full-Day Activities tab. This preserves the replaced schedule entry for future reference. As a result, injixo excludes the people scheduled for an activity with this property from the coverage calculation but the original schedule entry remains visible. |
| Special handling in optimized scheduling          | Only available for activities of the type Presence. Activities with this property can only be scheduled strictly as they are configured. The activities cannot be replaced and their duration is not flexible.<br>Learn more in the [dedicated section below](#special-handling-in-optimized-scheduling).                                                                                                |

## Special handling in optimized scheduling

This activity property means that the Optimized scheduling functionality can only schedule the activity strictly as it is configured. This property is typically used for scheduling overtime or back-office activities.<br>
There are two different use cases for this activity property:

Option 1: The activity is part of a day model. In this case, the activity can only be scheduled for the configured duration and within the timeframe defined in the day model. The activity cannot be used to replace other replaceable activities. How Optimized scheduling handles the activity also depends on {% link_new how the activity is configured within the day model | features/administration/daymodels/daymodel-creation.md | #add-a-presence-or-absence-activity %}:

- Configured as fixed element: The schedule optimization will only schedule the activity for the exact time for which it is configured.
- Configured as corridor element: The schedule optimization can move the activity within the defined corridor to optimize the coverage of other activities.

Use example:

- Add a back-office activity without staff requirements and with a duration of one hour to your day model. Optimized scheduling will schedule the activity for exactly one hour. If the activity is configured as a corridor element in the day model, the activity will be moved within the corridor to the time slot where it has the least impact on the coverage for other activities.

Option 2: The activity is not part of a day model. In this case, Optimized scheduling cannot schedule the activity automatically, and cannot use it to replace other replaceable activities. The activity can only be scheduled manually.

Use example:

- Create an overtime activity that is not included in any day model. The Optimized schedule functionality will not schedule the activity and will not use it to replace replaceable activities. Add the activity to the schedule manually when necessary. In this use case, you always have complete control over when the activity is scheduled, for how long, and to whom it is assigned.

> Note
>
> This property is only available after you have created the activity.

## Subactivities

You can assign activities to other activities. The activity to which activities are assigned becomes a multiactivity. The assigned activities are the subactivities of the multiactivity. Multiactivities allow you to schedule people with several skills when one of their skills is needed. In the list of activities, multiactivities are marked with an <em class="multiactivity-icon"></em> icon.

The Create optimized schedules functionality can schedule multiactivities if you ensure the following:

- Select the Presence type for the multiactivities and all subactivities.
- Configure both multiactivities and subactivities as paid and plannable.
- Assign all subactivities (and the multiactivity in a second step) to your planning unit.
- To control who can be scheduled, assign a different skill to each subactivity.
- (Optional) Assign a skill to the multiactivity. In this case, people must have this additional skill to perform the multiactivity. By default, the multiactivity itself does not require skills.

> Note
>
> If you do not use the Create optimized schedules functionality but only run the job optimization, injixo can replace replaceable activities with multiactivities on the condition that a person can carry out at least one subactivity of the multiactivity.
