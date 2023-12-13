---
title: Create typical daily distribution curves
product_label:
  - on-premise
---

In the menu item _Typical Daily Distribution Curves_{:.menu-item} you define for each event type - for example all weekdays and special days - the distribution of the forecast values in the course of the day. The typical daily curve is used in the forecast for the distribution of the value type (e.g. number of incoming calls or average processing time). The forecast base volume is distributed to the event type on the basis of this curve.

> Note
>
> The typical daily curve only displays the distribution of the value type. The volume actually expected is not determined until the forecast.

## Editing Category Parameter

Select the display parameters for the Typical Daily Curve. By default, a typical daily curve is based on the data from the 'Historical' version. Specify a value type and a period for which data was imported from the external system into the queue. It is also possible to create the typical daily distribution curve with forecasted data from the 'Standard' version.

| Queue | Select the queue whose data you want to use. |
| Value Type | Select the value type whose data you want to control or edit. |
| Version | Select a version of the day curves. In the 'Historical' version, you can check daily curves imported from the external system and edit them to determine a typical daily curve. In the version 'Standard' you can further process predicted daily curves. |
| Start Date | Specify the start date from which the day curves of an event type are to be displayed. For a typical day curve, at least one day curve of the event type (usually from the 'Historical' version) is required. |
| End Date | Specify the end date up to which the day curves of an event type are to be displayed. |
| Event Type | Select the event type whose day curves you want to control or edit. Only the event types that have been assigned to the selected queue in the administration are offered to you. |

Confirm your selection with _Apply_{:.doc-button}. The `table window`, `diagram window` and `edit window` will appear. If a Typical Daily Distribution Curve already exists, it will be displayed as a Daily dist. curve (saved) (thick black line in the graph window). You cannot change this curve manually.

The daily curve (current) (thick red line in the diagram window) is the current typical daily curve. It already considers the course of the stored Typical Daily Curve with a weighting of 50 %. Only the data that lies within the operating times of the queue is used to determine the progression. For each value type/event type combination, all daily curves within the period appear.

For the curve display in the diagram, you can choose between a step, line, and bar form. You can define the course of a typical daily curve by manually editing the daily curve (current) (thick red line) or by determining a typical daily curve using imported data.

## Create Typical Daily Curve without Data

If you are missing data from the external system for the set period, zero values are displayed in the table window. In the diagram window, the course of the individual daily curves and the daily curve (current) are also zero.

You can manually edit the course of the daily curve (current or any other curve without data):

- in the `Table window` directly into the column of the daily curve.
- in the `Diagram window` you manually drag the points of the daily curve to the desired positions.

> Note
>
> In the menu item _Edit Daily Distribution Curves_{:.menu-item} curves can also be calculated or edited using an automated procedure.

The changes to the course of the daily curves are not automatically saved.

If you really want to save historically edited data, click the _Save version data_{:.doc-button} button. Saving the version data in the 'Historical' version overwrites your imported data. As long as you have not yet saved the values, you can still discard the changes to the curve in the `Parameters` editing category. To do this, click _Apply_{:.doc-button}.

If you have created a day curve (current) whose history you want to use as a typical day curve for the forecast, then click _Save_{:.doc-button} in the edit category `Parameters`.

The course of the daily curve (saved) (thick black line in the diagram window) will be overwritten. The previous daily curve (current) (thick red line) becomes the new typical daily curve and updates the daily curve (saved).

## Create Typical Daily Curve with Control of Daily Version Values

Day curves in the 'Historical' version show the imported data for a period of 24 hours. From all imported data, the typical daily curve only takes into account the values that lie within the operating times of the queue.

You can see from the day curves whether operations also take place outside the queue operating times and whether their quantity may require an extension of the operating times. Individual curves can contain untypical values, for example, if the external system fails. You can define a typical course of the day by making a manual correction.

The data for the individual curves is displayed in the interval specified in the administration for the queue.

You can edit the individual daily curves manually by choosing:

- in the table window to correct the values directly in the column of the respective curve.
- In the diagram window, drag the course of the faulty daily curve to the desired position.
- Weight individual curves in the editing window.

The changes to the course of the daily curves are not automatically saved. If you really want to save historically edited data, click _Save version data_{:.doc-button}. By saving the version data in the version 'Historical' you overwrite your imported data.

In the editing window, you can use the _Trends_{:.doc-button} buttons to set a trend for the weighting of all curves. You can also evaluate curves individually using the weight sliders or exclude them completely from the calculation.

As long as you have not saved the values, you can discard your changes to the curve in the editing category `Parameters`. Click _Apply_{:.doc-button}.

If you have created a daily curve (current) whose course you want to use as a typical daily curve for the forecast, save the curve in the editing category `Parameters` by clicking on _Save_{:.doc-button}.

The course of the daily curve (saved) (thick black line in the diagram window) will be overwritten. The previous daily curve (current) (thick red line) becomes the new typical daily curve and updates the daily curve (saved).
