---
title: Forecast-Daten als CSV herunterladen
toc: false
product_label:
  - advanced
  - enterprise
  - classic
description: Lade Forecasts als CSV-Dateien von injixo Forecast herunter. Erfahre, wie diese Dateien formatiert sind.
---

In diesem Artikel lernst du:

- wie Du Forecasts und Versionen eines Workloads in eine CSV-Datei exportieren kannst.
- wie die Daten formatiert sind.

Exportiere Werte von bis zu einem Jahr. Die Zeitzone und das Intervall entsprechen dem Workload. Lade nur den **Forecast** oder auch die Versionen **Operativ** bzw. **Strategisch** herunter.

## Schritte zum Herunterladen

1. Öffne einen **Workload**.
2. Nutze die **Zeitnavigation**, um den Zeitraum auszuwählen.
3. Klicke auf das Kontextmenü _![Kontextmenü in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} (rechts des _Forecast verwenden_-Buttons).
4. Wähle **CSV herunterladen**.
5. Prüfe den Zeitraum und **wähle die gewünschten Forecasts**. Zur Auswahl stehen **Forecast** und die Versionen **Operativ** bzw. **Strategisch**. Die Forecasts und Versionen werden in einer einzelnen Datei gespeichert.
6. Bestätige Deine Auswahl mit _Download starten_{:.doc-button}.

## Beispiel für eine CSV-Datei

Die Datei enthält den Namen und den Kanal des Workloads. Ein Download des Anruf-Workloads _Bestellungen_ würde zu einer Datei namens `Bestellungen-Calls.csv` führen. Die Spaltenüberschriften zeigen die Forecast-Version an. Die Datei enthält Zeitstempel (formatiert als YYYY-MM-DD) und die Werte pro Werttyp für jeden Forecast, aber keine Informationen über Feiertage oder Ereignisse, die dem Workload hinzugefügt wurden, und keine historischen Daten.

Wenn Du **Forecast** sowie die Version **Operativ** auswählst, sieht die Datei so aus:

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
...
2020-05-17 16:30;40;180;35;175
2020-05-17 16:45;41;181;37;183
2020-05-17 17:00;40;180;35;175
2020-05-17 17:15;41;181;37;183
...
```

> Das Herunterladen ist nur für _Smart_ Workloads im _Live_ Modus verfügbar.
>
> Ändere den Modus des Workloads auf _Live_, um auf die Download-Option zugreifen zu können. Details zum _Live/Test_-Modus findest du unter {% link_new Workloads erstellen | features/forecast/injixo-forecast/manage-workloads.md %}.
