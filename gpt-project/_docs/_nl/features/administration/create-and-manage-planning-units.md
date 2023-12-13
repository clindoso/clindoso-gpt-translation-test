---
title: Eenheden aanmaken en beheren
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lees hoe je eenheden aanmaakt, beheert en verwijdert.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-use-virtual-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
redirect_from:
  - /nl/planning-unit-configuration/
redirect_reason: Updated filename on 21 August 2023
---

In eenheden worden medewerkers en configuratiegegevens gegroepeerd voor planningsdoeleinden. Je bedrijfslocaties hoeven niet per se overeen te komen met je eenheden. Zo kunnen medewerkers die op twee verschillende locaties werkzaam zijn, aan één eenheid worden {% link_new toegewezen | features/administration/employee-overview.md | #medewerkerinstellingen-configureren %}. We raden aan om één enkele eenheid te gebruiken, tenzij:

- je medewerkers in verschillende tijdzones werken. Gebruik in dat geval één eenheid per tijdzone.
- planners binnen je bedrijf verantwoordelijk zijn voor afzonderlijke groepen medewerkers, zoals een afdeling.

In injixo Advanced en Enterprise WFM kun je aangepaste gebruikersrollen gebruiken om de toegang van gebruikers tot verschillende eenheden te beperken.

Als je met meerdere eenheden werkt, dan kun je een medewerker uit een eenheid tijdelijk aan een andere eenheid toewijzen. Lees meer over het {% link_new overplaatsen van medewerkers | features/administration/employee-overview.md | #medewerkers-overplaatsen %}.

## Eenheden aanmaken

1. Ga naar _Plan > Configuratie > Eenheden_{:.breadcrumbs}.
2. Klik in de linker bovenhoek op het pictogram Nieuw {% icon item-add | icon-only %}.  
   Aan de rechterkant verschijnt een configuratievenster.
3. Vul de volgende velden in:

   - **Naam**: Unieke naam voor de eenheid (max. 50 tekens).
   - **Afkorting**: Afkorting voor de naam (max. 25 tekens).
   - **Kleur**: Optionele kleur voor de eenheid. Je ziet de kleur in Schedules.
   - **Interval**: Beïnvloedt hoe gedetailleerd gegevens in Schedules worden weergegeven, bijv. dekking en personeelsbehoefte. Het interval van de eenheid mag niet langer zijn dan het interval van de import van je contact- en agentstatusgegevens. In het vervolgkeuzemenu worden intervallen van de eenheid in minuten weergegeven. Wij raden aan om **15 minuten** te gebruiken. Het interval kan niet meer worden gewijzigd nadat het is opgeslagen. Lees meer over {% link_new het importeren van gegevens via integraties | features/acd-integration/cloud/how-integrations-work.md %}.
   - **Superieure eenheid**: Optionele eenheid die de eenheid bevat die je nu aanmaakt. Lees meer over {% link_new superieure eenheden | best-practices/how-to-use-virtual-planning-units.md %}.
   - **Tijdzones**: Tijdzone van de eenheid. De tijdzone kan niet meer worden gewijzigd nadat de eenheid is opgeslagen. Lees meer over het {% link_new werken met tijdzones | best-practices/working-with-timezones.md %}.

     > Opmerking
     >
     > De geselecteerde tijdzone moet overeenkomen met de tijdzone van de workloads in Forecast. Is dat niet het geval, dan kun je alleen forecasts bekijken en geen personeelsbehoeften overdragen voor planningsdoeleinden. Een integratie past de geïmporteerde gegevens aan volgens de tijdzone van je workloads.

4. Klik op _OK_{:.doc-button}.  
   Je kunt nu openingstijden of activiteiten toevoegen of {% link_new dagmodellen beperken | features/administration/create-and-manage-planning-units.md | #dagmodellen-beperken %}.

### Openingstijden toevoegen

Om openingstijden aan een eenheid toe te voegen, moet je eerst {% link_new de eenheid aanmaken | features/administration/create-and-manage-planning-units.md | #eenheden-aanmaken %}.

Voor planningsdoeleinden moet je openingstijden aan je eenheid toevoegen. Openingstijden beperken de dagelijkse tijden waarvoor je de {% link_new personeelsbehoefte kunt berekenen | features/forecast/injixo-forecast/staff-requirement.md %} en {% link_new geoptimaliseerde planningen kunt maken | features/scheduling/schedules/schedules-optimized-schedules.md %}. <!-- special public holiday day types or part of the linked article? -->

1. Klik in de sectie **Openingstijden** in het configuratievenster van de eenheid op het pictogram Toevoegen {% icon item-add | icon-only %} om de openingstijden voor bepaalde dagtypes toe te voegen.  
   Er wordt een dialoogvenster geopend.
2. Selecteer in de sectie **Dagtypes** een of meerdere {% link_new dagtypes | features/administration/day-types.md %}.
3. Voer in de velden **vanaf** en **tot en met** de begin- en eindtijd in (24-uurs formaat). Als je bedrijf 24 uur per dag geopend is, voer dan in beide velden 00:00 in.
4. (Optioneel) Voer in de velden **geldig vanaf** en **geldig tot en met** een datumbereik in waarop de openingstijden van toepassing zijn. Als de openingstijden altijd van toepassing zijn, laat de velden dan leeg. Lees meer over {% link_new geldigheidsperiodes | features/administration/set-a-validity-period.md %}.
5. Klik op _Ok_{:.doc-button}.

Klik op het {% icon item-edit %} of het pictogram Verwijderen {% icon item-delete | icon-only %} om de openingstijden te bewerken of verwijderen.

### Activiteiten toevoegen

Om activiteiten aan een eenheid toe te voegen, moet je eerst de {% link_new eenheid aanmaken | features/administration/create-and-manage-planning-units.md | #eenheden-aanmaken %}.

Voor planningsdoeleinden moet je activiteiten toevoegen aan eenheden. Je kunt alleen medewerkers inplannen voor activiteiten die aan de eenheid zijn toegevoegd. Alle eenheden bevatten standaard de activiteit Aanwezigheid. Je kunt de activiteit Aanwezigheid niet verwijderen.

Volg de volgende stappen om activiteiten aan een eenheid toe te voegen:

1. Klik in de sectie **Activiteiten** in het configuratievenster van de eenheid op het pictogram Toevoegen {% icon item-add | icon-only %}.  
   Er wordt een dialoogvenster geopend.
2. Klik op de activiteit die je wilt toevoegen.
3. (Optioneel) Voer in de velden **geldig vanaf** en **geldig tot en met** een tijdsperiode in. De functionaliteit {% link_new Geoptialiseerde planningen maken | features/scheduling/schedules/schedules-optimized-schedules.md %} houdt rekening met deze activiteit binnen de tijdsperiode die je hebt ingevoerd. Als in allebei de velden de waarde 00:00 is ingevoerd, bepaalt injixo de openingstijden van de eenheid. Gebruikers met adminrechten kunnen dit standaardgedrag in instelling _48408_{:.id-label} wijzigen. _Houd rekening met de openingstijden in AutoScheduler_.
4. (optioneel) Voer een tijd in voor de velden Geldig vanaf en Geldig tot en met om de periode waarin de activiteit kan worden ingepland, te beperken. Laat Geldig vanaf en Geldig tot en met leeg om de activiteit onbeperkt beschikbaar te maken.
5. Klik op _OK_{:.doc-button}.

Klik op het {% icon item-edit %} of het pictogram Verwijderen {% icon item-delete | icon-only %} om een activiteit te bewerken of verwijderen.

### Multiactiviteiten toevoegen

Om een {% link_new multiactiviteit | features/administration/activity-types-and-properties.md | #deelactiviteiten %} aan een eenheid toe te voegen, dien je eerst alle deelactiviteiten toe te voegen. De multiactiviteit verschijnt vetgedrukt in de lijst met activiteiten. Multiactiviteiten zijn niet beschikbaar in injixo Essential WFM.

### Dagmodellen beperken

Alle {% link_new dagmodellen  | features/administration/daymodels/daymodel-creation.md %} zijn standaard toegewezen aan je eenheden. Als je niet al je dagmodellen in een eenheid gebruikt, dan kun je het aantal dagmodellen voor die betreffende eenheid beperken.

Het beperken van dagmodellen kan het planningsproces met de functionaliteit Geoptimaliseerde roosters maken versnellen. Je kunt de resterende dagmodellen wel gebruiken om diensten te genereren, rapporten aan te maken of geoptimaliseerde planningen te maken. Dit kan ertoe leiden dat de andere configuratiegegevens, zoals weektijdpatronen, meer onderhoud vergen. Als een dagmodel dat in gebruik is wordt verwijderd, dan heeft dit geen invloed op de planningen en diensten die met dat betreffende dagmodel zijn gemaakt.

> Opmerking
> 
> Als je alle dagmodellen in de eenheid verwijdert, dan kun je diensten alleen inplannen door handmatig activiteiten aan de planning toe te voegen of door {% link_new activiteiten aan dienstenreeksen toe te voegen  | features/administration/shift-sequences.md %}. Alle andere planningsbenaderingen, zoals het gebruik van de functionaliteit Geoptimaliseerde planning maken of werktijdpatroonmodellen zijn niet langer mogelijk.

Volg de volgende stappen om het aantal dagmodellen te beperken:

1. Ga naar _Plan > Configuratie > Eenheden_{:.breadcrumbs}.
2. Selecteer de eenheid die je wilt bewerken en scroll naar de sectie **Dagmodellen**.
3. Klik op het {% icon item-edit %} naast de standaard configuratieoptie **[Alle]** en selecteer een dagmodel. Je kunt ook op het pictogram Verwijderen {% icon item-delete | icon-only %} klikken om de optie **[Alle]** te verwijderen. Om het aantal dagmodellen te beperken, moet je de optie **[Alle]** vervangen of verwijderen. Je kunt dagmodellen slechts eenmaal aan een eenheid toevoegen.  
   Sla stap 3 over als je later meer dagmodellen wilt toewijzen.
4. Klik op het pictogram Toevoegen {% icon item-add | icon-only %} om meer dan een dagmodellen toe te wijzen.
5. Klik op _OK_{:.doc-button}.

Klik op het {% icon item-edit %} of het pictogram Verwijderen {% icon item-delete | icon-only %} om een dagmodel te bewerken of verwijderen.

## Eenheden verwijderen

> Waarschuwing
> 
> Als je een eenheid verwijdert, dan worden ook de bijbehorende planningen verwijderd.

1. Ga naar _Plan > Configuratie > Eenheden_{:.breadcrumbs}.
2. Klik in de lijst op een eenheid die je wilt verwijderen.
3. Om ervoor te zorgen dat planningsgegevens juist worden weergegeven, dien je de activiteiten te verwijderen en de toegewezen dagmodellen uit de eenheid te verwijderen voordat je deze verwijdert.
4. Klik op het pictogram Verwijderen {% icon item-delete | icon-only %} in de linkerbovenhoek.
5. Klik op _Ja_{:.doc-button} om te bevestigen.
