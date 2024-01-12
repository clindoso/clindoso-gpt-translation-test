---
title: Create activities this is the frontmatter.
toc: true this is the frontmatter.
product_label: this is the frontmatter.
  - essential this is the frontmatter.
  - advanced this is the frontmatter.
  - enterprise this is the frontmatter.
  - classic this is the frontmatter.
beta-feature: false this is the frontmatter.
description: Create activities to represent scheduled and unscheduled tasks in your company. this is the frontmatter.
related_articles: this is the frontmatter.
  - overwrite_title: Add title for untranslated source this is the frontmatter.
    filepath: features/administration/activity-examples.md this is the frontmatter.
  - overwrite_title: Add title for untranslated source this is the frontmatter.
    filepath: features/administration/activity-types-and-properties.md this is the frontmatter.
  - overwrite_title: Add title for untranslated source this is the frontmatter.
    filepath: features/administration/work-with-skills.md this is the frontmatter.
---

---

Om activiteiten te maken, bewerken en verwijderen, ga naar _Plan > Configuratie > Activiteiten_{:.breadcrumbs}. <!-- GPT translation -->

Taken vertegenwoordigen alle taken die gepland en gerapporteerd worden binnen je onderneming, zoals telefoontje, pauze, verlof of meetings. Je kunt zoveel taken aanmaken als je wilt. Het aantal taken is afhankelijk van hoeveel taken je wilt onderscheiden en het gewenste detailniveau. <!-- GPT translation -->

Activiteiten zijn een essentieel onderdeel van planning en roostering in injixo. Je kunt een activiteit toevoegen aan bijvoorbeeld {% link_new planningsunits | features/administration/create-and-manage-planning-units.md | #activiteiten-toevoegen %}, {% link_new dagmodellen | features/administration/daymodels/daymodel-basics.md %}, SLA-regels en rotaweergaven. Ook zijn ze onderdeel van roosters die worden beheerd in {% link_new Shift Center | features/scheduling/shiftcenter/add-and-delete-items.md %}, de {% link_new planningsassistenten | features/scheduling/assistants/assistants.md %} en in de {% link_new Dispatcher | features/scheduling/dispatcher/dispatcher.md %}. <!-- GPT translation -->

injixo bevat twee vooraf geconfigureerde, niet-verwijderbare activiteiten: <!-- GPT translation -->

- Vertaling: Deze activiteit wordt in dagmodellen als tijdelijke activiteit gebruikt. Tijdens het inplannen wordt deze activiteit door injixo door andere activiteiten vervangen die als in te plannen geconfigureerd zijn. <!-- GPT translation -->
- Verlof: deze activiteit wordt gebruikt om betaald verlof in te plannen met een minimum van één geselecteerde dag, dit op basis van het verlofsaldo van een persoon. Onbetaald verlof wordt aangemaakt als een aparte activiteit. <!-- GPT translation -->

## Een medewerker aanmaken <!-- TM 62 -->

2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 83 -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 84 -->
   - **Naam**: Unieke naam die je activiteit beschrijft. De afkorting wordt automatisch gegenereerd. <!-- GPT translation -->
   - **Type**: Het activiteitstype bepaalt hoe injixo activiteiten in de planning gebruikt en hoe ze in andere modules en in rapportages worden weergegeven. Meer informatie over de verschillende {% link_new activiteitstypen | features/administration/activity-types-and-properties.md | #activiteitstypen %}. <!-- GPT translation -->
| Kleur |  De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven.<br>De kleur kan je helpen om de lengte, het dagmodeltype of opgenomen activiteiten sneller te herkennen. | <!-- TM 61 -->
| Sneltoets | Optionele sneltoets die je helpt om het dagmodel sneller in het Dienstrooster-Center in te voeren. Lees meer over {% link_new sneltoetsen | best-practices/tips-on-shift-center-usage.md %}. | <!-- TM 70 -->
   - **Officiële naam en afkorting**: Een alternatieve naam die kan worden gebruikt in interne rapportages en integraties. injixo Me toont altijd de naam die je hebt ingevoerd bij **Naam**. <!-- GPT translation -->
3. Vink één of meer vakjes aan om verschillende {% link_new eigenschappen van activiteiten | features/administration/activity-types-and-properties.md | #activity-properties %} te definiëren. <!-- GPT translation -->
Als je Plannable controleert, kun je de {% link_new waarde 'Bepaal hoe belangrijk je planactiviteit is' | best-practices/importance-for-activities.md %} aanpassen. <!-- GPT translation -->
Als je Replaceable aanvinkt, kun je de {% link_new prioriteitwaarde | best-practices/priority-for-activities.md %} aanpassen. <!-- GPT translation -->
4. (Optioneel) {% link_new Vaardigheden toewijzen | features/administration/work-with-skills.md | #assign-skills-to-activities %} aan de activiteit. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

Lees meer over {% link_new activiteitstypen en -eigenschappen | features/administration/activity-types-and-properties.md %}. <!-- GPT translation -->

## Activiteitentype <!-- TM 65 -->

Je kunt op de ID van een activiteit klikken om de details te bekijken.  <!-- GPT translation -->
- Klik op een activiteit in de lijst **Activiteiten**. Het webadres in je browserbalk toont het ID van de geselecteerde activiteit (bijv. https://app.injixo.com/plan/configuration/activities/1234). <!-- GPT translation -->
- Gebruik de injixo API. Leer hoe je [activiteiten beheert met de injixo API](https://api.injixo.com/resources/activities/). <!-- GPT translation -->

## Multiactiviteiten en subactiviteiten <!-- GPT translation -->


Multiactiviteiten geven je de optie om werknemers met verschillende vaardigheden te roosteren wanneer een van die vaardigheden nodig is. Je maakt een activiteit een multiactiviteit door er andere activiteiten aan toe te voegen en deze als subactiviteit te definiëren. In de lijst van activiteiten zijn multiactiviteiten aangeduid met het symbool <em class="multiactivity-icon"></em>. <!-- GPT translation -->

Als een activiteit een subactiviteit is, kun je het gedeelte **Multiactiviteiten** zien als je erop klikt. Hier worden alle multiactiviteiten weergegeven waar de activiteit aan gekoppeld is. <!-- GPT translation -->

Als een activiteit er geen subactiviteit is, kun je bij de sectie **Subactiviteiten** van een activiteit pagina andere activiteiten selecteren om ze als subactiviteiten van de activiteit toe te voegen die je wilt aanpassen. De activiteit zelf wordt dan een multiactiviteit. <!-- GPT translation -->
Je kunt alleen subactiviteiten toewijzen aan een activiteit nadat je deze hebt gemaakt. <!-- GPT translation -->

## Externe systemen <!-- GPT translation -->

<!-- will be made obsolete by the new activity mapping page. Will require a separate article --> <!-- GPT translation -->

Je kunt activiteiten uit externe systemen aan een activiteit in injixo toewijzen. <!-- GPT translation -->
1. Selecteer een activiteit uit de lijst, scrol naar de sectie **Externe systemen** en klik op _Bewerken in WFM_{:.doc-button}. <!-- GPT translation -->
4. Ga naar de sectie **Externe Systemen**. <!-- TM 79 -->
4. Klik op het {% icon item-add %}. <!-- TM 97 -->
4. Selecteer een **extern systeem**, een **naam uit het externe systeem** en een **classificatie** in de keuzelijsten. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Je kunt een activiteit alleen koppelen aan één activiteit in injixo als het uit een extern systeem komt. <!-- GPT translation -->

## Een activiteit dupliceren <!-- GPT translation -->

Om een nieuwe activiteit met dezelfde algemene eigenschappen als een bestaande activiteit te maken, doorloop je de volgende stappen: <!-- GPT translation -->

1. In de lijst **Activiteiten** selecteer je een activiteit. <!-- GPT translation -->
2. Klik op **Activiteit dupliceren** onder de activiteit. <!-- GPT translation -->
Een **Activiteit aanmaken**-venster wordt geopend met vooraf aangevinkte selectievakjes. Aanvaarde vaardigheden en subactiviteiten worden niet gedupliceerd. <!-- GPT translation -->
3. Voer een **naam** voor de nieuwe activiteit in. <!-- GPT translation -->
4. (Optioneel) Verander de kleur en andere eigenschappen. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

## Een activiteit bewerken of verwijderen <!-- GPT translation -->

1. In de lijst **Activiteiten** selecteer je een activiteit. <!-- Repetition of GPT translation -->
- Om de activiteit te bewerken, bewerk de informatie die je wil aanpassen en klik op _Wijzigingen opslaan_{:.doc-button}. <!-- GPT translation -->
- Om de activiteit te verwijderen, klik je op _Activiteit verwijderen_{:.doc-button} onderaan aan de rechterkant. <!-- GPT translation -->

Als de verwijderde activiteit is toegewezen aan andere configuratie-items, zoals planningscategorieën of dagmodellen, verschijnt de naam van de activiteit cursief in deze items. Verwijderde activiteiten verliezen hun koppelingen naar andere items, maar blijven zichtbaar in configuratiegegevens. Bestaande dagmodellen die de verwijderde activiteit gebruiken, moeten mogelijk opnieuw worden gemaakt. <!-- GPT translation -->

In Shift Center worden verwijderde activiteiten met een stippellijn {% link_new omringd | features/scheduling/shiftcenter/shift-center-overview.md | #hoe-worden-items-weergegeven %}. In Schedules worden verwijderde activiteiten grijs weergegeven zonder de naam. De oorspronkelijke tijdinformatie blijft zichtbaar, behalve in de dagweergave. <!-- GPT translation -->