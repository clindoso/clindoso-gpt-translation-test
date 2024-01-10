---
title: Wat zijn planningsperioden?
description: Ontdek voor welke doeleinden planningsperioden worden gebruikt en hoe je ze kunt weergeven, bewerken en verwijderen (Schedules).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
---

Planningsperioden beslaan een tijdvak van een aantal dagen, weken of maanden. Je hebt planningsperioden nodig als je:

- medewerkers de mogelijkheid wilt geven om {% link_new hun dienstrooster te bekijken | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %}.
- medewerkers de mogelijkheid wilt geven om {% link_new diensten met elkaar te ruilen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.
- medewerkers de mogelijkheid wilt geven om {% link_new op diensten te bieden | features/scheduling/schedules/schedules-shift-bidding.md %}.

Gebruik {% link_new verlofperioden | features/scheduling/time-off/time-off-periods.md %} als je medewerkers met verlof willen laten gaan.

## Status

Iedere planningsperiode heeft een status. Deze status geeft medewerkers voor het gehele tijdvak van de planningsperiode toegang tot bepaalde opties of beperkt de toegang hiertoe. Over het algemeen wijzig je de status van een planningsperiode meerdere keren voor, tijdens en na het planningsproces, bijvoorbeeld nadat je het rooster hebt voltooid of wanneer de periode voor het indienen van dienstverzoeken is verstreken.

| Status                | Toelichting                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Niet gepubliceerd           | Medewerkers kunnen het gepubliceerde dienstrooster niet bekijken, kunnen niet {% link_new op diensten bieden en geen diensten met elkaar ruilen                                                                                                                 | features/scheduling/schedules/schedules-shift-bidding.md %}. Gebruik deze status als je het dienstrooster nog niet met je medewerkers wilt delen. |
| Dienstverzoeken toegestaan | Medewerkers kunnen het gepubliceerde dienstrooster bekijken, meebieden op diensten, diensten met elkaar ruilen, en {% link_new opmerkingen | features/scheduling/shiftcenter/add-and-delete-items.md | #opmerkingen-toevoegen %} zien die op Plan-niveau zijn ingevoerd. Deze status kan niet worden toegekend als de planningsperiode een einddatum heeft die al is verstreken. |
| Gepubliceerd             | Medewerkers kunnen het gepubliceerde dienstrooster bekijken, diensten met elkaar ruilen  en opmerkingen zien, die op Plan-niveau zijn ingevoerd. Ze kunnen niet meebieden op diensten.                                                                                      |
| Voltooid              | Deze status betekent dat het rooster klaar is. Medewerkers kunnen diensten met elkaar ruilen.                                                                                                           |

## Weergave van planningsperioden

1. Ga naar _Plan > Schedules_{:.breadcrumbs}.
2. Klik op _Planningsperioden_{:.doc-button}.
3. Selecteer een **Eenheid** van het eerste keuzemenu. Begin met typen om de lijst te filteren.
4. (Optioneel) Kies in het tweede keuzemenu een **Selectie** om planningsperioden te filteren. Begin met typen om de lijst te filteren.  
   Als er planningsperioden zijn voor je geselecteerde eenheid (en selectie), dan worden deze nu getoond.  Meer informatie over de tabs en tabelkolommen vind je hieronder.

### Tabbladen Actueel en Verlopen

De volgende planningsperiodes van de eenheid en/of selectie worden weergegeven in de volgende tabs:

- **Actueel**: Planningsperiodes die gedeeltelijk of geheel in de toekomst liggen.
- **Verlopen**: Planningsperiodes die geheel in het verleden liggen.

Zelfs als je nog geen planningsperioden hebt aangemaakt, of als de filtercriteria niet voor bestaande planningsperioden gelden, dan zullen beide tabs leeg zijn.

### Tabelkolommen

De tabel met planningsperioden bevat zes kolommen:

- **Status**: de status van de planningsperiode
- **Selectie**: medewerkers die door de planningsperiode worden beïnvloed
- **Geldig vanaf**: het aanvangstijdstip van de planningsperiode
- **Geldig tot**: het eindtijdstip van de planningsperiode
- **Einddatum**: de uiterste datum waarop medewerkers mogen meebieden op diensten  en diensten met elkaar mogen ruilen
- **Geërfd van**: Wanneer je een planningsperiode aanmaakt voor een ouderentiteit, dan wordt de status voor alle subeenheden overgenomen. Er wordt alleen een naam van de ouderentiteit getoond als dit van toepassing is.

Je kunt de lijst sorteren op alle kolommen, door op de desbetreffende **kolomkop** te klikken. Klik nogmaals om de sorteervolgorde om te keren.

## Planningsperioden aanmaken

1. Ga naar _Plan > Schedules_{:.breadcrumbs}.
2. Klik op _Planningsperioden_{:.doc-button}.
3. Klik in de rechterbovenhoek op _Planningsperiode aanmaken_{:.doc-button}.
4. Selecteer een eenheid, een selectie, een periode, een einddatum (optioneel), en een status {[status](#status)} voor de planningsperiode.
5. Klik op _Opslaan_{:.doc-button} om de planningsperiode op te slaan.

## Planningsperioden bewerken

Selecteer voor een nieuwe status uit het keuzemenu in de kolom **Status**. De nieuwe status wordt automatisch opgeslagen.

Ga met je muis over een planningsperiode heen, klik op het {% icon pencil %} aan de rechterkant om alle instellingen van een planningsperiode en te bewerken (inclusief de status).

## Planningsperioden verwijderen

Om één of meer planningsperioden te verwijderen, dien je de **selectievakjes** links van de lijstitems aan te vinken. Het selectievakje bovenaan vinkt alle weergegeven items aan. Klik hieronder op de lijst op _Geselecteerde items verwijderen_{:.doc-button}.