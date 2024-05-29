---
title: Calculate staff requirements
redirect_from:
  - /staff-requirement/
redirect_reason: Updated filename on 04 March 2024
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Calculate staff requirements for calls, chat, email & more.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/multiactivity-script.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/outbound-calls-script.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
---

After you have generated a forecast, you can calculate staff requirements. You can choose from several requirement scripts and calculation methods available in injixo. You can also write constant staff requirements without a forecast if needed.

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first.

## Calculation methods and requirement scripts

injixo offers calculation methods and requirement scripts.
Learn which {% link_new requirement script or calculation method is the best | best-practices/requirement-scripts.md %} for your use case.<br>
Learn how to configure the [calculation methods](#configure-the-calculation-methods) in the next section.<br>
To learn how to configure the requirement scripts, click the following links:

- {% link_new Multiactivity script | features/forecast/requirement-scripts/multiactivity-script.md %}
- {% link_new Outbound script | features/forecast/requirement-scripts/outbound-calls-script.md %}
- {% link_new Constant requirement script | features/forecast/requirement-scripts/requirement-constant.md %}

## Configure the calculation methods

The calculation methods calculate staff requirements based on new data imports, changed calculation parameters, or {% link_new manual adjustments | features/forecast/injixo-forecast/manual-adjustments.md %}.
You can change your calculation method at any time.

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. In the **Staff requirements** section, click _Edit staff requirements_{:.doc-button}.
3. From the **Calculation method** drop-down menu, select an option:
   - **Erlang-C**
   - **Chat**
   - **Linear**
4. In the **Calculation parameters** section, configure the [calculation parameters](#calculation-parameters).
5. In the **Associated planning unit and activity** section, select the planning unit and the activity for which you want to use the staff requirements.  
   Learn more about [using staff requirements for scheduling](#use-staff-requirements-for-scheduling).
6. Click _Save_{:.doc-button}.

The graph in the **Staff requirements** section shows the calculated staff requirements within business hours. Learn how to {% link_new activate business hours | features/forecast/injixo-forecast/forecast-activate-business-hours.md %}.<br> Under the graph you can see the configured values for the parameters and the total person-hours required for the selected period.<br> Hover over the graph to see detailed information about the volume, the AHT, the staff requirements, any manual adjustments, and added events per interval.

### Calculation parameters

The following table includes the parameters that you can configure for each calculation method:

| Parameter                       | Description                                                                                                                                                                                                                                                                          | Configurable in Erlang-C | Configurable in Chat | Configurable in Linear |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ | -------------------- | ---------------------- |
| Target service level            | Percentage of incoming calls or chats to be handled within the target answer time.                                                                                                                                                                                                   | Yes                      | Yes                  | No                     |
| Target answer time              | Time in which the percentage of calls or chats specified in the target service level parameter should be handled.                                                                                                                                                                    | Yes                      | Yes                  | No                     |
| Shrinkage                       | The percentage of paid time during which people are not able to work, due to, e.g., restroom breaks, lateness, unplanned sick leaves, or technical issues.                                                                                                                           | Yes                      | Yes                  | Yes                    |
| Minimum required staff          | Enter a value to overwrite intervals with lower staff requirements values.                                                                                                                                                                                                           | Yes                      | Yes                  | Yes                    |
| Maximum required staff          | Enter a value to overwrite intervals with staff requirements values.                                                                                                                                                                                                                 | Yes                      | Yes                  | Yes                    |
| Fixed average handle time (AHT) | Enter a value to overwrite the forecasted AHT.<br>Check the checkbox **Apply the fixed AHT only when no AHT value is available** to use the fixed AHT value only for periods without AHT data. By default, the staff requirements calculation uses the AHT values from the forecast. | Yes                      | Yes                  | Yes                    |
| Maximum sessions                | Maximum number of parallel chat sessions that people can handle at a time.                                                                                                                                                                                                           | No                       | Yes                  | No                     |
| Overhead                        | Percentage of AHT that a person must spend on tasks that they cannot do in parallel, i.e. adding after-call notes to the CRM system. This parameter will not be considered if you enter 1 in the **Maximum sessions** field.                                                         | No                       | Yes                  | No                     |

## Use staff requirements for scheduling

To create a schedule based on staff requirements, you need to save them first. To save staff requirements, follow the steps described below.

You can only use staff requirements calculated for forecast versions or imported forecasts that you have saved for the period you select.<br>
Learn more about {% link_new forecast versions | features/forecast/injixo-forecast/save-forecast-versions.md %} or how to {% link_new import a forecast | features/forecast/injixo-forecast/import-forecast.md %}.

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select the period for which you want to use staff requirements.
3. In the **Staff requirements** section, select a forecast version from the drop-down menu on the left.
4. Click _Save staff requirements_{:.doc-button}.
5. In the **Save staff requirements** window, click _Save_{:.doc-button}.

injixo saves the staff requirements for the planning unit and activity that you selected while configuring the calculation method.

> Note
>
> You can use the staff requirements for a different planning unit or activity. <br> To do so, repeat the procedure to [configure the calculation method](#configure-the-calculation-methods), and select a different planning unit or activity. Then, follow the procedure to [use staff requirements for scheduling](#use-staff-requirements-for-scheduling).
