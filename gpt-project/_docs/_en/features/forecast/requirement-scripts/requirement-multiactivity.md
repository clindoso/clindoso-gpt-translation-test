---
title: Multiactivity script
description: Calculate employee requirements for multiskilled people.
toc: true
product_label:
  - advanced
  - enterprise
  - classic
---


The Calls - Multiactivity requirement script calculates staff requirements for your multiactivities. The calculation requires a forecast for each subactivity, and is based on Erlang-C using a service level.

## Prerequisites

Create at least one {% link_new multiactivity | features/administration/activity-types-and-properties.md | #subactivities %} and assign it to your planning unit. In Forecast, create a separate workload for each subactivity of the multiactivity.

Before you run the script, export the forecast for all subactivities:

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select the time frame using the date picker.
3. From the three-dots menu _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} at the top right, select **Use forecast**.
4. In the window that opens, select your forecast version.
5. Click _Use forecast_{:.doc-button}.
6. Click _Close_{:.doc-button}.
7. Repeat the steps 1-6 for all other subactivities.

The data required for the calculation is exported into queues that equal the workload names but start with an asterisk.

## Open the script

1. Go to _Forecast > Requirement Scripts_{:.breadcrumbs}.
2. In the **Calls - Multi-Activity** tile, click _Open_{:.doc-button}.  
A window opens with the iWFM Requirement Script (Multi-Activity).

### Time period, planning unit, and multiactivity

1. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
4. Select a **Multiactivity**.<br>
   The script window updates and displays fields for the subactivities.

### Subactivity parameters

Each subactivity can have its own calculation parameters, which are described below.

### Queue parameters

1. Select the **Calculation Method** Chat, Erlang C, or Linear.<br>
   The displayed script parameters will be updated.
2. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
5. {% include reusables/{{ page.lang }}/scripts/steps/version.md %}

### Erlang C parameters

1. {% include reusables/{{ page.lang }}/scripts/steps/service-level.md %} (not available for chats)
2. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}
    {% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}
5. (Chat only) {% include reusables/{{ page.lang }}/scripts/steps/seq-percent.md %}

## Run the script

1. To start the calculation, click _Ok_{:.doc-button}.<br> A window opens and displays the selected input parameters and the script execution results. <br>

## Check the calculation results

You can check the updated staff requirements for the selected planning unit and multiactivity in {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %} or in the parameter window in {% link_new Shift Center | features/scheduling/employee-requirement.md %} or {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}.
