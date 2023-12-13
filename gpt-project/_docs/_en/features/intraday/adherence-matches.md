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
- You can match one external activity to all injixo activities of a type, e.g. _Break_.

Due to Matches, the Real-Time and Intraday Adherence features treat external activities as _in adherence_ with the matched activities or types.

Note: injixo standard reports do not work based the matched activities but only consider the default activity mapping.

## Access the Activity Matches page

1. Go to _Intraday > Real-Time Adherence_{:.breadcrumbs}.
2. To access the **Activity Matches** page, choose any of these options:

   - Click the three dots menu _![three dots menu](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon} and select **Activity Matches**.
   - In the **agent table**, click an **activity** in the _Actual activity_ column.
   - In the **Activity Overview** section on the left, hover over an activity and click the **Matches icon**.<!-- todo: include icon -->

## Configure activities

1. [Access the Matches configuration](#access-the-activity-matches-page).
2. On the **Activity Matches** page, click an **activity**.

   A Cloud icon identifies activities with a default activity mapping.  
   The [special _Offline_ activity ](#the-offline-activity) also has the cloud icon.

   {{ 3 | image: 'List of Activities','40%' }}

The **Activity Matches** page displays the selected activity:

- Actual Activity: Default activity mapping, grouped by external system. If you see _No mappings defined_, there is no default activity mapping yet.
- Scheduled Activity: All matched activities and types that are considered as _in adherence_.

{{ 1 | image: 'Matches overview','90%' }}

### Manage external system mappings

To change the default activity mapping, click **Manage** and change the mapping in the **External Systems** section.

### Default matches

- Activities are matched to their type (editable).
- Activities of type _Holiday_, _Illness_, or _Absence_ are automatically matched to the three types (editable).
- Activities are matched to themselves (not editable).

### Manage activity matches

1. Under **Scheduled Activity**, click **Manage activity matches**.
2. In the **Manage activity Matches** window, check one or more checkboxes (or use the search to filter).
3. Click _Apply_{:.doc-button}.
   {{ 2 | image: 'Manage additional Matches',' 40%' }}

## The _Offline_ activity

The _Offline_ activity appears in the list of activities but cannot have a default activity mapping. You can use this special activity to improve your Adherence score. When agents need to log out from your external system for breaks, meetings, or trainings, such agents often appear as _out of adherence_ with the type _not present_.

To avoid such undesired _out of adherence_ states, you can configure the _Offline_ activity:

1. [Access the Matches configuration](#access-the-activity-matches-page).
2. On the **Activity Matches** page, click the **Offline** activity.
   {{ 3 | image: 'List of Activities','40%' }}
3. On the **Activity Matches** page, click _Manage activity matches_{:.doc-button} on the right.
4. In the **Manage activity Matches** window, select one or more activities that match _Offline_.
5. Click _Apply_{:.doc-button}.
