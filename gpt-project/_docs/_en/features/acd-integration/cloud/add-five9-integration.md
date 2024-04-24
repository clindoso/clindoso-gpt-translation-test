---
title: Add a Five9 integration
description: Connect your Five9 ACD to injixo and prepare a custom report to use queue grouping by skills.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from: /five9-grouping-by-skills/
redirect_reason: renamed file in Feb 2021
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

A Five9 integration is a cloud integration that imports calls, agent status data, and real-time adherence data.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Prerequisites

If you are grouping your queues by campaign, the integration reads the standard call log report from Five9.

If you are grouping your queues by skill, the integration needs a custom call log report from Five9 that includes skills. To import data from queues grouped by skills, follow the steps below in Five9:

 1. Create a new shared report folder named "Shared Reports (injixo)".
 2. Customize the standard call log report by including the "SKILL" column.
 3. Save the customized report as "Call Log with Skills" in the new shared folder.

For more detailed information on how to customize reports, refer to the Five9 Help Center.

## Add your Five9 integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Five9** tile, click _Add integration_{:.doc-button}.
4. Enter a unique name for the new integration that identifies the data source.
5. Enter the username and password for a Five9 user with the roles ADMIN and REPORTING.
6. In the **Configuration** section, select your account region and grouping option.
7. Click _Save integration_{:.doc-button}.

The integration now imports data into injixo. The initial import can take up to 15 minutes. All queues from the connected system will automatically be available for mapping on the {% link_new workload configuration screen | features/forecast/injixo-forecast/create-workloads.md | #create-workloads %} in injixo Forecast.

## What happens in the event of parallel agent states?

Sometimes, Five9 reports multiple states for an agent for the same period, for example:

| State   | Start time | End time |
| ------- | ---------- | -------- |
| Ready   | 13:00:00   | 13:00:05 |
| Inbound | 13:00:00   | 13:03:00 |

To avoid one state overwriting the other, the integration changes the beginning of the longer state. The beginning of the longer state becomes the end of the shorter one:

| State   | Start time | End time |
| ------- | ---------- | -------- |
| Ready   | 13:00:00   | 13:00:05 |
| Inbound | 13:00:05   | 13:03:00 |
