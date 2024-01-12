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

Om activiteiten te maken, te bewerken en om te verwijderen, ga je naar _Plan > Configuratie > Activiteiten_{:.breadcrumbs}. <!-- GPT translation -->

Activiteiten vertegenwoordigen alle taken die gepland en gerapporteerd worden in je bedrijf, zoals telefoon, pauze, afwezigheid, of meetings. Je kunt zoveel activiteiten creëren als je wilt. Het aantal activiteiten is afhankelijk van hoeveel taken je wilt onderscheiden en van het gewenste detailniveau. <!-- GPT translation -->

Activiteiten spelen een centrale rol bij plannings- en roostertaken in injixo. Ze zijn gelinkt aan andere configuratie-items, zoals aan {% link_new planningsreeksen | features/administration/create-and-manage-planning-units.md | #activiteiten-toevoegen %}, {% link_new dagmodellen | features/administration/daymodels/daymodel-basics.md %}, en maken deel uit van de roosters beheerd in het {% link_new Shift Center | features/scheduling/shiftcenter/add-and-delete-items.md %} of in de {% link_new rostereditor | features/scheduling/schedules/schedules-edit.md %}. <!-- GPT translation -->

injixo bevat twee voorgeconfigureerde (niet verwijderbare) activiteiten: <!-- GPT translation -->

- Vertaling: Deze activiteit wordt als tijdelijke activiteit gebruikt in dagentypes. Tijdens het plannen vervangt injixo deze activiteit door andere activiteiten die als planbaar zijn geconfigureerd. <!-- GPT translation -->
- Verlof: Deze activiteit wordt gebruikt om betaald verlof in te plannen op basis van iemands verlofsaldo. Maak onbetaald verlof aan met de aparte activiteit 'andere afwezigheden'. <!-- GPT translation -->

## Een medewerker aanmaken <!-- TM 62 -->

2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 83 -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 84 -->
   - **Naam**: Unieke naam om je activiteit te beschrijven. De afkorting wordt automatisch gegenereerd. <!-- GPT translation -->
   - **Type**: Het activiteitstype bepaalt hoe injixo gebruikmaakt van activiteiten bij de planning en hoe deze in andere modules en rapporten worden weergegeven. Meer informatie over de verschillende {% link_new activiteitstypen | features/administration/activity-types-and-properties.md | #activiteitstypen %}. <!-- GPT translation -->
| Kleur |  De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven.<br>De kleur kan je helpen om de lengte, het dagmodeltype of opgenomen activiteiten sneller te herkennen. | <!-- TM 61 -->
| Sneltoets | Optionele sneltoets die je helpt om het dagmodel sneller in het Dienstrooster-Center in te voeren. Lees meer over {% link_new sneltoetsen | best-practices/tips-on-shift-center-usage.md %}. | <!-- TM 70 -->
- **Officiële naam en afkorting**: Alternatieve naam die kan worden gebruikt voor interne rapportage en integraties. injixo Me toont altijd de naam die is ingevoerd bij **Naam**. <!-- GPT translation -->
3. Vink één of meerdere selectievakjes aan om verschillende {% link_new activiteitseigenschappen | features/administration/activity-types-and-properties.md | #activiteitseigenschappen %} in te stellen. <!-- GPT translation -->
Als je Plannable bekijkt, kun je de {% link_new importance-waarde|best-practices-nl/importance-for-activities.md%} bewerken. <!-- GPT translation -->
Als je Replaceable controleert, kun je de [{% link_new priority waarde | best-practices/priority-for-activities.md %}] aanpassen. <!-- GPT translation -->
4. (Optioneel) {% link_new Vaardigheden toewijzen | features/administration/work-with-skills.md | #assign-skills-to-activities %} aan de activiteit. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

Lees meer over {% link_new activiteitstypen en -eigenschappen  | features/administration/activity-types-and-properties.md %}. <!-- GPT translation -->

## Activiteitentype <!-- TM 65 -->

Om de ID van een activiteit te zien, kun je: <!-- GPT translation -->
- Klik op een bezigheid in de lijst met **Bezigheden**. Het URL in je browsertabblad toont de ID van de geselecteerde bezigheid (bijvoorbeeld https://www.injixo.com/plan/configuration/activities/1234). <!-- GPT translation -->
- Gebruik de injixo API. Leer hoe je [activiteitenbeheer kan uitvoeren met de injixo API](https://api.injixo.com/resources/activities/). <!-- GPT translation -->

## Multiactiviteiten en subactiviteiten <!-- GPT translation -->


Een multiactiviteit maakt het mogelijk om mensen in te plannen voor verschillende vaardigheden wanneer één vaardigheid nodig is. Je kunt een activiteit omvormen tot een multiactiviteit door er {% link_new andere activiteiten | features/administration/activity-types-and-properties.md | #subactiviteiten %} aan toe te wijzen. De toegewezen activiteiten worden de subactiviteiten. In de activiteitenlijst zijn multiactiviteiten herkenbaar aan het icoon <em class="multiactivity-icon"></em>. <!-- GPT translation -->

Als een activiteit een subactiviteit is, zie je wanneer je erop klikt de sectie **Multiactiviteiten** waarin alle multiactiviteiten worden weergegeven waar deze aan gekoppeld is. <!-- GPT translation -->

Als een activiteit niet onder een andere activiteit valt, kun je, wanneer je erop klikt, het gedeelte **Subactiviteiten** zien. Hier kun je andere activiteiten selecteren die onder de activiteit die je aan het bewerken bent zullen vallen. De activiteit zelf verandert dan in een multiactiviteit. <!-- GPT translation -->
Je kunt pas subactiviteiten toewijzen aan een activiteit nadat je de activiteit hebt aangemaakt. <!-- GPT translation -->

## Externe systemen <!-- GPT translation -->

<!-- will be made obsolete by the new activity mapping page. Will require a separate article -->

Je kunt activiteiten van externe systemen koppelen aan een activiteit in injixo. <!-- GPT translation -->
1. Selecteer een activiteit uit de lijst, scrol naar de sectyie **Externe systemen** en klik op _Bewerken in WFM_{:.doc-button}. <!-- GPT translation -->
4. Ga naar de sectie **Externe Systemen**. <!-- TM 79 -->
4. Klik op het {% icon item-add %}. <!-- TM 97 -->
Selecteer alle velden die je wilt toevoegen met behulp van de vervolgkeuzemenu's **Extern systeem**, **Naam uit extern systeem** en **Classificatie**. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Het is alleen mogelijk om een activiteit uit een extern systeem één keer toe te wijzen aan een activiteit in injixo. <!-- GPT translation -->

## Activiteit dupliceren <!-- GPT translation -->

Om een nieuwe activity met dezelfde algemene eigenschappen aan te maken als een bestaande activity, volg je deze stappen: <!-- GPT translation -->

1. In de **Activiteiten**-lijst selecteert u een activiteit. <!-- GPT translation -->
2. Klik op **Activiteit dupliceren** onder de naam van de activiteit. <!-- GPT translation -->
Een nieuw venster **Nieuwe activiteit maken** wordt geopend met vooraf aangevinkte selectievakjes toegewezen vaardigheden en deelactiviteiten worden niet gedupliceerd. <!-- GPT translation -->
3. Voer een **Naam** in voor de nieuwe activiteit. <!-- GPT translation -->
4. (Optioneel) Verander de kleur en andere eigenschappen. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

## Activiteit bewerken of verwijderen <!-- GPT translation -->

1. In de **Activiteiten**-lijst selecteert u een activiteit. <!-- Repetition of GPT translation -->
- Om de activiteit te bewerken pas je de gewenste informatie aan en klik je op _Wijzigingen opslaan_{:.doc-button}. <!-- GPT translation -->
- Om de activiteit te verwijderen, klik op _Verwijder activiteit_{:.doc-button} rechtsonder. <!-- GPT translation -->

Als de verwijderde activiteit aan andere configuratie-items is toegewezen, zoals planningsunits of dagmodellen, wordt de naam van de verwijderde activiteit nu cursief weergegeven op deze items. Een verwijderde activiteit verliest haar toewijzingen aan andere items, maar blijft zichtbaar in de configuratiedata. Je moet mogelijk wel opnieuw bestaande dagmodellen aanmaken die de verwijderde activiteit bevatten. <!-- GPT translation -->

Shift Center toont verwijderde activiteiten {% link_new omgeven door een gestreepte lijn | features/scheduling/shiftcenter/shift-center-overview.md | #how-are-items-displayed %}. In Schemabeheer worden verwijderde activiteiten in grijstinten getoond zonder hun naam. Oorspronkelijke tijdsaanduidingen blijven zichtbaar, dit geldt niet voor de dagweergave. <!-- GPT translation -->