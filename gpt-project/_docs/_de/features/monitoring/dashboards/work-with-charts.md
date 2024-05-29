---
title: Diagramme verwenden
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du Diagramme in einem Dashboard verwendest.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

Unter _Analyze > Dashboards_{:.breadcrumbs} kannst du mit Diagrammen und Zeitreihen deine Daten analysieren. Wähle dafür als erstes oben aus dem Dropdown-Menü ein Dashboard aus.

Neu bei Dashboards? Lerne zuerst {% link_new die Grundlagen | features/monitoring/dashboards/manage-dashboards.md %}.

## Diagramme im Überblick

Du kannst unter **Dashboards** folgende Aktionen ausführen:

- Datumsbereich für die Datenanzeige ändern: Wähle für jedes Diagramm oben rechts aus der Datumsauswahl einen Datumsbereich aus.
- In einem Diagramm zoomen: Klicke und ziehe die Stelle, die du dir näher ansehen möchtest.
- Herauszoomen: Klicke auf _Zoom zurücksetzen_{:.doc-button}.
- Zur Tabellenansicht wechseln: Klicke oben rechts in einem Diagramm auf das Tabelle-anzeigen-Icon {% icon table-list | icon-only %}.
- Zur Diagrammansicht zurückkehren: Klicke auf das Diagramm-anzeigen-Icon {% icon chart-view | icon-only %}.
- Daten in die Zwischenablage kopieren: Klicke auf das Tabelle-in-Zwischenablage-kopieren-Icon {% icon clone | icon-only %}.

> Hinweis
>
> Die Datums- und Zeitinformationen werden gemäß deinen injixo-Spracheinstellungen angezeigt. Dies kann zu Problemen führen, wenn du von injixo kopierte Daten in ein Excel- oder Google Sheets-Dokument einfügst, das eine andere Sprache verwendet.

## Zeitreihen verwenden

Zeitreihen sind Folgen von Datenpunkten, die in regelmäßigen Intervallen aufgezeichnet werden. Die folgenden Teilabschnitte erklären, wie du Zeitreihen in **Dashboards** verwenden und anpassen und damit deine Daten analysieren kannst, um informierte Entscheidungen zu treffen.

### Zeitreihen hervorheben

Um eine bestimmte Zeitreihe vorübergehend hervorzuheben, bewege in der Diagrammansicht den Mauszeiger über den Namen der Zeitreihe in der Legende. Alle anderen Zeitreihen treten dann in den Hintergrund.

### Zeitreihen ein- und ausblenden

Um Zeitreihen ein- und auszublenden, klicke neben dem Namen in der Legende auf das {% icon eye %} bzw. das {% icon eye_slash %}.

### Zeitreihen anpassen

1. Gehe zu _Analyze > Dashboards_{:.breadcrumbs}.
2. Klicke auf das {% icon ellipsis_v %} und wähle die Option **Bearbeiten**.
3. Bewege den Mauszeiger über den Namen der Zeitreihe in der Legende und klicke auf das Bearbeiten-Icon {% icon pencil | icon-only %}.
4. Ändere im Konfigurationsfenster **Graph anpassen** die Eigenschaften der Zeitreihe:
   - Bearbeite den **Namen**, der in der Legende angezeigt wird.
   - Wähle im Dropdown-Menü **Typ** entweder **Stufen** oder **Histogramm** (Balkendiagramm) aus.
   - Wähle eine andere als die vordefinierte **Farbe** aus.
   - Wähle aus, wie Daten im Diagramm aggregiert werden. Wähle entweder **Nach Intervall** (verfügbar für Zeiträume bis zu 8&nbsp;Tagen), um Intervallwerte anzuzeigen, oder **Nach Tag**, um tägliche Werte anzuzeigen.
   - Wähle aus, ob du die Werte der y-Achse **Links (standard)** oder **Rechts** anzeigen lassen möchtest.
5. Klicke auf _Speichern_{:.doc-button}.<br>Klicke auf _Bearbeitungsmodus verlassen_{:.doc-button}, um zum Anzeigemodus zurückzukehren.

### Zeitreihen löschen

1. Gehe zu _Analyze > Dashboards_{:.breadcrumbs}.
2. Klicke auf das {% icon ellipsis_v %} und wähle die Option **Bearbeiten**.
3. Bewege den Mauszeiger über den Namen der Zeitreihe in der Legende und klicke auf das Bearbeiten-Icon {% icon pencil | icon-only %}.
4. Klicke im Konfigurationsfenster **Graph anpassen** auf _Löschen_{:.doc-button}.
5. Klicke auf _Speichern_{:.doc-button}.<br>Klicke auf _Bearbeitungsmodus verlassen_{:.doc-button}, um zum Anzeigemodus zurückzukehren.
