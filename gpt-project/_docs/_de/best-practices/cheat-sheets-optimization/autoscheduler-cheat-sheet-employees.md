---
title: Einstellungen für Mitarbeiter
---

Hier stellen wir Dir einige Dinge zu Mitarbeitern vor, die sehr nützlich für die Planung mit der volloptimierten Planung (AutoScheduler) sind.

## Betriebszugehörigkeit

Der AutoScheduler plant generell nur aktive Mitarbeiter, d.&nbsp;h. Mitarbeiter mit einer gültigen Betriebszugehörigkeit, einem gültigen Vertrag und gesetztem Häkchen für die Schichtzuteilung.

Einem Mitarbeiter können mehrere Zeiträume für die _Betriebszugehörigkeit_ zugewiesen werden, so dass bspw. auch studentische Aushilfen oder saisonale Arbeitskräfte disponiert werden können.

{{ 1 | image: 'Betriebszugehörigkeit', '75%' }}

Dabei können Planungsfehler auftreten, die manuell korrigiert werden müssen, falls der Mitarbeiter in der Planungswoche nur anteilig zur Verfügung steht.
Der AutoScheduler berücksichtigt immer die Betriebszugehörigkeit des Mitarbeiters – unabhängig vom Status der Planungsregel _2609_{:.id-label} _Prüfung der Betriebszugehörigkeit_.

## Planungssperren

Auch an eine hinterlegte _Planungssperre_ muss sich der AutoScheduler zwingend halten, selbst dann, wenn die Prüfung der Planungsregel _2608_{:.id-label} _Planungssperre_ deaktiviert wurde. Planungssperren werden für längere Abwesenheiten wie Elternzeit, Haftstrafe oder Sabbatjahr hinterlegt. Bei Mitarbeitern in Kur oder Langzeitkranken wird in der Regel mit ganztägigen Aktivitäten gearbeitet.

{{ 2 | image: 'Planungsssperre', '75%' }}

## Verträge

Jeder Mitarbeiter benötigt einen gültigen _Vertrag_, um von injixo – unabhängig vom Planungsansatz – geplant zu werden. Pro Tag kann dem Mitarbeiter immer nur ein Vertrag zugewiesen werden. Sollte es zu einem Vertragswechsel innerhalb der Woche kommen, können im Wochenmodus des AutoScheduler unter Umständen Planungsfehler auftreten.

{{ 3 | image: 'Vertrag', '75%' }}

Der {% link_new AutoScheduler-Spickzettel – Verträge | features/administration/create-contracts.md %} enthält weitere Hinweise zu Vertragsparametern, die für den AutoScheduler relevant sind. Die Definition der Vertragsparameter ist besonders fehleranfällig, daher sollte darauf geachtet werden, welche Vorgaben für die Optimierung mit dem AutoScheduler hinterlegt werden müssen.

## Verfügbarkeiten

Falls Mitarbeiter während der gesamten Öffnungszeiten der Planungseinheit uneingeschränkt zur Verfügung stehen, müssen keine _Verfügbarkeiten_ hinterlegt werden. Sowie ein Mitarbeiter lediglich zu bestimmten Zeiten eingesetzt werden kann, können Verfügbarkeiten, für die Tagestypen, an denen die Einschränkung gilt, in den Stammdaten hinterlegt werden.

Alternierende Verfügbarkeiten werden mittels einer Schichtfolge, die Tagesmodelle vom Typ Verfügbarkeitsrahmen beinhaltet, oder direkt in der Ebene _Verfügbarkeit_ im Schicht Center vergeben.

{{ 4 | image: 'Verfügbarkeiten', '75%' }}

Sollte ein Mitarbeiter an einem bestimmten Wochentag nicht verfügbar sein, kann für diesen Tagestypen eine Verfügbarkeit von bspw. 07:00 Uhr bis 07:01 Uhr hinterlegt werden. Der Mitarbeiter steht also nur noch für eine Minute zur Verfügung und um ihn zu planen, muss der AutoScheduler eine Schicht finden, deren Bruttoschichtdauer kleiner oder gleich der Länge der Verfügbarkeit des Mitarbeiters ist.

Die Verfügbarkeit der Mitarbeiter ist für den AutoScheduler bindend – unabhängig vom Status der Planungsregel _2611_{:.id-label} _Verfügbarkeit des Mitarbeiters_.

## Qualifikationen

Der AutoScheduler prüft immer die erforderlichen Qualifikationen zum Ausführen einer Aktivität, unabhängig vom Status der Planungsregel _2605_{:.id-label} _Qualifikation der Mitarbeiter_. Mitarbeiter müssen eine Qualifikationsstufe für alle Aktivitäten eines Tagesmodells haben, um eine Schicht zu erhalten. Um für eine Multiaktivität geplant werden zu können, müssen Mitarbeiter mindestens für eine Teilaktivität qualifiziert sein.

Wenn es Qualifikationsstufen niedriger 100% gibt, konfiguriere die Einstellung _48069_{:.id-label} _Prozentwert der Eignung für Aktivitäten beachten_.

{{ 5 | image: 'Qualifikationsstufen', '75%' }}

## Planungseinheiten

Der AutoScheduler plant Mitarbeiter nur in der Planungseinheit, die dem Mitarbeiter mit höchster Priorität zugeordnet ist, unabhängig vom Status der Planungsregel _2607_{:.id-label} _Mitarbeiterzuordnung zu den Planungseinheiten_.

Bei Arbeitszeitberechnungen werden die Feiertage und Öffnungszeiten der primären, d.&nbsp;h., der Planungseinheit mit der höchsten Priorität zugrunde gelegt. Dies gilt auch bei der Arbeit mit virtuellen Planungseinheiten. Virtuellen Planungseinheiten dürfen Mitarbeitern in den Stammdaten nicht zugeordnet werden.

{{ 6 | image: 'Planungseinheiten', '75%' }}

Der beim Mitarbeiter hinterlegte _Planungskalender_ ist ausschließlich für die Zeitwirtschaft relevant. Spezielle Feiertage, die in diesem Planungskalender hinterlegt wurden, werden vom AutoScheduler ignoriert. Für die Planung eines Mitarbeiters (mit dem AutoScheduler) gilt standardmäßig der Planungskalender seiner höchstpriorisierten Planungseinheit.

Die Überschneidung von Schichten, die der Mitarbeiter in verschiedenen Planungseinheiten erhält, wird durch die Planungsregel _2612_{:.id-label} _Überschneidung von Aktivitäten/Schichten der Mitarbeiter in mehreren Planungseinheiten_ geprüft.

Ist für einen Mitarbeiter in einer Planungseinheit mit niedrigerer Priorität bereits eine Schicht oder Aktivität eingetragen, so wird dieser Buchungstag von der Optimierung mit dem AutoScheduler vollständig ausgeschlossen.

## Tagesmodelle

Wenn es für den Mitarbeiter eine explizite Tagesmodell-Zuordnung gibt, ist der AutoScheduler daran gebunden und darf ausschließlich die zugewiesenen _Tagesmodelle_ verwenden – unabhängig vom Status der Planungsregel _2661_{:.id-label} _Tagesmodellzuordnung zum Mitarbeiter_.

**Bitte unbedingt beachten**: Werden später weitere Tagesmodelle benötigt, müssen diese wieder explizit zugeordnet werden, da der AutoScheduler ausschließlich die hier beschriebene Tagesmodellzuordnung zum Mitarbeiter nutzt, wenn dem Mitarbeiter (mindestens) ein Tagesmodell in seinen Stammdaten zugewiesen wurde. Ist dem Mitarbeiter zusätzlich ein Planungsmodell zugeordnet, kann der AutoScheduler nur die Tagesmodelle aus den entsprechenden Wochenmodellen verwenden, die dem Mitarbeiter auch explizit zugewiesen wurden.

{{ 7 | image: 'Tagesmodelle', '75%' }}

## Schichtfolgen

Wenn dem Mitarbeiter in seinem Stammdatenblatt eine _Schichtfolge_ zugeordnet ist, die nicht über den Planungsschritt Schichtfolgen einfügen ins Schicht Center übertragen wurde, wird diese Zuordnung vom AutoScheduler ignoriert und der Mitarbeiter wird unter Berücksichtigung sonstiger Stammdaten und Planungsregeln durch den AutoScheduler flexibel geplant.

So kann es vorkommen, dass eine Teilzeitkraft, die gemäß Schichtfolge nur montags bis mittwochs von jeweils 08:00 Uhr bis 12:00 Uhr planbar ist, vom AutoScheduler nachmittags von Freitag bis Sonntag eingesetzt wird.

{{ 8 | image: 'Schichtfolgen', '75%' }}

Wurde die Schichtfolge über den Menüpunkt Schichtfolge einfügen im Schicht Center hinterlegt, kann der AutoScheduler die Aktivitätsblöcke optimieren. Inwieweit dem Mitarbeiter zusätzliche Arbeitszeit zugewiesen werden kann, ist von den Vertragsparametern sowie dem Wert der Einstellung _48309_{:.id-label} _Bestehende Aktivitäten berücksichtigen_ abhängig.

## Planungsmodelle

Wenn dem Mitarbeiter ein _Planungsmodell_ zugewiesen wurde, greift der AutoScheduler ausschließlich auf die Tagesmodelle innerhalb der Wochenmodelle dieses Planungsmodells zu. Somit ist der AutoScheduler zwingend daran gebunden und muss immer die darüber definierten Tagesmodelle verwenden – unabhängig vom Wert der Einstellung 48402 Ausschließlich Planungsmodellzuordnungen beachten.

Dabei ist zu beachten, dass sämtliche Tagesmodelle, die über das Planungsmodell für den Mitarbeiter vergeben werden können, explizit der Planungseinheit zugeordnet sein müssen – unabhängig vom gewählten Status der Planungsregel _2651_{:.id-label} _Tagesmodellzuordnung zu Planungseinheiten_.

Da Planungsmodelle ab und an auch Stolperfallen beinhalten, werden die Planungsmodelle separat im {% link_new AutoScheduler-Spickzettel – Planungsmodelle | best-practices/cheat-sheets-optimization/autoscheduler-cheat-sheet-wtpm.md %} erläutert.

{{ 9 | image: 'Planungsmodelle', '75%' }}

## Planungsregeln

Bestimmte Planungsregeln werden vom AutoScheduler immer hart interpretiert, unabhängig davon, wie Du diese unter _WFM > Administration > System > Planungsregeln_{:.breadcrumbs} konfiguriert hast. Weitere Informationen dazu findest Du bei den {% link_new Parametern für die volloptimierte Planung | features/administration/create-contracts.md %}.

## Auswahlen

Ein Mitarbeiter kann einer _Auswahl_ (oder auch mehreren) zugeordnet werden, was für den AutoScheduler keine größere Relevanz besitzt, da der AutoScheduler immer die gesamte Planungseinheit optimiert.

Wenn Du jedoch eine Auswahl selektiert hast, wird das Speichern der Planungsergebnisse auf die Mitarbeiter beschränkt, die dieser Auswahl angehören. Somit werden zwar alle Mitarbeiter durch den AutoScheduler geplant, aber die Schichtpläne werden nur für die Mitglieder der Auswahl geschrieben.

## Weitere Hinweise

Einträge in der Bearbeitungskategorie _Coach/Trainee_ können die Planung mit dem AutoScheduler verhindern. Der AutoScheduler und die Optimierungsprozesse planen keine Trainees. Falls ein Mitarbeiter im Optimierungszeitraum einem Coach als Trainee zugeordnet ist, wird er von der Optimierung ausgeschlossen. Daher ist darauf zu achten, dass keine Zuordnung als Trainee besteht, wenn ein Mitarbeiter automatisiert geplant werden soll.
