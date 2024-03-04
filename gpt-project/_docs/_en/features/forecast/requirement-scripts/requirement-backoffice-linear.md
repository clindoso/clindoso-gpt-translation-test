---
title: Backoffice linear requirement
description: Calculate employee requirements for backoffice tasks.
toc: false
product_label:
  - advanced
  - enterprise
  - classic
---

In this article, you will learn how to configure and run the _Backoffice (Linear) Requirement_ requirement script.

## What is the script for?

The _Backoffice (Linear) Requirement_ requirement script calculates the employee requirements for processing non-call-related back-office activities, such as letters, emails, and faxes, based on a linear calculation.

## Prerequisites

{% include reusables/{{ page.lang }}/scripts/cloud-prerequisites.md %}

## Run the script

1. Select the script **Backoffice (Linear) Requirement** from the drop-down menu **Select a requirement script** at the bottom of the workload page.
2. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
5. {% include reusables/{{ page.lang }}/scripts/steps/version.md %}
6. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
7. {% include reusables/{{ page.lang }}/scripts/steps/activity.md %}
8. Check the checkbox **Add to existing requirement** to add the calculation result to an already existing requirement. Uncheck it to overwrite an existing requirement.
9. Optional: Enter a value for **Addition (%)** to increase the calculated requirement by a fixed percentage, e.g. to account for shrinkage.
   {% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}

10. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
11. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}
12. Define back-office-specific parameters. Select one of the **options** and add values into the corresponding field:

- **Process jobs within x hours**. The timeframe in which documents need to be handled, e.g. documents which need to be handled within eight hours.
- **Process Jobs before x by y**. Use this to process the number of documents received by _X_ time in the queue before _Y_ time.

Example: 230 documents came in overnight. The documents must be processed by the end of the business day, i.e. before 5 p.m. on the same day. 13. Check the checkbox **Distribute only among opening hours** to distribute the calculation result to the time period of the contact center's opening hours. Uncheck it to write the values to 24 hours instead. 14. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %} 15. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %} 16. Click _Ok_{:.doc-button} to start the calculation.

A window will pop up. It will show your input parameters and the script execution results. Check the {% link_new saved employee requirement in the Shift Center | features/scheduling/edit-or-delete-staff-requirements.md %}.

{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}

{{ 1 | image: 'Backoffice Linear Script UI', '80%' }}
