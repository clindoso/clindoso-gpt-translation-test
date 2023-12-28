---
title: Dienstenruilverzoeken bekijken en goedkeuren
product_label:
  - essential
  - advanced
  - enterprise
description: Bekijk en keur ruil- en/of aanvraagdiensten goed en bekijk eerdere ruilingen.
archive_ref: 20210802-en-shift-exchange-overview
---

In injixo Me kunnen gebruikers met de rol agent {% link_new hun diensten | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #diensten-ruilen %} of hun vrije dagen met elkaar ruilen, zowel op dezelfde dag als op verschillende dagen.

Ruildiensten werkt als volgt:

1. Iemand biedt in injixo Me een dienst aan.
2. Anderen kunnen de geplaatste dienst zien en hun eigen dienst ter ruil aanbieden.
3. De persoon die de dienst heeft aangeboden, kiest een dienst ter ruil die het beste op hun behoefte aansluit.
4. injixo bevestigt de keuze automatisch en maakt zo nodig het goedkeuringsverzoek aan.
5. Een gebruiker met admintoegang of de rol planner controleert, keurt goed of wijst de geruilde dienst af. Om goedkeuringen automatisch te verwerken, wijzig je de instelling _48152_{:.id-label} _Ruilmodus_ van 0 in 1.

Voor meer informatie kun je je lezen in {% link_new Diensten ruilen met je collega's | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #diensten-ruilen %}.

Tip: In de {% link_new Teamkalender | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} kunnen mensen de werktijden van hun collega's bekijken en ruilverzoeken aanvragen.

## Vereisten

Een medewerker met de rol agent kunnen een dienst aanbieden, als aan de volgende voorwaarden is voldaan:

-  {% link_new Diensten ruilen | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} is in injixo Me geactiveerd.
-  alle activiteiten in een dienst zijn {% link_new ruilbaar met dienstenruil | features/administration/activity-types-and-properties.md %}.
-  er een {% link_new planningsperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} bestaat die de status Dienstruil is goedgekeurd, Gepubliceerd of Voltooid heeft.
-  in de geconfigureerde uiterste datum voor de planningspeiode dat nog niet is verstreken.
-  de waarde die in de instelling _48151_{:.id-label} is gedefinieerd voor dienstenruil. Met de waarde wordt het aantal dagen tot de huidige datum aangegeven waarbinnen een dienstenruil zonder risico's in het huidige plan mogelijk is.
-  ze toegang met de rol agent hebben tot injixo Me.

## Ruildiensten goedkeuren of afwijzen

Ga in _Plan > Dienstroosters_{:.breadcrumbs} als volgt te werk om ruildiensten te bekijken en goedkeuren of af te wijzen:

1. Klik op _Planningsacties_{:.doc-button}.
2. Selecteer **Ruildiensten goedkeuren**.
3. Selecteer een **eenheid**.
4. (Optioneel) Selecteer een **selectie**.
5. Selecteer een **datumreeks**. Als je in Dienstroosters nog geen datumreeks hebt geselecteerd, dan is de standaardwaarde Vandaag + zeven dagen.
6. Vink het vakje aan naast één of meerdere items die je wilt goedkeuren of afwijzen. Gebruik het vakje bovenaan om alle items in één keer te selecteren.
7. Klik op _Geselecteerde goedkeuren_{:.doc-button} of _Geselecteerde afwijzen_{:.doc-button}.  
   Verzoeken die goedgekeurd of afgewezen zijn worden naar het tabblad Informatie verplaatst.

Het rapport Ruilstatistieken in _WFM > Monitoring > Rapporten_{:.breadcrumbs} bevat de status van geruilde diensten (als Aangeboden, Geen wijzigingen, Afgewezen en Goedgekeurd) voor een instelbare periode.

## Een lijst met eerdere ruildiensten aanmaken

Op de pagina **Ruildiensten goedkeuren** tabblad Informatie wordt weergegeven wie welke dienst heeft geruild en op welke tijd. De lijst bevat goedgekeurde, afgewezen en geannuleerde verzoeken. Houd de muis boven het {% icon info_circle %}. voor meer informatie over geannuleerde verzoeken.

## Instellingen voor dienstenruil

Onder _WFM > Admin > Systeem > Instellingen_{:.breadcrumbs} bevinden zich verschillende instellingen zodat het proces dienstenruil aan de wensen van je bedrijf aan te passen:

- _48151_{:.id-label} _Geblokkeerde periode voor ruildiensten_: Aantal dagen vanaf de huidige datum totdat een ruil niet langer mogelijk is (standaard: 3 dagen).
- _48152_{:.id-label} _Ruilmodus_: Stel in of een gebruiker met admin-toegang of de rol planner ruildiensten goedkeurt tussen mensen (Standaard 0 voor goedkeuring. Kies 1 voor automatische ruilen zonder goedkeuring).
- _48153_{:.id-label} _Ruilrecht_: Ruilen tussen mensen binnen één eenheid (waarde 0, standaard), een selectie (waarde 1) of verschillende eenheden (waarde 2, niet aanbevolen).
- _48555_{:.id-label} _Ruildiensten af tegen VD_: Toestaan dat medewerkers diensten ruilen tegen vrije dagen (standaard: 0, nee).
- _48556_{:.id-label} _Ruildiensten af op verschillende dagen_: Toestaan dat medewerkers diensten ruilen op andere dagen van de week (standaard: 0, nee).
- _48999_{:.id-label} _Specifieke instructie aanzetten bij handelingen van subactiviteiten bij meerdere handelingen in combinatie met planningsregel 2605._: injixo controleert de vaardigheid voor elke subactiviteit bij het ruilen van diensten (standaard: 0, geen controle).

## Wanneer je diensten ruilt blokkeert

Medewerkers kunnen aangeboden en geruilde diensten inzien en ruilen in injixo Me als het ruilverzoek voldoet aan de regels van hun contract (contracturen) en als ze over de benodigde vaardigheden beschikken.

Voor meer informatie over waarom het ruilen wordt voorkomen in injixo Me, raadpleeg je het ruilverzoek in het Dienstencentrum_{:.menu-item}. Wanneer je de diensten kopieert en plakt, wordt in het {% link_new informatievenster | features/scheduling/shiftcenter/shift-center-overview.md | #info-window %} onder aan de pagina de {% link_new planningsregel | features/administration/create-contracts.md | #planningsregels %} en de reden weergegeven, zoals foute compétence ou autres contraintes contractuelles(Onjuiste competentie of andere contractuele beperkingen).
