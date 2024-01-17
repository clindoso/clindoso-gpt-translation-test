---
title: Create activities
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
beta-feature: false
description: Create activities to represent scheduled and unscheduled tasks in your company.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Ga naar _Plan > Configuratie > Activiteiten_{:.breadcrumbs} om activiteiten aan te maken, te bewerken en te verwijderen. <!-- GPT translation -->

Activiteiten staan voor alle taken die in je bedrijf worden ingepland en gerapporteerd, zoals telefoongesprekken, pauzes, afwezigheid of vergaderingen. Je kunt zoveel activiteiten aanmaken als je nodig hebt. Het aantal activiteiten hangt alleen af van hoeveel taken je wilt onderscheiden en het gewenste detailniveau. <!-- GPT translation -->

Activiteiten zijn een essentieel onderdeel van het plannings- en roosterproces in injixo. Ze zijn gekoppeld aan andere configuratie-items, bijvoorbeeld aan {% link_new eenheidsgroepen | features/administration/create-and-manage-planning-units.md | #activiteiten-toevoegen %} en {% link_new dagmodellen | features/administration/daymodels/daymodel-basics.md %}. Ze maken ook deel uit van de roosters die je in het {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/add-and-delete-items.md %} of in {% link_new Schedules | features/scheduling/schedules/schedules-edit.md %} beheert. <!-- GPT translation -->

injixo bevat twee vooraf geconfigureerde (niet verwijderbare) activiteiten: <!-- GPT translation -->

- Aanwezigheid: Deze activiteit wordt in dagmodellen als tijdelijke activiteit gebruikt. Bij het plannen vervangt injixo deze activiteit door andere activiteiten die als Planbaar zijn geconfigureerd. <!-- GPT translation -->
- Verlof: Deze activiteit wordt gebruikt om betaalde vakantie in te plannen op basis van het vakantierecht van een medewerker. Niet-betaalde vrije dagen dien je als een aparte activiteit aan te maken. <!-- GPT translation -->

## Een medewerker aanmaken <!-- TM 62 -->

2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 83 -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 84 -->
   - **Naam**: Unieke naam om je activiteit te beschrijven. De afkorting wordt automatisch gegenereerd. <!-- GPT translation -->
   - **Type**: Het activiteitentype bepaalt hoe injixo activiteiten bij het plannen gebruikt en waar en hoe ze in andere modules en rapportages worden weergegeven. Lees meer over de verschillende {% link_new activiteitentypen | features/administration/activity-types-and-properties.md | #activiteitentypen %}. <!-- GPT translation -->
| Kleur |  De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven.<br>De kleur kan je helpen om de lengte, het dagmodeltype of opgenomen activiteiten sneller te herkennen. | <!-- TM 61 -->
| Sneltoets | Optionele sneltoets die je helpt om het dagmodel sneller in het Dienstrooster-Center in te voeren. Lees meer over {% link_new sneltoetsen | best-practices/tips-on-shift-center-usage.md %}. | <!-- TM 70 -->
   - **Officiële naam en afkorting**: Dit is een alternatieve naam die voor interne rapportagedoeleinden en integraties kan worden gebruikt. In injixo Me wordt altijd de naam weergegeven die in het veld **Naam** is ingevoerd. <!-- GPT translation -->
3. Vink een of meer selectievakjes aan om verschillende {% link_new activiteiteneigenschappen | features/administration/activity-types-and-properties.md | #activiteiteneigenschappen %} in te stellen. <!-- GPT translation -->
Als je Plannable raadpleegt, kun je de {% link_new prioriteitswaarde | best-practices/importance-for-activities.md %} bewerken. <!-- GPT translation -->
Als je Vervangbaar aanvinkt, kun je de {% link_new prioriteitswaarde | best-practices/priority-for-activities.md %} bewerken. <!-- GPT translation -->
4. (Optioneel) {% link_new Wijs kwalificaties toe | features/administration/work-with-skills.md | #kwalificaties-aan-activiteiten-toewijzen %} aan de activiteit. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

Lees meer over {% link_new activiteitentypen en eigenschappen | features/administration/activity-types-and-properties.md %}. <!-- GPT translation -->

## Activiteitentype <!-- TM 65 -->

Ga als volgt te marker te werk: <!-- GPT translation -->
- Klik op een activiteit in de lijst met **Activiteiten**. In de URL in de adresbalk van je browser wordt de ID van de geselecteerde activiteit weergegeven (bijv. https://www.injixo.com/plan/configuration/activities/1234). <!-- GPT translation -->
- Maak gebruik van de injixo API. Lees hier hoe je [activiteiten via de injixo API beheert](https://api.injixo.com/resources/activities/). <!-- GPT translation -->

## Multiactiviteiten en deelactiviteiten  <!-- GPT translation -->


Multiactiviteiten maken het mogelijk om medewerkers met meerdere kwalificaties in te plannen, op het moment dat een van hun kwalificaties vereist is. Je kunt een activiteit omzetten in een multiactiviteit door {% link_new andere activiteiten toe te wijzen | features/administration/activity-types-and-properties.md | #deelactiviteiten %}. De toegewezen activiteiten worden de deelactiviteiten van de multiactiviteit. In de lijst met activiteiten worden multiactiviteiten aangegeven met een pictogram <em class="multiactivity-icon"></em> icon. <!-- GPT translation -->

Als een activiteit een overkoepelende activiteit is, dan verschijnt de sectie **Multiactiviteiten** zodra je op de activiteit klikt. Hier worden alle overkoepelende activiteiten weergegeven waaraan de geselecteerde activiteit is toegewezen. <!-- GPT translation -->

Indien een activiteit geen deelactiviteit is, dan verschijnt er na het klikken op het juweel de sectie **Deelactiviteiten**, waar je andere activiteiten kunt kiezen die als deelactiviteit worden toegevoegd aan de activiteit die wordt bewerkt. De betreffende activiteit verandert dan in een multiactiviteit. <!-- GPT translation -->
Je kunt deactiviteiten alleen nog aan een activiteit toewijzen nadat je deze hebt aangemaakt. <!-- GPT translation -->

## Externe systemen <!-- GPT translation -->

<!-- wordt overbodig door de nieuwe Activiteiten toewijzen-pagina. Er is een afzonderlijk artikel nodig --> <!-- GPT translation -->

Je kunt activiteiten uit externe systemen aan een activiteit in injixo toewijzen. <!-- GPT translation -->
1. Selecteer een activiteit uit de lijst, scrol naar de sectie **Externe systemen** en klik op _Bewerken in WFM_{:.doc-button}. <!-- GPT translation -->
4. Ga naar de sectie **Externe Systemen**. <!-- TM 79 -->
4. Klik op het {% icon item-add %}. <!-- TM 97 -->
4. Selecteer in de vervolgkeuzemenu's een **externe systeem**, een **naam van het externe systeem** en een **classificatie**. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

> Je kunt een activiteit van een extern systeem slechts eenmaal aan een enkele activiteit in injixo toewijzen. <!-- GPT translation -->

## Een activiteit dupliceren <!-- GPT translation -->

Volg deze stappen om een nieuwe activiteit te maken met dezelfde algemene eigenschappen als een bestaande activiteit: <!-- GPT translation -->

1. Selecteer in de lijst met **Activiteiten** een activiteit. <!-- GPT translation -->
2. Klik op **Activiteit dupliceren** onder de naam van de activiteit. <!-- GPT translation -->
Er wordt een **activiteit aanmaken** venster geopend met vooraf aangevinkte selectievakjes. Toegewezen kwalificaties en deelactiviteiten worden niet gedupliceerd. <!-- GPT translation -->
3. Voer een **Naam** in voor de nieuwe activiteit. <!-- GPT translation -->
4. (Optioneel) Wijzig de kleur en andere eigenschappen. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

## Een activiteit bewerken of verwijderen <!-- GPT translation -->

1. Selecteer in de lijst met **Activiteiten** een activiteit. <!-- Repetition of GPT translation
  - Om de activiteit te bewerken, pas je de gegevens die je wilt veranderen aan en klik je op *Wijzigingen opslaan*{:.doc-button}. <!-- GPT translation -->
  - Klik op _Activiteit verwijderen_{:.doc-button} om de activiteit te verwijderen. <!-- GPT translation -->

Als de verwijderde activiteit aan andere configuratie-items zoals eenheids- of dagmodellen was toegewezen, dan wordt de activiteit in deze items cursief weergegeven. Een verwijderde activiteit verliest zijn toewijzingen aan andere items, maar blijft zichtbaar bij de configuratiegegevens. Mogelijk dien je bestaande dagmodellen opnieuw aan te maken die de verwijderde activiteit gebruikten. <!-- GPT translation -->

In Shift Center worden verwijderde activiteiten {% link_new omkaderd door een streeplijn | features/scheduling/shiftcenter/shift-center-overview.md | #zo-worden-items-weergegeven %}. In Schedules worden verwijderde activiteiten in het grijs weergegeven zonder naam. De oorspronkelijke tijdsinformatie blijft zichtbaar, behalve in de dagweergave. <!-- GPT translation -->