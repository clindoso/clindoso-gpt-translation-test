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

Workloads staan voor de inputkanalen van je externe systeem. Hier worden de gegevens van je interactie met klanten geregistreerd. Aan de hand van geïmporteerde contactgegevens, die in queues zijn ondergebracht, berekent injixo Forecast de workloadforecasts upportactiviteiten plaatsvinden. Scanresultaten van schedule-adherence-uitkomsten, aanwezigheid, naverwerkingstijd, serviceverslagen en andere KPI's gaan ook een rol spelen. Je kunt ook je {% link_new forecasts importeren | features/forecast/injixo-forecast/import-forecast.md %} en importeren, hiervoor de workloads gebruiken. <!-- GPT translation -->

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

Hoeveel workloads en hoeveel queues je voor elke workload toevoegt, is afhankelijk van de behoeften van je organisatie. Denk hierbij aan de vraag of je voor elke queue afzonderlijke berekeningen voor volume, AHT en personeelsbehoeften nodig hebt. <!-- GPT translation -->

Bekijk het volgende voorbeeld: <!-- GPT translation -->

Je hebt in je ACD-systeem vijf queues geconfigureerd: <!-- GPT translation -->

- Support Tier 1 <!-- GPT translation -->
- Support Tier 2 <!-- GPT translation -->
- Product Sales North <!-- GPT translation -->
- Product Sales Central <!-- GPT translation -->
- Product Sales South <!-- GPT translation -->

In dit voorbeeld verwijzen de drie product sales-queues naar verschillende regio's. Dat betekent dat agenten met de juiste kwalificaties sales-gerelateerde vragen kunnen beantwoorden, ongeacht waar de contacten vandaan komen. Het kan relevant zijn om de sales-queues op basis van regio te scheiden om marketingcampagnes of andere indicatoren bij te kunnen houden. Toch is het niet nodig om de volgende activiteitenvolumes en personeelsbehoeften voor elke regio apart te forecasten. Je kunt [een workload aanmaken](#workloads-aanmaken) met de naam Product Sales, en alle drie de queues selecteren in de sectie **Queues toewijzen**. <!-- GPT translation -->

Daarentegen moeten het volume en de personeelsbehoefte voor supportvragen afzonderlijk worden berekend. Eerstelijns vragen zijn veelvoorkomend en gemakkelijker te beantwoorden dan tweedelijns vragen. Medewerkers die eerstelijns vragen behandelen, zijn niet noodzakelijkerwijs getraind om tweedelijns vragen te beantwoorden. Daarbij komen tweedelijns vragen minder vaak voor en heb je daarom minder personeel nodig. In dit geval maak je [twee workloads](#workloads-maken) aan, een queue voor 'Support Eerstelijns' en 'Support Tweedelijns', en wijs je de juiste queue aan elke workload toe. Als je wilt dat medewerkers die zich bezighouden met tweedelijns support ook eerstelijns vragen beantwoorden (met minder prioriteit), houd dan de twee afzonderlijke workloads gescheiden en gebruik een {% link_new multiactiviteit | features/administration/activity-types-and-properties.md | #subactiviteiten %} voor de planning. <!-- GPT translation -->

<!-- anchor for intercom forecast tour -->

## Workloads aanmaken <!-- TM 100 -->

Maak voor elke activiteit die je wilt plannen op basis van personeelsbehoefte een workload aan. Multiactiviteiten vereisen een workload voor de multiactiviteit, en een workload voor elke deelactiviteit. <!-- GPT translation -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op _Nieuwe workload_{:.doc-button} bovenaan in de lijst. <!-- GPT translation -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 100 -->

   - **Naam**: Unieke naam om je werklast te herkennen. <!-- TM 100 -->
   - **Tijdzone**: De {% link_new tijdzone | best-practices/working-with-timezones.md %} voor de workload kan later niet worden bewerkt. <!-- TM 100 -->

     > Opmerking <!-- TM 100 -->
     >
     > - Om de personeelsbehoefte voor een eenheid op te slaan, moet de tijdzone van de workload overeenkomen met de tijdzone van de eenheid. <!-- TM 100 -->
     > - Als je een andere tijdzone voor je workload hebt ingesteld dan voor de integratie weermee je gegevens importeert, worden de geïmporteerdegegevens met tijdsverschuiving in de workload weergegeven. Als voor een CSV-integratie bijvoorbeeld UTC-tijd is ingesteld en je voor je workload CEST-tijd (UTC +2 uur), worden de geïmporteerde gegevens van 8:00 uur in de workload weergegeven om 10:00 uur. <!-- TM 100 -->

   - (Optioneel) **Feestdagengebied**: Bevat nationale feestdagen die van invloed kunnen zijn op je forecast. <!-- GPT translation -->
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

   Op de pagina worden historische gegevens en een voorlopige forecastversie weergegeven.    <!-- GPT translation -->
   Nadat de berekening is afgerond laadt je de pagina opnieuw om de definitieve forecastversie te bekijken. <!-- GPT translation -->
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
5. (Optioneel) Selecteer de **Feestdagencode-regio** om alle nationale feestdagen volgens je forecast voor het jaar in aanmerking te nemen. <!-- GPT translation -->
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements. <!-- TM 100 -->
    {{ 4 | image: 'Import Workload basic configuration section' }} <!-- TM 100 -->
7. Click the tab **Forecast import**. <!-- TM 100 -->
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file. <!-- TM 100 -->
    {{ 5 | image: 'Import Workload parameters' }} <!-- TM 100 -->
9. Click *Create workload*{:.doc-button}. --> <!-- TM 100 -->

## Workloads bewerken <!-- TM 100 -->

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} een workload in de lijst door op de naam te klikken of typ de naam van de workload in het zoekveld. <!-- GPT translation -->
2. Klik op het {% icon pencil | icon-only %} om de werklastgegevens te bewerken.<br> <!-- GPT translation -->
   Je kunt queues toevoegen of verwijderen zonder dat je opnieuw gegevens hoeft te importeren. Weergegeven queues worden uitgegrijsd als hun interval of kanaal niet overeenkomt met eerder toegewezen queues. <!-- TM 100 -->
3. Klik op _Workload opslaan_{:.doc-button}. <!-- GPT translation -->
   Op basis van de nieuwe configuratie wordt de forecast mogelijk bijgewerkt. <!-- TM 100 -->

## Workloads verwijderen <!-- TM 100 -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op het pictogram **Verwijderen** naast de workload die je wilt verwijderen. <!-- GPT translation -->
2. Klik in het bevestigingsvenster op _Workload verwijderen_{:.doc-button}.   <!-- GPT translation -->
   injixo bewaart de bijbehorende historische gegevens. Om de gegevens opnieuw te kunnen gebruiken, voeg je de queue of queues toe aan een andere workload. <!-- GPT translation -->

## Navigeren naar workloads <!-- GPT translation -->

Ga in _Forecast > Workloads_{:.breadcrumbs} naar het gewenste dag-/dagdelenkader en klik erop om de pagina Dagdelenkadergegevens te openen. Deze pagina bevat de volgende drie secties: <!-- GPT translation -->

- Het gedeelte Volume <!-- GPT translation -->
- De sectie **AHT** <!-- GPT translation -->
- De sectie **Werkbelasting (in FTE)** <!-- GPT translation -->

Elke sectie bevat een grafiek en bewerkingsfunctionaliteiten. <!-- GPT translation -->

De grafieken tonen standaard gegevens van deze week. <!-- GPT translation -->

- Gebruik de datumprikker om een ander tijdsbereik te selecteren. Klik op een weeknummer om de hele week of klik op elke willekeurige dag en sleep om een periode korter of langer dan een week te selecteren. <!-- GPT translation -->
- Ga met _<_{:.doc-button} en _>_{:.doc-button} naar een eerdere of latere deel van de geselecteerde tijdsperiode. <!-- GPT translation -->

### De sectie Volume <!-- GPT translation -->

De grafiek in de sectie Contactvolume geeft het contactvolume weer voor historische gegevens, geïmporteerde forecast en de gegenereerde forecast. <!-- GPT translation -->
Beweeg de cursor over de grafiek voor gedetailleerde informatie over het volume, AHT, personeelsbehoefte, handmatige aanpassingen en toegevoegde gebeurtenissen.<br> <!-- GPT translation -->
Lees hoe je de {% link_new werkvolume aanpast | features/forecast/injixo-forecast/manual-adjustments.md | #het-volume-aanpassen%}. <!-- GPT translation -->

### De sectie Bewerkte AHT <!-- GPT translation -->

De sectie AHT is standaard verborgen zodra je de overzichtspagina voor workload opent of de pagina vernieuwt. Klik op het pictogram 'oog' {% icon eye_slash | icon_only %} om de sectie AHT weer te geven. <!-- GPT translation -->
De AHT-grafiek is alleen beschikbaar voor workloads met queues die AHT-gegevens bevatten.<br> <!-- GPT translation -->
Lees eerst hoe je de {% link_new AHT aanpast | features/forecast/injixo-forecast/manual-adjustments.md | #aht-aanpassen%}. <!-- GPT translation -->

### De sectie Behoefte aan medewerkers <!-- GPT translation -->

De grafiek in de sectie 'Personeelsbehoefte' geeft de berekende personeelsbehoefte weer. <!-- GPT translation -->
Onder de grafiek worden de geconfigureerde medewerkersbehoefteparameters en het totaal aantal persoon-uren weergegeven. Beweeg over de grafiek om meer gedetailleerde informatie over de AHT, volume, personeelsbehoefte, handmatige aanpassingen en toegevoegde gebeurtenissen weer te geven.<br> <!-- GPT translation -->
Lees eerst hoe je {% link_new de personeelsbehoefte voor het plannen gebruikt | features/forecast/injixo-forecast/calculate-staff-requirements.md | #use-staff-requirements-for-scheduling %}. <!-- GPT translation -->

## Veelgestelde vragen <!-- TM 100 -->

| Vraag                                         | Antwoord                                                                                                                                                                                                                                                                                                                                                      | <!-- GPT translation -->
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Waarom worden in de grafieken op een workloadpagina geen gegevens weergegeven? | injixo genereert een forecast voor 365 dagen na de laatste gegevensimport. Als de grafieken op een workloadpagina voor een bepaalde toekomstige periode geen gegevens weergeven, controleer dan of je integratie in _Account > Integraties_{:.breadcrumbs} nog steeds gegevens importeert. Controleer ook of de juiste queues aan de workload zijn toegewezen in de workloa.cfguratie. | <!-- GPT translation -->