---
title: Referenzdatum
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lerne, wie das Referenzdatum von Schichtfolgen und Planungsmodellen verwendet wird, um sich wiederholende Planungsmuster darzustellen.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-time-pattern-models.md
---

{% link_new Schichtfolgen | features/administration/shift-sequences.md %} und {% link_new Planungsmodelle | features/administration/work-time-pattern-models.md %} erfordern bei Zuweisung zum Mitarbeiter ein **Referenzdatum**, um einen Startpunkt für die Rotation festzulegen. Dieser Artikel erläutert, wofür das Referenzdatum verwendet wird und worauf bei der Eingabe zu achten ist.

## Fixpunkt für die Planung

Vielleicht ist Dir aufgefallen, dass sich Schichtfolgen auf "Woche 1", "Woche 2" usw. beziehen. In ähnlicher Weise werden Wochenmodelle innerhalb von Planungsmodellen an Position 1, Position 2 usw. aufgelistet.

In beiden Fällen gibst Du normalerweise nur wenige Wochen an, die der Länge des Musters entsprechen, das sich wiederholen soll, anstatt ein Muster für das ganze Jahr zu definieren.

injixo muss für die Planerstellung für jeden beliebigen Wochentag wissen, ob es das Muster für Woche 1, Woche 2 usw. verwenden soll. Das Referenzdatum liefert einen Fixpunkt, der es injixo ermöglicht, diese Frage zu beantworten.

> Referenzdatum vs. Gültig von/Gültig bis Datum
>
> Beachte, dass das Gültig von/bis Datum und das Referenzdatum völlig unterschiedlichen Zwecken dienen. Das Referenzdatum ist immer obligatorisch. Es definiert, welche Woche eine Schichtfolge bzw. welches Wochenmodell eines Planungsmodells verwendet wird. Die Gültig von/bis Daten sind immer optional und werden verwendet, um anzugeben, wann ein bestimmtes Stammdatenelement mit einem Mitarbeiter oder einer Planungseinheit verknüpft ist.

## Beispiel: Schichtfolgen

Beim Einfügen von Schichtfolgen behandelt injixo das Referenzdatum als den ersten Tag der Schichtfolge. Wenn also das Referenzdatum der 1. Januar ist und die Schichtfolge 14 Tage beträgt, ist der 1. bis 7. Januar Woche 1 und der 8. bis 14. Januar Woche 2.

So kannst Du die Schichtfolge für immer wiederholen, indem Du einfach ein _Datum_ als ersten _Referenzpunkt_ verwendest.

## Beispiel: Planungsmodelle

Genau wie bei den Schichtfolgen wird auch bei den Planungsmodellen das Referenzdatum als der erste Tag der wöchentlichen Rotation behandelt.  
Wenn das Referenzdatum also der 1. Januar ist und das Planungsmodell zwei Wochen lang ist, wird in der ersten Woche (1. bis 7. Januar) das erste Wochenmodell und in der zweiten Woche (8. bis 14. Januar) das zweite Wochenmodell verwendet.  
Die feste Reihenfolge der Wochenmodelle gilt nur für Planungsmodelle vom Typ **B - Starre Rotation** und **D - Kombi-Rotation (A/B)**.

## Nutze immer den ersten Tag der Woche

Das Referenzdatum muss immer auf den ersten Tag der Woche gesetzt werden, wie in Einstellung *48420*{:.id-label} *Erster Tag der Planungswoche* definiert. Wenn das Referenzdatum auf einen anderen Wochentag gesetzt wird, wechselt die Schichtfolge oder das Planungsmodell nach 7 Tagen (oder dem Ende der Schichtfolge, wenn diese weniger als 7 Tage beträgt) in eine neue Woche.

Wenn z.B. der 1. März ein Mittwoch ist und als Referenzdatum festgelegt ist, dann wird eine Schichtfolge Mittwoch, den 1. bis Dienstag, den 7. als Woche 1 und Mittwoch, den 8. bis Dienstag, den 14. als Woche 2 behandeln. Dadurch wird auch der für Montag in der Schichtfolge angegebene Plan in den Mittwoch eingefügt.

In diesem Szenario verwendet ein Planungsmodell vom Typ B oder D das in Position 1 definierte Wochenmodell für Woche 1 (Mittwoch bis Dienstag) und das in Position 2 definierte Wochenmodell für Woche 2 beginnend mit Mittwoch, den 8. März.

## Best Practice: Das gleiche Referenzdatum für mehrere Mitarbeiter

Als bewährte Praxis empfehlen wir, für alle Mitarbeiter das gleiche Referenzdatum (einschließlich des Jahres) festzulegen, unabhängig davon, wann sie eingestellt werden. So stellst Du sicher, dass injixo bei Mitarbeitern mit der gleichen Schichtfolge oder dem gleichen Planungsmodell für jeden beliebigen Tag im Jahr dasselbe Muster verwendet.

Um die Rotationen zwischen den Mitarbeitern auszugleichen, kannst Du zwar für das Referenzdatum unterschiedliche Startdaten hinterlegen, jedoch ist es nachträglich schwer das nachzuvollziehen und kann zu massiven Fehlern führen. Bei der Verwendung desselben Referenzdatums für alle Mitarbeiter musst Du mehr Zeilen in einer Schichtfolge oder mehrere Planungsmodelle anlegen, allerdings kannst Du dadurch Fehler leichter erkennen und beheben.
