---
title: Manually adjust the forecast
product_label:
  - advanced
  - enterprise
  - classic
description: Make manual adjustments to your forecasted contact volumes and AHT.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/events-and-holidays.md
---

In this article, you will learn:

- when to manually adjust a generated forecast.
- how to adjust volume or average handling time (AHT) values.
- the differences between volume and AHT adjustments.
- how to delete or change manual adjustments.
- how to transfer updated staff requirements for scheduling.

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first.

## When to manually adjust a generated forecast?

Modify a generated forecast to remove anomalies from the volume or AHT values.

Manually adjust the forecast calculation result if you:

- need to create a reliable forecast, but have insufficient or incorrect historical data.
- have volume or AHT values that deviate from current trends, e.g. structural changes in your business, and you don't expect them to change back.
- have unusually high or low volumes in a specific period, driven by one-off events such as a marketing campaign. Remove these anomalies or add an _Outage_ {% link_new event | features/forecast/injixo-forecast/events-and-holidays.md %} to exclude the period from the forecast calculation.

New forecast calculations do not overwrite manually adjusted values.

## Adjust volume or AHT

1. Go to _Forecast_{:.menu-item}.
2. Select a **workload**.
3. Select a **day**, **week**, or **month**.
4. Click _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} in the _Volume and AHT_ section.
5. Click **Adjust Volume**. To adjust the AHT, click **Adjust AHT**.
6. Below the graph, the **Manual adjustments** panel appears.

   {{ 1 | image: 'Manual adjustment dialog' }}

7. Adjust the **Date range** by clicking on the first and last date in the calendar. Select a **start time** and **end time** to update single intervals when using daily view.
8. Enter the **Volume** amount or **AHT** to increase or decrease the forecast. Place a minus sign preceding the value (e.g. -50) to decrease. Learn [how volume and AHT values are adjusted in detail](#differences-between-volume-and-aht-adjustments) below.
   - Choose **alter (%)** to adjust the original value by a percentage.
   - Choose **overwrite** to set the original value and the amount (positive whole number) for the **Date range**.
9. Select a **Reason for Editing** from the drop-down menu.
10. Click _Save_{:.doc-button} to apply the changes, or click _Cancel_{:.doc-button} to discard. Changes are instantly highlighted on the volume or AHT graph and visible in daily, weekly, monthly, and yearly views.

{{ 2 | image: 'Manual adjustments in injixo Forecast' }}

## Differences between volume and AHT adjustments

| Value  |      View      | Description                                                                                                                                                                                                                                                                   |
| :----: | :------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Volume |     Daily      | A percentage value decreases or increases the existing values for the selected intervals. An absolute value overwrites the selected intervals with the defined value for each interval.                                                                                       |
| Volume | Weekly/Monthly | A percentage value and an absolute value increase or decrease the total volume. The value distributes proportionally over the selected period, preserving the interval trends and distribution patterns.                                                                      |
|  AHT   |     Daily      | A percentage value decreases or increases the existing values for the selected intervals. An absolute value overwrites the selected intervals with the defined value for each interval.                                                                                       |
|  AHT   | Weekly/Monthly | A percentage value and an absolute value increase or decrease the total weighted average displayed. AHT values are distributed over the selected period, preserving the interval trends and distribution patterns. This may cause higher or lower values on one or more days. |

> Zero AHT values
>
> If a day shows no AHT values, you cannot adjust the AHT in the weekly or monthly view.  
> In the daily view, you can adjust the AHT by overwriting intervals with absolute values.  
> To see the changed AHT in the weekly or monthly view, enter a contact volume greater than zero.

## Change manual adjustments

Readjust values if there is a significant difference between the generated forecast and your manual adjustment. Use the same steps described in [Adjust Volume or AHT](#adjust-volume-or-aht).

Note: The fields do not show the values previously entered but remain blank. Another percentage increase/decrease for a period does not update the original value, but rather the value modified prior.

## Delete manual adjustments

Delete previous or obsolete adjustments.

1. Go to _Forecast_{:.menu-item}.
2. Select a **workload**.
3. Select a **day**, **week**, or **month**.
4. Click _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} in the _Volume and AHT_ section.
5. Select **Adjust Volume** or **Adjust AHT** in the displayed context menu.
6. Select a **day** or **interval(s)** from the drop-down menu.
7. Click _Clear selected Adjustments_{:.doc-button} to delete the displayed adjustment. Select _Clear all Adjustments_{:.doc-button} to remove all adjustments on the displayed day.

   {{ 4 | image: 'Dialog to clear adjustments' }}

## Transfer updated staff requirements for scheduling

For automatic calculation methods, manual adjustments will automatically recalculate the staff requirements. To use the updated staff requirements for scheduling, click _Use Requirements_{:.doc-button}.

To transfer the adjusted values for other calculation methods, click _Use Forecast_{:.doc-button}, next select your {% link_new staff requirement script | features/forecast/injixo-forecast/staff-requirement.md %}, configure the parameters, and click _OK_{:.doc-button} to run it. This will update your staff requirements using the adjusted values.
