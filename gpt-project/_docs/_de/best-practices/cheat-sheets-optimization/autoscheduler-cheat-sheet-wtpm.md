---
title: Nur bestimmte Schichten automatisch planen
redirect_from:
  - /de/best-practice-planungsmodelle
---

Mit Planungsmodellen kannst Du auf Wochenbasis verschiedene Planungsvorgaben umsetzen, sodass Du beispielsweise einen rotierenden Schichtwechsel von Früh- und Spätschichten planen kannst.

## Einführung

Planungsmodelle stellen Arbeitsmuster dar, die aus Wochenmodellen (in einer bestimmten Reihenfolge) bestehen, die wiederum aus Tagesmodellen bestehen.

Wenn einem Mitarbeiter ein Planungsmodell zugewiesen wurde, greift der AutoScheduler ausschließlich auf Tagesmodelle innerhalb der Wochenmodelle dieses Planungsmodells zu. Somit ist der AutoScheduler zwingend daran gebunden und muss immer die darüber definierten Tagesmodelle verwenden.

Sämtliche Tagesmodelle, die sich in den Wochenmodellen des Planungsmodells befinden, müssen explizit der Planungseinheit zugeordnet sein, der ein Mitarbeiter, dem dieses Planungsmodell zugewiesen wird, mit höchster Priorität angehört.

## Beispielszenario

Ein Mitarbeiter hat einen 5-Tages-Vertrag mit 20 Stunden Wochensoll und kann täglich ausschließlich für Schichten mit einer Länge von 4 Stunden eingesetzt werden. Kürzere oder längere Schichten sind im Vertrag nicht zugelassen.

Die Planungseinheit ist montags bis sonntags von 06:00 Uhr bis 22:00 Uhr geöffnet und die der Planungseinheit zugeordneten Tagesmodelle vom Typ zeitlich fixierte Schicht beginnen nur zur vollen Stunde.

Somit stehen in der Planungseinheit 13 fixe Tagesmodelle (siehe Spalte `vertragskonforme Tagesmodelle`) zur Verfügung, die die Vertragsparameter erfüllen und dem Mitarbeiter während der Vollständigen Optimierung zugewiesen werden können.

Die nachfolgenden Abbildungen illustrieren die unterschiedlichen Typen von Planungsmodellen anschaulich an einem kleinen Beispiel.

{{ 1 | image: "Tagesmodelle gruppiert in Wochenmodelle", '75%' }}

Da für den Mitarbeiter keine eingeschränkten Verfügbarkeiten gelten, muss der AutoScheduler nur die Ruhezeit zwischen zwei Buchungstagen einhalten und kann dem Mitarbeiter einen Schichtplan zuweisen, wie in der Zeile `kein Planungsmodell` illustriert. Dieser Schichtplan ist vertragskonform, auch wenn der Mitarbeiter nicht unbedingt begeistert sein wird.

Daher können die zur Verfügung stehenden Tagesmodelle mit Hilfe von Wochenmodellen eingeschränkt und gruppiert werden. Im Beispiel wurden die blauen Tagesmodelle außen vor gelassen und die verbleibenden Tagesmodelle in den Wochenmodellen `Früh`, `Mittel` und `Spät` gruppiert. Je nach Typ des Planungsmodells berücksichtigt der AutoScheduler die festgelegte Reihenfolge der Wochenmodelle bei der Schichtauswahl und kann so bspw. in der Spätwoche nur aus den Anfangszeiten 14:00 Uhr bis 16:00 Uhr wählen.

Dem Planungsmodell wurden die Wochenmodelle in der Reihenfolge `Früh`, `Mittel` und `Spät` zugewiesen.

### Planungsmodelltypen

Der Typ des Planungsmodells gibt der volloptimierten Planung (AutoScheduler) die Reihenfolge vor, in der die Wochenmodelle für die Planung verwendet werden sollen. Aus den in den Wochenmodellen enthaltenen Tagesmodellen erzeugt der AutoScheduler für jeden Tag einer Woche die Schichten, die den angegebenen Bedarf für eine bestimmte Aktivität optimal decken.

Wenn dieses Planungsmodell vom Typ A ist, kann der AutoScheduler für jeden Arbeitstag ein beliebiges Tagesmodell aus irgendeinem der drei Wochenmodelle wählen (s. Zeile `Planungsmodell Typ A`).

Ist dieses Planungsmodell vom Typ B, muss der AutoScheduler für jeden Arbeitstag das identische Tagesmodell aus dem gemäß Reihenfolge gültigen Wochenmodell wählen (s. Zeile `Planungsmodell Typ B`).

Wird für dieses Planungsmodell der Typ C hinterlegt, muss der AutoScheduler für jeden Arbeitstag das identische Tagesmodell wählen, kann aber die Reihenfolge der Wochenmodelle dem Bedarf anpassen( s. Zeile `Planungsmodell Typ C`).

Wurde für dieses Planungsmodell der Typ D gewählt, kann der AutoScheduler für jeden Arbeitstag ein beliebiges Tagesmodell aus dem gemäß Reihenfolge gültigen Wochenmodell wählen (s. Zeile `Planungsmodell Typ D`).

{{ 1 | image: 'Beispiel mit verschiedenen Planungsmodellen', '75%' }}

Weitere Informationen zu den unterschiedlichen Planungsmodelltypen findest Du {% link_new hier | features/administration/work-time-pattern-models.md %}.

### Verwendung von Tagesmodellen

Sollten dem Mitarbeiter sowohl Tagesmodelle als auch ein Planungsmodell zugeordnet sein, so kann der AutoScheduler nur die Tagesmodelle aus den entsprechenden Wochenmodellen verwenden

Falls einem Mitarbeiter, für den ein Planungsmodell gilt, in seinen Stammdaten explizit (persönliche) Tagesmodelle zugeordnet wurden, kann der AutoScheduler nur noch auf diese Teilmenge an Tagesmodellen zugreifen.

Werden später weitere Tagesmodelle benötigt und den Wochenmodellen zugewiesen, müssen diese ebenfalls explizit dem Mitarbeiter zugeordnet werden, da der AutoScheduler ausschließlich die Tagesmodellzuordnung zum Mitarbeiter nutzt, sowie dem Mitarbeiter (mindestens) ein Tagesmodell in seinen Stammdaten zugewiesen wurde.

Zusätzliche Tagesmodelle müssen auch der Planungseinheit zugeordnet werden, da Mitarbeiter mit dem betroffenen Planungsmodell sonst von der Optimierung ausgeschlossen werden, da "ein im Planungsmodell enthaltenes Tagesmodell von der ausgewählten Planungseinheit nicht unterstützt wird".

### Ausnahmetage

In Wochenmodellen kann auch eine Anzahl Ausnahmetage festgelegt werden. Der AutoScheduler kann an diesen Tagen und wenn es für die Deckung des Bedarfs erforderlich ist, entweder auf alle Tagesmodelle zugreifen, die den anderen zum Planungsmodell gehörenden Wochenmodellen zugeordnet sind oder ein spezielles Wochenmodell verwenden, das für Ausnahmetage festgelegt wurde.

Dabei gilt: Ausnahmetage sind optional und werden erst während der Optimierung und nicht bereits bei der Basisplanerstellung berücksichtigt. Das heißt, der AutoScheduler muss in der Lage sein, ohne die Verwendung der für Ausnahmetage festgelegten Tagesmodelle, einen Basisplan für den Mitarbeiter zu erstellen. Sollte dies nicht möglich sein, wird der Mitarbeiter von der Optimierung ausgeschlossen.

Falls der AutoScheduler eine Verbesserung des Deckungsergebnisses durch das Ersetzen einzelner Tagesmodelle durch Ausnahmetage erzielen kann, wird auf Ausnahmetage zurückgegriffen. Es besteht aber kein Zwang für den AutoScheduler, die definierte Anzahl an Ausnahmetagen zu verwenden.

{{ 2 | image: 'Planungs- und Wochenmodell in der Administration'}}

Das oben abgebildete Planungsmodell enthält ein Wochenmodell mit zwei variablen Tagesmodellen und ein spezielles Wochenmodell für Ausnahmetage. Darin hinterlegt ist ebenfalls ein variables Tagesmodell.

### Beispiel

Beiden Mitarbeitern in der folgenden Abbildung ist dieses Planungsmodell zugewiesen, jedoch besteht für Yvonne Aschmann noch eine explizite Tagesmodell-Zuordnung. Der AutoScheduler darf dem Mitarbeiter das Tagesmodell im Wochenmodell für die Ausnahmetage nicht zuordnen. Daher werden dem Mitarbeiter keine Ausnahmetage zugewiesen, auch wenn zwei Ausnahmetage gemäß Planungsmodell erlaubt wären.

{{ 3 | image: 'Bildschirmfoto 2017-02-23 um 09.19.13.png'}}
