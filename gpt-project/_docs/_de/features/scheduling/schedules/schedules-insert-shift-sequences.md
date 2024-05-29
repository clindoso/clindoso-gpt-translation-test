---
title: Schichtfolgen einfügen
product_label:
  - essential
  - advanced
  - enterprise
description: Unter Schedules kannst du mit Schichtfolgen wiederkehrende Schichtrotationen, Aktivitäten oder Verfügbarkeiten planen.
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
---

Schichtfolgen sind feste, sich wiederholende Abfolgen von Schichten, Aktivitäten oder Verfügbarkeiten. Du kannst Schichtfolgen für ausgewählte Mitarbeiter einfügen, um z.&nbsp;B. regelmäßig wiederkehrende Aufgaben oder Verfügbarkeiten zu planen.

## Voraussetzungen

Bevor du Schichtfolgen in den Schichtplan einfügen kannst, musst du folgende Voraussetzungen erfüllen:

- {% link_new Erstelle | features/administration/shift-sequences.md %} mindestens eine Schichtfolge.
- {% link_new Weise | features/administration/employee-overview.md | #eine-schichtfolge-zuweisen %} die Schichtfolge(n) einem Mitarbeiter zu.

## Schichtfolgen filtern

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Wähle rechts aus dem Dropdown-Menü **Planungsaktionen** die Option _Schichtfolgen einfügen_{:.doc-button} aus.
3. Wähle eine Planungseinheit aus.
4. (Optional) Wähle eine Auswahl aus.
5. Wähle einen Zeitraum aus.

   > Du kannst Schichtfolgen für einen Zeitraum von bis zu zwei Jahren einfügen.

   Im Abschnitt **Übersicht** siehst du Schichtfolgen, die deinem Filter entsprechen. Die Tabelle zeigt die Parameter an, die gesetzt werden, wenn du einem Mitarbeiter eine vorhandene Schichtfolge zuweist:

   | Option                   | Beschreibung                                                                                                                                                                                                                                                                                                                                  |
   | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Personalnummer           | Eindeutige Mitarbeiterkennung                                                                                                                                                                                                                                                                                                                 |
   | Name                     | Name des Mitarbeiters, dem die Schichtfolge zugewiesen ist                                                                                                                                                                                                                                                                                    |
   | Schichtfolge             | Name der zugewiesenen Schichtfolge                                                                                                                                                                                                                                                                                                            |
   | Reihenfolge              | Definiert die Reihenfolge, in der Schichtfolgen eingefügt werden, wenn ein Mitarbeiter mehrere Schichtfolgen hat. Schichtfolgen mit niedrigeren Werten werden zuerst eingefügt und werden möglicherweise von nachfolgenden Schichtfolgen überschrieben.                                                                                       |
   | Mitarbeiterzeile         | Legt fest, welche Zeile der Schichtfolge für den Mitarbeiter verwendet wird.                                                                                                                                                                                                                                                                  |
   | Referenzdatum            | Starttag der Schichtfolge. Wenn du eine Schichtfolge von mehr als sieben Tagen verwendest, um mehrere Mitarbeiter zu planen, lege für sie jeweils ein eigenes Referenzdatum fest. So startet die erste Woche ihrer jeweiligen Schichtfolge in unterschiedlichen Wochen und ihnen werden nicht dieselben Schichten zur selben Zeit zugewiesen. |
   | Gültig vom<br>Gültig bis | Zeitraum, für den die Schichtfolge dem Mitarbeiter zugewiesen wurde. Außerhalb des konfigurierten Gültigkeitszeitraums wird die Schichtfolge nicht in den Schichtplan eingefügt. Wenn der Gültigkeitszeitraum der Schichtfolge vollständig innerhalb des ausgewählten Zeitraums liegt, werden keine Daten angezeigt.                          |

## Schichtfolgen einfügen

1. Um einen Mitarbeiter auszuwählen, aktiviere die Checkbox zu Beginn der jeweiligen Zeile. Um alle Mitarbeiter auf einmal auszuwählen, aktiviere die Checkbox in der Kopfzeile.
2. (Optional) Wähle aus dem Dropdown-Menü **Optionen** unter der Übersichtstabelle aus, wie beim Einfügen von Schichtfolgen mit vorhandenen Schichtplänen umgegangen werden soll.

   | Option                                 | Beschreibung                                                                                             |
   | -------------------------------------- | -------------------------------------------------------------------------------------------------------- |
   | Ganztägige Aktivitäten löschen         | Ganztägige Aktivitäten werden gelöscht. Aktivitäten, die nicht ganztägig sind, bleiben erhalten.         |
   | Verfügbarkeitsrahmen löschen           | Verfügbarkeitsrahmen werden gelöscht.                                                                    |
   | Alle Aktivitäten und Schichten löschen | Alle Aktivitäten und Schichten werden von der Zielebene gelöscht. Verfügbarkeitsrahmen bleiben erhalten. |

   > Die ausgewählten Optionen werden je Mitarbeiter nur beim ersten Einfügen einer Schichtfolge angewendet.

3. (Optional) Ändere die Zielebene. Standardmäßig ist die Ebene Plan ausgewählt.
4. Klicke auf _Schichtfolgen einfügen_{:.doc-button}.

> Hinweis
>
> Wenn eine Schichtfolge bereits gelöschte Tagesmodelle enthält, werden diese dennoch in den Schichtplan übernommen und in Schedules und im Schicht Center mit einer gestrichelten Umrandung markiert.

## Reports mit Ergebnissen einsehen

Im Abschnitt **Historie** kannst du auf Reports zum aktuellen und vergangenen Einfügen von Schichtfolgen zugreifen. Klicke auf den Link **Details anzeigen**, um ggf. herauszufinden, warum Schichten oder Aktivitäten nicht eingefügt werden konnten. Eine vierstellige ID am Anfang einer Zeile verweist auf die jeweilige Planungsregel, die das Einfügen einer Schichtfolge verhindert.

Um Einträge aus dem Abschnitt **Historie** zu löschen, aktiviere die Checkbox neben einem Eintrag und klicke auf _Einträge löschen_{:.doc-button}. Um alle Einträge auf einmal auszuwählen, aktiviere die Checkbox ganz oben.

## Überschreiben von geplanten Aktivitäten verhindern

Wenn du mit Schichtfolgen ganztägige Aktivitäten in den Schichtplan einfügst, überschreibt injixo standardmäßig andere ganztägige Aktivitäten im Schichtplan, z.&nbsp;B. Abwesenheiten. Um das zu verhindern, aktiviere die Planungsregel _2645_{:.id-label} _Überschreiben von ganztägigen Aktivitäten durch Schichten oder Aktivitäten_.

Um das Überschreiben untertägiger Aktivitäten vom Typ Abwesenheit, Krankheit, Urlaub oder Meeting zu verhindern, aktiviere die Planungsregel _2648_{:.id-label} _Schreibschutz für Aktivitäten im Schicht Center_.

> Hinweis
>
> Schichtfolgen werden mit dem aktuell angemeldeten Benutzerkonto eingefügt. Planungsregeln können pro Benutzer unterschiedlich konfiguriert werden. Wenn du mehrere Konten hast, stelle sicher, dass du mit dem richtigen Konto angemeldet bist.

## Gültigkeitszeiträume

Wenn du Schichtfolgen einfügst, können Gültigkeitszeiträume das Ergebnis beeinflussen.

Um einen Zeitraum festzulegen, innerhalb dessen ein Tagesmodell geplant werden kann, kannst du den Gültigkeitszeitraum deiner Tagesmodelle begrenzen. Lege dafür ein Datum für die Parameter Gültig vom und Gültig bis fest. Nach dem Einfügen von Schichtfolgen wird möglicherweise folgende Fehlermeldung im Ergebnis-Report angezeigt: [2151] Das Tagesmodell der Schicht 'Schichtname' ist am Buchungstag dd.mm.yyyy nicht gültig. Aus diesem Grund kann die Schicht nicht eingeplant werden.

In jeder Schichtfolge kannst du einen Zeitraum festlegen, innerhalb dessen die Schichtfolge eingefügt werden darf. Standardmäßig sind Schichtfolgen jederzeit gültig. Wenn du den Zeitraum begrenzt, wird die Schichtfolge nicht außerhalb des festgelegten Zeitraums eingefügt. In diesem Fall wird keine Fehlermeldung ausgegeben.

Gültigkeitszeiträume, die in persönlichen Tagesmodellen (Tagesmodelle, die einzelnen Mitarbeitern zugewiesen sind) festgelegt sind, wirken sich nicht auf Schichtfolgen aus. Diese Tagesmodelle werden dennoch in Schichtfolgen eingefügt.

Hinweis: Wenn eine Schichtfolge bereits gelöschte Tagesmodelle enthält, werden diese dennoch in den Schichtplan übernommen und in Schedules und im Schicht Center mit einer gestrichelten Umrandung markiert. In diesem Fall wird keine Fehlermeldung ausgegeben.
