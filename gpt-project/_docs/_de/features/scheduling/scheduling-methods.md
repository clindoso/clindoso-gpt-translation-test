---
title: Verfügbare Planungsmethoden
promote-service: new-planner-training
description: Lerne die verschiedenen Planungsmethoden in injixo kennen.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/combined-scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

In diesem Artikel lernst Du:
- welche Planungsmethoden es gibt.
- welche Planungsmethode für welchen Anwendungsfall verwendet werden kann.

Du kannst die verschiedenen Planungsmethoden einzeln verwenden oder {% link_new kombinieren | features/scheduling/combined-scheduling-methods.md %}.

Die Planungsmethoden richten sich grundsätzlich nach den {% link_new Verträgen | features/administration/create-contracts.md %}, die den Mitarbeitern zugeordnet sind. Die Verträge enthalten die Anzahl der Arbeitstage, die Arbeitsstunden pro Tag, Woche oder Monat und andere Planungsparameter.

## Fixe Schichtplanung

Die fixe Schichtplanung bietet die geringste Flexibilität. Bei dieser Planungsmethode kommen vordefinierte {% link_new Schichtfolgen | features/administration/shift-sequences.md %} zum Einsatz.

Schichtfolgen definieren:
- die Wochentage, an denen ein Mitarbeiter arbeitet.
- die genaue Anfangs- und Endzeit der Schicht für jeden Arbeitstag.

Die aus diesen Schichtfolgen erstellten Schichtpläne können jede Woche gleich sein oder in Intervallen von 2 bis 53 Wochen wechseln.

Nachdem der Schichtplan erstellt ist, kannst Du die folgenden Elemente optimieren:  
- Positionen der Pausen in {% link_new Korridoren | features/administration/daymodels/daymodel-basics.md | #feste-elemente-vs-korridore %}
- {% link_new ersetzbare Aktivitäten | features/administration/activity-types-and-properties.md | #aktivitätseigenschaften %}

## Volloptimierte Planung

Die volloptimierte Planung bietet die größte Flexibilität. Nutze das *Optimierten Plan erstellen*-Feature, um automatisch einen vollständigen Schichtplan zu erstellen. injixo stellt sicher, dass die verschiedenen Aktivitäten mit der kleinstmöglichen Anzahl von Mitarbeitern bestmöglich abgedeckt sind.

Mit {% link_new Planungsmodellen | features/administration/work-time-pattern-models.md %} kannst Du festlegen, welche Schichten für die Planung zur Verfügung stehen. 

### Vollständig flexible Schichten

Weise Deinen Mitarbeitern für vollständig flexible Schichten Planungsmodelle {% link_new vom Typ A | features/administration/work-time-pattern-models.md | #vier-verschiedene-typen %} zu.  

Jede Schicht, die gemäß des Planungsmodells verfügbar ist und den vertraglichen Konditionen des Mitarbeiters entspricht, kann an jedem beliebigen Tag geplant werden.  

Um die Akzeptanz der Mitarbeiter für die von Dir erstellten Schichtpläne zu erhöhen, kannst Du bestimmte Schichten ausschließen, indem Du den Mitarbeitern persönliche Tagesmodelle hinzufügst oder [Verfügbarkeiten](#verfügbarkeiten] konfigurierst.

### Rotierende flexible Schichten

Weise Deinen Mitarbeitern für die rotierenden flexiblen Schichten Planungsmodelle {% link_new vom Typ B, C oder D | features/administration/work-time-pattern-models.md | #vier-verschiedene-typen %} zu.

Je nach Typ des Planungmodells werden die Schichten, die gemäß des Planungsmodells zur Verfügung stehen und den vertraglichen Konditionen des Mitarbeiters entsprechen, in einer bestimmten Reihenfolge geplant. Diese können sogar jeden Tag die gleiche Startzeit haben.

### Verfügbarkeiten

Verfügbarkeiten können die volloptimierte Planung ergänzen, um die Schichtoptionen einzuschränken. Erfahre mehr über {% link_new Verfügbarkeiten | features/administration/availabilities.md %}.

## Schichtwunsch-Verfahren

Beim {% link_new Schichtwunsch-Verfahren | features/scheduling/schedules/schedules-shift-bidding.md %} wird der finale Schichtplan erst nach Beteiligung Deiner Mitarbeiter erstellt. Sie können sich vorab im Mitarbeiterportal präferierte Schichten wünschen.

Der Workflow in Kürze:

1. Lege fest, wie viele Schichten Du benötigst.
2. Erzeuge Schichten auf der Basis des prognostizierten Mitarbeiterbedarfs.
3. Setze den Status Deiner Planperiode auf *Veröffentlicht*.
4. Deine Mitarbeiter können pro Tag zwei Wünsche abgeben (insgesamt maximal zehn).
5. Verlose die gewünschten Schichten.
6. Teile die restlichen Schichten zu. Mitarbeiter, deren Wunsch bei der Verlosung nicht erfüllt wurde, werden in diesem Schritt geplant.
