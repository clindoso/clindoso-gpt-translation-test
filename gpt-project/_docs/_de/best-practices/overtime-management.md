---
title: Mehrarbeit verwalten
product_label:
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du Aktivitäten so konfigurierst, dass du Überstunden für Mehrarbeit optimal planen und transparent dokumentieren kannst.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

Manchmal ist es nötig, dass deine Mitarbeiter Überstunden leisten, um ein vernünftiges Service-Level aufrechtzuerhalten. Gründe für Mehrarbeit können ein unerwartet hoher Workload sein oder Unterbesetzung aufgrund von hohen Abwesenheitszahlen bedingt durch Krankheit oder Urlaub.  
In vielen Fällen sehen die Verträge deiner Mitarbeiter vor, dass Überstunden mit einem höheren Stundenlohn abgegolten oder zum Urlaubsanspruch hinzugefügt werden. Es ist auch wichtig, weitere vertragliche Einschränkungen zu beachten, wie z.&nbsp;B. Ruhezeiten zwischen Schichten, wenn Mitarbeiter Überstunden leisten. Wenn dein Unternehmen Dienstleister ist, musst du möglicherweise auch deine Kunden über geplante Mehrarbeit informieren. 

In diesem Artikel erhältst du Tipps dazu, wie du Aktivitäten und Multiaktivitäten so konfigurierst, dass du ganz einfach Mehrarbeit planen und diese korrekt im Kennzahlenfenster für die Deckung und in deinen Reports anzeigen kannst.

Mehrarbeit sollte manuell im Schicht Center oder in Schedules als Ergänzung zum bestehenden Schichtplan geplant werden.

## Aktivitäten für Mehrarbeit erstellen

Im folgenden Beispiel verwenden wir eine Aktivität namens Anrufe. Führe die folgenden Schritte für alle Aktivitäten aus, für die du Mehrarbeit planen möchtest, z.&nbsp;B. für Anrufe oder E-Mails, aber nicht für Krankheit oder Urlaub.

1. {% link_new Erstelle und konfiguriere die Aktivität | features/administration/activities.md %} **Anrufe**. 
2. Kopiere die Aktivität **Anrufe** und nenne die neue Aktivität **Anrufe Mehrarbeit**. Du musst dieser Aktivität keine Qualifikationen hinzufügen.  
  - Aktiviere die Checkbox **Bei optimierter Planung abweichend behandeln**.
  - Vergewissere dich, dass die Checkbox **Wünschbar in Me** nicht aktiviert ist.
3. Füge in **Anrufe Mehrarbeit** die Aktivität **Anrufe** als Teilaktivität hinzu.  
  **Anrufe Mehrarbeit** ist jetzt eine Multiaktivität.
4. Füge beide Aktivitäten der entsprechenden Planungseinheit hinzu. Füge die Aktivität für die Mehrarbeit keinem Tagesmodell hinzu.

So konfiguriert kann die Aktivität Anrufe Mehrarbeit nur manuell geplant und während der Schichtplanoptimierung nicht ersetzt werden. Die Mitarbeiter können sich diese Aktivität in injixo Me nicht wünschen.

Indem du den Zusatz "Mehrarbeit" zum Namen der Multiaktivität hinzufügst, ist es für dich und deine Mitarbeiter auf dem Schichtplan sofort ersichtlich, wann sie Überstunden leisten, für wie lange und an welcher Aufgabe sie dabei arbeiten.

## Mehrarbeit planen

Du kannst Mehrarbeit entweder in _Plan > Schicht Center_{:.breadcrumbs} oder in _Plan > Schedules_{:.breadcrumbs} manuell planen.

Um Aktivitäten für Mehrarbeit im Schicht Center hinzuzufügen, gehe wie folgt vor:

1. Wähle die Planungseinheit und optional die Auswahl, zu der der Mitarbeiter gehört, für den du Mehrarbeit planen möchtest.
2. Klicke doppelt auf die Tageszelle des Mitarbeiters für den Tag, an dem er Überstunden leisten soll. Klicke auf den Tab **Multiaktivitäten** und wähle **Anrufe Mehrarbeit**.
3. Lege eine Start- und Endzeit für die Aktivität fest.
4. Klicke auf _OK_{:.doc-button}.

Die geplanten Überstunden werden sofort im Schichtplan und auf dem Tab Aktivitäten im {% link_new Kennzahlenfenster | features/scheduling/shiftcenter/shift-center-overview.md | #kennzahlenfenster %} angezeigt. Wenn du den Tab Aktivitäten so konfigurierst, dass darin die Deckung angezeigt wird, aktualisiert sich das Kennzahlenfenster und zeigt die geplanten Überstunden an.

Um Aktivitäten für Mehrarbeit in _Plan > Schedules_{:.breadcrumbs} hinzuzufügen, gehe wie folgt vor:

1. Doppelklicke auf eine Zelle im Schichtplan, um die Bearbeitungsansicht zu öffnen.
2. Klicke auf _Neue Aktivität hinzufügen_{:.doc-button}.  
  Eine neue Zeile mit der Aktivität wird hinzugefügt.
3. Wähle aus dem Dropdown-Menü in der neuen Zeile die Option **Anrufe Mehrarbeit**.
4. Lege eine Start- und Endzeit für die Aktivität fest.
5. Klicke auf _Speichern_{:.doc-button}.

## Reporting

Im Report **Aktivitäten in Stunden** ist zu sehen, dass der Mitarbeiter Mehrarbeit geleistet hat, da der Name der Aktivität diese Information enthält. So werden alle geleisteten Überstunden dokumentiert und können von den betreffenden Personen eingesehen werden, z.&nbsp;B. in der Finanzabteilung, um Ausgleichszahlungen zu veranlassen.
