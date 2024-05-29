---
title: Was ist injixo Forecast?
redirect_from:
  - /de/forecast_overview/
  - /de/general-functionality/
redirect_reason: redirect for intercom forecast tour, 2nd link, renamed article in june 2021
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Verwende injixo Forecast, um automatisch das zu erwartende Kontaktvolumen und die AHT zu ermitteln.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manual-adjustments.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/save-forecast-versions.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/download-forecast.md
---

injixo Forecast verknüpft deine historischen Daten mit Algorithmen, um daraus qualitativ hochwertige Forecasts zu erstellen. Die Algorithmen erkennen Trends, Muster und Schwankungen in deinen Daten. injixo Forecast verwendet viele verschiedene Arten von Algorithmen wie ARIMA, Holt-Winters, exponentielle Glättung, Regression oder Gradient Boosting.

injixo Forecast wählt automatisch den Algorithmus aus, der am besten zu deinen Daten passt. injixo erzeugt einen Forecast für 365 Tage nach dem Datenimport.

injixo Essential WFM verwendet einen einfachen Algorithmus, der einfache Durchschnittswerte in den historischen Daten verwendet, um einen langfristigen linearen Trend und wöchentliche Muster zu erkennen.

## Forecast erstellen

Sieh dir unseren Schnelleinstieg an, um zu erfahren, wie du {% link_new einen Forecast erstellst | getting-started/calculate-a-forecast.md %}. Mit jedem neuen Datenimport wird der erzeugte Forecast aktualisiert. In injixo Essential WFM wird einmal pro Woche ein neuer Forecast erzeugt.

Hinweis: Wenn dein Forecast nur wiederkehrende Wochenverläufe anzeigt, kann es sich dabei trotzdem um den optimalen Forecast handeln. In diesem Fall erfasst der Algorithmus kurzfristige Muster (für sich nicht wiederholende Schwankungen) und stuft langfristige Muster als nicht relevant ein. Schwankungen in den historischen Daten sind nicht immer Muster.

## Erforderliche Daten

injixo Forecast benötigt importierte eingehende Kontakte, durchschnittliche Bearbeitungszeit (AHT) und bearbeitete Kontakte.

Basic Workloads in injixo Classic benötigen historische Daten von mindestens zwei Wochen. Smart Workloads können einen Forecast mit historischen Daten von nur einem Tag erstellen. Bei Daten von zwei oder mehr Jahren berücksichtigen Smart Workloads monatliche und jährliche Schwankungen, wie z.&nbsp;B. Saisongeschäft.

Welche Workloads du nutzen kannst, hängt von deinem WFM-Plan ab (Classic, Essential, Advanced oder Enterprise WFM).

## Wie du mit geringer Datenqualität umgehst

Um einen genauen Forecast zu erstellen, müssen die historischen Daten sowohl vollständig (ausreichend große Datenmenge mit möglichst wenig Lücken) als auch bereinigt sein (enthalten keine irrelevanten Muster). Falsch ausgezeichnete {% link_new Ereignisse oder Feiertage | features/forecast/injixo-forecast/events-and-holidays.md %} wirken sich beispielsweise negativ auf die Forecast-Qualität aus.

Historische Daten können längere Ausfallzeiten enthalten oder es fehlen Daten für einen bestimmten Zeitraum. Je näher diese fehlenden Daten am aktuellen Tag liegen, desto geringer ist die Auswirkung auf die Forecast-Qualität.

Im folgenden findest du ein paar Tipps, um mit geringer Datenqualität umzugehen, je nachdem wie lange der Zeitraum mit minderwertigen oder fehlenden Daten ist:

| Zeitraum mit geringer Datenqualität | Tipp                                                                                           |
| ----------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ein paar Tage                       | Verwende {% link_new Ereignisse                                                                | features/forecast/injixo-forecast/events-and-holidays.md %}, um die betroffenen Tage als Störung zu kennzeichnen und sie von der Berechnung auszuschließen. |
| Ein paar Wochen                     | Lade weitere Daten ohne Datenlücken oder irrelevante Muster hoch.                              |
| Mehrere Wochen oder Monate          | Entferne die Daten, die vor der Lücke liegen. Importiere nur Daten, die nach der Lücke liegen. |

Hinweis: Falls du keine weiteren Daten hochladen kannst oder die Daten nach einer Lücke nicht ausreichend sind, versuchen die Algorithmen des Smart Forecast automatisch, die negativen Auswirkungen der fehlenden Daten so gering wie möglich zu halten.

> Prüfe und bereinige deine Daten vor dem Import
>
> Du kannst keine historische Daten entfernen. Wende dich bei Bedarf an dein Customer Success Team.

## Niedrige Volumen prognostizieren

injixo Forecast kann Forecasts für niedrige und hohe Kontaktvolumen erstellen. Wenn du einen Forecast auf Grundlage von Daten mit niedrigem Kontaktvolumen erstellst, erkennt injixo möglicherweise die täglichen Muster nicht. In seltenen Fällen kann dies dazu führen, dass für bestimmte Tage gar kein Forecast erstellt wird. Für einzelne Tage kannst du den Forecast manuell anpassen. Wenn die Situation häufiger auftritt, kannst du:

- Mehrere Queues zum Workload hinzufügen (was zu einem höheren Volumen führt).
- Einen anderen Ansatz verwenden, um Mitarbeiterbedarf für die Planung zu erzeugen, z.&nbsp;B. indem du {% link_new konstanten Bedarf erzeugst | features/forecast/requirement-scripts/requirement-constant.md %}.
