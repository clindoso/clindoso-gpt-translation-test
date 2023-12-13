---
title: Agentstatusgegevens importeren
product_label:
  - advanced
  - enterprise
  - classic
description: injixo zo configureren dat agentstatusgegevens op de juiste manier worden geïmporteerd.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-on-premise-integration.md
---

Externe systemen, zoals ACD's, leggen vast wanneer medewerkers overschakelen van de ene activiteit naar de andere. injixo kan deze gegevens gebruiken ter ondersteuning van Intraday Management.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Vereisten

Om agentstatusgegevens te importeren, moet je eerst {% link_new een integratie toevoegen | features/acd-integration/cloud/how-integrations-work.md %}. De integratie moet imports van agentstatusgegevens ondersteunen.

Ga naar _Account > Integraties_{:.breadcrumbs} om te controleren of het importeren van agentstatusgegevens door je integratie wordt ondersteund. Indien beschikbaar geeft injixo de labels Agentstatus (historische gegevens) en/of RTA (realtime) weer.

Nadat je de integratie hebt toegevoegd, moet je de medewerker-ID's van het externe systeem toevoegen aan medewerkers in injixo. Optioneel kun je de activiteiten van het externe systeem ook aan dezelfde activiteiten in injixo toewijzen.

## Medewerker-ID's van externe systemen

Medewerker-ID's van externe systemen zijn aanbiederspecifiek. Ze identificeren de gebruikers in het externe systeem aan de hand van een e-mailadres, een gebruikersnaam of een agent-ID.

Let op de juiste spelling, het juiste gebruik van hoofd- en kleine letters en spaties om te voorkomen dat een import mislukt.

| Aanbieder                 | Vereiste gebruikers-ID              |
| ---------------------- | ------------------------------------- |
| Five9                  | gebruikersnaam van Five9                  |
| Genesys Cloud          | gebruikersnaam van PureCloud              |
| Genesys Engage         | gebruikersnaam van PureEngage             |
| Talkdesk               | e-mailadres dat voor Talkdesk wordt gebruikt        |
| UJET                   | e-mailadres dat voor UJET wordt gebruikt            |
| Sikom                  | gebruikersnaam van Sikom                  |
| Mitel MiVoice Business | gebruikersnaam van Mitel MiVoice Business |
| Vonage                 | agent-ID van Vonage                  |
| Avaya CMS              | gebruikersnaam van Avaya CMS              |

## Medewerker-ID's van externe systemen aan medewerkers toewijzen in injixo

Om gegevens te importeren moet je externe gebruikers-ID's aan medewerkers toewijzen. Je kunt dit voor alle medewerkers doen, of alleen voor diegenen van wie je agentstatusgegevens wilt importeren.

1. Ga naar _WFM > Administratie > Planning > Medewerkers_{:.breadcrumbs} en selecteer een medewerker.
2. Klik bovenaan op **Externe systemen** of scroll naar beneden naar de sectie **Externe systemen**.
3. Klik op het pictogram Toevoegen {% icon item-add | icon-only %} om een extern systeem toe te voegen.  
   Er wordt een venster geopend.
4. Selecteer in het vervolgkeuzemenu **Extern systeem** de integratie die je eerder hebt aangemaakt.
5. Voer in het veld **Medewerker-ID Extern Systeem** een uniek nummer in voor je medewerkers, bijvoorbeeld het personeelsnummer.
6. Voer in het veld **Toevoeging** de gebruikers-ID van de medewerker in die in het externe systeem wordt gebruikt, bijvoorbeeld het e-mailadres van de medewerker.
7. Klik op _OK_{:.doc-button}.

Nadat je de secties van je medewerkers hebt bijgewerkt, worden de agentstatusgegevens bij de volgende import geïmporteerd.


## Activiteiten van het externe systeem toewijzen

Activiteiten uit externe systemen zijn de activiteiten die het externe systeem registreert als medewerkers zich aan- of afmelden, of van de ene activiteit naar de volgende omschakelen, bijvoorbeeld van e-mails naar telefonie.

Je kunt activiteiten uit externe systemen aan bestaande activiteiten toewijzen. Als je echter besluit om {% link_new nieuwe activiteiten aan te maken | features/administration/activities.md | #een-activiteit-aanmaken %}, zorg er dan voor dat je ze aan je {% link_new eenheid | features/administration/create-and-manage-planning-units.md | #activiteiten-toevoegen %} toevoegt, zodat ze later correct worden weergegeven.

Integraties slaan deze activiteiten standaard op in de activiteit Aanwezig (ID 1) en de status voor alle activiteiten wordt weergegeven als Aanwezig. injixo kan dezelfde activiteiten weergeven als je externe systeem. Hiervoor moet je de activiteiten van het externe systeem opnieuw aan andere activiteiten in injixo toewijzen. Volg hiervoor de onderstaande stappen.


Om activiteiten opnieuw toe te wijzen, moet je de integratie eerst pauzeren:

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Klik in de lijst met integraties op het pictogram Importeren opschorten {% icon pause_circle | icon-only %} naast de integratie waarvoor je activiteiten opnieuw wilt toewijzen.

Volg de volgende stappen zodra je je integratie hebt gepauzeerd:

1. Ga naar _Plan > Configuratie > Activiteiten_{:.breadcrumbs}.
2. Klik op de activiteit die je opnieuw wilt toewijzen.
3. Klik in de sectie **Externe Systemen** op _Bewerken in WFM_{:.doc-button}. 
4. Ga naar de sectie **Externe Systemen**.
5. Klik op het pictogram Toevoegen {% icon item-add | icon-only %}.
6. In het venster **Externe Systemen**:<br>
   - Selecteer in het vervolgkeuzemenu **Extern Systeem** de integratie die je eerder hebt aangemaakt.
   - Selecteer in het vervolgkeuzemenu **Aanduiding activiteit extern systeem** de activiteit van het externe systeem die je aan de in injixo geselecteerde activiteit wilt toewijzen.
   - Selecteer in het vervolgkeuzemenu **Classificatie** de waarde 1.
7. Klik op _OK_{:.doc-button}.

Om meer activiteiten opnieuw toe te wijzen, klik je op de volgende activiteit en ga je verder vanuit het configuratiemenu aan de rechterkant.


Als je klaar bent met het toewijzen van activiteiten, ga je naar _Account > Integraties_{:.breadcrumbs} en klik je op het pictogram Import hervatten {% icon play_circle | icon-only %} naast je integratie om het importeren te hervatten.
