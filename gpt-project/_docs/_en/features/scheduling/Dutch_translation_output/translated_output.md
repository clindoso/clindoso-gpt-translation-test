---
title: Dienstroosterseries invoegen
description: Plan herhalende reeksen van diensten, activiteiten of beschikbaarheden in met dienstroosterseries (SchedulePro).
promote-service: new-planner-training
product_label:
  - classic
---

Dienstroosterseries zijn vaste, zich herhalende sequenties van diensten, activiteiten of beschikbaarheden. Ze worden gebruikt om regelmatig terugkerende taken of beschikbaarheden van je medewerkers in te plannen. Voordat je deze inplant, dien je {% link_new dienstroosterseries aan te maken | features/administration/shift-sequences.md %} en deze vervolgens {% link_new toe te wijzen aan je medewerkers | features/administration/employee-overview.md | #optionele-inplanningsinstellingen %}.

> Dit artikel gaat over _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Als je injixo Essential WFM, Advanced WFM or Enterprise WFM gebruikt, gebruik je de functie {% link_new Dienstroosterseries invoegen | features/scheduling/capacity/capacity-insert-shift-sequences.md %} in _Plan > Capaciteit_{:.breadcrumbs}.

## Parameters instellen

Met het volgende dialoogvenster _WFM > Scheduling > SchedulePro > Dienstroosterseries invoegen_{:.breadcrumbs} stel je de volgende parameters in:

{{ 1 | image: 'Dienstroosterseries invoegen', '75%' }}

1. **Begin- en einddatum** (max. 2 jaar), een eenheid, eventueel een selectie en een doeldatum kiezen.
2. Bevestig je instellingen met _Medewerkerlijst aanmaken_{:.doc-button}. De [medewerkerlijst](#employee-list) wordt geopend.
3. Selecteer individuele medewerkers met de **selectievakjes voor hun medewerkernummer** of gebruik het eerste selectievakje links bovenaan om alle medewerkers te selecteren.
4. Klik op _Meer opties > Dienstroosterseries invoegen_{:.doc-button}.

De dienstroosterseries zijn ingevoegd. Vervolgens wordt er een bericht weergegeven met gebeurtenis- en documenteermeldingen. 

## Opties

In de sectie _Opties_{:.menu-item} vind je een aantal opties om plancontent te verwijderen:

| Optie                           | Toelichting                                                                                                                                                     |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Diensten en activiteiten verwijderen       | Bestaande diensten en activiteiten in de doeleenheid op de doeldatum worden vervangen door de geselecteerde dienstroosterserie.                       |
| Beschikbaarheid instellen verwijderen      | Bestaande beschikbaarheidsperiodes van medewerkers worden overschreven met de geselecteerde dienstroosterserie.                                                                      |
| alle activiteiten en diensten verwijderen | Bestaande alle activiteiten en diensten van medewerkers in de doeleenheid worden gewist en vervangen door de geselecteerde dienstroosterserie. Beschikbaarheidsperiodes blijven daarbij behouden. |

De opties worden alleen toegepast wanneer voor het eerst een dienstroosterserie voor een medewerker wordt ingevoegd. Als deze optie is geactiveerd, wordt de plancontent alleen gewist wanneer de dienstroosterserie voor het eerst wordt ingevoegd.

Doorgaans worden bestaande diensten en activiteiten in een dienstroosterserie door diensten en activiteiten in deze serie weggelaten als de bestaande items niet het type `Afwezigheid`, `Ziekte`, `Vakantie`, of `Vergadering` zijn. Om ervoor te zorgen dat diensten en activiteiten uit de applicatieplanning werden door diensten en activiteiten in een dienstroosterserie te wissen, dien je de inplanningsregel 2645_Application_liclabel_disallow_overwriting_of_full_day_activities_with_shifts_or_activities_ (\"Activiteiten in het Shift Center mogen niet met diensten of activiteiten worden overschreven\") te activeren.

Andere inplanningsregels kunnen invloed hebben op het resultaat:

- _2602_{:.id-label} _Check maximum duration of each activity as specified in the employee's contract_
- _2611_{:.id-label} _Check employee availability_
- _2613_{:.id-label} _Check maximum number of shifts on one day as specified in the employee's contract_
- _2648_{:.id-label} _Write protection for activities in the Shift Center_

## Medewerkerlijst

In de medewerkerlijst die wordt geopend door op _Medewerkerlijst aanmaken_{:.doc-button} te klikken, wordt informatie weergegeven over elke dienstroosterserie van je medewerkers.

{{ 2 | image: 'Dienstrooster-series van medewerkers' }}

Naast het medewerkernummer en de naam van de medewerker vind je in de medewerkerlijst ook zijn informatie over de dienstroosterserie zelf (naam, looptijd, geldigheid). De informatie over de serie, medewerkerslijn en referentiedatum is afkomstig uit de indiensttreding van de medewerker. Verwijderde series die nog steeds aan medewerkers zijn toegewezen, worden in cursief weergegeven.

### Volgorde van plannen

Wanneer er voor een medewerker meerdere dienstroosterseries worden ingevoegd, worden deze in oplopende volgorde in het plan ingevoerd.
De inhoud van een dienstroosterserie wordt al dan niet door de inhoud van een andere dienstroosterserie vervangen, afhankelijk van de in te voeren gegevens, de bestaande plancontent, de geselecteerde opties en de controle met inplanningsregels.

### Referentiedatum

injixo moet voor elke dag van de week weten of het het patroon voor week 1, week 2, enz. moet gebruiken. De referentiedatum biedt hiervoor een vast punt. De eerste dag van de dienstroosterserie wordt altijd ten opzichte van de referentiedatum ingevoerd. Deze referentiedatum is gedefinieerd tijdens het aan de medewerker toewijzen van een dienstroosterserie en valt altijd op de eerste dag van de week. Controleer indien nodig de instelling _48420_{:.id-label} \"Eerste dag van inplanweek\".

Voorbeeld: De periode waarvoor je een 3-wekelijkse dienstroosterserie wilt plannen, is van 9 juli tot 29 juli. De dienstroosterserie begint op 9 juli, maar de referentiedatum is vastgelegd op 2 juli. Op 9 juli wordt een gebeurtenis ingevoerd, namelijk de achste dag van de dienstroosterserie, omdat deze op 9 juli de eerste dag van week 2 van de serie is. Week 3 van de serie begint op 23 juli.
