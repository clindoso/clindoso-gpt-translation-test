---
title: Schedule multiskill agents
product_label:
  - advanced
  - enterprise
  - classic
description: Schedule multiskill agents using optimized scheduling.
toc: true
---

Contact centers offer their customers multiple channels, e.g. phone numbers for orders, or email and chat for complaints, which requires multiple skills. Not all agents are skilled in all areas, and they can only handle contacts they are skilled for.

## Representation in injixo

In injixo, optimized scheduling supports multiactivities that allow you to schedule multiskill or multichannel tasks.

Each input channel represents a subactivity and each employee skill a corresponding injixo skill. During scheduling, all employee skills are included simultaneously in the staff requirements calculation. This causes a pooling effect, so that the total requirement for agents decreases because all necessary skills are covered by fewer employees.

## Recommended approach

1. Create a {% link_new Multiactivity | features/administration/activity-types-and-properties.md | #subactivities %}.

2. Create the forecast. For multiactivity, you will need a workload for each skill and each contact channel.

3. Calculate the multiactivity staff requirements by using the `Calls - Multiactivity` script. For multichannel, there are further parameters, e.g for chat the `seq. (%)` parameter and the maximum number of simultaneous sessions; see {% link_new Multiactivity Requirement | features/forecast/requirement-scripts/requirement-multiactivity.md %} and {% link_new Chat Requirement | features/forecast/requirement-scripts/requirement-chat.md %}.

4. Run the **Create optimized schedule** functionality.

### Scheduling result

In _Shift Center_{:.menu-item}, the schedule only contains the multiactivity. The subactivities are visible in the parameter window:

{{ 2 | image: "Shift Center with parameters for multiactivity" }}

> Hint
>
> You cannot add up the staffing values for each subactivity to calculate the value for the multiactivity
>
> The multiactivity staffing always equals the number of people that has been scheduled. The Shift center does not display absolute numbers for subactivities, but the number of people skilled to perform this task. When people are skilled for multiple subactivities, the subactivity staffing values can be as high as the multiactivity staffing at maximum.

To see a person's assigned activities for a day, double-click a day cell and select the **Multi-Activities** tab.

{{ 1 | image: "subactivities in shift center dialog", '60%' }}

For intraday management, {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %} can display the coverage and staffing for multiactivities and their subactivities. Pull the staffing for the single subactivities and the multiactivity itself into the chart.

{{ 3 | image: "Multiactivity staffing dashboard" }}
