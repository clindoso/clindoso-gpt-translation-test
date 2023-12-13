---
title: Create typical weekly distribution curves
product_label:
  - on-premise
---

In the menu item _Typical Weekly Distribution Curves_{:.menu-item} you define the distribution of the forecast values in the forecast period. The typical weekly curve is used as the basis for distributing the value type over the forecast period. The base volume (or average) forecast in the forecast is distributed over the forecast period (number of weeks) on the basis of this curve. The week is the planning week configured in administration.

> Note
>
> The typical weekly curve only displays the distribution of the value type. The volume of the value type is not determined until the forecast.

To edit a typical weekly curve, open the menu item of the same name.

## Editing Category Parameter

In this editing category, select the display parameters for the typical weekly curve. By default, a typical weekly curve is based on the data from the 'Historical' version. Specify a value type and a period for which data was imported from the external system into the queue. However, it is also possible to create the typical weekly curve from forecasted data in the 'Standard' version.

| Queue | In this field, select the queue whose data you want to check or edit. |
| Value type | In this field, select the value type whose weekly curves you want to control or edit. |
| Version | In this field, select the version whose data you want to control or edit. In the 'Historical' version, you can check weekly curves imported from the external system and edit them to determine a typical weekly curve. In the version 'Standard' you can check and edit predicted weekly curves. |
| Week curve | Select a week curve if you want to save the typical week curve for a queue value type combination that deviates from the set parameters. For the same queue value type combination, select 'Default'. A typical weekly curve is always bound to a specific queue value type combination. You have the option of creating user-defined weekly curves and assigning them the queue value type combination of any typical weekly curve. This allows you to create a forecast for different queue value type combinations based on a single weekly curve. |
| Length of the weekly curve | Specify the number of weeks over which the typical weekly curve is to extend. The value range is between 1 and 55. The period for the forecast corresponds to the length of the weekly curve specified by you. This makes it possible to create typical weekly curves and user-defined weekly curves not only for the period of one week, but for a planning period consisting of several weeks up to a whole year. Note that the typical weekly curve starts on the first day of a planning week and ends on the last day of a planning week. |

> Important note
>
> Please note that the length selected here always corresponds to your forecast period. In the next step of the forecast (_Forecasting > ForecastPro > Forecast_{:.breadcrumbs}) you can set the starting point for the forecast, but the end point will be set automatically based on the weekly curve length. This means that if, for example, you have a weekly curve of length 1, but your planning rhythm is five weeks, you have to do the forecast five times to get forecast values for the whole period.

| Start date | Specify the start date from which the weekly curves are to be displayed. For a typical weekly curve at least 1 period of the length of a weekly curve (usually from the 'Historical' version) is required. |
| End date | Specify the end date up to which the weekly curves are to be displayed. |

Confirm your selection with _Apply_{:.doc-button}. The `table window`, `diagram window` and `edit window` will appear.

If a Typical Week Curve already exists, it will be displayed as a Week dist. curve (saved) (thick black line in diagram window). This curve cannot be changed.

The weekly curve (current) (thick red line) is the typical weekly curve determined from the underlying data. It already considers the course of the stored Typical Weekly Curve with a weighting of 50 %. Only the data that lies within the operating times of the queue is used to determine the daily totals.

All weekly curves within the period appear for each value type.

You can choose the curve display in the diagram.

You can define the course of a typical weekly curve by manually editing the existing weekly curve (current) (thick red line) (see [Edit typical weekly curve without data](#edit-typical-week-curve-without-data)) or by creating a typical weekly curve from imported data (see [Create typical weekly curve with control of weekly version values](#create-typical-week-curve-with-control-of-week-version-values)).



## Edit Typical Week Curve without Data

If data from the external system is missing for the set period, zero values are displayed in the `table window`. In the `diagram window` the course of the individual weekly curves as well as the weekly curve (stored) and the weekly curve (current) is also zero.

You can manually edit the course of the week curve (current or any other curve without data) by

- in the `table window` enter the values directly into the column of the weekly curve (current) or any other weekly curve.
- in the `diagram window` you manually drag the points of the week curve (current) or any week curve to the desired positions.

Since a weekly curve can consist of up to 55 weeks, each event type listed in the table column is identified by the corresponding number of the week.

As long as you have not yet saved the values, you can still discard the changes to the curve in the `Parameters` editing category. To do this, click _Apply_{:.doc-button}.

If you have created a weekly curve (current) whose history you want to use as a typical weekly curve for the forecast, then click _Save_{:.doc-button} in the editing category `Parameters`.

The course of the weekly curve (saved) (thick black line in the diagram window) will be overwritten. The previous weekly curve (current) (thick red line) becomes the new typical weekly curve and updates the weekly curve (saved).



## Create Typical Week Curve with Control of Week Version Values

Weekly curves in the 'Historical' version display the imported data of the value type per event type as a total or average value. This value only includes the data that was received during the operating time of the queue.

Individual curves can contain untypical values, for example, if the external system fails. You can define a typical weekly schedule by making a manual correction.

You can edit the weekly curves manually by correcting the values directly in the column of the respective curve in the `table window` and/or manually dragging the course of the erroneous weekly curve to the desired position in the `diagram window`.

In the `editing window` you can weight individual curves. Since a weekly curve can consist of up to 55 weeks, each event type listed in the table column is identified by the corresponding number of the week.

> Note
>
> Changes to the weekly curves do not affect stored data.
