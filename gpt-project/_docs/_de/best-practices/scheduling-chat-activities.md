---
title: Chat-Aktivitäten planen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du Chats planst.
redirect_from:
  - /de/best-practice-chat-activities/
promote-service: what-if-scenario
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
---

So planst du Chat-Aktivitäten:

- Importiere Chat-Daten über eine Integration.
- Füge die sich daraus ergebenden Queues in Forecast einem Workload hinzu.
- Ermittle den Mitarbeiterbedarf.

## Voraussetzungen

Damit du Daten für Chats importieren und den Mitarbeiterbedarf für chatbezogene Workloads ermitteln kannst, muss deine {% link_new Integration | features/acd-integration/cloud/how-integrations-work.md %} den Kontaktdatentyp Chats unterstützen.

## Forecast für Chat-Workloads erstellen

Um das zu erwartende Chat-Volumen zu ermitteln, gehe wie folgt vor:

1. {% link_new Erstelle einen neuen Workload | features/forecast/injixo-forecast/manage-workloads.md | #workloads-erstellen %}
2. Wähle im Abschnitt **Queues zuweisen** auf der Konfigurationsseite **Neuer Workload** eine oder mehrere Chat-Queues aus. Im ersten Dropdown-Menü kannst du nach Queue-Typen filtern.

Tipp: Um Zeiten mit außergewöhnlich hohem oder niedrigem Chat-Volumen zu berücksichtigen, kannst du deinem Workload {% link_new Ereignisse und Feiertage | features/forecast/injixo-forecast/events-and-holidays.md %} hinzufügen.

### Workaround für fehlende oder unzuverlässige Chat-Daten

Selbst wenn dir keine oder nur unzuverlässige Daten zum Erstellen eines Forecasts vorliegen, kannst du den Mitarbeiterbedarf für Chat ermitteln, um eine feste Anzahl an Personen für die Bearbeitung von Chats zu planen. Du kannst die Erstellung des Forecasts und die Berechnung des Mitarbeiterbedarfs überspringen und stattdessen das Bedarfsskript _Allgemein - Konstanter Bedarf_ ausführen. Erfahre mehr über {% link_new konstanten Bedarf | features/forecast/requirement-scripts/requirement-constant.md %}.

## Blockplanung vs. gemischte Planung

In injixo gibt es zwei verschiedene Methoden, Chats zu planen:

- Blockplanung: Personen werden innerhalb ihrer Schicht für einen oder mehrere Blöcke einer festen Aktivität geplant.
- Gemischte Planung: Personen werden so geplant, dass sie jegliche Kontakte bearbeiten, für die sie qualifiziert sind. Du kannst entweder beide Chat-Dienste miteinander kombinieren oder Chat mit anderen Kanälen wie E-Mails oder Anrufen.

Diese Methode legt fest, wie du deine Chat-Aktivitäten einrichtest und deinen Mitarbeiterbedarf berechnest.

### Blockplanung einrichten

Füge feste Blöcke mit Chat-(und anderen) Aktivitäten zu Tagesmodellen hinzu:

1. {% link_new Lege eine Aktivität | features/administration/activities.md | #aktivität-erstellen %} vom Typ Anwesenheit für deine neue Chat-Aktivität an.
2. {% link_new Füge die Aktivität einer Planungseinheit hinzu | features/administration/create-and-manage-planning-units.md | #aktivitäten-hinzufügen %}, in der du Chats planen möchtest.
3. (Optional) Falls nicht alle Personen innerhalb der Planungseinheit an der Chat-Aktivität arbeiten können, gehe wie folgt vor:
   1. {% link_new Lege eine Qualifikation an | features/administration/work-with-skills.md %}.
   2. {% link_new Füge die Qualifikation zur Chat-Aktivität hinzu | features/administration/work-with-skills.md | #aktivitäten-qualifikationen-zuweisen %}
   3. {% link_new Weise die Qualifikation der Person zu | features/administration/employee-overview.md | #mitarbeitereinstellungen-konfigurieren %}, die an den Chat-Aktivitäten arbeiten soll.
4. Erstelle oder aktualisiere {% link_new Tagesmodelle | features/administration/daymodels/daymodel-basics.md %}, indem du ihnen die Chat-Aktivität hinzufügst.

### Gemischte Planung einrichten

injixo kann Chat-Aktivitäten vom Typ Planbar planen, indem andere Aktivitäten vom Typ Ersetzbar in Tagesmodellen ersetzt werden.

Als Alternative kannst du Multiaktivitäten nutzen:

1. Lege eine Aktivität vom Typ Anwesenheit für deine neue Multiaktivität an.
2. Lege weitere Aktivitäten an, die du kombinieren möchtest und {% link_new füge sie als Teilaktivitäten | features/administration/activity-types-and-properties.md | #teilaktivitäten %} zur ersten Aktivität hinzu.
3. Lege Qualifikationen an und weise diese den (Teil-)Aktivitäten und deinen Personen zu.

## Mitarbeiterbedarf berechnen

Es gibt zwei Möglichkeiten, den Mitarbeiterbedarf für Chat-Aktivitäten zu berechnen.

### Für Blockplanung berechnen

Um die Berechnungsmethode zu konfigurieren und den Mitarbeiterbedarf zu berechnen, gehe wie folgt vor:

1.  Gehe zu **Forecast**.
2.  Wähle auf der **Forecast**-Seite einen Zeitraum, für den bereits ein Forecast existiert (Tages-, Wochen- oder Monatsansicht).
3.  Gehe auf der **Forecast**-Seite zum Abschnitt **Mitarbeiterbedarf** und klicke auf _Berechnungsparameter konfigurieren_{:.doc-button}.
4.  Wähle im Konfigurationsfenster **Mitarbeiterbedarf** die Option **Chat** aus dem Dropdown-Menü **Berechnungsmethode** und fülle das Formular aus.
    Erfahre mehr über die Berechnungsmethode für Chat und die benötigten Parameter im Artikel {% link_new Mitarbeiterbedarf berechnen | features/forecast/injixo-forecast/calculate-staff-requirements.md | #berechnungsmethoden-konfigurieren %}.
5.  Klicke auf _Konfiguration speichern_{:.doc-button}.

Auf der Forecast-Seite siehst du nun den berechneten Mitarbeiterbedarf für Chat-Aktivitäten.

Um ihn für die Planung zu verwenden, wähle einen zukünftigen Zeitraum aus und klicke im Abschnitt **Mitarbeiterbedarf** auf _Bedarf verwenden_{:.doc-button}.

### Für gemischte Planung berechnen

Um den Mitarbeiterbedarf aus dem Forecast zu übertragen, gehe wie folgt vor:

1. Gehe zu **Forecast**. Wähle die Workloads für jede der Multiaktivität zugewiesene Aktivität aus.
2. Wähle in jedem Workload denselben zukünftigen Berechnungszeitraum aus.
3. Klicke auf _Forecast verwenden_{:.doc-button}.

Um den Mitarbeiterbedarf zu berechnen, gehe wie folgt vor:

1. Klicke auf der **Forecast**-Seite oben rechts auf **Berechnungen für Multi-Aktivitäten, konstanten Bedarf und Outbound**.
2. Wähle das Skript **Anrufe - Multi-Activity** aus dem Dropdown-Menü **Skript zur Bedarfsberechnung auswählen**. Es öffnet sich ein neues Fenster oder ein neuer Browser-Tab.
3. Fülle das Formular im Konfigurationsfenster für das Skript aus. Wähle im Konfigurationsfenster für das Skript im Abschnitt **Planungseinheiten-Parameter** die Multiaktivität aus, die deine Chat-Aktivitäten enthält.
4. Konfiguriere im Abschnitt **Zugewiesene Aktivitäten** die folgenden Parameter für jede Chat-Aktivität.

   - Im Abschnitt **Queue-Parameter**:

     | **Parameter**                   | **Option**                                                                                                                                   |
     | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
     | Berechnungsmethode              | Chat                                                                                                                                         |
     | Queue                           | Wähle die Queue aus, die so heißt wie dein Workload mit vorangestelltem \*. Diese Queue enthält nun die Daten, die du zuvor übertragen hast. |
     | Version                         | Auto-Forecast                                                                                                                                |
     | Vorgänge                        | Chats - Eingehende                                                                                                                           |
     | Durchschnittliche Vorgangsdauer | Chats - AHT                                                                                                                                  |

   - Im Abschnitt **Erlang C-Parameter**:

     | **Parameter** | **Option**                                                                                                                                                  |
     | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | Seq (%)       | Gib den Prozentsatz der durchschnittlichen Bearbeitungszeit für Aufgaben ein, die nicht parallel bearbeitet werden können, z.&nbsp;B. Nachbearbeitungszeit. |
     | Max Sitzungen | Gib die maximale Anzahl an gleichzeitigen Chat-Sessions an.                                                                                                 |

   Der Mitarbeiterbedarf kann nun für die Planung verwendet werden.

## Chat-Aktivitäten planen

Wenn du die Chat-Daten importiert und den Mitarbeiterbedarf berechnet hast, hast du die Voraussetzungen erfüllt, um deine Chat-Aktivitäten zu planen. Verwende dazu eine der {% link_new Planungsmethoden | features/scheduling/scheduling-methods.md %} Schichtwunsch-Verfahren, Schichtplanoptimierung oder Schichtfolgen.

Den übertragenen Mitarbeiterbedarf und die Planungsergebnisse kannst du dir entweder in {% link_new Schicht Center | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %}, in {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %} oder in Dashboards {% link_new | features/monitoring/dashboards/dashboards-examples.md %} ansehen.
