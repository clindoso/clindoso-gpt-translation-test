---
title: View predicted service levels
product_label:
  - advanced
  - enterprise
description: Learn how to view predicted service levels for every scheduled activity in injixo.
---

In injixo, you can set up a view for predicted service levels per planning unit for every contact-related activity (e.g. call, chat, email) that you schedule for each interval of a day.
You only need to set up the configuration once for each relevant activity to display it in Shift Center. When you manually move shifts in Shift Center, the service level values in the parameter window will adapt automatically.

> Note
>
> You can only view predicted service levels for individual activities, not for multiactivities.

## Prerequisites

Before you can view the calculated values for predicted service levels, you need a workload including the following data:

- Offered contact volumes
- AHT
- Calculated staff requirements

### Transfer forecast and staff requirements data

To display the workload data in Shift Center, proceed as follows:

1. Go to _Forecast > Workloads_{:.breadcrumbs} and select the relevant workload.<br>The Workloads details page opens.
2. Select the period for which you want to transfer the forecast.
3. Click the three-dot menu on the right and select the **Use forecast** option.
4. In the dialog window, click _Use forecast_{:.doc-button} to confirm.
5. In the **Staff Requirements** section of the Workload details page, click _Save staff requirements_{:.doc-button}.
6. In the dialog window, click _Save_{:.doc-button} to confirm.

## Add the value type to the queue

1. Go to _WFM > Administration > Forecasting > Queues_{:.breadcrumbs}.
2. Select the queue with an asterisk. The queue has the same name as the [workload you transferred data from](#transfer-forecast-and-staff-requirements-data).
3. In the queue configuration window, go the the **Value Types** section.
4. To add a new value type, click the {% icon plus %}.
5. In the **Value Types** dialog window, select a value type. The name of the value type must match the channel of your workload. The name starts with the channel and ends in Predicted Service Level, e.g. **Calls Predicted Service Level** for a call workload.
6. Click _OK_{:.doc-button}.

Repeat this procedure for every queue for which you want to view predicted service levels.

## Configure the value type

For all Predicted Service Level value types, define the target answer time.

1. Go to _WFM > Administration > Forecasting > Queues_{:.breadcrumbs}.
2. Select the queue for which you want to configure the Predicted Service Level value type.
3. In the queue configuration window, go to the **Value Types** section.
4. Click the {% icon pencil %} next to the Predicted Service Level value type.<br>The **Value Types** configuration window opens.
5. In the configuration window, configure the value type:

   - **Planning unit** and **Activity**: From the drop-down menus, select the planning unit and activity for which you want to view the predicted service levels.
   - **Target Answer Time**: Enter the time in seconds according to your organization's Service Level Agreements.

6. Click _OK_{:.doc-button}.

## Configure how predicted service levels are displayed

1. Go to _WFM > Administration > Planning Units_{:.breadcrumbs}.
2. Select the planning unit for which you want to view predicted service levels.
3. In the planning unit configuration dialog, go to the **User-Defined Parameters** section.
4. Click the {% icon item-add %}.<br>The **User-Defined Parameters** configuration dialog opens.
5. In the configuration dialog, configure the parameters as follows:

- **General** section: Enter a unique name for the parameters. This name will be displayed in the heatmap in Shift Center.
- **Input for the Parameter** section: From the drop-down menus, select the queue that contains the historical data the forecast is based on (e.g. \*Inbound Customer Service), and the corresponding value type (e.g. Calls Predicted Service Level). Keep Auto-Forecast as the default option for Version. This way, the values will be continuously updated.
- **Display Heatmap** section: Make sure the checkbox is checked. Define an upper and lower limit for the service level value. Select the colors in which the values will be displayed in Shift Center. Find out more about the [ranges of values](#ranges-of-values).
- **Display in Infothek**: Make sure the checkbox is unchecked.

6. Click _OK_{:.doc-button}.

### Ranges of values

The ranges define the upper and lower limits of your organization's agreed service levels. Depending on what your target service levels are, you might want to configure the limits differently. For example, if the minimum acceptable value is 80%, set the lower limit to 80.
You can color-code values that exceed the upper or do not meet the lower limit. To highlight overstaffed periods, set the upper limit to a value below 100, e.g. 99.

## View predicted service levels in Shift Center

1. Go to _Plan > Shift Center_{:.breadcrumbs}.
2. Select the planning unit for which you want to view the predicted service levels.
3. At the bottom of the screen, select the **User-Defined Parameters** tab.  
   The screen shows a heatmap of the values you configured.
