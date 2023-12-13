---
title: Een on-premise integratie toevoegen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Verbind je on-premise-database met injixo om het contactvolume, AHT en agentstatusgegevens te importeren.
related_articles:
  - overwrite_title: Hoe werken integraties?
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: CloudLink installeren
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Agentstatusgegevens importeren
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Wat zijn on-premise-integraties?

On-premise-integraties gebruiken {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} om een systeem met je lokale netwerk te verbinden. Nadat ze zijn verbonden, importeren on-premise-integraties historische gegevens van maximaal drie jaar.

## Een on-premise integratie toevoegen

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Selecteer je externe systeem en klik op _Voeg integratie toe_{:.doc-button}. Als je externe systeem beschikbaar is in verschillende modellen, klik dan op _Kies een model_{:.doc-button} en klik op _Voeg integratie toe_{:.doc-button}.
3. Vul de vereiste informatie in het formulier in. Geef je integratie een unieke naam, zodat je later de bron van je gegevens terug kunt vinden.
4. Installeer de {% link_new injixo Cloud Link-client | features/acd-integration/cloud/install-cloud-link.md %}.
5. Klik op _Integratie opslaan_{:.doc-button}.

{{ 1 | image: 'Integratie van Genesys Engage', '85%' }}

De integratie importeert nu contactgegevens naar injixo. De eerste import kan wat langer duren. Alle queues van het gekoppelde systeem zijn automatisch beschikbaar voor toewijzing op het {% link_new workload-configuratiescherm | features/forecast/injixo-forecast/manage-workloads.md | #workloads-aanmaken %} in injixo Forecast.

Als je integratie de import van agentstatusgegevens ondersteunt, dan dien je eerst {% link_new externe gebruiker-IDs en activiteiten toe te wijzen | features/acd-integration/cloud/import-agent-status-data.md %}. Daarna kan de integratie agentstatusgegevens importeren.
