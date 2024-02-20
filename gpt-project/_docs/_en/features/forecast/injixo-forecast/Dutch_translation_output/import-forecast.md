---
title: Forecasts importeren <!-- GPT translation -->
description: Een forecast uit een externe bron importeren naar injixo Forecast. <!-- GPT translation -->
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Als je historische gegevens wilt gebruiken die zijn gegenereerd door een externe bron, zoals een externe toepassing of je door je klanten, dan kun je externe forecasts in injixo Forecast importeren. <!-- TM 100 -->

Ben je nog niet zo vertrouwd met injixo Forecast? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}. <!-- TM 100 -->

## De import voorbereiden <!-- TM 100 -->

### Vereisten <!-- TM 100 -->

Om een forecast te importeren, heb je in ieder geval het volgende nodig: <!-- TM 100 -->

- Een {% link_new integratie | features/acd-integration/cloud/how-integrations-work.md %} die gegevens importeert. <!-- TM 100 -->
- Een workload met een {% link_new queue | features/forecast/injixo-forecast/manage-workloads.md | #queues-en-kanalen %}. <!-- TM 100 -->
  <!-- GPT translation -->
### Een queue aanmaken <!-- TM 100 -->

Om een queue aan te maken, moet je via een integratie historische contactgegevens importeren. Queues worden automatisch door integraties gegenereerd. <!-- TM 100 -->

Als je nog geen integratie hebt die continu historische gegevens importeert, maak dan een queue aan door een eenovudig CSV-bestand te importeren. <!-- TM 100 -->

1. {% link_new Stel een CSV-integratie in | features/acd-integration/cloud/add-csv-integration.md | #een-nieuwe-csv-integratie-configureren %}. <!-- TM 100 -->
   - Sla tijdens de installatie de stap voor het installeren van Cloud Link over. <!-- TM 100 -->
   - Selecteer **Contactgegevens** in de sectie **CSV-schemaconfiguratie**. <!-- TM 100 -->
2. Maak een CSV-bestand aan voor contactgegegevens met minimaal één regel voor een enkele interval, bijvoorbeeld: <!-- TM 100 -->
    ```
   Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT <!-- TM 100 -->
ForecastImportQueue;22/02/2022;02:02;2;2;2 <!-- TM 100 -->
    ```
3. {% link_new Importeer het CSV-bestand handmatig | features/acd-integration/cloud/add-csv-integration.md | #csv-bestand-handmatig-importeren %}.   <!-- GPT translation -->
   De queue wordt naar de import vernoemd. <!-- TM 100 -->
   Gebruik deze queue om forecasts in al je workloads te importeren. <!-- TM 100 -->

### De queue aan een workload toewijzen <!-- TM 100 -->

Bij het aanmaken van een workload moet je een queue aan een workload toewijzen. Dit is een integraal onderdeel van het aanmaakproces, dat vereist is om [een forecast te importeren](#een-forecast-importeren). Lees meer over hoe je {% link_new een workload aanmaakt | features/forecast/injixo-forecast/manage-workloads.md | #workloads-aanmaken %}. <!-- TM 100 -->

Je kunt een forecast in een bestaande workload importeren of een van je queues aan een nieuwe workload toevoegen. <!-- TM 100 -->

### Vereisten voor importgegevens <!-- TM 100 -->

Je importgegevens moeten aan de volgende criteria voldoen: <!-- TM 100 -->

| Vereiste                          | Details                                                                                                                            | <!-- TM 100 -->
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | <!-- TM 100 -->
| Tijdstempelformaat                     | YYYY-MM-DD HH:MM                                                                                                                   | <!-- TM 100 -->
| Volumegegevens                          | Hele getallen (integers)                                                                                                           | <!-- TM 100 -->
| AHT-gegevens                             | Hele getallen (integers) of decimale getallen (met een decimale komma)                                                                  | <!-- TM 100 -->
| Formaat kopregel                   | `Timestamp;Offered;AHT` of met aangepaste tekst (bijvoorbeeld: `Timestamp;Offered_customtext;AHT_customtext`).                                 | <!-- TM 100 -->
| Scheidingstekens                 | Puntkomma of komma (automatische herkenning)                                                                                                 | <!-- TM 100 -->
| Maximale bestandsgrootte                    | 20 MB<br>Zorg ervoor dat bestanden niet meer dan 20.000 regels bevatten (aanbevolen).                                                                         | <!-- TM 100 -->
| Tijdzone                            | Moet overeenkomen met de tijdzone van de queue                                                                                             | <!-- TM 100 -->
| Intervallengte                      | Moet overeenkomen met de intervallengte van de queue (15, 30 of 60 minuten)                                                               | <!-- TM 100 -->


Je kunt ook {% link_new een forecast (of een forecastversie) | features/forecast/injixo-forecast/download-forecast.md %} in CSV-formaat downloaden en gebruiken als sjabloon voor je eigen importbestand. De forecast leest alleen de kolommen `Timestamp`, `Offered` en `AHT`. Overige kolommen, zoals `Offered_operational` en `AHT_operational` in het onderstaande voorbeeld, worden genegeerd. <!-- TM 100 -->

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational <!-- TM 100 -->
2020-05-17 16:30;40;180;50;170 <!-- TM 100 -->
```

### Omgaan met ontbrekende importgegevens <!-- TM 100 -->

Je importbestanden kunnen intervallen zonder gegevens bevatten. Het resulterende volume en de AHT-grafiek geven geïmporteerde waarden als nul (0) weer. Lege rijen of ontbrekende waarden worden niet geïmporteerd. <!-- TM 100 -->

Als er voor een of meerdere intervallen geen gegevens beschikbaar zijn, dan kun je je CSV-bestand als volgt bewerken: <!-- TM 100 -->

- Laat het volume en AHT weg: <!-- TM 100 -->

  ```
  Timestamp;Offered;AHT <!-- TM 100 -->
  2020-05-17 15:00;30;210 <!-- TM 100 -->
  2020-05-17 15:15;; <!-- TM 100 -->
  2020-05-17 15:30;40;180 <!-- TM 100 -->
  ```

- Importkolommen gevuld met nullen: <!-- TM 100 -->

  ```
  Timestamp;Offered;AHT <!-- TM 100 -->
  2020-05-17 15:00;30;210 <!-- TM 100 -->
  2020-05-17 15:15;0;0 <!-- TM 100 -->
  2020-05-17 15:30;40;180 <!-- TM 100 -->
  ```

- Laat de hele rij weg: <!-- TM 100 -->

  ```
  Timestamp;Offered;AHT <!-- TM 100 -->
  2020-05-17 15:00;30;210 <!-- TM 100 -->
  2020-05-17 15:30;40;180 <!-- TM 100 -->
  ```

## Een forecast importeren <!-- GPT translation -->

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} de workload waarvoor je een externe forecast wilt importeren. <!-- GPT translation -->
2. Selecteer in het menu met de drie stipjes _![Contextmenu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} in de rechterbovenhoek de optie **Forecastgegevens importeren**. <!-- GPT translation -->
3. Klik op _Kies bestand_{:.doc-button} en selecteer het CSV-bestand dat je wilt importeren. <!-- GPT translation -->
4. Klik op _Gegevens importeren_{:.doc-button}.<br> <!-- GPT translation -->
   Het venster wordt bijgewerkt en geeft aan of het importeren wel of niet is gelukt. <!-- GPT translation -->
5. Klik op *Gereed*.{:.doc-button} <!-- GPT translation -->
Vernieuw de pagina om de bijgewerkte grafiek voor de importperiode te bekijken. De geïmporteerde waarden worden in de secties Volume en AHT in de grafieken weergegeven als een bruine lijn. <!-- GPT translation -->
   Om de geïmporteerde forecast in de grafiek te verbergen, klik je het pictogram Weergeven/verbergen {% icon eye | icon-only %} in de legenda naast **Import**. <!-- GPT translation -->