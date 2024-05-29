---
title: Schichtfolgen einfügen
description: Plane mit Schichtfolgen sich wiederholende Abfolgen von Schichten, Aktivitäten oder Verfügbarkeiten (SchedulePro).
product_label:
  - classic
redirect_from:
  - /de/best-practice-shift-sequences/
  - /de/scheduling-shift-sequences/
  - /de/scheduling-insert-shift-sequences/
redirect_reason: removed best practice articles July 2020
promote-service: new-planner-training
---

Schichtfolgen sind feste, sich wiederholende Abfolgen von Schichten, Aktivitäten oder Verfügbarkeiten. Diese werden für die Planung von regelmäßig wiederkehrenden Aufgaben oder Verfügbarkeiten Deiner Mitarbeiter genutzt. Vor dem Einfügen musst Du die {% link_new Schichtfolgen anlegen | features/administration/shift-sequences.md %} und {% link_new Deinen Mitarbeitern zuordnen | features/administration/employee-overview.md | #eine-schichtfolge-zuweisen %}.

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Wenn Du injixo Essential WFM, Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen die Funktion {% link_new Schichtfolgen einfügen | features/scheduling/schedules/schedules-insert-shift-sequences.md %} unter _Plan > Schedules_{:.breadcrumbs}.

## Parameter festlegen

Über folgenden Dialog in _WFM > Scheduling > SchedulePro > Schichtfolgen einfügen_{:.breadcrumbs} kannst Du Schichtfolgen einfügen:

{{ 1 | image: 'Schichtfolgen einfügen', '75%' }}

1. Wähle ein **Start- und Enddatum** (Maximal: 2 Jahre), eine Planungseinheit, ggf. eine Auswahl und die Zielebene aus.
2. Bestätige Deine Parameter mit _Mitarbeiterliste aufbauen_{:.doc-button}. Es erscheint die [Mitarbeiterliste](#mitarbeiterliste).
3. Selektiere über die **Checkbox vor der Personalnummer einzelne Mitarbeiter** oder nutze die erste Checkbox oben links, um alle Mitarbeiter auszuwählen.
4. Klicke auf _Schichtfolgen einfügen_{:.doc-button}.

Die Schichtfolgen werden eingefügt. Am Ende erscheint ein weiteres Fenster, ggf. mit Meldungen zu Problemen beim Einfügen.

## Optionen

Im Bereich _Optionen_{:.menu-item} gibt es verschiedene Optionen für das Löschen von bereits bestehendem Planinhalt:

| Option                                 | Erläuterung                                                                                                                                                                              |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ganztägige Aktivitäten löschen         | Bestehende ganztägige Aktivitäten der Mitarbeiter werden vor dem Einfügen aus der Zielebene gelöscht und durch die ausgewählte Schichtfolge ersetzt.                                     |
| Verfügbarkeitsrahmen löschen           | Bestehende Verfügbarkeitsrahmen der Mitarbeiter werden durch die ausgewählte Schichtfolge überschrieben.                                                                                 |
| Alle Aktivitäten und Schichten löschen | Bestehende Aktivitäten und alle Schichten der Mitarbeiter auf der Zielebene werden gelöscht und durch die ausgewählte Schichtfolge ersetzt; Verfügbarkeitsrahmen bleiben dabei erhalten. |

Die Optionen werden nur beim Einfügen der ersten Schichtfolge eines Mitarbeiters berücksichtigt, d.&nbsp;h. bei einer aktivierten Option wird der Planinhalt nur beim Einfügen der ersten Schichtfolge gelöscht.

Vorhandene ganztägige Aktivitäten werden grundsätzlich durch ganztägige Aktivitäten aus einer Schichtfolge ersetzt, wenn die existierenden Einträge nicht vom Typ `Abwesenheit`, `Krankheit`, `Urlaub` oder `Meeting` sind. Um ein Überschreiben von ganztägigen Aktivitäten (z.B. Urlaub) durch untertägige Aktivitäten oder Schichten aus einer Schichtfolge zu verhindern, aktiviere die Planungsregel _2645_{:.id-label} _Überschreiben von ganztägigen Aktivitäten durch Schichten oder Aktivitäten_.

Weitere Planungsregeln können einen Einfluss auf das Ergebnis haben:

- _2648_{:.id-label} _Schreibschutz für Aktivitäten im Schicht Center_
- _2613_{:.id-label} _Maximale Anzahl von Schichten an einem Buchungstag gemäß Vertrag_
- _2602_{:.id-label} _Maximale Dauer einer Aktivität gemäß Vertrag_
- _2611_{:.id-label} _Verfügbarkeit des Mitarbeiters_

## Mitarbeiterliste

Die Mitarbeiterliste, die nach dem Klick auf _Mitarbeiterliste aufbauen_{:.doc-button} erscheint, enthält Informationen zu allen Schichtfolgen Deiner Mitarbeiter.

{{ 2 | image: 'Schichtfolgen der Mitarbeiter' }}

Neben der Personalnummer und dem Namen des Mitarbeiters enthält die Liste auch Informationen zur Schichtfolge selbst (Name, Länge, Gültigkeit). Die Informationen Reihenfolge, Mitarbeiterzeile und Referenzdatum stammen aus der Zuordnung zum Mitarbeiter. Gelöschte Schichtfolgen, die noch Mitarbeitern zugeordnet sind, erscheinen in kursiv.

### Reihenfolge

Beim Einfügen von mehreren Schichtfolgen pro Mitarbeiter werden diese in aufsteigender Reihenfolge in den Schichtplan eingefügt.
Ob der Inhalt einer Schichtfolge tatsächlich durch den Inhalt einer anderen Schichtfolge ersetzt wird, hängt vom Inhalt der einzufügenden Schichtfolge, von den bereits vorhandenen Planinhalten, von den ausgewählten Optionen sowie der Prüfung durch Planungsregeln ab.

### Referenzdatum

Für jeden Wochentag muss injixo entscheiden, ob das Muster für Woche 1, Woche 2 usw. verwendet werden soll. Das Referenzdatum gibt hierfür einen Fixpunkt vor. Der erste Tag der Schichtfolge wird immer in Bezug auf das Referenzdatum eingefügt. Es wird bei der Zuordnung der Schichtfolge zum Mitarbeiter definiert und sollte immer auf dem ersten Tag der Woche liegen. Standardmäßig ist der Beginn deiner Arbeitswoche auf Sonntag bzw. Montag festgelegt, je nachdem, in welcher Region du dich befindest. Falls du einen anderen Tag dafür festlegen möchtest, wende dich an deinen Consultant.

Beispiel: Der Zeitraum für das Einfügen ist der 9. - 29. Juli. Die Schichtfolge beginnt ab 9. Juli, das Referenzdatum ist aber der 2. Juli. Für den 9. Juli wird der 8. Tag der Schichtfolge, z.B. Montag 2, eingefügt.
