---
title: Outbound calls
description: Calculate employee requirements for outbound calls.
toc: true
product_label:
  - advanced
  - enterprise
  - classic
---

To determine staff requirements for campaigns with outgoing calls, use the Calls - Outbound requirement script.  The calculation is based on the total number of contacts addressed in the campaign, the campaign duration, and the expected average handling time for each call.

## Prerequisites

If you do not want to use a fixed value for your outgoing calls, export your forecast first:

1. Go to _Forecast_{:.menu-item}.
2. Select a **Workload** from the drop-down menu.
3. Select a **Time frame**.
4. In the **Volume and AHT** section, click _Use Forecast_{:.doc-button}. 
5. In the **Prepare Forecast for staff requirement calculation** window that opens, select your forecast version.
6. Click _Use this Forecast_{:.doc-button}.
7. Click _Close_{:.doc-button}.

## Select the script

1. Go to _Forecast_{:.menu-item}.
2. On the right side, click **Calculations for Multi-Activity, Constant Requirement and Outbound**.
3. Click _Select a requirement script_{:.doc-button}.
4. Select **Calls - Outbound** from the drop-down menu.
   A new window opens and displays the Requirement Script (Outbound Calling).

## Configure the script
 
In the script window, you can configure the following parameters:

| Parameter                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Queue                        | Select the queue for which you want to use the script.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Records                      | The total number of target contacts for your campaign.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Contact rate (%)             | The percentage of answered outgoing calls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Redial rate (%)              | Several redial attempts are made and distributed over the selected date range. Example: You want to reach a total of 5,000 contacts during a campaign. A redial rate of 10% means that 500 unreached contacts will be redialed (second attempt). Next, 50 redials are made (third attempt), and so on. This continues until the number of unanswered calls is less than 1. In this example with 5,000 target contacts, the resulting number of contacts is 5,555. |
| Start date                   | Beginning of the date range for the calculation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| End date                     | End of the date range for the calculation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Right party connect rate (%) | The Right Party Connect (RPC) rate determines the percentage of calls that reach their intended target, because a dialer cannot distinguish whether the call is answered by the right person, the wrong person (e.g. a spouse) or an answering machine. Select fixed and enter a fixed value in the field below, or select variable and select a value type with forecasted connect rates.                                                                                                              |
| Shrinkage (%)                | (Optional) Indicates how much productive time the contact center loses because paid people are on an unscheduled break or on sick leave, etc. This value compensates for the lost time so that the service goal remains achievable.                                                                                                                                                                                                                                                                           |
| Average handling time        | Select fixed or variable. <!-- add AHT definition? -->                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| RPC in seconds               | Average handling time (in seconds), including after-call work for a call with the correct contact person.                                                                                                                                                                                                                                                                                                                                                                                                           |
| WPC in seconds               | Average handling time (in seconds) for a call with someone who is not the correct contact person.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Planning Unit                | The planning unit for the calculation. If you change the planning unit, the activity field will update and display all selectable activities that are assigned to the planning unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Activity                     | Activity for which you want to write staff requirements.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Minimum Staff                | Minimum number of people per interval. Enter a value to overwrite intervals with lower values.                                                                                                                                                                                                                                                                                                                                                                            |
| Maximum Staff                | Maximum number of people per interval. Enter a value to overwrite intervals with higher values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Run the script

After you have configured the script, click _OK_{:.doc-button} to start the calculation. A window will display your input parameters and the script execution results. Check the {% link_new saved staff requirements in the Shift Center | features/scheduling/employee-requirement.md %}.

{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %} <!-- keep this or move to classic article? -->

{{ 1 | image: 'Outbound Script UI', '80%' }}
