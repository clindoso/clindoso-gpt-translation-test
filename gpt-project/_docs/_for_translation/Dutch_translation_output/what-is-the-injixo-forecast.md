---
title: Wat is injixo Forecast? <!-- TM 100 -->
redirect_from:
  - /forecast_overview/
  - /general-functionality/
redirect_reason: redirect for intercom forecast tour, 2nd link, renamed article in june 2021
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Gebruik injixo Forecast om automatisch een forecast te berekenen voor het contactvolume en de AHT. <!-- TM 100 -->
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manual-adjustments.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/store-forecast-versions.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/download-forecast.md
gpt_translation: true
---

injixo Forecast neemt je historische gegevens als basis en werkt deze uit met behulp van algoritmes om nauwkeurige forecasts te genereren. De algoritmes herkennen trends, patronen en fluctuaties die in je gegevens opgenomen zijn. injixo Forecast maakt hiervoor gebruik van verschillende soorten algoritmes, zoals ARIMA, Holt-Winters, exponentiële gladstrijking, regressie of gradient boosting. <!-- GPT translation -->

injixo Forecast kiest automatisch het algoritme dat het beste bij jouw gegevens past. injixo maakt een forecast aan voor 365 dagen na het importeren van de gegevens. <!-- GPT translation -->

injixo Essential WFM maakt gebruik van een basisalgoritme dat gemiddelde waarden in de historische gegevens gebruikt om een langetermijntrend en weekpatronen te herkennen. <!-- TM 100 -->

## Een forecast genereren <!-- TM 100 -->

Bekijk onze snelstartgids om te zien hoe je {% link_new een forecast genereert | getting-started/calculate-a-forecast.md %}. Elke nieuwe gegevensimport updatet de gegenereerde forecast; injixo Essential WFM genereert een keer per week een nieuwe forecast. <!-- TM 100 -->

Opmerking: Als je gegenereerde forecast alleen herhaalde weekpatronen weergeeft, dan kan dit nog steeds de optimale forecast zijn. In dit geval legt het algoritme kortetermijnpatronen vast (voor niet-herhalende fluctuaties) en beschouwt langetermijnpatronen als niet relevant. Fluctuaties in de historische gegevens zijn niet altijd patronen. <!-- TM 100 -->

## Gegevensvereisten <!-- TM 100 -->

Voor injixo Forecast is het nodig dat je aangeboden contacten, gemiddelde afhandeltijd (AHT) en behandelde contacten importeert. <!-- TM 100 -->

Voor basisworkloads in injixo Classic zijn minimaal twee weken aan historische gegevens nodig. Smart workloads kunnen een forecast genereren op basis van slechts een dag aan historische gegevens. Als er meer dan twee jaar aan gegevens beschikbaar zijn, dan werken smart workloads met maandelijkse en jaarlijkse fluctuaties, zoals seizoensperiodes. <!-- TM 100 -->

Welke soort workloads voor jou beschikbaar zijn, is afhankelijk van je WFM-plan (Classic, Essential, Advanced of Enterprise WFM). <!-- TM 100 -->

## Omgang met gegevens van een slechte kwaliteit <!-- TM 100 -->

Om een nauwkeurige forecast te genereren, moeten historische gegevens compleet zijn (genoeg gegevens met zo min mogelijk hiaten) en zuiver (vrij van irrelevante patronen). Zo heeft een foutieve markering van {% link_new gebeurtenissen of feestdagen | features/forecast/injixo-forecast/events-and-holidays.md %} een negatieve invloed op de foreacastkwaliteit. <!-- GPT translation -->

Historische gegevens kunnen ontbrekende of beschadigde en verkeerd gelabelde gegevens bevatten.  <!-- GPT translation -->

Hier zijn enkele tips voor het beheer van gegevens van een slechte kwaliteit, afhankelijk van hoe lang de periode met slechte of ontbrekende gegevens is: <!-- TM 100 -->

| Tijdsbestek met gegevens van een slechte kwaliteit     | Tip                                                                                                                                                         | <!-- TM 100 -->
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Een paar dagen | Gebruik {% link_new events | features/forecast/injixo-forecast/events-and-holidays.md %} om de betreffende dagen als een storing te markeren en sluit ze uit van de berekening.                                  | <!-- TM 100 -->
| Een paar weken    | Upload extra gegevens zonder gaten of niet-relevante patronen. | <!-- TM 100 -->
| Meerdere weken of maanden  | Verwijder de gegevens die voorafgaan aan het gat. Importeer alleen de gegevens van na het gat.                            | <!-- TM 100 -->

Opmerking: Als je geen aanvullende gegevens kunt uploaden of niet genoeg gegevens hebt van na het gat, dan proberen de Smart Forecast-algoritmen de negatieve invloed van de ontbrekende gegevens automatisch te minimaliseren. <!-- TM 100 -->

> Controleer en zuiver gegevens voordat je deze importeert. <!-- TM 100 -->
>
> Je kunt historische gegevens niet verwijderen. Neem contact op met je Customer Success-team indien nodig. <!-- TM 100 -->

## Forecasts genereren voor lage contactvolumes <!-- TM 100 -->

injixo Forecast kan forecasts genereren voor lage en hoge contactvolumes. Bij het genereren van een forecast op basis van gegevens met lage contactvolumes, kan injixo de dagelijkse patronen mogelijk niet herkennen. Hoewel het bijna nooit voorkomt, kan dit ertoe leiden dat er voor bepaalde dagen geen forecast wordt gegenereerd. Wanneer dit losse dagen betreft, raden wij je aan de forecast handmatig aan te passen. Indien dit vaker voorkomt, kun je: <!-- TM 100 -->

- Meerdere queues toevoegen aan de workload (dit resulteert in hogere volumes). <!-- TM 100 -->
- Een andere aanpak gebruiken om personeelsbehoefte voor het plannen, bijvoorbeeld. {% link_new een constante personeelsbehoefte genereren | features/forecast/requirement-scripts/requirement-constant.md %}. <!-- TM 100 -->