---
title: Activiteiten aanmaken
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
beta-feature: false
description: Maak activiteiten aan die de geplande en ongeplande taken in je bedrijf weergeven.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Voor het aanmaken, bewerken en verwijderen van activiteiten ga je naar _Plan > Configuratie > Activiteiten_{:.breadcrumbs}.

Activiteiten staan voor alle taken die binnen je bedrijf worden ingepland en gerapporteerd, zoals telefonie, pauze, verlof of meetings.<br>
Je kunt zoveel activiteiten aanmaken als je wilt. Het aantal activiteiten is alleen afhankelijk van het aantal taken dat je wilt onderscheiden en hoe ver je de taken wilt specificeren.<br>
Activiteiten zijn een essentieel onderdeel van je planning in injixo. Ze zijn gekoppeld aan andere configuratie-items, zoals {% link_new eenheden | features/administration/create-and-manage-planning-units.md | #activiteiten-toevoegen %} en {% link_new dagmodellen | features/administration/daymodels/daymodel-basics.md %}. Ze maken ook deel uit van de planningen die in het {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/add-and-delete-items.md %} en in {% link_new Schedules | features/scheduling/schedules/schedules-edit.md %} worden beheerd.

injixo bevat twee voorgeconfigureerde (niet-verwijderbare) activiteiten:<br>
- Aanwezigheid: Deze activiteit wordt in dagmodellen als placeholder-activiteit gebruikt. Tijdens het plannen vervangt injixo deze activiteit door andere activiteiten die als Planbaar zijn geconfigureerd.
- Vakantie: Deze activiteit wordt gebruikt om betaald verlof in te plannen op basis van de verlofrechten van een medewerker. Onbetaald verlof dient als afzonderlijke activiteit te worden aangemaakt.

## Een activiteit aanmaken

1. Klik op _Nieuwe activiteit_{:.doc-button}.
2. Voeg algemene informatie toe voor je activiteit:
   - **Naam**: Unieke naam om je activiteit te beschrijven. De afkorting wordt automatisch gegenereerd.
   - **Type**: Het type activiteit bepaalt hoe injixo activiteiten tijdens het plannen gebruikt en hoe deze in andere modules en rapporten worden weergegeven. Lees meer over {% link_new activiteitentypen | features/administration/activity-types-and-properties.md | #activiteitentype %}.
   - **Kleur**: De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven. Het helpt je om de verschillende activiteiten van elkaar te onderscheiden.
   - **Sneltoets**: Optionele sneltoets waarmee je de activiteit sneller in Shift Center kunt invoeren. Meer informatie over {% link_new sneltoetsen | best-practices/tips-on-shift-center-usage.md | #tip-2-shortcuts-for-a-quick-assignment-of-activities %}.
   - **Officiële naam en officiële afkorting**: Alternatieve naam die voor interne rapportages en integraties kan worden gebruikt. injixo Me geeft altijd de naam weer die je onder **Naam** hebt ingevoerd.
3. Vink een of meerdere selectievakjes aan om verschillende {% link_new opties voor de activiteit | features/administration/activity-types-and-properties.md | #activiteiteneigenschappen %} in te stellen.
  Als je Planbaar aanvinkt, dan kun je de waarde bij {% link_new Rang | best-practices/importance-for-activities.md %} bewerken.
  Als je Vervangbaar selecteert, dan kun je de waarde bij {% link_new Prioriteit | best-practices/priority-for-activities.md %} bewerken.
4. (Optioneel) {% link_new Wijs kwalificaties toe | features/administration/work-with-skills.md | #kwalificaties-aan-activiteiten-toevoegen %} aan de activiteit.
5. Klik op _Activiteit aanmaken_{:.doc-button}.

Lees meer over {% link_new activiteitentypen en -eigenschappen | features/administration/activity-types-and-properties.md %}.

### Activiteiten-ID

Om de ID van een activiteit te zien, kun je: 
- In de lijst met **Activiteiten** op een activiteit klikken. De URL in je browser geeft de ID van de geselecteerde activiteit weer (bijvoorbeeld https://www.injixo.com/plan/configuration/activities/1234).
- De injixo-API gebruiken. Lees hoe je [activiteiten beheert via de injixo-API](https://api.injixo.com/resources/activities/).

## Multiactiviteiten en deelactiviteiten 


Met multiactiviteiten kan injixo medewerkers inplannen die meerdere kwalificaties hebben als een van hun kwalificaties nodig is. Je kunt van een activiteit een multiactiviteit maken door er {% link_new andere activiteiten aan toe te wijzen | features/administration/activity-types-and-properties.md | #deelactiviteiten %}. De toegewezen activiteiten worden dan deelactiviteiten. In de lijst met activiteiten worden multiactiviteiten gemarkeerd met een <em class="multiactivity-icon"></em>.

Als je op een deelactiviteit klikt, dan krijg je de sectie **Multiactiviteiten** te zien, waarin alle multiactiviteiten worden weergegeven waaraan de deelactiviteit is toegewezen.

Als je op een activiteit klikt die geen deelactiviteit is, dan krijg je de sectie **Deelactiviteiten** te zien. Hier kun je andere activiteiten als deelactiviteit toevoegen aan de activiteit die je aan het bewerken bent. De activiteit zelf wordt in dat geval een multiactiviteit.
Je kunt deelactiviteiten alleen aan een activiteit toewijzen nadat je deze hebt aangemaakt.

## Externe systemen

<!-- will be made obsolete by the new activity mapping page. Will require a separate article -->

Je kunt activiteiten van externe systemen koppelen aan een activiteit in injixo.
1. Selecteer een activiteit uit de lijst, scroll naar de sectie **Externe systemen** en klik op _Bewerken in WFM_{:.doc-button}. 
2. Ga naar de sectie **Externe systemen**.
3. Klik op het {% icon item-add %}.
4. Selecteer in de vervolgkeuzemenu's een **extern systeem**, **aanduiding activiteit extern systeem** en **classificatie**.
5. Klik op _OK_{:.doc-button}.

> Je kunt een activiteit uit een extern systeem slechts één keer aan een enkele activiteit in injixo toevoegen.

## Een activiteit kopiëren

Volg de volgende stappen om een activiteit met dezelfde algemene eigenschappen als een bestaande activiteit te kopiëren:

1. Selecteer een activiteit uit de lijst met **Activiteiten**.
2. Klik onder de naam van de activiteit op **Activiteit kopiëren**.
Het venster **Nieuwe activiteit aanmaken** met vooraf aangevinkte selectievakjes wordt geopend. Toegewezen activiteiten en deelactiviteiten worden niet gekopieerd.
3. Voer een **naam** in voor de nieuwe activiteit.
4. (Optioneel) Wijzig de kleur en andere eigenschappen.
5. Klik op _Activiteit aanmaken_{:.doc-button}.

## Een activiteit bewerken of verwijderen

1. Selecteer een activiteit uit de lijst met **Activiteiten**.
  - Om de activiteit te bewerken, bewerk je de gegevens die je wilt wijzen en klik je vervolgens op _Wijzigingen opslaan_{:.doc-button}.
  - Om de activiteit te verwijderen, klik je rechtsonder op _Activiteit verwijderen_{:.doc-button}.

Als de verwijderde activiteit aan andere configuratie-items was toegewezen, zoals eenheden of dagmodellen, dan wordt de naam van de activiteit in deze items cursief weergegeven. Een verwijderde activiteit is niet langer toegewezen aan andere items, maar blijft wel zichtbaar in de configuratiegegevens. Eventuele dagmodellen waarin de verwijderde activiteit was opgenomen, moeten opnieuw worden aangemaakt.<br>
In het Dienstrooster-Center worden verwijderde activiteiten {% link_new oncirkeld met een stippellijn | features/scheduling/shiftcenter/shift-center-overview.md | #how-are-items-displayed %}.<br>
In Schedules worden verwijderde activiteiten uitgegrijsd en zonder naam weergegeven. De originele tijdinformatie blijft zichtbaar, behalve in het dagoverzicht.
