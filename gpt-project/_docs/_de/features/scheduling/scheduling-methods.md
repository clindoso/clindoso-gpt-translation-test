---
title: Planungsmethoden
promote-service: new-planner-training
description: Erfahre, welche verschiedenen Planungsmethoden es in injixo gibt.
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

In injixo gibt es verschiedene Planungsmethoden, die du entweder einzeln oder {% link_new in Kombination| features/scheduling/combined-scheduling-methods.md %} verwenden kannst.

Die verschiedenen Planungsmethoden decken unterschiedliche Anwendungsfälle ab. Alle Planungsmethoden richten sich nach den Informationen, die in den {% link_new Verträgen| features/administration/create-contracts.md %} deiner Mitarbeiter konfiguriert sind, sowie nach der Anzahl der Arbeitstage, der Arbeitsstunden pro Tag, Woche oder Monat und weiteren Planungsparametern.

## Voraussetzungen

Stelle vor der Verwendung von Planungsmethoden sicher, dass du folgende Konfigurationselemente unter _Plan > Konfiguration_{:.breadcrumbs} erstellt hast:

- Qualifikationen
- Aktivitäten
- Tagesmodelle
- Planungseinheiten
- Verträge
- Mitarbeiter

Je nach Planungsmethode können weitere Konfigurationselemente erforderlich sein, z.&nbsp;B. Schichtfolgen oder Planungsmodelle.

## Fixe Planung

Die fixe Planung basiert auf {% link_new Schichtfolgen| features/administration/shift-sequences.md %}. Eine Schichtfolge ist ein wöchentlich wiederkehrendes Muster von Tagesmodellen oder Aktivitäten. Sie legt die Tage fest, an denen ein Mitarbeiter arbeitet und die genauen Start- und Endzeiten der Schicht. Die fixe Planung bietet dadurch die höchste Beständigkeit, ist aber gleichzeitig auch die unflexibelste Planungsmethode.

Die mit Schichtfolgen erstellten Schichtpläne können jede Woche gleich sein oder in Intervallen von 2 bis 53 Wochen wechseln.

Nachdem der Schichtplan erstellt wurde, kannst du immer noch {% link_new Pausen optimieren| features/scheduling/schedules/break-optimization.md %} oder die {% link_new Joboptimierung| features/scheduling/schedules/schedules-job-optimization.md %} ausführen, um deinen Schichtplan weiter zu optimieren.

**Pausen optimieren** verschiebt geplante Pausen in den Zeitraum, in dem sie den geringsten Einfluss auf deine Deckung haben. injixo kann Pausen nur verschieben, wenn sie innerhalb eines {% link_new Korridors in einem Tagesmodell | features/administration/daymodels/daymodel-basics.md | #feste-elemente-vs-korridore %} konfiguriert wurden.

**Joboptimierung** kann Aktivitäten mit anderen planbaren Aktivitäten ersetzen, wenn sie als ersetzbar konfiguriert wurden. Dies sorgt für die bestmögliche Deckung für alle Aktivitäten auf Grundlage ihres jeweiligen Mitarbeiterbedarfs. Die Zeiten für Schichtbeginn und -ende bleiben dabei unverändert. **Joboptimierung** kann genau wie **Pausen optimieren** Pausenzeiten innerhalb eines Schichtplans verschieben.

## Optimierte Planung

Die optimierte Planung bietet die meiste Flexibilität. Bei dieser Planungsmethode verwendest du die Funktionalität {% link_new Optimierten Plan erstellen| features/scheduling/schedules/schedules-optimized-schedules.md %}, um automatisch einen vollständigen Schichtplan zu erstellen. injixo sorgt für die bestmögliche Deckung für alle Aktivitäten mit so wenigen Mitarbeitern wie möglich.

Standardmäßig kann die Funktionalität **Optimierten Plan erstellen** Mitarbeiter mit jedem beliebigen {% link_new Tagesmodell| features/administration/daymodels/daymodel-basics.md %} planen, das der Planungseinheit der Mitarbeiter zugewiesen ist und zu ihren Verträgen passt. 

Je nach Konfiguration kann die Verwendung verschiedener Tagesmodelle bei der Schichtplanung zu unbeständigen Schichtplänen führen. Beispielsweise könnten dadurch Mitarbeiter für eine Nachtschicht am Montag, eine Nachmittagsschicht am Dienstag und eine Morgenschicht am Mittwoch geplant werden.

Um einzugrenzen, welche Tagesmodelle bei der Schichtplanung verwendet werden dürfen, konfiguriere {% link_new Planungsmodelle | features/administration/work-time-pattern-models.md %}. Ein Planungsmodell besteht aus {% link_new Wochenmodellen | features/administration/work-time-pattern-models.md | #wochenmodelle-erstellen %} und legt fest, wie deinen Mitarbeitern Tagesmodelle zugewiesen werden. Mit Planungsmodellen kannst du wiederkehrende Schichtmuster anlegen und Einschränkungen für die Funktionalität **Optimierten Plan erstellen** festlegen.

Um Mitarbeiter mit Planungsmodellen zu planen, weise jedem Mitarbeiter ein Planungsmodell zu. Du kannst einem Mitarbeiter nicht mehrere Planungsmodelle mit demselben Gültigkeitszeitraum zuweisen.

### Vollständig flexible Schichten

Um Schichtpläne mit vollständig flexiblen Schichten zu erstellen, erstelle Planungsmodelle vom {% link_new Typ A | features/administration/work-time-pattern-models.md | #planungsmodelltypen %} und weise sie deinen Mitarbeitern zu.

Mit Typ A kann injixo aus dem Planungsmodell jedes Tagesmodell für jeden Tag in jeder Woche auswählen, solange es mit dem Vertrag des Mitarbeiters übereinstimmt.

Auf diese Weise erhältst du die besten Schichtpläne, um die Anforderungen deines Unternehmens zu erfüllen. Gleichzeitig können dadurch aber sehr unbeständige Schichtpläne erstellt werden, die sich negativ auf deine Mitarbeiter auswirken. Um die negativen Auswirkungen gering zu halten, kannst du für manche Mitarbeiter bestimmte Schichten ausschließen, indem du ihnen individuelle Tagesmodelle zuweist oder [Verfügbarkeiten](#verfügbarkeiten) verwendest.

### Rotierende flexible Schichten

Um Schichtpläne mit rotierenden flexiblen Schichten zu erstellen, erstelle Planungsmodelle vom {% link_new Typ B, C oder D | features/administration/work-time-pattern-models.md | #planungsmodelltypen %} und weise sie deinen Mitarbeitern zu.

Mit den Typen B, C und D legst du eine bestimmte Reihenfolge fest. An diese hält sich injixo bei der Auswahl der verfügbaren Tagesmodelle aus dem ausgewählten Planungsmodell und sofern sie mit den Verträgen der Mitarbeiter übereinstimmen. Außerdem kannst du eine feste Startzeit für die Schichten oder einen Zeitraum bestimmen, innerhalb dessen Schichten beginnen sollen.

### Verfügbarkeiten

Mit {% link_new Verfügbarkeiten| features/administration/availabilities.md %} kannst du konfigurieren, dass Mitarbeiter an einem bestimmten Tag oder während festgelegter Zeiten nicht verfügbar sind. Zu den durch Verträge und die Öffnungszeiten der Planungseinheit bereits festgelegten Einschränkungen kommen durch Verfügbarkeiten weitere hinzu.

Wenn Mitarbeitern Verfügbarkeiten zugewiesen sind, können sie nur für Schichten geplant werden, die zu dem Zeitraum ihrer Verfügbarkeiten passen.

## Schichtwunsch-Verfahren

Wenn du mit dem {% link_new Schichtwunsch-Verfahren| features/scheduling/schedules/schedules-shift-bidding.md %} arbeitest, wird der endgültige Schichtplan erst erstellt, wenn die Mitarbeiter Gelegenheit hatten, in injixo Me Wünsche für die von ihnen bevorzugten Schichten abzugeben.

Um einen Schichtplan mit dem Schichtwunsch-Verfahren zu erstellen, gehe wie folgt vor:

1. Lege fest, wie viele Schichten du für eine {% link_new Planperiode| features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} benötigst.
2. {% link_new Erzeuge Schichten | features/scheduling/schedules/schedules-shift-bidding.md | #schichten-erzeugen %} auf Basis des prognostizierten Mitarbeiterbedarfs.
3. Setze den Status deiner Planperiode auf **Veröffentlicht**. Mitarbeiter können pro Tag zwei Wünsche abgeben (insgesamt maximal zehn).
4. Starte die {% link_new Verlosung | features/scheduling/shift-bidding.md | #verlosung-gewünschter-schichten %} für Schichten, auf die Wünsche abgegeben wurden.
5. Teile die restlichen Schichten zu. Mitarbeiter, deren Wunsch bei der Verlosung nicht erfüllt wurde, werden in diesem Schritt geplant.

Nachdem der Schichtplan erstellt wurde, kannst du immer noch die {% link_new Joboptimierung| features/scheduling/schedules/schedules-job-optimization.md %} ausführen, um die geplanten Aktivitäten und die Position der Pausen zu optimieren.

> Verwende die Aktivität Anwesend, wenn du Schichtwunsch-Verfahren und **Joboptimierung** kombinierst
>
> Wenn Mitarbeiter in injixo Me Wünsche auf Schichten abgeben können, aber du danach die **Joboptimierung** verwenden möchtest, verwende in den Tagesmodellen nur die Standard-Systemaktivität Anwesend (Aktivitätskennung: 1). So verhinderst du, dass Mitarbeiter sich zunächst Schichten mit bestimmten Aktivitäten wünschen, ihnen dann aber durch die **Joboptimierung** ganz andere Aktivitäten zugewiesen werden.