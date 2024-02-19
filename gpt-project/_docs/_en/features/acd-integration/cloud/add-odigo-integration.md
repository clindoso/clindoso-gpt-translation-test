---
title: Add an Odigo integration
description: Learn how to connect your Odigo ACD to injixo to import data.
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

The Odigo integration imports real-time agent status and real-time adherence data.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add an Odigo integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Odigo** tile, click _Add integration_{:.doc-button}.
4. Enter a unique name for the new integration that identifies the data source.
5. In the **Credentials** and **Contact data** sections, fill out all mandatory fields.
6. (Optional) Configure the import of detailed break agent statuses:
- Check the checkbox **Import detailed break agent statuses**.<br>When importing break statuses, injixo includes information about the type of break taken.<br>Note: If you check this checkbox, you also need to update the {% link_new activity mapping | features/intraday/map-external-status.md | #remap-already-mapped-external-statuses %}.
- Enter your Odigo URL including the tenant ID.
- Enter the username and password for the web service.
7. Click _Save integration_{:.doc-button}.

## Configure your Odigo integration

1. In the **Generate injixo URL token** section, click _Generate_{:.doc-button}.
2. Copy the injixo URL token to your clipboard.<br>
The injixo URL token is only shown once. If you cannot finish your setup right away, store it in a safe place, e.g. into a password manager.
3. In the Administration section of your Odigo interface, activate sending notifications to an external server. To do this, contact Odigo.
4. Paste the copied **injixo URL token** as notification URL.
5. Save your settings in Odigo and go back to injixo.

To activate the integration, you need to restart the server. To do this, contact Odigo.<br>
injixo will then start importing RTA data, but the data will only be visible after you have mapped external user identifiers to your people.

## Map external users to your people

1. Go to _WFM > Administration > Scheduling > Employees_{:.breadcrumbs}.
2. Assign external user identifiers to your people.

Learn more about {% link_new mapping external user identifiers | features/acd-integration/cloud/import-agent-status-data.md | #map-external-identifiers-to-people-in-injixo %} to people.

## Map external statuses to injixo activities

1. Go to _Intraday > Configuration_{:.breadcrumbs}.
2. Map external statuses from Odigo to injixo activities.

Learn more about {% link_new mapping external statuses | features/intraday/map-external-status.md | #map-external-statuses-to-activities %} to injixo activities.

