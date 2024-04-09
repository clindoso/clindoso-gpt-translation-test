---
title: Workloads aanmaken <!-- TM 100 -->
redirect_from:
  - /workloads/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Maak workloads aan die het historische en voorspelde contactvolume en AHT weergeven. Kom meer te weten over de verschillende workloadtypen. <!-- TM 100 -->
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
gpt_translation: true
---

Ga naar _Forecast_{:.breadcrumbs} om workloads aan te maken, te bewerken of te verwijderen. <!-- TM 100 -->

Workloads koppelen de toegangskanalen van je externe systeem met daarin de gegevens van je klantinteracties. Op basis van de geïmporteerde contactgegevens die in queues zijn opgeslagen, berekent injixo Forecast een workloadforecast voor je. Configureerbare gebeurtenissen, feestdagen of openingstijden beïnvloeden het forecastresultaat. Tevens is het mogelijk om je {% link_new forecast te importeren | features/forecast/injixo-forecast/import-forecast.md %} in workloads. <!-- GPT translation -->

In workloads configureer je de berekening van de personeelsbehoefte. De personeelsbehoefte is nodig voor planningsdoeleinden. <!-- TM 100 -->

Ben je nog niet zo vertrouwd met injixo Forecast? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}. <!-- TM 100 -->

## Vereisten <!-- TM 100 -->

- Voeg {% link_new een native of CSV-integratie | features/acd-integration/cloud/how-integrations-work.md %} toe en importeer historische gegevens voor minstens een queue. <!-- TM 100 -->
- Importeer aangeboden contacten, gemiddelde afhandeltijd (AHT), en afgehandelde contacten. Voor workloads met meerdere queues moet in de afgehandelde contacten de AHT en de berekende gewogen gemiddelden worden weergegeven. <!-- TM 100 -->

injixo maakt queues aan op basis van de gegevens die door een integratie zijn geïmporteerd. Het interval van de gegevensimport bepaalt het interval van de queues die op basis van deze gegevens worden aangemaakt. Je kunt alleen queues met hetzelfde interval aan een workload toevoegen. <!-- TM 100 -->

## Queues en kanalen <!-- TM 100 -->

Contactgegevens die door een integratie worden geïmporteerd, worden opgeslagen in queues. Deze queues zijn altijd gekoppeld aan een kanaal. Als je [workloads aanmaakt](#workloads-aanmaken) kun je queues filteren op kanaal en ze aan de workload toevoegen. Native integraties stellen automatisch het kanaal in voor queues. Niet alle integraties ondersteunen alle kanalen. <!-- TM 100 -->
Voor een CSV-integratie moet je het kanaal handmatig instellen. Je kunt een kanaal per kolom toevoegen of één kanaal selecteren voor het bestand wanneer je {% link_new de kolommen van een CSV-bestand toewijst | features/acd-integration/cloud/add-csv-integration.md | #de-kolommen-toewijzen %}. <!-- TM 100 -->

De volgende kanalen worden door integraties ondersteund: <!-- TM 100 -->

- Gesprekken <!-- TM 100 -->
- Chats <!-- TM 100 -->
- E-mails <!-- TM 100 -->
- Cases <!-- TM 100 -->
- Documenten <!-- TM 100 -->
- Sociale media <!-- TM 100 -->

injixo Forecast groepeert queues per kanaal. Je kunt alleen queues met hetzelfde interval aan een workload toevoegen. <!-- TM 100 -->

## Workloads en Queues <!-- GPT translation -->

Hoeveel workloads je configureert en hoeveel queues je aan elke workload toevoegt, is volledig afhankelijk van de behoeften van je bedrijf. Je moet je afvragen of je een aparte volume-, AHT- en personeelsbehoefteberekening voor elke queue nodig hebt. <!-- GPT translation -->

Bekijk het volgende voorbeeld: <!-- GPT translation -->

Je hebt vijf queues in je ACD-systeem geconfigureerd: <!-- GPT translation -->

- Support Tier 1 <!-- GPT translation -->
- Support Tier 2 <!-- GPT translation -->
- Product Sales North <!-- GPT translation -->
- Product Sales Central <!-- GPT translation -->
- Product Sales Zuid <!-- GPT translation -->

In dit voorbeeld verwijzen de drie product-sales-queues naar verschillende regio's binnen een land met daarbij een voertaal. Daardoor zijn mensen die ervaren zijn in het beantwoorden van verkoopgerelateerde vragen in staat om de verkoop te stimuleren, ongeacht waar het contact vandaan komt. Het kan eventueel zritig zijn om de sales-queues op regio te splitsen, bijvoorbeeld om marketingcampagnes of andere metrieken te monitoren, maar het is niet nodig om de contactvolumes en personeelsbehoefte van het ene naar het andere gebied te forecasten. Je kunt (één workload aanmaken)[#workloads-aanmaken] met de naam Product Sales en in de sectie **Queues toewijzen** alle drie de Product Sales-queues selecteren. <!-- GPT translation -->

Dat is bij supportvragen met een hoge prioriteit, ongeacht of het een 'Tier 1' of 'Tier 2' supportvraag betreft, anders. Tier 1-supportvragen komen vaker voor en zijn gemakkelijker af te handelen dan Tier 2-supportvragen. Medewerkers die Tier 1-supportvragen afhandelen zijn niet per se ook opgeleid om Tier 2-supportvragen te beantwoorden. Omdat Tier 2-supportvragen bovendien minder vaak voorkomen, heb je minder personeel nodig om deze af te handelen. 

Hier stel je [twee workloads](#workloads-aanmaken) in, Support Tier 1 en Support Tier 2 en wijs je de juiste queue aan elke workload toe. Het is aan te raden om medewerkers die verantwoordelijk zijn voor Tier 2 op de lange termijn ook Tier 1-verzoeken met een lagere prioriteit te laten behandelen, houd de beide workloads dan gescheiden en gebruik een {% link_new Multi-activiteit | features/administration/activity-types-and-properties.md | #subactivities %} voor het plannen. <!-- GPT translation -->

<!-- anchor for intercom forecast tour -->

## Workloads aanmaken <!-- TM 100 -->

Maak voor elke activiteit die je op basis van personeelsbehoefte wilt plannen, een afzonderlijke workload aan. Multiactivities vereisen een workload voor de multiactivity en een workload voor elke deelactiviteit. <!-- GPT translation -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op _Nieuwe workload_{:.doc-button} boven aan de lijst. <!-- GPT translation -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 100 -->

   - **Naam**: Unieke naam om je werklast te herkennen. <!-- TM 100 -->
   - **Tijdzone**: De {% link_new tijdzone | best-practices/working-with-timezones.md %} voor de workload kan later niet worden bewerkt. <!-- TM 100 -->

     > Opmerking <!-- TM 100 -->
     >
     > - Om de personeelsbehoefte voor een eenheid op te slaan, moet de tijdzone van de workload overeenkomen met de tijdzone van de eenheid. <!-- TM 100 -->
     > - Als je een andere tijdzone voor je workload hebt ingesteld dan voor de integratie weermee je gegevens importeert, worden de geïmporteerdegegevens met tijdsverschuiving in de workload weergegeven. Als voor een CSV-integratie bijvoorbeeld UTC-tijd is ingesteld en je voor je workload CEST-tijd (UTC +2 uur), worden de geïmporteerde gegevens van 8:00 uur in de workload weergegeven om 10:00 uur. <!-- TM 100 -->

   - (Optioneel) **Feestdagregio**: Inclusief nationale feestdagen die invloed kunnen hebben op je forecast. <!-- GPT translation -->
   - (Optioneel) **Eenheid** en **Activiteit**: Vereist om {% link_new openingstijden te activeren | features/forecast/injixo-forecast/forecast-activate-business-hours.md %} in de sectie **Openingstijden**. <!-- TM 100 -->

3. (alleen injixo Classic) Selecteer een optie uit de sectie **Prijsmodel**: <!-- TM 100 -->

   - **Live-modus** (betaald): Maandelijks gefactureerd. Kan niet worden teruggedraaid naar de Testmodus. <!-- TM 100 -->
   - **Testmodus** (gratis): Je kunt alleen forecasts bekijken en geen personeelsbehoeften overdragen voor planningsdoeleinden. <!-- TM 100 -->

4. Selecteer de queues voor je workload in de sectie **Queues toewijzen**. <!-- TM 100 -->

   Om het aantal weergegeven queues te verkleinen: <!-- TM 100 -->

   - Filter de queues op kanaal (gesprekken, chats, enz.). <!-- TM 100 -->
   - Vink de selectievakjes voor geselecteerde, niet-geselecteerde of inactieve queues aan. Inactieve queues zijn queues die geïmporteerd zijn door integraties die verwijderd zijn. <!-- TM 100 -->
   - Gebruik het zoekveld boven de tabel. Je kunt zoeken op de naam van de queue, de integratie of de workload. <!-- TM 100 -->

   Opmerking: Als het interval of kanaal van een queue niet overeenkomt met het interval of kanaal van de geselecteerde queue, worden alle queues die niet overeenkomen, uitgegrijsd. <!-- TM 100 -->

5. Klik op _Workload aanmaken_{:.doc-button}. <!-- TM 100 -->

   De pagina geeft historische gegevens en een voorlopige versie van de forecast weer.   <!-- GPT translation -->
   Nadat de berekening is voltooid, laad je de pagina opnieuw om de definitieve prognoseversie te zien. <!-- GPT translation -->
   De nieuwe workload wordt weergegeven in de lijst met workloads. <!-- TM 100 -->

Als je injixo Essential gebruikt, kun je Basic workloads aanmaken. Voor Basic workloads zijn minimaal twee weken aan historische gegevens nodig. Openingstijden worden niet ondersteund door Basic workloads. <!-- TM 100 -->

Als je injixo Advanced of Enterprise WFM gebruikt, kun je Smart workloads aanmaken. Smart workloads genereren een forecast op de historische gegevens van slechts een dag. Openingstijden worden ondersteund door Smart workloads. <!-- TM 100 -->

Als je injixo Classic gebruikt, moet je daarnaast ook het forecastmodel (Smart of Basic) selecteren voor elke workload. Voor Smart workloads moet je kiezen tussen de Live-modus en de Testmodus. De Testmodus is gratis, maar laat je de forecast alleen bekijken. Je kunt geen personeelsbehoefte overdragen voor planningsdoeleinden. De Live-modus biedt de volledige functionaliteit en wordt maandelijks in rekening gebracht. Slimme workloads in de Live-modus kunnen niet worden teruggedraaid naar de Testmodus. <!-- TM 100 -->

<!-- hidden: feature not live yet -->
<!-- ## Create workloads without historical data

You only need an integration and historical data import if you want injixo to create forecasts. To add forecast data by {% link_new importing a forecast | features/forecast/injixo-forecast/import-forecast.md %} that has been generated externally or to {% link_new create constant staff requirements | features/forecast/requirement-scripts/requirement-constant.md %}, you can create a workload using the tab *Forecast Import*: <!-- TM 100 -->

1. Go to **Forecast**{:.breadcrumbs}. <!-- TM 100 -->
2. Click _Create Workload_{:.doc-button} in the upper right corner of the forecast page. <!-- TM 100 -->
3. In the *Basic configuration* section, enter a **Name** for your new workload. <!-- TM 100 -->
4. Select the **Time zone** to display data. Note: The set time zone must match the planning unit to save staff requirements. <!-- TM 100 -->
5. (Optioneel) Selecteer de **Feestdageregio** om rekening te houden met alle nationale feestdagen die van invloed zijn op je forecast voor het hele jaar. <!-- GPT translation -->
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements. <!-- TM 100 -->
    {{ 4 | image: 'Import Workload basic configuration section' }} <!-- TM 100 -->
7. Click the tab **Forecast import**. <!-- TM 100 -->
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file. <!-- TM 100 -->
    {{ 5 | image: 'Import Workload parameters' }} <!-- TM 100 -->
9. Click *Create workload*{:.doc-button}. --> <!-- TM 100 -->

## Workloads bewerken <!-- TM 100 -->

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} een workload in de lijst of zoek op pagin… op workload-naam. <!-- GPT translation -->
2. Klik op het {% icon pencil | icon-only %} om de werkbelastinggegevens te bewerken.<br> <!-- GPT translation -->
   Je kunt queues toevoegen of verwijderen zonder dat je opnieuw gegevens hoeft te importeren. Weergegeven queues worden uitgegrijsd als hun interval of kanaal niet overeenkomt met eerder toegewezen queues. <!-- TM 100 -->
3. Klik op _Workload opslaan_{:.doc-button}.   <!-- GPT translation -->
   Op basis van de nieuwe configuratie wordt de forecast mogelijk bijgewerkt. <!-- TM 100 -->

## Workloads verwijderen <!-- TM 100 -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op het {% icon trash %} naast de workload die je wilt verwijderen. <!-- GPT translation -->
2. Klik in het bevestigingsvenster op _Workload verwijderen_ {:.doc-button}. <!-- GPT translation -->
   injixo de bijbehorende historische gegevens op. Voeg de queue(‘s) opnieuw aan een andere Workload toe om de gegevens opnieuw te gebruiken. <!-- GPT translation -->

## Door workloads navigeren <!-- GPT translation -->

In _Forecast > Workloads_{:.breadcrumbs} selecteer je een workload om de pagina met workloadgegevens te openen. De pagina bevat de volgende drie secties: <!-- GPT translation -->

- De sectie Volume <!-- GPT translation -->
- De sectie **Gemiddelde afhandeltijd (AHT)** <!-- GPT translation -->
- De sectie **Afhandelingscapaciteit** <!-- GPT translation -->

Elke sectie bevat een diagram en bewerkingsfunctionaliteiten. <!-- GPT translation -->

De grafieken tonen standaard gegevens van de huidige week. <!-- GPT translation -->

- Gebruik het vervolgkeuzemenu Datumkiezer om een andere tijdsperiode te selecteren. Klik op een weeknummer om de hele week te selecteren, of klik op een dag en sleep vervolgens om een kortere of langere periode te selecteren. <!-- GPT translation -->
- Gebruik de knoppen _<_ (Vorige){:.doc-button} en _>_ (Volgende){:.doc-button} om naar datums in het verleden en de toekomst binnen de geselecteerde periode te navigeren. <!-- GPT translation -->

### De sectie Volume <!-- GPT translation -->

De grafiek in de sectie Volume geeft het contactvolume weer op basis van historische gegevens, geïmporteerde forecasts en gegenereerde forecasts. <!-- GPT translation -->
Beweeg de cursor over de grafiek voor informatie over het volume, de geschatte AHT, personeelsbehoefte, handmatige aanpassingen en toegevoegde gebeurtenissen.<br> <!-- GPT translation -->
Lees hoe je de {% link_new Volumecurve aanpast | features/forecast/injixo-forecast/manual-adjustments.md | #het-volume-aanpassen%}. <!-- GPT translation -->

### De sectie AHT <!-- GPT translation -->

De sectie AHT is standaard verborgen wanneer je de pagina met workloaddetails opent of opnieuw laadt. Klik op het pictogram Oog om de sectie AHT weer te geven. <!-- GPT translation -->
De AHT-grafiek is alleen beschikbaar voor workloads met queues die AHT-gegevens bevatten.<br> <!-- GPT translation -->
Lees eerst hoe je de {% link_new AHT aanpast | features/forecast/injixo-forecast/manual-adjustments.md | #aht-aanpassen %}. <!-- GPT translation -->

### De sectie Personeelsbehoefte <!-- GPT translation -->

In de sectie Behoefte aan personeel wordt de berekende personeelsbehoefte weergegeven in een grafiek. <!-- GPT translation -->
Onder de grafiek worden de geconfigureerde parameters voor de personeelsbehoefte en het totaal aantal gewerkte uren weergegeven. Beweeg de muis over de grafiek om gedetailleerde informatie weer te geven over het gemiddelde afhandelingsvolume, het volume, de personeelsbehoefte, enige handmatige aanpassingen en toegevoegde gebeurtenissen. <!-- GPT translation -->
Ontdek hoe je {% link_new de personeelsbehoefte voor het plannen gebruikt | features/forecast/injixo-forecast/calculate-staff-requirements.md | #use-staff-requirements-for-scheduling %}. <!-- GPT translation -->

## Veelgestelde vragen <!-- TM 100 -->

| Vraag                                     | Antwoord                                                                                                                                                                                                                                                                                                                                                       | <!-- GPT translation -->
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Waarom geven de grafieken op de pagina Workload geen gegevens weer? | injixo genereert een forecast 365 dagen na de laatste gegevensimport. Als de grafieken op een pagina Workload over een bepaald tijdsbestek in de toekomst geen gegevens weergeven, controleer dan in _Account > Integraties_{:.breadcrumbs} of er nog steeds gegevens geïmporteerd worden. Controleer eveneens of de juiste queues in de Workload zijn toegewezen in de workloadconfiguratie. | <!-- GPT translation -->