---
title: Find replacement employees for activities, full days or understaffed shifts
product_label:
  - advanced
  - enterprise
  - classic
description: Find employees to cover absences or understaffed shifts. Learn also how to exchange shifts between two employees.
redirect_from: /find-functions/
redirect_reason: renamed file in March 2021
---

In this article, you will learn how to:

- find a replacement employee for a certain activity or shift or for a full day.
- find employees for understaffed shifts.
- exchange activities and day models between two employees.

New to the Shift Center? Learn {% link_new the basics | features/scheduling/shiftcenter/shift-center-overview.md %} first.

## Find a replacement employee

If a scheduled employee cannot perform a certain activity or shift or cannot work for a full day (e.g. due to sick leave), you have to find a replacement employee. This employee needs the skills to take over the respective activities or shifts.

To find a replacement employee for a full day:

1. In the schedule window, click the column header of the day to expand the day.
2. Right-click a cell in the expanded day.
3. Select **Find replacement employee for day...** or press **CTRL + Q**.

To find a replacement for a single activity:

1. In the schedule window, right-click the **activity** in the expanded day.
2. Select **Find Replacement Employee...** or press **CTRL + R**.

{{ 1 | image: "Find replacement employee Context menu", '50%' }}

In both cases, a list of employees appears which possess the skills to take over the activities or shifts. You can now select additional options to further filter the employees shown in the list:

1. Click the **Options** tab.
   - Choose the option **Observe** in the row _Selections_ if you want to only show replacement employees that belong to the same selection group(s) as the employee.
   - In the row _Placements_, you can decide to only show employees **With the same working hours and the same date**, with **At least one placement on the same scheduled day** or with **No placements on the same scheduled day**. The last two options refer to whether or not there are already elements in the employee's schedule on the scheduled day.
2. Go back to the **Replacement Employee** tab. If there are no replacement employees who meet your filter criteria, the tab will remain greyed out. Otherwise, it shows skilled employees which meet your filter criteria.
3. Click a **replacement employee**. The line is highlighted. This action can (partly) replace any existing activities or shifts in employees' schedules.
   {{ 2 | image: "Find replacement employee details", '60%' }}
4. Click _Ok_{:.doc-button}. Before performing the replacement, injixo checks whether the scheduling rules have been adhered to. The schedule items are then moved to the selected employee.

## Find employees for understaffed shifts

The parameter window shows understaffed shifts in red. To find an employee for an understaffed shift:

1. Switch to the **Day Models** tab.
2. Right-click a **data cell** and select **Find Employees for Shift...**.
   {{ 3 | image: "Find replacement employee details", '60%' }}
3. On the **Employee** tab, you will see the day model and its start time. For day models of type _Variable Shift_, you can adjust the **Start Time**. Below, you see a list of employees who are available for the understaffed shift you selected.
   {{ 4 | image: "Find replacement employee details", '60%' }}
4. Go to the **Options** tab. Here, you can further filter the employees shown in the list. If you select **None on the same booking day** for _Placements_, only those employees are shown which don't have any shifts on the selected day.
5. Go back to the **Employees** tab. If there are no replacement employees who meet your filter criteria, the tab will remain greyed out. Otherwise, it shows skilled employees which meet your filter criteria.
6. Select an **employee**. Note that the employees might already have activities or shifts in their schedule on that day which might get (partly) replaced.
7. Confirm the day model assignment with _Ok_{:.doc-button}. Before performing the assignment, injixo checks whether the scheduling rules have been adhered to.

## Exchange shifts between two employees

<!-- move into separate article -->

You can exchange all activities and shifts of a given day between two employees.

1. Right-click a **day cell** in the schedule window.
2. Select **Find Exchange Partner**. A list of employees appears whose skills and contract parameters match those of the selected employee.
   {{ 5 | image: "Find exchange partner context menu", '60%' }}
3. Click the **Options** tab to select additional filter criteria.
   - Choose the option **Observe** in the row _Selections_ if you want to only show replacement employees that belong to the same selection group(s) as the employee.
   - In the row _Placements_, you can decide to only show employees **With the same working hours and the same date**, with **At least one placement on the same scheduled day** or with **No placements on the same scheduled day**. The last two options refer to whether or not there are already elements in the employee's schedule on the scheduled day.
4. Go back to the **Find Exchange Partner** tab. If there are no replacement employees who meet your filter criteria, the tab will remain greyed out. Otherwise, it shows skilled employees which meet your filter criteria.
5. Select an **employee** and click _Ok_{:.doc-button} to confirm the exchange. Before performing the exchange, injixo checks whether the scheduling rules have been adhered to.
   {{ 6 | image: "Select exchange partner ", '60%' }}
