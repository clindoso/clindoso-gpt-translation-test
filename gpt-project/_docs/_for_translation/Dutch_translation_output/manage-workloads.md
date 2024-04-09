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

De Workloads in injixo Forecast stellen de bronnen van je externe systeem (zoals e-mailadressen, WhatsApp-nummers, telefoonnummers, communicatiekanalen) voor, en slaan informatie over je klantinteracties op. Op basis van de geïmporteerde contactgegevens die in de queues zijn opgeslagen, berekent injixo's Forecast een workloadforecast. Bij de forecast-resultaten spelen configureerbare events, feestdagen, ad openingstijden een rol. Je kunt ook je forecast in de Workloads {% link_new importeren | features/forecast/injixo-forecast/import-forecast.md %}. <!-- GPT translation -->

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

Het aantal workloads dat je configureert en het aantal queues dat je aan elke workload toevoegt, hangt af van de behoeften van je organisatie. Je moet overwegen of je voor elke workload afzonderlijke volume-, AHT- en personeelsberekeningen nodig hebt. <!-- GPT translation -->

Neem het volgende voorbeeld in overweging: <!-- GPT translation -->

Je hebt in je ACD-systeem vijf queues geconfigureerd: <!-- GPT translation -->

- Supportniveau 1 <!-- GPT translation -->
- Support Tier 2 <!-- GPT translation -->
- Product Sales North <!-- GPT translation -->
- Product Sales Central <!-- GPT translation -->
- Product Sales Zuid <!-- GPT translation -->

In dit voorbeeld verwijzen de drie artikelverkoopqueues naar verschillende regio's in een land met een belangrijkste taal. Dat betekent dat agenten die sales-vragen kunnen beantwoorden dit kunnen doen, ongeacht de herkomst van het contact. Het kan zinvol zijn om de salesqueues per regio in te delen om het succes van marketingcampagnes en andere variabelen te volgen, maar het is niet nodig om forecastactiviteiten voor elk van de drie regio's uit te voeren. Je kunt [één workload](#workloads-aanmaken) aanmaken met de naam Product Sales en de drie Product Sales-queues selecteren in de sectie **Queues toewijzen**. <!-- GPT translation -->

Daarom moeten het volume en de personeelsbehoefte voor supportaanvragen afzonderlijk worden berekend. Tier 1- (eerste contact) aanvragen komen vaker voor en zijn eenvoudiger af te handelen dan Tier 2- (tweede contact) aanvragen. Medewerkers die met Tier 1-aanvragen om kunnen gaan, zijn niet noodzakelijk gekwalificeerd om Tier 2-aanvragen te beantwoorden. Omdat Tier 2-aanvragen bovendien minder vaak voorkomen, heb je minder medewerkers nodig om ze af te handelen. Hier maak je [twee workloads aan](#create-workloads), Support Tier 1 en Support Tier 2 en wees je voor elke workload de geschikte queue toe. Als je wilt dat medewerkers van het tweede echelon ook eerstelijnsvragen met een lagere prioriteit afhandelen, hou dan de twee workloads gescheiden en gebruik een {% link_new Subactiviteit | features/administration/activity-types-and-properties.md | #subactivities  %}voor de planning van meerdere activiteiten. <!-- GPT translation -->

<!-- anchor for intercom forecast tour -->

## Workloads aanmaken <!-- TM 100 -->

Maak voor elke activiteit die je met medewerkersbehoefte wilt plannen een workload aan. Multiactiviteiten vereisen een workload voor de multiactiviteit en een workload voor elke deelactiviteit. <!-- GPT translation -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op _Nieuwe workload aanmaken_ boven aan de lijst. <!-- GPT translation -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 100 -->

   - **Naam**: Unieke naam om je werklast te herkennen. <!-- TM 100 -->
   - **Tijdzone**: De {% link_new tijdzone | best-practices/working-with-timezones.md %} voor de workload kan later niet worden bewerkt. <!-- TM 100 -->

     > Opmerking <!-- TM 100 -->
     >
     > - Om de personeelsbehoefte voor een eenheid op te slaan, moet de tijdzone van de workload overeenkomen met de tijdzone van de eenheid. <!-- TM 100 -->
     > - Als je een andere tijdzone voor je workload hebt ingesteld dan voor de integratie weermee je gegevens importeert, worden de geïmporteerdegegevens met tijdsverschuiving in de workload weergegeven. Als voor een CSV-integratie bijvoorbeeld UTC-tijd is ingesteld en je voor je workload CEST-tijd (UTC +2 uur), worden de geïmporteerde gegevens van 8:00 uur in de workload weergegeven om 10:00 uur. <!-- TM 100 -->

   - (Optioneel) **Feestdag regio**: Omvat nationale feestdagen die van invloed kunnen zijn op je forecast. <!-- GPT translation -->
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

   Op deze pagina worden historische gegevens en een eerste versie van de forecast weergegeven. <!-- GPT translation -->
   Nadat de berekening is voltooid, kun je de pagina vernieuwen om de definitieve forecastversie te bekijken. <!-- GPT translation -->
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
5. (Optioneel) Selecteer de **Feestdageregio** om alle nationale feestdagen te laten gelden die van invloed zijn op je forecast voor een jaar. <!-- GPT translation -->
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements. <!-- TM 100 -->
    {{ 4 | image: 'Import Workload basic configuration section' }} <!-- TM 100 -->
7. Click the tab **Forecast import**. <!-- TM 100 -->
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file. <!-- TM 100 -->
    {{ 5 | image: 'Import Workload parameters' }} <!-- TM 100 -->
9. Click *Create workload*{:.doc-button}. --> <!-- TM 100 -->

## Workloads bewerken <!-- TM 100 -->

1. In *Forecast > Workloads*, selecteer je een workload in de lijst. Je kunt ook de naam van de workload in het zoekveld typen. <!-- GPT translation -->
2. Klik op het pictogram Bewerken {% icon pencil | icon-only  %} om de detailinstellingen voor de workload te wijzigen.<br> <!-- GPT translation -->
   Je kunt queues toevoegen of verwijderen zonder dat je opnieuw gegevens hoeft te importeren. Weergegeven queues worden uitgegrijsd als hun interval of kanaal niet overeenkomt met eerder toegewezen queues. <!-- TM 100 -->
3. Klik op _Workload opslaan_{:.doc-button}. <!-- GPT translation -->
   Op basis van de nieuwe configuratie wordt de forecast mogelijk bijgewerkt. <!-- TM 100 -->

## Workloads verwijderen <!-- TM 100 -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op het {% icon trash %} naast de workload die je wilt verwijderen. <!-- GPT translation -->
2. Klik in het bevestigingsvenster op _Workload verwijderen_{:.doc-button}. <!-- GPT translation -->
   injixo bewaart de gerelateerde historische gegevens. Om de gegevens opnieuw te gebruiken, voeg je de queue toe aan een andere workload. <!-- GPT translation -->

## Navigeren: Workloads <!-- GPT translation -->

In _Forecast > Workloads_{:.breadcrumbs} selecteer je een workload om de pagina \**workloaddetails** te openen. De pagina bevat de volgende groepen: <!-- GPT translation -->

- Het gedeelte Volume <!-- GPT translation -->
- De sectie **AHT** <!-- GPT translation -->
- De sectie **Roosterbehoefte** <!-- GPT translation -->

Elke sectie bevat een grafiek en bewerkopties. <!-- GPT translation -->

De grafieken tonen standaard gegevens van de lopende week. <!-- GPT translation -->

- Om een andere tijdsperiode te selecteren, gebruik je de datumkiezer. Klik op het weeknummer om de hele week te selecteren, of klik op elk willekeurige dag en sleep om een kortere of langere periode dan een week te selecteren. <!-- GPT translation -->
- Gebruik _<_ en _>_ om naar een voorgaande of volgende periode te navigeren binnen de geselecteerde periode. <!-- GPT translation -->

### De sectie Volume <!-- GPT translation -->

De grafiek in de sectie Volume toont contactvolume voor historische gegevens, geïmporteerde forecasts en gegenereerde forecasts. <!-- GPT translation -->
Beweeg de cursor over de grafiek voor gedetailleerde informatie over volume, AHT, personeelsbehoefte, handmatige aanpassingen en toegevoegde gebeurtenissen.<br> <!-- GPT translation -->
Lees hoe je het {% link_new volume aanpast | features/forecast/injixo-forecast/manual-adjustments.md | #het-volume-aanpassen%}. <!-- GPT translation -->

### De sectie Adherence to staff (AHT) <!-- GPT translation -->

De sectie AHT is standaard verborgen en wordt pas weergegeven als je de laadpagina Opdrachtgegevens opent of herlaadt. Klik op het pictogram **Ogen** om de sectie AHT weer te geven. <!-- GPT translation -->
De AHT-grafiek is alleen beschikbaar voor workloads met queues die AHT-gegevens bevatten.<br> <!-- GPT translation -->
Maak je eerst vertrouwd met het {% link_new aanpassen van de AHT | features/forecast/injixo-forecast/manual-adjustments.md | #aht-aanpassen %}. <!-- GPT translation -->

### De sectie Behoefte nodig glEnable_staff:requirements:staff:requirements<section> <!-- GPT translation -->

In de sectie Grafiek van de staff requirements worden de berekende personeelsbehoeften weergegeven. <!-- GPT translation -->
Onder de grafiek worden de geconfigureerde vereisten voor het aantal medewerkers en het totaal aantal gewerkte uren weergegeven. Beweeg de muis over de grafiek om gedetailleerde informatie over AHT, volume, personeelsbehoefte, eventuele handmatige aanpassingen en toegevoegde events te bekijken.<br> <!-- GPT translation -->
Lees hoe je {% link_new de personeelsbehoefte \\\(forecast\\\) voor het plannen gebruikt | features/forecast/injixo-forecast/calculate-staff-requirements.md | #use-staff-requirements-for-scheduling %}. <!-- GPT translation -->

## Veelgestelde vragen <!-- TM 100 -->

| Vraag                                     | Antwoord                                                                                                                                                                                                                                                                                                                                                       | <!-- GPT translation -->
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Waarom zijn de grafieken op de workloadpagina leeg? | injixo genereert een forecast voor 365 dagen na de laatste import. Als de grafieken op de workloadpagina geen gegevens weergeven voor een bepaalde toekomstige tijdsperiode, controleer dan of je integratie nog steeds gegevens importeert onder _Account > Integraties_{:.breadcrumbs}. | <!-- GPT translation -->