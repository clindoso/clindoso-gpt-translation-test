---
title: Intraday Adherence
toc: true
product_label:
  - advanced
  - enterprise
description: Krijg inzicht in de mate waarin medewerkers zich gedurende de dag aan hun planning hebben gehouden.
archive_ref: 20210422-de-adherence
---

Met Intraday Adherence kun je de ingeplande activiteiten van medewerkers vergelijken met de activiteiten die zij hebben uitgevoerd om eventuele out-of-adherence-perioden in het verloop van de dag vast te stellen.

Intraday Adherence geeft gegevens weer nadat je de {% link_new realtime agentstatusimport | features/acd-integration/cloud/import-agent-status-data.md %} hebt geconfigureerd.

Ben je nog niet zo vertrouwd met realtime adherence? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/intraday/real-time-adherence.md %}.

## Gegevens opzoeken en weergeven

1. Ga naar _Intraday > Intraday Adherence_{:.breadcrumbs}
2. Selecteer een **eenheid** en/of **groep** om gegevens van agenten weer te geven.
3. Klik op _Vandaag_{:.doc-button} of _Gisteren_{:.doc-button} of gebruik de **datumkiezer** om een andere dag weer te geven.

De tabel geeft out-of-adherence-gegevens per medewerker weer. In de tabelkop kun je perioden herkennen met een lage adherence. Je kunt de tabel sorteren of de zoekfunctie bovenaan de pagina gebruiken om het aanzicht te filteren. Zie {% link_new filteren en sorteren | features/intraday/real-time-adherence.md | #search-and-filter %}.

{{ 1 | image: 'Intraday Adherence','100%' }}

> Beperk het aanzicht voor bepaalde gebruikers tot relevante medewerkers
>
> Configureer de leesrechten voor specifieke eenheden of groepen op basis van {% link_new gebruiker of gebruikersrol | getting-started/configure-user-roles.md | #wfm-rechten-instellen %}.

## Adherence-score

De score laat zien of er afwijkingen waren tussen de ingeplande en uitgevoerde activiteiten van medewerkers.

Je kunt de adherence gedurende het verloop van de dag in de grafiek analyseren. Als de dag nog niet is afgelopen, wordt de score berekend tot en met de tijdstempel van de laatste update. Deze wordt boven de adherence-score weergegeven.

De stippellijn geeft de beoogde adherence-score weer. Je kunt {% link_new de beoogde score aanpassen | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}.

{{ 2 | image: 'Adherence score','100%' }}

## Tabel met adherence-gegevens van agenten

In de tabel worden de adherence-gegevens voor de medewerkers weergegeven die vandaag waren ingepland. De tabel kan worden gesorteerd op de naam van de medewerker en de adherence-score.

Elke rij in de tabel staat voor de tijdlijn van een medewerker. Je kunt de verschillen tussen de ingeplande en uitgevoerde activiteiten van de medewerker bekijken. Elke medewerker heeft een individuele adherence-score. De individuele scores opgeteld vormen samen de totale score van de eenheid (weergegeven in de tabelkop). Afwijkingen worden gemarkeerd als de score zakt tot onder de {% link_new geconfigureerde beoogde adherence-score | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}.

De kleuren geven drie verschillende soorten afwijkingen aan:

- Niet aanwezig (rood)
- Verkeerde activiteit (geel)
- Niet ingepland (blauw)

Klik op een agent om de {% link_new intraday adherence van agenten | features/intraday/adherence-intraday.md | #intraday-adherence-van-agenten %} te bekijken. {% link_new Matches | features/intraday/adherence-matches.md %} en {% link_new buffertijden | features/intraday/real-time-adherence.md | #buffer-time %} hebben invloed op de status en de soorten adherence. Lees meer over de {% link_new status en soorten | features/intraday/real-time-adherence.md | #status %}.

{{ 3 | image: 'Tabel met adherence-gegevens van agenten','100%' }}

## Intraday adherence van agenten

Het aanzicht Intraday adherence van agenten biedt inzicht in adherence-incidenten. Zo kun je zien op welke momenten medewerkers hun planning niet hebben opgevolgd. Klik op een regel in de tabel om te bekijken wat een medewerker gedurende de dag heeft gedaan. In het aanzicht worden afzonderlijke activiteiten weergegeven aan de hand van de ingestelde kleuren.

In de tijdlijn kun je de ingeplande en uitgevoerde activiteiten vergelijken en de daaruit resulterende out-of-adherence-statussen bekijken. De onderstaande tabel geeft elke out-of-adherence-periode weer op een regel.

Gebruik de volgende functies om het dagaanzicht te wijzigen:

- de **maandkiezer** bovenaan en het **dagelijks overzicht** aan de linkerkant.
- de **navigatiepijlen** naast de datum van vandaag boven de tabel.

Het dagelijks overzicht geeft de adherence-score weer voor elke dag van een geselecteerde maand. Boven het dagaanzicht kun je verschillende kernindicatoren voor de geselecteerde maand, bijvoorbeeld de adherence-score of de ingeplande duur.

{{ 4 | image: 'Details over de planningsopvolging van agenten gedurende de dag','100%' }}

## Adherence-rapport (CSV-bestand)

Soms is het wellicht nodig om adherence-gegevens voor afzonderlijke medewerkers over een langere periode te analyzeren, bijvoorbeeld om bonusbetalingen te berekenen. Het Adherence-rapport is een CSV-bestand dat samengevoegde adherence- en conformiteitsgegevens bevat. Volg deze stappen om het te downloaden:

1. Ga naar _Intraday > Intraday Adherence_{:.breadcrumbs}
2. Selecteer minimaal een eenheid en/of groep.
3. Klik op _Rapport downloaden_{:.doc-button}.  
   Er wordt een venster geopend.
4. Selecteer een datumbereik voor het rapport. Je kunt een datumbereik van een dag tot en met zes maanden in het verleden selecteren.
5. Klik op _Rapport downloaden_{:.doc-button}.

In de onderstaande tabel worden de kolommen van het rapport uitgelegd.

| Kolom             | Definitie                                                                     | Berekening                                                                |
| ------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Minutes in adherence | Aantal minuten adherence (activiteiten): Tijd besteed aan activiteiten die overeenkomen met de ingeplande activiteiten      | -- |
| Minutes out of adherence  | Aantal minuten out-of-adherence (activiteiten). Tijd besteed aan activiteiten die niet overeenkomen met de ingeplande activiteiten        | -- |                  
| Adherence in %   | Adherence (activiteiten) in %: Percentage van werktijd besteed aan activiteiten die overeenkomen met de ingeplande activiteiten       | Aantal minuten adherence/ingeplande minuten * 100% |
| Minutes out of conformance   | Aantal minuten out-of-adherence (werktijd) %: Het verschil tussen de gewerkte tijd en de ingeplande tijd             | Gewerkte minuten - ingeplande minuten |
| Conformance in % | Adherence (werktijd) in %: Percentage gewerkte tijd in overeenstemming met de ingeplande werktijd | Gewerkte tijd/ingeplande tijd * 100% |
| Scheduled in %  | Ingepland in %: Het percentage ingeplande werktijd voor een bepaald type activiteit. | Ingeplande tijd voor het relevante type activiteit/totale ingeplande tijd * 100%              |
| Actual in %  | Gewerkt in %. Het percentage gewerkte tijd dat aan een bepaald type activiteit is besteed | Gewerkte tijd voor het relevante type activiteit/totale gewerkte tijd * 100%              |

Elke rij met gegevens bevat een link om de bijbehorende gegevens in _Intraday > Intraday Adherence_{:.breadcrumbs} weer te geven.

## Veelgestelde vragen

| Vraag                            | Antwoord                                                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Waarom ontbreken sommige (of alle) medewerkers? | Wis je zoekopdracht. Controleer of de medewerkers naar wie je op zoek bent vandaag zijn ingepland in de geselecteerde eenheid of groep.           |
| Waarom kan ik geen specifieke datum selecteren? | Je hebt toegang tot historische adherence-gegevens van de afgelopen zes maanden tot de huidige datum, plus de huidige maand (bijvoorbeeld: als het vandaag 15 juli is, dan kun je datums selecteren tussen 1 januari en 15 juli.) |
