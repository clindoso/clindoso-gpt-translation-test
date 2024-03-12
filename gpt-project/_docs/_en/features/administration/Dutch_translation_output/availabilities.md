---
title: Beschikbaarheden <!-- TM 100 -->
product_label:
  - advanced
  - enterprise
  - classic
description: Maak herbruikbare beschikbaarheden aan om tijdsperiodes te definiëren, tijdens welke medewerkers kunnen worden ingepland. <!-- TM 100 -->
redirect_from:
  - /availability-periods/
redirect_reason: rename article September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
---

Met beschikbaarheden kun je aangeven wanneer een medewerker niet beschikbaar is om te zworken op bepaalde dagen of tijden. Zo kun je de beperkingen van de openingstijden van je eenheden en de contracten van je medewerkers verder verfijnen. <!-- GPT translation -->

Je kunt alleen een dienst of activiteit aan de planning toevoegen, als deze in het geconfigureerde tijdsframe past. Personen die geen beschikbaarheid hebben geconfigureerd, gelden te allen tijde als beschikbaar in je openingstijden. <!-- GPT translation -->

Hier zijn enkele voorbeelden van toepassingen: <!-- GPT translation -->

- vaste werktijden en -dagen voor elke week configureren <!-- GPT translation -->
- Beschikbaarheden over de weken heen laten rouleren <!-- GPT translation -->
- Tijdelijk beschikbare medewerkers configureren <!-- GPT translation -->

injixo houdt in de geoptimaliseerde planning standaard rekening met de beschikbaarheid van medewerkers. Bij het aanmaken van diensten wordt hier (nog) geen rekening mee gehouden. Pas bij het toewijzen van diensten wordt met de beschikbaarheid rekening gehouden. <!-- GPT translation -->

injixo houdt alleen rekening met beschikbaarheden als de planningsregel _2611_{:.id-label} is geactiveerd. Schakel deze regel uit als je medewerkers diensten wilt laten aanvragen en je ze diensten langer dan hun beschikbaarheid wilt toewijzen. <!-- GPT translation -->

In injixo Me kunnen medewerkers tot maximaal 14 dagen {% link_new zelf hun beschikbaarheid invoeren | features/injixo-me/use-injixo-me/explore-injixo-me.md | #je-beschikbaarheid-instellen-beschikbaarheid %}. Zowel de betrokken medewerkers als planners moeten overbodige items regelmatig handmatig verwijderen uit de lijst. Controleer deze beschikbaarheden handmatig voor dat je een planning maakt om planningsfouten te voorkomen. <!-- GPT translation -->
## Beschikbaarheden configureren <!-- GPT translation -->

Je kunt beschikbaarheid op twee manieren configureren: <!-- GPT translation -->

- Persoonlijke beschikbaarheden: Stel tijdelijke of permanente beschikbaarheden voor individuele medewerkers in in _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- GPT translation -->
- Dagmodelbeschikbaarheden: Voeg beschikbaarheden toe aan dienstenseries om dezelfde beschikbaarheid toe te wijzen aan meerdere medewerkers. <!-- GPT translation -->

Opmerking: Dagmodelbeschikbaarheden overschrijven de persoonlijke beschikbaarheden, evenals beschikbaarheden die handmatig zijn ingevoerd. <!-- GPT translation -->

## Vaste werkdagen/tijden configureren <!-- GPT translation -->

Voorbeeld: Een medewerker kan vanwege kinderopvang alleen op woensdag en vrijdag in de ochtend van 8 uur tot 12 uur werken. Je kunt de beschikbaarheid van deze medewerker als volgt configureren: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- TM 100 -->
2. Selecteer de persoon in de lijst. <!-- GPT translation -->
3. Klik met de knop **Toevoegen** {% icon item-add | icon-only %} in de sectie **Beschikbaarheid** aan de rechterkant. <!-- GPT translation -->
4. Configureer de beschikbaarheid: <!-- GPT translation -->
    - (Optioneel) **Geldig vanaf** en **Geldig tot en met**: Als de beschikbaarheid slechts in een bepaalde periode geldig is, dan beperken de datums de {% link_new geldigheidsperiode | features/administration/set-a-validity-period.md %}. <!-- GPT translation -->
    - **Dagtypes**: Selecteer Woensdag en Vrijdag. Houd CTRL ingedrukt om meerdere opties te selecteren. <!-- GPT translation -->
    - **Vanaf**: Voer 8:00 in. <!-- GPT translation -->
    - **Tot**: Voer 12:00 uur in. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}. <!-- TM 100 -->


## Beschikbaarheden over weken heen verschuiven <!-- GPT translation -->

De volgende subsecties beschrijven hoe je uitgaat van de beschikbaarheden om te plannen voor het volgende voorbeeld, of voor vergelijkbare usecases: <!-- GPT translation -->

- je contactcenter is geopend van 8:00 tot 20:00 uur; <!-- GPT translation -->
- In de even weken draait eenhedenplanning A ochtenddiensten en eenhedenplanning B avonddiensten. <!-- GPT translation -->
- In oneven weken werkt EHE B van 07:00 tot 15:00 uur en EHE A van 08:30 tot 22:30 uur. <!-- GPT translation -->
- De ochtend-, of de vroegdienst begint om 8:00 uur en eindigt om 14:00 uur. <!-- GPT translation -->
- De avonddienst is van 14:00 uur tot 20:00 uur. <!-- GPT translation -->

### Dagmodellen `adds up` Maak beschikbaarheid uurmodellen aan <!-- GPT translation -->

Ga naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs} en klik op het pictogram Nieuw toevoegen {% icon item-add | icon-only %} om een _dagmodel aan te maken | features/administration/daymodels/daymodel-creation.md %}.<br>In het volgende voorbeeld lees je hoe je twee dagmodellen instelt om een ochtenddienst en een avonddienst af te wisselen. <!-- GPT translation -->


Voor de ochtenddienst: <!-- GPT translation -->

1. Maak een nieuw dagmodel aan. <!-- GPT translation -->
2. Stel het dagmodel in: <!-- GPT translation -->
    - **Type**: Selecteer **Beschikbaarheidskader**. <!-- GPT translation -->
    - **Naam** en **Afkorting**: Geef een unieke naam en afkorting op, bijvoorbeeld Beschikbaarheid 8&nbsp;AM - 2&nbsp;PM en Avail 8AM-2PM. <!-- GPT translation -->
    - (Optioneel) **Kleur**: Selecteer een kleur om de dagmodellen gemakkelijker te lokaliseren. <!-- GPT translation -->
    - **Begingrens Beschikbaarheid**: Voer 08:00 uur in. <!-- GPT translation -->
    - **Einde beschikbaarheidsperiode**: Voer 14:00 in.<br> Je kunt ook de **tijdsduur beschikkbaarheidsperiode** instellen. De maximale waarde is 48 uur. <!-- GPT translation -->
3. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Voor de avonddienst: <!-- GPT translation -->

1. Maak een nieuw dagmodel aan. <!-- Repetition of GPT translation -->
2. Stel het dagmodel in: <!-- Repetition of GPT translation -->
    - **Type**: Selecteer **Beschikbaarheidskader**. <!-- Repetition of GPT translation -->
    - **Naam** en **Afkorting**: Voer een unieke naam en afkorting in, bijvoorbeeld Beschikbaarheid 14:00-20:00 uur en Beschik 14-20 uur. <!-- GPT translation -->
    - (Optioneel) **Kleur**: Selecteer een kleur om de dagmodellen gemakkelijker te lokaliseren. <!-- Repetition of GPT translation -->
    - **Vanaf**: Voer 14:00. <!-- GPT translation -->
    - **Einde beschikbaarheidsperiode**: Voer 20:00 in.<br> Als alternatief kun je een **Periode duur beschikbaarheid** instellen. De maximale waarde is 48 uur. <!-- GPT translation -->
3. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

### Een dienstenserie aanmaken en toewijzen <!-- GPT translation -->

Volg deze stappen om de twee dagmodellen die je net hebt aangemaakt, te gebruiken bij het inplannen: <!-- GPT translation -->


1. {% link_new Maak een dienstenserie aan | features/administration/shift-sequences.md | #dienstenseries-aanmaken %} met twee **Medewerkersregels** en een **Duur** van 14 dagen.<br> <!-- GPT translation -->
2. Voeg de dagmodellen beurtelings toe aan de dienstenserie. Voeg in rij 1 het ochtendmodel toe in week 1 en het avondmodel toe in week 2. Voeg in rij 2 de dagmodellen in omgekeerde volgorde toe. <!-- GPT translation -->
3. {% link_new Wijs de dienstenserie toe | features/administration/employee-overview.md | #dienstenserie-toewijzen %} aan je medewerkers: <!-- GPT translation -->
    - Selecteer de eerste rij voor de medewerkers van eenhheid A. <!-- GPT translation -->
    - Voor medewerkers in eenhied B, selecteer de tweede medewerkersregel. <!-- GPT translation -->
    - Stel een **uitgangsdatum** in om aan te geven vanaf wanneer de dienstenreeks moet worden gepland. Stel de uitgangsdatum in op een weekdag waarop jouw planningsweek begint, bv. maandag. <!-- GPT translation -->
4. {% link_new Voeg de dienstenserie toe | features/scheduling/schedules/schedules-insert-shift-sequences.md | #dienstenseries-toevoegen %} aan je planning. <!-- GPT translation -->


## Het aandeel medewerkers met beschikbaarheden tijdelijk aanpassen <!-- GPT translation -->

Voorbeeld: Een van je medewerkers is in een bepaalde week alleen van 9:00 tot 12:00 uur beschikbaar.<br>Volg hetzelfde proces als voor [Vaste werkdagen/-tijden voor elke week configureren](#vaste-werkdagen--tijden-voor-elke-week-configureren), om deze tijden aan de specifieke week toe te voegen. <!-- GPT translation -->

## Beschikbaarheden bewerken <!-- GPT translation -->

Je kunt de beschikbaarheid bewerken die je voor een individuele medewerker hebt ingesteld: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- TM 100 -->
2. Selecteer de medewerker voor wie je de beschikbaarheid wilt bewerken. <!-- GPT translation -->
3. Klik in het rechter zijpaneel op **Beschikbaarheid**. <!-- GPT translation -->
4. Klik naast de beschikbaarheidsstatus die je wilt wijzigen op het {% icon pencil | icon-only %}. <!-- GPT translation -->
5. Bewerk de beschikbaarheid. <!-- GPT translation -->
6. Klik in het venster **Beschikbaarheid bewerken** op _OK_{:.doc-button}. <!-- GPT translation -->
7. Klik in het **Configuratie-eenheden**-venster op _OK_{:.doc-button} aan de linkerkant. <!-- GPT translation -->

7. Bewerk het dagmodel:  <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs}. <!-- GPT translation -->
2. Selecteer het dagmodel dat je wilt bewerken. <!-- GPT translation -->
3. Bewerk het dagmodel. <!-- GPT translation -->
4. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Je kunt beschikbaarheden ook bewerken in het Dienstrooster-Center. Lees meer over {% link_new hoe je beschikbaarheden toevoegt en verwijdert in het Dienstrooster-Center | features/scheduling/shiftcenter/add-and-delete-items.md | #beschikbaarheid-toevoegen %}. Voor tijdelijke wijzigingen plak je werk- en dagmodelbeschikbaarheden in de cel om ze te converteren in handmatig toegevoegde beschikbaarheden. <!-- GPT translation -->

In Shift Center worden de beschikbaarheden in elk niveau met het symbool `<>` weergegeven. Beweeg je muis boven het symbool om alle details te bekijken. In de dagcellen worden de beschikbaarheden als oranje elementen weergegeven. In uitgevouwen dagcellen worden de beschikbaarheden van medewerkers weergegeven als witte balken met een oranje omlijning. <!-- GPT translation -->

## Beschikbaarheden verwijderen <!-- GPT translation -->

Je kunt de beschikbaarhheidsinstellingen die je voor een enkele medewerker hebt geconfigureerd, verwijderen: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- TM 100 -->
2. Selecteer de medewerker wiens beschikbaarheidsgegevens je wilt verwijderen. <!-- GPT translation -->
3. Klik in het rechter zijpaneel op **Beschikbaarheid**. <!-- Repetition of GPT translation -->
4. Klik naast de beschikbaarheid die je wilt verwijderen op het pictogram Verwijderen:  {% icon item-delete | icon-only %}. <!-- GPT translation -->
5. Klik in het venster **Bevestiging** op _Ja_{:.doc-button}. <!-- GPT translation -->
6. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Als je dagmodellen van het type **Beschikbaarheidsperiode** hebt geconfigureerd, verwijder dan het dagmodel: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs}. <!-- Repetition of GPT translation -->
2. Selecteer het dagmodel dat je wil verwijderen. <!-- GPT translation -->
3. Klik in de actiebalk op het pictogram Dagmodel verwijderen {% icon item_delete | icon-only | repeat %}. <!-- GPT translation -->
4. Klik in het **Bevestigingsvenster** op _Ja_{:.doc-button}. <!-- GPT translation -->