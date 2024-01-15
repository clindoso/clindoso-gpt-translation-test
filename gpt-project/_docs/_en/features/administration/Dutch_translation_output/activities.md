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

Voor het aanmaken, bewerken en verwijderen van activiteiten ga je naar _Plan > Configuratie > Activiteiten_{:.breadcrumbs}. <!-- GPT translation -->

Activiteiten omvatten alle taken die in uw bedrijf worden ingepland en gerapporteerd, zoals telefonie, pauze, vrije tijd, of vergaderingen. U kunt zoveel activiteiten aanmaken als u wilt. De hoeveelheid activiteiten die u kunt aanmaken is uitsluitend afhankelijk van hoe gedetailleerd u de rapportage wilt hebben en hoeveel verschillende taken u wilt kunnen onderscheiden. <!-- GPT translation -->

Activiteiten zijn een essentieel onderdeel van de planning en de roostering binnen injixo. Ze zijn gekoppeld aan andere configuratie-items, bijvoorbeeld aan {% link_new planningsgroepen | features/administration/create-and-manage-planning-units.md | #activiteiten-toevoegen %}, {% link_new dagentypes | features/administration/daymodels/daymodel-basics.md %}. Activiteiten spelen ook een rol in de roosters die je maakt in het {% link_new planbord | features/scheduling/shiftcenter/add-and-delete-items.md %} of in {% link_new Roosters | features/scheduling/schedules/schedules-edit.md %}. <!-- GPT translation -->

injixo bevat twee vooraf geconfigureerde (niet-verwijderbare) activiteiten: <!-- GPT translation -->

- Vertaling: Deze activiteit fungeert als placeholder-activiteit in dagmodellen. Tijdens het plannen vervangt injixo deze activiteit door een andere activiteit die geconfigureerd is als Inplanbaar. <!-- GPT translation -->
- Vakantie: geef met dit type aan welke betaalde vakantie  werknemers volgens hun vakantieaanspraken opnemen. Geef onbetaald verlof aan met de activiteit Onbetaald verlof. <!-- GPT translation -->

## Een medewerker aanmaken <!-- TM 62 -->

2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 83 -->
2. Voeg de algemene informatie toe voor je workload: <!-- TM 84 -->
   - **Naam**: Unieke naam om jouw activiteit te beschrijven. De afkorting wordt automatisch gegenereerd. <!-- GPT translation -->
   - **Type**: De activiteitstypen bepalen de functie van activiteiten in de planning en hoe deze activiteiten in overige modules en rapportages worden afgebeeld. Meer informatie over de verschillende {% link_new activiteitstypen | features/administration/activity-types-and-properties.md | #activiteitstypen %}. <!-- GPT translation -->
| Kleur |  De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven.<br>De kleur kan je helpen om de lengte, het dagmodeltype of opgenomen activiteiten sneller te herkennen. | <!-- TM 61 -->
| Sneltoets | Optionele sneltoets die je helpt om het dagmodel sneller in het Dienstrooster-Center in te voeren. Lees meer over {% link_new sneltoetsen | best-practices/tips-on-shift-center-usage.md %}. | <!-- TM 70 -->
   - **Officiële naam en afkorting**: Alternatieve naam die kan worden gebruikt voor interne rapportages en integraties. injixo Me toont altijd de naam die is ingevoerd onder **Naam**. <!-- GPT translation -->
3. Vink een of meer selectievakjes aan om verschillende {% link_new eigenschappen van een activiteit | features/administration/activity-types-and-properties.md | #activiteitseigenschappen %} in te stellen. <!-- GPT translation -->
Als je Plannable gebruikt kun je de {% link_new belang-waarde | best-practices/importance-for-activities.md %} bewerken. <!-- GPT translation -->
Als je een vervangbare activiteit controleert, kun je de {% link_new prioriteitswaarde | best-practices/priority-for-activities.md %} bewerken. <!-- GPT translation -->
4. (Optioneel) {% link_new Vakken toewijzen | features/administration/work-with-skills.md | #assign-skills-to-activities %} aan de activiteit. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

Bekijk hier meer informatie over de {% link_new activity types en properties | features/administration/activity-types-and-properties.md %}. <!-- GPT translation -->

## Activiteitentype <!-- TM 65 -->

Om het ID van een activiteit te zien, voer je de volgende stappen uit: <!-- GPT translation -->
- Klik op een activiteit in de lijst **Activities**. Het adres in je browservenster toont het ID van de geselecteerde activiteit (bijv. https://www.injixo.com/plan/configuration/activities/1234). <!-- GPT translation -->
- Gebruik de injixo API. Leer hoe je [activiteiten beheert via de injixo API](https://api.injixo.com/resources/activities/). <!-- GPT translation -->

## Multiactiviteiten en subactiviteiten <!-- GPT translation -->


Multiactiviteiten stellen je in staat om roostersamenstellingen voor medewerkers met verschillende vaardigheden te maken wanneer een van die vaardigheden nodig is. Je kunt een activiteit in een multiactiviteit veranderen door het {% link_new aan andere activiteiten arbeidsplannen te koppelen | features/administration/activity-types-and-properties.md | #subactiviteiten %}. Deze activiteiten worden dan de subactiviteiten van de multiactiviteit.  In de lijst met activiteiten zijn multiactiviteiten herkenbaar aan het <em class="multiactivity-icon"></em> pictogram. <!-- GPT translation -->

Als een activiteit een subactiviteit is, kun je wanneer je erop klikt de paragraaf **Multibestanden** zien, waarin alle multibestanden worden weergegeven waaraan de subactiviteit is gekoppeld. <!-- GPT translation -->

Als een activiteit zelf geen subactiviteit is, kun je, wanneer je erop klikt, de sectie **Subactiviteiten** zien. Hier kun je andere activiteiten selecteren om subactiviteiten van de activiteit die je bewerkt te worden. De activiteit zelf wordt dan een multiactiviteit. <!-- GPT translation -->
Je kunt alleen subactiviteiten aan een activiteit toewijzen nadat je de activiteit hebt aangemaakt. <!-- GPT translation -->

## Externe systemen <!-- GPT translation -->

<!-- will be made obsolete by the new activity mapping page. Will require a separate article -->

Je kunt activiteiten uit externe systemen koppelen aan een activiteit in injixo. <!-- GPT translation -->
1. Selecteer een activiteit uit de lijst, scroll naar de sectie **Externe systemen**, en klik op _'Bewerken in SPM'_{:.doc-button}. <!-- GPT translation -->
4. Ga naar de sectie **Externe Systemen**. <!-- TM 79 -->
4. Klik op het {% icon item-add %}. <!-- TM 97 -->
4. Selecteer een **extern systeem**, een **naam uit het externe systeem** en een **classificatie** uit de vervolgkeuzemenu's. <!-- GPT translation -->
5. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

Je kan een activiteit uit een extern systeem alleen toewijzen aan een activiteit in injixo als deze leeg is en nog niet toegewezen is. <!-- GPT translation -->

## Een activiteit dupliceren <!-- GPT translation -->

Om een nieuwe activiteit met dezelfde algemene eigenschappen als een bestaande activiteit te maken, dien je de volgende stappen te volgen: <!-- GPT translation -->

1. In de lijst met **Activiteiten** selecteer je een activiteit. <!-- GPT translation -->
2. Klik op **Activiteit repliceren** onder de activiteitsnaam. <!-- GPT translation -->
Er wordt een nieuw venster **Activiteit maken** geopend met voorgevinkte selectievakjes. Toegekende vaardigheden en subactiviteiten worden niet gedupliceerd. <!-- GPT translation -->
3. Voer een **Naam** in voor de nieuwe activiteit. <!-- GPT translation -->
4. (Optioneel) Wijzig de kleur en andere eigenschappen. <!-- GPT translation -->
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}. <!-- TM 81 -->

## Activiteit bewerken of verwijderen <!-- GPT translation -->

1. In de lijst met **Activiteiten** selecteer je een activiteit. <!-- Repetition of GPT translation -->
- Om de activiteit aan te passen, pas je de informatie aan die je wilt wijzigen en klik je op _Wijzigingen opslaan_{:.doc-button}. <!-- GPT translation -->
- Om de activiteit te verwijderen, klik je rechtsonder op _Activiteit verwijderen_{:.doc-button}. <!-- GPT translation -->

Als de verwijderde activiteit is toegewezen aan andere configuratie-items, zoals planningsgroepen of dagmodellen, wordt de naam cursief weergegeven in de betreffende items. Een verwijderde activiteit verliest de toewijzing aan andere items, maar blijft zichtbaar in de configuratiegegevens. Het kan zijn dat je bestaande dagmodellen opnieuw moet maken waarin de verwijderde activiteit is meegenomen. <!-- GPT translation -->

In Shift Center worden verwijderde activiteiten {% link_new omlijst door een stippellijn | features/scheduling/shiftcenter/shift-center-overview.md | #hoe-worden-items-getoond %}. In Schedules worden verwijderde activiteiten weergegeven in grijs, zonder naam. De originele tijdinformatie blijft zichtbaar, behalve in de dagweergave. <!-- GPT translation -->