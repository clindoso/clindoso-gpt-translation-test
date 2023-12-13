---
title: Werken met kwalificaties
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lees hoe kwalificaties in injixo de kwalificaties van je medewerkers weergeven. Kwalificaties en kwalificatieniveaus aanmaken, bewerken en verwijderen.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/configure-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
redirect_from:
  - /nl/skills/
redirect_reason: Updated filename on 24 July 2023
---

Kwalificaties zorgen ervoor dat mensen alleen worden ingepland voor activiteiten waarvoor ze gekwalificeerd zijn. Kwalificaties koppelen de vaardigheden van je medewerkers (bijvoorbeeld productkennis, talen, communicatiekanalen, etc.) aan activiteiten waar zij aan kunnen werken en die je inplant met injixo.

Ga naar _Plan > Configuratie > Kwalificaties_{:.breadcrumbs} om kwalificaties te configureren.

## Kwalificaties aanmaken

Maak voor elke activiteit die een bepaalde vaardigheid vereist minimaal een kwalificatie aan. Als je een kwalificatie aanmaakt, zet injixo het kwalificatieniveau standaard op 100%. Kwalificatieniveaus geven aan hoe bekwaam medewerkers moeten zijn om aan een activiteit te werken, bijvoorbeeld 100% bekwaamheid in de Engelse taal maar slechts 50% bekwaamheid in de Spaanse taal. Je kunt voor een kwalificatie meerdere kwalificatieniveaus aanmaken. 

> Als medewerkers geen specifieke vaardigheden nodig hebben om aan een activiteit te werken, hoef je er geen kwalificatie voor aan te maken.

1. Klik op _Nieuwe kwalificatie_{:.doc-button}.
2. Voer een **Naam** in.
   De afkorting wordt automatisch gegenereerd, maar je kunt deze bewerken.
3. (Optioneel) Klik op _Kwalificatieniveau toevoegen_{:.doc-button} om de standaard **Score** van een kwalificatieniveau te selecteren, of om aanvullende kwalificatieniveaus toe te voegen als je medewerkers hebt die minder ervaren zijn in het uitvoeren van de activiteit. Zie ook: [Bereken de geschiktheid op basis van score en weging](#de-geschiktheid-berekenen-op-basis-van-score-en-weging).
4. Klik op _Kwalificatie aanmaken_{:.doc-button}.  

 Vervolgens kun je een [kwalificatieniveau aan een medewerker toewijzen](#kwalificatieniveaus-aan-een-medewerker-toewijzen) en [kwalificaties aan activiteiten toevoegen](#kwalificaties-aan-activiteiten-toevoegen).

## Kwalificaties kopiëren

Volg deze stappen om een nieuwe kwalificatie aan te maken met dezelfde kwalificatieniveaus als een bestaande kwalificatie.

1. Klik in de lijst met **Kwalificaties** op de kwalificatie die je wilt kopiëren.
2. Klik onder de naam van de kwalificatie op **Kwalificatie kopiëren**.  
   Het venster **Nieuwe kwalificatie aanmaken** met vooraf ingevulde kwalificatieniveaus wordt geopend.
3. Voer een **Naam** in voor de nieuwe kwalificatie.
4. (Optioneel) Bewerk de kwalificatieniveaus.
5. Klik op _Kwalificatie aanmaken_{:.doc-button}.

## Kwalificaties en kwalificatieniveaus bewerken

1. Selecteer een kwalificatie uit de lijst.
2. Bewerk de kwalificatie of kwalificatieniveau(s).
   Om een kwalificatieniveau te verwijderen, klik je op het {% icon trash %} ernaast.
3. Klik op _Wijzigingen opslaan_{:.doc-button}.

## Kwalificaties verwijderen

1. Selecteer een kwalificatie uit de lijst.
2. Klik op _Kwalificatie verwijderen_{:.doc-button} en bevestig je keuze.

## Kwalificaties aan activiteiten toevoegen

1. Ga naar _Plan > Configuratie > Activiteiten_{:.breadcrumbs}.
2. Selecteer een activiteit uit de lijst en scroll naar de sectie **Kwalificaties**.
3. Selecteer een kwalificatie uit het vervolgkeuzemenu.
4. (Optioneel) Wijzig de waarde bij **Weging**. Als je maar een kwalificatie toevoegt, houd dan de standaardwaarde van 100% aan.
   Voor activiteiten die meer dan een kwalificatie nodig hebben, kun je [een weging toekennen](#de-geschiktheid-berekenen-op-basis-van-score-en-weging) om aan te geven welke kwalificatie belangrijker is.
7. Klik op _Wijzigingen opslaan_{:.doc-button}.

## Kwalificatieniveaus aan een medewerker toewijzen

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}.
2. Selecteer een medewerker uit de lijst en ga naar de sectie **Kwalificatieniveaus**.
3. Klik op het {% icon item-add %} en selecteer een of meerdere kwalificatieniveaus uit de lijst.
   Om meerdere items te selecteren, houd je **Shift** of **Ctrl** ingedrukt terwijl je klikt.
4. (Optioneel) Voeg een {% link_new geldigheidsperiode | features/administration/set-a-validity-period.md %} toe aan de kwalificatie door datums **geldig vanaf** en **geldig tot** te selecteren.
   Je kunt niet verschillende kwalificatieniveaus van dezelfde kwalificatie aan een medewerker toewijzen voor dezelfde geldigheidsperiode.
 5. Klik op _OK_{:.doc-button}.  
   De activiteiten waarvoor een of meerdere kwalificaties vereist zijn, verschijnen in de sectie **Activiteiten** van de betreffende medewerker.

Een activiteit kan een of meerdere kwalificaties bevatten. Om aan een activiteit te werken waarvoor meerdere kwalificaties nodig zijn, moeten de toegewezen personen over alle vaardigheden beschikken.

Tip: Om in een keer meerdere kwalificaties aan meerdere medewerkers toe te wijzen, kun je de functionaliteit {% link_new massa-update | features/administration/employee-overview.md | #massa-update-gebruiken %} gebruiken. 

## De geschiktheid berekenen op basis van score en weging

injixo kan een geschiktheidspercentage berekenen op basis van:

- De beoordeling van iemands kwalificatieniveau
- De wegingswaarde wanneer een activiteit meerdere kwalificaties vereist

Voorbeeld: Je hebt een activiteit genaamd "Gesprekken in het Spaans" die twee vaardigheden vereist, Spaans en Gesprekken. De kwalificatie Spaans is twee keer zo belangrijk als de vaardigheid Gesprekken. De wegingswaarden zijn 100 voor Spaans en 50 voor Gesprekken.

- Medewerker 1 heeft de kwalificatieniveaus Spaans 50% en Gesprekken 100%.
- Medewerker 2 heeft de kwalificatieniveaus Spaans 100% en Gesprekken 50%.

Dit resulteert in een geschiktheidspercentage van 66,66% voor medewerker 1 en 83,33% voor medewerker 2.

Het geschiktheidspercentage wordt berekend met deze formule: `(Som(de weging van elke kwalificatie * het kwalificatieniveaupercentage van de medewerker voor de betreffende kwalificatie) / (som van de weging van alle kwalificaties)`

Als een activiteit slechts één vaardigheid vereist, dan is het geschiktheidspercentage gelijk aan het kwalificatieniveau van de medewerker.

Om het geschiktheidspercentage in {% link_new geoptimaliseerde planning | features/scheduling/schedules/schedules-optimized-schedules.md %} weer te geven (in plaats van het aantal medewerkers), dien je de instelling _48069_{:.id-label} _Percentage van kwalificatie voor activiteiten meetellen_ te configureren. In het {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %} en {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %} kunnen de dekking en bezettingsgraad niet worden weergegeven op basis van de geschiktheid van medewerkers. In deze gevallen worden de dekking en bezetting altijd als 100% weergegeven, zodat het aantal medewerkers wordt weergegeven.
