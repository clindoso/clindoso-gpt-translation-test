---
title: Forecast-Versionen speichern
description: Speichere Forecasts in Forecast-Versionen, um sie mit dem tatsächlichen Volumen zu vergleichen. Diese Informationen kannst du für kurz- und langfristiges Forecasting verwenden.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
redirect_from:
  - de/versions/
redirect_reason: Updated filename on 29 March 2023
---

Mit Forecast-Versionen kannst du Forecast-Werte für bestimmte Zeiträume speichern. Verwende Forecast-Versionen, um den ursprünglichen Forecast mit den aktuellen Werten zu vergleichen. So kannst du sehen, wie andere Faktoren, wie z.&nbsp;B. Ereignisse, deine Forecasts beeinflussen. Du kannst eine Forecast-Version auch als Grundlage für die {% link_new Berechnung des Mitarbeiterbedarfs | features/forecast/injixo-forecast/calculate-staff-requirements.md %} verwenden oder Daten aus einer Forecast-Version in {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %} anzeigen.

## Forecast-Version speichern

In injixo gibt es zwei Forecast-Versionen:

- Operativ: Nutze diese Version für kurzfristige Forecasts zum Berechnen des Mitarbeiterbedarfs.
- Strategisch: Nutze diese Version für langfristige Forecasts, um die Kapazitäten deines Unternehmens zu planen.

Um die Standard-Forecast-Daten in einer Forecast-Version zu speichern, gehe wie folgt vor:

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Wähle den Zeitraum aus, für den du die Forecast-Version speichern möchtest. Klicke auf eine Kalenderwoche, um die ganze Woche auszuwählen oder auf einen beliebigen Tag und ziehe dann mit der Maustaste, um einen Zeitraum kürzer oder länger als eine Woche auszuwählen.
3. Klicke oben rechts auf das {% icon ellipsis_v %} und wähle die Option _Forecast in Version speichern_{:.doc-button}.
4. Wähle im Konfigurationsfenster die Forecast-Version, in der du die Daten speichern möchtest.

   > Hinweis
   >
   > Es kann innerhalb eines Workloads nur jeweils eine operative und eine strategische Forecast-Version je Zeitraum geben. Wenn du innerhalb desselben Zeitraums Daten in derselben Forecast-Version speicherst, werden bestehende Daten überschrieben.

5. Klicke auf _Speichern_{:.doc-button}.

Die Graphen für Volumen und AHT zeigen die Daten der Forecast-Version als farbige Linien an. Die Daten der Version Operativ werden als lila Linie angezeigt. Die Daten der Version Strategisch werden als grüne Linie angezeigt.
