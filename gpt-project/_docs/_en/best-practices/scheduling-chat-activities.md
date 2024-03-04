---
title: Schedule chat activities
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to schedule chats.
redirect_from:
  - /best-practice-chat-activities/
promote-service: what-if-scenario
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
---

To schedule chat activities, take the following steps:

- Import chat data using an integration.
- Add the resulting queues to a workload in Forecast.
- Calculate staff requirements for scheduling.

## Prerequisites

To import data for chats and calculate staff requirements in chat-related workloads, your {% link_new integration | features/acd-integration/cloud/how-integrations-work.md %} must support the Chats contact data type.

## Forecast chat workloads

To forecast the chat volume, proceed as follows:

1. {% link_new Create a new workload | features/forecast/injixo-forecast/manage-workloads.md | #create-workloads %}.
2. In the **Assign queues** section of the **New Workload** configuration page, select one or more chat queues. The first drop-down menu allows you to filter by queue type.

Tip: To consider periods with unusually high or low chat volumes, you can {% link_new add events and public holidays | features/forecast/injixo-forecast/events-and-holidays.md %} to your workload.

### Workaround for no chat history or unreliable data

Even with no or unreliable data to create forecasts, you can create chat staff requirements to schedule a fixed number of employees to handle chats. You can skip forecasting and the staff requirements calculation and run the _Other - Constant Requirement_ script. Learn more about {% link_new constant requirement | features/forecast/requirement-scripts/requirement-constant.md %}.

## Block vs. blended scheduling

injixo offers two different ways to schedule chats:

- Block scheduling: Employees are scheduled for one or more blocks of a fixed activity during their shift.
- Blended scheduling: Employees are scheduled to handle any contacts for which they are skilled. You can blend both chat services or chats with other channels, such as emails or calls.

The method determines how you need to set up your chat activities and calculate staff requirements.

### Set up block scheduling

Add fixed blocks of chat (and other) activities to day models:

1. {% link_new Create an activity | features/administration/activities.md | #create-an-activity %} of type Presence for your new chat activity.
2. {% link_new Add the activity to a planning unit | features/administration/create-and-manage-planning-units.md | #add-activities %} in which you’d like to schedule chats.
3. (Optional) If only some people in the planning unit can work on the chat activity, proceed as follows:
   1. {% link_new Create a skill | features/administration/work-with-skills.md %}.
   2. {% link_new Add the skill to the chat activity | features/administration/work-with-skills.md | #assign-skills-to-activities %}.
   3. [Add the skill to the people](/employee-overview#configure-employee-settings) who will work on chat activities.
4. Create or update {% link_new day models | features/administration/daymodels/daymodel-basics.md %} by adding the chat activity to them.

### Set up blended scheduling

injixo can schedule chat activities of type Plannable by replacing other activities of type Replaceable in day models.

Alternatively, you can use multiactivities:

1. Create an activity of type Presence for your new multiactivity.
2. Create other activities you want to blend and {% link_new add them as subactivities | features/administration/activity-types-and-properties.md | #subactivities %} to the first activity.
3. Create skills and add them to the (sub)activities and your employees.

## Calculate staff requirements

There are two different ways to calculate staff requirements for chat activities.

### Calculate for block scheduling

To configure the calculation method and calculate staff requirements, proceed as follows:

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select a period for which a forecast exists.
3.  Scroll down to the **Staff Requirements** section and click _Edit staff requirements_{:.doc-button}.
4.  In the **Staff requirements** configuration window, select **Chat** from the **Calculation method** drop-down menu and complete the form.
    Learn more about the calculation method for chat and required parameters in the article {% link_new Calculate staff requirements | features/forecast/injixo-forecast/calculate-staff-requirements.md | #configure-the-calculation-methods %}.
5.  Click _Save_{:.doc-button}.

The workload details page page now displays calculated staff requirements for chat activities.

To use them for scheduling, proceed as follows:
1. Select a time period in the future.
2. In the **Staff requirements** section, click _Save staff requirements_{:.doc-button}.
3. In the **Save staff requirements** window, click _Save_{:.doc-button}.

### Calculate for blended scheduling

To transfer staff requirements from a forecast, proceed as follows:

1. Go to **Forecast**. Select the workloads for each subactivity of the multiactivity.
2. In each workload, select the same calculation period in the future.
3. From the three-dots menu _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} at the top right, select **Use forecast**.
4. In the window that opens, select your forecast version.
5. Click _Use forecast_{:.doc-button}.

To calculate staff requirements, proceed as follows:

1. Go to _Forecast > Requirement Scripts_{:.breadcrumbs}.
2. In the **Calls - Multi-Activity** tile, click _Open_{:.doc-button}.  
   A configuration window with the script parameters opens.
3. In the script configuration window, complete the form. In the **Planning Unit Parameters** section, select the multiactivity that includes your chat activities.
4. In the **Assigned activities** section, configure the following parameters for each chat activity:

   - Under **Queue Parameters**:

     | **Parameter**         | **Description**                                                                                                                       |
     | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
     | Calculation method    | Chat                                                                                                                                  |
     | Queue                 | Select the queue with the same name as your workload, prefixed with \*. This queue now contains the data you have transferred before. |
     | Version               | Auto-Forecast                                                                                                                         |
     | Processes             | Chats Offered                                                                                                                         |
     | Average Handling Time | Chats Average Handle Time                                                                                                             |

   - Under **Erlang C Parameters**:

     | **Parameter** | **Description**                                                                                            |
     | ------------- | ---------------------------------------------------------------------------------------------------------- |
     | Seq (%)       | Enter the percentage of AHT that is spent on tasks which cannot be done in parallel, e.g. after-call work. |
     | Max Sessions  | Enter the maximum number of parallel chats.                                                                |

   The staff requirements are now available for scheduling.

## Schedule chat activities

After you have imported chat data and calculated staff requirements, you have completed all prerequisites to schedule your chat activities using the {% link_new available scheduling methods | features/scheduling/scheduling-methods.md %} shift bidding, optimized schedules, or shift sequences.

You can see transferred staff requirements and the scheduling result in the {% link_new Shift Center | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %}, in {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}, or in {% link_new Dashboards | features/monitoring/dashboards/dashboards-examples.md %}.
