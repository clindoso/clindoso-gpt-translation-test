---
title: Calculate staff requirements
redirect_from:
  - /staff-requirement/
redirect_reason: used in intercom forecast product tour
product_label:
  - advanced
  - enterprise
  - classic
description: Calculate staff requirements for calls, chat, email & more.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-backoffice-linear.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-asa.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-abandoned-calls.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-outbound.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/employee-requirement.md
---

The last step in forecasting is to calculate staff requirements using one of several calculation methods. To set where staff requirements are saved, select a planning unit and an activity in your workloads. You can also write constant staff requirements without a forecast.

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first.

## Available calculation methods

There are several calculation methods for staff requirements available in injixo. To learn how to configure a calculation method, click the links below:

- {% link_new Erlang-C, Linear, and Chat | features/forecast/injixo-forecast/staff-requirement.md | #configure-integrated-calculation-methods %}
- {% link_new Multiactivity | features/forecast/requirement-scripts/requirement-multiactivity.md %}
- {% link_new Outbound | features/forecast/requirement-scripts/requirement-outbound.md %}
- {% link_new Back office | features/forecast/requirement-scripts/requirement-backoffice-linear.md %}
- {% link_new Abandonment rate | features/forecast/requirement-scripts/requirement-abandoned-calls.md %}
- {% link_new Average speed of answer | features/forecast/requirement-scripts/requirement-asa.md %}
- {% link_new Constant requirement | features/forecast/requirement-scripts/requirement-constant.md %}

Note: Read the article {% link_new Choose the correct requirement script | best-practices/requirement-scripts.md %} to learn which method best suits your use case.

## Configure integrated calculation methods

The integrated methods update staff requirements calculation results based on new data imports, changed calculation parameters, or {% link_new manual adjustments | features/forecast/injixo-forecast/manual-adjustments.md %}.

1. Go to _Forecast_{:.doc-button} and select a workload.
2. Scroll to the **Staff Requirements** section:

   - In a new workload, click _Configure calculation parameters_{:.doc-button}.
   - To change the configured calculation method, click _Edit Calculation Method_{:.doc-button}.

3. In the **Calculation Method** drop-down menu, select Erlang C (for calls), Chat, or Linear (for storable volumes).
   Note: Learn more about [the Other option](#additional-calculation-methods), also available in the drop-down menu.

4. In the **Calculation parameters** section, configure the [calculation parameters](#calculation-parameters) for the selected calculation method.
5. In the **Storage Location** section, select a Planning Unit and an Activity. If you [transfer staff requirements for scheduling](#transfer-staff-requirements-for-scheduling), you will save it here.

6. Click _Save Configuration_{:.doc-button}.

### Calculation parameters

There are different mandatory and optional parameters that depend on the selected calculation method:

| Parameter                         | Details                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Target Service Level              | Percentage of incoming calls or chats to be handled within the Target Answer Time                                                                                                                                                                                                                                                                          |
| Target Answer Time                | Time in which the percentage of calls or chats specified in the Target Service Level parameter should be handled, e.g. 80% of the calls in 20 seconds.                                                                                                                                                                                                     |
| Shrinkage                         | The percentage of unplanned absences, e.g. for toilet and drinking breaks, employees coming in late, unexpected sick leave or technical issues. To get to the total number of required employees including shrinkage `(s%)`, divide the number of employees by `(1 - s%)`. If you need 70 agents and the shrinkage is 10%, you need 78 employees in total. |
| Minimum Required Staff            | Enter a value to overwrite intervals with lower values. Shown as a horizontal line in the daily view.                                                                                                                                                                                                                                                      |
| Maximum Required Staff            | Enter a value to overwrite intervals with higher values. Shown as a horizontal line in the daily view. Note: The entered values can overwrite the originally calculated staff requirements values.                                                                                                                                                         |
| Fixed Average Handling Time (AHT) | Enter a value to overwrite the forecasted AHT with a fixed value. Select **Apply the fixed AHT only when no AHT value is available** to use the fixed AHT value only for periods, in which no AHT value is available as a fallback. By default, the staff requirements calculation uses the AHT values from the forecast.                                  |
| Maximum Sessions                  | Maximum number of parallel chat sessions employees can handle at a time.                                                                                                                                                                                                                                                                                   |
| Overhead                          | Percentage of AHT that an employee must spend on tasks that they cannot do in parallel, i.e. adding after-call notes to the CRM system. This parameter will have no effect if you enter 1 for Maximum Sessions                                                                                                                                             |

### View calculated staff requirements

The **Staff Requirements** section at the bottom of the page displays a graph with the calculated staff requirements. Above the graph, you can see the configured values for the parameters and the total person-hours required for the selected period.

Hover over the graph to see a tooltip with volume, AHT, and people required for the interval (in daily view) or person-hours for the day (weekly and monthly view). If you have configured a fixed average handling time, the tooltip displays the fixed value instead of the forecasted AHT.

{{ 1 | image: 'Graph for Staff Requirements'}}

### Transfer staff requirements for scheduling

Transfer staff requirements for a time period to create optimized schedules or run a job optimization.

1. Go to _Forecast_{:.doc-button} and select a **workload**.
2. In the daily, weekly, or monthly view, select a **time period** for which you want to transfer staff requirements.
3. (Optional) In the **Staff Requirements** section, select a **forecast version**, or the **imported forecast** for the staff requirements calculation from the drop-down menu on the right.

   > The selected value defaults to Auto-Forecast.
   >
   > Forecast versions and the imported forecast must have been previously stored for the selected time period. Learn more about {% link_new forecast versions | features/forecast/injixo-forecast/store-forecast-versions.md %} or how to {% link_new import a forecast | features/forecast/injixo-forecast/import-forecast.md %}.

4. In the **Staff Requirements** section, click _Use Requirements_{:.doc-button}.  
   A new window will show the selected time frame, planning unit, and activity.  
   If you have not selected a planning unit and activity when setting up the calculation method for the workload, you will see the message: Not assigned. To fix it, close the window and click **Edit Calculation Method**.

5. To transfer the staff requirements, click _Save_{:.doc-button}.  
   Staff requirements for your activity has been stored.  
   You can repeat the steps for the next workload or continue with your scheduling process.

<!-- Header used in intercom forecast tour -->

## Additional calculation methods

The other two methods to calculate staff requirements require to run a script and configure the parameters in a separate window.

| Method             | Usage                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Other              | Calculation methods for back office, calculations based on average speed of answer, and abandonment rates.               |
| Additional scripts | Calculation methods for multiactivity, outbound, and the option to write constant staff requirements without a forecast. |

### Set up the Other calculation method

1. Go to _Forecast_{:.doc-button} and select a **workload**.
2. In the **Staff Requirements** section, click _Edit Calculation Method_{:.doc-button}.
3. In the **Calculation Method** drop-down menu, select **Other**.
4. Click _Save_{:.doc-button}.

Run the scripts as follows:

1. Select the **time period**, for which you want to save staff requirements.
2. Click _Use Forecast_{:.doc-button}.  
   The results are transferred to WFM.
3. In the **Staff Requirements** section, select a script from the drop-down menu.
4. In the new window or tab, configure the parameters. Select the following values for the Queue and Version parameters:
   - Queue parameter: The queue that has the same name as the workload starting with an asterisk (\*).
   - Version parameter: The Auto-Forecast version
5. To run the script, click _OK_{:.doc-button}.  
   A window displays the calculation results.

### Calculate requirement for multiactivities or outbound campaigns

1. Go to _Forecast_{:.doc-button} and select a **workload**.
2. Select the **time period**, for which you want to create staff requirements.
3. To transfer the forecast for the desired time period into the Auto-Forecast version, click _Use Forecast_{:.doc-button}.

   > Before you start the script for multiactivities, click _Use Forecast_{:.doc-button} in each workload for the subactivities.

4. Click **Calculations for Multiactivity, Constant Requirement and Outbound** in the upper right.
5. Select a **requirement script** from the drop-down menu.
6. In the new window or tab, configure the parameters. Select following values for the Queue and Version parameters:
   - Queue parameter: The queue that has the same name as the workload starting with an asterisk (\*). For multiactivities, select the correct subactivity workloads
   - Version parameter: The Auto-Forecast version
7. To run the script, click _OK_{:.doc-button}.  
   The staff requirements values are saved. A new window displays the calculation results.

## Write constant staff requirements

1. Go to _Forecast_{:.doc-button}.
2. Click **Calculations for Multiactivity, Constant Requirement and Outbound**.
3. Select the **constant requirement script** from the **drop-down** menu.
4. In the new window or tab, configure the parameters. Learn more about {% link_new the Constant requirement script | features/forecast/requirement-scripts/requirement-constant.md %}.
5. To run the script, click _OK_{:.doc-button}.  
   The staff requirements values are saved. A new window displays the calculation results.
