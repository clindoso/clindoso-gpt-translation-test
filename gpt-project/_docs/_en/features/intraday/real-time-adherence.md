---
title: Real-Time Adherence
toc: true
product_label:
  - advanced
  - enterprise
description: Check how closely your agents are adhering to their schedules in real time.
archive_ref: 20210422-en-adherence
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
redirect_from:
  - /adherence/
redirect_reason: Updated filename on 07 December 2022
---

In _Intraday > Real-Time Adherence_{:.breadcrumbs}, you can compare the scheduled activities with a person's actual status in real-time. When your agents log their status in an external system, such as an ACD, an integration configured in injixo will import agent status data. You will see if the activities people are currently working on are in adherence to the schedule. This allows you to identify when a person deviates from the schedule and to take action if necessary.

## Prerequisites

For the Real-Time Adherence functionality to work properly, make sure you meet the following prerequisites:

- The Real-Time Adherence functionality uses information from your ACD about the activities that people are currently working on. To access this data and display it in injixo, set up the {% link_new real-time agent status import | features/acd-integration/cloud/import-agent-status-data.md %}.
- Allow the Real-Time Adherence functionality to open a {% link_new WebSocket connection | getting-started/system-requirements.md | #share-urls-for-websockets %}. This is required for real-time updates. If the WebSocket connection cannot be opened or needs to be recreated due to firewalls or an unstable network connection, you will see a message when the page tries to reconnect.

After external data has been imported, you need to add the external user identifiers to your people in injixo. Remap external activities to existing or new injixo activities for more adherence details.

You can map one or more external activities to one activity from injixo.<!-- link activity mapping when merged --> To define a more detailed mapping, use {% link_new Matches | features/intraday/adherence-matches.md %}.

## Get started

After you have selected a **Planning unit** and optionally a **Selection**, the page will display data. You can get a general overview or details about the individual status of a person in both the external system and injixo.

Tip: Limit permissions to specific planning units or selections by configuring {% link_new user roles | getting-started/configure-user-roles.md | #set-wfm-permissions %}.

### Status

Each person has a status based on the comparison between the scheduled activity and the actual activity:

| Status           | Description                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------------- |
| In adherence     | The type of the scheduled activity is the same as the type of the actual activity. The row is not highlighted.  |
| Out of adherence | The activity types of the scheduled activity and of the actual one do not match. The row is highlighted in red. |

> Note
>
> With no integration and mapped external user identifiers:
>
> - A scheduled person appears as in adherence, and their actual activity appears as Offline.
> - A person who is not scheduled but is engaged in an activity appears as Not scheduled.
> - A person who is not scheduled and is offline is not displayed.

Note the following behavior for scheduled people:

- People without an assigned external user identifier appear as Offline. No status can be imported. You will not see any data in the external system level in Schedules or Shift Center.
- People who have been scheduled for activities of type Vacation or Illness and who are logged into the external system appear as Not Scheduled.

### Out of adherence types

The following types and colors are displayed in the [agent table](#adherence-overview-agent-table):

| Type           | Color  | Description                                                                                                                                                              |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Not present    | Red    | The person is scheduled to work on a specific activity, but there is no information available from the external system. Data is not imported or not mapped correctly.    |
| Wrong activity | Yellow | According to the external system, the person is working on an activity that does not match the scheduled activity in injixo.                                             |
| Not Scheduled  | Blue   | The person is not scheduled for any activity in injixo but the external system sent a status. This Out of adherence type does not affect the Adherence Score negatively. |

### Buffer time

The buffer time defines the duration after which an Out of adherence status takes effect. Learn how to [change the default buffer time](#change-the-buffer-time).

In a real work environment, people are rarely able to adhere to their schedule to the second. This can lead to a cluttered display. The buffer time helps you to focus on the people who need your attention.

If a person is within the defined buffer time, the displayed time value for the Out-of-adherence duration is already increasing while:

- the person's row is not highlighted and only the status marker changes.
- the person's status has no negative effect on the adherence score.
- the person's row is not displayed if the _Show only out of adherence_ filter is activated.

## Monitor Real-Time-Adherence

The Real-Time-Adherence page consists of different sections.

### <a name="define-the-target-adherence-score"></a>Adherence scores in percent

On the left, you can see two sections with percentage values:

- Real-Time Adherence: the percentage of people who are currently in adherence or in buffer time.
- Intraday Adherence: the aggregate adherence score for the past intervals of the day.

Hover over the graphs in the **Intraday Adherence** section to see the values for single intervals:

- Gray: Adherence score for the past intervals of the day. Times of the day with high or low adherence.
- Blue: Trend of the Intraday Adherence score. This shows the general trend over the day so far.
- Pink: The currently configured Adherence Target Score, lower values are highlighted.

{{ 3 | image: "Intraday Adherence graphs", '45%' }}

Note: The times are displayed in the timezone of the selected planning unit. If you have only chosen a selection, and you use multiple time zones in injixo, the times appear in the timezone that has been configured in your company account. The graphs show the business hours of the selected planning unit where applicable.

### Agent overview

<!-- still agent in the UI - october 2023 -->

In the Agent overview section, you can see the number of agents for the three Out-of-adherence types and the number of agents that are in adherence, in buffer time, and out of adherence.

### Breaks and Presence

The Breaks section shows the number of scheduled and currently logged in agents and the numerical difference between them for all activities of type Break. The Presence section shows the same information for activities of type Presence.

### Activity overview

In the Activity overview section, you can see how many agents are scheduled for an activity in injixo and how many agents are currently working on this activity. You can sort the table by clicking any header. Hover over an activity to edit the matches for this activity or to filter the list of agents on the right by that activity.

### Adherence overview: Agent table

The table shows people being in adherence or out of adherence. You can sort the table by clicking any header. Check the checkbox **Show only out of adherence** next to the search bar to show only the people who are out of adherence.

The table contains the following columns:

| Column                    | Description                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Name                      | Name of the person                                                                                          |
| Actual activity           | Name of the activity that the person is currently working on (based on data from the External System level) |
| Status                    | Status as a colored marker with a tooltip for the name of the status                                        |
| Scheduled activity        | Name of the activity the person is currently scheduled (if applicable)                                      |
| Out-of-adherence duration | Time the person has been out of adherence                                                                   |
| Current activity duration | Time passed since the start of the current activity                                                         |

### Search and filter

To filter the table content, use one of the following options:

| Where             | Action                                                    | Search hint                                                                                        |
| ----------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Search bar        | Type in **(partial) search terms**                        | Search for people's names, activities, or statuses. Use a comma to separate multiple search terms. |
| Agent overview    | Click a **status**                                        | You can add multiple statuses. Click again to remove the status from the search.                   |
| Activity overview | Hover over a table row and click the **magnifying glass** | You can add multiple activities. Click again to remove the activity from the search.               |

<!-- {{ 5 | image: "Table with details per agent", '75%' }} -->

### Single-Person adherence details

To open a timeline view below the table, click a person's name. You will see the person's scheduled activities and a corresponding timeline of Out-of-adherence statuses for the day. You can also see how long the person is scheduled and the out-of-adherence duration. The dedicated Adherence Score shows the relationship between these two numbers.

{{ 6 | image: 'Details of a person','100%' }}

Click an **Out-of-adherence status** to open a detailed view of the actual activities performed by a person. You can also see the activity type and the duration. The detailed view groups many short Out-of-adherence statuses that happen in a row into one block.

{{ 7 | image: 'Out-of-adherence details','100%' }}

## Configuration

Real-Time Adherence can be configured according to your needs.

### Change the Adherence Target Score

The Adherence Target Score is displayed as a graph in the Intraday Adherence section. The score defaults to 90%.

Users with admin access can change the Adherence Target Score by following these steps:

1. Click the {% icon ellipsis_v %}.
2. Select **Adjust your Adherence Target**.
3. Enter a new value.
4. Click _Apply_{:.doc-button}.

> The configured score applies to everyone in your injixo tenant.

### Change the buffer time

Users with admin access can set a separate buffer time for each Out-of-adherence status:

1. Click the {% icon ellipsis_v %}.
2. Select **Adjust your buffer time**.
3. Select the same or different values from the **Not present**, **Wrong activity**, and **Not scheduled** drop-down menus.
4. Click _Apply_{:.doc-button}.

> The configured buffer time applies to everyone in your injixo tenant.

## Troubleshoot wrong or missing external status information in injixo

People without an assigned external user identifier appear as Offline. No status can be imported due to this missing mapping. You will not see any data in the external system level in Schedules or Shift Center. Add the correct external user identifier and wait for the next data import. Check already configured external user identifiers for typos.

If you see unexpected gaps in the data in the external system level in Shift Center or Schedules, make sure all relevant external activities are mapped to either the Present activity (ID 1) or individual activities. Learn more about {% link_new mappings | features/acd-integration/cloud/import-agent-status-data.md %}. <!-- Add new article about activity mapping, update naming -->

If this does not resolve the problem, get a report that shows the actual status in the external system, take a screenshot of the data in the external system level, and contact our support team.
