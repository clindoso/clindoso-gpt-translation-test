---
title: Dienstruilverzoeken bekijken en goedkeuren
product_label:
  - essential
  - advanced
  - enterprise
description: Bekijk aanvragen voor dienstruilingen en keur ze goed of af, en bekijk eerdere dienstruilingen.
---

In injixo Me kunnen gebruikers met de rol Agent {% link_new hun diensten ruilen | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #diensten-ruilen %} of vrije dagen met elkaar ruilen, zowel op dezelfde dag als op andere dagen.

Diensten ruilen werkt als volgt:

1. Een medewerker biedt in injixo Me een dienst aan.
2. Andere medewerkers kunnen de geplaatste dienst zien en hun eigen dienst te ruil aanbieden.
3. De medewerker die de dienst heeft aangeboden, kiest een teganaanbod uit dat het beste op zijn behoefte aansluit.
4. injixo bevestigt de keuze automatisch en maakt indien van toepassing het goedkeuringsverzoek aan.
5. Een gebruiker met admin-toegang of de rol Planner beoordeelt, en keurt de aangevraagde diensruiling goed of wijst hem af. Om goedkeuringen automatisch te verwerken, wijzig je de instelling _48152_{:.id-label} _Ruilautorisatie_ van 0 naar 1.

Lees het artikel {% link_new Diensten ruilen met je collega's | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #diensten-ruilen %} voor meer informatie over hoe medewerkers diensten kunnen ruilen in injixo Me.

Tip: In de {% link_new Teamkalender | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} kunnen medewerkers de werktijden van hun collega's bekijken en ruilverzoeken indienen.

## Vereisten

Een medewerker met de rol Agent kan een dienst aanbieden, als aan de volgende voorwaarden is voldaan:

- {% link_new Diensten ruilen | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} is in injixo Me geactiveerd.
- Alle activiteiten in een dienst zijn {% link_new ruilbaar met Diensten ruilen | features/administration/activity-types-and-properties.md %}.
- Er bestaat een {% link_new planningsperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} met de status Diensten ruilen is goedgekeurd, Gepubliceerd of Voltooid.
- De ingestelde deadline voor de planningspeiode is nog niet verstreken.
- De waarde die voor de instelling _48151_{:.id-label} is ingesteld staat dienstruilingen. De ingestelde waarde staat voor het aantal dagen vanaf de huidige datum tot wanneer een dienst kan worden geruild zonder dat er een risico ontstaat voor de huidige planning.
- De medewerker heeft toegang tot injixo Me.

## Dienstruilingen goedkeuren of afwijzen

Ga als volgt te werk om dienstruilverzoeken in _Plan > Schedules_{:.breadcrumbs} te bekijken en goed te keuren of af te wijzen:

1. Klik op _Planningsacties_{:.doc-button}.
2. Selecteer **Dienstruilingen goedkeuren**.
3. Kies een **eenheid**.
4. (Optioneel) Kies een **groep**.
5. Selecteer een **datumbereik**. Als je in Schedules nog geen datumbereik hebt geselecteerd, dan wordt het datumbereik standaard op de huidige datum + zeven dagen gezet.
6. Vink de **selectievakjes** naast één of meerdere aanvragen aan die je wilt goedkeuren of afwijzen. Gebruik het selectievakje bovenaan om alle aanvragen in één keer te selecteren.
7. Klik op _Selectie goedkeuren_{:.doc-button} of _Selectie afwijzen_{:.doc-button}.  
   Verzoeken die goedgekeurd of afgewezen zijn worden naar het tabblad Informatie verplaatst.

Het rapport Ruiloverzicht in _WFM > Controle > Rapporten_{:.breadcrumbs} bevat de status van dienstruilingen (zoals _Voorgesteld_, _Onbewerkt_, _Afgewezen_ en _Ingewilligd_) voor een instelbare periode.

## Een lijst met eerdere dienstruilingen aanmaken

Op de pagina **Dienstruilingen goedkeuren** wordt in het tabblad Informatie weergegeven wie wanneer welke dienst heeft geruild. De lijst bevat goedgekeurde, afgewezen en geannuleerde verzoeken. Beweeg je cursor over het informatiepictogram {% icon info_circle | icon-only %} voor meer informatie over geannuleerde verzoeken.

## Instellingen voor diensten ruilen

Onder _WFM > Administratie > Systeem > Instellingen_{:.breadcrumbs} vind je verschillende instellingen waarmee je het proces voor diensten ruilen aan de behoeften van je bedrijf aan kunt passen:

- _48151_{:.id-label} _Blokkade van 'diensten ruilen'_: aantal dagen dat vanaf de huidige datum in de planning geblokkeerd is voor Diensten ruilen (standaardinstelling: 3 dagen).
- _48152_{:.id-label} _Ruilautorisatie_: Stel in of dienstruilingen tussen medewerkers moeten worden goedgekeurd door een gebruiker met admin-toegang of de rol Planner (Standaardwaarde 0 voor goedkeuring. Kies 1 voor automatische dienstruilingen zonder vereiste goedkeuring).
- _48153_{:.id-label} _Ruilmodus_: Dienstruilingen tussen medewerkers binnen één eenheid (waarde 0, standaard), een groep (waarde 1) of verschillende eenheden (waarde 2, niet aanbevolen).
- _48555_{:.id-label} _Ruilen met vrije dagen_: Toestaan dat medewerkers diensten ruilen tegen vrije dagen (standaardwaarde: 0, nee).
- _48556_{:.id-label} _Ruilen tussen verschillende dagen_: Toestaan dat medewerkers diensten ruilen op andere dagen van de week (standaard: 0, nee).
- _48999_{:.id-label} _Specifieke controles voor subactiviteiten van multiactiviteiten activeren in combinatie met planningsregel 2605_: injixo controleert de kwalificaties voor elke deelactiviteit bij het ruilen van multiactiviteiten (standaard: 0, geen controle).

## Wanneer diensten ruilen is geblokkeerd

Medewerkers kunnen diensten die in injixo Me worden aangeboden bekijken en ruilen als het ruilverzoek voldoet aan de regels van hun contract (contractuele werkuren) en als ze over de benodigde kwalificaties beschikken.

Om te zien waarom een dienstruiling in injixo Me niet mogelijk is, kun je het ruilverzoek in het Dienstrooster-Center_{:.menu-item} simuleren. Als je de diensten kopieert, wordt in het {% link_new informatievenster | features/scheduling/shiftcenter/shift-center-overview.md | #message-window %} onder aan de pagina de planningsregel en de reden weergegeven, bijvoorbeeld: onjuiste kwalificaties of andere contractuele beperkingen.
