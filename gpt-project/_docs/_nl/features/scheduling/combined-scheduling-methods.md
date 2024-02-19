---
title: Planningsmethoden combineren
product_label:
  - advanced
  - enterprise
  - classic
description: Combineer planningsmethoden om aan de behoeften van je bedrijf te voldoen.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/availabilities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-time-pattern-models.md
---

Je kunt alle {% link_new planningsmethoden | features/scheduling/scheduling-methods.md %} op verschillende manieren combineren om planningen aan te maken die de juiste balans vinden tussen de behoeften van je personeel en die van je bedrijf.

In de volgende voorbeelden laten we enkele veelvoorkomende usecases zien voor het combineren van planningsmethoden. Je kunt ook andere combinaties van planningsmethoden gebruiken om de behoeften van je bedrijf zo goed mogelijk te dekken.

## Usecase 1: Medewerkers met flexibele diensten en medewerkers met specifieke werkuren of -dagen.  

Voor deze usecase kun je een gefixeerde planning combineren met roulerende flexibele diensten of volledig flexibele diensten.

Om je medewerkers met deze combinatie in te plannen, moet je eerst de configuratiegegevens instellen die in de volgende tabel worden weergegeven, en deze vervolgens aan de betreffende medewerkers toewijzen:


| Medewerkers met flexibele diensten            | Medewerkers met specifieke werkuren of -dagen                                                                                        |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wijs de planningsmodellen die je wilt gebruiken toe aan de medewerkers. | Maak specifieke dienstenseries aan die de uren of dagen aangeven wanneer ze werken en laat de rest van de week leeg.<br>Wijs de dienstenserie en de betreffende planningsmodellen aan hen toe.                                    |

Volg deze stappen om je medewerkers in te plannen:

1. Voeg je dienstenseries toe.
2. Gebruik de functionaliteit **Geoptimaliseerde planning maken**.<br>injixo plant je roulerende en volledig flexibele diensten zo in, dat de dekking door de dienstenseries wordt aangevuld.


## Usecase 2: Medewerkers met roulerende diensten en medewerkers met flexibele diensten

Voor deze usecase kun je roulerende flexibele diensten en volledig flexibele diensten combineren.

Om je medewerkers met deze combinatie in te plannen, moet je eerst de configuratiegegevens aan de betreffende medewerkers toewijzen, zoals in de volgende tabel wordt weergegeven:

| Medewerkers met roulerende flexibele diensten           | Medewerkers met volledig flexibele diensten                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wijs planningsmodellen van het type B of D aan hen toe. | Wijs planningsmodellen van type A aan hen toe.                                   |


Gebruik de functionaliteit **Geoptimaliseerde planning maken**.<br>Aan medewerkers met roulerende flexibele diensten wordt de roulatie toegewezen die wordt bepaald door hun planningsmodellen. Medewerkers met volledig flexibele diensten vullen de rest van de planning in.

## Usecase 3: Medewerkers met roulerende diensten en een beperkte beschikbaarheid

Deze usecase is van toepassing op medewerkers die roulerende diensten werken, maar op bepaalde tijden niet beschikbaar zijn. Ze kunnen op woensdagen bijvoorbeeld tot uiterlijk 17:00 uur werken.

Voor deze usecase kun je beschikbaarheden en roulerende flexibele diensten combineren. 

1. Stel voor je medewerkers {% link_new beschikbaarheden | features/administration/availabilities.md %} in die aangeven wanneer ze niet kunnen werken. In dit geval zijn ze alleen tot uiterlijk 17:00 uur beschikbaar.
2. Wijs de betreffende planningsmodellen aan hen toe.

Voor weken waarin de medewerker ochtenddiensten draait, wordt deze op woensdag ingepland.<br>Voor weken waarin de medewerker avonddiensten draait, wordt deze niet op woensdag ingepland, maar alleen op de overige weekdagen.

## Usecase 4: Medewerkers met gefixeerde diensten en een beperkte beschikbaarheid op bepaalde tijden. 

Deze usecase betreft medewerkers die gefixeerde diensten werken, maar op bepaalde dagen beperkt beschikbaar zijn. Ze werken bijvoorbeeld nacht- of weekenddiensten, maar alleen om de week.

Voor deze usecase kun je {% link_new dagmodellen van het type Beschikbaarheidsperiode | features/administration/daymodels/daymodel-basics.md | #typen-dagmodellen %} toevoegen aan {% link_new dienstenseries | features/administration/shift-sequences.md %} om het planningsresultaat op bepaalde dagen te beïnvloeden.<br>Zie de twee voorbeelden hieronder.

Volg deze stappen om medewerkers zo in te plannen dat ze om het weekend werken:

1. Maak een dagmodel aan van het type Beschikbaarheidsperiode met een tijdsbereik van middernacht (0:00 uur) tot 0:01 uur, dat als blocker dient.
2. Voeg het dagmodel aan één weekend in een dienstenserie met 14 dagen toe en laat alle overige velden leeg.
3. Wijs de dienstenserie toe aan de betreffende medewerkers.
4. Voeg de dienstenserie toe aan je planning.
5. Gebruik de functionaliteit **Geoptimaliseerde planning maken**.

injixo plant elk tweede weekend geen diensten in en optimaliseert de resterende dagen.

Volg deze stappen om medewerkers zo in te plannen dat ze om de week nachtdiensten draaien:

1. Maak een dagmodel van het type Beschikbaarheidsperiode aan met een tijdsbereik van middernacht (0:00 uur) tot 's middags (12:00 uur).
2. Voeg het dagmodel toe aan elke dag van een week in een dienstenserie met 14 dagen en laat alle overige dagen leeg.
3. Wijs de dienstenserie toe aan de betreffende medewerkers.
4. Voeg de dienstenserie toe aan je planning.
5. Gebruik de functionaliteit **Geoptimaliseerde planning maken**.

injixo plant de nachtdiensten in weken in tijdens welke medewerkers beschikbaar zijn, op basis van het planningsmodel dat aan elke medewerker is toegewezen. Voor andere weken kan injixo elke dienst toewijzen die voldoet aan het planningsmodel.
