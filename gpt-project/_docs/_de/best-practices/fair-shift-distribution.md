---
title: Faire Verteilung von Schichten
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Sorge für eine gleichmäßigere Verteilung der Schichten und eine bessere Akzeptanz des Schichtplans.
redirect_from:
  - /de/best-practice-fair-shift-distribution/
---

Unabhängig davon, ob Du die volloptimierte Planung oder das Schichtwunsch-Verfahren einsetzt, kann es passieren, dass manche Mitarbeiter aufgrund von Verfügbarkeiten oder bestimmten Qualifikationen häufiger unbeliebte Schichten erhalten als andere. Dies kann schnell zu Unzufriedenheit unter den Mitarbeitern, sinkender Arbeitsmoral und erhöhter Personalfluktuation führen.

Dieser Artikel gibt einige Best-Practice-Tipps, die eine gleichmäßigere Verteilung der Schichten und eine größere Fairness gewährleisten.

## Schichtfolgen für eine gleichmäßige Verteilung

Nutze Schichtfolgen, um eine gleichmäßigere Verteilung von Aufgaben oder Schichten zu gewährleisten. Mit Schichtfolgen erstellst Du Schichtpläne, die sich regelmäßig wiederholen.

{{ 1 | image: 'Schichtfolgen'}}

Vor allem für Samstagseinsätze sind Schichtfolgen empfehlenswert. Samstagsschichten werden gleichmäßig unter Deinen Mitarbeiter verteilt. Deine Mitarbeiter können sogar absehen, wann sie voraussichtlich das nächste Mal für eine Samstagsschicht eingeteilt werden.

### Schichtfolgen mit optimierten Schichtplänen kombinieren

Wenn Du die Vorteile von optimierten Schichtplänen nutzt, aber trotzdem einige Schichten gleichmäßig verteilen möchtest, ist es möglich, Schichtfolgen mit der Optimierung zu kombinieren. Wenn Du z. B. Wochenendschichten rotieren möchtest, kannst Du eine {% link_new Tagesmodell-Verfügbarkeit | features/administration/availabilities.md %} erstellen, die den Tag als nicht mehr verfügbar einstellt. Diese Verfügbarkeit fügst Du dann an jedem zweiten Wochenende in einer Schichtfolge ein, während alle anderen Tage frei bleiben. Bevor Du die optimierte Schichtpläne erstellst, füge einfach die Schichtfolge in den Schichtplan ein.

In Wochen mit einer blockierenden Verfügbarkeit erhält der Mitarbeiter keinen Schichtplan für das Wochenende. Der Schichtplan unter der Woche wird optimiert. In Wochen, in denen das Wochenende nicht blockiert ist, kann der Mitarbeiter am Wochenende arbeiten und wird voraussichtlich auch dafür eingeteilt. Der Schichtplan für das Wochenende wird jedoch weiterhin optimiert, ebenso wie der Schichtplan für den Rest der Woche.

## Optimierte Rotation: Planungsmodelle

Wenn Du wechselnde Schichtzeiten planst, verwende *Planungsmodelle*{:.menu-item}. 

Mit Planungsmodellen kannst Du Deine Mitarbeiter wöchentlich rotierend in Früh-, Mittel- und Spätschichten zu planen (als Beispiel). In jeder Woche werden die Schichten, die geplant werden können, aus einer Liste von **Tagesmodellen** ausgewählt, die Du in einem **Wochenmodell** festlegst. Die Optimierung wird durch den **Typ** eingeschränkt, den Du im Planungsmodell angibst - *flexible Rotation*, *feste Rotation*, usw.

{{ 2 | image: 'Planungsmodell mit Rotation für Früh-/Mittel- und Spät-Schichten', '50%' }}

## Unbeliebte Schichten: Ausnahmetage

Wenn Du unbeliebte Schichten oder Aufgaben nicht für eine gesamte Woche verteilen, sondern beispielsweise lediglich einmal pro Woche planen möchtest, kannst Du *Planungsmodelle*{:.menu-item} mit **Ausnahmetagen** einsetzen.

{{ 3 | image: 'Wochenmodell für Ausnahmetage', '50%' }}

1. Erstelle ein *Wochenmodell*{:.menu-item} mit Deinen normalen Schichten.
2. Gib im Wochenmodell einen Wert von 1 oder mehr für **Maximale Anzahl von Ausnahmetagen pro Woche** ein. 
3. Erstelle ein zweites *Wochenmodell*{:.menu-item}, das die unbeliebten Schichten enthält. 
4. Füge einem Planungsmodell das Wochenmodell mit Deinen Standardschichten hinzu.
5. Wähle das Wochenmodell mit den unbeliebten Schichten im Dropdown-Menü **Wochenmodell für Ausnahmetage** aus.

## Gerechteres Schichtwunsch-Verfahren

Kurzfristig kann es im Schichtwunsch-Verfahren vorkommen, dass ein Mitarbeiter nicht die gewünschten Schichten bekommt. Für mehr Fairness kannst Du bestimmten Auswahlen den Vorzug geben. So wird sich langfristig eine faire Verlosung einstellen, welche durch das reine Zufallsprinzip eventuell nicht gegeben wäre. 

Ordne dazu die Mitarbeiter verschiedenen Auswahlen zu und rotiere in jeder Planung die Auswahl, für die Du zuerst Schichten verlost.

Beispiel: 
- Im Juni wünscht erst Auswahl A, gefolgt von B und schließlich C.
- Im Juli wünscht erst Auswahl B, gefolgt von C und schließlich A.
- Im August wünscht erst Auswahl C, gefolgt von A und schließlich B.
- Usw.
