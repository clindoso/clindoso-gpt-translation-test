---
title: Add a Cisco ICM integration
description: Learn how to connect your Cisco ICM to injixo to import data.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

The Cisco ICM integration imports real-time adherence data. The integration uses {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add a Cisco ICM integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Cisco ICM** tile, click _Add integration_{:.doc-button}.

## Set up your Cisco ICM integration

1. Enter a unique **Name** for the new integration that identifies the data source.
2. In the **injixo Cloud Link** section, click the **Download link** for your operating system.<br>
   > Note
   >
   > If you have already downloaded Cloud Link for another integration, you still need to download the Cisco-specific version from this page.
3. Install and connect {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.<br>
4. In the **Configuration** section, set up your integration:

   - Enter a **Connection string** with the required parameters to connect to your Cisco database:  
     `DRIVER={MS SQL Server};Server=myServerAddress;Database=myDataBase;UserId=myUsername;Password=myPassword;`
   - Select your **Database time zone** from the drop-down menu.
   - Enter your Cisco ICM **Client ID** and **Password**.
   - Enter your **Peripheral gateway 1**.
   - (Optional) Enter your **Peripheral gateway 2**.

5. Click _Save integration_{:.doc-button}.

injixo will start importing RTA data, but the data will only be visible after you have mapped external user identifiers to your people.

## Map external users to your people

1. Go to _WFM > Administration > Scheduling > Employees_{:.breadcrumbs}.
2. Assign external user identifiers to your people.
   > Note
   >
   > The external user identifiers are the Unified CCE Skill Target IDs.

Learn more about {% link_new mapping external user identifiers | features/acd-integration/cloud/import-agent-status-data.md | #map-external-identifiers-to-people-in-injixo %} to people.

## Map external statuses to injixo activities

1. Go to _Intraday > Configuration_{:.breadcrumbs}.
2. Map external statuses from Cisco ICM to injixo activities.

Learn more about {% link_new mapping external statuses | features/intraday/map-external-status.md | #map-external-statuses-to-activities %} to injixo activities.
