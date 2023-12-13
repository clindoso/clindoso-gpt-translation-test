---
title: Een Genesys Cloud-integratie toevoegen
description: Lees hoe je je Genesys Cloud-CRM met injixo verbindt om gegevens te importeren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Een Genesys Cloud-integratie is een cloud-integratie die de oproep-, e-mail- en chatgeschiedenis, en agentstatus- en RTA-gegevens importeert.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Genesys Cloud-integratie toevoegen

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Genesys**-tegel op _Kies een model_{:.doc-button}.
4. Klik in de sectie **Genesys Cloud** op _Voeg integratie toe_{:.doc-button}.

## Je Genesys Cloud-integratie configureren

1. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
2. Ga naar de sectie **API toegangsgegevens** en kopieer en plak je API-key en API-secret van Genesys Cloud.
3. Selecteer in de sectie **Configuratie** je accountregio.
4. (Optioneel) Vink het selectievakje **Gedetailleerde 'on-queue'-agentstatussen importeren** aan.<br>De agentstatus 'on-queue' omvat verschillende statussen, zoals: communication, interacting, idle, not responding. Bij het importeren van agentstatussen maakt injixo onderscheid tussen individuele statussen die onder 'queue' worden samengevat.
5. Klik op _Integratie opslaan_{:.doc-button}.
