---
title: Average speed of answer
description: Calculate employee requirements based on an average speed of answer goal.
toc: false
product_label:
  - advanced
  - enterprise
  - classic
---

In this article, you will learn how to configure and run the _Calls - Average Speed of Answer_ requirement script.

## What is the script for?

The _Calls - Average Speed of Answer_ requirement script calculates the minimum number of employees required to achieve your service goal based on the Average Speed of Answer (ASA). The ASA is the average waiting time before a call is answered.

## Prerequisites

{% include reusables/{{ page.lang }}/scripts/cloud-prerequisites.md %}

## Run the script

1. Select the script **Calls - Average Speed of Answer** from the drop-down menu **Select a requirement script** at the bottom of the workload page.
2. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
5. {% include reusables/{{ page.lang }}/scripts/steps/version.md %}
6. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
7. {% include reusables/{{ page.lang }}/scripts/steps/activity.md %}
8. Enter a value for **ASA (sec.)** to specify the average time in seconds in which an employee must answer calls.
9. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}
10. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
11. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}
    {% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}

12. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
13. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}
14. Click _Ok_{:.doc-button} to start the calculation.

A window will pop up. It shows your input parameters and the script execution results. Check the {% link_new saved employee requirement in the Shift Center | features/scheduling/employee-requirement.md %}.

{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}

{{ 1 | image: 'ASA Script UI', '80%' }}
