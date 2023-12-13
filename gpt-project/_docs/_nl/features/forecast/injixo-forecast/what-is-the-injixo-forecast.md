---
title: Wat is injixo Forecast?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Gebruik injixo Forecast om automatisch een forecast te berekenen voor het contactvolume en de AHT.
related_articles:
  - overwrite_title: Workloads aanmaken
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: De forecast handmatig aanpassen
    filepath: features/forecast/injixo-forecast/manual-adjustments.md
  - overwrite_title: Forecastversies opslaan
    filepath: features/forecast/injixo-forecast/store-forecast-versions.md
  - overwrite_title: Forecastgegevens als CSV-bestand downloaden
    filepath: features/forecast/injixo-forecast/download-forecast.md
---

injixo Forecast combineert historische gegevens met algoritmen om hoogwaardige forecasts te genereren. De algoritmen herkennen trends, patronen en fluctuaties in je gegevens. injixo Forecast maakt gebruik van een groot aantal soorten algoritmen, zoals ARIMA, Holt-Winters, exponentiële vereffening, regressie of gradient boosting. 

injixo Forecast selecteert automatisch het algoritme dat het meest geschikt is voor je gegevens. De forecast wordt gegenereerd voor 365 dagen en kan worden weergegeven in dag-, week-, maand- en jaaraanzichten.

injixo Essential WFM maakt gebruik van een basisalgoritme dat gemiddelde waarden in de historische gegevens gebruikt om een langetermijntrend en weekpatronen te herkennen.

## Een forecast genereren

Bekijk onze snelstartgids om te zien hoe je {% link_new een forecast genereert | getting-started/calculate-a-forecast.md %}. Elke nieuwe gegevensimport updatet de gegenereerde forecast; injixo Essential WFM genereert een keer per week een nieuwe forecast.

Opmerking: Als je gegenereerde forecast alleen herhaalde weekpatronen weergeeft, dan kan dit nog steeds de optimale forecast zijn. In dit geval legt het algoritme kortetermijnpatronen vast (voor niet-herhalende fluctuaties) en beschouwt langetermijnpatronen als niet relevant. Fluctuaties in de historische gegevens zijn niet altijd patronen.

## Gegevensvereisten

Voor injixo Forecast is het nodig dat je aangeboden contacten, gemiddelde afhandeltijd (AHT) en behandelde contacten importeert.

Voor basisworkloads in injixo Classic zijn minimaal twee weken aan historische gegevens nodig. Smart workloads kunnen een forecast genereren op basis van slechts een dag aan historische gegevens. Als er meer dan twee jaar aan gegevens beschikbaar zijn, dan werken smart workloads met maandelijkse en jaarlijkse fluctuaties, zoals seizoensperiodes.

Welke soort workloads voor jou beschikbaar zijn, is afhankelijk van je WFM-plan (Classic, Essential, Advanced of Enterprise WFM).

## Omgang met gegevens van een slechte kwaliteit

Om een nauwkeurige forecast te genereren, moeten historische gegevens zowel volledig (genoeg gegevens met zo min mogelijk gaten) en zuiver (vrij van niet-relevante patronen) zijn. Denk bijvoorbeeld aan onjuist gemarkeerde {% link_new gebeurtenissen of feestdagen | features/forecast/injixo-forecast/events-and-holidays.md %} die de kwaliteit van de forecast beïnvloeden.

Historische gegevens kunnen langdurige storingen bevatten, of er kunnen gegevens ontbreken voor een bepaalde tijdsperiode. Hoe dichter de ontbrekende gegevens bij de actuele datum liggen, hoe minder de kwaliteit van de forecast wordt beïnvloed. 

Hier zijn enkele tips voor het beheer van gegevens van een slechte kwaliteit, afhankelijk van hoe lang de periode met slechte of ontbrekende gegevens is:

| Tijdsbestek met gegevens van een slechte kwaliteit     | Tip                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Een paar dagen | Gebruik {% link_new events | features/forecast/injixo-forecast/events-and-holidays.md %} om de betreffende dagen als een storing te markeren en sluit ze uit van de berekening.                                  |
| Een paar weken    | Upload extra gegevens zonder gaten of niet-relevante patronen. |
| Meerdere weken of maanden  | Verwijder de gegevens die voorafgaan aan het gat. Importeer alleen de gegevens van na het gat.                            |

Opmerking: Als je geen aanvullende gegevens kunt uploaden of niet genoeg gegevens hebt van na het gat, dan proberen de Smart Forecast-algoritmen de negatieve invloed van de ontbrekende gegevens automatisch te minimaliseren.

> Controleer en zuiver gegevens voordat je deze importeert.
>
> Je kunt historische gegevens niet verwijderen. Neem contact op met je Customer Success-team indien nodig.

## Forecasts genereren voor lage contactvolumes

injixo Forecast kan forecasts genereren voor lage en hoge contactvolumes. Bij het genereren van een forecast op basis van gegevens met lage contactvolumes, kan injixo de dagelijkse patronen mogelijk niet herkennen. Hoewel het bijna nooit voorkomt, kan dit ertoe leiden dat er voor bepaalde dagen geen forecast wordt gegenereerd. Wanneer dit losse dagen betreft, raden wij je aan de forecast handmatig aan te passen. Indien dit vaker voorkomt, kun je:

- Meerdere queues toevoegen aan de workload (dit resulteert in hogere volumes).
- Een andere aanpak gebruiken om personeelsbehoefte voor het plannen, bijvoorbeeld. {% link_new een constante personeelsbehoefte genereren | features/forecast/requirement-scripts/requirement-constant.md %}.
