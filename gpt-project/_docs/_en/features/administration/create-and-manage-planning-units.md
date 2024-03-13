---
title: Create and manage planning units
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to create, configure, and delete planning units.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-use-virtual-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
redirect_from:
  - /planning-unit-configuration/
redirect_reason: Updated filename on 21 August 2023
---

Planning units group people and configuration data for scheduling purposes. Your business locations do not necessarily have to correspond to your planning units. For example, people who work at two different locations can be {% link_new assigned | features/administration/employee-overview.md | #configure-employee-settings %} to one planning unit. We recommend using one single planning unit, unless:

- people are in different time zones. In this case, use one planning unit per time zone.
- planners in your company are responsible for separate groups of people, e.g. according to business units.

injixo Advanced and Enterprise WFM provide custom user roles to restrict user access to different planning units.

If you are working with several planning units, you can temporarily change an employee’s assignment from one planning unit to another. Learn more about how to {% link_new delegate employees | features/administration/employee-overview.md | #delegate-employees %}.

## Create planning units

1. Go to _Plan > Configuration > Planning Units_{:.breadcrumbs}.
2. Click the New icon {% icon item-add | icon-only %} in the upper left.  
   A configuration panel opens on the right side.
3. Complete the following fields:

   - **Name**: Unique name for the planning unit (max. 50 characters).
   - **Abbreviation**: Abbreviation for the name (max. 25 characters).
   - **Color**: Optional color for the planning unit. You will see the color in Schedules.
   - **Interval**: Influences the level of detail in which data is displayed in Schedules, e.g. coverage and staff requirements. The planning unit interval should not be longer than the interval of your contact and agent status data imports. The drop-down menu shows planning unit intervals in minutes. We recommend using **15&nbsp;minutes**. The interval cannot be changed after saving. Learn more about {% link_new data imports through integrations | features/acd-integration/cloud/how-integrations-work.md %}.
   - **Parent Planning Unit**: Optional planning unit that contains the planning unit you are creating. Learn more about {% link_new parent planning units | best-practices/how-to-use-virtual-planning-units.md %}.
   - **Time Zone**: Time zone of the planning unit. The time zone cannot be changed after saving the planning unit. Learn more about {% link_new working with time zones | best-practices/working-with-timezones.md %}.

     > Note
     >
     > The selected time zone must match the time zone of your workloads in Forecast. Otherwise, you cannot transfer staff requirements for scheduling. An integration will adjust the imported data according to the time zone of your workloads.

4. Click _Ok_{:.doc-button}.  
   You can now add business hours, activities, or {% link_new limit day models | features/administration/create-and-manage-planning-units.md | #limit-day-models %}.

### Add business hours

To add business hours to a planning unit, you need to {% link_new create the planning unit first | features/administration/create-and-manage-planning-units.md | #create-planning-units %}.

For scheduling, you need to add business hours to your planning unit. Business hours limit the daily hours for which you can {% link_new calculate staff requirements | features/forecast/injixo-forecast/staff-requirement.md %} and {% link_new create optimized schedules | features/scheduling/schedules/schedules-optimized-schedules.md %}. <!-- special public holiday day types or part of the linked article? -->

1. In the **Business Hours** section of the planning unit configuration panel, click the {% icon item-add %} to add the business hours for certain day types.  
   A dialog window opens.
2. In the **Day Types** section, select one or more {% link_new day types | features/administration/day-types.md %}.
3. Enter the start and end time in the **From** and **To** fields (24&nbsp;hours format). If you are open 24&nbsp;hours, enter 00:00 in both fields.
4. (Optional) In the **Valid from** and **Valid to** fields, enter a date range that the business hours apply to. If the business hours always apply, leave the fields blank. Learn more about {% link_new validity periods | features/administration/set-a-validity-period.md %}.
5. Click _Ok_{:.doc-button}.

To modify or remove business hours, click the {% icon item-edit %} or the {% icon item-delete %}.

### Add activities

To add activities to a planning unit, you need to {% link_new create the planning unit first | features/administration/create-and-manage-planning-units.md | #create-planning-units %}.

For scheduling, you need to add activities to planning units. You can only schedule people for activities that you have added to the planning unit. By default, all planning units include the Present activity. You cannot delete the Present activity.

To add activities to a planning unit, proceed as follows:

1. In the **Activities** section of the planning unit configuration panel, click the {% icon item-add %}.  
   A dialog window opens.
2. Click the activity you want to add.
3. (Optional) Enter a time range in the **From** and **To** fields. The {% link_new Create optimized schedules | features/scheduling/schedules/schedules-optimized-schedules.md %} functionality will consider this activity within the time range you entered. When both fields have the value 00:00, injixo considers the business hours of the planning unit. Users with admin access can change this default behavior in setting _48408_{:.id-label} _Take into account business hours in AutoScheduler_.
4. (Optional) Enter a time in the **Valid from** and **Valid to** fields to limit when the activity is available for scheduling. Leave **Valid from** and **Valid to** blank to make it always available.
5. Click _Ok_{:.doc-button}.

To edit or delete an activity, click the {% icon item-edit %} or the {% icon item-delete %}.

### Add multiactivities

To add a {% link_new multiactivity | features/administration/activity-types-and-properties.md | #subactivities %} to a planning unit, you need to add all the respective subactivities first. The multiactivity appears in bold in the list of activities. Multiactivities are not available in injixo Essential WFM.

### Limit day models

By default, all {% link_new day models | features/administration/daymodels/daymodel-creation.md %} are assigned to your planning units. If you do not use all day models in a planning unit, you can limit the number of day models for that planning unit.

Limiting day models can speed up scheduling with the Create optimized schedules functionality. However, you can only use the remaining day models to generate shifts, create reports, or create optimized schedules. This may involve more effort in maintaining the other configuration data, e.g. week time patterns. Deleting a day model in use does not affect the schedules and shifts created with that day model.

> Note
> 
> If you delete all day models in the planning unit, you can only schedule shifts by adding activities manually to the schedule or by {% link_new inserting activities in shift sequences | features/administration/shift-sequences.md %}. All other scheduling approaches, e.g. using the Create optimized schedules functionality or work time pattern models, will not work.

To limit the number of day models, proceed as follows:

1. Go to _Plan > Configuration > Planning Units_{:.breadcrumbs}.
2. Select the planning unit you want to edit and scroll to the **Day Models** section.
3. Click the {% icon item-edit %} next to the default configuration option **[All]** and select a day model. You can also click the {% icon item-delete %} to delete the **[All]** option. To limit the number of day models, you need to either replace or delete the **[All]** option. You cannot add day models to a planning unit more than once.  
   Skip step 3 if you want to assign more day models later.
4. Click the {% icon item-add %} to assign one or more day models.
5. Click _Ok_{:.doc-button}.

To edit or delete a day model, click the {% icon item-edit %} or the {% icon item-delete %}.

## Delete planning units

> Warning
> 
> If you delete a planning unit, the corresponding schedules are also deleted.

1. Go to _Plan > Configuration > Planning Units_{:.breadcrumbs}.
2. In the list, click the planning unit you want to delete.
3. To ensure that scheduling data is still displayed correctly, delete the activities and remove the assigned day models from the planning unit before deleting it.
4. Click the {% icon item-delete %} in the upper left.
5. To confirm, click _Yes_{:.doc-button}.
