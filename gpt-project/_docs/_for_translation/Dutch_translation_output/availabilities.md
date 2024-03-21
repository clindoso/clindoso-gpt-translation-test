---
title: Beschikbaarheden
product_label:
  - advanced
  - enterprise
  - classic
description: Maak herbruikbare beschikbaarheden aan om tijdsperiodes te definiëren, tijdens welke medewerkers kunnen worden ingepland.
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

Beschikbaarheden stellen de niet- of gedeeltelijke beschikbaarheid van medewerkers op bepaalde dagen of tijden tijdens de planning vast. Ze beperken de reeds gedefinieerde beperkingen van de openingsuren en contracten van je medewerkers. <!-- GPT translation -->

Je kunt alleen een dienst of activiteit toevoegen in de planning als deze binnen het geconfigureerde tijdsbestek past. Personen zonder geconfigureerde beschikbaarheid worden geacht om tijdens je (geconfigureerde) openingstijden altijd beschikbaar te zijn. <!-- GPT translation -->

Zo kunnen beschikbaarheden worden gebruikt voor: <!-- GPT translation -->

- Vaste werkdagen/-tijden voor elke week configureren <!-- GPT translation -->
- Beschikbaarhheidsdiensten heen en weer 'schuiven' tussen weken. <!-- GPT translation -->
- tijdelijk beschikbare medewerkers configureren <!-- GPT translation -->

injixo houdt bij het maken van geoptimaliseerde planningen standaard rekening met de beschikbaarheid. Availabilities worden niet meegenomen bij het genereren van diensten, maar pas op het moment dat diensten worden toegewezen. <!-- GPT translation -->

injixo houdt alleen rekening met de beschikbaarheden als de planningregel _2611_{:.id-label} is geactiveerd. Schakel deze regel uit om agenten diensten te laten aanvragen en toewijzen die langer zijn dan hun beschikbaarheid. <!-- GPT translation -->

In injixo Me kun je de configuratie 'Achteraf verwijderen' activeren, waardoor medewerkers verwijderde beschikbaarheden tijdens het werken gelijk kunnen 'afmelden'. <!-- GPT translation -->

## Beschikbaarheden configureren <!-- GPT translation -->

Je kunt de beschikbaarheid op twee manieren configureren: <!-- GPT translation -->

- Persoonlijke beschikbaarheden: Je kunt tijdelijke of permanente medewerkersbeschikbaarheden opzetten aan de hand van het pad _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. <!-- GPT translation -->
- Dagmodelbeschikbaarheden: Voeg beschikbaarheid toe aan dienstenseries om dezelfde beschikbaarheid aan meerdere werknemers toe te kennen. <!-- GPT translation -->

Opmerking: Dagmodelbeschikbaarheden overschrijven beschikbaarheden die voor een enkele medewerker gelden en handmatig zijn toegevoegd. <!-- GPT translation -->

## Een vast weekmodel met werktijden/configureren <!-- GPT translation -->

Voorbeeld: Een medewerker is vanwege zorgtaken op woensdag en vrijdag alleen 's ochtends vanaf 8:00 uur tot 12:00 uur beschikbaar voor werk. Je kunt als volgt de beschikbaarheid van deze medewerker configureren: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}.
2. Selecteer de naam van de medewerker in de lijst. <!-- GPT translation -->
3. Klik rechts op het **Beschikbaarheid**-gedeelte op het pictogram Nieuw toevoegen {% icon item-add | icon-only %}. <!-- GPT translation -->
4. Configureer de beschikbaarheid: <!-- GPT translation -->
    - (Optioneel) **Geldig vanaf** en **Geldig tot en met**: Als deze beschikbaarheid alleen op een bepaalde datumbereik van toepassing is, dan beperken deze datums de {% link_new geldigheidsperiode | features/administration/set-a-validity-period.md %} van de beschikbaarheid. <!-- GPT translation -->
    - **Dagtypes**: Selecteer Woensdag en Vrijdag. Druk op CTRL om meerdere items te selecteren. <!-- GPT translation -->
    - **Vanaf**: Voer 8:00 in. <!-- GPT translation -->
    - **Tot en met**: Voer 12:00 in. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}.

## Beschikbaarheden roteren over weken <!-- GPT translation -->

In de onderstaande subsecties lees je hoe je inzetbaarheden kunt gebruiken om een planning te maken voor het volgende voorbeeld, of voor soortgelijke usecases: <!-- GPT translation -->

- je contactcenter is open van 8.00 - 20.00 uur. <!-- GPT translation -->
- Tijdens even weken werkt eenheden A de ochtenddienst en eenheid B de avonddienst. <!-- GPT translation -->
- In oneven weken werkt eenheid B ochtenddiensten en eenheid A avonddiensten. <!-- GPT translation -->
- De ochtendploeg werkt van 8:00 tot 14:00 uur. <!-- GPT translation -->
- De late dienst is van 14:00 tot 20:00 uur. <!-- GPT translation -->

### Dagmodellen Beschikbaarheid aanmaken <!-- GPT translation -->

Ga naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs} en klik op het pictogram **Nieuw** {% icon item-add | icon-only %} om {% link_new een dagmodel aan te maken | features/administration/daymodels/daymodel-creation.md %}.<br>In het volgende voorbeeld wordt uitgelegd hoe je twee dagmodellen instelt, zodat een ochtend- en avonddienst afwisselend worden toegewezen. <!-- GPT translation -->

Ga als volgt te werk om het dagmodel voor de ochtenddienst te configureren: <!-- GPT translation -->

1. Maak een nieuw dagmodel aan. <!-- GPT translation -->
2. Stel het dagmodel in: <!-- GPT translation -->
    - **Type**: Selecteer **Beschikbaarheidsperiode**. <!-- GPT translation -->
    - **Naam** en **Afkorting**: Voer een unieke naam en afkorting in, bijvoorbeeld Beschikbaarheid 8&nbsp;AM - 2&nbsp;PM en Besch 8AM-2PM. <!-- GPT translation -->
    - (Optioneel) **Kleur**: Selecteer een kleur om het dagmodel gemakkelijker te kunnen vinden. <!-- GPT translation -->
    - **Begin Beschikbaarheidsperiode**: Voer 8:00 in. <!-- GPT translation -->
    - **Einde beschikbaarheidskader**: Voer 14:00 in.<br> Je kunt ook de optie **Duur van het-beschikbaarheidkader instellen**. De maximale waarde is 48 uur. <!-- GPT translation -->
3. Klik op _OK_{:.doc-button}.

Volg deze stappen om het dagmodel voor de avonddienst in te stellen: <!-- GPT translation -->

1. Maak een nieuw dagmodel aan. <!-- Repetition of GPT translation -->
2. Stel het dagmodel in: <!-- Repetition of GPT translation -->
    - **Type**: Selecteer **Beschikbaarheidsperiode**. <!-- Repetition of GPT translation -->
    - **Naam** en **Afkorting**: Voer een unieke Naam en afkorting in, bijv. Beschikbaarheid: 14:00 - 20:00 uur en Besch. 14-20 uur. <!-- GPT translation -->
    - (Optioneel) **Kleur**: Selecteer een kleur om het dagmodel gemakkelijker te kunnen vinden. <!-- Repetition of GPT translation -->
    - **Start Beschikbaarheidsperiode**: Voer 14:00 uur in. <!-- GPT translation -->
    - **Einde beschikbaarheidsperiode**: Voer 20:00 in.<br> Je kunt deze limiet ook in **Beschikbaarheidsperiode duur (optioneel)** instellen. De maximale waarde is 48 uur. <!-- GPT translation -->
3. Klik op _OK_{:.doc-button}.

### Een dienstenserie aanmaken en toewijzen <!-- GPT translation -->

Volg deze stappen om de twee dagmodellen die je zojuist hebt aangemaakt te gebruiken voor het plannen: <!-- GPT translation -->

1. {% link_new Maak een dienstenserie aan met twee **Medewerkers-rijen** en een **Duur** van 14 dagen.<br> <!-- GPT translation -->
2. Voeg de dagmodellen op elkaar afwisselend toe aan de dienstenserie. Selecteer in rij 1 het model Ochtenddienst in week 1, en het model Middagdienst in week 2. Voeg de modellen in omgekeerde volgorde toe in rij 2. <!-- GPT translation -->
3. {% link_new Wijs de dienstenserie toe | features/administration/employee-overview.md | #dienstenseries-toewijzen %} aan je medewerkers: <!-- GPT translation -->
    - Selecteer de eerste rij in de tabel. <!-- GPT translation -->
    - Selecteer de tweede medewerkersregel voor medewerkers toegewezen aan eenheid B. <!-- GPT translation -->
    - Gebruik een **verwante datum** om te bepalen vanaf welke datum de dienstenserie moet worden gepland. Stel de referentiedatum in op de dag van de week waarop je roosterweek begint, bijvoorbeeld maandag. <!-- GPT translation -->
4. {% link_new Voer de dienstenserie toe | features/scheduling/schedules/schedules-insert-shift-sequences.md | #dienstenseries-toevoegen %}. <!-- GPT translation -->

## Tijdelijk beschikbare medewerkers configureren <!-- GPT translation -->

Voorbeeld: Een van je medewerkers is in een bepaalde week alleen beschikbaar van 9.00 tot 12.00 uur.<br>Volg de stappen om datums/tijden in te stellen als [weekdagen/tijden met weekfixaties](#weekdagen-inclusief-tijden-met-weekfixaties-instellen). Voeg de relevante geldigheidsperiode toe en ingesteld de juiste **Vanaf**- en **Tot_en_met**-waarden. <!-- GPT translation -->

## Beschikbaarheid bewerken <!-- GPT translation -->

Je kunt de beschikbaarhheid bewerken die je voor een afzonderlijke medewerker hebt geconfigureerd: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}.
2. Selecteer de medewerker voor wie je de beschikbaarheid wilt bewerken. <!-- GPT translation -->
3. Klik in het rechter zijpaneel op **Beschikbaarheid**. <!-- GPT translation -->
4. Klik naast **Beschikbaarheid bewerken** op het {% icon pencil 16px %}. <!-- GPT translation -->
5. Bewerk de beschikbaarheid. <!-- GPT translation -->
6. Klik in de sectie **Beschikbaarheid** op _OK_{:.doc-button}. <!-- GPT translation -->
7. Klik in de **Beschikbaarheid**-venster op _OK_{:.doc-button}. <!-- GPT translation -->

Als je beschikbaarheden hebt geconfigureerd met dagmodellen van het type **Beschikbaarheidsperiode**, bewerk dan het dagmodel: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs}. <!-- GPT translation -->
2. Selecteer het dagmodel dat je wilt bewerken. <!-- GPT translation -->
3. Bewerk het dagmodel. <!-- GPT translation -->
4. Klik op _OK_{:.doc-button}.

Je kunt ook beschikbaarheid bewerken in Dienstrooster-Center. Lees meer over {% link_new  hoe je plaasten toevoegt en verwijdert in Dienstrooster-Center | features/scheduling/shiftcenter/add-and-delete-items.md | #beschikbaarheid-toevoegen %}. tijdelijke wijzigingen kun je als volgt aanbrengen: Je kopieert persoonlijke en dagmodelbeschikbaarheden naar een cel om deze om te zetten naar handmatig toegevoegde beschikbaarheden. <!-- GPT translation -->

In het Dienstrooster-Center worden de beschikbaarhheidsniveaus weergegeven met een `<>`-symbool. Beweeg de muis over het symbool om de details te bekijken. In het weergavekader van de dag worden de beschikbaarheden weergegeven als oranje elementen. In het uitgeklapte celbereik worden de beschikbaarheden van medewerkers weergegeven als witte balken met een oranje streep eronder. <!-- GPT translation -->

## Beschikbaarheden verwijderen <!-- GPT translation -->

Je kunt de beschikbaarhheidsinstellingen verwijderen die je voor een afzonderlijke medewerker hebt ingevoerd. <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}.
2. Selecteer de medewerker bij wie je de beschikbaarheid wilt verwijderen. <!-- GPT translation -->
3. Klik in het rechter zijpaneel op **Beschikbaarheid**. <!-- Repetition of GPT translation -->
4. Klik naast de beschikbaarheid die je wilt verwijderen op het pictogram Verwijderen {% icon item-delete | icon-only %}. <!-- GPT translation -->
5. Klik in het venster **Bevestigen** op _Ja_{:.doc-button}. <!-- GPT translation -->
6. Klik op _OK_{:.doc-button}.

Als je beschikbaarheden hebt ingesteld met dagmodellen van het type **Tijdperiode beschikbaarheid**, verwijder dan het dagmodel: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Dagmodellen_{:.breadcrumbs}. <!-- Repetition of GPT translation -->
2. Selecteer het dagmodel dat je wilt verwijderen. <!-- GPT translation -->
3. Klik in de actiebalk op het pictogram Dagmodel verwijderen {% icon item-delete | icon-only %}. <!-- GPT translation -->
4. Klik in het venster **Bevestiging** op _Ja_{:.doc-button}. <!-- GPT translation -->