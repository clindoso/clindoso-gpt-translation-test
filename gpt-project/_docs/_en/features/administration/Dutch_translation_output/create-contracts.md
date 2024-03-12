---
title: Contracten aanmaken <!-- TM 100 -->
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Maak contracten aan om de werktijd per week en overige regels voor je medewerkers vast te leggen. <!-- TM 100 -->
redirect_from:
  - /contracts-overview/
  - /contract-creation/
redirect_reason: Updated filename on 08 December 2023
---

In _Plan > Configuratie > Contracten_{:.breadcrumbs} kun je contracten voor de medewerkers invoeren die je wilt inplannen. Je kunt zoveel contracten aanmaken als je wilt. Met contracten kun je beperkingen vastleggen waar bij het plannen rekening gehouden moet worden. <!-- TM 100 -->

- Het minimum en maximum aantal werkdagen per week <!-- TM 100 -->
- Het minimale, nominale en maximale aantal werkuren per dag <!-- TM 100 -->
- Het minimale, nominale en maximale aantal werkuren per week <!-- TM 100 -->
- Het maximaal aantal werkuren per maand <!-- TM 100 -->

Contracten bevatten ook informatie over werktijdenbeleid in je bedrijf, bijvoorbeeld het aantal rustdagen tussen diensten. Je kunt ook planningsparameters instellen voor de functionaliteit **Geoptimaliseerde planning maken**. <!-- TM 100 -->

## Een contract aanmaken <!-- TM 100 -->

Ga naar _Plan > Configuratie > Contracten_{:.breadcrumbs} en volg deze stappen om een nieuw contract aan te maken: <!-- TM 100 -->

1. Klik op het {% icon item-add %} linksboven. <!-- TM 100 -->
2. Voer in de sectie **Algemeen** de basisinformatie voor het contract in:<br> <!-- TM 100 -->
    - **Naam**: Voer een unieke naam in (max. 50 tekens). <!-- TM 100 -->
    - **Afkorting**: Voer de naam in of een kortere versie hiervan (max. 25 tekens). <!-- TM 100 -->
    - **Kleur**: Aan de hand van de kleur kun je het contract eenvoudig vinden. <!-- TM 100 -->
3. Voer in de sectie **Werkdagen per week** het aantal werkdagen per week in. <!-- TM 100 -->
4. Selecteer in de sectie **Berekening werkdagen** een berekeningsmethode. <br> <!-- TM 100 -->
    - Kies je voor **Standaard**, dan wordt de volgorde van de dagen in de planningsweek aangehouden.<br> <!-- TM 100 -->
    - Kies je voor **Flexibel**, dan worden de werkdagen in de openingstijden van de eenheid vrij gekozen. <!-- TM 100 -->
5. Voer de [**Richtlijnen voor de werktijd**](#richtlijnen-voor-de-werktijd) en [**Werktijd per dag**](#werktijd-per-dag). <!-- TM 100 -->
6. (Optioneel) Configureer de [**AutoScheduler-parameters**](#autoscheduler-parameters) of de [**Planningsparameters**](#planningsregels). <!-- TM 100 -->
7. Klik op _OK_{:.doc-button} om je contract op te slaan. <!-- TM 100 -->

## Richtlijnen voor de werktijd <!-- TM 100 -->

Richtlijnen voor de minimum, nominale en maximum werktijden zijn essentieel voor het plannen. Richtlijnen voor de werktijd worden gecombineerd met de plannings- en AutoScheduler-parameters. <!-- TM 100 -->

### Dag <!-- TM 100 -->

- **Minimum**: Voer het minimum aantal werkuren per dag in. Als je geen waarde invoert, wordt de nominale tijd als minimum beschouwd. Deze parameter wordt geverifieerd via de planningsparameter _2615_{:.id-label}. <!-- TM 100 -->
- **Nominaal**: Voer het nominale aantal werkuren per dag in. Voer een waarde tussen 0 en 24 uur in en houd daarbij rekening met de standaard werktijden. <!-- TM 100 -->
- **Maximum**: Voer het maximum aantal werkuren per dag in. Als je geen waarde invoert, wordt de nominale tijd beschouwd als maximum. Deze parameter wordt geverifieerd via de planningsparameter _2614_{:.id-label}. <!-- TM 100 -->

### Week <!-- TM 100 -->

- **Minimale weekduur**: Voer het minimale aantal werkuren per week in. Gebruikers met admin-toegang kunnen het begin van de werkweek instellen in _Account > Systeeminstellingen_{:.breadcrumbs} via het vervolgkeuzemenu **Start van de week**. Je kunt het aantal weekenddagen instellen in Configuratie-instelling _48421_{:.id-label}. <!-- GPT translation -->
- **Planningsrichtlijn**: Voer het aanbevolen aantal werkuren per week in. Deze waarde is verplicht als je geen waarden invoert in het veld **Werkuren voor elke dag van de week**. <!-- GPT translation -->
- **Maximum**: Voer het maximum aantal werkuren per week in. Deze parameter wordt geverifieerd door de planningsparameters _2618_{:.id-label} en _2629_{:.id-label}. <!-- GPT translation -->

### Maand <!-- TM 100 -->

- **Maximum**: Voer het maximum aantal werkuren per maand in. Deze parameter wordt geverifieerd via de planningsparameter _2619_{:.id-label}. <!-- TM 100 -->


## Werktijd per dag <!-- TM 100 -->

Je kunt het aantal werkuren per dag vastleggen voor medewerkers met dit contract. Bij de configuratie van de **richtlijnen voor de werktijd** is deze sectie optioneel. injixo kan deze informatie echter gebruiken om betaalde afwezigheid, zoals vakantie of ziekte te berekenen. <!-- TM 100 -->

Voorbeeld: <!-- TM 100 -->
Een medewerker werkt 40 uur per week en 8 uur per dag en is op woensdag en zondag vrij. Om ervoor te zorgen dat de werkuren gelijkmatig over de week worden verdeeld, voer je in de velden voor Maandag, Dinsdag, Donderdag, Vrijdag en Zaterdag 8:00 in, en in de velden voor Woensdag en Zondag 0:00. Als een medewerker zich ziek meldt of betaald verlof neemt, dan worden de werkuren nog steeds op basis van de hier ingevoerde uren berekend. <!-- TM 100 -->

Als je een veld leeg laat, dan wordt standaard de volgende formule gebruikt: [Aantal nominale uren per week/aantal werkdagen]. Dit leidt mogelijk tot miscalculaties, omdat injixo uitgaat van een gelijkmatige verdeling van werkuren over alle werkdagen. <!-- TM 100 -->

## AutoScheduler-parameters <!-- TM 100 -->


- **Max. aantal op elkaar volgende werkdagen**: Vul dit veld in als je eenheid 7/7 dagen geopend is. Voer het maximaal aantal op elkaar volgende vrije dagen in waarmee **Geoptimaliseerde planning maken** rekening moet houden. Als een medewerker bijvoorbeeld 5 dagen per week werkt, gebruik dan deze parameter om te voorkomen dat deze 10 dagen achter elkaar werkt. <!-- TM 100 -->
- **Min. aantal vrije dagen per week**: Vul dit veld in als je eenheid in de weekenden geopend is. Voer het maximaal aantal op elkaar volgende niet-werkdagen in waarmee **Geoptimaliseerde planning maken** tijdens elke planningsweek rekening moet houden. <!-- TM 100 -->
- **Min. aantal op elkaar volgende vrije dagen per week**: Vul dit veld in als je wilt garanderen dat je medewerkers elke week minimaal een periode met opeenvolgende vrije dagen heeft. Voer het minimaal aantal opeenvolgende niet-werkdagen per week in, dat de functionaliteit **Geoptimaliseerde planning maken** elke week in acht moet nemen. <!-- TM 100 -->
- **Max. op elkaar volgende vrije dagen**: Vul dit veld in als je het aantal opeenvolgende vrije dagen voor je medewerkers wilt beperken om een consistente bezetting te garanderen en lange pauzes te vermijden. Voer het maximaal aantal op elkaar volgende vrije dagen in waarmee de functionaliteit **Geoptimaliseerde planning maken** rekening moet houden. De waarde wordt niet per week, maar over meerdere weken berekend. <!-- TM 100 -->
- **Minimale rusttijd tussen twee diensten (in uren)**: Voer hier een waarde in als je aan arbeidswetten betreffende rusttijden tussen diensten moet voldoen. Voer de minimale rusttijd in waar rekening mee moet worden gehouden tussen twee op eikaar volgende diensten. <!-- GPT translation -->
- **Minimumaantal werkdagen per week**: Vul dit veld in om wekelijks een minimaal bezettingsniveau in je eenheid te behouden, om ervoor te zorgen dat er altijd genoeg medewerkers zijn om een onverwacht hoog oproepvolume te verwerken. Voer het minimaal aantal werkdagen in dat per planningsweek moet worden ingepland. <!-- TM 100 -->
- **Richttijdcontingent i.p.v. contractuele richttijd/week**: Vink dit selectievakje aan als je de waarden van berekende richttijdcontingenten in de functionaliteit **Geoptimaliseerde planning maken** maken wilt gebruiken. Lees meer over {% link_new richttijdcontingenten | features/scheduling/planning-periods/target-work-accounts.md %}. <!-- TM 100 -->
- **Max. een werkdag op zaterdag eens per n weken**: Vul dit veld in als je een eerlijke verdeling van weekendwerk onder je medewerkers wilt garanderen en wilt voorkomen dat dezelfde mensen consequent op zaterdag werken. Voer het maximum aantal weken (1-5) in tijdens welke een medewerker op zaterdag kan werken. De waarde 2 staat bijvoorbeeld voor elke tweede zaterdag. <!-- TM 100 -->
- **Werkdag toewijzen na een hele vakantiedag**: Vul dit veld in als je de functionaliteit **Geoptimaliseerde planning maken** wilt dwingen om een werkdag in te plannen na een volledige verlofdag. Als de medewerker meerdere dagen na elkaar vrij heeft, dan wordt de werkdag na de laatste verlofdag ingepland. <!-- TM 100 -->

## Planningsregels <!-- TM 100 -->

Planningsregels bepalen algemene en contractgerelateerde regels voor je planningsproces. In de contractconfiguratie worden planningsregels planningsparameters genoemd. <!-- TM 100 -->

Ga naar _WFM > Administratie > Systeem > Planningsregels_{:.breadcrumbs}. Klik op een regel in de lijst om een beschrijving van de betreffende regel te bekijken. Planningsregels worden meestal geconfigureerd tijdens de onboarding met je injixo-consultant. <!-- TM 100 -->

Gebruikers met admintoegang kunnen elke regel bewerken, uitzonderingen instellen en zelfs gebruikerspecifieke waarden of standaardwaarden terugzetten. <!-- TM 100 -->

> Potential risk of scheduling errors
>
> Changes to scheduling rules are complex and can result in scheduling errors if done incorrectly. Do not change them yourself if you are not sure about the consequences. If you need to change a scheduling rule, contact your consultant.

Contractspecifieke planningsregels zorgen ervoor dat de voorwaarden van elk contract worden meegenomen bij het plannen. Als een contract bijvoorbeeld een bepaalde rustperiode met een bepaalde lengte of een maximaal aantal werkuren per dag voorschrijft, dan zorgen de planningsregels ervoor dat aan deze voorwaarden wordt voldaan. Het overtreden van deze regels kan leiden tot planningsconflicten, ontevredenheid onder medewerkers en mogelijke contractovertredingen. <!-- TM 100 -->

### Statusindicator <!-- TM 100 -->

In de lijst kun je de status van elke planningsregel bekijken: <!-- TM 100 -->

  - Grijs: De regel is gedeactiveerd en wordt niet meegenomen bij het plannen. <!-- TM 100 -->
  - Geel: De regel staat in de softmodus. Als deze regel wordt overtreden, wordt er tijdens het plannen een waarschuwing gegenereerd. De actie wordt wel gewoon uitgevoerd. <!-- TM 100 -->
  - Rood: De regel is volledig geactiveerd. Bij elke overtreding van het contract wordt er een foutmelding gegenereerd met details over de specifieke regel die is overtreden. <!-- TM 100 -->