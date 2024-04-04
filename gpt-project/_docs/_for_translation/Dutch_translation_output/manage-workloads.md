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

Workloads stellen de inputkanalen van je externe systeem in kaart, waarin de gegevens van de interacties met je klanten worden opgeslagen. Op basis van de in het systeem geïmporteerde contactgegevens die in queues worden opgeslagen, berekent injixo Forecast een forecast voor de workload. Configurable events, feestdagen of openingstijden hebben invloed op het forecastresultaat. Je kunt tevens {% link_new je forecast importeren | features/forecast/injixo-forecast/import-forecast.md %} into workloads. <!-- GPT translation -->

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

## Workloads en queues <!-- GPT translation -->

Hoeveel workloads en queues je instelt, is volledig afhankelijk van de behoeften van je organisatie. Je moet overwegen of je afzonderlijke berekeningen voor volume, gesprekstijd en personeelsbehoefte voor elke queue nodig hebt. <!-- GPT translation -->

Bekijk het volgende voorbeeld: <!-- GPT translation -->

Je hebt vijf queues geconfigureerd in je ACD-systeem: <!-- GPT translation -->

* Support Tier 1 <!-- GPT translation -->
- Support Tier 2 <!-- GPT translation -->
- Verkoop Noord-West <!-- GPT translation -->
- Product Sales Central <!-- GPT translation -->
- Product Sales Zuid <!-- GPT translation -->

In dit voorbeeld verwijzen de drie product sales-queues naar verschillende regio's van een land en een voertaal. Dat betekent dat agents met de juiste kwalificaties op alle vragen gerelateerd aan verkoop kunnen antwoorden, ongeacht waar de lead vandaan komt. Het kan relevant zijn om de sales-queues per regio op te splitsen om marketingcampagnes of andere KPI's te volgen, maar het is niet nodig om contactvolumes en personeelsbehoefte per regio te forecasten. Je kunt [een workload aanmaken](#workloads-aanmaken) met de naam Product Sales en selecteer in de sectie **Queues toewijzen** alle drie de Product Sales-queues. <!-- GPT translation -->

In contrast, de contactvolumen en personeelsbehoefte voor supportvragen van niveau 1 moeten apart worden berekend. Vragen van niveau 1 zijn veel voorkomend en gemakkelijker te behandelen dan vragen van niveau 2. Medewerkers die goed zijn in het afhandelen van vragen van niveau 1, zijn niet per se geschikt voor het beantwoorden van vragen van niveau 2. Daarnaast, omdat vragen van niveau 2 minder vaak voorkomen, heb je minder medewerkers nodig om ze te kunnen afhandelen. Hier [maak je twee workloads aan](#workloads-aanmaken), Support Niveau 1 en Support Niveau 2 en wijst de toepasselijke queue toe aan elk van hen. Als je wilt dat de medewerkers die verantwoordelijk zijn voor niveau 2 ook niveau 1-vragen met een lagere prioriteit afhandelen, bewaar dan de twee van elkaar gescheiden workloads, en gebruik een {% link_new multiactiviteit | features/administration/activity-types-and-properties.md | #subactiviteiten %} voor de planning. <!-- GPT translation -->

<!-- anchor for intercom forecast tour -->

## Workloads aanmaken <!-- TM 100 -->

Maak voor elke activiteit die je met personeelsbehoefte wilt inplannen, een workload aan. Multiactiviteiten hebben een workload nodig voor de multiactiviteit en een workload voor elke deelactiviteit. <!-- GPT translation -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op de knop _Nieuwe workload_{:.doc-button} boven aan de lijst. <!-- GPT translation -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 100 -->

   - **Naam**: Unieke naam om je werklast te herkennen. <!-- TM 100 -->
   - **Tijdzone**: De {% link_new tijdzone | best-practices/working-with-timezones.md %} voor de workload kan later niet worden bewerkt. <!-- TM 100 -->

     > Opmerking <!-- TM 100 -->
     >
     > - Om de personeelsbehoefte voor een eenheid op te slaan, moet de tijdzone van de workload overeenkomen met de tijdzone van de eenheid. <!-- TM 100 -->
     > - Als je een andere tijdzone voor je workload hebt ingesteld dan voor de integratie weermee je gegevens importeert, worden de geïmporteerdegegevens met tijdsverschuiving in de workload weergegeven. Als voor een CSV-integratie bijvoorbeeld UTC-tijd is ingesteld en je voor je workload CEST-tijd (UTC +2 uur), worden de geïmporteerde gegevens van 8:00 uur in de workload weergegeven om 10:00 uur. <!-- TM 100 -->

   - (Optioneel) **Feestdagregio**: Houdt rekening met feestdagen die van invloed kunnen zijn op je forecast. <!-- GPT translation -->
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

   Op deze pagina worden historische gegevens en een voorlopige versie van de forecast weergegeven. <!-- GPT translation -->
   Wanneer de berekening is afgerond, moet je de pagina verversen om de uiteindelijke forecastversie te zien. <!-- GPT translation -->
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
5. (Optioneel) Selecteer de **Feestdagregio** om rekening te houden met alle feestdagen die invloed hebben op je forecast voor het komende jaar. <!-- GPT translation -->
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements. <!-- TM 100 -->
    {{ 4 | image: 'Import Workload basic configuration section' }} <!-- TM 100 -->
7. Click the tab **Forecast import**. <!-- TM 100 -->
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file. <!-- TM 100 -->
    {{ 5 | image: 'Import Workload parameters' }} <!-- TM 100 -->
9. Click *Create workload*{:.doc-button}. --> <!-- TM 100 -->

## Workloads bewerken <!-- TM 100 -->

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} een workload uit de lijst of voer de naam van de workload in in het zoekveld. <!-- GPT translation -->
2. Klik op het pictogram Potlood {% icon pencil | icon-only %} om de detailgegevens van de workload te bewerken. <!-- GPT translation -->
   Je kunt queues toevoegen of verwijderen zonder dat je opnieuw gegevens hoeft te importeren. Weergegeven queues worden uitgegrijsd als hun interval of kanaal niet overeenkomt met eerder toegewezen queues. <!-- TM 100 -->
3. Klik op _Workload opslaan_{:.doc-button}. <!-- GPT translation -->
   Op basis van de nieuwe configuratie wordt de forecast mogelijk bijgewerkt. <!-- TM 100 -->

## Workloads verwijderen <!-- TM 100 -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op het {% icon trash %} naast de workload die je wilt verwijderen. <!-- GPT translation -->
2. Klik in het venster op _Workload verwijderen_{:.doc-button}. <!-- GPT translation -->
   injixo slaat de gerelateerde historische gegevens op. Om de gegevens opnieuw te gebruiken, voeg je de queue(s) toe aan een andere workload. <!-- GPT translation -->

## Navigatie: Workloads <!-- GPT translation -->

Ga in _Forecast > Workloads_{:.breadcrumbs} naar een workload en selecteer deze om de pagina met workloadgegevens te openen. De pagina bestaat uit de volgende drie secties: <!-- GPT translation -->

- De sectie **Volume** <!-- GPT translation -->
- De sectie **AHT** <!-- GPT translation -->
- De sectie **Aantal krachten** <!-- GPT translation -->

Elke sectie bevat een grafiek en bewerkingsfunctionaliteiten. <!-- GPT translation -->

De grafieken tonen standaard gegevens van deze week. <!-- GPT translation -->

- Gebruik het datumkiezer om een andere tijdsperiode te selecteren. Klik op een weeknummer om de hele week te selecteren, of klik op een dag en sleep om een kortere of langere periode dan een week te selecteren. <!-- GPT translation -->
- Gebruik '<' en '>' om naar eerder en later in de geselecteerde tijdsperiode te navigeren. <!-- GPT translation -->

### De sectie Volume <!-- GPT translation -->

De grafiek in de sectie Volume geeft het contactvolume weer voor eerder geïmporteerde en gegenereerde forecasts. <!-- GPT translation -->
Beweeg de muisaanwijzer over de grafiek om gedetailleerde informatie weer te geven over de volume, AHT, personeelsbehoefte, handmatige aanpassingen en toegevoegde gebeurtenissen.<br> <!-- GPT translation -->
Lees hoe je het {% link_new volume aanpast | features/forecast/injixo-forecast/manual-adjustments.md | #het-volume-aanpassen%}. <!-- GPT translation -->

### De sectie AHT <!-- GPT translation -->

De sectie AHT is standaard verborgen als je de pagina met workload-details opent of herlaadt. Klik op het pictogram 're': {% icon eye_slash | close  %} om de sectie AHT weer te geven. <!-- GPT translation -->
De AHT-grafiek is alleen zichtbaar voor workloads met queues waarvoor AHT-gegevens beschikbaar zijn.<br> <!-- GPT translation -->
Lees hoe je de {% link_new AHT-aannames aanpast | features/forecast/injixo-forecast/manual-adjustments.md %}. <!-- GPT translation -->

### De sectie Personeelsbehoefte <!-- GPT translation -->

De grafiek in de sectie **Benodigde capaciteit** geeft de berekende personeelsbehoefte weer. <!-- GPT translation -->
Onder de grafiek zie je de geconfigureerde parameters voor de personeelsbehoefte en het totaal aantal personeelsuren. Beweeg de aanwijzer over de grafiek om gedetailleerde informatie te zien over het AHT, het volume, het personeelsaanbod en eventuele handmatige aanpassingen en toegevoegde gebeurtenissen. <!-- GPT translation -->
Lees hoe je {% link_new personeelsbehoefteberekeningen gebruikt voor het inplannen | features/forecast/injixo-forecast/calculate-staff-requirements.md | #het-gebruik-van-personeelsbehoefteberekeningen-voor-het-scheduling %}. <!-- GPT translation -->

## Veelgestelde vragen <!-- TM 100 -->

| Vraag                                     | Antwoord                                                                                                                                                                                                                                                                                                                                                       | <!-- GPT translation -->
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Waarom zijn de grafieken op een workloadpagina leeg? | injixo genereert een forecast tot 365 dagen na de laatste gegevensimport. Als de grafieken op een workloadpagina voor een bepaalde toekomstige periode geen gegevens weergeven, dan raden we aan om te controleren of je integratie nog wel gegevens blijft importeren. Ga naar _Account > Integraties_{:.breadcrumbs}. Daarnaast is het relevant om te controleren of de juiste queues aan de workload zijn toegewezen in de workload-configuratie. | <!-- GPT translation -->