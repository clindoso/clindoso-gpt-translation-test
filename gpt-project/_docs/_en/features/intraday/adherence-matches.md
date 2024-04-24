---
title: Configure Matches
product_label:
  - advanced
  - enterprise
description: Create rules to define which combination of scheduled and current activities are considered to be in adherence.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
---

New to Real-Time Adherence? Learn {% link_new the basics | features/intraday/real-time-adherence.md %} first.

## What is Matches?

By default, you can only map one external activity (agent status) to one activity in injixo. In some cases, this default activity mapping is insufficient and leads to a low adherence score in the Real-Time Adherence feature, e.g. if mapping rules are too broad.

Matches provides a special mapping option for external activities:

- You can match one external activity to multiple injixo activities.
- You can match one external activity to all injixo activities of a type, e.g. Break.

Due to Matches, the Real-Time and Intraday Adherence features treat external activities as in adherence with the matched activities or types.

Note: injixo standard reports do not work based the matched activities but only consider the default activity mapping.

## Access the Activity Matches page

1. Go to _Intraday > Real-Time Adherence_{:.breadcrumbs}.
2. To access the **Activity Matches** page, choose any of these options:

   - Click the three dots menu _![three dots menu](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon} and select **Activity Matches**.
   - In the **agent table**, click an **activity** in the Actual activity column.
   - In the **Activity Overview** section on the left, hover over an activity and click the **Matches icon**.<!-- todo: include icon -->

## Configure activities

1. [Access the Matches configuration](#access-the-activity-matches-page).
2. On the **Activity Matches** page, click an **activity**.

   A cloud icon {% icon cloud_arrow_up_gray | icon-only %} identifies activities with a default activity mapping.  
   The [special Offline activity ](#the-offline-activity) also has the cloud icon {% icon cloud_arrow_up_gray | icon-only %}.

   {{ 3 | image: 'List of Activities','40%' }}

The **Activity Matches** page displays the selected activity:

- Actual Activity: Default activity mapping, grouped by external system. If you see No mappings defined, there is no default activity mapping yet.
- Scheduled Activity: All matched activities and types that are considered as in adherence.

{{ 1 | image: 'Matches overview','90%' }}

### Manage mappings of external statuses

To change the default mappings, click **Edit in Intraday**. injixo will redirect you to _Intraday > Configuration_{:.breadcrumbs}, where you can {% link_new remap the external statuses  | features/intraday/map-external-status.md %}.

### Default matches

- Activities are matched to their type (editable).
- Activities of type Holiday, Illness, or Absence are automatically matched to the three types (editable).
- Activities are matched to themselves (not editable).

### Manage activity matches

1. Under **Scheduled Activity**, click **Manage activity matches**.
2. In the **Manage activity Matches** window, check one or more checkboxes (or use the search to filter).
3. Click _Apply_{:.doc-button}.
   {{ 2 | image: 'Manage additional Matches',' 40%' }}

## The Offline activity

The Offline activity appears in the list of activities but cannot have a default activity mapping. You can use this special activity to improve your Adherence score. When agents need to log out from your external system for breaks, meetings, or trainings, such agents often appear as out of adherence with the type not present.

To avoid such undesired out of adherence states, you can configure the Offline activity:

1. [Access the Matches configuration](#access-the-activity-matches-page).
2. On the **Activity Matches** page, click the **Offline** activity.
   {{ 3 | image: 'List of Activities','40%' }}
3. On the **Activity Matches** page, click _Manage activity matches_{:.doc-button} on the right.
4. In the **Manage activity Matches** window, select one or more activities that match Offline.
5. Click _Apply_{:.doc-button}.
