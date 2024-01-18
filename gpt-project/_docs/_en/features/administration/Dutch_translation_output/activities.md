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

Ga naar _Plan > Configuratie > Activiteiten_{:.breadcrumbs} om activiteiten toe te voegen, bewerken of verwijderen. <!-- GPT translation -->

Activiteiten vertegenwoordigen alle taken die zijn ingepland en geregistreerd worden in je bedrijf, denk bijvoorbeeld aan telefonie, pauze, verlof en vergaderingen. Je kunt zoveel activiteiten aanmaken als je wilt. Het aantal activiteiten is alleen afhankelijk van het aantal taken dat je wilt onderscheiden en het gewenste detailniveau. <!-- GPT translation -->

Activiteiten zijn een essentieel onderdeel van het plannings- en roosterproces in injixo. Ze zijn verbonden met andere configuratie-items, bijvoorbeeld met {% link_new eenheidsgroepen | features/administration/create-and-manage-planning-units.md | #activiteiten-toevoegen %}, {% link_new dagmodellen | features/administration/daymodels/daymodel-basics.md %}. Ze maken ook deel uit van de planningen die in het {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/add-and-delete-items.md %} of in {% link_new Planningen | features/scheduling/schedules/schedules-edit.md %} worden beheerd. <!-- GPT translation -->

injixo bevat twee vooraf geconfigureerde (niet-verwijderbare) activiteiten: <!-- GPT translation -->

- Aanwezig: Deze activiteit wordt in dagmodellen als placeholderteken gebruikt. Tijdens het roosteren vervangt injixo deze activiteit door andere activiteiten die zijn geconfigureerd als inplanbaar. <!-- GPT translation -->
- Vakantie: Deze activiteit wordt gebruikt om betaalde vakantie in te plannen op basis van het vakantierecht van een medewerker. Plan onbetaalde verlofdagen in als afzonderlijke activiteit. <!-- GPT translation -->

## Een medewerker aanmaken <!-- TM 62 -->

5. Klik op _Workload aanmaken_{:.doc-button}. <!-- TM 66 -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 84 -->
   - **Naam**: Unieke naam om je activiteit te beschrijven. De afkorting wordt automatisch gegenereerd. <!-- GPT translation -->
   - **Type**: Het activiteitentype bepaalt hoe injixo activiteiten bij het plannen gebruikt en hoe ze in andere modules en rapportages worden weergegeven. Lees meer over de verschillende {% link_new activiteitentypen | features/administration/activity-types-and-properties.md | #activiteitentypen %}. <!-- GPT translation -->
| Kleur |  De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven.<br>De kleur kan je helpen om de lengte, het dagmodeltype of opgenomen activiteiten sneller te herkennen. | <!-- TM 61 -->
| Sneltoets | Optionele sneltoets die je helpt om het dagmodel sneller in het Dienstrooster-Center in te voeren. Lees meer over {% link_new sneltoetsen | best-practices/tips-on-shift-center-usage.md %}. | <!-- TM 70 -->
   - **Officiële naam en afkorting**: Alternatieve naam die kan worden gebruikt voor interne rapportages en integraties. injixo Me geeft altijd de naam weer die is ingevoerd onder **Naam**. <!-- GPT translation -->
3. Vink een of meer selectievakjes aan om verschillende {% link_new activiteiteneigenschappen | features/administration/activity-types-and-properties.md | #activiteiteneigenschappen %} in te stellen. <!-- GPT translation -->
Als je Plannable raadpleegt, kun je de {% link_new belangwaarde | best-practices/importance-for-activities.md %} bewerken. <!-- GPT translation -->
Als je Vervangbaar selecteert, kun je de {% link_new prioriteitswaarde | best-practices/priority-for-activities.md %} bewerken. <!-- GPT translation -->
4. (Optioneel) {% link_new Wijs kwalificaties toe | features/administration/work-with-skills.md | #assign-skills-to-activities %} aan de activiteit. <!-- GPT translation -->
5. Klik op _Workload aanmaken_{:.doc-button}. <!-- TM 80 -->

Lees meer over {% link_new activiteitentypen en eigenschappen | features/administration/activity-types-and-properties.md %}. <!-- GPT translation -->

## Activiteitentype <!-- TM 65 -->

Ga als volgt te werk om de ID van een activiteit te bekijken: <!-- GPT translation -->
- Klik op een activiteit in de lijst **Activiteiten**. In de URL van de adresbalk van je browser wordt zo het ID van de geselecteerde activiteit weergegeven (bijv. https://www.injixo.com/plan/configuration/activities/1234). <!-- GPT translation -->
- Gebruik de injixo API. Lees hoe je [activiteiten via de injixo API beheert](https://api.injixo.com/resources/activities/). <!-- GPT translation -->

## Multiactiviteiten en subactiviteiten  <!-- GPT translation -->


Met multiactiviteiten kun je medewerkers met verschillende kwalificaties inplannen als een van deze kwalificaties nodig is. Je kunt een activiteit tot een multiactiviteit maken door {% link_new andere activiteiten toe te wijzen | features/administration/activity-types-and-properties.md | #deelactiviteiten %}. De toegewezen activiteiten worden de deelactiviteiten van de multiactiviteit.  In de lijst met activiteiten worden multiactiviteiten aangegeven met het <em class="multiactivity-icon"></em>-pictogram. <!-- GPT translation -->

Als een activiteit een subactiviteit is, dan wordt bij het klikken op **Meerkeuzeactiviteit** de sectie **Meerkeuzeactiviteiten** weergegeven, waar alle meerkeuzeactiviteiten worden weergeven waaraan ze is toegewezen. <!-- GPT translation -->

Als een activiteit geen deelactiviteit is, dan verschijnt na een klik de sectie **Deelactiviteiten**. Hier selecteer je andere activiteiten die deelactiviteit van de activiteit worden die je op dat moment bewerkt. De activiteit op zich wordt dan een multi-activiteit. <!-- GPT translation -->
Je kunt pas een deelactiviteit aan een activiteit toewijzen nadat je de activiteit hebt aangemaakt. <!-- GPT translation -->

## Externe systemen <!-- GPT translation -->

<!-- will be made obsolete by the new activity mapping page. Will require a separate article -->

Je kunt activiteiten uit externe systemen aan een activiteit in injixo toewijzen. <!-- GPT translation -->
1. Selecteer een activiteit uit de lijst, scrol naar de sectie **Externe systemen** en klik op _Bewerken in WFM_{:.doc-button}. <!-- GPT translation -->
4. Ga naar de sectie **Externe Systemen**. <!-- TM 79 -->
3. Klik op het {% icon item-add %}. <!-- GPT translation -->
4. Selecteer in de vervolgkeuzemenu's een **extern systeem**, een **naamuit het externe systeem** en een **classificatie**. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

> Je kunt een activiteit uit een extern systeem alleen eenmalig aan een activiteit in injixo toewijzen. <!-- GPT translation -->

## Een activiteit dupliceren <!-- GPT translation -->

Volg deze stappen om een nieuwe activiteit met dezelfde algemene eigenschappen als een bestaande activiteit aan te maken: <!-- GPT translation -->

1. Selecteer een activiteit in de lijst met **Activiteiten**. <!-- GPT translation -->
2. Klik op **Activiteit dupliceren** onder de naam van de activiteit. <!-- GPT translation -->
Er wordt een **Nieuwe activiteit aanmaken**-venster geopend met vooraf aangevinkte selectievakjes. Toegewezen kwalificaties en deelactiviteiten worden niet gedupliceerd. <!-- GPT translation -->
3. Voer een **Naam** in voor de nieuwe activiteit. <!-- GPT translation -->
4. (Optioneel) Wijzig de kleur en andere eigenschappen. <!-- GPT translation -->
5. Klik op _Workload aanmaken_{:.doc-button}. <!-- TM 80 -->

## Een activiteit bewerken of verwijderen <!-- GPT translation -->

1. Selecteer een activiteit in de lijst met **Activiteiten**. <!-- Repetition of GPT translation
  - Om de activiteit te bewerken, bewerk je de informatie die je wilt wijzigen en klik je op _Gemaakte wijzigingen opslaan_{:.doc-button}. <!-- GPT translation -->
  - Klik op _Activiteit verwijderen_{:.doc-button} onder in het venster om de activiteit te verwijderen. <!-- GPT translation -->

Als de verwijderde activiteit aan andere items zoals eenheidsmodellen of dagmodellen was toegewezen, dan wordt de naam van de activiteit in deze items cursief weergegeven. Een verwijderde activiteit raakt de toewijzingen aan andere items kwijt, maar blijft zichtbaar in de configuratiegegevens. Mogelijk dien je bestaande dagmodellen opnieuw aan te maken die de verwijderde activiteit bevatten. <!-- GPT translation -->

In Shift Center worden verwijderde activiteiten {% link_new weergegeven in een gestreept kader | features/scheduling/shiftcenter/shift-center-overview.md | #weergave-van-items %}. In Schedules worden verwijderde activiteiten in grijs weergegeven, maar zonder de naam. De oorspronkelijke tijdsinformatie blijft zichtbaar, behalve in de dagweergave. <!-- GPT translation -->