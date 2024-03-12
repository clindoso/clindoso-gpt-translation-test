---
title: Availabilities
product_label:
  - advanced
  - enterprise
  - classic
description: Create reusable availabilities to define time frames when employees can be scheduled.
redirect_from:
  - /availability-periods/
redirect_reason: rename article September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
---

With availabilities, you can define when a person is not or only partially available for scheduling on specific days or times. You can also further narrow down the restrictions already defined by your planning units' business hours and your people's contracts.

You can only insert a shift or activity into the schedule if it fits into the configured time frame. People with no configured availability are considered to be available at all times within your business hours.

There are many uses for availabilities, for example:

- Configure fixed working days/times for each week
- Rotate availabilities across weeks
- Configure temporarily available people

By default, injixo respects availabilities when creating optimized schedules. Availabilities are not considered when generating the shifts but when shifts are assigned.

injixo only checks availabilities if the scheduling rule _2611_{:.id-label} is activated. Deactivate this rule to let your people request and be assigned shifts that are longer than their availability.

You can allow {% link_new people to enter their own availabilities | features/injixo-me/use-injixo-me/explore-injixo-me.md | #set-your-availabilities-availability %} in injixo Me up to a maximum of 14. People themselves or planners must regularly delete any obsolete entries from the list. Check these availabilities manually before creating a schedule to avoid scheduling errors.
## Configure availabilities

You can configure availabilities in two ways:

- Personal availabilities: Configure temporary or permanent availabilities for individual people in _Plan > Configuration > Employees_{:.breadcrumbs}.
- Day model availabilities: Add availabilities to shift sequences to assign the same availability to several people.

Note: Day model availabilities overwrite personal availabilities, as well as availabilities that have been manually inserted.

## Configure fixed working days/times for each week

Example: A person is only available to work on mornings from 8 AM to noon due to childcare responsibilities on Wednesdays and Fridays. You can configure their availability as follows:

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. Select the person from the list.
3. In the **Availability** section on the right, click the Add icon {% icon item-add | icon-only %}.
4. Configure the availability:
    - (Optional) **Valid from** and **Valid to**: If the availability is only valid for a certain date range, the dates limit its {% link_new validity period | features/administration/set-a-validity-period.md %}.
    - **Day Types**: Select Wednesday and Friday. Hold CTRL to select multiple entries.
    - **From**: Enter 8:00.
    - **To**: Enter 12:00.
5. Click _OK_{:.doc-button}.


## Rotate availabilities across weeks

The following subsections explain how to use availabilities to plan for the following example, or for similar use cases:

- Your contact center is open from 8&nbsp;AM to 8&nbsp;PM.
- On even weeks, planning unit A works morning shifts and planning unit B works evening shifts.
- On odd weeks, planning unit B works morning shifts and planning unit A works evening shifts.
- The morning shift is from 8&nbsp;AM to 2&nbsp;PM.
- The evening shift is from 2&nbsp;PM to 8&nbsp;PM.

### Create Availability Period day models

To {% link_new create day models | features/administration/daymodels/daymodel-creation.md %}, go to _Plan > Configuration > Day models_{:.breadcrumbs} and click the New icon {% icon item-add | icon-only %}.<br>The following example shows how to set up two day models to rotate a morning shift and an evening shift.


For the morning shift:

1. Create a new day model.
2. Configure the day model:
    - **Type**: Select **Availability Period**.
    - **Name** and **Abbreviation**: Enter a unique name and abbreviation, e.g. Availability 8&nbsp;AM - 2&nbsp;PM and Avail 8AM-2PM.
    - (Optional) **Color**: Select a color to help you identify the day model.
    - **Availability Period Start**: Enter 8:00.
    - **Availability Period End**: Enter 14:00.<br> Alternatively, set an **Availability Period Duration**. The maximum value is 48 hours.
3. Click _OK_{:.doc-button}.

For the evening shift:

1. Create a new day model.
2. Configure the day model:
    - **Type**: Select **Availability Period**.
    - **Name** and **Abbreviation**: Enter a unique name and abbreviation e.g. Availability 2&nbsp;PM - 8&nbsp;PM and Avail 2PM-8PM.
    - (Optional) **Color**: Select a color to help you identify the day model.
    - **Availability Period Start**: Enter 14:00.
    - **Availability Period End**: Enter 20:00.<br> Alternatively, set an **Availability Period Duration**. The maximum value is 48 hours.
3. Click _OK_{:.doc-button}.

### Create and assign a shift sequence

To use the two day models you just created for planning, follow these steps:


1. {% link_new Create a shift sequence | features/administration/shift-sequences.md | #create-shift-sequences %} with two **Employee rows** and a **Duration** of 14 days.<br>
2. In the shift sequence, insert the day models alternating. In row 1, add the morning day model in week 1, and the evening day model in week 2. Add the day models in the reverse order in row 2.
3. {% link_new Assign the shift sequence | features/administration/employee-overview.md | #assign-a-shift-sequence %} to your people:
    - For people in planning unit A, select the first employee row.
    - For people in planning unit B, select the second employee row.
    - Set a **reference date** to define when the shift sequence starts to be planned. Set the reference date to the day of the week when your scheduling week begins, e.g. Monday.
4. {% link_new Insert the shift sequence | features/scheduling/schedules/schedules-insert-shift-sequences.md | #insert-shift-sequences %} into your schedule.


## Configure temporary available people

Example: One of your people is only available to work from 9&nbsp;AM to 12&nbsp;PM on a certain week.<br>To configure their availability accordingly, follow the same steps as for [Configure fixed working days/times for each week](#configure-fixed-working-daystimes-for-each-week). Add the relevant {% link_new validity period | features/administration/set-a-validity-period.md %} and the correct **From** and **To** values.

## Edit availabilities

You can edit the availabilities you configured for an individual person:

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. Select the person for whom you want to edit the availability.
3. In the right side panel, click **Availability**.
4. Next to the availability you want to edit, click the {% icon pencil %}.
5. Edit the availability.
6. In the **Availability** window, click _OK_{:.doc-button}.
7. At the bottom of the right side panel, click _OK_{:.doc-button}.

If you have configured availabilities with day models of type **Availability period**, edit the day model:

1. Go to _Plan > Configuration > Day models_{:.breadcrumbs}.
2. Select the day model you want to edit.
3. Edit the day model.
4. Click _OK_{:.doc-button}.

You can also edit availabilities in Shift Center. Learn more about {% link_new how to add and delete availabilities in Shift Center | features/scheduling/shiftcenter/add-and-delete-items.md | #add-an-availability %}. For temporary changes, you can copy and paste personal and day model availabilities to a cell to convert them to manually inserted availabilities.

Shift Center displays availabilities in each level with a `<>` symbol. Hover over the symbol to see the details. In the day cells, availabilities are displayed as orange elements. In expanded day cells, people's availabilities appear as white bars underlined in orange.

## Delete availabilities

You can delete the availabilities you configured for an individual person:

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. Select the person for whom you want to delete the availability.
3. In the right side panel, click **Availability**.
4. Next to the availability you want to delete, click the {% icon item-delete %}.
5. In the **Confirmation** window, click _Yes_{:.doc-button}.
6. Click _OK_{:.doc-button}.

If you have configured availabilities with day models of type **Availability period**, delete the day model:

1. Go to _Plan > Configuration > Day models_{:.breadcrumbs}.
2. Select the day model you want to delete.
3. Click the {% icon item-delete %} in the action bar.
4. In the **Confirmation** window, click _Yes_{:.doc-button}.