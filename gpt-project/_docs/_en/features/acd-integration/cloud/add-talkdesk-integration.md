---
title: Add a Talkdesk integration
description: Learn how to connect your Talkdesk ACD to injixo to import data.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

A Talkdesk integration is a cloud integration that imports historical call data and agent status data.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add a Talkdesk integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Talkdesk** tile, click _Add integration_{:.doc-button}.
4. Enter a unique name for the new integration that identifies the data source.
5. In the **User credentials** section, complete the form with Talkdesk-specific information:

   - Enter your Talkdesk account name.
   - Enter the client ID and the client secret of a Talkdesk OAuth client.

     > For Client ID and Client secret, [create a new OAuth client](https://docs.talkdesk.com/docs/creating-a-new-oauth-client) in Talkdesk.
     >
     > You can also use an existing OAuth client that has been configured as follows:
     >
     > - Grant type: client-credentials
     > - Scopes: data-reports:read and data-reports:write

6. In the **Configuration** section, select your account region.

7. Click _Save integration_{:.doc-button}.  
   The integration will test the connection and report any issues.  
   When the check has passed, the integration will start importing data to injixo.

<!-- ## Talkdesk Data in injixo -->

## What's next?

When call data has been imported into queues, you can create your first workload. To learn more about the steps required to set up agent status data, check out the related articles.
