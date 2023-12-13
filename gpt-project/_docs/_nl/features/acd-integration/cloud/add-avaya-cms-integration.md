---
title: Een Avaya CMS-integratie toevoegen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lees hoe je je Avaya-database met injixo verbindt om gegevens te importeren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Een Avaya CMS-integratie is een on-premise-integratie die gespreks- en agentstatusgegevens importeert.

De integratie maakt gebruik van {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Avaya CMS-integratie toevoegen

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Avaya CMS**-tegel op _Voeg integratie toe_{:.doc-button}.

## Je nieuwe Avaya CMS-integratie configureren

1. Geef de nieuwe integratie een unieke naam die nog niet wordt gebruikt.
   Aan de hand van de naam kun je de gegevensbron vinden en bepalen welke queue bij welke integratie hoort.<br>Voorbeeld: Avaya-integratie - Customer Support-team
1. Installeer en maak verbinding met {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
1. Configureer je integratie in de sectie **Configuratie**:
 - Voer de [connection string](#connection-string) in die de parameters bepaalt die nodig zijn om je CMS-database te verbinden. 
 - Selecteer de tijdzone van je database in het vervolgkeuzemenu.
 - Vink het selectievakje **Gedetailleerde agentstatussen importeren** aan om informatie over skills (agent profile) en splits (call routing) aan geïmporteerde agentstatussen toe te voegen.
 - Vink het selectievakje **Realtime gegevens importeren** aan als je realtime agentstatusgegevens wilt importeren. Voer in dat geval in het veld **Poort** een poortnummer in.<br>
   injixo Cloud Link opent een TCP-luisterpoort op de gespecificeerde poort. De Avaya Generic RTA-service maakt verbinding met deze poort en begint realtime agentstatusgegevens te streamen. De Avaya Generic RTA-service is gelicentieerd en geconfigureerd in Avaya.
1. Klik op _Integratie opslaan_{:.doc-button} om de integratie in te stellen.

De integratie importeert vanaf nu gegevens in injixo. Om agentstatusgegevens te importeren moet je eerst {% link_new externe gebruikers-ID's en activiteiten toewijzen | features/acd-integration/cloud/import-agent-status-data.md %} zodra je Avaya-integratie is ingesteld. Als je de optie **Realtime gegevens importeren** al had ingesteld, pauzeer dan eerst je integratie.

## Connection string

De Avaya CMS-integratie heeft de connection string nodig om verbinding te maken met je Avaya CMS-database. Omdat Avaya CMS meestal gebruik maakt van een IBM Informix-database, moet je een speciale connection string gebruiken. 

Voorbeelden van connection strings die gebruikmaken van de IBM Informix ODBC-driver:<br>
- `DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;` (native-toegang via ODBC-driver)
- `DSN=AvayaCMS;DELIMIDENT=y;` (vereist een ODBC-verbinding met de naam AvayaCMS)
Als je Avaya CMS geen IBM Informix-database gebruikt, dan moet je eerst voor de vereiste connection string zorgen voor je specifieke databasetype en ODBC-driver. Avaya ondersteunt alleen ODBC-connectiviteit.

## Een Avaya CMS-integratie bewerken

Als er integratiegegevens veranderen, denk bijvoorbeeld aan aanmeldgegevens voor de database, dan kun je de configuratie van je integratie bewerken en updaten. De gegevensimport gaat gewoon door met de geüpdate configuratie.
