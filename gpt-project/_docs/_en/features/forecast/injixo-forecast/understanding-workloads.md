---
title: Workloads setup example
toc: false
redirect_from:
  - /understanding-workloads/
redirect_reason: used in intercom forecast product tour
description: Set up workloads for different types of input channels.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

This article provides an example workload setup for your sales and support queues.

With injixo, you schedule employees to perform activities, e.g. _Sales_ or _Support_. For each activity that you wish to schedule optimally, you must calculate staff requirements. When you use injixo Forecast, you specify contacts that drive the staff requirements, called {% link_new workloads | features/forecast/injixo-forecast/manage-workloads.md %}. A single workload is used to create staff requirements for one scheduled activity. Each workload may read historical data from one or more queues.

Let's look at an example. Imagine that in your phone system, you have five queues configured:

- Product Sales East, Central, and West
- Support Tier 1 and Tier 2

## Handle Tier 1 and Tier 2 support queues separately

It's important to your contact center to split up your Tier 1 and Tier 2 support queues; it's a lot easier for you to train agents for Tier 1 support, and you have a lot more volume there, so you don't want your Tier 2 agents to get stuck answering easy questions at the expense of harder ones.

It's clear that the call volume for Tier 1 support and Tier 2 support represent two different types of work that need to be done. That doesn't mean that some agents can't do more than one (a Tier 2 agent can handle a Tier 1 call, and might do so at a lower priority), but it means that not all agents can do both (you don't want your Tier 1 agents handling Tier 2 questions that they're not trained for). Work that comes in the Tier 1 support queue is not the same as work that comes in the Tier 2 support queue.

Since the work is different for Tier 1 and Tier 2 support, you'll want to forecast these queues separately, so that you know how many Tier 1 and Tier 2 agents you need.

## Forecast East, Central, and Western sales calls together

It's also important to your business to split your sales queues into East, Central, and West: you want to be able to report on calls from these regions separately, so that you can track marketing campaigns independently in these regions. However, for the _contact center_, this isn't an important distinction. Any agent who can handle a sales call for the Eastern region can handle a call in Central or West just as easily.

The situation for your sales queues is different from your support queues. Once your sales calls have come into their regional queues, it doesn't matter to your agents where they came from. Work that comes in the Eastern sales queue is the same as work that comes in the Central or Western regional queues. And since it would be inefficient to have only some sales agents handle queues from the Eastern region, you set up your phone system so that all of your sales agents take calls from all three regions.

You can forecast East, Central, and Western sales calls together, since the work is the same, and so injixo Forecast allows you to group these three queues into a single workload and drive the staff requirements for the _Sales_ activity.

## Conclusion

Workloads are designed to reflect that calls coming into different queues may still represent the same type of work. In the scenario above, you have five queues, but only three Workloads: Tier 1 Support, Tier 2 Support, and Sales (representing calls from the Eastern, Central, and Western regions).

Later on, when you set up your activities, all of your Presence activities will be associated with the Workload that forecasts their staff requirements.

> Taking Calls from Multiple Workloads
>
> In our scenario, we have noted that Tier 1 Support agents can't handle Tier 2 calls, but Tier 2 Support agents can handle Tier 1 calls. Although you want to reserve your Tier 2 agents for their more difficult Tier 2 calls, it might make sense to route Tier 1 calls to them, perhaps at a lower priority or after a delay. Since the work is different, you'll want to keep Tier 1 and Tier 2 calls in their own workloads, but you want to be able to account for Tier 2 agents handling Tier 1 calls. You can do this using {% link_new multiactivities | features/administration/activity-types-and-properties.md | #subactivities %}.
