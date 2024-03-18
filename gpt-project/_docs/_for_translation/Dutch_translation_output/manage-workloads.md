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
---

Ga naar _Forecast_{:.breadcrumbs} om workloads aan te maken, te bewerken of te verwijderen. <!-- TM 100 -->

Workloads staat voor de kanalen van je externe systeem die de details van je klantinteracties vastleggen. injixo Forecast berekent op basis van geïmporteerde contactgegevens die in queues zijn opgeslagen een forecast voor de workload. Configureerbare gebeurtenissen, feestdagen of openingstijden beïnvloeden de forecast. Je kunt ook je {% link_new forecast importeren | features/forecast/injixo-forecast/import-forecast.md %} in Workloads. <!-- GPT translation -->

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

Hoeveel workloads en queues je instelt, hangt volledig af van de behoeften van je organisatie. Bij het instellen moet je aangeven of je afzonderlijke bandbreedtes, AHT- en personeelsbehoeftenberekeningen per queue wilt maken. <!-- GPT translation -->

Bekijk het volgende voorbeeld: <!-- GPT translation -->

Je hebt vijf queues geconfigureerd in je ACD-systeem: <!-- GPT translation -->

- Support Tier 1 <!-- GPT translation -->
- Support Tier 2 <!-- GPT translation -->
- Product Sales North <!-- GPT translation -->
- Product Sales Central <!-- GPT translation -->
- Product Sales South <!-- GPT translation -->

In dit voorbeeld verwijzen de drie productsales-queues naar verschillende regio's van een land waar uitsluitend de hoofdtaal wordt gesproken. Dit betekent dat medewerkers die vragen op het gebied van sales behandelen dit kunnen doen ongeacht waar het contact vandaan komt. Het is relevant om de sales-queues te splitsen op basis van campagnes of andere relevante indicatoren, maar het is niet nodig om de te verwachten contactvolumes en personeelsbehoefte per regio te voorcasten. Je kunt [een workload aanmaken](#workloads-aanmaken) met de naam Product Sales en vervolgens in de sectie **Queues toewijzen** alle drie de queues selecteren. <!-- GPT translation -->

De volume en personeelsbehoefte voor supportaanvragen moeten daarentegen afzonderlijk worden berekend. Tier 1-aanvragen zijn algemener en gemakkelijker te behandelen dan tier 2-aanvragen. Medewerkers die tier 1-aanvragen afhandelen, zijn niet per se bevoegd om tier 2-aanvragen te beantwoorden. Daarnaast komen tier 2-aanvragen minder vaak voor. Deze categorie is daarom minder tijdrovend en kan met minder medewerkers worden afgehandeld. Maak hier [twee workloads aan](#workloads-aanmaken) voor Support Tier 1 en Support Tier 2 en wijs de relevante queues toe aan elke workload. Als je medewerkers die verantwoordelijk zijn voor tier 2-aanvragen ook tier 1-aanvragen met minder urgentie wilt laten afhandelen, houd dan de twee afzonderlijke workloads gescheiden en gebruik voor het plannen van de activiteiten van beide medewerkers een {% link_new multiactiviteit | features/administration/activity-types-and-properties.md | #subactiviteiten %}. <!-- GPT translation -->

<!-- anchor for intercom forecast tour -->

## Workloads aanmaken <!-- TM 100 -->

Maak voor elke activiteit die je wilt plannen op personeelsbehoefte een workload aan. Multiactiviteiten hebben een workload nodig voor de multiactiviteit en voor elke deelactiviteit. <!-- GPT translation -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op _Nieuwe workload_{:.doc-button} boven aan de lijst. <!-- GPT translation -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 100 -->

   - **Naam**: Unieke naam om je werklast te herkennen. <!-- TM 100 -->
   - **Tijdzone**: De {% link_new tijdzone | best-practices/working-with-timezones.md %} voor de workload kan later niet worden bewerkt. <!-- TM 100 -->

     > Opmerking <!-- TM 100 -->
     > <!-- TM 100 -->
     > - Om de personeelsbehoefte voor een eenheid op te slaan, moet de tijdzone van de workload overeenkomen met de tijdzone van de eenheid. <!-- TM 100 -->
     > - Als je een andere tijdzone voor je workload hebt ingesteld dan voor de integratie weermee je gegevens importeert, worden de geïmporteerdegegevens met tijdsverschuiving in de workload weergegeven. Als voor een CSV-integratie bijvoorbeeld UTC-tijd is ingesteld en je voor je workload CEST-tijd (UTC +2 uur), worden de geïmporteerde gegevens van 8:00 uur in de workload weergegeven om 10:00 uur. <!-- TM 100 -->

   - (Optioneel) **Feestdagregio**: Bevat feestdagen die van invloed kunnen zijn op je forecast. <!-- GPT translation -->
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

   Op de pagina worden historische gegevens en een voorlopige forecastversie weergegeven.   <!-- GPT translation -->
   Als de berekening is voltooid, dan moet je de pagina vernieuwen om de definitieve forecastversie te zien. <!-- GPT translation -->
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
5. (Optioneel) Selecteer de **Feestdagregio** om alle feestdagen waarvan de forecast van je huidige jaar afhankelijk is in te stellen. <!-- GPT translation -->
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements. <!-- TM 100 -->
    {{ 4 | image: 'Import Workload basic configuration section' }} <!-- TM 100 -->
7. Click the tab **Forecast import**. <!-- TM 100 -->
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file. <!-- TM 100 -->
    {{ 5 | image: 'Import Workload parameters' }} <!-- TM 100 -->
9. Click *Create workload*{:.doc-button}. --> <!-- TM 100 -->

## Workloads bewerken <!-- TM 100 -->

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} een workload in de lijst of voer de naam van de workload in het zoekveld in. <!-- GPT translation -->
2. Klik op het pictogram Bewerken {% icon pencil | icon-only %} om de gegevens van de workloads te wijzigen.<br> <!-- GPT translation -->
   Je kunt queues toevoegen of verwijderen zonder dat je opnieuw gegevens hoeft te importeren. Weergegeven queues worden uitgegrijsd als hun interval of kanaal niet overeenkomt met eerder toegewezen queues. <!-- TM 100 -->
3. Klik op _Werkbelasting opslaan_{:.doc-button}.   <!-- GPT translation -->
   Op basis van de nieuwe configuratie wordt de forecast mogelijk bijgewerkt. <!-- TM 100 -->

## Workloads verwijderen <!-- TM 100 -->

1. Klik in _Forecast > Workloads_{:.breadcrumbs} op het pictogram met de vuilnisbak {% icon trash | icon-only %} naast de workload die je wilt verwijderen. <!-- GPT translation -->
2. Klik in het bevestigingsvenster op _Workload verwijderen_{:.doc-button}.    <!-- GPT translation -->
   injixo bewaart de bijbehorende historische gegevens. Om deze gegevens opnieuw te gebruiken, voeg je het betreffende aandachtsgebied of de aandachtsgebieden toe aan een andere workload. <!-- GPT translation -->

## Navigeren naar Workloads <!-- GPT translation -->

In _Forecast > Workloads_{:.breadcrumbs} selecteer je een workload om de detailpagina van de workload te openen. De pagina bevat drie volgenede secties: <!-- GPT translation -->

- Het gedeelte Volume <!-- GPT translation -->
- De sectie **AHT** <!-- GPT translation -->
- De sectie **Middelenbehoefte** <!-- GPT translation -->

Elke sectie bevat een grafiek en bewerkingsfunctionaliteiten. <!-- GPT translation -->

De grafieken tonen standaard gegevens van de huidige week. <!-- GPT translation -->

- Gebruik de datumkiezer om een andere tijdsperiode te selecteren. Klik op een weeknummer om de hele week te selecteren, of klik op een dag en sleep om een kortere of langere periode te selecteren. <!-- GPT translation -->
- Gebruik _<_{:.doc-button} en _>_{:.doc-button} om naar het verleden en volgende week te navigeren van de actueel geselecteerde periode. <!-- GPT translation -->

### Het volumegedeelte <!-- GPT translation -->

De grafiek in de sectie Volume geeft contactvolume weer voor historische gegevens, geïmporteerde forecasts en gegenereerde forecasts. <!-- GPT translation -->
Beweeg je cursor over de grafiek om gedetailleerde informatie te zien over het Volume, de AHT, de personeelsbehoefte, handmatige aanpassingen en toegevoegde gebeurtenissen.<br> <!-- GPT translation -->
Lees hoe je de {% link_new bandbreedte aanpast | features/forecast/injixo-forecast/manual-adjustments.md | #bandbreedte-aanpassen%}. <!-- GPT translation -->

### De sectie AHT <!-- GPT translation -->

De sectie Gemiddelde afhandeltijd wordt standaard verborgen bij het openen of herladen van de pagina met werkbelasting. Klik op het pictogram Het oog icon eye_slash te klikken om de sectie Gemiddelde afhandeltijd weer te geven. <!-- GPT translation -->
De AHT-grafiek is alleen beschikbaar wanneer queues van workloads gegevens over de After Call Work (ACW) bevatten.<br> <!-- GPT translation -->
Ga naar {% link_new Handmatige aanpassingen in de forecast | features/forecast/injixo-forecast/manual-adjustments.md %} voor meer informatie over het {% link_new aanpassen van de AHT | features/forecast/injixo-forecast/manual-adjustments.md %}. <!-- GPT translation -->

### Het sectie Behoefte aan medewerkers <!-- GPT translation -->

In de sectie Vereiste medewerkers wordt een grafiek met de berekende behoefte aan medewerkers weergegeven. <!-- GPT translation -->
*Onder de grafiek worden de geconfigureerde bandbreedteparameters en het totaal aantal persoon-uren weergegeven. Beweeg je cursor over de grafiek om gedetailleerde informatie te bekijken over AHT, volume, bandbreedte, eventuele handmatige wijzigingen en toegevoegde gebeurtenissen.*<br> <!-- GPT translation -->
Learn how to use {% link_new personeelsbehoefte voor planning | features/forecast/injixo-forecast/calculate-staff-requirements.md | #use-staff-requirements-for-scheduling %}. <!-- GPT translation -->

## Veelgestelde vragen <!-- TM 100 -->

| Vraag                                     | Antwoord                                                                                                                                                                                                                                                                                                                                                       | <!-- GPT translation -->
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Waarom zijn de grafieken op een workload-pagina leeg? | injixo genereert een forecast voor 365 dagen na de laatste gegevensimport. Als de grafieken op een workload-pagina geen weergavekader tonen over een bepaalde toekomstige periode, controleer dan of je integratie nog steeds gegevens importeert in _Account > Integraties_{:.breadcrumbs}. Controleer ook of in de workload-configuratie de juiste queues aan de workload zijn toegewezen. | <!-- GPT translation -->