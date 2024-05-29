---
title: Choose the right method to calculate your staff requirements
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn which staff calculation method suits your needs best.
toc: true
---

injixo offers calculation methods and requirements scripts to calculate staff requirements.

## Calculation methods

- Erlang-C: Calculation method for inbound contacts based on the target volume and service level.
- Chat: Calculation method based on Erlang-C with an additional parameter to set a number of consecutive chat sessions.
- Linear: Calculation method for contacts that do not need to be handled in real time (e.g. letters, emails, tickets, or orders). The calculation result is based on the forecasted volume and, optionally, on AHT.

Learn how to {% link_new configure the calculation methods | features/forecast/injixo-forecast/calculate-staff-requirements.md %}.

## Requirement scripts

- {% link_new Constant requirement | features/forecast/requirement-scripts/requirement-constant.md %}: For activities for which you have no forecast, but for which you know the number of people needed for each time range. You can enter your own staff requirements values. You can define values for multiple timespans and activities.
- {% link_new Multiactivity | features/forecast/requirement-scripts/multiactivity-script.md %}: To schedule multiskilled people and combine different channels (e.g. several hotlines, or a combination of chats and calls).
- {% link_new Outbound | features/forecast/requirement-scripts/outbound-calls-script.md %}: For campaigns with outbound calls. You can set parameters that define the campaign duration, redial rate, right party contact rate, etc.
- Backoffice linear: For indirect communication, like letters or emails, that need to be handled within a predefined time frame. To access this script, talk to your consultant.
- Average speed of answer (ASA): Script based on Erlang-C that focuses on the average waiting time. To access this script, talk to your consultant.
- Abandoned call rate: Script based on Erlang-C that lets you define your service goal as the maximum abandoned call rate. You can also use it if your goal is based on PCA (Percentage of Calls Answered). To access this script, talk to your consultant.

## Data types and relevant staff requirements calculation methods

The following table displays which calculation methods and requirement scripts are suitable for which data type when calculating staff requirements:

| Data type or parameter                                 | Erlang-C (method) | Chat (method) | Linear (method) | Constant requirement (script) | Multiactivity (script) | Outbound (script) |
| ------------------------------------------------------ | ----------------- | ------------- | --------------- | ----------------------------- | ---------------------- | ----------------- |
| Data that can be stored (e.g. emails, tickets, orders) | No                | No            | No              | No                            | Yes                    | Yes               |
| Calls                                                  | Yes               | No            | No              | No                            | Yes                    | No                |
| Chat                                                   | No                | Yes           | No              | Yes                           | Yes                    | No                |
| Inbound contacts                                       | Yes               | Yes           | Yes             | Yes                           | Yes                    | No                |
| Outbound contacts                                      | No                | No            | No              | No                            | No                     | Yes               |
| One line only                                          | Yes               | Yes           | Yes             | Yes                           | No                     | Yes               |
| Several lines                                          | No                | No            | No              | No                            | Yes                    | No                |
| Historical data                                        | Yes               | Yes           | Yes             | No                            | Yes                    | Yes               |
| Type of service goal                                   | Yes               | Yes           | No              | No                            | Yes                    | Yes               |
| Service level (e.g. 80/20)                             | Yes               | Yes           | No              | No                            | Yes                    | Yes               |
