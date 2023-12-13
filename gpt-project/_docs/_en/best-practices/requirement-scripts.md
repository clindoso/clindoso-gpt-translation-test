---
title: Choose the correct requirements script
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn which staff calculation method suits your needs best.
toc: false
---

injixo offers a variety of methods to calculate staff requirements.
While your Contact Center's service level agreement (SLA) may have a service goal of handling 80% of all calls within 20 seconds, Erlang-C may not be the optimal script to determine staff requirements.
There are a number of factors to consider when deciding on which script best suits your Contact Center's particular requirements. <br>
This best practices article provides an interactive decision tree exercise and reference table to help you determine which script is best suited for your organization.

## Decision guidance

The following diagram will help you to decide which requirement script is the right one for you:

{{ 1 | image: 'Workflow', '60%' }}

## Requirements scripts overview

For a full picture of all available staff calculation methods, here is an overview:

- {% link_new Constant requirement script | features/forecast/requirement-scripts/requirement-constant.md %}: For any type of activity where you don't have a forecast, but you know exactly how many people you need at which time. You can enter your own staff requirements numbers. You can even set multiple Timespans and Activities to plan for.
- {% link_new Linear requirement script | features/forecast/requirement-scripts/requirement-linear.md %}: For non-direct communication such as letters, emails or orders, based on the assumption that this volume is processed sequentially. The calculation result is based on the forecasted volume and optionally AHT.
- {% link_new Backoffice Linear requirement script | features/forecast/requirement-scripts/requirement-backoffice-linear.md %}: For non-direct communication (letters, emails, etc.) that you would like to handle in a pre-defined time frame. Choose between processing messages within x hours or processing all messages that came in by e.g. 8 am by the end of business day.
- {% link_new Chat requirement script | features/forecast/requirement-scripts/requirement-chat.md %}: Erlang-C based calculation method with an additional parameter to specify a number of consecutive chat sessions.
- {% link_new Erlang-C (Single Activity) requirement script | features/forecast/requirement-scripts/requirement-erlangc.md %}: Standard staff staff calculation method for inbound based on the volume and the service level you would like to achieve.
- {% link_new Multiactivity requirement script | features/forecast/requirement-scripts/requirement-multiactivity.md %}: For scheduling multiskill agents and the combination of different channels (e.g several hotlines but also combinations of chats and calls).
- {% link_new Average Speed of Answer Requirement (ASA) script | features/forecast/requirement-scripts/requirement-asa.md %}: Variation of Erlang-C that focuses on the average wait time before your agents answer incoming calls.
- {% link_new Abandoned Call Rate requirement script | features/forecast/requirement-scripts/requirement-abandoned-calls.md %}: Define your service goal as the maximum abandoned call rate, based on Erlang-C. Also useable if your goal is based on PCA (Percentage of Calls Answered), simply reverse the PCA target. For example, if your PCA is 80%, add an abandonment rate target of 20%.
- {% link_new Outbound requirement script | features/forecast/requirement-scripts/requirement-outbound.md %}: For campaigns with outbound calls. The script includes parameters to specify campaign duration, redial rate, right party contact rate, etc.

Still not sure which Script to use? Take a look at the table and Flowchart below to help you decide!

{{ 2 | image: 'Overview for requirement scripts' }}
