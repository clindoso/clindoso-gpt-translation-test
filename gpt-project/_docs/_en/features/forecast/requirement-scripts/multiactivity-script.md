---
title: Multiactivity script
description: Calculate staff requirements for multiactivities.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /requirement-multiactivity/
redirect_reason: Updated filename on 06 March 2024
---

Use the Multiactivity script to calculate staff requirements for your multiactivities. The calculation is based on Erlang-C using a service level.

## Prerequisites

- Create at least one {% link_new multiactivity | features/administration/activity-types-and-properties.md | #subactivities %} and assign it to your planning unit.
- Create a {% link_new workload | features/forecast/injixo-forecast/create-workloads.md | #create-workloads %} for each subactivity of the multiactivity.

## Export the forecast for all subactivity workloads

Before you can run the Multiactivity script, export the forecasts for the workloads created of all subactivities:

1. In _Forecast > Workloads_{:.breadcrumbs}, select the workload you created for a subactivity.
2. Select the time frame using the date picker. Click on a week number to select the whole week, or click any day and drag to select a period shorter or longer than a week.
3. From the {% icon ellipsis_v %} at the top right, select **Use forecast**.
4. In the window that opens, select the forecast you want to use.
5. Click _Use forecast_{:.doc-button}.
6. Click _Close_{:.doc-button}.
7. Repeat the steps 1-6 for all the workloads created for your subactivities.

injixo saves the data required for the staff requirements calculation into queues in _WFM > Administration > Forecasting > Queues_{:.breadcrumbs}. Queues have the name of the corresponding workload with a leading asterisk, e.g.\*yourWorkloadName.

## Configure the script

1. Go to _Forecast > Requirement Scripts_{:.breadcrumbs}.
2. In the **Calls - Multi-Activity** tile, click _Open_{:.doc-button}.
3. In the script configuration window, configure the following settings:
    - In the **Date** section:
      - **Start Date**: Enter the start date for the staff requirements calculation.
      - **Number of Days**: Enter the number of days after the start date for which you want to calculate staff requirements.
    - In the **Planning Unit Parameters** section:
      - **Planning Unit** and **Multi-Activity**.<br>
      The script configuration window updates and displays the calculation parameters for the relevant subactivities.
    - In the **Subactivity** section, you can configure different calculation parameters for each subactivity. Start with the parameters in the **Queue Parameters** section:
      - **Calculation Method**: Select **Erlang-C**, **Linear**, or **Chat**.<br>The script configuration window updates and displays the relevant configurable parameters. See the [table below](#calculation-parameters-in-the-erlang-c-section) to learn which parameters are configurable for each calculation method.
      - **Queue**: Select the queue that contains the data you want to use for the calculation.
      - **Processes**: Select the value type of the contact volume, e.g. Calls Offered.
      - **Average Handling Time**: If your workloads have a forecasted average handle time (AHT), select the relevant value type. Otherwise, select **[None]**.
      - **Version**: Select **Auto-Forecast**. In injixo Enterprise on-premise, you can select a different version.

## Calculation parameters in the Erlang C section

| Parameter                         | Description                                                                                                            | Configurable in Erlang-C | Configurable in Linear | Configurable in Chat |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |--------  | -------- |
| Service Level (%)             | Percentage of contacts that should be handled within the time you configure in the **Service Sec.** parameter.                                                                                                                                                                    | Yes | No | Yes |
| Service Sec.            | Time within which the percentage of contacts you configure in the **Service Level (%)** parameter should be handled.                                                                                                                                                                                            | Yes | No | Yes |
| Add (%)                         | The percentage value by which you want to increase the calculated staff requirements. Learn how to [configure this parameter](#configure-the-add--parameter-to-account-for-shrinkage) to account for shrinkage. | Yes | Yes | Yes |
| Minimum Staff            | Enter a value to overwrite lower staff requirements.                                                                                                                                                                                                                                                     | Yes | Yes | Yes |
| Maximum Staff            | Enter a value to overwrite higher staff requirements.                              | Yes | Yes | Yes |
| Fixed Average Handling Time | If you selected a type in the **Average Handling Time** parameter in the **Queue Parameters** section, keep the default value here.<br> If you selected **[None]** in the **Average Handling Time** parameter, enter a value in seconds.                                 | Yes | Yes | Yes |
| Seq (%)                  | Percentage of AHT that people spend on tasks they cannot do in parallel, such as after-call work.                                                                                                                                                                                                                                                                                   | No | No | Yes |
| Max Sessions                          | Maximum number of parallel chats that a person can handle at a time.                                                                                                                                             | No | No | Yes |

### Configure the Add (%) parameter to account for shrinkage

To configure the **Add (%)** parameter so that it accounts for shrinkage, use the following formula, where s% is your shrinkage rate: 1/(1-s%)-1. The result expressed as a percentage is the value to enter in the **Add (%)** parameter. For example, to account for a shrinkage of 20%, the calculation is 1/(1-0.2)-1, which equals 25%.

## Run the script

- To start the calculation, click _OK_{:.doc-button}.<br>A window opens and displays the selected input parameters and the script results. <br>

## See the calculation results

You can see the updated staff requirements for the selected planning unit and multiactivity in {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %} or in the parameter window in {% link_new Shift Center | features/scheduling/edit-or-delete-staff-requirements.md %} or {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}.
