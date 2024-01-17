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

Activiteiten staan voor alle taken die in je bedrijf worden ingepland en gerapporteerd, zoals telefonie, pauzes, verlof en vergaderingen. Je kunt zoveel activiteiten aanmaken als je wilt. Het aantal activiteiten is alleen afhankelijk van het aantal taken dat je wilt onderscheiden en het gewenste detailniveau. <!-- GPT translation -->

Activiteiten zijn een essentieel onderdeel van het plannings- en scheduling-proces in injixo. Ze zijn gekoppeld aan andere configuratie-items, zoals {% link_new eenheidentypen | features/administration/create-and-manage-planning-units.md | #activiteiten-aanmaken-en-bewerken %}, {% link_new dagmodellen | features/administration/daymodels/daymodel-basics.md %}. Ze maken ook deel uit van de door het {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/add-and-delete-items.md %} of in {% link_new Dienstroosters | features/scheduling/schedules/schedules-edit.md %}. <!-- GPT translation -->

injixo bevat twee vooraf geconfigureerde (niet te verwijderen) activiteiten: <!-- GPT translation -->

- Huidig moment: Deze activiteit wordt in dagmodellen als placeholdertool gebruikt. Tijdens het planningsproces vervangt injixo deze activiteit door andere activiteiten die als Planbaar zijn geconfigureerd. <!-- GPT translation -->
- Vakantie: Deze activiteit wordt gebruikt om betaalde vakantie in te plannen op basis van het verlofrecht van een medewerker. Voer onbetaalde verlofaanvragen als een afzonderlijke activiteit in. <!-- GPT translation -->

## Een medewerker aanmaken <!-- TM 62 -->

2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 83 -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 84 -->
   - **Naam**: Unieke naam ter aanduiding van je activiteit. De afkorting wordt automatisch gegenereerd. <!-- GPT translation -->
   - **Type**: Het activiteitentype bepaalt hoe injixo activiteiten bij het plannen gebruikt en hoe ze in andere modules en rapporten worden weergegeven. Lees meer over de verschillende {% link_new activiteitentypes | features/administration/activity-types-and-properties.md | #activiteitentypes %}. <!-- GPT translation -->
| Kleur |  De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven.<br>De kleur kan je helpen om de lengte, het dagmodeltype of opgenomen activiteiten sneller te herkennen. | <!-- TM 61 -->
| Sneltoets | Optionele sneltoets die je helpt om het dagmodel sneller in het Dienstrooster-Center in te voeren. Lees meer over {% link_new sneltoetsen | best-practices/tips-on-shift-center-usage.md %}. | <!-- TM 70 -->
   - **Officiële naam en afkorting**: Alternatieve naam die voor interne rapportagedoeleinden en integraties kan worden gebruikt. In injixo Me wordt altijd de naam weergegeven die onder **Naam** is ingevoerd. <!-- GPT translation -->
3. Vink een of meerdere selectievakjes aan om verschillende {% link_new activiteiteneigenschappen | features/administration/activity-types-and-properties.md | #activiteiteneigenschappen %} in te stellen. <!-- GPT translation -->
Als je Plannable raadpleegt, kun je de {% link_new kwalificatiewaarde | best-practices/importance-for-activities.md %} bewerken. <!-- GPT translation -->
Als je Vervangbaar selecteert, kun je de {% link_new prioriteitswaarde | best-practices/priority-for-activities.md %} bewerken. <!-- GPT translation -->
4. (Optioneel) {% link_new Wijs kwalificaties toe | features/administration/work-with-skills.md | #kwalificaties-aan-activiteiten-toewijzen %} aan de activiteit. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

Lees meer over {% link_new activiteitentypen en eigenschappen | features/administration/activity-types-and-properties.md %}. <!-- GPT translation -->

## Activiteitentype <!-- TM 65 -->

Je kunt de ID van een activiteit als volgt bekijken: <!-- GPT translation -->
- Klik op een activiteit in de lijst met **activiteiten**. In de URL-balk van je browser wordt het ID van de geselecteerde activiteit weergegeven (bijv. https://www.injixo.com/plan/configuration/activities/1234). <!-- GPT translation -->
- Maak gebruik van de injixo API. Lees hoe je [activiteiten beheert via de injixo API](https://api.injixo.com/resources/activities/). <!-- GPT translation -->

## Multiactiviteiten en deelactiviteiten  <!-- GPT translation -->


Multiactiviteiten zorgen ervoor dat je medewerkers met diverse kwalificaties in kunt plannen wanneer een van hun kwalificaties nodig is. Je kunt een activiteit omzetten in een multiactiviteit door {% link_new andere activiteiten toe te wijzen | features/administration/activity-types-and-properties.md | #subactiviteiten %}. De toegewezen activiteiten worden de deelactiviteiten van de multiactiviteit.  In de activiteitenlijst worden multiactiviteiten aangeduid met een pictogram <em class="multiactivity-icon"></em>. <!-- GPT translation -->

Als een activiteit een subactiviteit is, zie je bij selecteren de sectie **Multiactiviteiten**. Deze sectie geeft alle multiactiviteiten weer waaraan de activiteit is toegewezen. <!-- GPT translation -->

Als een activiteit geen subactiviteit is, dan vind je in de sectie **Subactiviteiten** een verwijzing naar andere activiteiten die je als de nieuwe hoofdactiviteit kunt selecteren. De betreffende activiteit wordt dan de multiactiviteit. <!-- GPT translation -->
Je kunt pas deelactiviteiten aan een activiteit toewijzen nadat de activiteit is aangemaakt. <!-- GPT translation -->

## Externe systemen <!-- GPT translation -->

<!-- wordt overbodig door de nieuwe pagina Activiteiten toewijzen. Vereist een afzonderlijk artikel --> <!-- GPT translation -->

Je kunt activiteiten uit andere systemen aan een activiteit in injixo toewijzen. <!-- GPT translation -->
1. Selecteer een activiteit uit de lijst, scrol naar de sectie **Externe systemen** en klik op _Bewerken in WFM_{:.doc-button}. <!-- GPT translation -->
4. Ga naar de sectie **Externe Systemen**. <!-- TM 79 -->
4. Klik op het {% icon item-add %}. <!-- TM 97 -->
4. Selecteer in de vervolgkeuzemenu's een **externe system** en een **naam uit het externe systeem** en een **classificatie**. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

> Je kunt een activiteit alleen vanuit een extern systeem naar een enkele activiteit in injixo overdragen. <!-- GPT translation -->

## Een activiteit dupliceren <!-- GPT translation -->

Volg deze stappen om een nieuwe activiteit met dezelfde algemene eigenschappen als een bestaande activiteit aan te maken: <!-- GPT translation -->

2. Selecteer een activiteit in de lijst met **Activiteiten**. <!-- GPT translation -->
2. Klik op **Activiteit dupliceren** onder de naam van de activiteit. <!-- GPT translation -->
Het venster **Nieuwe activiteit aanmaken** wordt geopend met vooraf aangevinkte selectievakjes. Toegewezen kwalificaties en deelactiviteiten worden niet gedupliceerd. <!-- GPT translation -->
Voer een **naam** in voor de nieuwe activiteit. <!-- GPT translation -->
4. (Optioneel) Wijzig de kleur en andere eigenschappen. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

## Een activiteit bewerken of verwijderen <!-- GPT translation -->

2. Selecteer een activiteit in de lijst met **Activiteiten**. <!-- Repetition of GPT translation
  - Bewerken: Bewerk de informatie die je wilt wijzigen en klik op _Wijzigingen opslaan_{:.doc-button}. <!-- GPT translation -->
- Klik op _Activiteit verwijderen_{:.doc-button} rechtsonder om de activiteit te verwijderen. <!-- GPT translation -->

Als de verwijderde activiteit aan andere configuratie-items, zoals eenheids- of dagmodellen, was toegewezen, dan wordt de naam van de activiteit in deze items met een _' aangegeven. Een verwijderde activiteit wordt weliswaar niet langer aan andere items toegewezen, maar blijft zichtbaar in de configuratiedata. Het is mogelijk dat je bestaande dagmodellen opnieuw moet aanmaken die de verwijderde activiteit bevatten. <!-- GPT translation -->

In Shift-Center worden verwijderde activiteiten {% link_new weergegeven met een gestippelde rand | features/scheduling/shiftcenter/shift-center-overview.md | #hoe-worden-items-weergegeven %}. In Schedules worden verwijderde activiteiten in een lichtere tekstkleur zonder naam weergegeven. De oorspronkelijke tijdsinformatie blijft zichtbaar, behalve in de dagweergave. <!-- GPT translation -->