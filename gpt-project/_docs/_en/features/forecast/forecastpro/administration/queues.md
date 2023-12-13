---
title: Create queues
product_label:
  - on-premise
description: Learn how to use queues to import data for all of your contact channels.
---

In this article, you will learn:

- what queues are used for.
- how to configure them.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

Queues represent all channels that customers can contact you on.

Xlink imports call statistics directly into a combination of queue, value type and version. Xlink requires a mapping between ACD and injixo. For the Xlink mapping, we recommend to map ACD queues 1:1 to injixo queues. In that way, you can easily combine queues in injixo Forecast.

## Creating Queues

The manual creation of queues is needed if you use Xlink to import data.

Go to _WFM > Administration > Forecasting > Queues_{:.breadcrumbs} and follow these steps to create a queue:

1. Click the {% icon item-add %} in the action bar.
2. Enter a **Name** and an **Abbreviation**, for example, **Inbound** and **IB**.
3. Set it to **Active**.
4. Choose the **Interval** length of your queue. This should be the same as in your ACD.
5. Select the **Time Zone** of your queue.
6. Confirm with _OK_{:.doc-button}.
7. Enter the **Event Types**.
8. Choose the **Value Types** that should be available for your queue.

### Configure General Fields

In the section _General_, you have different fields to configure your queue:

| Field             | Description                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| Type              | Type of the queue. Select **Standard Queue**.                                                          |
| Name/Abbreviation | These fields are used to identify your queue.                                                          |
| Active            | You can set your queue to active. Otherwise, no data will be imported.                                 |
| Interval          | The interval depends on the interval of your ACD or external system.                                   |
| Description       | You can add a description to your queue so that so you can easily identify what the queue is used for. |
| Parent Queue      | To visualize a hierarchy in your queues, you can set a parent queue.                                   |
| Time Zone         | Define the time zone in which your data is set.                                                        |

### Define Event Types

Event types are the opening hours of your queue. We recommend adding every weekday and defining **Start Time** and **End Time** as 00:00 to cover the whole day. Opening hours are relevant for your forecast in _ForecastPro_{:.menu-item}, they do not affect _injixo Forecast_{:.menu-item}.

### Add Value Types

The value types represent the numbers which are imported from your external system, such as contact volumes for different channels. Use them to create forecasts or only to display them in other features. For forecasting purposes, only offered and answered volumes as well as AHT values are required. Before you can assign values types in injixo Enterprise on-premise you need to create them in _Adminstration > Forecasting > Value Types_{:.breadcrumbs}. Value types are pre-defined in injixo Cloud versions. Assign the right value types depending on the channel of your workload e.g. for calls _Calls Offered_, _Calls Answered_, _Calls Average Handling Time_.
