---
title: Create activities
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
beta-feature: false
description: Create activities to represent scheduled and unscheduled tasks in your company.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

To create, edit and delete activities, go to _Plan > Configuration > Activities_{:.breadcrumbs}.

Activities represent all tasks that are scheduled and reported on in your company, such as telephony, break, time off, or meetings. You can create as many activities as you want. The number of activities depends only on how many tasks you want to distinguish and the desired level of detail.

Activities are an essential part of planning and scheduling in injixo. They are linked to other configuration items, e.g. to {% link_new planning units | features/administration/create-and-manage-planning-units.md | #add-activities %}, {% link_new day models | features/administration/daymodels/daymodel-basics.md %}. They are also part of the schedules managed in {% link_new Shift Center | features/scheduling/shiftcenter/add-and-delete-items.md %} or in {% link_new Schedules | features/scheduling/schedules/schedules-edit.md %}.

injixo includes two pre-configured (non-deletable) activities:

- Present: This activity is used as a placeholder activity within day models. During scheduling, injixo replaces this activity with other activities that are configured as Plannable.
- Vacation: This activity is used to schedule paid vacation based on a person’s vacation entitlement. Create unpaid time off as a separate activity.

## Create an activity

1. Click _New activity_{:.doc-button}.
2. Enter the general information for your activity:
   - **Name**: Unique name to describe your activity. The abbreviation will be automatically generated.
   - **Type**: The activity type determines how injixo uses activities in scheduling and how they are displayed in other modules and reporting. Learn more about the different {% link_new activity types | features/administration/activity-types-and-properties.md | #activity-types %}.
   - **Color**: The color appears in schedule and configuration data pages. It can help you identify different activities.
   - **Shortcut**: Optional keyboard shortcut to help you insert the activity more quickly in Shift Center. Learn more about {% link_new shortcuts | best-practices/tips-on-shift-center-usage.md | #tip-2-shortcuts-for-a-quick-assignment-of-activities %}.
   - **Official name and abbreviation**: Alternative name that can be used for internal reporting and integrations. injixo Me always displays the name entered under **Name**.
3. Check one or more checkboxes to set different {% link_new activity properties | features/administration/activity-types-and-properties.md | #activity-properties %}.
  If you check Plannable, you can edit the {% link_new importance value | best-practices/importance-for-activities.md %}.
  If you check Replaceable, you can edit the {% link_new priority value | best-practices/priority-for-activities.md %}.
4. (Optional) {% link_new Assign skills | features/administration/work-with-skills.md | #assign-skills-to-activities %} to the activity.
5. Click _Create activity_{:.doc-button}.

Learn more about {% link_new activity types and properties | features/administration/activity-types-and-properties.md %}.

### Activity ID

To see the ID of an activity, you can: 
- Click an activity in the **Activities** list. The URL on your browser bar shows the ID of the selected activity (e.g. https://www.injixo.com/plan/configuration/activities/1234).
- Use the injixo API. Learn how to [manage activities through the injixo API](https://api.injixo.com/resources/activities/).

## Multiactivities and subactivities 


Multiactivities allow you to schedule people with several skills when one of their skills is needed. You can turn an activity into a multiactivity by {% link_new assigning other activities | features/administration/activity-types-and-properties.md | #subactivities %} to it. The activities assigned become its subactivities.  In the list of activities, multiactivities are marked with an <em class="multiactivity-icon"></em> icon.

If an activity is a subactivity, when you click it you can see the section **Multiactivities**, which displays all multiactivities it is assigned to.

If an activity is not a subactivity, when you click it you can see the section **Subactivities**, where you can select other activities to be subactivities of the activity that you are editing. The activity itself would then become a multiactivity.
You can only assign subactivities to an activity after you have created it.

## External systems

<!-- will be made obsolete by the new activity mapping page. Will require a separate article -->

You can map activities from external systems to an activity in injixo.
1. Select an activity from the list, scroll to the **External systems** section, and click _Edit in WFM_{:.doc-button}.
2. Navigate to the **External systems** section.
3. Click the {% icon item-add %}.
4. Select an **external system**, a **name from the external system**, and a **classification** from the drop-down menus.
5. Click _OK_{:.doc-button}.

> You can assign an activity from an external system only once to a single activity in injixo.

## Duplicate an activity

To create a new activity with the same general properties as an existing activity, follow these steps:

1. In the **Activities** list, select an activity.
2. Click **Duplicate activity** under the activity name.  
A **Create new activity** window opens with pre-checked checkboxes. Assigned skills and subactivities are not duplicated.
3. Enter a **Name** for the new activity.
4. (Optional) Change the color and other properties.
5. Click _Create activity_{:.doc-button}.

## Edit or delete an activity

1. In the **Activities** list, select an activity.
  - To edit the activity, edit the information you want to change and click _Save changes_{:.doc-button}.
  - To delete the activity, click _Delete activity_{:.doc-button} in the lower right.

If the deleted activity was assigned to other configuration items, such as planning units or day models, its name is displayed in italics in these items. A deleted activity loses its assignments to other items but will remain visible in configuration data. You may need to recreate existing day models that used the deleted activity.

Shift Center displays deleted activities {% link_new surrounded by a dashed line | features/scheduling/shiftcenter/shift-center-overview.md | #how-are-items-displayed %}. Schedules displays deleted activities in gray without the name. The original time information will remain visible, except in the daily view.
