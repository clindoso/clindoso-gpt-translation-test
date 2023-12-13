---
title: Externe Forecasts importieren
description: Einen externen Forecast in den injixo Forecast importieren.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

In diesem Artikel lernst Du:
- die Formatierungs- und Importanforderungen.
- wie Du mit Datenlücken in der Importdatei umgehst.
- wie Du eine Importvorlage erstellst, indem Du einen Forecast herunterlädst.
- wie Du einen Forecast importierst und das Ergebnis überprüfst.

Neu in injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

Du kannst Forecasts in injixo importieren, die in einem externen Tool oder von Deinen eigenen Kunden erstellt wurden.

## Eine Queue als Import-Voraussetzung

> Für den Import benötigst du mindestens eine Queue in deiner injixo-Instanz.

Erstelle eine Queue, die in allen Workloads verwendet werden kann:

1. {% link_new Erstelle eine CSV-Integration | features/acd-integration/cloud/add-csv-integration.md | #csv-integration-hinzufügen %} für Kontaktdaten.  
2. Erstelle eine CSV-Datei für Kontaktdaten mit mindestens einer Zeile für ein einzelnes Interval, z.&nbsp;B.:
    ```
    Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
    ForecastImportQueue;22/02/2022;02:02;2;2;2
    ``` 
3. {% link_new Lade die Datei manuell hoch | features/acd-integration/cloud/add-csv-integration.md | #manueller-datenimport %}.  

Nachdem die Queue erstellt ist, kannst du {% link_new den Workload erstellen | features/forecast/injixo-forecast/manage-workloads.md %}, der für den [Forecast-Import](#forecast-importieren) notwendig ist.

## Format- und Dateivoraussetzungen

Forecast-Importe benötigen ein festes CSV-Format:
  - Zeitstempel-Format: *YYYY-MM-DD HH:MM*
  - Volumen und AHT-Werte: ganze Zahlen (Integer) oder Dezimalwerte (mit Punkt)
  - Trennzeichen (automatische Erkennung): Semikolon oder Komma

* Die Zeitzone und die Intervall-Länge (15, 30 oder 60 Minuten) müssen mit den Queues im Workload übereinstimmen. <!-- Änderungen bei Importen ohne Historie -->
* Die maximale Größe der Importdatei beträgt 20 MB. Erstelle Dateien mit 20.000 Zeilen oder weniger (empfohlen).
* Die erforderliche Kopfzeile unterstützt zwei Formate:

    ```
    Timestamp;Offered;AHT
    2020-05-17 15:00;30;210
    ```

    Ersetze *deintext* bei Bedarf, der Unterstrich ist erforderlich.
    ```
    Timestamp;Offered_deintext;AHT_deintext
    2020-05-17 15:00;30;210
    ```


## Datenlücken in der Importdatei

injixo füllt leere Intervalle nicht mit Nullen auf. Fehlende Intervalle erscheinen in Graphen als kein Wert. Wenn du Nullen in deiner Datei hast, werden diese als Null angezeigt.

Wenn ein oder mehrere Intervalle keine Daten enthalten, kannst Du:

- die gesamte Zeile weglassen (die Zeile *\-\- keine Daten \-\-* nicht übernehmen):

    ```
    Timestamp;Offered;AHT
    2020-05-17 15:00;30;210
    -- keine Daten --
    2020-05-17 15:30;40;180
    ```

- Volumen und AHT leer lassen:

    ```
    Timestamp;Offered;AHT
    2020-05-17 15:00;30;210
    2020-05-17 15:15;;
    2020-05-17 15:30;40;180
    ```

- mit Nullen gefüllte Spalten importieren:

    ```
    Timestamp;Offered;AHT
    2020-05-17 15:00;30;210
    2020-05-17 15:15;0;0
    2020-05-17 15:30;40;180
    ```

## Vorlage durch Forecast-Download erstellen

Um eine Vorlage für eine Importdatei zu erstellen, {% link_new lade andere Forecasts oder Versionen herunter | features/forecast/injixo-forecast/download-forecast.md %}. Die Exportdatei kann z. B. mehrere Forecast-Versionen enthalten:

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
2020-05-17 16:30;40;180;50;170
```

Der Import liest nur den *Zeitstempel* und die ersten Spalten *Offered* und *AHT*; alle weiteren Spalten (im obigen Beispiel *Offered_operational* und *AHT_operational*) werden ignoriert.

## Forecast importieren

1. Gehe zu *Forecast*{:.menu-item}.
2. Wähle aus dem Dropdown-Menü oben den **Workload**, in den du den externen Forecast importieren möchtest.
3. Klicke auf _![Kontextmenü in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon}, um das Kontextmenü zu öffnen.
4. Wähle **Forecastdaten importieren**.
5. Klicke **Datei auswählen** und wähle die **CSV-Datei**, die Du importieren möchtest.
6. Bestätige Deine Auswahl mit _Import starten_{:.doc-button}. injixo zeigt auf der Seite eine Meldung, ob der Import erfolgreich war oder nicht.
7. Klicke *Fertig*{:.doc-button}.

Wenn Du den Bildschirm aktualisierst, zeigt das Diagramm einen neuen Graphen an. Um den importierten Forecast im Diagramm auszublenden, klicke auf das **Augensymbol** in der Legende neben *Import*.

{{ 2 | image: "Importierter Forecast", '80%' }}
