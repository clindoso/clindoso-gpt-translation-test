---
title: Adjust the forecast
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

Edit a generated forecast to remove irregularities from the contact volume or the average handle time (AHT).

Adjust the forecast if any of the following conditions apply:

- You do not have enough historical data, or your data is not correct.
- Your contact volume or AHT values deviate from current trends and you do not expect them to change back. Such deviations could be due, for example, to structural changes in your business.
- Your contact volumes are unusually high or low during a specific period, for example during a marketing campaign. Remove these irregularities, or {% link_new add an outage | features/forecast/injixo-forecast/events-and-holidays.md  |#add-an-event-or-an-outage-to-a-workload %} to exclude the period from the forecast calculation.

New forecast calculations do not overwrite manually adjusted values.

## Adjust the volume

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select a time frame from the date picker.<br>The time frame you select determines the adjustment options.
3. In the volume section, click _Adjust volume_{:.doc-button}.
4. In the window, configure your adjustment:
  - **Date range**: Available if you selected a time frame of several days in step 2.
  - **Start time** and **End time**: Available if you selected a time frame of one day in step 2.
  - **alter (%)**: To adjust the current value (volume) by a percentage.
  - **overwrite**: To replace the current value (volume) with a new value (positive whole number).
  - **Value**: The value (volume) can be a positive or a negative number.
Learn [how volume and AHT values are adjusted](#how-do-time-frames-affect-volume-and-aht-adjustments).
5. Click _Apply adjustment_{:.doc-button}.<br>
   Changes are highlighted in the volume graph. Hover over the graph to see a tooltip with more details about your contact volume, AHT, staff requirements, and events.

## Adjust the AHT

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select a time frame from the date picker.
3. Next to **AHT**, click the {% icon eye_slash %}.
4. Click _Adjust AHT_{:.doc-button}.
5. In the window, configure your adjustment:
  - **Date range**: Available if you selected a time frame of several days in step 2.
  - **Start time** and **End time**: Available if you selected a time frame of one day in step 2.
  - **alter (%)**: To adjust the current value (AHT) by a percentage.
  - **overwrite**: To replace the current value (AHT) with a new value (positive whole number).
  - **Value**: The value (AHT) can be a positive or a negative number.<br> Learn [how volume and AHT values are adjusted](#how-do-time-frames-affect-volume-and-aht-adjustments).
6. Click _Apply adjustment_{:.doc-button}.<br>
  Changes are highlighted in the AHT graph. Hover over the graph to see a tooltip with more details about your contact volume, AHT, staff requirements, and events.
 
Repeat this procedure to readjust values if there is a significant difference between the generated forecast and your manual adjustment. The fields do not show the values previously entered but remain blank. Another percentage increase or decrease for a period updates the value modified before, not the original value.

## How do time frames affect volume and AHT adjustments?

Adjustments have a different impact based on the time frame you selected in the date picker:

| Value  |      Time frame              |  Impact of the adjustment   
| ----------- | ---------------------------- | ------------------------------------------------------------------------------------------------------ | 
| Volume |     Single day      | A percentage value decreases or increases the existing values for all intervals within **Start time** and **End time**.<br> An absolute value overwrites the existing values for all intervals within **Start time** and **End time**.                                               |
| Volume | Several days | Both a percentage value and an absolute value increase or decrease the total volume. The value distributes proportionally over the selected period, preserving the interval trends and distribution patterns.                                                                      |
|  AHT   |     Single day     | A percentage value decreases or increases the existing values for the intervals included within **Start time** and **End time**.<br> An absolute value overwrites the existing values for each interval included within **Start time** and **End time**.                                                                                       |
|  AHT   | Several days | A percentage value and an absolute value increase or decrease the total weighted average displayed. AHT values are distributed over the selected period, preserving the interval's trends and distribution patterns. This may cause higher or lower values on one or more days. |

> Missing AHT values
>
> If a day shows no AHT values, you can only adjust the AHT for a single day and not for a longer time range.
>  To adjust the AHT for a single day, use absolute values.  
> If you enter a contact volume greater than zero, you will see the changed AHT in a view with several days.

## Delete adjustments

You can delete adjustments that are no longer relevant.

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select a time frame from the date picker.
3. Select the adjustments you want to delete:
  - In the volume section, click _Adjust volume_{:.doc-button}.
  - In the **AHT** section, click _Adjust AHT_{:.doc-button}.
4. Select a **Date range**.
5. Click _Clear all adjustments_{:.doc-button} to remove all adjustments from the time frame.<br>
  injixo displays the original forecast values for the selected time frame.

## Use staff requirements for scheduling

Manual adjustments will automatically recalculate the staff requirements.

If you configured the staff requirements calculation on the workload page, you can use the new values for scheduling by clicking _Save staff requirements_{:.doc-button}.<br>
To use the adjusted values for the Multiactivity, Outbound, or Constant requirement script, proceed as follows:

1. From the three-dots menu _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} at the top right, select **Use forecast**.
2. In the window, click _Use forecast_{:.doc-button}.
3. In _Forecast > Requirement Scripts_{:.breadcrumbs}, select a script.
4. Configure and run the script.<br>Learn how to configure the {% link_new Multiactivity script | features/forecast/requirement-scripts/requirement-multiactivity.md %}, the {% link_new Outbound script | features/forecast/requirement-scripts/requirement-outbound.md %}, and the {% link_new Constant requirement script | features/forecast/requirement-scripts/requirement-constant.md %}.
