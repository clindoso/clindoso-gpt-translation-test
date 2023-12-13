---
title: Een Mitel-integratie toevoegen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lees hoe je je Mitel-CRM verbindt met injixo om gegevens te importeren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Een Mitel-integratie is een on-premise-integratie die de oproep-, chat- en social media-geschiedenis, en agentstatusgegevens importeert.

De integratie maakt gebruik van {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Mitel-integratie toevoegen

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Mitel**-tegel op _Voeg integratie toe_{:.doc-button}.

## Je nieuwe Mitel-integratie configureren

1. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
2. Installeer en maak verbinding met {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Selecteer in de sectie **Regionale instellingen** je **ACD tijdzone**.
4. Stel in de sectie **Toegangsgegevens database** je integratie in:
 - Voer je databasehost en -poort in.
 - Voer je gebruikersnaam en wachtwoord voor de database in.
5. Als je agentstatusgegevens wilt importeren, dan vink je het selectievakje **Agentstatusgegevens importeren** aan in de sectie **Configuratie**.<br>Opmerking: Om agentstatusgegevens te importeren, dien je eerst {% link_new externe gebruikers-ID's en activiteiten toe te wijzen | features/acd-integration/cloud/import-agent-status-data.md %}.
6. Klik op _Integratie opslaan_{:.doc-button}.

De integratie importeert vanaf nu gegevens in injixo. 

## Een Mitel-integratie bewerken

Als er integratiegegevens veranderen, denk bijvoorbeeld aan aanmeldgegevens voor de database, dan kun je de configuratie van je integratie bewerken en updaten. De gegevensimport gaat gewoon door met de geüpdate configuratie.
