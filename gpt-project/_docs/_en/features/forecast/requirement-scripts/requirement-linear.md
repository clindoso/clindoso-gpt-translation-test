---
title: Linear requirement
description: Calculate employee requirements based on a linear calculation.
toc: false
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

In this article, you will learn how to configure and run the _Linear Requirement_ requirement script.

## What is the script for?

The _Linear Requirement_ requirement script uses a linear calculation to determine the employee requirements that are needed to handle the forecasted volume for activities that can be handled asynchronously, such as emails or letters.

## Configure the built-in injixo Forecast calculation

In all injixo cloud versions, you can configure the script in injixo Forecast and use the automatic staff requirements calculation:

1. Go to _Forecast_{:.menu-item}.
2. Select a **Workload** from the drop-down menu.
3. Click _Edit Calculation Method_{:.doc-button}. (Only available on days with forecast data.)
4. Select **Linear Requirement** from the _Calculation Method_ drop-down menu.
5. In the section _Calculation Parameters_, configure the following **parameters**:

   - **Shrinkage**: the amount of time that your employees spend on breaks and unplanned absences that are not spent on processing customer queues
   - **Fixed Average Handling Time (AHT)**: the average amount of time that it takes you to handle an interaction with a customer, including post-interaction paperwork, etc.
   - **Minimum required Staff**: the minimum number of employees needed to handle the forecasted volume of calls, emails, etc.
   - **Maximum required Staff**: the maximum number of employees needed to handle the forecasted volume of calls, emails, etc.

6. In the section _Storage Location_, select a **Planning Unit** and **Activity**.
7. Click _Save configuration_{:.doc-button}.

The employee requirement is automatically calculated and appears in your workload.

## Run the script manually (on-premise only)

1. Go to _WFM > Forecast > ForecastPro > Forecast_{:.breadcrumbs} or _WFM > Administration > Forecasting > Scripts_{:.breadcrumbs}. The script requires an existing forecast for the combination of queue, value type, and version. You can run the script as part of your forecast. The script name may vary because you can enter a custom name when creating the script.
2. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
5. Select the **Version** in which your forecast is saved. By default, the version _Forecast_ or _Standard_ contains the forecast.
6. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
7. {% include reusables/{{ page.lang }}/scripts/steps/activity.md %}
8. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}
   {% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}

9. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
10. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}
11. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
12. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}
13. {Click _Ok_{:.doc-button} to start the calculation. A window will pop up. It shows your input parameters and the script execution results. Check the {% link_new saved employee requirement in the Shift Center | features/scheduling/employee-requirement.md %}.

{{ 1 | image: 'Linear Script UI', '80%' }}
