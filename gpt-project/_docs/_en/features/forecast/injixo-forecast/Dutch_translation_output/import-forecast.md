---
title: Forecasts importeren <!-- GPT translation -->
description: Importeer een forecast van een externe bron in injixo Forecast. <!-- GPT translation -->
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Als je historische gegevens van een externe bron wilt gebruiken, voornamelijk een externe toepassing of gegevens van je klanten, dan kun je externe forecastgegevens in injixo Forecast importeren. <!-- GPT translation -->

Ben je nog niet vertrouwd met injixo Forecast? Maak je dan eerst vertrouwd met {% link_new de basisprincipes | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}. <!-- GPT translation -->

## Import voorbereiden <!-- GPT translation -->

### Vereisten <!-- GPT translation -->

Om een forecast te importeren, heb je minimaal nodig: <!-- GPT translation -->

- Een {% link_new integratie | features/acd-integration/cloud/how-integrations-work.md %} die gegevens importeert. <!-- GPT translation -->
- Een workload met een {% link_new queue | features/forecast/injixo-forecast/manage-workloads.md | #queues-and-channels %} <!-- GPT translation -->
   <!-- GPT translation -->
### Een queue aanmaken <!-- GPT translation -->

Om een queue aan te maken, moet je historische contactgegevens importeren met behulp van een integratie. Queues worden automatisch door integraties aangemaakt. <!-- GPT translation -->

Als je geen integratie hebt die continu historische gegevens importeert, maak dan een queue door een eenvoudige CSV-bestand te importeren: <!-- GPT translation -->

1. {% link_new Maak een CSV-integratie aan | features/acd-integration/cloud/add-csv-integration.md | #configure-a-new-csv-integration %}. <!-- GPT translation -->
   - Sla de installatiestap voor Cloud Link over. <!-- GPT translation -->
   - Selecteer in de sectie **Contactgegevens (optioneel)**. <!-- GPT translation -->
2. Maak een CSV-bestand voor contactgegevens aan met voor elke interval minimaal één regel, bv.: <!-- GPT translation -->
   ```
   Queue;Datum;Tijd;Inkomende oproepen;Beantwoorde oproepen;AHT <!-- GPT translation -->
   ForecastImportQueue;22-02-2022;02:02;2;2;2 <!-- GPT translation -->
   ```
3. {% link_new Importeer het CSV-bestand handmatig | features/acd-integration/cloud/add-csv-integration.md | #bestand-importeren-handmatig %}.   <!-- GPT translation -->
   De queue wordt aangemaakt na de import. <!-- GPT translation -->
   Gebruik deze queue om forecasts te importeren naar al je workloads. <!-- GPT translation -->

### De queue aan een workload toewijzen <!-- GPT translation -->

Bij het aanmaken van een workload is het nodig om er een queue aan toe te wijzen. Het is een essentieel onderdeel van het aanmaken en een vereiste om [een forecast te importeren](#een-forecast-importeren). Lees meer over hoe je {% link_new een workload aanmaakt | features/forecast/injixo-forecast/manage-workloads.md | #workloads-aanmaken %}. <!-- GPT translation -->

Je kunt een forecast importeren in een bestaande workload, of een van je queues aan een nieuwe workload toevoegen. <!-- GPT translation -->

### Eén vereiste voldoet niet aan de importvereisten. <!-- GPT translation -->

Je importgegevens moeten aan de volgende eisen voldoen: <!-- GPT translation -->

| Eisen                          | Details                                                                                                                            | <!-- GPT translation -->
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | <!-- GPT translation -->
| Tijdstempelformaat                     | JJJJ-MM-DD UU:MM                                                                                                                   | <!-- GPT translation -->
| Volumogegevens                          | Gehele getallen (integers)                                                                                                           | <!-- GPT translation -->
| AHT-gegevens                             | Hele getallen (integers) of decimalen (met een decimaalteken)                                                                  | <!-- GPT translation -->
| Opmaak voor koptekstregel                   | `Timestamp;Aangeboden;AHT` of met aangepaste tekst (bijvoorbeeld: `Timestamp;Aangeboden_aangepastetekst;AHT_aangepastetekst`).                                 | <!-- GPT translation -->
| Scheidingstekens                 | Puntkomma of komma (automatische detectie)                                                                                                 | <!-- GPT translation -->
| Maximale bestandsgrootte                    | 20 MB<br>Houd bestanden onder 20.000 rijen (aanbevolen).                                                                         | <!-- GPT translation -->
| Tijdzone                            | Moet overeenkomen met de tijdzone van de queue.                                                                                             | <!-- GPT translation -->
| Lengte interval                      | Moet overeenkomen met de intervalgrootte van de queue (15, 30 of 60 minuten).                                   | <!-- GPT translation -->


Je kunt ook {% link_new een forecast (of een forecastversie) downloaden | features/forecast/injixo-forecast/download-forecast.md %} in CSV-formaat en het gebruiken als een template voor je eigen importbestand. De forecast leest alleen de kolommen `Timestamp`, `Offered` en `AHT`. Andere kolommen, zoals `Offered_operational` en `AHT_operational` worden genegeerd. <!-- GPT translation -->

```
Tijd;Aangeboden op start Auto;Afhandeltijd (AHT) start Auto;Aangeboden operationeel;AHT operationeel <!-- GPT translation -->
2020-05-17 16:30;40;180;50;170 <!-- GPT translation -->
```

### Leemtes in de importgegevens aanvullen <!-- GPT translation -->

Er kunnen intervallen zonder gegevens optreden in je importbestanden. Het resulterende volume- of AHT-diagram toont de geïmporteerde waarden als nul (0). Lege rijen of waarden worden niet geïmporteerd. <!-- GPT translation -->

Als er geen gegevens zijn voor een of meer intervallen, bewerk je je CSV-bestand als volgt: <!-- GPT translation -->

- Laat Volume verlof en AHT leeg: <!-- GPT translation -->

  ```
  Timestamp;Was aangeboden;AHT <!-- GPT translation -->
  2020-05-17 15:00;30;210 <!-- GPT translation -->
  2020-05-17 15:15;; <!-- GPT translation -->
  2020-05-17 15:30;40;180 <!-- GPT translation -->
  ```

* Kolommen importeren met nullen: <!-- GPT translation -->

  ```
  Timestamp;Was aangeboden;AHT <!-- Repetition of GPT translation
  2020-05-17 15:00;30;210 <!-- Repetition of GPT translation
  2020-05-17 15:15;0;0 <!-- GPT translation -->
  2020-05-17 15:30;40;180 <!-- Repetition of GPT translation
  ```

- de hele rij weglaten: <!-- GPT translation -->

  ```
  Timestamp;Was aangeboden;AHT <!-- Repetition of GPT translation
  2020-05-17 15:00;30;210 <!-- Repetition of GPT translation
  2020-05-17 15:30;40;180 <!-- Repetition of GPT translation
  ```

## Een forecast importeren <!-- GPT translation -->

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} de forecast voor de workload waarvoor je een externe forecast wilt importeren. <!-- GPT translation -->
2. Selecteer in het drie-puntenmenu _![Contextmenu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} op de rechtermuisknop **Forecastgegevens importeren**. <!-- GPT translation -->
3. Klik op _Kies bestand_{:.doc-button} en selecteer het CSV-bestand dat je wilt importeren. <!-- GPT translation -->
4\. Klik op _Gegevens importeren_{:.doc-button}.<br> <!-- GPT translation -->
   Het venster wordt vernieuwd en geeft aan of de import wel of niet is geslaagd. <!-- GPT translation -->
5. Klik op _Gereed_{:.doc-button}.<br> <!-- GPT translation -->
Vernieuw de pagina om de geüpdate grafiek voor de importperiode te bekijken. De geïmporteerde waarden worden als bruine lijn in de grafieken in de secties Volume en AHT getoond. <!-- GPT translation -->
   Klik op het pictogram Weergeven/verbergen {% icon eye | icon-only %} in de legenda naast **Import** om de geïmporteerde forecast in de grafiek te verbergen. <!-- GPT translation -->