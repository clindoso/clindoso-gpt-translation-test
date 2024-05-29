---
title: Forecasts importieren
description: Importiere einen Forecast aus einer externen Quelle in injixo Forecast.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

Wenn du historische Daten verwenden möchtest, die von einer externen Quelle, wie z.&nbsp;B. von einer externen Anwendung oder von deinen Kunden erstellt wurden, kannst du externe Forecasts in injixo Forecast importieren.

Neu bei injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Import vorbereiten

### Voraussetzungen

Um einen Forecast zu importieren, benötigst du mindestens:

- Eine {% link_new Integration | features/acd-integration/cloud/how-integrations-work.md %}, die Daten importiert
- Einen Workload mit einer {% link_new Queue | features/forecast/injixo-forecast/create-workloads.md | #queues-und-kanäle %}

### Queue erstellen

Um eine Queue zu erstellen, musst du über eine Integration historische Kontaktdaten importieren. Queues werden automatisch von Integrationen erstellt.

Wenn du keine Integration hast, die fortlaufend historische Daten importiert, erstelle eine Queue, indem du eine einfache CSV-Datei importierst:

1. {% link_new Erstelle eine CSV-Integration | features/acd-integration/cloud/add-csv-integration.md | #neue-csv-integration-konfigurieren %}.
   - Überspringe die Cloud Link-Installation.
   - Wähle im Abschnitt **CSV-Schema-Konfiguration** die Option **Kontaktdaten**.
2. Erstelle eine CSV-Datei für Kontaktdaten, die mindestens eine Zeile für ein einzelnes Intervall enthält, z.&nbsp;B.:
   ```
   Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
   ForecastImportQueue;22/02/2022;02:02;2;2;2
   ```
3. {% link_new Importiere die CSV-Datei manuell | features/acd-integration/cloud/add-csv-integration.md | #manueller-datenimport %}.  
   Die Queue wird nach dem Import erstellt.
   Verwende diese Queue, um Forecasts in alle deine Workloads zu importieren.

### Queue einem Workload zuweisen

Wenn du einen Workload erstellst, musst du ihm eine Queue zuweisen. Dies ist ein integraler Bestandteil der Workloaderstellung und eine Voraussetzung für den [Forecast-Import](#forecast-importieren). Erfahre mehr darüber, wie du {% link_new Workloads erstellst | features/forecast/injixo-forecast/create-workloads.md | #workloads-erstellen %}.

Du kannst einen Forecast in einen bestehenden Workload importieren oder einem neuen Workload jede deiner Queues hinzufügen.

### Importdatenanforderungen

Deine Importdaten müssen folgende Anforderungen erfüllen:

| Anforderung          | Erläuterung                                                                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Zeitstempelformat    | YYYY-MM-DD HH:MM                                                                                                                               |
| Volumendaten         | Ganze Zahlen                                                                                                                                   |
| AHT-Daten            | Ganze Zahlen oder Dezimalwerte (mit Dezimalpunkt)                                                                                              |
| Format der Kopfzeile | `Timestamp;Offered;AHT` oder mit benutzerdefiniertem Text (z.&nbsp;B. `Timestamp;Offered_benutzerdefiniertertext;AHT_benutzerdefiniertertext`) |
| Trennzeichen         | Semikolon oder Komma (automatische Erkennung)                                                                                                  |
| Maximale Dateigröße  | 20&nbsp;MB<br>Erstelle Dateien mit höchstens 20.000 Zeilen (Empfehlung).                                                                       |
| Zeitzone             | Muss der Zeitzone der Queue entsprechen.                                                                                                       |
| Intervalllänge       | Muss der Intervalllänge der Queue entsprechen (15, 30 oder 60&nbsp;Minuten).                                                                   |

Alternativ kannst du einen Forecast (oder eine Forecast-Version) {% link_new im CSV-Format herunterladen | features/forecast/injixo-forecast/download-forecast.md %} und als Vorlage für deine eigene Importdatei verwenden. Der Forecast liest nur die Spalten `Timestamp`, `Offered` und `AHT`. Weitere Spalten wie `Offered_operational` oder `AHT_operational` im folgenden Beispiel werden ignoriert.

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
2020-05-17 16:30;40;180;50;170
```

### Datenlücken in der Importdatei

Es kann vorkommen, dass manche Intervalle in deinen Importdateien keine Daten enthalten. Der Graph für Volumen bzw. AHT zeigt nur importierte Werte als Null (0) an. Leere Zeilen oder Werte werden nicht importiert.

Wenn für ein oder mehrere Intervalle keine Daten vorliegen, kannst du deine CSV-Datei wie folgt bearbeiten:

- Lasse die Spalten für Volumen und AHT leer:

  ```
  Timestamp;Offered;AHT
  2020-05-17 15:00;30;210
  2020-05-17 15:15;;
  2020-05-17 15:30;40;180
  ```

- Importiere mit Nullen gefüllte Spalten:

  ```
  Timestamp;Offered;AHT
  2020-05-17 15:00;30;210
  2020-05-17 15:15;0;0
  2020-05-17 15:30;40;180
  ```

- Lasse die gesamte Zeile weg:

  ```
  Timestamp;Offered;AHT
  2020-05-17 15:00;30;210
  2020-05-17 15:30;40;180
  ```

## Forecast importieren

1. Wähle in _Forecast > Workloads_{:.breadcrumbs} den Workload aus, für den du den externen Forecast importieren möchtest.
2. Wähle aus dem Drei-Punkte-Menü _![Kontextmenü in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} oben rechts die Option **Forecast-Daten importieren**.
3. Klicke auf _Datei auswählen_{:.doc-button} und wähle die CSV-Datei, die du importieren möchtest.
4. Klicke auf _Import starten_{:.doc-button}.<br>
   Das Fenster aktualisiert sich und zeigt an, ob der Import erfolgreich war.
5. Klicke auf _Fertig_{:.doc-button}.<br>
   Aktualisiere die Seite, um den aktualisierten Graphen für den Importzeitraum anzuzeigen. Die importierten Werte werden als braune Linie in den Graphen in den Abschnitten für Volumen und AHT angezeigt.
   Um den importierten Forecast im Diagramm auszublenden, klicke auf das Anzeigen/Ausblenden-Icon {% icon eye | icon-only %} in der Legende neben **Importiert**.
