---
title: Mit Diagrammen arbeiten
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lerne wie Du mit Diagrammen in einem Dashboard arbeitest.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

In diesem Artikel lernst Du:
- wie Du den Datumsbereich änderst.
- wie Du hinein- und hinauszoomst.
- wie Du die Tabellenansicht verwendest und Daten kopierst.
- wie Du Zeitreihen hervorhebst oder ausblendest.
- wie Du Zeitreihen anpasst oder löschst.

Um die beschriebenen Funktionen zu nutzen, musst Du ein Dashboard auswählen. Neu in Dashboards? Lerne zuerst {% link_new die Grundlagen | features/monitoring/dashboards/dashboards-overview.md %}.

## Datumsbereich ändern

Lege oben rechts in jedem Diagramm einen fixen **Zeitbereich** für die Anzeige fest oder aktiviere zusätzlich **Rollierender Zeitraum** (optional). In diesem Modus wird das Startdatum jeden Tag um einen Tag verschoben.

## Hinein- und Hinauszoomen

Betrachte Diagramme detaillierter mit der Zoomfunktion. Markiere dazu einfach mit der Maus in einem Diagramm den Bereich, der Dich interessiert. Klicke auf *Zoom zurücksetzen*{:.doc-button}, um wieder den gesamten Zeitrahmen zu sehen.

## In die Tabellenansicht wechseln

Als Alternative zur grafischen Darstellung zeigt die Tabellenansicht Zeitstempel und Werte für jedes Diagramm. Wechsele zwischen Diagramm- und Tabellenansicht, indem Du auf _![Tabellenansicht](/assets/img/common/dashboards/table.png)_{:.doc-button-icon} über einem Diagramm klickst.

### Daten in die Zwischenablage kopieren

Die Tabellenansicht bietet eine Kopierfunktion. Klicke auf _![Tabelle kopieren](/assets/img/common/dashboards/copy.png)_{:.doc-button-icon} und füge die Daten dann per Copy & Paste in Deine Tabellenkalkulation ein. Die erste Spalte enthält Datum und Uhrzeit, Du musst Formeln in Deiner Tabellenkalkulation nutzen, um beide zu trennen.

Hinweis: Die Datums- und Zeitangaben werden entsprechend Deiner injixo-Spracheinstellungen lokalisiert, was problematisch sein könnte, wenn Du die Daten von Deinem Tenant in eine Excel oder Google-Sheets-Version kopierst, die eine andere Sprache verwendet.

## Zeitreihen hervorheben

Um eine bestimmte Zeitreihe temporär hervorzuheben, bewege den Mauszeiger über den **Namen der Zeitreihe** in der Legende. Alle anderen Zeitreihen treten dann in den Hintergrund.

## Zeitreihen ein- und ausblenden

Blende andere Zeitreihen aus, indem Du auf _![Diagramme ein- und ausblenden](/assets/img/common/dashboards/view.png)_{:.doc-button-icon} neben dem Namen der Zeitreihe in der Legende klickst.

## Zeitreihen anpassen

1. Klicke auf _![Kontextmenü](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} neben dem Namen des aktuell ausgewählten Dashboards.
2. Klicke auf **Bearbeiten**, um den Bearbeitungsmodus für das Dashboard aufzurufen.
3. Bewege den Mauszeiger über den **Namen der Zeitreihe** in der Legende und klicke dann auf das **Bleistiftsymbol**.
4. Ändere im Dialogfenster *Diagramm anpassen* die Eigenschaften der Zeitreihe. Du kannst:
    - den **Namen** bearbeiten, der in der Legende angezeigt wird.
    - den **Typ** des Diagramms ändern. Wähle zwischen **Stufen** oder **Histogramm** (Balkendiagramm).
    - eine andere vordefinierte **Farbe** auswählen.
    - ändere die Art der Datenaggregation im Diagramm. Wähle **Nach Intervall** (verfügbar für Zeiträume bis zu 8 Tagen), um Intervallwerte anzuzeigen, oder **Nach Tag**, um die Werte für den Tag anzuzeigen.
    - Ändere, wo die y-Achse angezeigt wird. Wähle zwischen **Links (Standard)** und **Rechts**.
5. Klicke auf *Speichern*{:.doc-button}.
6. Klicke auf *Bearbeitungsmodus schließen*{:.doc-button}, um zum Anzeigemodus zurückzukehren.

   {{ 3 | image: "Einen Graphen anpassen", '40%' }}

## Zeitreihen löschen

1. Klicke auf _![Kontextmenü](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} neben dem Namen des aktuell ausgewählten Dashboards.
2. Klicke auf **Bearbeiten**, um den Bearbeitungsmodus für das Dashboard aufzurufen.
3. Bewege den Mauszeiger über den **Namen der Zeitreihe** in der Legende und klicke dann auf das **Bleistiftsymbol**.
4. Klicke im Dialogfenster *Diagramm anpassen* auf *Löschen*{:.doc-button}, um die ausgewählte Zeitreihe zu löschen. Dadurch wird der Bearbeitungsdialog geschlossen.
5. Klicke auf *Speichern*{:.doc-button}.
6. Klicke auf *Bearbeitungsmodus verlassen*{:.doc-button}, um zum Anzeigemodus zurückzukehren.
