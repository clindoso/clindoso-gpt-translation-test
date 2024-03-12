---
title: Workloads aanmaken
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Maak workloads aan die het historische en voorspelde contactvolume en AHT weergeven. Kom meer te weten over de verschillende workloadtypen.
related_articles:
  - overwrite_title: Wat is injixo Forecast?
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Met workloads werken
    filepath: features/forecast/injixo-forecast/work-with-workloads.md
  - overwrite_title: Openingstijden activeren
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
---

Ga naar _Forecast_{:.breadcrumbs} om workloads aan te maken, te bewerken of te verwijderen.

Workloads brengen de inputkanalen van je externe systeem in kaart, dat de gegevens van je klantinteracties registreert. injixo Forecast gebruikt geïmporteerde contactgegevens die zijn opgeslagen in queues om een forecast voor de workload te berekenen. Configureerbare gebeurtenissen, feestdagen of openingstijden beïnvloeden het resultaat van de forecast. Je kunt je forecast ook {% link_new in workloads importeren | features/forecast/injixo-forecast/import-forecast.md %}.

In workloads configureer je de berekening van de personeelsbehoefte. De personeelsbehoefte is nodig voor planningsdoeleinden.

Ben je nog niet zo vertrouwd met injixo Forecast? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Vereisten

- Voeg {% link_new een native of CSV-integratie | features/acd-integration/cloud/how-integrations-work.md %} toe en importeer historische gegevens voor minstens een queue.
- Importeer aangeboden contacten, gemiddelde afhandeltijd (AHT), en afgehandelde contacten. Voor workloads met meerdere queues moet in de afgehandelde contacten de AHT en de berekende gewogen gemiddelden worden weergegeven.

injixo maakt queues aan op basis van de gegevens die door een integratie zijn geïmporteerd. Het interval van de gegevensimport bepaalt het interval van de queues die op basis van deze gegevens worden aangemaakt. Je kunt alleen queues met hetzelfde interval aan een workload toevoegen.

## Queues en kanalen

Contactgegevens die door een integratie worden geïmporteerd, worden opgeslagen in queues. Deze queues zijn altijd gekoppeld aan een kanaal. Als je [workloads aanmaakt](#workloads-aanmaken) kun je queues filteren op kanaal en ze aan de workload toevoegen. Native integraties stellen automatisch het kanaal in voor queues. Niet alle integraties ondersteunen alle kanalen.

Voor een CSV-integratie moet je het kanaal handmatig instellen. Je kunt een kanaal per kolom toevoegen of één kanaal selecteren voor het bestand wanneer je {% link_new de kolommen van een CSV-bestand toewijst | features/acd-integration/cloud/add-csv-integration.md | #kolommen-toewijzen %}.  

De volgende kanalen worden door integraties ondersteund:

- Gesprekken
- Chats
- E-mails
- Cases
- Documenten
- Sociale media

injixo Forecast groepeert queues per kanaal. Je kunt alleen queues met hetzelfde interval aan een workload toevoegen.

<!-- anchor for intercom forecast tour -->

## Workloads aanmaken<a name="creating-a-new-workload"></a>

We raden aan om voor elke activiteit die je met personeelsbehoefte wilt inplannen een workload aan te maken. Multiactiviteiten vereisen één workload voor de multiactiviteit, en één workload voor elke deelactiviteit.

1. Klik boven de lijst op _Nieuwe workload_{:.doc-button}.
2. Voeg de algemene informatie toe voor je workload:
   - **Naam**: Unieke naam om je werklast te herkennen.
   - **Tijdzone**: De {% link_new tijdzone | best-practices/working-with-timezones.md %} voor de workload kan later niet worden bewerkt.

     > Opmerking
     >
     > - Om de personeelsbehoefte voor een eenheid op te slaan, moet de tijdzone van de workload overeenkomen met de tijdzone van de eenheid.
     > - Als je een andere tijdzone voor je workload hebt ingesteld dan voor de integratie weermee je gegevens importeert, worden de geïmporteerdegegevens met tijdsverschuiving in de workload weergegeven. Als voor een CSV-integratie bijvoorbeeld UTC-tijd is ingesteld en je voor je workload CEST-tijd (UTC +2 uur), worden de geïmporteerde gegevens van 8:00 uur in de workload weergegeven om 10:00 uur.

   - (Optioneel) **Feestdagen regio**: Omvat nationale feestdagen die je forecast kunnen beïnvloeden.
   - (Optioneel) **Eenheid** en **Activiteit**: Vereist om {% link_new openingstijden te activeren | features/forecast/injixo-forecast/forecast-activate-business-hours.md %} in de sectie **Openingstijden**.

3. (alleen injixo Classic) Selecteer een optie uit de sectie **Prijsmodel**:

   - **Live-modus** (betaald): Maandelijks gefactureerd. Kan niet worden teruggedraaid naar de Testmodus.
   - **Testmodus** (gratis): Je kunt alleen forecasts bekijken en geen personeelsbehoeften overdragen voor planningsdoeleinden.

4. Selecteer de queues voor je workload in de sectie **Queues toewijzen**.

   Om het aantal weergegeven queues te verkleinen:

   - Filter de queues op kanaal (gesprekken, chats, enz.).
   - Vink de selectievakjes voor geselecteerde, niet-geselecteerde of inactieve queues aan. Inactieve queues zijn queues die geïmporteerd zijn door integraties die verwijderd zijn.
   - Gebruik het zoekveld boven de tabel. Je kunt zoeken op de naam van de queue, de integratie of de workload.

5. Klik op _Workload aanmaken_{:.doc-button}.

   De pagina geeft historische gegevens en een eerste forecastversie weer.  
   Als de berekening is afgerond, dien je de pagina te vernieuwen om de uiteindelijke forecastversie te bekijken.  
   De nieuwe workload wordt weergegeven in de lijst met workloads.

Als je injixo Essential gebruikt, kun je Basic workloads aanmaken. Voor Basic workloads zijn minimaal twee weken aan historische gegevens nodig. Openingstijden worden niet ondersteund door Basic workloads.

Als je injixo Advanced of Enterprise WFM gebruikt, kun je Smart workloads aanmaken. Smart workloads genereren een forecast op de historische gegevens van slechts een dag. Openingstijden worden ondersteund door Smart workloads.

Als je injixo Classic gebruikt, moet je daarnaast ook het forecastmodel (Smart of Basic) selecteren voor elke workload. Voor Smart workloads moet je kiezen tussen de Live-modus en de Testmodus. De Testmodus is gratis, maar laat je de forecast alleen bekijken. Je kunt geen personeelsbehoefte overdragen voor planningsdoeleinden. De Live-modus biedt de volledige functionaliteit en wordt maandelijks in rekening gebracht. Slimme workloads in de Live-modus kunnen niet worden teruggedraaid naar de Testmodus.

<!-- hidden: feature not live yet -->
<!-- ## Create workloads without historical data

You only need an integration and historical data import if you want injixo to create forecasts. To add forecast data by {% link_new importing a forecast | features/forecast/injixo-forecast/import-forecast.md %} that has been generated externally or to {% link_new create constant staff requirements | features/forecast/requirement-scripts/requirement-constant.md %}, you can create a workload using the tab *Forecast Import*:

1. Go to **Forecast**{:.breadcrumbs}.
2. Click _Create Workload_{:.doc-button} in the upper right corner of the forecast page.
3. In the *Basic configuration* section, enter a **Name** for your new workload.
4. Select the **Time zone** to display data. Note: The set time zone must match the planning unit to save staff requirements.
5. (Optional) Select the **Holiday region** to acknowledge all national holidays that affect your forecast for the year.
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements.
    {{ 4 | image: 'Import Workload basic configuration section' }}
7. Click the tab **Forecast import**.
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file.
    {{ 5 | image: 'Import Workload parameters' }}
9. Click *Create workload*{:.doc-button}. -->

## Workloads bewerken

1. Selecteer een workload uit de lijst met workloads of typ de naam van de workload in het zoekveld in.
2. Klik op het {% icon pencil %} om de gegevens van de workload te bewerken.  
   Je kunt queues toevoegen of verwijderen zonder dat je opnieuw gegevens hoeft te importeren.
3. Klik op _Workload opslaan_{:.doc-button}.
   Op basis van de nieuwe configuratie wordt de forecast mogelijk bijgewerkt.

## Workloads verwijderen

1. Klik op het {% icon trash %} naast de workload in de lijst.
2. Klik in het bevestigingsvenster op _Workload verwijderen_{:.doc-button}.  
    injixo slaat de bijbehorende historische gegevens op. Om de gegevens te hergebruiken, voeg je de queue(s) toe aan een andere workload.
