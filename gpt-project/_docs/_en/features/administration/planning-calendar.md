---
title: Configure planning calendars
description: Configure planning calendars to automatically adjust your standard business hours for days with different business hours.
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

In a planning calendar, you can use {% link_new day types | features/administration/day-types.md %} to mark days with special business hours or staffing needs (e.g. marketing campaign days or public holidays). This way, you can ensure these days are automatically considered during scheduling. If you add a day type to the planning calendar, it overwrites the standard business hours for that day. You can create different planning calendars for different planning units or regions, for example, if those have different opening hours or public holidays.

## Configure a planning calendar

Prerequisite: Before you configure a planning calendar, make sure that you have created the relevant custom {% link_new day types | features/administration/day-types.md %} you want to add to it.

1. Go to _Plan > Configuration > Planning calendar_{:.breadcrumbs}.
2. In the action bar, click the New icon {% icon item-add | icon-only %}.
3. Configure the planning calendar:
    - **Year**: Specify for which year you want to use the planning calendar.<br>To create a planning calendar that spans more than one year, for example, if you create schedules that span more than one year, use _<_{:.doc-button} and _>_{:.doc-button} to navigate to a past or future year. Then, configure each year's calendar separately.
    - **Calendar Template**: Select the public holiday region and click _Apply_{:.doc-button}.<br>The planning calendar is automatically filled with the public holidays of your selected region or country.<br>If you want to include more than one region in one planning calendar, repeat this step for every region you want to add.<br>Note: Each cell in the planning calendar can only contain one public holiday. If you select a template that includes a public holiday on the same day as a previously selected template, cells that already contain a public holiday entry are overwritten.
    - **Insert Day Type**: From the drop-down menu, select the custom day type and click every calendar cell you want to add the day type to.<br>Note: You can only assign one day type per day. If you click a cell that already contains a day type, it is overwritten. If you want to include more than one custom day type in one planning calendar, repeat this step for every day type that you want to add.
4. In the action bar, click the Save as icon _![save as button](/assets/img/common/saveas.gif)_{:.doc-button-icon}.
5. In the confirmation window, enter a name for the calendar and click _OK_{:.doc-button}.

## Remove day types from the planning calendar

If your planning unit is closed on certain days and your people do not receive any holiday pay for those days, make sure that those days are not included in your planning calendar as {% link_new day types with holiday mode | features/administration/day-types.md | #holiday-mode %}. If you do not remove those day types from your planning calendar, injixo reduces the target working time for that week and people are scheduled for fewer hours. Learn more about how to {% link_new schedule public holidays | best-practices/scheduling-public-holidays.md | #closed-use-the-planning-calendar %}.

To remove day types from the planning calendar, proceed as follows:
1. Go to _Plan > Configuration > Planning calendar_{:.breadcrumbs}.
2. To remove individual day types, click **Delete**.
3. Click every cell in the planning calendar from which you want to remove the day type.
4. (Optional) To delete all entries in the calendar for the currently selected year, click _Clear Year_{:.doc-button}.
5. (Optional) To delete all entries in the calendar for the entire time range, click _Delete All_{:.doc-button}.
5. Click the Save icon _![save button](/assets/img/common/save.gif)_{:.doc-button-icon}.


## Edit an existing planning calendar

1. Go to _Plan > Configuration > Planning calendar_{:.breadcrumbs}.
2. From the **Calendar** drop-down menu in the action bar, select the calendar you want to edit.<br>If you want to copy a planning calendar before editing, for example to use the same template and day types but for a different year, click the Save as icon _![save as button](/assets/img/common/saveas.gif)_{:.doc-button-icon} in the action bar.
3. When you have completed your changes, click the Save icon _![save button](/assets/img/common/save.gif)_{:.doc-button-icon}.

## Use a planning calendar for scheduling

To use a planning calendar for scheduling, proceed as follows:

1. Go to _Plan > Configuration > Planning units_{:.breadcrumbs}.
2. Select the planning unit to which you want to assign the planning calendar.
2. In the **Planning Calendar** section, click the New icon {% icon item-add | icon-only %}.
3. In the **Planning Calendar** configuration window, select a planning calendar.<br>You can choose a single calendar that spans several years, for example if you create a schedule that exceeds one year. If you want to assign different planning calendars for each year, choose one calendar at a time and use the **Valid from** and **Valid To** fields to set the time period when it should be used. Note that single-year planning calendars only work for single-year schedules.
4. Click _OK_{:.doc-button}

> Note
>
> If your planning unit contains children planning units, the planning calendar is not automatically assigned to them. If required, assign the planning calendar manually to each child planning unit.
