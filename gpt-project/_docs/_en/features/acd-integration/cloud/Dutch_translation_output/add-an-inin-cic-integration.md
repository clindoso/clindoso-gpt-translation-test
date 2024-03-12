---
title: Voeg een Interactive Intelligence CIC-integratie toe <!-- GPT translation -->
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lees hoe je injixo met Interactive Intelligence CIC verbindt om gegevens te importeren. <!-- GPT translation -->
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Een Interactive Intelligence CIC-integratie maakt verbinding met een on-premise Interactive Intelligence-platform en importeert daar activiteitengegevens. <!-- GPT translation -->

De integratie maakt gebruik van {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}. <!-- TM 100 -->

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}. <!-- TM 100 -->

## Een Interactive Intelligence CIC-integratie toevoegen <!-- GPT translation -->

1. Ga naar _Account > Integraties_{:.breadcrumbs}. <!-- TM 100 -->
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}. <!-- TM 100 -->
3. Klik in de **Genesys**-tegel op _Kies een model_{:.doc-button}. <!-- TM 100 -->
4. In de sectie **Interactive Intelligence CIC** klik je op _Voeg integratie toe_{:.doc-button}. <!-- GPT translation -->

## Maak je Interactive Intelligence CIC-integratie aan <!-- GPT translation -->

1. Geef de nieuwe integratie een unieke naam die nog niet wordt gebruikt. <!-- TM 100 -->
   De naam helpt je om de gegevensbron te identificeren en te bepalen welke queue bij welke integratie hoort.<br>Voorbeeld: CIC - Customer Support Team <!-- GPT translation -->
2. Installeer en maak verbinding met {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}. <!-- TM 100 -->
3. Stel in de sectie **Configuratie** de integratie als volgt in: <!-- GPT translation -->
 - **Tijdzone**: Selecteer een tijdzone voor de ACD uit de vervolgkeuzelijst. <!-- GPT translation -->
 - **Serveradressen ACD**: Voer de DNS-naam of het IP-adres en de poort van je ACD in, gescheiden door een dubbelepunt, bijvoorbeeld: acd.example.com:8080.<br>Scheid je invoer met komma's als je meerdere ACD's wilt invullen. <!-- GPT translation -->
4. Klik op _Integratie opslaan_{:.doc-button} om de integratie aan te maken. <!-- GPT translation -->

De integratie importeert nu gegevens in injixo. Om agentstatusgegevens te importeren, moet je eerst {% link_new externe gebruikers-ID's of actviteiten toewijzen | features/acd-integration/cloud/import-agent-status-data.md %} nadat de Interactive Intelligence CIC-integratie is aangemaakt. <!-- GPT translation -->

## Een Interactive Intelligence CIC-integratie bewerken <!-- GPT translation -->

Je kunt de integratiebewerken om de configuratie te actualiseren als er integratiedetails zijn gewijzigd, zoals je ACD-poort. De gegevensimport loopt onverminderd door met de nieuwe configuratie. <!-- GPT translation -->