---
title: Een Talkdesk-integratie toevoegen
description: Lees hoe je je Talkdesk-ACD verbindt met injixo om gegevens te importeren.
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
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Een Talkdesk-integratie is een cloudintegratie die oproep- en agentstatusgegevens importeert.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Talkdesk-integratie toevoegen

1. Ga naar _Account > Integraties_{:.breadcrumbs}.  
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Talkdesk**-tegel op _Voeg integratie toe_{:.doc-button}.
4. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
5. Voer in de sectie **Gebruikersgegevens** de Talkdesk-specifieke informatie in:

   - Voer je accountnaam voor Taskdesk in.
   - Voer de client-ID en de client-secret van een Talkdesk OAuth-client in.

     > Maak voor Client-ID en Client-secret in Talkdesk [een nieuwe OAuth-client](https://docs.talkdesk.com/docs/creating-a-new-oauth-client) aan.
     >
     > Je kunt ook een bestaande OAuth-client gebruiken die als volgt is geconfigureerd:
     >
     > - Toekenningstype: clientgegevens
     > - Scopes: data-reports:read and data-reports:write

6. Selecteer in de sectie **Configuratie** je accountregio.

7. Klik op _Integratie opslaan_{:.doc-button}.  
   De integratie test de verbinding en rapporteert eventuele problemen.  
   Nadat de controle is uitgevoerd, begint de integratie gegevens naar injixo te importeren.

<!-- ## Talkdesk Data in injixo -->

## En nu?

Nadat gespreksgegevens in queues zijn geïmporteerd, kun je je eerste workload aanmaken. Lees de gerelateerde artikelen voor meer informatie over de stappen die nodig zijn om agentstatusgegevens in te stellen.
