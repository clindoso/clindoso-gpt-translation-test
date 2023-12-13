---
title: Edit daily distribution curves
product_label:
  - on-premise
---

In _Forecasting > ForecastPro > Edit Daily Distribution Curves_{:.breadcrumbs} you can adjust interval values imported from external systems that you consider untypical. These could, for example, be days with a different volume or zero values due to failures on the ACD. Using this you can create new typical daily curves. You can also use this function to adjust predicted daily curves from the forecast of daily values to short-term changes in process volume or process duration. The staff calculation can be started via the same menu item, where the changed values are taken into account.

## Editing Category Parameters

| Queue | Select the queue whose daily curves you want to control or edit. |
| Value Type | Select the value type whose day curves you want to control or edit. |
| Version | Select the version whose day curves you want to control or edit. Historic or Forecast|
| Start date | Specify the start date from which the day curves are to be displayed. |
| End date | Specify the end date up to which the daily curves are to be displayed. |

Confirm your selection with _Apply_{:.doc-button}. The `Table Window` and `Diagram Window` will appear. All interval values within the selected time period are displayed in ascending order.

If you display several day curves in a graph, not all interval points of a day curve are visible. As soon as you select a single day curve in the table for editing, all associated interval times are displayed again. Click _Total values_{:.doc-button} to return to the view of all daily curves.

The table adds in the column `Total Values` for each interval values of all curves. In the line `Sum` all daily interval values of a daily curve are added. The Total Values column shows the daily interval values of all daily curves in the Sum row. It corresponds to the sum of all operations (or the average operation duration) in the display period.

> Note
>
> The changes to the course of the daily curves are not automatically saved.

The values of the edited daily curves can be saved in the selected version by clicking on _Save_{:.doc-button}.

Note: By saving the version data in the version 'Historical' you overwrite your imported data.

### Create Daily Curve

You can create daily curves in the `table window` as well as in the `graph window` or calculate them in the editing category `Calculation`. The calculation function is the fastest solution.

For rows in which the total value of an interval is 0 and for columns in which the sum of all intervals of a daily curve is also 0, you can only enter daily interval values for an interval of any daily curve. The row Sum, the column Total Values and the total of the total values are updated accordingly.

The curve is displayed in the `graph window`.

> Note
>
> To edit a curve in the graph window, first select the corresponding day in the table. As soon as you have selected a day in the table, only the curve of this day will be displayed in the graph window.

Then set the course and interval values of the daily curve by dragging the interval points to the desired position. The table values are updated.

## Using Calculation Section

> Note
>
> To edit a day curve in the `Calculation` editing category, first select the day in the table for which the calculation is to be performed.

The following option pairs can be combined for the calculation.

**Option Pair 1**

Use this option to create new daily curves. For example, if you enter the options 'Interval', 'Overwrite' and 'Absolute' and the value 50 for a curve with zero values, the value 50 is written for each day interval in the specified interval.

- `Time Slot`: Activate this option if you want the value to be added to each daily interval value in the specified interval in full.
- `Day`: Activate this option if the specified value is to be distributed proportionally to all daily interval values. You cannot use this option to create new daily curves.

For each option you can check the `Observe Business Hours` checkbox if you want the daily curve to be created only within the operating times of your queue.

If you have decided to calculate timeslots, then perform the calculation one after the other for each timeslot, specifying the corresponding start time and end time. The entry 00.00 o'clock in the End time field is interpreted as 24.00 o'clock.

> Note
>
> Note that the `Time Slot` option adds the specified value to each day interval in full, while the `Day` option divides the value proportionally among all day intervals. Curves containing only zero values can therefore only be calculated with the `Interval` option.

**Option Pair 2**

- `Increase/Decrease`: Activate this option if the specified value is to be added to or subtracted from the existing daily interval values according to the selected option Interval or Day in Full or Proportional.
- Overwrite: Activate this option if each daily interval value is to be overwritten by the specified value according to the selected option `Time Slot` or `Day` in full or in part.

**Option Pair 3**

This option cannot be used to create new curves.

- `Percentage`: Activate this option if the specified value is a percentage value to be added to the daily interval values according to the `Time Slot` or `Day` option selected.
- `Absolute`: Activate this option if the specified value is to be added to each daily interval value according to the selected `Time Slot` or `Day` option in full or in part.

If you start the staff calculation after editing a daily curve in the menu item _Edit Daily Distribution Curves_{:.menu-item}, the saved version data is used for staff calculation and staff calculation method execution.

Save your created curves in the version 'Historical', if they should be available in the menu item _Typical Daily Distribution Curves_{:.menu-item} for the creation of a typical daily curve.

### Edit Daily Curves

You can edit a day curve in the `table window`, in the `graph window` or in the `calculation` editing category.

The following values can be edited:

- The interval value of any daily curve. The line `Sum` is updated. The `Total Values` column is also updated.
- The sum of all interval values of a day, if not equal to 0. All interval values of the day are updated. The value is distributed among the daily intervals in such a way that the ratio of the values to each other is maintained. If the value for an interval is 0, this value is retained. All values in the Total Values column, including the total value for all totals, are also updated.
- The total value of all totals, if not equal to 0. All interval values of all curves are updated. The value is distributed over all intervals in such a way that the ratio of the values to each other is maintained. If the value for an interval is 0, this value is retained. All values in the line `Total` and in the column `Total Values` are also updated.
- The total value of all curves for an interval in the `Total Values` column, if it is not equal to 0. All daily interval values are updated. The total value is divided among the daily interval values in such a way that the ratio of the values to each other is maintained. If the value for the interval for a curve is 0, this value is retained. All values in the `Total Values` column, including the total value for all totals, are also updated.

> Note
>
> To edit a curve in the `diagram window`, you must first select the corresponding tag in the table. To return to the overview of all day curves, click the column header `Total Values`. No curve can be edited for the `Total Values` column. As soon as you have selected a day in the table, only the curve of the selected day is displayed in the `diagram window`.

Then set the course and interval values of the daily curve by dragging the interval points to the desired position. The table values are updated.
