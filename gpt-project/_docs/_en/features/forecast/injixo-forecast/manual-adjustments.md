---
title: Adjust the forecast
product_label:
  - advanced
  - enterprise
  - classic
description: Make manual adjustments to your forecasted contact volumes and AHT.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/events-and-holidays.md
---

You can edit a generated forecast to remove irregularities from the contact volume or the average handle time (AHT).

Adjust the forecast if any of the following conditions apply:

- You do not have enough historical data, or your data is not correct.
- Your contact volume or AHT values deviate from current trends and you do not expect them to change back. Such deviations could be due, for example, to structural changes in your business.
- Your contact volumes are unusually high or low during a specific period, for example during a marketing campaign.<br> In this case, remove the irregularities, or {% link_new add an outage | features/forecast/injixo-forecast/events-and-holidays.md  | #add-an-event-or-an-outage-to-a-workload %} to exclude the period from the forecast calculation.

New forecast calculations do not overwrite manually adjusted values.

## Adjust the volume

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select a time frame from the date picker. Click on a week number to select the whole week, or click any day and drag to select a period shorter or longer than a week.<br>The time frame you select determines the adjustment options shown.
3. In the volume section, click _Adjust volume_{:.doc-button}.
4. In the configuration window, configure your adjustment:
  - **Date range**: Available if you selected a time frame of several days in step 2.
  - **Start time** and **End time**: Available if you selected a time frame of one day in step 2.
  - **alter (%)**/**overwrite**: Select one option from the drop-down menu.<br>**alter (%)** adjusts the current volume value by a percentage, that can be a positive or negative number.<br>**overwrite** replaces the current volume value with a new value, that must be a positive whole number.
  - **Value**: Enter a value to alter or overwrite the volume.<br>Learn [how volume and AHT values are adjusted](#how-do-time-frames-affect-volume-and-aht-adjustments).
5. Click _Apply adjustment_{:.doc-button}.<br>
   Changes are highlighted in the volume graph. Hover over the graph to see more details about your contact volume, AHT, staff requirements, and events.

## Adjust the AHT

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select a time frame from the date picker. Click on a week number to select the whole week, or click any day and drag to select a period shorter or longer than a week.
3. Next to **AHT**, click the {% icon eye_slash %}.
4. Click _Adjust AHT_{:.doc-button}.
5. In the configuration window, configure your adjustment:
  - **Date range**: Available if you selected a time frame of several days in step 2.
  - **Start time** and **End time**: Available if you selected a time frame of one day in step 2.
  - **alter (%)**/**overwrite**: Select one option from the drop-down menu.<br>**alter (%)** adjusts the current AHT value by a percentage, that can be a positive or negative number.<br>**overwrite** replaces the current AHT value with a new value, that must be a positive whole number.
  - **Value**: Enter a value to alter or overwrite the AHT.<br> Learn [how volume and AHT values are adjusted](#how-do-time-frames-affect-volume-and-aht-adjustments).
6. Click _Apply adjustment_{:.doc-button}.<br>
  Changes are highlighted in the AHT graph. Hover over the graph to see more details about your contact volume, AHT, staff requirements, and events.
 
Repeat this procedure to readjust values if there is a significant difference between the generated forecast and your manual adjustment. 

>Note
>
> If you readjust volume or AHT values, the configuration window does not show the values you entered previously. Another percentage increase or decrease for a period updates the value adjusted before, not the original value.

## How do time frames affect volume and AHT adjustments?

Adjustments have a different impact based on the time frame you selected in the date picker:

| Value  |      Time frame              |  Impact of the adjustment   
| ----------- | ---------------------------- | ------------------------------------------------------------------------------------------------------ | 
| Volume |     Single day      | A percentage value decreases or increases the existing values for all intervals within **Start time** and **End time**.<br> An absolute value overwrites the existing values for all intervals within **Start time** and **End time**.                                               |
| Volume | Several days | Both a percentage value and an absolute value increase or decrease the total volume. The value distributes proportionally over the selected period, preserving the  trends and distribution patterns for all intervals.                                                                      |
|  AHT   |     Single day     | A percentage value decreases or increases the existing values for the intervals included within **Start time** and **End time**.<br> An absolute value overwrites the existing values for all intervals included within **Start time** and **End time**.                                                                                       |
|  AHT   | Several days | Both a percentage value and an absolute value increase or decrease the total weighted average displayed. AHT values are distributed over the selected period, preserving the trends and distribution patterns for all intervals. This may result in higher or lower values on one or more days. |


## Delete adjustments

You can delete adjustments that are no longer relevant.

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select the adjustments you want to delete:
  - In the volume section, click _Adjust volume_{:.doc-button}.
  - In the **AHT** section, click _Adjust AHT_{:.doc-button}.
3. Select a **Date range**.
4. Click _Delete all adjustments_{:.doc-button} to remove all adjustments from the selected date range.<br>
  injixo displays the original forecast values for the selected date range.

## Use staff requirements for scheduling

Manual adjustments automatically recalculate the staff requirements.

If you {% link_new configured the staff requirements calculation | features/forecast/injixo-forecast/calculate-staff-requirements.md %} on the workload page, you can use the new values for scheduling by clicking _Save staff requirements_{:.doc-button}.<br>
To use the adjusted values for the Multiactivity, Outbound, or Constant requirement script, proceed as follows:

1. From the {% icon ellipsis_v %} at the top right, select **Use forecast**.
2. In the configuration window, click _Use forecast_{:.doc-button}.
3. In _Forecast > Requirement Scripts_{:.breadcrumbs}, select a script.
4. Configure and run the script.<br>Learn how to configure the {% link_new Multiactivity script | features/forecast/requirement-scripts/multiactivity-script.md %}, the {% link_new Outbound script | features/forecast/requirement-scripts/outbound-calls-script.md %}, and the {% link_new Constant requirement script | features/forecast/requirement-scripts/requirement-constant.md %}.
