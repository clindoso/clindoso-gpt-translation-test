---
title: Wat zijn planningsperioden?
description: Ontdek voor welke doeleinden planningsperioden worden gebruikt en hoe je ze kunt weergeven, bewerken en verwijderen (Schedules).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Medewerkers toestaan om hun planningen te bekijken
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
  - overwrite_title: Medewerkers toestaan om diensten te ruilen
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Verlofperioden
    filepath: features/scheduling/time-off/time-off-periods.md
---

Planningsperioden beslaan een tijdvak van een aantal dagen, weken of maanden. Gebruik ze als je:

- medewerkers de mogelijkheid wilt geven om {% link_new hun planning te bekijken | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %};
- medewerkers de mogelijkheid wilt geven om {% link_new diensten met elkaar te ruilen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %};
- medewerkers de mogelijkheid wilt geven om {% link_new zich op diensten in te schrijven | features/scheduling/schedules/schedules-shift-bidding.md %}.

Gebruik {% link_new verlofperioden | features/scheduling/time-off/time-off-periods.md %} om medewerkers de mogelijkheid te geven om verlofaanvragen in te dienen.

## Status

Iedere planningsperiode heeft een status. Deze status geeft medewerkers gedurende de hele planningsperiode toegang tot bepaalde opties of beperkt de toegang hiertoe. Meestal wijzig je de status van een planningsperiode meerdere keren tijdens het planningsproces, bijvoorbeeld nadat je de planning hebt afgesloten of wanneer de periode voor het indienen van dienstverzoeken is verstreken.

| Status                | Toelichting                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Niet gepubliceerd           | Medewerkers kunnen de gepubliceerde planning niet bekijken, kunnen zich niet {% link_new op diensten inschrijven en geen diensten met elkaar ruilen.                                                                                                                 | features/scheduling/schedules/schedules-shift-bidding.md %} Gebruik deze status als je de planning nog niet met je medewerkers wilt delen. |
| Inschrijven op diensten geactiveerd | Medewerkers kunnen de gepubliceerde planning bekijken, zich inschrijven op diensten, diensten met elkaar ruilen en {% link_new opmerkingen | features/scheduling/shiftcenter/add-and-delete-items.md | #add-comments %} bekijken die op het niveau Planning zijn ingevoerd. Deze status kan niet worden toegekend als de planningsperiode een einddatum heeft die al is verstreken. |
| Gepubliceerd             | Medewerkers kunnen de gepubliceerde planning bekijken, diensten met elkaar ruilen en opmerkingen bekijken die op het niveau Planning zijn ingevoerd. Ze kunnen zich niet inschrijven op diensten.                                                                                      |
| Afgesloten              | Deze status geeft aan dat de planning definitief is. Medewerkers kunnen diensten met elkaar ruilen.                                                                                                           |

## Planningsperioden weergeven

1. Ga naar _Plan > Schedules_{:.breadcrumbs}.
2. Klik op _Planningsperioden_{:.doc-button}.
3. Selecteer een **Eenheid** van het eerste vervolgkeuzemenu. Begin met typen om de lijst te filteren.
4. (Optioneel) Kies in het tweede vervolgkeuzemenu een **Groep** om planningsperioden te filteren. Begin met typen om de lijst te filteren.  
   Als er planningsperioden zijn voor je geselecteerde eenheid (en groep), dan worden deze nu weergegeven. Meer informatie over de tabbladen en tabelkolommen vind je hieronder.

### Tabbladen Lopend en Verlopen

De volgende planningsperioden van de eenheid en/of groep worden weergegeven in de volgende tabbladen:

- **Lopend**: Planningsperioden die gedeeltelijk of geheel in de toekomst liggen.
- **Verlopen**: Planningsperioden die geheel in het verleden liggen.

Als je nog geen planningsperioden hebt aangemaakt, of als geen van de planningsperioden aan de filtercriteria voldoen, dan blijven beide tabbladen leeg.

### Tabelkolommen

De tabel voor planningsperioden bevat zes kolommen:

- **Status**: de status van de planningsperiode
- **Groep**: de groep medewerkers die in de planningsperiode zijn ingepland
- **Geldig vanaf**: de begindatum van de planningsperiode
- **Geldig tot**: de einddatum van de planningsperiode
- **Deadline**: de uiterste datum waarop medewerkers zich op diensten kunnen inschrijven en diensten met elkaar kunnen ruilen
- **Geërfd van**: Wanneer je een planningsperiode aanmaakt voor een superieure eenheid, dan wordt de status voor alle ondergeschikte eenheden overgenomen. De naam van de superieure eenheid wordt alleen in de kolom weergegeven als dat van toepassing is.

Je kunt de lijst sorteren op alle kolommen door op de betreffende **kolomkop** te klikken. Klik nogmaals om de sorteervolgorde om te keren.

## Planningsperioden aanmaken

1. Ga naar _Plan > Schedules_{:.breadcrumbs}.
2. Klik op _Planningsperioden_{:.doc-button}.
3. Klik in de rechterbovenhoek op _Planningsperiode aanmaken_{:.doc-button}.
4. Selecteer een eenheid, een groep, een periode, een deadline (optioneel), en een [status](#status) voor de planningsperiode.
5. Klik op _Opslaan_{:.doc-button} om de planningsperiode op te slaan.

## Planningsperioden bewerken

Om de status van een planningsperiode bij te werken, selecteer je een nieuwe status uit het vervolgkeuzemenu in de kolom **Status**. De nieuwe status wordt automatisch opgeslagen.

Om alle instellingen van een planningsperiode te bewerken (inclusief de status), beweeg je de cursor over een planningsperiode en klik je op het {% icon pencil %} aan de rechterkant.

## Planningsperioden verwijderen

Om één of meer planningsperioden te verwijderen, gebruik je de **selectievakjes** links van de lijstitems. Om alle weergegeven items te selecteren, vink je het bovenste selectievakje aan. Klik op _Selectie verwijderen_{:.doc-button} onder de lijst.
