---
title: Mitarbeiterbedarf bearbeiten oder löschen
toc: false
product_label:
  - advanced
  - enterprise
description: Erfahre, wie du die von injixo berechneten Werte für den Mitarbeiterbedarf bearbeiten oder löschen kannst.
archive_ref: 20210819-de-employee-requirement
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

Der Mitarbeiterbedarf legt fest, wie viele Mitarbeiter du für eine Aktivität zu einer bestimmten Zeit benötigst. Du benötigst den Mitarbeiterbedarf, um Schichtpläne mit der Funktionalität **Optimierten Plan erstellen** zu erstellen oder um sie mit den Funktionalitäten **Joboptimierung** bzw. **Pausen optimieren** zu optimieren.

Als letzten Schritt der Forecasterstellung erzeugst du den Mitarbeiterbedarf. In injixo Forecast kannst du den automatisch erzeugten Mitarbeiterbedarf verwenden oder eine spezielle Bedarfsberechnungsmethode ausführen. Stelle sicher, dass für alle relevanten Aktivitäten ein Mitarbeiterbedarf vorliegt, bevor du einen Schichtplan erstellst.

## Mitarbeiterbedarf einsehen und bearbeiten

In injixo gibt es vier Stellen, an denen du den Mitarbeiterbedarf einsehen kannst:

- _Forecast_{:.menu-item}
- _Analyze > Dashboards_{:.breadcrumbs}
- _Plan > Schedules_{:.breadcrumbs}
- _Plan > Schicht Center_{:.breadcrumbs} 

Die folgende Tabelle enthält Details zu den verfügbaren Optionen je Stelle:

<style>
table {
   margin-left: 0px;
}
</style>

| Wo  | Einsehen | Bearbeiten | Löschen |
| ------ |--------| -------- |-------- |
| _Forecast_{:.menu-item} | Ja | Ja | Ja |
| _Analyze > Dashboards_{:.breadcrumbs} | Ja | Nein | Nein |
| _Plan > Schedules_{:.breadcrumbs} | Ja | Nein | Nein |
| _Plan > Schicht Center_{:.breadcrumbs} | Ja | Ja | Nein |

### Mitarbeiterbedarf im Schicht Center bearbeiten

1. Gehe zu _Plan > Schicht Center_{:.breadcrumbs}.
2. Wähle unten in der Ansicht einen der Tabs **Aktivitäten - Bedarf** bzw. **Aktivitätsübersicht**.<br>
   > Nachricht Keine Angaben in einer Zelle
   >
   > Wenn eine Zelle in der unteren Tabelle die Meldung Keine Angaben anzeigt, wähle aus dem Dropdown-Menü **Ebenen** oben rechts die Ebene **Plan** bzw. **Aktueller Stand** aus.

3. Um eine Planungseinheit auszuklappen, klicke auf der linken Seite einer Tabelle auf das {% icon plus %}.
4. Klicke mit der rechten Maustaste auf eine beliebige Zelle in der unteren Tabelle und wähle **Mitarbeiterbedarf bearbeiten**.
5. Klicke im Fenster **Mitarbeiterbedarf bearbeiten** auf eine Zelle und gib einen neuen Wert ein.<br>
  Du kannst keine blau markierten Zellen bearbeiten. Sie stehen für gelöschte Aktivitäten, die der Planungseinheit noch zugewiesen sind.<br>
  
6. (Optional) Um mehrere Zellen auf einmal zu bearbeiten, kopiere eine Zeile mit Werten aus einer Kalkulationstabelle. Klicke auf eine Zelle und bewege den gedrückten Mauszeiger nach rechts. Drücke Strg+V, um die Werte einzufügen.<br>
7.  Klicke auf _OK_{:.doc-button}.

### Mitarbeiterbedarf in Forecast bearbeiten

Um den Mitarbeiterbedarf manuell zu bearbeiten, kannst du das Skript Allgemein - Konstanter Bedarf in _Forecast_{:.breadcrumbs} ausführen. Die folgende Schrittanleitung erklärt, wie du das Skript für diesen speziellen Anwendungsfall konfigurierst. Wenn du mehr zu den einzelnen Konfigurationsoptionen erfahren möchtest, sieh dir den Artikel {% link_new Konstanter Bedarf| features/forecast/requirement-scripts/requirement-constant.md %} an.

1. Gehe zu _Forecast > Bedarfsskripte_{:.breadcrumbs}.
2. Klicke in der Kachel **Allgemein - Konstanter Bedarf** auf _Öffnen_{:.doc-button}.<br>
3. Konfiguriere im Skript-Konfigurationsfenster folgende Einstellungen:
   - Im Abschnitt **Datum**:
     - **Startdatum**
     - **Anzahl Tage**: Gib an, für wie viele aufeinanderfolgende Tage ab dem Startdatum der geänderte Mitarbeiterbedarf gilt.
     - **Wochentagsabhängig**: Wähle **Nein**.
     - **Zu bestehendem Bedarf addieren**: Lasse die Checkbox deaktiviert.
     - **Tage mit Zeitabschnitten**: Um den Mitarbeiterbedarf für alle Tage in einem Zeitraum zu bearbeiten, wähle 1.
     - **Zeitabschnitte pro Tag**: Wähle die Anzahl der Zeitabschnitte pro Tag, für die du den Mitarbeiterbedarf bearbeiten möchtest (z.&nbsp;B. 1, wenn du den Mitarbeiterbedarf für den ganzen Tag bearbeiten möchtest, oder 3, wenn du jeweils einen Mitarbeiterbedarf für den Morgen, Nachmittag und Abend konfigurieren möchtest).
     - **Anzahl Aktivitäten**: Wähle die Anzahl der Aktivitäten aus, für die du den Mitarbeiterbedarf bearbeiten möchtest.
   - Im Abschnitt **Daten**:
     - **Planungseinheit** und **Aktivität**: Wähle die entsprechenden Daten je Aktivität, für die du den Mitarbeiterbedarf bearbeiten möchtest.
     - **Mitarbeiter**: Gib die Zahl ein, die du als Mitarbeiterbedarf verwenden möchtest.
     - **Beginn** und **Ende**: Gib die Zeiträume ein, für die du den Mitarbeiterbedarf bearbeiten möchtest.
4. Klicke auf _OK_{:.doc-button}.

## Mitarbeiterbedarf löschen

Du kannst den Mitarbeiterbedarf in injixo grundsätzlich nicht löschen. Allerdings kannst du den Mitarbeiterbedarf auf 0 setzen, was dieselbe Wirkung hat, wie ihn zu löschen.

 Es gibt zwei Möglichkeiten, den Mitarbeiterbedarf auf 0 zu setzen:
 - Befolge die Schritte zum [Bearbeiten des Mitarbeiterbedarfs im Schicht Center](#mitarbeiterbedarf-im-schicht-center-bearbeiten) und trage 0 in die entsprechenden Zellen ein.
 
 - Befolge die Schritte zum [Bearbeiten des Mitarbeiterbedarf in Forecast](#mitarbeiterbedarf-in-forecast-bearbeiten) und trage 0 in das Feld **Mitarbeiter** ein.

Das folgende Bild zeigt, wie du anhand der Konfiguration des Skripts Konstanter Bedarf den Mitarbeiterbedarf in Forecast für einen ganzen Kalendertag (hier: Tag 1) löschen kannst:

{{ 3 | image: 'Beispiel des Skripts Konstanter Bedarf mit einer Aktivität von 00:00 bis 00:00 und einem Mitarbeiterbedarf von 0', '80%' }}
