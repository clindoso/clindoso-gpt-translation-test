---
title: Dagtypes aanmaken en gebruiken
description: Maak dagtypes aan om feestdagen en andere speciale dagen aan te geven, waarop je openingstijden afwijken.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Eenheden aanmaken en beheren
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Create and use planning calendars
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Nationale feestdagen inplannen
    filepath: best-practices/scheduling-public-holidays.md
---

Dagtypes staan voor de dagen met standaard openingstijden en dagen met afwijkende openingstijden.

Voeg dagtypes toe aan je {% link_new eenheid | features/administration/create-and-manage-planning-units.md | #openingstijden-toevoegen %} om openingstijden in te stellen voor de standaarddagen van de week en voor speciale dagen. Als je bedrijf bijvoorbeeld open is op feestdagen, dan houdt injixo op die dagen bij de planningsoptimalisatie rekening met de ingevoerde openingstijden.

In _Plan > Configuratie > Dagtypes_{:.breadcrumbs} kun je:

- de standaard dagtypes bekijken.
- aangepaste dagtypes aanmaken, bewerken en verwijderen.

## Een aangepast dagtype aanmaken

Op sommige dagen wijken je openingstijden mogelijk af van de standaardtijden, bijvoorbeeld bij speciale promoties of feestdagen. Volg deze stappen om voor deze dagen aangepaste dagtypes aan te maken:

1. Klik in de actiebalk op het pictogram Nieuw {% icon item-add | icon-only %}.
2. Voer een **Naam** in (max. 50 tekens).
3. Voer een **Afkorting** in (max. 25 tekens).  
   De afkorting wordt in de planningskalender weergegeven.
4. (Optioneel) Vink het selectievakje **Feestdagmodus** aan.<br>[Lees meer](#feestdagmodus) over hoe je dagtypes voor feestdagen configureert.
5. Klik op _OK_{:.doc-button}.

## Feestdagmodus

 Om een dagtype als feestdag te markeren, vink je het selectievakje **Feestdagmodus** aan in het configuratievenster Dagtype.

### Dagtypes aanmaken voor nationale feestdagen

Je kunt op twee manieren dagtypes voor nationale feestdagen aanmaken:

- Maak dagtypes aan met de feestdagmodus en {% link_new voeg ze toe aan je planningskalender | features/administration/planning-calendar.md | #configure-a-planning-calendar %}.

- Voeg een {% link_new kalendersjabloon | features/administration/planning-calendar.md | #configure-a-planning-calendar %} toe aan je planningskalender. Alle daarin opgenomen dagtypes voor nationale feestdagen worden opgenomen. De feestdagmodus is geactiveerd.

De feestdagmodus past de werktijden van medewerkers op deze dag hierop aan. Als je besluit om de dag als normale werkdag in te plannen, dan kun je de feestdagmodus deactiveren door {% link_new het dagtype te bewerken | features/administration/day-types.md | #een-dagtype-bewerken %}.

## Een dagtype bewerken

> Waarschuwing
>
> Als je de feestdagmodus wijzigt in een dagtype dat op dat moment in gebruik is, dan moet je de tijdaccounts of {% link_new richttijdcontingenten | features/scheduling/planning-periods/target-work-accounts.md %} opnieuw berekenen.
   
1. Selecteer een dagtype uit de lijst.
2. Bewerk de gegevens die je wilt wijzigen.
3. Klik op _OK_{:.doc-button}.

## Een dagtype verwijderen

> Opmerking
> 
> Voordat je een dagtype verwijdert, {% link_new dien je het uit alle planningskalenders | features/administration/planning-calendar.md | #remove-day-types-from-the-planning-calendar %} te verwijderen. Je kunt standaard dagtypes niet verwijderen.

1. Selecteer een dagtype uit de lijst.
2. Klik op het {% icon item-delete %} in de actiebalk.

## Dagtypes in het planningsproces

injixo houdt tijdens het plannen rekening met dagtypes. 
- Als je eenheid regelmatig werkt op een feestdag, dan hoef je alleen maar {% link_new openingstijden aan de eenheid toe te voegen | features/administration/create-and-manage-planning-units.md | #openingstijden-toevoegen %}.  
- Als je eenheid niet werkt op een feestdag, of geopend is met speciale openingstijden, lees dan het artikel {% link_new Nationale feestdagen inplannen | best-practices/scheduling-public-holidays.md %}.
