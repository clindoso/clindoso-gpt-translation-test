---
title: Forecasts importeren
description: Importeer een forecast van een externe bron in injixo Forecast.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Als je historische gegevens wilt gebruiken die zijn gegenereerd door een externe bron, zoals een externe toepassing of je door je klanten, dan kun je externe forecasts in injixo Forecast importeren.

Ben je nog niet zo vertrouwd met injixo Forecast? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## De import voorbereiden

### Vereisten

Om een forecast te importeren, heb je in ieder geval het volgende nodig:

- Een {% link_new integratie | features/acd-integration/cloud/how-integrations-work.md %} die gegevens importeert.
- Een workload met een {% link_new queue | features/forecast/injixo-forecast/manage-workloads.md | #queues-en-kanalen %}.
 
### Een queue aanmaken

Om een queue aan te maken, moet je via een integratie historische contactgegevens importeren. Queues worden automatisch door integraties gegenereerd.

Als je nog geen integratie hebt die continu historische gegevens importeert, maak dan een queue aan door een eenovudig CSV-bestand te importeren.

1. {% link_new Stel een CSV-integratie in | features/acd-integration/cloud/add-csv-integration.md | #een-nieuwe-csv-integratie-configureren %}.
   - Sla tijdens de installatie de stap voor het installeren van Cloud Link over.
   - Selecteer **Contactgegevens** in de sectie **CSV-schemaconfiguratie**.
2. Maak een CSV-bestand aan voor contactgegegevens met minimaal één regel voor een enkele interval, bijvoorbeeld:
   ```
   Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
ForecastImportQueue;22/02/2022;02:02;2;2;2
   ```
3. {% link_new Importeer het CSV-bestand handmatig | features/acd-integration/cloud/add-csv-integration.md | #handmatige-bestandsimport %}.
   De queue wordt naar de import vernoemd.
   Gebruik deze queue om forecasts in al je workloads te importeren.

### De queue aan een workload toewijzen

Bij het aanmaken van een workload moet je een queue aan een workload toewijzen. Dit is een integraal onderdeel van het aanmaakproces, dat vereist is om [een forecast te importeren](#een-forecast-importeren). Lees meer over hoe je {% link_new een workload aanmaakt | features/forecast/injixo-forecast/manage-workloads.md | #workloads-aanmaken %}.

Je kunt een forecast in een bestaande workload importeren of een van je queues aan een nieuwe workload toevoegen.

### Vereisten voor importgegevens

Je importgegevens moeten aan de volgende criteria voldoen: 

| Vereiste                          | Details                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Tijdstempelformaat                     | YYYY-MM-DD HH:MM                                                                                                                   |
| Volumegegevens                          | Hele getallen (integers)                                                                                                           |
| AHT-gegevens                             | Hele getallen (integers) of decimale getallen (met een decimale komma)                                                                  |
| Formaat kopregel                   | `Timestamp;Offered;AHT` of met aangepaste tekst (bijvoorbeeld: `Timestamp;Offered_customtext;AHT_customtext`).                                 |
| Scheidingstekens                 | Puntkomma of komma (automatische herkenning)                                                                                                 |
| Maximale bestandsgrootte                    | 20 MB<br>Zorg ervoor dat bestanden niet meer dan 20.000 regels bevatten (aanbevolen).                                                                         |
| Tijdzone                            | Moet overeenkomen met de tijdzone van de queue                                                                                             |
| Intervallengte                      | Moet overeenkomen met de intervallengte van de queue (15, 30 of 60 minuten)                                                               |


Je kunt ook {% link_new een forecast (of een forecastversie) | features/forecast/injixo-forecast/download-forecast.md %} in CSV-formaat downloaden en gebruiken als sjabloon voor je eigen importbestand. De forecast leest alleen de kolommen `Timestamp`, `Offered` en `AHT`. Overige kolommen, zoals `Offered_operational` en `AHT_operational` in het onderstaande voorbeeld, worden genegeerd.

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
2020-05-17 16:30;40;180;50;170
```

### Omgaan met ontbrekende importgegevens

Je importbestanden kunnen intervallen zonder gegevens bevatten. Het resulterende volume en de AHT-grafiek geven geïmporteerde waarden als nul (0) weer. Lege rijen of ontbrekende waarden worden niet geïmporteerd.

Als er voor een of meerdere intervallen geen gegevens beschikbaar zijn, dan kun je je CSV-bestand als volgt bewerken:

- Laat het volume en AHT weg:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:15;;
2020-05-17 15:30;40;180
  ```

- Importkolommen gevuld met nullen:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:15;0;0
2020-05-17 15:30;40;180
  ```

- Laat de hele rij weg:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:30;40;180
  ```

## Een forecast importeren

1. Ga naar _Forecast_{:.menu-item}.
2. Selecteer in het vervolgkeuzemenu bovenaan de **Workload** waarin je de externe forecast wilt importeren.
3. Klik rechtsboven in de sectie **Volume en AHT** op het pictogram met de drie puntjes {% icon ellipsis_v | icon-only %}.
4. Selecteer **Forecastgegevens importeren**.
5. Klik op _Bestand kiezen_{:.doc-button} en selecteer het CSV-bestand dat je wilt importeren.
6. Klik op _Start importeren_{:.doc-button}.
   De pagina wordt automatisch bijgewerkt en geeft aan of de import geslaagd is of niet.
7. Klik op _Klaar_{:.doc-button}.<br>
Vernieuw de pagina om de nieuwe grafiek te bekijken voor de geïmporteerde periode. Deze wordt boven de forecast in de sectie **Volume en AHT** met een paarse lijn weergegeven.
   Om de geïmporteerde forecast in de grafiek te verbergen, klik je op het pictogram Weergeven/verbergen {% icon eye | icon-only %} in de legenda naast **Importeren**.
