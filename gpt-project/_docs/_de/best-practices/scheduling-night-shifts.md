---
title: Nachtschichten planen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du mit injixo Nachtschichten planst.
---

injixo bietet dir verschiedene Möglichkeiten zur Planung von Nachtschichten.

Hinweise:

- injixo prüft die Einhaltung von Ruhezeiten vor und nach einer Nachtschicht. Sieh dir deshalb die ganze Woche an.
- Bei einem 24/7-Betrieb musst du im Forecast auch den Mitarbeiterbedarf für den Montag der Folgewoche berechnen. Andernfalls werden Mitarbeiter am Montag nicht korrekt geplant.
- Essential WFM unterstützt nur Szenario 1.

## Szenario 1: Nachtschichten werden gerecht auf alle Mitarbeiter verteilt

Um sicherzustellen, dass Nachtschichten gerecht auf alle Mitarbeiter verteilt werden, kannst du {% link_new Schichtfolgen | features/administration/shift-sequences.md %} verwenden.

Rechne zuerst aus, wie viele Nachtschichten du benötigst und überlege, wie du diese möglichst gerecht auf alle Mitarbeiter verteilen kannst. Beachte dabei, dass du beim Ein- und Austritt von Mitarbeitern ggf. die Schichtfolgen bearbeiten und neu verteilen musst.

{{ 3 | image: 'Schichtfolge mit verteilten Nachtschichten', '80%' }}

Anschließend kannst du einen optimierten Plan erstellen, um die übrigen Schichten zu verteilen.

**Vorteil:**

- Nachtschichten werden immer gerecht auf alle Mitarbeiter verteilt.

**Nachteile:**

- Hoher manueller Aufwand, um die Schichtfolgen aktuell zu halten
- Keine Flexibilität
- Manuelle Planung bei Ausfällen oder Urlauben notwendig

## Szenario 2: Nachtschichten stellen die Ausnahme dar

Du kannst deine Nachtschichten in deine bestehenden {% link_new Planungsmodelle | best-practices/fair-shift-distribution.md | #optimierte-rotation-planungsmodelle %} integrieren.

Dazu benötigst du ein eigenes Wochenmodell für die Wochen mit Nachtschichten. Das Wochenmodell enthält nur Tagesmodelle für Nachtschichten. Wähle das Wochenmodell als _Wochenmodell für Ausnahmetage_ in deinem Planungsmodell.

Die Anzahl der möglichen Nachtschichten legst du im Wochenmodell fest (_maximale Anzahl von Ausnahmetagen pro Woche_). So kannst du die Nachtschichten pro Woche festlegen.

Da die Nachtschichten nur nach Bedarf verteilt werden, kann es für manche Mitarbeiter auch Wochen ohne Nachtschichten geben.

{{ 2 | image: 'Möglicher Aufbau eines Planungsmodells mit Nachtschicht-Ausnahme-Wochenmodell', '80%' }}

**Vorteil:**

- Da die meisten Contact Center in der Regel ausgelastet und unterbesetzt sind, werden die eigentlich optionalen Ausnahmetage tendenziell immer geplant.

**Nachteile:**

- Da die Mitarbeiter ihre Nachtschichten zufällig erhalten und du keine Rotation für Nachtschichten festlegen kannst, kann es zu einer unfairen Verteilung kommen.
- Bei einer hohen Unterdeckung innerhalb des Tages kann es zu Unterdeckung bei den Nachtschichten kommen.

## Szenario 3: Mitarbeiter werden wochenweise für Nachtschichten geplant

Auch in diesem Szenario integrierst du deine Nachtschichten in deine bestehenden {% link_new Planungsmodelle | best-practices/fair-shift-distribution.md | #optimierte-rotation-planungsmodelle %}.

Lege für die Nachtschichtwoche ein eigenes Wochenmodell an. Füge aber nur Tagesmodelle für Nachtschichten hinzu.

{{ 1 | image: 'Möglicher Aufbau eines Planungsmodells mit Nachtschicht-Woche', '80%' }}

**Vorteil:**

- Alle Mitarbeiter werden gleichmäßig für Nachtschichten geplant.

**Nachteil:**

- Nachtschichten können immer nur für volle Wochen geplant werden.

## Szenario 4: Mitarbeiter können sich Nachtschichten wünschen

Wenn deine Mitarbeiter ihre Nachtschichten selbst wählen sollen, nutze das {% link_new Schichtwunsch-Verfahren | features/scheduling/shift-bidding.md %}. Du kannst das Schichtwunsch-Verfahren wie üblich für alle Schichten oder nur für Nachtschichten verwenden.

Du kannst Schichten verlosen und zuweisen oder das Schichtwunsch-Verfahren mit optimierten Plänen kombinieren. In letzterem Fall kannst du allerdings nicht gleichzeitig mit Planungsmodellen arbeiten.

Du kannst die maximale Anzahl der Nachtschichten über den {% link_new Schichtbedarf | features/scheduling/shift-requirement.md %} begrenzen.

{{ 4 | image: 'Schichtbedarfstabelle anpassen', '80%' }}

**Vorteil:**

- Gefühlte Fairness, weil Nachtschichten selbst gewählt werden

**Nachteile:**

- Nachtschichten müssen manuell geplant werden, wenn sich nicht genügend Mitarbeiter Nachtschichten wünschen.
- Nachtschichten müssen vor der restlichen Planung gewünscht werden.

## Nachtschichtbezogene Einstellungen

- _48161_{:.id-label} _Modus für die Definition von Nachtarbeit_  
- _48121_{:.id-label} _Nachtarbeit früheste Startzeit_  
- _48122_{:.id-label} _Nachtarbeit Dauer_  
- _48162_{:.id-label} _Referenzuhrzeit für Nachtarbeit_

## Zusätzliche Beschränkungen für Nachtschichten in Verträgen

- _2632_{:.id-label} _Maximale Anzahl an Buchungstagen mit Nachtarbeit pro Woche gemäß Vertrag_
- _2633_{:.id-label} _Maximale Anzahl an Buchungstagen mit Nachtarbeit pro Monat gemäß Vertrag_
- _2634_{:.id-label} _Maximale Anzahl an aufeinander folgenden Buchungstagen mit Nachtarbeit gemäß Vertrag_
- _2635_{:.id-label} _Minimale Anzahl freier Tage nach Nachtarbeit_
- _2636_{:.id-label} _Ruhezeit nach Nachtarbeit_
- _2637_{:.id-label} _Maximale Anzahl Arbeitstage vor Nachtarbeit_
