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
gpt_translation: true
---

Beschikbaarheden bepalen wanneer een medewerker niet of slechts beperkt inzetbaar is op bepaalde dagen of tijdstippen. Je kunt de beperkingen die al zijn vastgelegd door de openingstijden van je eenheden en de contracten van je medewerkers verder beperken. <!-- GPT translation -->

Je kunt alleen een dienst of activiteit aan de planning toevoegen als deze binnen de geconfigureerde tijdsperiode past. Personen zonder geconfigureerde beschikbaarheid worden beschouwd als altijd beschikbaar binnen de door de afdeling of het contract gespecificeerde ruimte. <!-- GPT translation -->

Beschikbaarheden hebben diverse mogelijke toepassingen: <!-- GPT translation -->

- Vaste werkdagen/tijden voor elke week instellen <!-- GPT translation -->
- Beschikbaarheden over weken heen verschuiven <!-- GPT translation -->
- tijdelijk beschikbare medewerkers configureren <!-- GPT translation -->

In principe houdt injixo bij het maken van geoptimaliseerde planningen wel rekening met beschikbaarheden. Beschikbaarheden worden niet meegenomen bij het genereren van diensten, maar pas bij het toewijzen van diensten aan medewerkers. <!-- GPT translation -->

injixo houdt bij de planning alleen rekening met medewerkersbeschikbaarheid als het planningsprincipe _2611_{:.id-label} is geactiveerd. Als je wilt dat medewerkers diensten van een langere duur kunnen aanvragen en worden ingepland, dan raden we je aan om planningsprincipe 2611 te deactiveren. <!-- GPT translation -->

## Beschikbaarheden configureren <!-- GPT translation -->

Je kunt de beschikbaarheid op twee manieren configureren: <!-- GPT translation -->

- Persoonlijke beschikbaarheid: Stel tijdelijke of permanente beschikbaarheden in voor afzonderlijke medewerkers in _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- GPT translation -->
- Dagmodel-beschikbaarheden: Voeg beschikbaarheden toe aan dienstenseries om meerdere medewerkers dezelfde beschikbaarheid toe te wijzen. <!-- GPT translation -->

Opmerking: Dagmodel-beschikbaarheden worden boven persoonlijke beschikbaarheden geplaatst, evenals beschikbaarheden die handmatig zijn toegevoegd. <!-- GPT translation -->

## Vaste werkdagen en -tijden configureren voor elke week <!-- GPT translation -->

Voorbeeld: Een medewerker is op woensdag- en vrijdagochtend maar tot 12:00 uur beschikbaar in verband met kinderopvang. Je kunt zijn beschikbaarheid als volgt instellen: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- TM 100 -->
2. Selecteer de persoon in de lijst. <!-- GPT translation -->
3. Klik in de sectie **Beschikbaarheid** aan de rechterkant op het pictogram Nieuw toevoegen {% icon item-add | icon-only %}. <!-- GPT translation -->
4. Configureer de beschikbaarheid: <!-- GPT translation -->
    - (Optioneel) **Geldig vanaf** en **Geldig tot en met**: Als de beschikbaarheid geldig is voor een bepaalde datumbereik, dan beperken de datums de {% link_new geldigheidsperiode | features/administration/set-a-validity-period.md %}. <!-- GPT translation -->
    - **Dagtypes**: Selecteer Woensdag en Vrijdag. Houd CTRL ingedrukt om meerdere velden te selecteren. <!-- GPT translation -->
    - **Tot**: Voer 8:00 in. <!-- GPT translation -->
    - **Tot en met**: Voer 12:00 uur in. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

## Beschikbaarheden kopiëren naar andere weken <!-- GPT translation -->

In de volgende subsecties wordt uitgelegd hoe je benhoudsafspraken door de weken kunt roteren om te plannen voor het volgende praktijkvoorbeeld of een soortgelijk gebruiksscenaria: <!-- GPT translation -->

- Je contactcenter is geopend van 8:00 tot 20:00 uur. <!-- GPT translation -->
- Planning eenheid A werkt in de even weken ochtenddiensten en planning eenheid B werkt avonddiensten. <!-- GPT translation -->
- In oneven weken werkt E met ochtenddiensten en werkt A met avonddiensten. <!-- GPT translation -->
- De ochtenddienst is van 08:00 tot 14:00 uur. <!-- GPT translation -->
- De late dienst is van 14:00 tot 20:00 uur. <!-- GPT translation -->

### Beschikbaarheidsmodellen aanmaken voor een bepaalde dag <!-- GPT translation -->

Ga naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs} en klik op het Nieuw-pictogram {% icon item-add | icon-only %} om {% link_new een dagmodel aan te maken | features/administration/daymodels/daymodel-creation.md %}.<br>In het volgende voorbeeld wordt uitgelegd hoe twee dagmodellen worden geconfigureerd om een *Ochtenddienst* en *Avonddienst* af te wisselen. <!-- GPT translation -->

Ga als volgt te werk om het dagmodel in te stellen voor de ochtendploeg: <!-- GPT translation -->

1. Maak een nieuw dagmodel aan. <!-- GPT translation -->
2. Stel het dagmodel in: <!-- GPT translation -->
    - **Type**: Selecteer **Beschikbaarheidsperiode**. <!-- GPT translation -->
    - **Naam** en **Afkorting**: Gebruik een unieke naam en afkorting, bijvoorbeeld: Beschikbaarheid 8&nbsp;AM - 2&nbsp;PM en Avail 8AM-2PM. <!-- GPT translation -->
    - (Optioneel) **Kleur**: Selecteer een kleur die je helpt om het dagmodel snel te vinden. <!-- GPT translation -->
    - **Begintijd beschikbaarheidsperiode**: Voer 08:00 in. <!-- GPT translation -->
    - **Einde beschikbaarheidsperiode**: Voer 14:00 in.<br> Of stel de **Beschikbaarheidsperiode Duur** in. De maximale waarde is 48 uur. <!-- GPT translation -->
3. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Volg deze stappen om het dagmodel in te stellen voor de avonddienst: <!-- GPT translation -->

1. Maak een nieuw dagmodel aan. <!-- GPT translation --> <!-- Repetition of GPT translation -->
2. Stel het dagmodel in: <!-- GPT translation --> <!-- Repetition of GPT translation -->
    - **Type**: Selecteer **Beschikbaarheidsperiode**. <!-- GPT translation --> <!-- Repetition of GPT translation -->
    - **Naam** en **Afkorting**: Voer een unieke naam en afkorting in, bijvoorbeeld: Hele dag, OF Afdeling. <!-- GPT translation -->
    - (Optioneel) **Kleur**: Selecteer een kleur die je helpt om het dagmodel snel te vinden. <!-- GPT translation --> <!-- Repetition of GPT translation -->
    - **Begintijd Beschikbaarheidsperiode**: Voer 14:00 in. <!-- GPT translation -->
    - **Einde beschikbaarheidsperiode**: Voer 20:00 in.<br> Je kunt ook de **Beschikbaarheidsperiode** instellen. De maximale waarde is 48 uur. <!-- GPT translation -->
3. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

### Een dienstenserie aanmaken en toewijzen <!-- GPT translation -->

Volg deze stappen om de twee dagmodellen die je zojuist hebt gemaakt, te gebruiken voor het plannen: <!-- GPT translation -->

1. {% link_new Maak een dienstenserie aan | features/administration/shift-sequences.md | #dienstenseries-aanmaken %} met twee **Ledenregels** en een **Looptijd** van 14 dagen.<br> <!-- GPT translation -->
2. Voeg in de dienstenserie achtereenvolgens dagmodellen toe, beginnend met de ochtend op maandag in week 1. Begin in rij 1 met het ochtenddagmodel in week 1 en kies in week 2 een avonddienst. Begin in rij 2 met de diamodellen in omgekeerde volgorde. <!-- GPT translation -->
3. Wijs de dienstenserie 3-OPERA-JAMEL aan je medewerkers toe: <!-- GPT translation -->
    - Selecteer de eerste personeelsregel voor medewerkers in eenheid A. <!-- GPT translation -->
    - Selecteer de tweede medewerkersregel voor medewerkers in eenheiden van niveau B. <!-- GPT translation -->
    - Stel een **referentiedatum** in om aan te geven vanaf welke datum de dienstenserie moet worden ingepland. Stel de referentiedatum in op de weekdag waarop je planningsweek begint, zoals bijvoorbeeld maandag. <!-- GPT translation -->
4. {% link_new Voeg de dienstenserie toe | features/scheduling/schedules/schedules-insert-shift-sequences.md | #dienstenseries-toevoegen %} aan je planning. <!-- GPT translation -->

## Medewerkers met een tijdelijke beschikbaarheid configureren <!-- GPT translation -->

Voorbeeld: Een van je medewerkers is op een bepaalde weekdag alleen beschikbaar van 9:00 tot 12:00 uur.<br>Om hun beschikbaarheid juist in te stellen, volg je de instructies om [in te stellen dat hij op bepaalde dagen/tijden is ingepland](#gespecificeerde-werktijden). Voeg de betreffende {% link_new geldigheidsperiode | features/administration/set-a-validity-period.md %} toe met de juiste waarden voor **Vanaf** en **Tot en met**. <!-- GPT translation -->

## Beschikbaarheid bewerken <!-- GPT translation -->

Je kunt de beschikbaarheidsinstellingen aanpassen die je voor een afzonderlijke medewerker hebt geconfigureerd. <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- TM 100 -->
2. Selecteer de medewerker voor wie je de beschikbaarheid wilt bewerken. <!-- GPT translation -->
3. Klik in het rechter zijpaneel op **Beschikbaarheid**. <!-- GPT translation -->
4. Klik naast de beschikbaarheidsinstelling die je wilt bewerken op het {% icon pencil | pencil-icon %}. <!-- GPT translation -->
5. Bewerk de beschikbaarheid. <!-- GPT translation -->
6. Klik in het venster **Beschikbaarheid bewerken** op _OK_{:.doc-button}. <!-- GPT translation -->
7. Klik op _OK_{:.doc-button} onderaan het rechterpaneel. <!-- GPT translation -->

Als je beschikbaarheden hebt geconfigureerd met dagmodellen van het type **Inroosterperiode**, bewerk dan het betreffende dagmodel: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs}. <!-- GPT translation -->
2. Selecteer het dagmodel dat je wilt bewerken. <!-- GPT translation -->
3. Bewerk het dagmodel. <!-- GPT translation -->
4. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Je kunt ook beschikbaarheden bewerken in het Diensten-Center. Lees meer over {% link_new hoe je beschikbaarheden toevoegt en verwijdert in Diensten-Center | features/scheduling/shiftcenter/add-and-delete-items.md | #beschikbaarheid-toevoegen %}. Tijdelijke wijzigingen kun je kopiëren en plakken van je dagmodelbeschikbaarheden naar een cel, om deze daarna in handmatig toegevoegde beschikbaarheden te wijzigen. <!-- GPT translation -->

In het Dienstrooster-Center worden beschikbaarheden op elk weergegeven niveau met een `<>`-symbool weergegeven. Beweeg de muis over het symbool om de details te bekijken. In de dagcellen worden beschikbaarheden als oranje elementen weergegeven. In uitgebreide dagcellen worden de beschikbaarhheiden van je medewerkers met oranje onderstreepte witte staven weergegeven. <!-- GPT translation -->

## Beschikbaarheden verwijderen <!-- GPT translation -->

Je kunt de beschikbaarheidsconfiguraties verwijderen die je hebt aangemaakt voor een individuele medewerker. <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- TM 100 -->
2. Selecteer de medewerker waarvoor je de beschikbaarheid wilt verwijderen. <!-- GPT translation -->
3. Klik in het rechter zijpaneel op **Beschikbaarheid**. <!-- GPT translation --> <!-- Repetition of GPT translation -->
4. Klik naast de beschikbaarheid die je wilt verwijderen op het pictogram Verwijderen {% icon item-delete | icon-only %}. <!-- GPT translation -->
5. Klik in het venster **Bevestiging** op _Ja_{:.doc-button}. <!-- GPT translation -->
6. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Als je beschikbaarheden hebt geconfigureerd met dagmodellen van het type **Beschikbaarheidsperiode**, verwijder dan eerst het dagmodel: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs}. <!-- GPT translation --> <!-- Repetition of GPT translation -->
2. Selecteer het dagmodel dat je wilt verwijderen. <!-- GPT translation -->
3. Klik op het pictogram Verwijderen {% icon item-delete | icon-only %} in de actiebalk. <!-- GPT translation -->
4. Klik in het venster **Bevestiging** op _Ja_{:.doc-button}. <!-- GPT translation -->

## Beschikbaarheden in injixo Me <!-- GPT translation -->

In injixo Me kunnen **medewerkers zelf hun eigen beschikbaarheid** toevoegen. Ze kunnen maximaal 14 beschikbaarheden toevoegen. Voor het maken van een planning dienen plannners alle overbodige vermeldingen uit de lijst te verwijderen om te voorkomen dat er potentieel planningsfouten optreden. <!-- GPT translation -->

Volg deze stappen om medewerkers in injixo Me toegang te verlenen om hun eigen beschikbaarheid toe te voegen: <!-- GPT translation -->

1. Ga naar **Me**. <!-- GPT translation -->
2. Schakel de optie **Beschikbaarheden** in. <!-- GPT translation -->

Medewerkers kunnen in Me hun weekbeschikbaarheid toevoegen en bewerken. Hun beschikbaarheid wordt in hun configuratiegegevens weergegeven. <!-- GPT translation -->