---
title: Contracten aanmaken
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Maak contracten aan om de werktijd per week en overige regels voor je medewerkers vast te leggen.
redirect_from:
  - /nl/contracts-overview/
  - /nl/contract-creation/
redirect_reason: Updated filename on 08 December 2023
---

In _WFM > Administratie > Planning > Contracten_{:.breadcrumbs} kun je de contracten voor de medewerkers invoeren die je wilt inplannen. Je kunt zoveel contracten aanmaken als je wilt. In contracten kun je beperkingen vastleggen waarmee bij het plannen rekening moet worden gehouden.

- Het minimum en maximum aantal werkdagen per week
- Het minimum, nominale en maximum aantal werkuren per dag
- Het minimum, nominale en maximum aantal werkuren per week

Contracten bevatten ook informatie over werktijdenbeleid in je bedrijf, bijvoorbeeld het aantal rustdagen tussen twee diensten. Je kunt ook planningsparameters instellen voor de functionaliteit Geoptimaliseerde planning maken.

## Een contract aanmaken

1. Klik op het {% icon item-add %}.
2. Voer in de sectie **Algemeen** de basisinformatie voor het contract in:<br>
    - Voer een **naam** in (max. 50 tekens).
    - Voer een **afkorting** in (max. 25 tekens).
    - Selecteer een **kleur**.
3. Voer in de sectie **Werkdagen per week** het aantal werkdagen per week in.
4. Selecteer in de sectie **Berekening werkdagen** een berekeningsmethode. <br>
    - Kies je voor **Standaard**, dan wordt de volgorde van de dagen in de planningsweek aangehouden.<br>
    - Kies je voor **Flexibel**, dan worden de werkdagen in de openingstijden van de eenheid vrij gekozen.
5. Voer de [**Richtlijnen voor de werktijd**](#richtlijnen-voor-de-werktijd) en [**Werktijd per dag**](#werktijd-per-dag) in.
6. (Optioneel) Configureer de [**AutoScheduler-parameters**](#autoscheduler-parameters) en **Planningsparameters**.
7. Klik op _OK_{:.doc-button} om je contract op te slaan.

## Richtlijnen voor de werktijd

Richtlijnen voor de minimum, nominale en maximum werktijden zijn essentieel voor het plannen. Richtlijnen voor de werktijd worden gecombineerd met Planningsregels en Instellingen.

### Dag

- **Minimum**: Voer het minimum aantal werkuren per dag in. Als je geen waarde invoert, wordt de nominale tijd als minimum beschouwd. Deze parameter wordt geverifieerd via planningsregel _2615_{:.id-label}.
- **Nominaal**: Voer het nominale aantal werkuren per dag in. We raden aan om een waarde tussen 0 en 24 uur in te voeren en rekening te houden met de standaard werktijden.
- **Maximum**: Voer het maximum aantal werkuren per dag in. Als je geen waarde invoert, wordt de nominale tijd beschouwd als maximum. Deze parameter wordt geverifieerd via planningsregel _2614_{:.id-label}.

### Week

- **Minimum**: Voer het minimum aantal werkuren per week in. Je kunt het begin van de planningsweek met de instelling _48420_{:.id-label} instellen. Je kunt het aantal dagen in het weekend instellen met de instelling _48421_{:.id-label}.
- **Nominaal**: Voer het nominale aantal werkuren per dag in. Deze waarde is vereist als je geen waarden invoert bij Werktijd per dag. Je kunt het begin van de planningsweek met de instelling _48420_{:.id-label} instellen.
- **Maximum**: Voer het maximum aantal werkuren per dag in. Deze parameter wordt geverifieerd door de planningsregels _2618_{:.id-label} en _2629_{:.id-label}. 

### Maand

- **Maximum**: Voer het maximum aantal werkuren per maand in. Deze parameter wordt geverifieerd via de planningsregel _2619_{:.id-label}.


## Werktijd per dag

Je kunt het aantal werkuren per dag vastleggen voor medewerkers met dit contract. Als de Richtlijnen voor de werktijd zijn geconfigureerd, dan hoef je hier geen waarden in te voeren. Het is echter wel handig om bepaalde afwezigheid te berekenen, zoals vakantie of ziekte.

Voorbeeld:
Een medewerker heeft op vrijdag betaald verlof. In het contract wordt voor vrijdagen 8 uur aangegeven. Voor die dag worden er dus 8 werkuren geteld.

Voer het maximum aantal werkuren per dag in. Voer voor niet-werkdagen 0:00 uur in. Als je een veld leeg laat, dan wordt standaard de volgende formule gebruikt: [Aantal nominale uren/aantal werkdagen]. Dit kan leiden tot een onjuiste berekening.

## AutoScheduler-parameters

- **Max. aantal op elkaar volgende werkdagen**: Voer het maximum aantal op elkaar volgende werkdagen in waarmee de functionaliteit Geoptimaliseerde planning maken rekening moet houden. Hoeft niet te worden ingevuld voor eenheden zonder openingstijden tijdens het weekend. Als een medewerker bijvoorbeeld 5 dagen per week werkt, gebruik dan deze parameter om te voorkomen dat deze 10 dagen achter elkaar werkt.
- **Min. aantal vrije dagen per week**: Voer het minimum aantal dagen in waarmee de functionaliteit Geoptimaliseerde planning maken tijdens elke planningsweek rekening moet houden. Hoeft niet te worden ingevuld voor eenheden zonder openingstijden tijdens het weekend.
- **Min. aantal op elkaar volgende vrije dagen per week**: Voer het minimum aantal dagen in waarmee de functionaliteit Geoptimaliseerde planning maken tijdens elke planningsweek rekening moet houden.
- **Max. aantal op elkaar volgende vrije dagen**: Voer het maximaal aantal op elkaar volgende vrije dagen in waarmee de functionaliteit Geoptimaliseerde planning maken rekening moet houden. De waarde wordt niet per week, maar over meerdere weken berekend.
- **Min. rusttijd (uren) tussen twee diensten**: Voer de minimale rusttijd in waarmee de functionaliteit Geoptimaliseerde planning maken rekening moet houden tussen twee op elkaar volgende diensten.	
- **Minimumaantal werkdagen per week**: Voer het minimum aantal werkdagen in dat per planningsweek moet worden ingepland.
- **Richttijdcontingent i.p.v. contractuele richttijd/week**: Vink dit selectievakje aan als je de waarden van berekende richttijdcontingenten in de functionaliteit Geoptimaliseerde planning maken wilt gebruiken. Lees meer over {% link_new richttijdcontingenten | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Max. een werkdag op zaterdag eens per n weken**: Voer het maximum aantal weken (1-5) tijdens welke een medewerker op zaterdag kan werken. De waarde 2 staat bijvoorbeeld voor elke tweede zaterdag.
- **Werkdag toewijzen na een hele vakantiedag**: Verplicht de functionaliteit Geoptimaliseerde planning maken om na een volledige verlofdag een werkdag in te plannen. Als de medewerker meerdere dagen na elkaar vrij heeft, dan wordt de werkdag na de laatste verlofdag ingepland.
