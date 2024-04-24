---
title: Outbound calls script
description: Calculate staff requirements for outbound calls.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /requirement-outbound/
redirect_reason: Updated filename on 18 March 2024
---

Use the Outbound calls requirement script to calculate staff requirements for campaigns with outgoing calls. The calculation is based on the total number of contacts addressed in the campaign, the campaign duration, and the expected average handle time (AHT).

## Prerequisites

To calculate staff requirements with a forecasted call distribution, start by exporting the forecast:

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select the time frame using the date picker. Click on a week number to select the whole week, or click any day and drag to select a period shorter or longer than a week.
3. From the {% icon ellipsis_v %} at the top right, select **Use forecast**.
4. In the **Use this forecast to calculate staff requirements** window, select the forecast you want to use.
5. Click _Use forecast_{:.doc-button}.
6. Click _Close_{:.doc-button}.

Alternatively, you can use the Outbound calls requirement script to calculate staff requirements without a forecast. Learn how to configure the parameters accordingly in the [Campaign Data section table](#campaign-data-section).

## Configure the script

1. Go to _Forecast > Requirement Scripts_{:.breadcrumbs}.
2. In the **Calls-Outbound** tile, click _Open_{:.doc-button}.  

The script configuration window includes three sections. Learn how to configure the parameters in the tables below.

### Campaign Data section

| Parameter                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Queue                        | Select the queue for which you want to use the script.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Records                      | The total number of target contacts for your campaign. Select **fixed** and enter a value in the field below to calculate staff requirements without a forecast. Select **variable** and select a value type with forecasted target contacts.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Contact rate (%)             | The percentage of answered outgoing calls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Redial rate (%)              | The percentage of contacts that are attempted again after unsuccessful attempts. The redial attempts are distributed over the date range you configure with the **Start date** and **End date** parameters. Learn more about the redial rate in the [dedicated section below](#what-is-the-redial-rate). |
| Start date                   | Beginning of the date range for the calculation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| End date                     | The end of the date range for the calculation. Select **Date** and enter a date in the field below, or select **Campaign Duration Days** and enter a value in the field below.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Right party connect rate (%) | The percentage of calls that are answered by the intended people. Select **fixed** and enter a value in the field below, or select **variable** and select a value type with forecasted right party connect rate.                                                                                                                                                                                                                                                             |
| Shrinkage (%)                | (Optional) The percentage of paid time during which people are not available to handle contacts, due to, for example, unscheduled breaks or sick leaves.     |

### Average Handling Time section

| Parameter        | Description                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fixed/variable   | Select **fixed** and enter fixed values in the fields below, or select **variable** and select value types in the fields below.                                                                                                                                                                                                                         |
| RPC in seconds   | AHT, in seconds, for a call with the right contact person. This value includes the after-call work.                                                                                                                                                                                                                                                       |
| WPC in seconds   | AHT, in seconds, for a call answered by the wrong party, such as a call that is answered by the wrong contact person or a call that is forwarded to voicemail.                                                                                                                                                                                          |

### Employee workload section

| Parameter        | Description                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Planning Unit    | The planning unit for which you want to calculate the staff requirements. If you change the planning unit, the **Activity** drop-down menu updates and displays all the activities assigned to the planning unit. |
| Activity         | The activity for which you want to calculate the staff requirements.                                                                                                                                            |
| Minimum Staff    | The minimum number of people required per interval. Enter a value to overwrite intervals with lower staff requirements.                                                                                          |
| Maximum Staff    | The maximum number of people required per interval. Enter a value to overwrite intervals with higher staff requirements.                                                                                         |

## Run the script

- To start the calculation, click _OK_{:.doc-button}.<br>A window opens and displays the input parameters you selected and the script results.

You can see the {% link_new saved staff requirements in Shift Center | features/scheduling/edit-or-delete-staff-requirements.md %}.

Note: In injixo Enterprise on-premise, go to _WFM > Forecast > ForecastPro > Forecast_{:.breadcrumbs} or _WFM > Administration > Forecasting > Scripts_{:.breadcrumbs}. The script requires an existing forecast for the combination of queue, value type, and version. The script name may vary because you can enter a custom name when creating the script.

## What is the redial rate?

The redial rate is the percentage of calls that are attempted again after unsuccessful attempts. The process of making additional attempts (known as redials) continues until the number of unanswered calls is less than 1.<br>Example: You want to reach a total of 5,000 people. A redial rate of 10% means that 500 unanswered calls are redialed during the second attempt, 50 unanswered calls are redialed during the third attempt, 5 unanswered calls are redialed during the fourth attempt. In this case, the total number of attempted calls is 5,555.
