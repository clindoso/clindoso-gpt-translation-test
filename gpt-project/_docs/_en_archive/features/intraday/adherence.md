---
title: Use the Adherence Module
toc: false
description: Use the adherence module to see whether employees are following their schedule or not in real time.
archived_date: 2021-04-22
archive_ref: 20210422-en-adherence
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

With _Adherence_{:.menu-item}, you can compare the schedules of your Employees with their actual state in real-time, enabling you to actively manage schedule adherence and achieve the full potential of your forecasting and scheduling efforts.

_Adherence_{:.menu-item} can be found right under the _Intraday_{:.menu-item} main menu group. Users with _Admin access_, the role _Supervisor_, or the role _Supervisor Basic_ have access.

## Adherence Overview

The adherence overview is a table showing the scheduled activities and the actual activities for all selected employees. Click on a column heading to sort by any column.
To display employee data, you need to select a planning unit and/or a selection.

Available columns:

| Name | Names of the displayed employees. |
| Scheduled Activity | The activities which the displayed employees are scheduled to perform at the current time (if any). |
| Adherence Status | Every displayed agent has a status. These statuses are in adherence, in buffer time, or out of adherence. If an agent is currently out of adherence, their status will be shown as _Wrong activity_, _Not present_, or _Not scheduled_. Each status is color coded. |
| Actual Activity | The activity that the agent is currently performing (based on the _External System_ or _Time Recording_ level. |
| Out Of Adherence Duration | This displays how long the employee has been out of adherence. |
| Actual Activity Duration | The amount of time since the actual activity began. |

## Adherence Status

Each agent has a status based on the comparison between the scheduled activity and the actual activity. By default, when the activity types of both the scheduled and the actual activity are the same, the agent's status is _in adherence_ and no specific highlighting is applied to the view.\*

If there is a mismatch between the scheduled and the actual activity type, the agent is either _in buffer time_ (if configured) or _out of adherence_. There are three different reasons, why agents can be out of adherence:

- **Not Present**: The agent is scheduled to work on a specific activity, but there is no information from the ACD or external system, that the agent is actually doing anything.
- **Wrong Activity**: According to the ACD, the agent is working on an activity that does not match the scheduled one.\*
- **Not Scheduled**: The agent is not scheduled at all, but there is activity data in the ACD or external system. Agents with this status have no negative effect on the adherence score.

Use Matches to define which combinations of activities are considered in adherence.

## Agents in Buffer Time

In reality, agents are rarely able to adhere to their schedule to the second. This might lead to a very noisy display, especially if you're looking at a large number of agents. Agents constantly switching states makes it hard to concentrate on the agents that require attention.

For this reason, you have the ability to define a specific duration before an _out of adherence_ status takes full effect. You can define this buffer time by clicking the settings icon. The buffer time can be defined independently for each of the three _out of adherence_ states. Please note that this setting applies to all users of Adherence in your company and only users with the Admin role are able to change this setting.

If an agent is in buffer time

- the agent's row is not highlighted and only the status icon changes.
- the agents has no negative effect on the adherence score.
- the agent will not be shown if the _only show out of adherence_ filter is enabled.

However, the agent's out of adherence duration starts from the moment they enter the buffer time.

## Adherence Score

{{ 1 | image: 'Adherence score','50%' }}

The Adherence score provides a quick overview of the adherence state of the selected planning unit and/or selection at the current moment.

The _Adherence %_ shows the percentage of agents who are in adherence or in buffer time.

The colored legend above provides details about the distribution of agents who are out of adherence.

Below, you see a detailed breakdown of agents currently scheduled and actually present, agents scheduled for, and actually on a break as well as a delta for both of these.

## Activity Overview

{{ 2 | image: 'Activity overview','50%' }}

The activity overview gives you a straightforward outline of performance for each scheduled activity in the selected planning unit and/or a selection. The table may be sorted by any column by clicking on the column heading.

The table contains the following columns:

| Activity | Name of scheduled activity. |
| Scheduled | Number of agents with this activity scheduled. |
| Actual | Number of agents working on this activity, based on the data from the ACD. |

## Omnisearch

Above the list of agents, you will find an Omnisearch bar. You can type in (partial) agent names, activities, and exception states. Different search terms can be separated with a comma and the search will show results for any of these terms.

Alternatively, you can click the required elements on the left side of the screen, namely the three exception states and any activity in the Activity Overview list. Once you click one of these, they will be added to the search. If you click them again, they will be removed.

> Notes
>
> - _Adherence_{:.menu-item} depends on agent status data being provided from your ACD via its integration with injixo. You will also need to assign _Employee ID_ in _External System_ to each employee in _Administration_{:.menu-item} to map status changes from the ACD to the correct employees.
> - The injixo reporting suite includes two helpful reports about historical adherence. Check out the Adherence & Conformance Reports.
