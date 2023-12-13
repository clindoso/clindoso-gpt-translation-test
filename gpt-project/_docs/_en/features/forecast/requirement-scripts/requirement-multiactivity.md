---
title: Call script for multiactivity
description: Calculate employee requirements for multiskilled agents.
toc: false
product_label:
  - advanced
  - enterprise
  - classic
---

In this article, you will learn how to configure and run the _Calls - Multiactivity_ requirement script.

## What is the script for?

Use the _Calls - Multiactivity_ requirement script to calculate staff requirements for your multiactivities. The calculation requires forecasted call volumes for each subactivity, and is based on Erlang C using a service level.

## Prerequisites

The script requires at least one {% link_new multiactivity | features/administration/activity-types-and-properties.md | #subactivities %} in injixo.

You need to export the forecast for all subactivities first:

1. Go to _Forecast_{:.menu-item}.
2. Select a **Workload** from the drop-down menu.
3. Select a **Time frame**.
4. Click _Use Forecast_{:.doc-button}.
5. Repeat the steps 2-4 for all other subactivities.

## Run the script

{% include reusables/{{ page.lang }}/scripts/cloud-special-method.md %}

1. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
4. Select a **Multiactivity**. The dialog will show more input fields for the subactivities. You need to configure them individually.
5. Select a **Calculation Method**. You can select _Chat_, _Erlang C_, or _Linear._ The selection will change the available parameters.
6. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
7. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
8. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
9. {% include reusables/{{ page.lang }}/scripts/steps/version.md %}
10. {% include reusables/{{ page.lang }}/scripts/steps/service-level.md %} It is not available for the _Calculation Method_ Chat.
11. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}
    {% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}

12. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
13. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}
14. For _Calculation Method_ chat only: {% include reusables/{{ page.lang }}/scripts/steps/seq-percent.md %}
15. Click _Ok_{:.doc-button} to start the calculation. A window will pop up. It shows your input parameters and the script execution results. Check the {% link_new saved employee requirement in the Shift Center | features/scheduling/employee-requirement.md %}.

{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}

{{ 1 | image: 'Multiactivity Script UI', '80%' }}
