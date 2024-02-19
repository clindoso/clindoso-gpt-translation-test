---
title: Schedule public holidays
description: Learn how to handle public holidays in your schedule.
product_label:
  - advanced
  - enterprise
  - classic
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
---

Public holidays can be challenging for scheduling and operations.
injixo supports you in the following:

- Visualizing the public holiday in your schedule
- Blocking your schedule if your planning unit is closed
- Accommodating changes in your business hours as compared to normal days

## Open: Treat public holidays as workdays

If your planning unit is open regularly on public holidays, you don't need to change your schedules. Handle any public holidays as normal working days.

## Open with different business hours (planning calendar)

If your contact center is open on a public holiday, but has different business hours, use a planning calendar. injixo must adhere to the minimum working hours per week. Day models and the working hours defined in contracts must comply with business hours.

1. Create a {% link_new Planning calendar | features/administration/planning-calendar.md %}.
2. Add all relevant public holidays. If your planning unit is closed on weekends, do not add any holidays on weekends.
3. Assign the Planning calendar {% link_new to your planning unit | features/administration/create-and-manage-planning-units.md %}.
4. In the **Business Hours** section of the planning unit, add the public holidays.
5. In the **From** and **To** fields, enter the business hours for each day.  
   On public holidays, injixo will only generate staff requirements and schedule people within the business hours. Other days will not be affected.

Note: Scheduling rule _2631_{:.id-label} _Check contractual ban on work scheduled for holidays (both day models and activities)_ checks the holiday mode. If the scheduling rule and the corresponding checkbox in the contract are activated, you cannot assign activities or day models to employees on public holidays.

> Tip: Public holidays on weekends
>
> If you use the planning calendar and holiday mode, but your planning unit is basically closed on weekends, remove all public holidays that fall on a weekend from the planning calendar. This way, injixo can determine the correct number of working days for the week.

## Closed: Use paid full-day absence activities

If your planning unit is closed on public holidays, schedule a paid full-day activity of type Absence to block injixo from creating a schedule for such days:

1. Create an activity of type Absence, such as Public Holiday.
2. Check the checkboxes **Paid** and **Allow as Full-Day Activity**.
3. Assign the activity to your planning unit.
4. Schedule the Public Holiday activity for all employees on public holidays.  
   Tip: To add the activity, you can use the **Employee** tab in the dialog in Shift Center. Learn more about {% link_new adding multiple items at once | features/scheduling/shiftcenter/add-and-delete-items.md | #add-items-to-multiple-employees-at-once %}.

injixo determines the target working time for the days as follows:

| Configured contract option             | Details                                                                             |
| -------------------------------------- | ----------------------------------------------------------------------------------- |
| Work Time Guidelines                   | injixo calculates the value (Target Work Time per Week / by Number of Working Days) |
| Working Hours for Each Day of the Week | injixo considers the value entered for the weekday                                  |

Users with the Agent role can see the public holidays in their calendars in _Me > My Calendar_{:.breadcrumbs}.

## Closed: Use the planning calendar

If your planning unit is closed on public holidays, you can also add public holidays to a planning calendar, which you assign to your planning unit. Your planning unit is automatically closed on such days, when you do not assign any business hours to the public holidays you add to your planning unit.

Public holidays reduce the working hours per week and using a planning calendar can cause problems depending on your contract configuration, for example with such contract:

- Working time per week of 40 hours over five days
- Minimum and target working time per day of eight hours

With one public holiday in a week, injixo can only schedule four working days with eight hours each. Create optimized schedules cannot schedule people where the contractual minimum working hours (of 40 hours) per week cannot be met. Even if the minimum number of four working days could be adhered to, no schedule will be created.

Calculation example for the above contract:

- `(Scheduled Working Time / Number of Working Days) * (Number of Working Days - Public Holidays)`
- `(40 hours / 5 days) * (5 - 1) = 32 hours`

To allow injixo to create a schedule, you would need to lower the values for the minimum working hours to 32 hours and for the minimum number of working days per week to 4 days. The downsides with this approach is that you need to change the contracts for weeks with public holidays (and revert the change for normal weeks again). Also, injixo could schedule a four-day week in weeks without public holidays with this configuration if you are overstaffed.

To avoid the need to change contracts on a regular basis, better use the paid full-day absence activities described above.

Note: If the contractual working time is defined in the **Working hours for each day of the week** section, use a paid full-day absence. Otherwise, optimized scheduling cannot create a schedule for such contracts. On the one hand, optimization must schedule a certain number of working hours on certain days, and on the other hand, there are no opening hours on one of these days.

## Visualize public holidays (Shift Center)

When you work with a planning calendar to schedule public holidays, the Shift Center will highlight public holidays in the planning unit for which you have added the planning calendar. If you do not use the planning calendar, you can still visualize public holidays in day cells in a separate planning unit, which does not affect your scheduling:

1. Create a separate planning unit and assign a planning calendar. Do not add people or activities.
2. Add a leading underscore or blank space to the name of the new planning unit, e.g. \_Calendar.  
   Because the Shift Center displays planning units in alphabetical order, the new planning unit shows up in first position.

   {{ 5 | image: 'Planning unit for displaying public holidays', '90%' }}
