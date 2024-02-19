---
title: Linear requirement (on-premise)
description: Calculate employee requirements based on a linear calculation.
toc: false
product_label:
  - on-premise
---

The Linear requirement script uses a linear calculation method to determine the staff requirements to handle the forecasted volume for activities that can be handled asynchronously, such as emails or letters.

## Configure the script

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
13. Click _Ok_{:.doc-button} to start the calculation.<br>
   A window opens with your input parameters and the script execution results. Check the {% link_new saved staff requirements in Shift Center | features/scheduling/employee-requirement.md %}.

{{ 1 | image: 'Linear Script UI', '80%' }}
