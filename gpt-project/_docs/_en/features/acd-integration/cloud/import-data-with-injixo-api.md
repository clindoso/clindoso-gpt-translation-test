---
title: Import data with injixo API
navigation_title: injixo API
product_label:
  - advanced
  - enterprise
description: Add an injixo API integration to import contact and agent status data from your external system.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/manage-dashboards.md
---

injixo uses vendor-specific and universal integrations to import contact and agent status data from external systems.

## What is an injixo API integration?

In injixo Advanced and Enterprise WFM, injixo API integrations allow you to send API requests to import data (e.g. when there is no standard integration for your external system). For this purpose, the injixo API provides the following resources:

- [Contact Event resource](https://api.injixo.com/resources/contact-store/contact-events): Contact events are recorded when customers contact your company via call, email, or chat. injixo stores this data in queues grouped by queue name and channel.
- [Agent Status resource](https://api.injixo.com/resources/agent-status-store/agent-status): Agent status data is recorded when employees switch from one activity to the next, e.g. login, wrap-up time, or logout.

## Add an injixo API integration

Users with admin access can add an injixo API integration as follows:

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Universal Interfaces** tile, click _Select model_{:.doc-button}.
4. In the **injixo API** section, click **Add integration**.
5. Enter a unique name for the new integration.
6. Click **Save integration**.<br>The **Access injixo API** section becomes available.
7. To generate the injixo API key, click _Generate_{:.doc-button}.

Authentication also works with personal access tokens that have been created in user profiles in the {% link_new **Personal access tokens** | features/reporting/injixo-api/injixo-api.md | #authorization-personal-access-token %} section.

> You cannot access the API key again later.
>
> - Store the API key in a safe place, e.g. your password manager.
> - The current API key expires if any user generates a new API key for the integration or deletes the integration.

## Import data <a id="import-contact-or-agent-status-data">

To identify the API integration and to authenticate, include the injixo API key and the integration configuration ID in API requests:

1. Add your injixo API key to the Authorization request header.
2. Find or copy your integration configuration ID:
   - Go to _Account > Integrations_{:.breadcrumbs}.
   - In your API integration section, click the {% icon pencil %}.
   - In the **Access injixo API** section, click _{% icon clone | icon-only %} Copy_{:.doc-button}.
3. Add your integration configuration ID to the **meta** object in the request body.

To import data from your external system to injixo regularly, you need to run your own application. For sample scripts in Ruby and Python, check the user guides in the [injixo API documentation](https://api.injixo.com).

## Testing data imports

For testing, you can send single POST requests to the API. The data array in the examples below contains a single data point but you can change it if needed. Replace at least the sample API key (abc123456=) and the integrationConfigurationId value (1234) with your own.

The API only supports HTTPS. Send your requests to https://api.injixo.com to avoid `not_found` errors.

### cURL on the command line

The following examples show how to send data to the API using [cURL](https://curl.se/). cURL is a command line tool that exchanges data with a server through a terminal.

Contact events:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456=" \
 -d '{"data":[{"properties":{"offered":true,"handled":false,"duration":124.6},"queueName":"Level 1 support","queueIdentifier":"1337_99","timestamp":"2021-12-06T10:34:22Z","channel":"calls"}],"meta":{"integrationConfigurationId":1234}}' \
 https://api.injixo.com/external-systems/contact-events
```

Note: Each new combination of `queueIdentifier`, `queueName`, and `integrationConfigurationId` will create a new queue. To avoid duplicate queue names, make sure you add the same queueIdentifier or the same integrationConfigurationId for each request with the same queue name.

Agent status:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456==" \
 -d '{"data":[{"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2021-12-06T10:00:00Z","endTime":"2021-12-06T15:00:00Z"}],"meta":{"integrationConfigurationId":8431,"externalSystem":"My ACD"}}' \
 https://api.injixo.com/external-systems/agent-statuses
```

### REST clients

The following examples show how to send data to the API using a REST client, such as [Postman](https://www.postman.com/downloads/).

1. Include a JSON request header:

   ```
   {
     "Content-type": "application/json",
     "Authorization": "Bearer abc123456="
   }
   ```

2. Include a different JSON request body for contact events and agent status data.<br><br>

   Example request body for contact events: `/external-systems/contact-events`:

   ```
   {
     "data": [
       {
         "properties": { "offered": true, "handled": false, "duration": 124.6 },
         "queueName": "Level 1 support",
         "queueIdentifier": "1337_99",
         "timestamp": "2021-12-06T10:34:22Z",
         "channel": "calls"
       },
       {
         "properties": { "offered": true, "handled": true, "duration": 200.1 },
         "queueName": "Level 1 support",
         "queueIdentifier": "1337_99",
         "timestamp": "2021-12-06T10:46:22Z",
         "channel": "calls"
       }
     ],
     "meta": { "integrationConfigurationId": 1234 }
   }
   ```

   Example request body for agent status: `/external-systems/agent-statuses`:

   ```
   {
     "data": [
       {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-06T08:00:00Z","endTime":"2022-12-06T13:00:00Z"},
       {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-07T09:00:00Z","endTime":"2022-12-07T10:00:00Z"}
     ],
     "meta": {
       "integrationConfigurationId": 1234,
       "externalSystem": "My ACD"
     }
   }
   ```

## Your first API request - what next?

After you have sent a successful API request, you need to wait before you can see data in injixo. You can work with the imported data as follows:

- Contact events requests: In **Forecast**, the **New workload** and **Edit workload** pages will display the imported queues when data has been processed.
- Agent status data requests: The first request with new agent IDs will not result in actual agent status data in Shift Center. To see data, {% link_new map at least one external identifier | features/acd-integration/cloud/import-agent-status-data.md | #map-external-identifiers-to-people-in-injixo %} (sent as agentIdentifier) to a person. You need to send another request to display the data.
