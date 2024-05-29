---
title: Calculate a forecast
description: Follow the basic steps required to create a forecast.
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
redirect_from:
  - /quickstart-forecasting/
redirect_reason: Updated filename on 29 November 2023
---

This article lists the steps necessary to create your first {% link_new forecast | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}. Based on historical data, the forecast calculates the number of employees needed to handle the incoming volumes for an activity in a planning unit.
This article provides an overview of the procedure of creating a forecast. To learn more about the details of each step, follow the links in this article.

Use this article as a checklist to support your onboarding. Contact your consultant if you have any questions.

## Prerequisite

Before you create a schedule, make sure you have correctly {% link_new set up your base configuration | getting-started/set-up-base-configuration.md %}.

## 1. Set up an integration

Under _Account > Integrations_{:.breadcrumbs}, set up an {% link_new integration | features/acd-integration/cloud/how-integrations-work.md %} with your external system to upload historical data. The integration will upload data to injixo and create queues.

## 2. Set up a workload

Under _Forecast_{:.breadcrumbs}, create {% link_new a workload from the queues created by your integration | features/forecast/injixo-forecast/create-workloads.md %}. A forecast will be generated within minutes.

Note: To {% link_new import external forecasts | features/forecast/injixo-forecast/import-forecast.md %} you must select at least one queue. If no queue is present, you must upload at least one data point using a {% link_new CSV integration | features/acd-integration/cloud/add-csv-integration.md %}.

## 3. Create and add events

Create all {% link_new events | features/forecast/injixo-forecast/events-and-holidays.md %} that might influence your forecast calculation. Add the created events to the history and forecast within your workload(s) to improve the calculation result.

## 4. Save a forecast version

A {% link_new forecast version | features/forecast/injixo-forecast/save-forecast-versions.md %} is a snapshot of the current calculation result. Save the forecast version for later review or to compare your forecast with the volume on the actual day, e.g. in {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %}.

## 5. Calculate staff requirements

To create optimized schedules or run the job optimization, you must first {% link_new calculate the staff requirements | features/forecast/injixo-forecast/calculate-staff-requirements.md %} for the corresponding activities within your workloads.

## What's next?

You've done it! You are now ready to {% link_new create your first schedule | getting-started/create-a-schedule.md %} based on your forecast and staff requirements.
