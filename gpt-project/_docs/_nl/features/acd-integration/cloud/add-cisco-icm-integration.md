---
title: Een Cisco ICM-integratie toevoegen
description: Lees hoe je je Cisco-ICM verbindt met injixo om gegevens te importeren.
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

De Cisco ICM-integratie importeert RTA-gegevens. De integratie maakt gebruik van {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Cisco ICM-integratie toevoegen

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Cisco ICM**-tegel op _Voeg integratie toe_{:.doc-button}.

## Je Cisco ICM-integratie configureren

1. Geef de nieuwe integratie een unieke **naam** die naar de gegevensbron verwijst.
2. Klik in de sectie **injixo Cloud Link** op de **downloadlink** voor je besturingssysteem.<br>
   > Opmerking
   >
   > Ook als je Cloud Link al hebt gedownload voor een andere integratie, moet je op deze pagina nog steeds de Cisco-specifieke versie downloaden.
3. Installeer en maak verbinding met {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.<br>
4. Configureer je integratie in de sectie **Configuratie**:

   - Voer een **connection string** in met de vereiste parameters om verbinding te maken met je Cisco-database:   
   `DRIVER={MS SQL Server};Server=myServerAddress;Database=myDataBase;UserId=myUsername;Password=myPassword;`
   - Selecteer je **Tijdzone database** in het vervolgkeuzemenu.
   - Voer je **client-ID** en **wachtwoord** voor Cisco ICM in.
   - Voer je **periferie-gateway 1** in.
   - (Optioneel) Voer je **periferie-gateway 2** in.

4. Klik op _Integratie opslaan_{:.doc-button}.

Vanaf nu importeert injixo RTA-gegevens. Deze worden pas zichtbaar nadat je externe gebruikers-ID's aan je medewerkers hebt toegewezen.

## Externe gebruikers aan je medewerkers toewijzen

1. Ga naar _WFM > Administratie > Planning > Medewerkers_{:.breadcrumbs}.
2. Wijs externe gebruikers-ID's toe aan je medewerkers.
   > Opmerking
   >
   > De externe gebruikers-ID's zijn de Unified CCE Skill Target IDs.

Lees meer over {% link_new het toewijzen van externe gebruikers-ID's | features/acd-integration/cloud/import-agent-status-data.md | #medewerker-ids-van-externe-systemen-aan-medewerkers-toewijzen-in-injixo %}.

## Agentstatussen toewijzen aan injixo-activiteiten

1. Ga naar _WFM > Administratie > Planning > Activiteiten_{:.breadcrumbs}.
2. Wijs Cisco ICM-activiteiten toe aan injixo-activiteiten.

Lees meer over het {% link_new toewijzen van externe activiteiten | features/acd-integration/cloud/import-agent-status-data.md | #activiteiten-van-het-externe-systeem-toewijzen %} aan injixo-activiteiten.
