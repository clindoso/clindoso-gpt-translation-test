---
title: Hoe werken integraties?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lees hoe integraties werken, welke integraties worden ondersteund en hoe je integraties toevoegt en verwijdert.
promote-service: acd-integration-support
related_articles:
  - overwrite_title: Cloudlink installeren
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Agentstatusgegevens importeren
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

## Wat zijn integraties?

Om je workforce management te ondersteunen, heeft injixo contact- en agentstatusgegevens uit externe systemen nodig, zoals ACD- of CRM-systemen. Door je ACD en/of CRM in injixo te integreren, kan injixo je gegevens ontvangen en verwerken.

injixo biedt systeemeigen vendorspecifieke integraties en algemene integraties. Afhankelijk van de integratie ontvangt injixo informatie met een interval van 15, 30 of 60 minuten (import van historische gegevens) of zelfs binnen seconden (import van realtime gegevens).

### Aanleveringsmethoden

De aanleveringsmethode van een integratie bepaalt hoe injixo verbinding maakt met het externe systeem.

- Cloud: integraties die direct verbonden zijn met een ander cloudsysteem, zoals  Five9 of Vonage
- On-premise: integraties waarvoor je eerst {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} moet configureren, voordat ze zich met een systeem in je lokale netwerk kunnen verbinden, zoals Genesys Engage of Sikom

### Vendorspecifieke en algemene integraties

Vendorspecifieke integraties zijn afgestemd op een bepaald systeem en een aanbevolen manier om verbinding te maken. Indien er geen vendorspecifieke integratie beschikbaar is, kun je ook een algemene integratie gebruiken:

- Database: on-premise-integratie die gebruik maakt van een SQL-query om gegevens uit een database te lezen
- CSV: integratie op basis van bestanden om CSV-bestanden te importeren met injixo Cloud Link
- injixo API: cloudintegratie vereist om HTTP-verzoeken naar injixo API te sturen

### Welke gegevens worden er geïmporteerd?

Afhankelijk van de integratie importeert injixo contactgegevens en/of agentstatusgegevens:

- Contactgegevens (telefonie, chats, social media, tickets, e-mails, documenten) bevatten de ontvangen en verwerkte volumes en de gemiddelde afhandeltijd. Ze worden gebruikt om forecasts te berekenen.
- Agentstatusgegevens (aanmelden, afmelden, nawerk, pauzes etc.) bevatten informatie over de activiteiten van personen, bijvoorbeeld wanneer een activiteit afsluiten en met de volgende activiteit beginnen. Deze gegevens worden gebruikt voor intraday management.

## Een integratie toevoegen

Lees de volgende artikelen voor meer informatie over het configureren van je integratie:

- {% link_new Een cloudintegratie toevoegen | features/acd-integration/cloud/add-cloud-integration.md %}
- {% link_new Een on-premise-integratie toevoegen | features/acd-integration/cloud/add-on-premise-integration.md %}
- {% link_new Een CSV-integratie toevoegen | features/acd-integration/cloud/add-csv-integration.md %}
- {% link_new Een database-integratie toevoegen | features/acd-integration/cloud/add-database-integration.md %}
- {% link_new Gegevens importeren met injixo API | features/acd-integration/cloud/import-data-with-injixo-api.md %}

Zodra je een integratie hebt toegevoegd begint deze gegevens naar injixo te sturen.

Contactgegevens worden automatisch geïmporteerd. Om met contactgegevens te werken, dien je geïmporteerde queues aan een (nieuwe) workload toe te voegen om {% link_new een forecast te berekenen | getting-started/calculate-a-forecast.md %}. Bereken vervolgens de personeelsbehoefte en maak daarna je planning aan.

> Dit is een vereiste om agentstatusgegevens weer te kunnen geven.
>
> Om agentstatusgegevens te bekijken in de Intraday-module, dien je {% link_new externe gebruikers- en activiteiten-ID's te mappen | features/acd-integration/cloud/import-agent-status-data.md %}. Pauzeer eerst je integratie voordat je hiermee begint.

## De gegevensimport pauzeren

De activiteitenmapping wordt overschreven door de actieve integratie. Om de mapping te behouden, dien je de gegevensimport van de integratie te pauzeren door op het {% icon pause_circle %} naast de integratie op de overzichtspagina te klikken.

Om de gegevensimport te hervatten zodra het mappen is afgerond, klik je op het {% icon play_circle %}. Ontbrekende gegevens worden opnieuw geïmporteerd.

## Een integratie verwijderen

Als een integratie wordt verwijderd, blijven de geïmporteerde gegevens behouden. De queues blijven aan je workload toegewezen. Je kunt de queues die door een integratie zijn aangemaakt niet verwijderen.

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Klik vervolgens op het {% icon pencil %} naast de integratie die je wilt verwijderen.
3. Klik rechtsonder op _Integratie verwijderen_{:.doc-button}.

Je hebt de integratie uit injixo verwijderd.

Opmerking: Je kunt geen queues aan nieuwe workloads toevoegen als de ze door een verwijderde integratie zijn geïmporteerd.

## Veelgestelde vragen

| Vraag                                                | Antwoord                                                                                                                                                                                                                                                     |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kan ik twee integraties met dezelfde naam aanmaken?       | Ja, maar dit wordt niet aanbevolen. injixo gebruikt de queues van je integratie om forecasts te maken. Als er meerdere queues zijn met dezelfde naam, kan er verwarring ontstaan bij het identificeren van de gegevensbron en het vaststellen welke queue bij welke integratie hoort. |
| Kan ik een bestaande naam van een integratie voor een nieuwe integratie gebruiken? | Om de oude van de nieuwe integratie in injixo Forecast te kunnen onderscheiden, is het raadzaam om de naam van de oude integratie te veranderen in _integratienaam_oud_, voordat je de nieuwe integratie aanmaakt en de oude verwijdert.                                                  |
