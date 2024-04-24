---
title: Map external statuses to activities
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description:
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
---

New to real-time adherence? Learn {% link_new the basics | features/intraday/real-time-adherence.md %} first.

The real-time adherence feature uses data from your external system (usually an ACD) about what your people do when they are at work. injixo imports this data directly from your ACD after you have set up an integration.

In order to monitor your people's adherence to their schedule, you need to map the statuses your ACD uses (here called external statuses) to your activities in injixo.

Go to _Intraday > Configuration_{:.breadcrumbs} to map external statuses to injixo activities.

## Mapping strategies

How you map external statuses to activities will depend on your monitoring needs.

Imagine your ACD uses these three statuses: waiting for call, on a call, and after-call work. In injixo, you schedule the activity Calls. There are two strategies that you can follow, depending on the level of detail that you need:

Option A: You want to monitor how well your people adhere to their scheduled activities. In this case, you can map all three external statuses to the activity Calls. This way, whenever your people have any of those three statuses in the ACD, injixo will show that they are doing calls, and compare that activity to their schedule.

Option B: You want a higher level of detail in your adherence monitoring. You want to know how much time your people spend waiting for a call, actually being on a call, and doing after-call work. In this case, you would create three additional activities corresponding to the three external statuses, and {% link_new match | features/intraday/adherence-matches.md %} the three new activities to the activity Calls. You can then map each external status to its corresponding activity.

## Map external statuses to activities


1. In _Intraday > Configuration_{:.breadcrumbs}, select an activity from the list.<br>Under **Integrations**, you will see a list of your integrations.
2. Click the integration with the system whose external statuses you want to map.<br>In the **External statuses** section, you can find all statuses from the external system.<br>If a status is already mapped to an activity, the activity's name is displayed next to it.
3. Select all external statuses you want to map to that activity.
4. Click _Save changes_{:.doc-button}.

You can use the search field to search external statuses by name, or you can enter "unmapped" to see all statuses from the selected integration that are not yet mapped to any activity.

## Remap already mapped external statuses

You can map an already mapped external status to another activity.

1. In _Intraday > Configuration_{:.breadcrumbs}, select an activity, and then an integration.
2. In the **External statuses** section, select the external statuses that you want to remap.<br>You will see a yellow warning icon next to the name of the activity to which the external status is currently mapped.
3. Click _Save changes_{:.doc-button}.<br>The previous mapping is overwritten.