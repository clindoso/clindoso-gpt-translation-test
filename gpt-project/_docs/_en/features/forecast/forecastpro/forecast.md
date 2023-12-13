---
title: Create forecasts and employee requirements
product_label:
  - on-premise
---

In the course of the forecast process, a forecast for a value type is created from imported, calculated, or forecast data and a requirement is determined from this. A forecast can be created for value types whose data is stored.

## Forecast - Forecast

The forecast data is stored in a forecast version - usually in the 'Standard' version. The employee requirements are transferred to SchedulePro as a planning basis.

The prerequisites for the forecast process are fulfilled if you have created a typical daily curve for each event type of the week and a typical weekly curve for the forecast period.

The forecast process consists of three steps, which are explained below:

1. forecast of the weekly values with determination of the base volume
2. forecast of the daily values
3. determination of requirement and execution of scripts

To make a forecast, open the menu item _Forecast_{:.menu-item}.

### Parameter Selection for the forecast

In the processing category `Parameters` you select the origin of the data for the forecast.

| Source Queue | Select the queue whose typical weekly distribution curves and typical daily curves you want to use for the forecast (usually "Historical Data"). |
| Value Type | First determine the value type for the forecast and then select the target queue (usually "incoming calls" and "average processing time") |
| Target Queue | In this field, select the queue under which the predicted values are stored. If time zone display is activated, the time zone of the source and target queue must be identical. Only queues that contain the same value type as the source queue are displayed in the selection field. Source queue and target queue can be identical. |
| Weekly Distribution Curve | You can specify a user-defined weekly curve for the forecast if you have saved data in a user-defined weekly curve in the menu item _Typical weekly curve_{:.menu-item}. This allows you to make a forecast for different queue value type combinations without having to create a typical week curve for each one. This procedure is recommended if the same weekly pattern applies to several queue value type combinations. If you want to create differentiated forecasts for each individual queue value type combination, choose 'Standard'. |
| Source version | Specify the version whose data is to be used for the forecast (usually the 'Historical' version with the data from the external system). |
| Target version | Select the version in which the forecast data is to be saved (usually the 'Standard' version with the planning data). |
| Forecast Start date | Enter the start of the forecast period here. The start date should be the first weekday of a planning week, since the typical weekly curve starts on this day. The end is determined automatically by the program. A forecast is created for the length of the stored Typical Weekly Curve. If the start date were on a different weekday than the first, e.g. on the third, the forecast values for the first and second day would not be based on the most current typical week curve. |
| Forecast End date | The end date is determined automatically by the program. The forecast period has the same length as the stored typical weekly curve. |

Complete your details and then change to the processing category `Forecast of weekly values`.

### Editing Category Forecast of the Weekly Values

Select the evaluation period for the calculation of the base volume in the processing category `Forecast of the Weekly Values`.

| Start of Evaluation | Enter the start of the evaluation period from which the base volume is to be calculated. The start date must correspond to the first day of the planning week. The forecast evaluates weekly curves from day 1 to day 7 of a planning week. If the weekday of the start date and day 1 of the planning week differ, the base volume cannot be calculated correctly. The calculation of a trend requires the specification of a period of at least two typical weekly curves. |
| End of Evaluation | Enter the end date for the evaluation period. The end date must be the same as the last weekday of the planning week. |

Confirm your selection with _Apply_{:.doc-button}. The `table window`, `diagram window` and `edit window` will appear.

## Forecast of the Weekly Values

In the Forecast of the Weekly Values editing category, you determine the base volume or the base average of the value type for the forecast. The value can be entered manually in the Base Volume field or determined using available data.

For each weekly curve of the selected period, the weekly total of the specified value type is displayed. The total or the average only takes into account data within the opening hours.

## Forecast of the Daily Values

After you have determined the base volume for the forecast in the processing category "Forecast of the Weekly Values", you create a forecast for all event types in the forecast period in the processing category "Forecast of the Daily Values".

| Forecast Date | Select the date for which the daily values are to be displayed after the calculation. The name of the event type is displayed in the Event Type field. |
| Event Type | This field automatically displays the name of the event type that is assigned to the date selected in the 'Forecast Date' field in the forecast calendar. |

To calculate the forecast of the daily values, confirm your selection by clicking on _Calculate_{:.doc-button}. A `table window` and a `diagram window` will open for the day set in the `Forecast Date` field.

By selecting a date you can control the forecast value for each event type and correct it manually if necessary. The dates are stored in the target version selected for the forecast. You can change the forecast values and thus the curve manually. Enter the corrected value for the period in the table column of the forecast daily curve. The change in the curve is then visible in the `diagram window`.

If the predicted daily volume is to be changed, you can change the total value in the last row of the table. The new total value is automatically distributed to the intervals according to the daily curve.

To save the changed forecast data, click _Save_{:.doc-button} for each event type.

> Note
>
> If you want to check or edit predicted daily version values later, the data in the menu item _Edit Daily Distribution Curves_{:.menu-item} is usually displayed in the version 'Standard'. The forecast values can be adapted to changed situations at short notice. Possible are changes of single 'daily interval values', changes of the 'daily total values', changes of the 'sum of all daily total values' within the display period or the increase or reduction of all daily interval values. You can also create a completely new daily curve. The predicted curve can be influenced.

## Calculation of Requirements and Execution of Scripts

The employee requirement can be determined if you have carried out the forecast of the weekly values and the forecast of the daily values for the forecast period in the menu item _Forecast_{:.menu-item} or have edited the individual daily curves in the menu item _Edit Daily Distribution Curves_{:.menu-item}.

You can start the script to determine the requirement in the same menu item in the editing category `Requirement calculation`.

Depending on the desired staff calculation, it is necessary to forecast the weekly and daily values for each value type. For example when using the staff calculation script "Calls - Single Activity (Erlang C)". Here, the forecast should be made before the staff calculation for the value types "incoming calls" and "average processing time".

### Processing Category requirement Calculation

The staff calculation is available in the menu items _Forecast_{:.menu-item} and _Edit Daily Distribution Curves_{:.menu-item} under the processing category `Requirement calculation`.

Select the script you want to use to determine the requirement.

Click _Run_{:.doc-button} to select one of the scripts. In the script execution parameter dialog, enter the parameters required for the calculation (see the documentation for each script).

After you have entered all the information correctly, confirm the execution of the script with _Ok_{:.doc-button}. The script will be executed. The employee requirement is now calculated and saved. A validity check is performed by the planning rule _2606_{:.id-label} _Activity assignment to the planning units_. If the calculation or transfer of the employee requirements violates a planning rule with the status 'hard', the employee requirements are not determined or saved. After successful completion of the calculation and transfer process, the calculation result is displayed in the 'Forecast window'.

### Forecast - Log for Script Execution

You will receive a log with the exact content of the staff calculation.

When the script processes forecast data, the log displays the forecast volumes for each day of the forecast period for the selected value types along with the resulting employee requirements per interval. The employee requirement is only calculated for the period within the operating hours of the queue, even if the requirement exceeds the opening hours.

The calculated {% link_new employee requirements | features/scheduling/employee-requirement.md %} are available in injixo for further processing.
