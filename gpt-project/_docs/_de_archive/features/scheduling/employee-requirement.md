---
title: Mitarbeiterbedarf
description: Über den Menüpunkt Mitarbeiterbedarf erhältst Du eine Tagesübersicht über alle erzeugten Mitarbeiterbedarfe je Planungseinheit.
redirect_reason: renamed file in Nov 2020
archive_ref: 20210819-de-employee-requirement
archived_date: 2021-08-19
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
---

In diesem Artikel lernst Du:
- was Mitarbeiterbedarf ist.
- wie Du Dir den Mitarbeiterbedarf anschaust.
- wie Du den Mitarbeiterbedarf manuell bearbeitest.

## Was ist Mitarbeiterbedarf?

Mitarbeiterbedarf ist die Basis für alle automatischen Optimierungsprozesse. Dieser definiert, wie viele Mitarbeiter Du für eine Aktivität zu einem bestimmten Zeitpunkt in einer Planungseinheit benötigst.
injixo nutzt Mitarbeiterbedarfe z. B. für die *Joboptimierung*, die *Pausenoptimierung* und um einen *optimierten Schichtplan* zu erstellen.
Mitarbeiterbedarf erscheint in einigen Bereichen von injixo auch als *Bedarf*.

Mitarbeiterbedarf wird im letzten Schritt des Forecast-Prozesses automatisch erzeugt. In injixo Forecast kannst Du den automatisch generierten Mitarbeiterbedarf verwenden oder ein spezielles Skript zur Bedarfsberechnung ausführen.

Hinweis: Prüfe zu Beginn Deiner Planung, ob alle Mitarbeiterbedarfe korrekt erzeugt wurden. Den Mitarbeiterbedarf kannst Du Dir im {% link_new Schicht Centers | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %} oder in {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %} ansehen. In {% link_new Dashboards | features/monitoring/dashboards/dashboards-examples.md %} kannst Du Diagramme erstellen, die den Bedarf aus verschiedenen Tagen, Aktivitäten und Planungseinheiten anzeigen.

## Mitarbeiterbedarf ansehen oder bearbeiten (SchedulePro)

1. Gehe zu *WFM > Scheduling > SchedulePro > Mitarbeiterbedarf*{:.breadcrumbs}.
2. Wähle eine **Planungseinheit**.
3. Wähle ein **Datum**.
4. Klicke auf *Anwenden*{:.doc-button}, um die Tabelle anzuzeigen.
    {{ 1 | image: 'Tabelle für den Mitarbeiterbedarf', '100%' }}

Gib Werte wie folgt ein:  

1. Wähle eine **Zelle**.
2. Gib einen **Wert** in eine **Zelle** ein.
3. Kopiere die Werte und füge sie mit **STRG+C** or **STRG+V** ein (optional).
4. Klicke auf *Speichern*{:.doc-button}.

Lösche Werte wie folgt:  

1. Wähle **eine oder mehrere Zellen**.
2. Drücke die Taste **Entf** auf Deiner Tastatur.
3. Klicke auf *Speichern*{:.doc-button}.

## Mitarbeiterbedarf ansehen oder bearbeiten im Schicht Center

Im Schicht Center kannst Du den Mitarbeiterbedarf überprüfen und bei Bedarf manuelle Änderungen für einzelne Tage vornehmen:

1. Gehe zu *Plan > Schicht Center*{:.breadcrumbs}.
2. Klicke auf den Reiter *Aktivitäten* oder *Aktivitätsübersicht* unten im Kennzahlenfenster.
3. Klicke auf *+*{:.doc-button}, um eine Planungseinheit zu öffnen.
4. Klicke mit der rechten Maustaste auf eine **Zelle**.
5. Wähle im Kontextmenü **Mitarbeiterbedarf bearbeiten** aus.

{{ 4 | image: 'Mitarbeiterbedarf bearbeiten im Kontextmenü', '80%' }}

Du siehst die Bedarfswerte für alle Aktivitäten der Planungseinheit für das gewählte Datum auf Interval-Basis. Multiaktivitäten erscheinen fett. Gelöschte, aber der Planungseinheit noch zugeordnete Aktivitäten werden kursiv dargestellt; Eingabefelder sind in diesem Fall ausgegraut und gesperrt. Der Mitarbeiterbedarf wird in der Ortszeit der Planungseinheit angezeigt.

Bearbeite Werte wie folgt:

1. Klicke auf die **Zelle** eines Intervalls und trage den **neuen Wert** ein
2. Kopiere die Werte und füge sie ein mit **STRG+C** or **STRG+V** (optional).
3. Klicke auf *OK*{:.doc-button}, um Deine Änderungen zu speichern.

{{ 3 | image: 'Mitarbeiterbedarfstabelle', '80%' }}
