---
title: Medewerkersbehoefte bewerken of verwijderen
toc: false
product_label:
  - advanced
  - enterprise
description: Leer hoe je de vraagwaarde voor personeel van injixo bewerkt of verwijdert.
archive_ref: 20210819-en-employee-requirement
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

Personeelsbehoefteuren geven aan hoeveel mensen je op een bepaald tijdstip nodig hebt voor een activiteit. Maak personeelsbehoefteuren om planningen te maken met de functionaliteit **Geoptimaliseerde planning maken** or ze te optimaliseren  met **Joboptimalisatie** of **Pauzes optimaliseren**. <!-- GPT translation -->

Het genereren van personeelsbehoefte is de laatste stap in het forecastproces. In injixo Forecast kun je de automatisch gegenereerde behoeften gebruiken of een specifieke berekeningsmethode voor personeelsbehoeften uitvoeren. Zorg ervoor dat voor alle relevante activiteiten personeelsbehoeften zijn gegenereerd voordat je een planning maakt. <!-- GPT translation -->

## Bekijk en bewerk personeelsbehoefte <!-- GPT translation -->

In injixo kun je personeelsbehoefte op de volgende vier plaatsen bekijken: <!-- GPT translation -->

- _Forecast_{:.menu-item} <!-- GPT translation -->
- _Analyze > Dashboard_{:.breadcrumbs} <!-- GPT translation -->
- _Plan > Schedules_{:.breadcrumbs} <!-- GPT translation -->
- _Plan > Dienstrooster-Center_{:.breadcrumbs}  <!-- GPT translation -->

De volgende tabel bevat meer informatie over de instellingen die in elk tabblad beschikbaar zijn: <!-- GPT translation -->

<style>
table {
   margin-left: 0px; <!-- GPT translation -->
}
</style>

| Locatie  | Weergave | Bewerken | Verwijderen | <!-- GPT translation -->
| ------ |--------| -------- |-------- |
| _Forecast_{:.menu-item} | Ja | Ja | Ja | <!-- GPT translation -->
| _Analyze > Dashboard_{:.breadcrumbs} | Ja | Nee | Nee | <!-- GPT translation -->
| Plan > Schedules_{:.breadcrumbs} | Ja | Nee | Nee | <!-- GPT translation -->
| _Plan > Dienstrooster-Center_{:.breadcrumbs} | Ja | Ja | Nee | <!-- GPT translation -->

### Vereisten voor medewerkers in het Dienstrooster-Center bewerken <!-- GPT translation -->

1. Ga naar _Plan > Dienstrooster-Center_{:.breadcrumbs}. <!-- GPT translation -->
2. Selecteer onderin het paneel het tabblad **Activiteiten - Behoefte** of het tabblad **Activiteitoverzicht**.<br> <!-- GPT translation -->
   > No Data message in a cell <!-- GPT translation -->
   >
   > Als de onderste tabel de melding **Geen gegevens** bevat, selecteer dan in het vervolgkeuzemenu **Levels** aan de rechterkant (naast het pictogram) **Voortgang** of **Actueel**. <!-- GPT translation -->

3. Klik op het {% icon plus %} aan de linkerkant van elke tabel om eenheid te bekijken. <!-- GPT translation -->
4. Klik met de rechtermuisknop op een cel in de onderste tabel en selecteer **Beheer personeelsbehoefte**. <!-- GPT translation -->
5. Klik in het venster **Medewerkersvereiste bewerken** op een cel en voer de nieuwe waarde in. <!-- GPT translation -->
  Je kunt cellen niet bewerken die blauw zijn gemarkeerd, omdat ze verwijderde activiteiten voorstellen die nog steeds aan de eenheid zijn toegewezen. <!-- GPT translation -->

6\. (Optioneel) Om meerdere cellen tegelijkertijd te bewerken, kopieer je een rij met waarden uit je spreadsheet. Klik op een cel en beweeg de muis naar rechts. Druk op Ctrl+V om de waarden te plakken.<br> <!-- GPT translation -->
7. Klik op _OK_{:.doc-button}.

### Vereiste capaciteit van medewerkers in Forecast bewerken <!-- GPT translation -->

Om handmatig personeelsbehoefte te bewerken, voer je het script voor constante behoefte uit in _Forecast_{:.breadcrumbs}. Hieronder wordt beschreven hoe je het script configureert voor deze specifieke usecase. Zie voor meer informatie over de individuele configuratieopties het artikel {% link_new Constant requirement | features/forecast/requirement-scripts/requirement-constant.md %}. <!-- GPT translation -->

1. Ga naar _Forecast > Vraagscripts_{:.breadcrumbs}. <!-- GPT translation -->
2. Klik in de tegel **Anders - Constante behoefte** op _Openen_{:.doc-button}.<br> <!-- GPT translation -->
3. Configureer in het script-configuratievenster de volgende instellingen: <!-- GPT translation -->
   - In de sectie **Datum**: <!-- GPT translation -->
     - **Begindatum** <!-- GPT translation -->
     - **Aantal dagen**: Voer in voor hoeveel opeenvolgende dagen na de begindatum de gewijzigde personeelsbehoefte van toepassing is. <!-- GPT translation -->
    - **Geef voor elke dag van de week weer**: Selecteer **Nee**. <!-- GPT translation -->
     - **Aan een bestaande vereiste toevoegen**: Laat het selectievakje leeg. <!-- GPT translation -->
     - **Aantal dagen met tijdsbestekken**: Selecteer 1 om de personeelsbehoefte voor alle dagen binnen een datumbereik te bewerken. <!-- GPT translation -->
     - **Aantal tijdsperiodes per dag**: Selecteer het aantal tijdsperioden per dag waarvoor je de personeelsbehoefte wilt bewerken. (1 bijvoorbeeld als je de personeelsbehoefte voor de hele dag wilt bewerken, en 3 als je verschillende personeelsbehoeften voor de ochtend, middag en avond wilt invoeren). <!-- GPT translation -->
     - **Aantal activiteiten**: Selecteer het aantal activiteiten waarvoor je de personeelsbehoefte wilt bewerken. <!-- GPT translation -->
   - In de sectie **Gegevens**: <!-- GPT translation -->
     - **Eenheid** en **Activiteit**: Selecteer de relevante gegevens voor elke activiteit waarvan je de personeelsbehoefte wilt bewerken. <!-- GPT translation -->
     - **Agents**: Voer het aantal dat je als personeelsbehoefte wilt gebruiken in. <!-- GPT translation -->
     - **Begin** en **Einde**: Geef het tijdsbereik aan waarvoor je de personeelsbehoefte wilt bewerken. <!-- GPT translation -->
4. Klik op _OK_{:.doc-button}.

## Personeelsbehoefte verwijderen <!-- GPT translation -->

Het is in Injixo niet mogelijk om personeelsbehoeften te verwijderen. Je kunt de personeelsbehoeften op 0 zetten, dit heeft hetzelfde effect als 'verwijderen'. <!-- GPT translation -->

Je kunt de volgende twee opties gebruiken om de personeelsbehoefte op 0 in te stellen: <!-- GPT translation -->

- Volg de stappen om [de personeelsbehoefte in het Dienstrooster-Center te bewerken](#de-personeelsbehoefte-in-het-dienstrooster-center-bewerken) en voer of kopieer 0 in de relevante cellen. <!-- GPT translation -->
- Volg de stappen om [te werken in de dropdownmenu's Staff Requirements, Dag en tijd en Achtergrondinformatie in Forecas](#medewerkersbehoefte-in-forecast) en voer 0 in  het relevante cellen. <!-- GPT translation -->

>In de volgende afbeelding zie je de configuratie van het constante behoefte-script om de personeelsbehoefte in Forecast voor een hele kalenderdag te verwijderen (hier: Dag 1): <!-- GPT translation -->

{{ 3 | image: 'Voorbeeld van de configuratie voor het constant behoefte-script met één activiteit van 00:00 uur tot 00:00 uur en 0 behoefte', '80%' }} <!-- GPT translation -->