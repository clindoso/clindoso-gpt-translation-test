---
title: Abandonment rate
description: Calculate employee requirements based on an abandon rate goal.
toc: false
product_label:
  - advanced
  - enterprise
  - classic
---

In this article, you will learn how to configure and run the _Calls - Abandonment-Rate_ requirement script.

## What is the script for?

The _Calls - Abandonment-Rate_ requirement script calculates the employees required to handle the forecasted call volume for an activity. Use this script if your service goals include a certain abandonment rate.

## Prerequisites

The script needs three input parameters:

- The average time before a caller hangs up (typically recorded by your telephony system)
- The percentage of calls to be answered
- The number of seconds it takes to answer the defined percentage of calls

{% include reusables/{{ page.lang }}/scripts/cloud-prerequisites.md %}

## Run the script

1. Select the script **Calls - Abandonment-Rate** from the drop-down menu **Select a requirement script** at the bottom of the workload page.
2. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
5. {% include reusables/{{ page.lang }}/scripts/steps/version.md %}
6. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
7. {% include reusables/{{ page.lang }}/scripts/steps/activity.md %}
8. Set an **Abandon Rate (%)** and a **Time until Abandon (sec.)**. These parameters define the percentage of abandoned calls and the waiting time that callers remain on the line before hanging up. For instance, the script assumes that if you answer 93% of calls in N seconds, 7% of calls will be abandoned.
9. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}
   {% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}

10. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
11. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}
12. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
13. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}
14. Click _Ok_{:.doc-button} to start the calculation.

A window will pop up. It shows your input parameters and the script execution results. You can check the {% link_new stored employee requirement values in the Shift Center | features/scheduling/employee-requirement.md %}.

{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}

{{ 1 | image: 'Abandoned Calls Script UI', '80%' }}
