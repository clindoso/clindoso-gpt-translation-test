---
title: Dashboards beheren
permalink: /dashboards-overview/
promote-service: team-leader-training
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Gebruik dashboards om je contactvolume- en bezettingsgegevens te analyseren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/work-with-charts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

In _Analyze > Dashboards_{:.breadcrumbs} kun je dashboards aanmaken en weergeven met maximaal vier verschillende grafieken. Elke grafiek kan wordt gebruikt om meerdere tijdseries en datumbereiken weer te geven. Als je nog geen dashboard hebt, dan wordt deze pagina weergegeven in de bewerkingsmodus en kun je [een dashboard aanmaken](#dashboards-aanmaken).

- Om een bestaand dashboard weer te geven, selecteer je een dashboard in het vervolgkeuzemenu of typ je in het veld om te filteren.
- Beweeg de cursor over een grafiek in het dashboard om de waarden voor een specifiek interval weer te geven.
- Klik op het pictogram **Maximaliseren** rechtsboven om over te schakelen naar volledig scherm. <!-- GPT translation -->

Je kunt ook {% link_new wisselen tussen grafiek- en tabelweergave | features/monitoring/dashboards/work-with-charts.md %} met het Pictogram Tabel weergeven {% icon table-list | icon-only %} en het Pictogram Grafiek weergeven {% icon chart-view | icon-only %} in de rechterbovenhoek. <!-- GPT translation -->

## Dashboards aanmaken

1. Ga naar _Analyze > Dashboards_{:.breadcrumbs}. <!-- GPT translation -->
2. Selecteer **Nieuw dashboard maken** in het pictogram met drie stippen ({% icon ellipsis_v | icon-only %}) aan de rechterkant. <!-- GPT translation -->
3. Configureer de volgende velden: <!-- GPT translation -->
  - **Naam**: Unieke naam voor je dashboard. <!-- GPT translation -->
  - **Indeling**: Selecteer het aantal en de indeling van je diagrammen. <!-- GPT translation -->
  - **Ongetitelde grafiek**: Naam voor elke grafiek. De namen hoeven niet uniek te zijn. <!-- GPT translation -->
4. Selecteer voor elke grafiek een **datumbereik**. <!-- GPT translation -->
5. (Optioneel) Activeer de optie **Gebruik rollende datums** om de startdatum elke dag met één dag te verschuiven. <!-- GPT translation -->
6. Sleep- en servicetijdseries naar de diagrammen om verschillende key figures visueel weer te geven: <!-- GPT translation -->
   - **Workloads**: History, Forecast, Import and {% link_new forecast versions | features/forecast/injixo-forecast/store-forecast-versions.md %}.  <!-- GPT translation -->
   - **Eenheden**: Bezetting, personeelsbehoefte, dekking voor ingeplande diensten en activiteiten, plus aangevraagde diensten in Me. <!-- GPT translation -->
   - **WFM-rijen**: Workloadgegevens in WFM-rijen die je heeft opgeslagen door in de workload-pagina op _Forecast gebruiken_{:.doc-button} te klikken. Deze optie is mogelijk niet beschikbaar, afhankelijk van je WFM-plan. <!-- GPT translation -->

      > Opmerking <!-- GPT translation -->
      > <!-- GPT translation -->
      > - Het pictogram met de "i" in de legenda van een gegevensreeks wordt weergegeven als je geen gegevens hebt ingevoerd voor een bepaalde tijdsperiode. <!-- GPT translation -->
      > - In werkbelastingen kun je afhankelijk van jouw integratie speciale kerncijfers zien. Als je werkbelastingen alleen wachtrijen bevatten die afkomstig zijn van een [Genesys Cloud-integratie](/genesys-cloud-integration-installeren/), dan worden binnenkomsten zonder actie, het gemiddelde antwoordniveau en binnen service level aangenomen binnen de context weergegeven. <!-- GPT translation -->

7. Klik op _Opslaan_{:.doc-button}.<br>Klik op _Bewerkmodus afsluiten_{:.doc-button} om terug te keren naar de weergavemodus. <!-- GPT translation -->

### Een dashboard dupliceren <!-- GPT translation -->

Volg deze stappen om een nieuw dashboard aan te maken met dezelfde basiskenmerken als een bestaand dashboard: <!-- GPT translation -->
1. Ga naar _Analyze > Dashboards_{:.breadcrumbs}. <!-- Repetition of GPT translation -->
2. Selecteer in het vervolgkeuzemenu een dashboard. <!-- GPT translation -->
3. Select **Dashboard klonen** in de {% icon ellipsis_v | icon-only %}. <!-- GPT translation -->
4. Bewerk indien nodig de naam en configuratiegegevens. <!-- GPT translation -->
5. Klik op _Opslaan_{:.doc-button}. <!-- TM 100 -->

### Dashboards automatisch vernieuwen <!-- GPT translation -->

Je kunt het geselecteerde dashboard automatisch vernieuwen. Selecteer daarvoor een interval uit het vervolgkeuzemenu aan de rechterkant en klik op _{% icon "arrows-rotate" | icon-only %} Auto-Refresh_{:.doc-button}.<br>In de linker benedenhoek van het scherm zie je wanneer het dashboard voor het laatst is bijgewerkt. <!-- GPT translation -->

## Dashboards bewerken <!-- GPT translation -->

1. Ga naar _Analyze > Dashboards_{:.breadcrumbs}. <!-- Repetition of GPT translation -->
2. Selecteer in het vervolgkeuzemenu een dashboard. <!-- Repetition of GPT translation -->
3. Selecteer **Bewerken** vanaf het **meer opties-menu** {% icon more_vertical | icon-only %} aan de rechterkant. <!-- GPT translation -->
4. Bewerk het dashboard, pas de {% link_new tijdreeksen aan | features/monitoring/dashboards/work-with-charts.md | #tijdreeksen-aanpassen %} of {% link_new verwijder | features/monitoring/dashboards/work-with-charts.md | #tijdreeksen-verwijderen %} deze. <!-- GPT translation -->
5. Klik op **Opslaan**{:.doc-button}. Klik op **Bewerkingsmodus afsluiten**{:.doc-button} om terug te gaan naar de weergavemodus. <!-- GPT translation -->

## Dashboards verwijderen <!-- GPT translation -->

1. Ga naar _Analyze > Dashboards_{:.breadcrumbs}. <!-- Repetition of GPT translation -->
2. Selecteer in het vervolgkeuzemenu een dashboard. <!-- Repetition of GPT translation -->
3. Selecteer **Bewerken** vanaf het **meer opties-menu** {% icon more_vertical | icon-only %} aan de rechterkant. <!-- Repetition of GPT translation -->
4. Klik op **Verwijderen**{:.doc-button} rechtsonder in het scherm. <!-- GPT translation -->
5. Klik in het bevestigingsvenster op _Dashboard verwijderen_{:.doc-button}.<br> Klik op _Dashboard behouden_{:.doc-button} om de verwijdering af te breken. <!-- GPT translation -->

Als je het laatste dashboard verwijdert, wordt de pagina bewerkingsmodus. Deze blijft totdat je [een nieuw dashboard aanmaakt](#een-dashboard-aanmaken). <!-- GPT translation -->