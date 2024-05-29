---
title: Forecast herunterladen
toc: true
product_label:
  - advanced
  - enterprise
  - classic
description: Lade Forecasts als CSV-Dateien von injixo Forecast herunter. Erfahre, wie diese Dateien formatiert sind.
---

Unter _Forecast > Workloads_{:.breadcrumbs} kannst du deine Forecast-Daten als CSV-Datei herunterladen.

Du kannst Daten von bis zu einem Jahr exportieren. Du kannst die Forecast-Daten als eigene {% link_new Version | features/forecast/injixo-forecast/save-forecast-versions.md | #forecast-version-speichern %} herunterladen oder gemeinsam mit beiden bzw. einer der Versionen Operativ/Strategisch.

## Forecast herunterladen

1. Wähle in _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Wähle mit der Datumsauswahl den Zeitraum aus. Klicke auf eine Kalenderwoche, um die ganze Woche auszuwählen oder auf einen beliebigen Tag und ziehe dann mit der Maustaste, um einen Zeitraum kürzer oder länger als eine Woche auszuwählen.
3. Klicke oben rechts auf das {% icon ellipsis_v %} und wähle die Option **CSV herunterladen**.
4. Wähle aus, welche Forecast-Daten du herunterladen möchtest.<br>Um alle verfügbaren Versionen auszuwählen, aktiviere die Checkbox **Alle**.
5. Klicke auf _Als CSV herunterladen_{:.doc-button}.<br>
   Die heruntergeladenen Forecast-Versionen werden in einer Datei gespeichert.

## Beispiel für eine CSV-Datei

Der Dateiname der CSV-Datei enthält den Namen des Workloads und des Kanals. Die CSV-Datei für den Anruf-Workload Bestellungen heißt dann beispielsweise `Bestellungen-Anrufe.csv`. Die Spaltenüberschriften zeigen die Forecast-Version an. Die Datei enthält Zeitstempel (im Format YYYY-MM-DD) und Werte für jeden Forecast und verwendet die Zeitzone und das Intervall des Workloads. Die Datei enthält weder Daten zu Feiertagen, zu dem Workload hinzugefügten Ereignissen noch andere historische Daten.

Wenn du die Versionen **Forecast** und **Operativ** auswählst, sieht die Datei wie folgt aus:

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
...
2020-05-17 16:30;40;180;35;175
2020-05-17 16:45;41;181;37;183
2020-05-17 17:00;40;180;35;175
2020-05-17 17:15;41;181;37;183
...
```

> Smart Workloads können nur im Live-Modus heruntergeladen werden.
>
> Um die Download-Funktion nutzen zu können, stelle deinen Workload auf den Live-Modus um. Um mehr über den Live-Modus und den Test-Modus zu erfahren, sieh dir den Artikel {% link_new Workloads erstellen | features/forecast/injixo-forecast/create-workloads.md %} an. Smart Workload sind nur in den WFM-Plänen Enterprise und Advanced verfügbar.
