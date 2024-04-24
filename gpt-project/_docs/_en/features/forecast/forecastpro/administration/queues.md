---
title: Create queues
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to use queues to import data for all of your contact channels.
---

Data about your customer interactions is recorded by your ACD. This contact data is imported into injixo by {% link_new integrations | features/acd-integration/cloud/how-integrations-work.md %} to create forecasts. Xlink does not create queues automatically, other injixo integrations do. Queues are always associated with a channel and can be selectively added to workloads in Forecast.

When you click **Use Forecast** in a workload that contains queues from a non-Xlink integration, a queue will automatically be created in _WFM > Administration > Forecasting > Queues_{:.breadcrumbs} for specific {% link_new staff requirements calculation | features/forecast/injixo-forecast/calculate-staff-requirements.md %} methods. This queue will have the name of the workload with a leading asterisk, e.g. \*yourWorkloadName. Forecast data will be available in the version Auto-Forecast. 

## Create queues

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

Xlink does not create queues during imports. To create queues for the Xlink mapping, go to _WFM > Administration > Forecasting > Queues_{:.breadcrumbs} and proceed as follows:

1. Click the {% icon item-add %} in the action bar.
2. Enter a **Name** and an **Abbreviation**.
3. Check the **Active** checkbox. If not checked, Xlink will not import data into this queue.
4. Select an **Interval**. The interval length should be the same as in your ACD.
5. (Optional) Enter a **Description**, e.g. to identify what the queue is used for.
6. (Optional) Select a **Parent Queue**. This can be used to visualize a hierarchy in the list of queues.
7. Select a **Time Zone**.
8. Click _OK_{:.doc-button}.
   Now, you can add event types and value types to the queue.

Tip: Map single ACD queues to injixo queues to be able to combine volumes later by selecting the queues in workloads.

### Add event types

Opening hours set here do not affect injixo Forecast. Event types are only applicable for the old ForecastPro module in the injixo Enterprise on-premise WFM plan where event types set opening hours for queues.

Select an event type from the list and add a start time and end time. If you add 00:00 to both fields, the queue is open 24 hours.

### Add value types

In Xlink, you need to create and assign value types to a queue. Other integrations add pre-defined value types for offered and answered volumes and AHT if you click **Use Forecast** in a workload. Such value types are based on the channel of the queue, for example, you will see Calls Offered, Calls Answered, Calls Average Handling Time for call workloads.

You can still add additional value types manually. Add missing value types if you cannot transfer staff requirements due to an error message.


Depending on your WFM plan, you can also display queues in {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %}.
