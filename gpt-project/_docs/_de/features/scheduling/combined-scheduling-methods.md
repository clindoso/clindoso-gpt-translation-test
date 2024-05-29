---
title: Planungsmethoden kombinieren
product_label:
  - advanced
  - enterprise
  - classic
description: Kombiniere die verschiedenen Planungsmethoden, um die Anforderungen deines Unternehmens zu erfüllen.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/availabilities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-time-pattern-models.md
---

Dir stehen viele Möglichkeiten zur Verfügung, die verfügbaren {% link_new Planungsmethoden| features/scheduling/scheduling-methods.md %} miteinander zu kombinieren, um einen Schichtplan zu erstellen, der sowohl die Anforderungen deiner Mitarbeiter als auch die deines Unternehmens berücksichtigt.

In den folgenden Beispielen findest du typische Anwendungsfälle dafür, wie du Mitarbeiter mit kombinierten Planungsmethoden planen kannst. Du kannst Planungsmethoden auch auf andere Weise kombinieren, um die Anforderungen deines Unternehmens bestmöglich zu erfüllen.

## Anwendungsfall 1: Mitarbeiter mit flexiblen Schichten plus Mitarbeiter mit festgelegten Arbeitszeiten/-tagen

Bei diesem Anwendungsfall kannst du die fixe Planung mit rotierenden flexiblen Schichten oder vollständig flexiblen Schichten kombinieren.

Um deine Mitarbeiter mit dieser Kombination zu planen, musst du als Erstes die in der folgenden Tabelle angegebenen Stammdaten konfigurieren und sie den entsprechenden Mitarbeitern zuweisen:

| Mitarbeiter mit flexiblen Schichten                            | Mitarbeiter mit festgelegten Arbeitszeiten/-tagen                                                                                                                                                                              |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Weise ihnen die Planungsmodelle zu, die du verwenden möchtest. | Erstelle spezifische Schichtfolgen, in denen die Zeiten bzw. Tage festgelegt sind, an denen sie arbeiten sollen und lasse den Rest der Woche leer.<br>Weise ihnen die Schichtfolgen und die entsprechenden Planungsmodelle zu. |

Um deine Mitarbeiter zu planen, gehe wie folgt vor:

1. Füge deine Schichtfolgen ein.
2. Nutze die Funktionalität **Optimierten Plan erstellen**.<br>injixo plant deine rotierenden und vollständig flexiblen Schichten und ergänzt damit die Deckung durch die Schichtfolgen.

## Anwendungsfall 2: Mitarbeiter mit rotierenden Schichten plus Mitarbeiter mit flexiblen Schichten

Bei diesem Anwendungsfall kannst du rotierende flexible Schichten und vollständig flexible Schichten miteinander kombinieren.

Um deine Mitarbeiter mit dieser Kombination zu planen, musst du als Erstes die in der folgenden Tabelle angegebenen Konfigurationselemente den entsprechenden Mitarbeitern zuweisen:

| Mitarbeiter mit rotierenden flexiblen Schichten  | Mitarbeiter mit vollständig flexiblen Schichten |
| ------------------------------------------------ | ----------------------------------------------- |
| Weise ihnen Planungsmodelle vom Typ B oder D zu. | Weise ihnen Planungsmodelle vom Typ A zu.       |

Nutze die Funktionalität **Optimierten Plan erstellen**.<br>Mitarbeiter mit rotierenden flexiblen Schichten werden entsprechend ihrer Planungsmodelle in der Rotation geplant. Die Lücken im Schichtplan werden dann mit Mitarbeitern mit vollständig flexiblen Schichten aufgefüllt.

## Anwendungsfall 3: Mitarbeiter mit rotierenden Schichten und eingeschränkter Verfügbarkeit

Dieser Anwendungsfall trifft auf Mitarbeiter zu, die in rotierenden Schichten arbeiten, aber zu bestimmten Zeiten nicht verfügbar sind, z.&nbsp;B. kann ein Mitarbeiter mittwochs nicht nach 17&nbsp;Uhr arbeiten.

Bei diesem Anwendungsfall kannst du Verfügbarkeiten und rotierende flexible Schichten miteinander kombinieren.

1. Konfiguriere {% link_new Verfügbarkeiten| features/administration/availabilities.md %} für deine Mitarbeiter, um festzulegen, wann sie nicht arbeiten können. In diesem Fall ist ein Mitarbeiter mittwochs nur bis 17&nbsp;Uhr verfügbar.
2. Weise ihm das entsprechende Planungsmodell zu.

In den Wochen, in denen der Mitarbeiter in der Morgenschicht arbeitet, wird er mittwochs geplant.<br>In den Wochen, in denen der Mitarbeiter die Abendschicht arbeitet, wird er mittwochs nicht geplant. Stattdessen wird er für andere Tage der Woche geplant.

## Anwendungsfall 4: Mitarbeiter mit festen Schichten und zeitlich eingeschränkter Verfügbarkeit

Dieser Anwendungsfall trifft auf Mitarbeiter zu, die in festen Schichten arbeiten, aber an bestimmten Tagen zeitlich eingeschränkt sind, z.&nbsp;B. wenn sie in Nachtschichten oder am Wochenende arbeiten, dies aber immer nur jede zweite Woche.

Bei diesem Anwendungsfall kannst du {% link_new Tagesmodelle vom Typ Verfügbarkeitsrahmen | features/administration/daymodels/daymodel-basics.md | #tagesmodelltypen %} zu {% link_new Schichtfolgen| features/administration/shift-sequences.md %} hinzufügen, um das Planungsergebnis für bestimmte Tage zu beeinflussen.<br>Sieh dir die beiden folgenden Beispiele an.

Um Mitarbeiter zu planen, die jedes zweite Wochenende arbeiten, gehe wie folgt vor:

1. Erstelle ein Tagesmodell vom Typ Verfügbarkeitsrahmen mit einem Zeitraum von Mitternacht (0:00) bis 0:01 als Blocker.
2. Füge das Tagesmodell einem Wochenende in einer Schichtfolge mit 14&nbsp;Tagen hinzu und lasse alle anderen Tage leer.
3. Weise die Schichtfolge den entsprechenden Mitarbeitern zu.
4. Füge die Schichtfolge in deinen Schichtplan ein.
5. Nutze die Funktionalität **Optimierten Plan erstellen**.

injixo plant für die entsprechenden Mitarbeiter an jedem zweiten Wochenende keine Schichten und optimiert die übrigen Tage.

Um Mitarbeiter zu planen, die jede zweite Woche in Nachtschichten arbeiten, gehe wie folgt vor:

1. Erstelle ein Tagesmodell vom Typ Verfügbarkeitsrahmen mit einem Zeitraum von Mitternacht (0:00) bis Mittag (12:00) als Blocker.
2. Füge das Tagesmodell in einer Schichtfolge mit 14&nbsp;Tagen an jedem Wochentag ein und lasse alle anderen Tage leer.
3. Weise die Schichtfolge den entsprechenden Mitarbeitern zu.
4. Füge die Schichtfolge in deinen Schichtplan ein.
5. Nutze die Funktionalität **Optimierten Plan erstellen**.

injixo plant die Nachtschicht in den Wochen, in denen die Mitarbeiter verfügbar sind und hält sich dabei an das Planungsmodell, das jedem Mitarbeiter zugewiesen ist. Für die anderen Wochen kann injixo jede Schicht planen, die mit dem Planungsmodell übereinstimmt.
