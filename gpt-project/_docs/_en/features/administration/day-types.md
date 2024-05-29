---
title: Create and use day types
description: Create day types to represent holidays and other special days that change your business hours.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/configure-planning-calendars.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-public-holidays.md
---

Day types define the days with standard business hours and days with different business hours.

Add day types to your {% link_new planning unit | features/administration/create-and-manage-planning-units.md | #add-business-hours %} to set business hours for the standard days of the week and for special days, e.g. if your organization is open on public holidays. injixo will take into account the defined business hours for those days during schedule optimization.

In _Plan > Configuration > Day types_{:.breadcrumbs} you can:

- View the default day types.
- Create, edit, and delete custom day types.

## Create a custom day type

On some days, your business hours might differ from the standard, e.g. when there are special promotions or public holidays. To create custom day types for those days, follow these steps:

1. Click the New icon {% icon item-add | icon-only %} in the action bar.
2. Enter a **Name** (max. 50 characters).
3. Enter an **Abbreviation** (max. 25 characters).  
   The abbreviation will appear in the planning calendar.
4. (Optional) Check the **Holiday Mode** checkbox.<br>[Learn more](#holiday-mode) about how to configure day types for public holidays.
5. Click _OK_{:.doc-button}.

## Holiday mode

To mark a day type as a public holiday, activate the **Holiday Mode** checkbox in the day type configuration window.

### Create day types for public holidays

There are two ways to create day types for public holidays:

- Create day types with holiday mode and {% link_new add them to your planning calendar | features/administration/configure-planning-calendars.md | #configure-a-planning-calendar %}.

- Add a {% link_new calendar template | features/administration/configure-planning-calendars.md | #configure-a-planning-calendar %} to your planning calendar. This will automatically create all included day types for public holidays with activated holiday mode.

Holiday mode will reduce people's working hours on this day accordingly. If you decide to schedule the day as a normal working day, you can always deactivate the holiday mode by {% link_new editing the day type | features/administration/day-types.md | #edit-a-day-type %}.

## Edit a day type

> Warning
>
> If you change the holiday mode of a day type that is currently in use, you must recalculate time accounts or {% link_new target work accounts | features/scheduling/planning-periods/target-work-accounts.md %}.

1. Select a day type from the list.
2. Edit the data that you want to change.
3. Click _OK_{:.doc-button}.

## Delete a day type

> Note
>
> Before you delete a day type, {% link_new remove it from all planning calendars | features/administration/configure-planning-calendars.md | #remove-day-types-from-the-planning-calendar %}. You cannot delete default day types.

1. Select a day type from the list.
2. Click the {% icon item-delete %} in the action bar.

## Day types in scheduling

injixo considers day types during scheduling.

- If your planning unit is regularly open on a public holiday, you only need to {% link_new add business hours to the planning unit | features/administration/create-and-manage-planning-units.md | #add-business-hours %}.
- If your planning unit is closed on a public holiday, or if it is open with special opening hours, read the article {% link_new Schedule public holidays | best-practices/scheduling-public-holidays.md %}.
