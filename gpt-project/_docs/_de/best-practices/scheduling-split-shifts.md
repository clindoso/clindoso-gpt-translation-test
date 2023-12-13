---
title: Split-Schichten planen
product_label:
  - advanced
  - enterprise
  - classic
description: Lerne, was Split-Schichten sind und wie Du sie für verschiedene Zwecke nutzen kannst.
redirect_from:
  - /de/best-practice-split-shifts/
---

In diesem Artikel lernst Du:
* was Split-Schichten sind.
* wie Du Split-Schichten nutzen kannst, um einen regelmäßig auftretenden starken Rückgang beim Mitarbeiterbedarf zu berücksichtigen.
* wie Du Split-Schichten nutzt, um mehr Flexibilität bei der Planung zu erreichen.
* wie Du die Nutzung von Split-Schichten auf einen oder mehrere Tage pro Mitarbeiter oder auf bestimmte Mitarbeiter beschränkst.
* wie Du Split-Schichten im Schichtwunsch-Verfahren nutzt.

## Was sind Split-Schichten?

Eine Split-Schicht besteht typischerweise aus zwei Schichten am selben Arbeitstag, die durch eine längere Pause getrennt sind. Die Pause ist länger als eine normale Mittagspause, oft mehr als 2 Stunden. Split-Schichten können aus mehr als zwei Schichten bestehen. Beachte, dass Split-Schichten normalerweise bei der Mehrheit der Mitarbeiter nicht beliebt sind.

Split-Schichten sind sinnvoll, wenn
- Du um die Mittagszeit oder zu einem anderen Zeitpunkt des Tages einen starken Rückgang beim Mitarbeiterbedarf hast, den Du bei der Planung berücksichtigen möchtest.
- Du Deine Planungsergebnisse verbessern willst, indem Du für mehr Planungsflexibilität sorgst.
- Du nur wenige Teilzeitkräfte hast.
- Wenn einige Mitarbeiter sich Split-Schichten wünschen.

## Split-Schichten für die volloptimierte Planung einrichten

Wenn Du Split-Schichten in der volloptimierten Planung nutzen willst, musst Du zunächst ein eigenes {% link_new Tagesmodell | features/administration/daymodels/daymodel-creation.md %} erstellen. Je nachdem, was Du erreichen willst, kannst Du zwischen Tagesmodellen mit festen und variablen Schichten wählen.

### Ein wiederkehrendes Bedarfstief berücksichtigen

Wenn Du ein wiederkehrendes Bedarfstief zu einer bestimmten Tageszeit berücksichtigen möchtest, solltest Du ein Tagesmodell vom Typ *Zeitlich fixierte Schicht* erstellen. Das Tagesmodell hat dann z.B. eine Gesamtdauer von 12 Stunden und eine lange Pause von 4 Stunden von 10 Uhr bis 14 Uhr, um das Mittagstief auszugleichen.

Die Einstellungen für ein zeitlich fixiertes Tagesmodell könnten wie folgt aussehen:

{{ 2 | image: 'Tagesmodell mit zeitlich fixierten Schichten erstellen', '50%' }}

### Mehr Flexibilität in der Planung erreichen

Wenn Du stattdessen insgesamt mehr Flexibilität in Deiner Schichtplanung möchtest, erstelle ein oder mehrere Tagesmodelle vom Typ *Variable Schicht*. Jedes Tagesmodell bekommt einen Pausenkorridor, in dem die Pause flexibel geplant werden kann. Wenn Du mehrere Tagesmodelle erstellst, kannst Du die Position und Länge des Pausenkorridors variieren. Damit gibst Du der volloptimmierten Planung noch mehr Möglichkeiten, den Bedarf bestmöglich zu decken.

Die Einstellungen für ein variables Tagesmodell könnten wie folgt aussehen:

{{ 3 | image: 'Tagesmodell vom Typ *Variable Schicht* erstellen', '50%' }}

## Die Verwendung von Split-Schichten begrenzen

Split-Schichten sind bei den meisten Mitarbeitern eher unbeliebt. Um eine maximale Anzahl von Split-Schichten pro Woche festzulegen, verwende {% link_new Planungsmodelle | features/administration/work-time-pattern-models.md %} und Wochenmodelle:

1. Erstelle ein {% link_new **Wochenmodell** | features/administration/work-time-pattern-models.md %} und füge Deine Standard-Tagesmodelle hinzu, die Du für die Planung verwenden möchtest. Setze die *Maximale Anzahl von Ausnahmetagen pro Woche* auf die Anzahl der Tage, an denen Du die Verwendung von Split-Schichten pro Mitarbeiter und Woche erlauben möchtest, z.B. 1.

    {{ 4 | image: 'Wochenmodell Standard', '50%' }}

2. Erstelle ein **zweites Wochenmodell** und füge das Tagesmodell mit den Split-Schichten hinzu, das Du zuvor erstellt hast. Behalte bei *Maximale Anzahl von Ausnahmetagen pro Woche* die Standardeinstellung 0 bei.

    {{ 5 | image: 'Wochenmodell-Ausnahme für Split-Schichten', '50%' }}

3. Erstelle ein neues **Planungsmodell**.

4. Wähle bei *Wochenmodell für Ausnahmetage* das Wochenmodell aus, das die Split-Schichten enthält. Dadurch stellst Du sicher, dass es für die Ausnahmetage verwendet wird.

    {{ 7 | image: 'Planungsmodell mit Split-Schichten', '50%' }}

5. Weise das Planungsmodell unter *WFM > Administration > Scheduling > Mitarbeiter*{:.breadcrumbs} Deinen Mitarbeitern zu.

Während der volloptimierten Planung prüft injixo nun, ob durch die Verwendung einer Split-Schicht eine bessere Deckung erreicht werden kann. Aufgrund der Konfiguration der Ausnahmetage werden Split-Schichten jedem Mitarbeiter aber nur für die von Dir angegebenen maximalen Tage pro Woche zugewiesen.

## Split-Schichten auf bestimmte Mitarbeiter beschränken

Du kannst festlegen, dass nur ausgewählte Mitarbeiter Split-Schichten durch die volloptimierte Planung erhalten. Verwende dazu den folgenden Trick:

1. Gehe zu _Plan > Konfiguration_{:.breadcrumbs} und wähle **Qualifikationen**.
2. Erstelle eine neue **Qualifikation** und nenne sie *Pause (Split-Schicht)*.
3. Gehe zu *WFM > Administration > Scheduling > Aktivitäten*{:.breadcrumbs}.
4. Erstelle eine **Aktivität** vom Typ *Pause* und nenne sie *Pause (Split-Schicht)*.
5. Scrolle in der neuen Aktivität zum Abschnitt **Qualifikationen** und weise die Qualifikation *Pause (Split-Schicht)* zu.
6. Gehe zu *WFM > Administration > Scheduling > Tagesmodelle*{:.breadcrumbs}.
7. Erstelle ein **Tagesmodell** für die Split-Schicht. Du kannst ein Tagesmodell vom Typ *Zeitlich fixierte Schicht* oder *Variable Schicht* erstellen, abhängig von Deinen Zielen (siehe oben).
8. Weise dem neuen Tagesmodell im Abschnitt **Pausen (Schichterzeugung)** die neu erstellte Pause namens *Pause (Split-Schicht)* zu.
9. Gehe zu *WFM > Administration > Scheduling > Mitarbeiter*{:.breadcrumbs}.
10. Weise den Mitarbeitern, die Split-Schichten erhalten sollen, im Abschnitt **Qualifikationsstufen** die Qualifikation *Pause (Split-Schicht)* zu.

Du hast nun
* eine gesonderte Pausenaktivität erstellt, die eine besondere Pausen-Qualifikation erfordert.
* die Pausenaktivität dem Tagesmodell der Split-Schicht zugewiesen.
* die Qualifikation für die neue Pause bestimmten Mitarbeitern zugewiesen.

Dies stellt sicher, dass nur diese Mitarbeiter das Split-Schicht-Tagesmodell in der automatischen Planung erhalten können.

## Split-Schichten im Schichtwunsch-Verfahren verwenden

Es gibt zwei Möglichkeiten, Split-Schichten im {% link_new Schichtwunsch-Verfahren | features/scheduling/schedules/schedules-shift-bidding.md %} zu verwenden:

* Du kannst fixe und variable Tagesmodelle verwenden, die Du extra für Split-Schichten erstellt hast.
* Du kannst bereits existierende kurze Tagesmodelle verwenden. Die Mitarbeiter erhalten dann zwei oder mehr davon pro Tag.

Einige Hinweise für die zweite Option:  

- Achte darauf, dass Mitarbeiter mehr als ein Tagesmodell erhalten können. Setze in den Verträgen der jeweiligen Mitarbeiter den Planungsparameter *2613*{:.id-label} *Maximale Anzahl von Schichten an einem Buchungstag* auf den Wert 2 oder höher.
- Stelle sicher, dass die Schichtbedarfstabelle unter *WFM > Scheduling > SchedulePro > Schichtbedarf*{:.breadcrumbs} genügend kurze Schichten definiert, damit alle Mitarbeiter ihr Wochensoll erreichen können.
- Wenn Du mit festen Schichten arbeitest, brauchst Du genügend Schichten am Anfang und am Ende des Tages, um zwei Schichten pro Mitarbeiter zuweisen zu können. Bei sich überschneidenden Schichten kann nur eine der Schichten zugewiesen werden.

> Schichtwunsch-Verfahren und volloptimierte Planung
>   
> Wenn eine Schicht bereits durch das Schichtwunsch-Verfahren zugewiesen wurde, können durch die volloptimierte Planung keine weiteren Schichten am selben Tag hinzugefügt werden. Der Grund dafür ist, dass die volloptimierte Planung nur ein Tagesmodell pro Tag zulässt.
