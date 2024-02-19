---
title: Dienstenseries toevoegen
product_label:
  - essential
  - advanced
  - enterprise
description: In Schedules kun je dienstenseries gebruiken om zich herhalende roulaties van diensten, activiteiten of beschikbaarheden in te plannen.
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
---

Dienstenseries zijn vaste, zich herhalende series van diensten, activiteiten of beschikbaarheden. Je kunt dienstenseries toevoegen voor geselecteerde medewerkers, bijvoorbeeld om regelmatig terugkerende taken of beschikbaarheden in te plannen.

## Vereisten

Voordat je dienstenseries aan je planning kunt toevoegen, moet je het volgende doen:

- {% link_new Maak | features/administration/shift-sequences.md %} minimaal een dienstenserie aan.
- {% link_new Wijs | features/administration/employee-overview.md | #een-dienstenserie-toewijzen %} de dienstenserie(s) toe aan een medewerker.

## Dienstenseries filteren

1. Ga naar _Plan > Schedules_{:.breadcrumbs}.
2. Selecteer in het vervolgkeuzemenu **Planningsacties** aan de rechterkant _Dienstenseries toevoegen_{:.doc-button}.
3. Selecteer een eenheid.
4. (Optioneel) Selecteer een groep.
5. Stel een periode in.

   > Je kunt dienstenseries toevoegen voor maximaal twee jaar.

   In de sectie **Overzicht** worden dienstenseries weergegeven die overeenkomen met je filter. In de tabel worden gegevens weergegeven die worden ingesteld als je een bestaande dienstenserie aan een medewerker toewijst.

   | Optie                 | Beschrijving                                                                                                                                                                                                                                                                       |
   | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
   | Personeelsnummer       | De unieke ID van de medewerker                                                                                                                                                                                                                                               |
   | Naam                   | De naam van de medewerker aan wie de dienstenserie is toegewezen                                                                                                                                                                                                                                                                 |
   | Dienstenserie         | De naam van de toegewezen dienstenserie                                                                                                                                                                                                                                                    |
   | Volgorde               | Bepaalt de volgorde waarin dienstenseries worden toegevoegd als een medewerker meerdere dienstenseries heeft. Dienstenseries met lagere waarden worden als eerste toegevoegd en kunnen door volgende dienstenseries worden overschreven.                                                                  |
   | Medewerkersregel           | Bepaalt welke regel van de dienstenserie voor de medewerker wordt gebruikt.                                                                                                                                                                                                               |
   | Referentiedatum         | Beginpunt van de dienstenserie.  |
   | Geldig vanaf<br>Geldig tot | De periode waarvoor de dienstenserie aan de medewerker is toegewezen. Buiten de geconfigureerde geldigheidsperiode wordt de dienstenserie niet aan de planning van de medewerker toegevoegd. Als de geldigheidsperiode van de dienstenserie volledig binnen de geselecteerde periode valt, dan wordt de dienstenserie niet weergegeven. |

## Dienstenseries toevoegen

1. Vink het selectievakje naast de regel van een medewerker aan om deze te selecteren. Vink het selectievakje in de kopregel aan om alle medewerkers te selecteren.
2. (Optioneel) Selecteer in het vervolgkeuzemenu **Opties** onder de overzichtstabel wat er met bestaande planningen moet gebeuren als je dienstenseries toevoegt.

   | Optie                           | Beschrijving                                                                                             |
   | -------------------------------- | --------------------------------------------------------------------------------------------------- |
   | Alle activiteiten en diensten verwijderen | Alle activiteiten en diensten worden uit het doelniveau verwijderd. Beschikbaarheidsperioden blijven behouden. |
   | Activiteiten over de hele dag verwijderen       | Activiteiten over de hele dag worden verwijderd. Activitieten die niet een hele dag beslaan, blijven behouden.                              |
   | Beschikbaarheidsperioden verwijderen      | Beschikbaarheidsperioden worden verwijderd.                                                                   |

   <!-- {{ 2 | image: 'Options', '40%' }} -->

   > De geselecteerde opties worden alleen toegepast bij het toevoegen van de eerste dienstenserie voor de medewerker.

3. (Optioneel) Wijzig het doelniveau. Standaard is het niveau Planning geselecteerd.
4. Klik op _Dienstenseries toevoegen_{:.doc-button}.

> Opmerking  
>  
> Als verwijderde dagmodellen nog steeds in een dienstenserie aanwezig zijn, dan worden ze alsnog aan de planning toegevoegd (in Schedules en het Dienstrooster-Center voorzien van een kader van stippellijnen).

## Resultaatrapporten bekijken

In de sectie **Invoeggeschiedenis** vind je rapporten voor de huidig een vorige sessies waarbij je dienstenseries hebt toegevoegd. Als je naast een sessie op de link **Details bekijken** klikt, dan wordt er een rapport geopend waarin een succesmelding of eventuele opgetreden problemen worden weergegeven. Het rapport geeft ook nummers van planningsregels weer en de reden waarom diensten of activiteiten niet konden worden toegevoegd.

Je kunt sessies uit de sectie **Invoeggeschiedenis** verwijderen door de selectievakjes naast een sessie aan te vinken of door het selectievakje bovenaan te gebruiken om alles te selecteren en vervolgens op _Invoer verwijderen_{:.doc-button} te klikken.


## Omgang met bestaande planningen

Een activiteit over de hele dag in een dienstenserie (bijvoorbeeld Ziekte) vervangt standaard een activiteit over de hele dag in de planning (bijvoorbeeld Vakantie).

Als gevolg kunnen activiteiten over de hele dag en andere activiteiten die een dagdeel beslaan worden overschreven door kortere activiteiten en dagmodellen. Om dit voor Activiteiten over de hele dag te voorkomen, activeer je planningsregel _2645_{:.id-label}. Voor overige activiteiten die een dagdeel beslaan van het type, Ziekte, Vakantie of Vergadering, activeer je planningsregel _2648_{:.id-label}.

## Geldigheidsperiodes

Als je dienstenseries toevoegt, kunnen geldigheidsperioden invloed hebben op de resultaten.

Om de periode te bepalen waarin een dagmodel kan worden ingepland, kun je de geldigheidsperiode van je dagmodellen beperken door een Geldig van- en Geldig tot-datum in te stellen. Nadat je dienstenseries hebt toegevoegd, kan in het resultatenrapport de volgende foutmelding worden weergegeven: [2151] De dagmodellen voor de dienst 'naam van dagmodel' zijn ongeldig voor de boekingsdag dd/mm/yyyy.

In elke dienstenserie kun je een periode instellen waarin de dienstenserie kan worden toegevoegd. Standaard zijn dienstenseries altijd geldig. Als je de periode beperkt, wordt de dienstenserie niet buiten de ingestelde periode toegevoegd. In dat geval krijg je geen foutmelding te zien.

Geldigheidsperioden in persoonlijke dagmodellen (dagmodellen die aan medewerkers zijn toegewezen) hebben geen invleod op dienstenseries. Deze dagmodellen in dienstenseries worden gewoon toegevoegd.

Opmerking: Verwijderde dagmodellen die nog steeds deel uitmaken van een dienstenserie worden toegevoegd en in het Dienstrooster-Center en in Schedules voorzien van een kader van stippellijnen. In dat geval krijg je geen foutmelding te zien.
