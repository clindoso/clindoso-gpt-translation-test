---
title: Work with workloads
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to work with and navigate the graphs in workloads that show the volume and average handle time.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/events-and-holidays.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manual-adjustments.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/store-forecast-versions.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/download-forecast.md
---

In this article, you will learn how to work with and navigate in the volume and average handling time graphs in workloads.

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first. If you don't have any workloads yet, learn how to {% link_new create your first workload | features/forecast/injixo-forecast/manage-workloads.md %}.

## Display workload details

1. Go to _Forecast_{:.menu-item}.
2. Select a workload, using one of the following options:
   - Select the workload from the drop-down menu on top.
   - Type the workload name in the search field.
   - Click the workload in the list.

{{ 3 | image: 'Select a workload' }}

### Navigate in workloads

- Use the **time navigation** to select a daily, weekly, monthly, or yearly view.
- Click the **date range** to select a time period from the calendar.
- Use _<_{:.doc-button} and _>_{:.doc-button} to navigate the selected date range.
- To get back to the current time period, click the first button on the left, e.g. **This week** (labelled according to the selected view).

  {{ 1 | image: 'Workload time navigation', '80%' }}

### Volume and average handling time graphs

The diagram displays volume and the average handling time (AHT) graphs for historical data, imported forecasts, and generated forecasts as. On top, you see the total volume and AHT (total weighted average) for the selected period.

The captions help you to identify the different graphs and {% link_new manual adjustments | features/forecast/injixo-forecast/manual-adjustments.md %}; hide graphs by clicking the **eye icon**.

Note: The AHT graph is unavailable for workloads with queues that do not provide AHT data.

{{ 4 | image: 'Volume and AHT graphs', '80%' }}

### Staff requirements graph

In the _Staff Requirements_ section, configure/edit the staff calculation method.

The section displays the calculation results for automatic calculation methods. On top, you see the configured parameters and resulting total people-hours for the selected period.

{{ 5 | image: 'Staff requirements graph', '80%' }}

To use staff requirements for scheduling, select the forecast or forecast version from the first drop-down menu above (_Auto-Forecast_ is preselected), and click _Use Requirements_{:.doc-button}.

To transfer the values for other calculation methods, click _Use Forecast_{:.doc-button} on the top right next to the graphs above. The workload is now available in WFM as a queue. The queue name starts with an asterisk (**\***). Next, select your {% link_new staff requirements script | features/forecast/injixo-forecast/staff-requirement.md %}, select the queue and the _Autoforecast_ version, configure the parameters, and click _OK_{:.doc-button} to run the script.
