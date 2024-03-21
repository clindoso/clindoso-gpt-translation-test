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
gpt_translation: True
---

Beschikbaarheidsrestricties bepalen op welke dagen en tijden medewerkers niet of slechts beperkt beschikbaar zijn om werk in te plannen. Zo kun je de beperkingen die worden bepaald door de openingstijden van je eenheden en de contracten van je medewerkers nog verder beperken. <!-- GPT translation -->

Je kunt alleen een dienst toevoegen als deze binnen het geconfigureerde tijdsbestek past. Medewerkers zonder geconfigureerde beschikbaarheid worden beschouwd als zijnde altijd beschikbaar binnen je openingstijden. <!-- GPT translation -->

Beschikbaarheden worden op verschillende manieren gebruikt, bijvoorbeeld: <!-- GPT translation -->

- vaste werkdagen/-tijden voor elke week configureren <!-- GPT translation -->
- Beschikbaarheid over weken draaien <!-- GPT translation -->
- De beschikbaarheid te configureren voor medewerkers die tijdelijk beschikbaar zijn. <!-- GPT translation -->

injixo houdt standaard rekening met medewerkersbeschikbaarheid bij het maken van geoptimaliseerde roosters. Beschikbaarheid wordt niet in acht genomen bij het genereren van diensten, maar pas bij het toewijzen van diensten aan de betreffende medewerker. <!-- GPT translation -->

By default, injixo houdt rekening met Availabilities (2599) bij het maken van geoptimaliseerde planningen. Bij het genereren van diensten niet, maar wel bij het toewijzen ervan. Alleen als de planningsregel _2611_{:.id-label} is geactiveerd, houdt injixo bij het toewijzen van diensten rekening met Availabilities. <!-- GPT translation -->

## Beschikbaarheden configureren <!-- GPT translation -->

Beschikbaarheden kun je op twee manieren configureren: <!-- GPT translation -->

- Persoonlijke beschikbaarheid: Stel tijdelijke of permanente beschikbaarheden in voor afzonderlijke medewerkers under _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- GPT translation -->
- Dagmodelbeschikbaarheden: Voeg beschikbaarheden toe aan dienstenseries om dezelfde beschikbaarheden aan meedere medewerkers toe te wijzen. <!-- GPT translation -->

Opmerking: Dagmodelbeschikbaarheden overschrijven alle andere beschikbaarheden, inclusief handmatig toegevoegde nieuwe beschikbaarheden. <!-- GPT translation -->

## Vaste werkdagen/-tijden configureren voor elke week <!-- GPT translation -->

Voorbeeld: Een medewerker is vanwege kinderopvang op woensdagen en vrijdagen slechts beschikbaar in de ochtend van 8:00 uur tot 12:00 uur. Je kunt de beschikbaarheid van deze medewerker als volgt configureren: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- TM 100 -->
2. Selecteer de persoon in de lijst. <!-- GPT translation -->
3. Klik in de sectie **Beschikbaarheid** aan de rechterkant op het pictogram Nieuwe toevoegen {% icon item-add | icon-only %}. <!-- GPT translation -->
4. Stel de beschikbaarheid in: <!-- GPT translation -->
    - (Optioneel) **Geldig vanaf** en **geldig tot en met**: Als de beschikbaarheid slechts gedurende een bepaalde periode geldig is, dan worden deze datums de {% link_new geldigheidsperiode | features/administration/set-a-validity-period.md %}. <!-- GPT translation -->
    - **Dagtypes**: Selecteer Woensdag en Vrijdag. Houd CTRL ingedrukt om meerdere opties te selecteren. <!-- GPT translation -->
    - **Vanaf**: Voer 8:00 in. <!-- GPT translation -->
    - **Tot en met**: Voer vervolgens 12:00 uur in. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

## Beschikbaarheden over weken heen kopiëren <!-- GPT translation -->

De volgende subsecties leggen uit hoe je aan de hand van het volgende voorbeeld, of soortgelijke use cases plant met beschikbaarheden: <!-- GPT translation -->

- Je contactcenter is geopend van 8.00 tot 1.9.00 uur. <!-- GPT translation -->
- In de even weken werkt eenhuid A ochtenddiensten en eenheid B avonddiensten. <!-- GPT translation -->
- In oneven weken werkt EKEMMM (Eenheid Klaingke week ochtend, akeern week avond) van 06:00 tot 14:00 uur en eenheid AEV van 14:00 tot 22:00 uur. <!-- GPT translation -->
- De ochtend- vindt plaats van 8.00 uur tot 14.00 uur. <!-- GPT translation -->
- De middagdienst is van 14:00 tot 20:00 uur. <!-- GPT translation -->

### Dagmodellen Beschikbaarheid. <!-- GPT translation -->

Om {% link_new dagmodellen aan te maken | features/administration/daymodels/daymodel-creation.md %} ga je naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs} en klik je op het pictogram Nieuw {% icon item-add | icon-only %}.<br>In het volgende voorbeeld wordt uitgelegd hoe je twee dagmodellen configureert om een ochtend- en avonddienst rouleren. <!-- GPT translation -->

Volg deze stappen om een dagmodel voor de ochtenddienst in te stellen: <!-- GPT translation -->

1. Maak een nieuw dagmodel aan. <!-- GPT translation -->
2. Stel het dagmodel in: <!-- GPT translation -->
    - **Type**: Selecteer **Beschikbaarheidsperiode**. <!-- GPT translation -->
    - **Naam** en **afkorting**: Voer een unieke naam en afkorting in, bijvoorbeeld Beschikbaarheid 8&nbsp;'s ochtends - 2&nbsp;'s middags en Afst 8am-2pm. <!-- GPT translation -->
    - (Optioneel) **Kleur**: Selecteer een kleur om het dagmodel makkelijker terug te kunnen vinden. <!-- GPT translation -->
    - **Begintijd Beschikbaarheidsperiode**: Voer 8:00 in. <!-- GPT translation -->
    - **Einde beschikbaarheidsperiode**: Voer 14:00 in.<br> Je kunt ook de **Duur beschikbaarheidsperiode** instellen. De maximumwaarde is 48 uur. <!-- GPT translation -->
3. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Volg de volgende stappen om voor de avonddienst het dagmodel te configureren: <!-- GPT translation -->

1. Maak een nieuw dagmodel aan. <!-- Repetition of GPT translation -->
2. Stel het dagmodel in: <!-- Repetition of GPT translation -->
    - **Type**: Selecteer **Beschikbaarheidsperiode**. <!-- Repetition of GPT translation -->
    - **Naam** en **Afkorting**: Voer een unieke naam en afkorting in, bijvoorbeeld Beschikbaarheid 14:00 - 20:00 uur en 2PM-8PM. <!-- GPT translation -->
    - (Optioneel) **Kleur**: Selecteer een kleur om het dagmodel makkelijker terug te kunnen vinden. <!-- Repetition of GPT translation -->
    - **Begin Beschikbaarheidsperiode**: Voer 14:00 in. <!-- GPT translation -->
    - **Einde Beschikbaarheidskader**: Voer 20:00 uur in.<br>  Het is ook mogelijk om de **Beschikbaarheid** te beperken tot een bepaalde tijdsduur. De maximale waarde is 48 uur. <!-- GPT translation -->
3. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

### Een dienstenserie aanmaken en toewijzen <!-- GPT translation -->

Volg deze stappen om de twee dagmodellen zo in te stellen dat je ze bij het plannen kunt gebruiken: <!-- GPT translation -->

1. {% link_new Maak een dienstenserie aan | features/administration/shift-sequences.md | #dienstenseries-aanmaken %} met twee **Medewerkersregels** en een **Tijdsduur** van 14 dagen.<br> <!-- GPT translation -->
2. Voeg in de dienstenserie de dagmodellen om en om toe. Gebruik onder rij 1 in week 1 het dagmodel Ochtend, en voeg in week 2 het dagmodel Avond toe. Voeg in rij 2 de dagmodellen in omgekeerde volgorde toe. <!-- GPT translation -->
3. {% link_new Wijs de dienstenserie toe | features/administration/employee-overview.md | #een-dienstenserie-toewijzen %} aan je medewerkers: <!-- GPT translation -->
    - Selecteer de eerste medewerkersrij voor mensen in eenheden van het planningstype A. <!-- GPT translation -->
    - Selecteer de medewerkers in eenheids-B door de tweede personeelsrij te selecteren. <!-- GPT translation -->
    - Stel een **refentiedatum** in om te definiëren wanneer de dienstenserie begint met plannen. Stel de referentiedatum in op de dag in de week waar je rosterweek begint, bijvoorbeeld maandag. <!-- GPT translation -->
4. {% link_new Inserteer de dienstenserie | features/scheduling/schedules/schedules-insert-shift-sequences.md | #dienstenseries-toevoegen %}. <!-- GPT translation -->

## Tijdelijk beschikbare medewerkers configureren <!-- GPT translation -->

Voorbeeld: Een van je medewerkers is de komende week alleen beschikbaar voor werk van **9:00** tot **12:00 uur**.<br>Om hun beschikbaarheid dienovereenkomstig in te stellen, doorloop je de stappen om [vast werkdag-/tijdinstellingen in te stellen voor elke week](#vast-werkdagtijdstijden-instellen-voor-elke-week). Voeg de relevante {% link_new geldigheidsdatum | features/administration/set-a-validity-period.md %} en de juiste **Vanaf** \(*From*\) en **Tot** \( *To* \) toe. <!-- GPT translation -->

## Beschikbaarheden bewerken <!-- GPT translation -->

Je kunt de beschikbaarhheidsinstellingen bewerken, die je voor een individuele medewerker hebt geconfigureerd. <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- TM 100 -->
2. Selecteer de medewerker voor wie je de beschikbaarheid wilt bewerken. <!-- GPT translation -->
3. Klik in het rechter zijpaneel op **Beschikbaarheid**. <!-- GPT translation -->
4. Klik naast de beschikbaarheid die je wilt bewerken op het pictogram Bewerken {% icon pencil | icon-only %}. <!-- GPT translation -->
5. Bewerk de beschikbaarheid. <!-- GPT translation -->
6. Klik in het venster **Beschikbaarheid** op _OK_{:.doc-button}. <!-- GPT translation -->
7. Klik in de rechter benedenhoek van het rechter zijpaneel op _OK_{:.doc-button}. <!-- GPT translation -->

Als je beschikbaarheden met dagmodellen van het type **Beschikbaarheidsperiode** hebt geconfigureerd, bewerk dan het dagmodel: <!-- GPT translation -->

1. Ga naar *Plan > Configuratie > Dagmodellen*{:.breadcrumbs}. <!-- GPT translation -->
2. Selecteer het dagmodel dat je wilt bewerken. <!-- GPT translation -->
3. Bewerk het dagmodel. <!-- GPT translation -->
4. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Je kunt beschikbaarheid ook rechtstreeks in Dienstrooster-Center bewerken. Lees meer over {% link_new hoe je in Dienstrooster-Center beschikbaarheden toevoegt en verwijdert | features/scheduling/shiftcenter/add-and-delete-items.md | #beschikbaarheid-toevoegen %}. Je kunt persoonlijke of dagmodel-beschikbaarheden kopiëren en plakken in een cel om ze tijdelijk in handmatig toegevoegde beschikbaarheid om te zetten. <!-- GPT translation -->

In Dienstrooster-Center worden beschikbaarheden op ieder niveau met een `<>`-symbool weergegeven. Beweeg je cursor over het symbool voor de details. In de dagcellen worden beschikbaarheden als oranje elementen weergegeven. In uitgeklapte dagcellen worden medewerkersbeschikbaarheden weergegeven als witte balken met een oranje onderstreping. <!-- GPT translation -->

## Beschikbaarheden verwijderen <!-- GPT translation -->

Je kunt de beschikbaarhheidsinstellingen die je voor een individueel persoon hebt geconfigureerd verwijderen: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- TM 100 -->
2. Selecteer de persoon van wie je de beschikbaarheid wilt verwijderen. <!-- GPT translation -->
3. Klik in het rechter zijpaneel op **Beschikbaarheid**. <!-- Repetition of GPT translation -->
4. **Klik naast de beschikbaarheid die je wilt verwijderen op het pictogram Verwijderen**. <!-- GPT translation -->
5. Klik in het venster op **Ja**{:.doc-button} om te bevestigen. <!-- GPT translation -->
6. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Als je beschikbaarheden met dagmodellen van het type **Beschikbaarheid** hebt geconfigureerd, verwijder dan het dagmodel: <!-- GPT translation -->

1. Ga naar *Plan > Configuratie > Dagmodellen*{:.breadcrumbs}. <!-- Repetition of GPT translation -->
2. Selecteer het dagmodel dat je wilt verwijderen. <!-- GPT translation -->
3. Klik op het pictogram Verwijderen {% icon item-delete | icon-only %} in de handelingenbalk. <!-- GPT translation -->
4. Klik in het **Bevestigingsvenster** op _Ja_{:.doc-button}. <!-- GPT translation -->

## Beschikbaarheden in injixo Me <!-- GPT translation -->

Je kunt {% link_new medewerkers toestaan om in injixo Me zelf hun beschikbaarheid in te stellen | features/injixo-me/use-injixo-me/explore-injixo-me.md | #beschikbaarheid-instellen %}. Medewerkers kunnen maximaal 14 beschikbaarheden toevoegen. Planners dienen daarom regelmatig verouderde regels te verwijderen voordat zij een planning maken om eventuele planningsconflicten te voorkomen. <!-- GPT translation -->

Volg deze stappen om medewerkers toegang te geven om in injixo Me hun eigen beschikbaarheid in te voeren: <!-- GPT translation -->

1. Ga naar **Me**. <!-- GPT translation -->
2. Schakel de optie **Beschikbaarheid** in. <!-- GPT translation -->

Zodra dat is ingeschakeld, kunnen medewerkers in Me hun weekbeschikbaarheden toevoegen of aanpassen. Deze informatie wordt opgeslagen onder Configuratie. <!-- GPT translation -->