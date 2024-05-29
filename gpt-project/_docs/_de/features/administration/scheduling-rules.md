---
title: Planungsregeln
---

In diesem Artikel lernst Du:

- wofür Du Planungsregeln benötigst.
- wie Du den Status der Regeln anpasst.
- wie Planungsregeln und Verträge zusammenhängen.

Die Planungsregeln (im Weiteren auch als Regeln bezeichnet) definieren Vorgaben für den Planungsprozess.

Jede Regel ist durch eine eindeutige vier-stellige ID gekennzeichnet, z.B. 2611, 2614 oder 2648. Du findest diese ID auch in anderen Modulen von injixo wieder, z.B. in Verträge oder Ergebnisreports von Optimierungen, wenn ein Verstoß gegen diese Regel aufgetreten ist.

Manche Regeln sind nur nutzbar, wenn Du injixo Enterprise Cloud oder injixo Enterprise on-premise nutzt.

Um mehr Informationen über eine Regel zu erhalten, wähle sie in _WFM > Administration > System > Planungsregeln_{:.breadcrumbs} aus:

{{ 1 | image: 'Regelübersicht' }}

## Arten von Planungsregeln

Es gibt zwei unterschiedliche Arten von Planungsregeln: allgemeine und vertragsbezogene Regeln.

### Allgemeine Planungsregeln

Allgemeine Planungsregeln gelten immer und werden unabhängig vom Vertrag definiert.

Beispiele:

_2605_{:.id-label} _Qualifikation der Mitarbeiter_  
_2611_{:.id-label} _Verfügbarkeit des Mitarbeiters_  
_2648_{:.id-label} _Schreibschutz für Aktivitäten im Schicht Center_  
_2651_{:.id-label} _Tagesmodellzuordnung zu Planungseinheiten_

### Vertragsbezogene Planungsregeln

Die vertragsbezogenen Regeln gelten für jeden Mitarbeiter mit einem gültigen Vertrag und werden anhand der Parameterwerte im Vertrag definiert; beispielsweise welche Ruhezeiten pro Vertragsgruppe eingehalten werden müssen. In _WFM > Administration > System > Planungsregeln_{:.breadcrumbs} kannst Du für diese Regeln festlegen, ob sie überprüft werden oder nicht.

Beispiele:

_2601_{:.id-label} _Ruhezeit zwischen zwei Buchungstagen gemäß Vertrag_  
_2614_{:.id-label} _Maximale Arbeitszeit/Tag gemäß Vertrag (Tagesmodelle und Aktivitäten)_

## Status der Planungsregeln

Eine Fehlermeldung mit einer vier-stelligen ID verweist immer auf die Verletzung einer Planungsregel. Der Hinweis enthält die Information, welche Regel verletzt und weitere Details zum Regelbruch. Kannst Du jedoch Planungsaktionen durchführen, die nicht erlaubt sein sollten (z. B. kannst Du einer Teilzeitkraft eine zu lange Schicht zuweisen), überprüfe, ob die entsprechende Regel aktiviert ist.

Hierfür gibt es drei unterschiedliche Farbkodierungen, die Dir den Status der Planungsregel anzeigen:

- **Grau**  
  Die Regel ist nicht aktiviert und wird dementsprechend nicht überprüft.

- **Gelb**  
  Die Regel ist auf weich eingestellt, sodass alle Planungsaktionen gegen diese Regel verstoßen können. Du erhältst jedoch einen entsprechenden Hinweis, wenn ein Regelverstoß vorliegt.

- **Rot**  
  Die Regel ist aktiviert. Wenn eine Planungsaktion gegen die Regel verstößt, lässt sich diese nicht ausführen und es wird eine Fehlermeldung mit zusätzlichen Informationen erzeugt.

## Wie kann man den Status der Regeln anpassen?

Benutzer mit _Admin-Zugriff_ können den Status jeder Regel in _WFM > Administration > System > Planungsregeln_{:.breadcrumbs} anpassen sowie Ausnahmen und benutzerspezifische Werte definieren.

{{ 2 | image: 'Status einer Planungsregel', '40%' }}

### Ausnahmen definieren

In den meisten Fällen wirst Du Regeln für alle Benutzer von injixo anpassen, sodass jeder unter den gleichen Voraussetzungen Änderungen am Schichtplan vornehmen kann. Unter bestimmten Bedingungen ist es jedoch sinnvoll, für einzelne Nutzer oder Benutzergruppen Abweichungen bei den Planungsregeln zu definieren. Beispielsweise dürfen Deine Supervisoren gewisse Regeln umgehen, um bestmöglich auf die Herausforderungen in der Tagessteuerung zu reagieren.

- **Standard jeder Nutzer**  
  Dies ist der allgemeine Status einer Regel, welcher standardmäßig überall berücksichtigt wird.

- **Aktueller Nutzer**  
  An dieser Stelle kannst Du Ausnahmen für Deinen eigenen Benutzer erstellen.

- **Benutzer**  
  Als Admin kannst Du für jeden Benutzer den Status der Planungsregeln individuell überprüfen und einstellen.

- **Benutzergruppen**  
  Du kannst Ausnahmen für eine gesamte Benutzergruppe (z.B. Planer oder Supervisor) erstellen.

- **Programmteile**  
  Über die Programmteile legst Du fest, wie die Planungsregel während der Verlosung, Wunschgenehmigung, Optimierung und Zuteilung geprüft werden.
