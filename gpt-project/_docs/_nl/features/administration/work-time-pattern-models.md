---
title: Planningsmodellen aanmaken
product_label:
  - advanced
  - enterprise
  - classic
description: Gebruik planningsmodellen bij je planningsoptimalisatie om te voorkomen dat je medewerkers willekeurige diensten toegewezen krijgen.
related_articles:
  - overwrite_title: Een referentiedatum instellen
    filepath: features/administration/reference-date.md
  - overwrite_title: Een geoptimaliseerde planning aanmaken
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-split-shifts.md
---

 Een planningsmodel bestaat uit [weekmodellen](#weekmodellen-aanmaken) en bepaalt hoe {% link_new dagmodellen | features/administration/daymodels/daymodel-basics.md %} worden toegewezen aan je medewerkers.

In de volgende afbeelding wordt de samenstelling van dagmodellen en weekmodellen in een planningsmodel weergegeven.

{{ 1 | image: 'Structuur van een planningsmodel' }}

Met planningsmodellen kun je herhalende patronen van diensten aanmaken en planningsbeperkingen instellen voor de functionaliteit **Geoptimaliseerde planning maken**.<br>
Planningsmodellen hebben de volgende voordelen:

- Ze geven aan welke dagmodellen kunnen worden gebruikt om een medewerker in te plannen.
- Medewerkers krijgen geen willekeurig gecombineerde diensten toegewezen.
- Ze bepalen de begintijden voor de diensten.
- Ze geven een volgorde aan voor de toewijzing van dagmodellen.

Als alternatief voor planningsmodellen kun je dienstenseries gebruiken of {% link_new beschikbaarheden | features/administration/availabilities.md %} voor je medewerkers configureren.

## Vereisten

Om planningsmodellen te kunnen gebruiken, moet aan de volgende vereisen zijn voldaan:
- Je hebt {% link_new dagmodellen | features/administration/daymodels/daymodel-creation.md %} en [weekmodellen](#weekmodellen-aanmaken) aangemaakt, en dagmodellen aan de weekmodellen toegevoegd.
- Elk planningsmodel bevat minstens een weekmodel.
- Elk weekmodel bevat minstens een {% link_new dagmodel | features/administration/daymodels/daymodel-basics.md %}.
- Je hebt planningsmodellen aan je medewerkers toegewezen.

## Weekmodellen aanmaken

Een weekmodel is een groep dagmodellen. Je kunt dagmodellen groeperen op basis van verschillende criteria, bijvoorbeeld dienstlengte, activiteiten, begintijd, etc.<br>

Je kunt weekmodellen alleen gebruiken als onderdeel van een planningsmodel. Voor een werkweek plant injixo medewerkers in volgens de dagmodellen die in het weekmodel zijn opgenomen. Zo weet je zeker dat al je medewerkers eerlijkere en consistentere werkuren krijgen.

Volg deze stappen om een weekmodel aan te maken:

1. Ga naar _Plan > Configuratie > Weekmodellen_{:.breadcrumbs}.
2. Klik op het pictogram Nieuw {% icon item-add | icon-only %} in de linker bovenhoek.
    Aan de rechterkant wordt een configuratievenster geopend.
3. Configureer de instellingen van het weekmodel:<br>
  **Naam**: Voer een unieke naam in (max. 50 tekens).<br>
  **Afkorting**: Voer de naam in of een kortere versie hiervan (max. 25 tekens).<br>
  **Kleur**: De kleur helpt je het weekmodel in een lijst te vinden.<br>
  **Maximumaantal Uitzonderingsdagen per Week**: Op [uitzonderingsdagen](#uitzonderingsdagen) negeert injixo de regels van het planningsmodel om tegemoet te komen aan de personeelsbehoefte.
4. Klik op _OK_{:.doc-button}.

Je kunt nu dagmodellen aan je weekmodellen toevoegen.

### Dagmodellen aan een weekmodel toevoegen

1. Ga in het configuratievenster van het weekmodel naar de sectie **Dagmodellen** en klik op het pictogram Toevoegen {% icon item-add | icon-only %}.
2. Selecteer een of meerdere dagmodellen uit de lijst.
3. Klik op _OK_{:.doc-button}.

Je kunt zowel {% link_new gefixeerde als variabele dagmodellen | features/administration/daymodels/daymodel-basics.md | #typen-dagmodellen %} aan een weekmodel toevoegen. Als je variabele dagmodellen gebruikt, dan kan de functionaliteit **Geoptimaliseerde planning maken** de optimale begintijd van de diensten bepalen binnen de beperkingen die door het dagmodel worden bepaald.

> Opmerking
>
> injixo kan alleen dagmodellen inplannen die aan de eenheid zijn toegewezen waaraan de persoon is toegewezen. Als je {% link_new de dagmodellen hebt beperkt | features/administration/create-and-manage-planning-units.md | #dagmodellen-beperken %} in je eenheid, dan worden de dagmodellen die je zou verwachten op basis van je planningsmodel mogelijk niet gebruikt.
>
> injixo kan vervangbare activiteiten in een dienst vervangen door planbare activiteiten. Gebruik variabele dagmodellen voor elke dienstduur dat een contract nodig heeft en gebruik de systeemactiviteit Aanwezig (ID: 1) als {% link_new basisactiviteit | features/administration/daymodels/daymodel-basics.md | #basisactiviteit-en-dienstduur %}. Maak niet voor elke afzonderlijke activiteit dagmodellen aan.

## Planningsmodellen aanmaken

1. Ga naar _Plan > Configuratie > Planningsmodellen_{:.breadcrumbs}.
2. Klik op het pictogram Nieuw {% icon item-add | icon-only %} in de actiebalk.
3. Configureer de instellingen van het planningsmodel:<br>
  **Naam**: Voer een unieke naam in (max. 50 tekens).<br>
  **Afkorting**: Voer de naam in of een kortere versie hiervan (max. 25 tekens).<br>
  **Kleur**: De kleur helpt je het planningsmodel in een lijst te vinden.<br>
  **Type**: Het [type](#planningsmodeltypen) bepaalt hoe injixo het planningsmodel gebruikt.<br>
  **Weekmodel voor Uitzonderingsdagen**: Selecteer het weekmodel dat voor [uitzonderingsdagen](#uitzonderingsdagen) moet worden ingepland.
4. Klik op _OK_{:.doc-button}.

Je kunt nu weekmodellen aan je planningsmodel toevoegen.

### Weekmodellen aan een planningsmodel toevoegen

1. Klik in het dialoogvenster van het planningsmodel op het pictogram Toevoegen {% icon item-add | icon-only %} in de sectie **Weekmodellen**.
2. Selecteer een **Weekmodel** uit de lijst.
3. Stel een **Rang** in.<br>
  Als je meerdere weekmodellen toevoegt, klik je op de pictogrammen Omlaag {% icon down-arrow-blue | icon-only %} en Omhoog {% icon up-arrow-blue | icon-only %}. om de rang te wijzigen.
4. Klik op _OK_{:.doc-button}.

### Rang

De rang van weekmodellen binnen planningsmodellen is relevant als je planningsmodellen van het type [type B of D](#planningsmodeltypen) gebruikt. injixo wijst de weekmodellen toe in de volgorde die hier zijn geconfigureerd.

Gebruik de pictogrammen Omlaag {% icon down-arrow-blue | icon-only %} en Omhoog {% icon up-arrow-blue | icon-only %} om de rang van de weekmodellen te bepalen.

## Planningsmodeltypen

| Type | Naam               | Gebruik van weekmodellen                                                      | Toewijzing van dagmodellen | Begintijd van dienst              | Effect             |
| ---- | ------------------ | -------------------------------------------------------------------------- | -------------------- | ----------------------------- | --------------------------------- |
| A    | Flexibele Keuze | injixo kan een willekeurig dagmodel selecteren uit de weekmodellen die voor elke dag van elke week zijn opgenomen. | injixo kan elk dagmodel uit elk weekmodel gebruiken. | Flexibel    | Afhankelijk van de kantooruren van je bedrijf kan type A leiden tot een verdeling van diensten die je medewerkers als willekeurig of stressvol kunnen ervaren. Zo kan een medewerker een vroege dienst toegewezen krijgen op maandag, een nachtdienst op dinsdag en een late dienst op woensdag etc. |
| B    | Starre Rotatie     | injixo plant de weekmodellen in de volgorde in die door hun rang wordt bepaald. | Voor elke week selecteert injixo het dagmodel dat de personeelsbehoefte het beste dekt. | Vast    | Als je dit type planningsmodel aan medewerkers toewijst, dan moet je een {% link_new referentiedatum instellen | features/administration/reference-date.md %}. De referentiedatum bepaalt wanneer het planningsmodel als eerste wordt gebruikt.<br> Elke medewerker krijgt voor de hele week hetzelfde dagmodel toegewezen, bijvoorbeeld: begintijd 9:00 uur van maandag tot vrijdag. Deze regel kan alleen worden overschreven door uitzonderingsdagen in te stellen. Dit is het meest consistente diensttoewijzing van alle vier de typen. |
| C    | Variabele Rotatie  | injixo houdt geen rekening met de gedefinieerde rang van weekmodellen. | injixo selecteert een dagmodel voor de hele week. | Vast    | Medewerkers kunnen elk weekpatroon toegewezen krijgen om zo goed mogelijk aan de personeelsbehoefte te voldoen. Aangezien de diensten op hetzelfde tijdstip beginnen, hebben medewerkers de hele week consistente werkuren. |
| D    | Combi-rotatie (A/B) | injixo houdt rekening met de rang die voor de weekmodellen is vastgelegd. | injixo selecteert een dagmodel voor de hele week.| Flexibel (binnen een tijdsperiode)    |  Op basis van de personeelsbehoefte kan injixo medewerkers inplannen met vroege diensten met een begintijd tussen 8:00 uur en 10:00 uur. Met type D kan injixo flexibeler plannen zodat er zo goed mogelijk aan de personeelsbehoefte wordt voldaan, terwijl er redelijk consistente planningen aan je medewerkers worden toegewezen. |



## Uitzonderingsdagen

Op uitzonderingsdagen kan injixo de regels negeren die door het actueel gebruikte [planningsmodel](#planningsmodeltypen) worden bepaald. Zo kun je uitzonderingsdagen gebruiken om een nachtdienst in te plannen in een week waarin een medewerker gewoonlijk ochtenddiensten draait.<br>

Uitzonderingsdagen geven prioriteit aan de personeelsbehoefte en zorgen voor een betere dekking. Hierdoor krijgen je medewerkers wel minder consistente planningen.

Volg deze stappen om uitzonderingsdagen in te plannen:

1. [Maak een afzonderlijk weekmodel aan](#weekmodellen-aanmaken) en wijs het toe aan de dagmodellen die je als uitzondering wilt gebruiken.
2. In het dialoogvenster van de weekmodellen die je voor de standaard dienst wilt gebruiken, dien je het aantal uitzonderingsdagen per week aan te geven.
3. Klik in het dialoogvenster van het planningsmodel het weekmodel dat je voor uitzonderingsdagen wilt gebruiken.

Bij het selecteren van een dagmodel voor de week kan injixo geen dagmodellen gebruiken die voor uitzonderingsdagen zijn gedefinieerd. Zorg ervoor dat alle configuratiegegevens voor het plannen (bijvoorbeeld alle dagmodellen die je gebruikt en het planningsmodel) voldoen aan de {% link_new werktijdrichtlijnen | features/administration/create-contracts.md | #richtlijnen-voor-de-werktijd %} die in het arbeidscontract van de medewerker worden vermeld. Als het dagmodel dat voor de week wordt gebruikt overeenkomt met het contract, dan kan injixo het oorspronkelijke dagmodel vervangen door een dagmodel dat voor uitzonderingsdagen is gedefinieerd, om beter aan de personeelsbehoefte te voldoen.

## Planningsmodellen aan medewerkers toewijzen

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}.
2. Selecteer een medewerker uit de lijst.
3. Klik op het pictogram Toevoegen {% icon item-add | icon-only %} in de sectie **Planningsmodellen**.<br>
   Aan de rechterkant wordt een configuratievenster geopend.
4. Configureer de instellingen:<br>
  **geldig vanaf/geldig tot en met**: Stel een {% link_new geldigheidsperiode | features/administration/set-a-validity-period.md %} in.<br>
  **Planningsmodel**<br>
  **Referentiedatum**: Stel een {% link_new referentiedatum | features/administration/reference-date.md %} in op de datum van de eerste dag waarop het planningsmodel wordt gebruikt.
5. Klik op _OK_{:.doc-button}.

Gebruik de functionaliteit {% link_new massa-update | features/administration/mass-update.md %} om een planningsmodel aan meerdere medewerkers tegelijk toe te wijzen.

> Let er bij het gebruik van massa-update op dat je planningsmodellen van het type B toewijst.
>
> Als je de functionaliteit Massa-update gebruikt en voor iedereen dezelfde referentiedatum instelt, worden alle medewerkers op dezelfde tijden met hetzelfde weekmodel ingepland.
>
> Selecteer in plaats daarvan kleinere groepen voor de massa-update en stel de daaropvolgende maandagen als referentiedatum. Op deze manier zal de rotatie van elke groep in een andere week beginnen.

## Voorbeelden

### Voorbeeld A: Starre rotatie met vroege en late diensten

Configureer een planningsmodel van type B (starre rotatie) en wijs er drie verschillende weekmodellen aan toe. Vergeet niet om de rang voor de weekmodellen in te stellen.

- Weekmodel 1 (rang 1) bevat modellen voor ochtenddiensten (diensten die beginnen tussen 7.00 uur en 9.00 uur).
- Weekmodel 2 (rang 2) bevat dagmodellen voor avonddiensten (diensten die eindigen om 23.00 uur).
- Weekmodel 3 (rang 3) bevat dagmodellen voor middagdiensten (diensten die beginnen tussen 11.00 uur en 12.00 uur).

Met dit planningsmodel roteren medewerkers consistent tussen een week met morgendiensten, een week met avonddiensten en een week met middagdiensten. 

Hoewel dit enige flexibiliteit vereist, hebben medewerkers heel consistente werkuren gedurende de week.

### Voorbeeld B: Uitzonderingsdagen voor nachtdiensten

Configureer een planningsmodel met drie verschillende weekmodellen. Stel maximaal twee uitzonderingsdagen per week in.

- Weekmodel 1 bevat dagmodellen voor ochtenddiensten.
- Weekmodel 2 bevat dagmodellen voor avonddiensten.
- Weekmodel 3 bevat dagmodellen voor nachtdiensten (selecteer dit dagmodel in het vervolgkeuzemenu **Weekmodel voor Uitzonderingsdagen**).

Met dit planningsmodel wisselen medewerkers tussen ochtenddiensten in de eerste week en avonddiensten in de daarop volgende week. Maar omdat je al twee uitzonderingsdagen hebt geselecteerd, kunnen medewerkers ook twee nachtdiensten per week toegewezen krijgen, als dat de beste toewijzing is om aan de personeelsbehoefte te voldoen.

<!-- TODO: very special example, add some more context  -->
<!-- ### Example: Performance-Based Scheduling With WTPMs and Preferred Day Models

Use Work Time Pattern Models and preferred day models  for Performance-Based Shift Assignment.

* Within the Week Time Patterns, assign the shifts according to agents' performance.
* Assign the Work Time Pattern Model to an agent with a validity period. Adjust it regularly according to performance scores.

For your high achievers you can pick some of the day models and assign them directly to these employees as personal day models. The AutoScheduler will only use these day models while generating schedules. This ensures that out-of-favor shifts are not assigned to high performing agents. -->

<!-- TODO: Example: normal use case scheduling different hours or working days in different weeks -->
<!-- ### Example: Scheduling Different Number of Working Days or Hours in Different Weeks -->
<!-- There is a bad German article /de/scheduling-different-wtm/ using WTPM Type B with two WTMs 4x10 and 5x8 hour shifts, with Autoscheduler contract parameter. minimum days per week with value 4 and scheduling parameter 2602 with value 10:00 -->
