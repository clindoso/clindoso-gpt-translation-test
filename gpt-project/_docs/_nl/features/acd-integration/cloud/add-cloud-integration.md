---
title: Een cloudintegratie toevoegen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Verbind je cloud-ACD met injixo om gegevens te importeren.
related_articles:
  - overwrite_title: Hoe werken integraties?
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Een Five9-integratie toevoegen
    filepath: features/acd-integration/cloud/add-five9-integration.md
  - overwrite_title: Agentstatusgegevens importeren
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Wat zijn cloudintegraties?

Cloudintegraties halen gegevens direct uit een cloudsysteem. injixo ondersteunt een groot aantal cloudintegraties.

## Een cloudintegratie toevoegen

1. Ga naar *Account > Integraties*{:.breadcrumbs}. Op deze pagina worden alle beschikbare integraties weergegeven.
2. Klik *Voeg integratie toe*{:.doc-button} en voer de benodigde informatie in. In dit voorbeeld stellen we de Five9-integratie in, maar de procedure voor het instellen van andere cloudintegraties is vergelijkbaar.
3. Kies een unieke naam voor je integratie. De naam moet verwijzen naar de bron van de gegevens.
4. Voer de **gebruikersnaam** en het **wachtwoord** in van een gebruiker die in je Five9-account een adminrol heeft.
5. Stel de overige integratiespecifieke gegevens in (zoals de regio van je Five9-account en de manier waarop je je queues wilt groeperen).
6. Klik op _Integratie opslaan_{:.doc-button} om de integratie op te zetten met de ingevoerde gegevens.

{{ 1 | image: 'Five9-integratie', '80%' }}

De integratie importeert nu gegevens naar injixo. Het importeren kan tot 15 minuten duren. Alle queues van het gekoppelde systeem zijn automatisch beschikbaar voor mapping op het {% link_new workload-configuratiescherm | features/forecast/injixo-forecast/manage-workloads.md | #workloads-aanmaken %} in injixo Forecast.

Als je integratie de import van agentstatusgegevens ondersteunt, dan dien je eerst {% link_new externe gebruiker-IDs en activiteiten te mappen | features/acd-integration/cloud/import-agent-status-data.md %} voordat je agentstatusgegevens kunt importeren.
