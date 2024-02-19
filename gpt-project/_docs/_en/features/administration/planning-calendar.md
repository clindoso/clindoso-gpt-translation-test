---
title: Create and use planning calendars
description: Set up planning calendars to automatically adjust your operating hours for holidays and other days with special business hours.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/day-types.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-public-holidays.md
---

In this article, you will learn:

- what planning calendars are and how they work.
- how to create, edit, copy and delete them.
- how to add public holidays and day types.
- how to use a planning calendar for scheduling.

## What is a planning calendar?

With a planning calendar, you can mark days with different opening hours and staffing needs (e.g. marketing campaign days or public holidays) to ensure they are automatically considered during scheduling.

The days are marked using {% link_new day types | features/administration/day-types.md %}. If you enter a day type in the planning calendar, it overwrites the opening hours of the normal weekday (Mon-Sun) for that day.

It might make sense to create different planning calendars for different planning units or regions. A calendar can span multiple years.

{{ 1 | image: 'empty planning calendar' }}

## Create a planning calendar

1. Go to _WFM > Administration > Scheduling > Planning Calendar_{:.breadcrumbs}
2. Click the {% icon item-add %} in the action bar. Start editing the empty calendar below.
3. Click _![save as button](/assets/img/common/saveas.gif)_{:.doc-button-icon} in the action bar to save the empty calendar.
4. Enter a **Name** for the calendar and click _Ok_{:.doc-button}.

Now you can automatically add the public holidays of your region and single day types.

### Add the public holidays of your region

1. Go to in _WFM > Administration > Scheduling > Planning Calendar_{:.breadcrumbs}
2. Select the **Year** for which you want to add public holidays.
3. Select your country and region from the drop-down menu below **Calendar Template**.
4. Click _Apply_{:.doc-button} to insert all public holidays from the template. Repeat steps 1 to 3 if you want to add the public holidays of another region or if you want to add the same public holidays to another year. Note that if you insert the public holidays of another template, some days that already contained public holidays can be overwritten with the new data.
5. Click _![save button](/assets/img/common/save.gif)_{:.doc-button-icon} in the action bar to save the calendar.

When you insert a calendar template, injixo automatically creates the {% link_new day types | features/administration/day-types.md %} for all special days included in the template if they do not exist yet.

The inserted days are automatically configured as public holidays by activating the _Holiday Mode_ in the settings of the day type. If you want to treat a certain public holiday as a normal workday in the working time calculation, deactivate the public holiday mode manually at _WFM > Administration > Scheduling > Day Types_{:.breadcrumbs}.

On days where your planning unit is closed but employees do not receive holiday pay, you should delete day types with holiday mode from the calendar. Otherwise, injixo will reduce the target working time for this week and employees will be scheduled for fewer hours than normal.

### Add custom day types to the planning calendar

Make sure you first {% link_new create the day types | features/administration/day-types.md %} you want to add.

1. Select **Insert Day Type**.
2. Select the **day type** you want to add from the drop-down menu.
3. To add the day type to a day, click a **day cell** within the planning calendar. You can only assign one day type per day. If you click a cell that already contains a day type, it will be overwritten.
4. You can use _![undo button](/assets/img/common/undo.gif)_{:.doc-button-icon} and _![redo button](/assets/img/common/redo.gif)_{:.doc-button-icon} in the action bar to undo and redo your changes.
5. Repeat the process for other day types you want to add.
6. Click _![save button](/assets/img/common/save.gif)_{:.doc-button-icon} in the action bar to save the calendar.

### Remove day types from the planning calendar

Remove day types from the planning calendar using one of these options:

- Select the option **Delete** and then click a cell within the planning calendar to delete its day type.
- Click the **Clear Year** button to delete the calendar content for the displayed year.
- Click the **Delete All** button to delete the calendar content for the entire calendar time range.

## Modify or copy an existing planning calendar

1. Use the **Calendar** drop-down menu in the action bar to select a calendar of your choice. To copy a planning calendar before editing, click _![save as button](/assets/img/common/saveas.gif)_{:.doc-button-icon} in the action bar.
2. Add or remove day types, or insert a calendar template with public holidays as described above. You can also rename the calendar by clicking _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon} in the action bar.
3. Click _![save button](/assets/img/common/save.gif)_{:.doc-button-icon} to save the calendar.

## Use a planning calendar for planning

To use a planning calendar, assign it to a planning unit under _WFM > Administration > Scheduling > Planning Units_{:.breadcrumbs}:

1. Select the **Planning Unit**.
2. Scroll to the **Planning Calendar** section.
3. Click the {% icon item-add %}.
4. Choose a **Planning Calendar**. You can assign a single calendar which contains several years. If you want to assign different planning calendars for each year, choose each calendar one at a time and use **Valid from** and **Valid To** to set the time period when it should be used.
5. Click _Ok_{:.doc-button}

If your planning unit contains subordinate planning units, the planning calendar is _not_ automatically assigned to them. If required, assign the planning calendar manually.
