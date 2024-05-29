---
title: Aktivitätstypen und -eigenschaften
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, welche verschiedenen Aktivitätstypen es gibt und welchen Zweck die einzelnen Konfigurationsoptionen für Aktivitäten haben.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-schedule-multiskill-agents.md
redirect_from:
  - /de/activity-properties/
redirect_reason: Updated filename on 11 October 2023
---

Wenn du Aktivitäten {% link_new erstellst und bearbeitest | features/administration/activities.md %}, wirken sich die verschiedenen Konfigurationsoptionen darauf aus, wie die Aktivitäten in deinem Schichtplan und deinen Reports verwendet und angezeigt werden.

## Aktivitätstypen

Der Aktivitätstyp wirkt sich auf deine Schichtplanung aus und bestimmt:

- wie die Aktivität in der optimierten Schichtplanung behandelt wird.
- wo du die Aktivität verwenden kannst.
- wie die Aktivität in Schedules und im Schicht Center angezeigt wird.
- ob die Aktivität in Reports enthalten ist. <!-- illness, absences, vacation -->

In der folgenden Tabelle findest du weitere Details zu jedem Aktivitätstyp:

| Typ         | Beschreibung                                                                                                                                                                                                            |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anwesenheit | Alle Aktivitäten, an denen Mitarbeiter arbeiten.<br>Aktivitäten vom Typ Anwesenheit werden von injixo abhängig vom Mitarbeiterbedarf geplant.                                                                           |
| Pause       | Bezahlte oder unbezahlte Pausen innerhalb einer Schicht.<br>Nur Aktivitäten vom Typ Pause können in Tagesmodellen als Pausenaktivitäten konfiguriert werden. Du kannst die Funktionalität {% link_new Pausen optimieren | features/scheduling/schedules/break-optimization.md %} verwenden, um Pausen innerhalb des Schichtplans so zu verteilen, dass du die optimale Deckung für Aktivitäten mit Mitarbeiterbedarf erhältst. |
| Krankheit   | Bezahlte oder unbezahlte Abwesenheiten wie z.&nbsp;B. Krankheitstage oder Arzttermine.<br>In den Krankheitsstatistiken von injixo erscheinen nur Aktivitäten vom Typ Krankheit.                                         |
| Urlaub      | Bezahlter oder unbezahlter Urlaub, Betriebsurlaub, etc.<br> In den Urlaubsstatistiken erscheinen nur Aktivitäten vom Typ Urlaub.                                                                                        |
| Abwesenheit | Andere Abwesenheiten, die sich auf den Schichtplan auswirken, wie zum Beispiel externe Weiterbildung, Überstundenabbau usw.<br>In den Abwesenheitsstatistiken erscheinen nur Aktivitäten vom Typ Abwesenheit.           |
| Meeting     | Aktivitätstyp für die {% link_new Planung von Meetings                                                                                                                                                                  | features/scheduling/meetings/meetings-overview.md %}.                                                                                                                                                |

## Aktivitätseigenschaften

Die Aktivitätseigenschaften wirken sich auf deinen Schichtplan aus und darauf, wie du die Aktivität verwenden kannst.
Du kannst Aktivitätseigenschaften mit den folgenden Checkboxen festlegen:

| Eigenschaft                                              | Auswirkung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bezahlt                                                  | Aktiviert die Arbeitszeitberechnung für geplante Aktivitäten. Sind Pausen oder Abwesenheiten bezahlt, werden sie als Arbeitszeit angerechnet. Wenn sie unbezahlt sind, werden sie nicht in der Berechnung der Nettoarbeitszeit berücksichtigt.                                                                                                                                                                                                                                                  |
| Ruhezeit einhalten                                       | Verhindert eine Verletzung der im Vertrag festgelegten Ruhezeit. injixo überprüft die Ruhezeit nur, wenn die Planungsregel _2601_{:.id-label} aktiviert ist.                                                                                                                                                                                                                                                                                                                                    |
| Planbar                                                  | injixo kann die Aktivität planen, wenn du die Funktionalität Optimierten Plan erstellen verwendest, oder kann sie während der Joboptimierung optimieren. Wir empfehlen, diese Eigenschaft für Aktivitäten mit Mitarbeiterbedarf zu verwenden. Sie wird üblicherweise nicht für Aktivitäten vom Typ Abwesenheit, Urlaub oder Krankheit verwendet.                                                                                                                                                |
| Wünschbar in Me                                          | Damit können Mitarbeiter in injixo Me Abwesenheiten (Abwesenheit, Urlaub, Krankheit) beantragen (wenn es eine {% link_new Abwesenheitsperiode                                                                                                                                                                                                                                                                                                                                                   | features/scheduling/time-off/time-off-periods.md %} mit dem Status Veröffentlicht) gibt. Beim Schichtwunsch-Verfahren sind Schichten mit Aktivitäten vom Typ Anwesenheit und Pause automatisch wünschbar.                                       |
| Tauschbar beim Schichttausch                             | Damit können Mitarbeiter die {% link_new Aktivität in injixo Me untereinander tauschen                                                                                                                                                                                                                                                                                                                                                                                                          | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}. Dazu müssen alle Aktivitäten (inklusive Pausen), die in Tagesmodellen enthalten sind, als **Tauschbar beim Schichttausch** konfiguriert sein. |
| Überdeckung erlauben, wenn Mitarbeiterbedarf gleich null | injixo kann die Aktivität auch für Zeiten ohne Mitarbeiterbedarf planen. Standardmäßig deckt dies keine Intervalle ab, für die der Mitarbeiterbedarf bei 0 liegt.                                                                                                                                                                                                                                                                                                                               |
| Ersetzbar                                                | injixo kann die Aktivität durch planbare Aktivitäten mit Mitarbeiterbedarf ersetzen. Dies ist erforderlich, um {% link_new Meetings                                                                                                                                                                                                                                                                                                                                                             | features/scheduling/meetings/meetings-overview.md %} für diese Aktivität zu planen.                                                                                                                                                             |
| Ganztägig erlauben                                       | Du kannst die Aktivität für einen ganzen Tag planen (in Schedules oder auf dem Tab Ganztägige Aktivitäten in der Tagesansicht im Schicht Center). Wenn die Aktivität außerdem als Bezahlt konfiguriert ist, wird dem Mitarbeiter das entsprechende vertragliche Tagessoll als Arbeitszeit gutgeschrieben.<br>Erforderlich, damit Mitarbeiter die Aktivität als ganztägige Aktivität in injixo Me beantragen können.                                                                             |
| Tagesstatus                                              | Nur für ganztägige Aktivitäten verfügbar. Mit dem Tagesstatus kannst du die Aktivität manuell im Schicht Center als Tagesstatus auf dem Tab Ganztägige Aktivitäten planen. Dies sorgt dafür, dass der ersetzte Eintrag im Schichtplan als zukünftige Referenz erhalten bleibt. Als Folge davon vernachlässigt injixo Mitarbeiter, die für eine Aktivität mit dieser Eigenschaft geplant wurden, bei der Berechnung der Deckung, wobei der ursprüngliche Eintrag im Schichtplan sichtbar bleibt. |
| Bei optimierter Planung abweichend behandeln             | Nur verfügbar für Aktivitäten vom Typ Anwesenheit. Aktivitäten mit dieser Eigenschaft können nur exakt so geplant werden, wie sie konfiguriert wurden. Diese Aktivitäten können nicht ersetzt werden und ihre Dauer ist nicht flexibel.<br>Erfahre mehr dazu im [folgenden Abschnitt](#bei-optimierter-planung-abweichend-behandeln).                                                                                                                                                           |

## Bei optimierter Planung abweichend behandeln

Diese Eigenschaft hat zur Folge, dass die Funktionalität Optimierten Plan erstellen die Aktivität nur exakt so planen kann, wie sie konfiguriert wurde. Diese Eigenschaft wird üblicherweise verwendet, um Überstunden oder Back-Office-Aktivitäten zu planen.

Es gibt zwei verschiedene Anwendungsfälle für diese Aktivitätseigenschaft:

Option 1: Die Aktivität gehört zu einem Tagesmodell. In diesem Fall kann die Aktivität nur für die festgelegte Dauer und innerhalb des im Tagesmodell definierten Zeitraums geplant werden. Die Aktivität kann nicht verwendet werden, um ersetzbare Aktivitäten zu ersetzen. Wie mit der Aktivität bei der Schichtplanoptimierung umgegangen wird, hängt auch davon ab, wie die {% link_new Aktivität im Tagesmodell konfiguriert | features/administration/daymodels/daymodel-creation.md %} ist.

- Als fixes Element konfiguriert: Die Schichtplanoptimierung plant die Aktivität exakt für die Zeit, für die sie konfiguriert ist.
- Als Korridorelement konfiguriert: Die Schichtplanoptimierung kann die Aktivität innerhalb des festgelegten Korridors verschieben, um die Deckung für andere Aktivitäten zu optimieren.

Anwendungsbeispiel:

- Füge deinem Tagesmodell eine Back-Office-Aktivität ohne Mitarbeiterbedarf und mit einer Dauer von einer Stunde hinzu. Die Schichtplanoptimierung plant die Aktivität für genau eine Stunde. Wenn die Aktivität im Tagesmodell als Korridorelement konfiguriert ist, wird die Aktivität innerhalb des Korridors in das Zeitfenster verschoben, in dem sie die geringsten Auswirkungen auf die Deckung für andere Aktivitäten hat.

Option 2: Die Aktivität gehört nicht zu einem Tagesmodell. In diesem Fall kann die Schichtplanoptimierung die Aktivität nicht automatisch planen und sie auch nicht verwenden, um ersetzbare Aktivitäten zu ersetzen. Die Aktivität kann nur manuell geplant werden.

Anwendungsbeispiel:

- Erstelle eine Überstundenaktivität, die in keinem Tagesmodell enthalten ist. Die Funktionalität Optimierten Plan erstellen plant die Aktivität nicht und verwendet sie auch nicht, um ersetzbare Aktivitäten zu ersetzen. Füge die Aktivität bei Bedarf manuell zum Schichtplan hinzu. In diesem Anwendungsfall hast du immer die Kontrolle darüber, wann und für wie lange die Aktivität geplant und wem sie zugewiesen wird.

> Hinweis
>
> Diese Eigenschaft ist nur verfügbar, nachdem du die Aktivität erstellt hast.

## Teilaktivitäten

Du kannst Aktivitäten zu anderen Aktivitäten hinzufügen. Die Aktivität, der andere Aktivitäten hinzugefügt werden, wird eine Multiaktivität. Die hinzugefügten Aktivitäten sind die Teilaktivitäten der Multiaktivität. Mit Multiaktivitäten kannst du Personen mit mehreren Qualifikationen planen, wenn eine ihrer Qualifikationen benötigt wird. In der Aktivitätenliste sind Multiaktivitäten mit einem _Icon_{:.multiactivity-icon} markiert.

Die Funktionalität Optimierten Plan erstellen kann Multiaktivitäten planen, wenn du folgendes tust:

- Wähle den Typ Anwesenheit sowohl für die Multiaktivitäten als auch für alle ihre Teilaktivitäten.
- Konfiguriere sowohl die Multiaktivitäten als auch die Teilaktivitäten als bezahlt und planbar.
- Füge alle Teilaktivitäten (und anschließend auch die Multiaktivität) deiner Planungseinheit hinzu.
- Um zu steuern, wer geplant werden kann, weise jeder Teilaktivität eine andere Qualifikation zu.
- (Optional) Weise der Multiaktivität eine Qualifikation zu. In diesem Fall müssen die Personen diese Zusatzqualifikation besitzen, um die Multiaktivität ausführen zu können. Standardmäßig müssen der Multiaktivität keine Qualifikationen zugewiesen werden.

> Hinweis
>
> Wenn du nicht die Funktionalität Optimierten Plan erstellen verwendest, sondern nur die Joboptimierung ausführst, kann injixo ersetzbare Aktivitäten mit Multiaktivitäten ersetzen, solange ein Mitarbeiter mindestens eine der Teilaktivitäten der Multiaktivität ausführen kann.
