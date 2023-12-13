---
title: Zeitzonen verstehen und nutzen
description: Lerne, wie sich Zeitzonen auf die Anzeige von Daten auswirken und wie Du eine für Dich passende Benutzer-Zeitzone einstellst.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /de/best-practice-timezones/
---

In diesem Artikel lernst Du:
* wie Zeitzonen in injixo funktionieren.
* wie Du Deine Benutzer-Zeitzone einstellst.
* wie die Einstellung Deiner Benutzer-Zeitzone und der Zeitzonen von Planungseinheiten, Queues und Workloads die Anzeige von Daten in injixo beeinflusst.

## Zeitzonen in injixo

injixo unterstützt die Schichtplanung über mehrere Zeitzonen hinweg.

Jede {% link_new Planungseinheit | features/administration/create-and-manage-planning-units.md %}, {% link_new Queue | features/forecast/forecastpro/administration/queues.md %} und jeder {% link_new Workload | features/forecast/injixo-forecast/manage-workloads.md %} hat eine Zeitzone, die Du beim Erstellen des Elements festlegst. Du kannst die Zeitzone nicht nachträglich ändern. Wenn Du sie ändern musst, musst Du das Element neu erstellen.

Die Kombination aus den Zeitzonen der Elemente sowie der für Dein Benutzerkonto eingestellten Zeitzone entscheidet darüber, wie injixo die Daten in den verschiedenen Modulen anzeigt.

## Deine Benutzer-Zeitzone einstellen

Deine Benutzer-Zeitzone steuert, wie die Daten in Modulen wie dem Schicht Center, Schedules und Dashboards angezeigt werden. Ändere Deine Benutzer-Zeitzone, um Daten aus der Sicht einer beliebigen Zeitzone anzuzeigen:

1. Klicke auf Deinen **Benutzernamen** in der oberen rechten Ecke.
2. Wähle eine **Zeitzone** aus.
3. Klicke auf *Profil speichern*{:.doc-button}.

Wenn Du ein injixo-Modul erneut aufrufst, verschieben sich die Daten entsprechend Deiner neuen Benutzer-Zeitzone.

Beispiel: Dein Contact Center ist in New York, aber Du arbeitest in Berlin. Stelle Deine Benutzer-Zeitzone auf Berliner Zeit ein und die Zeitzone der Planungseinheit auf New Yorker Zeit, um Schichtpläne in Deiner Ortszeit zu sehen. Ändere Deine Benutzer-Zeitzone auf New Yorker Zeit, um Schichtpläne in der Ortszeit des entfernten Standorts zu sehen, in diesem Fall New Yorker Zeit.

## Welche Zeitzone wird von welchem Modul verwendet?

Einige injixo-Module verwenden zur Anzeige von Daten die Benutzer-Zeitzone, andere die Zeitzone, die für die Planungseinheit oder den Workload definiert wurde. Manche Module zeigen auch den Zeitversatz zwischen der Benutzer-Zeitzone und der Zeitzone der Planungseinheit oder des Workloads an. Erfahre, welche Zeitzone in welchen Modulen verwendet wird und wo sie angezeigt wird.

### Schicht Center

Die beiden Hauptbereiche des Schicht Centers - das Planfenster und das Kennzahlenfenster - zeigen Daten in der Benutzer-Zeitzone an. Wenn es einen Zeitversatz zwischen der Benutzer-Zeitzone und der Zeitzone der Planungseinheit gibt, wird dieser in eckigen Klammern neben dem Namen der Planungseinheit angezeigt.

{{ 3 | image: "Zeiten im Planfenster - Schicht Center - Lokale Benutzerzeit", '90%' }}

Wenn Du einen Tag bearbeitest, werden die Daten während der Bearbeitung in der Zeitzone der Planungseinheit angezeigt.

{{ 4 | image: "Zeiten im Bearbeitungsmenü - Zeitzone der Planungseinheit", '80%' }}

### Schedules

Das Modul Schedules unter *Plan > Schedules*{:.breadcrumbs} zeigt Daten in der Zeitzone des Benutzers an. Wenn es einen Zeitversatz zwischen der Zeitzone des Benutzers und der Planungseinheit gibt, wird dieser neben dem Namen der Planungseinheit angezeigt.

{{ 11 | image: "Schedules Zeitversatz", '80%' }}

Wenn Du einen Tag bearbeitest, werden die Daten während der Bearbeitung in der Zeitzone der Planungseinheit angezeigt.

### Dashboards

Das Modul Dashboards unter *Analyze > Dashboards*{:.breadcrumbs} zeigt die Daten in der Benutzer-Zeitzone an. Die aktuelle Benutzer-Zeitzone steht in der unteren rechten Ecke.

Wenn Du in den Bearbeitungsmodus wechselst, indem Du auf _![Kontextmenü](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} und dann auf **Bearbeiten** klickst, öffnet sich der Navigator auf der linken Seite. Rechts neben den Elementen im Navigator wird die Zeitzone der jeweiligen Planungseinheit oder des Workloads angezeigt.

{{ 12 | image: "Dashboards-Baumstruktur im Navigator", '80%' }}

### injixo Me

injixo Me zeigt Zeiten für Schichten und Aktivitäten in der Benutzer-Zeitzone an.

### Reports

Die Reports, die Du mit dem Modul Reports unter *WFM > Controlling > Reports*{:.breadcrumbs} erstellst, zeigen Daten in der Zeitzone der Planungseinheit an. Im oberen Bereich eines Reports wird auch der Zeitversatz zwischen der Zeitzone der Planungseinheit und der Benutzer-Zeitzone angezeigt.

{{ 7 | image: "Zeitzone der Planungseinheit und Zeitversatz zur Benutzer-Zeitzone", '60%' }}

### injixo Forecast

Das Modul injixo Forecast unter *Forecast*{:.breadcrumbs} zeigt Daten in der für den Workload eingestellten Zeitzone an. Die Zeitzone des Workloads wird rechts neben dem Namen des Workloads im Dropdown-Menü eingeblendet.

{{ 8 | image: "Workload mit Zeitzone in Auswahlliste", '100%' }}

Wenn Du Queues mit unterschiedlichen Zeitzonen in einem Workload kombinierst, passt injixo Forecast die Daten an die im Workload ausgewählte Zeitzone an.

### Bedarfsberechnungsfenster

Wenn Du den Mitarbeiterbedarf für einen Workload berechnest, kannst Du die Berechnungsmethode *Andere* auswählen, um spezielle Bedarfsberechnungsskripte zu nutzen. Folge den Anweisungen im Artikel {% link_new Mitarbeiterbedarf berechnen | features/forecast/injixo-forecast/staff-requirement.md | #die-berechnungsmethode-andere-einrichten %}, um das jeweilige Skript-Fenster zu öffnen. Dort werden Dir die Zeitzonen der Queue und der Planungseinheit angezeigt.

Der Mitarbeiterbedarf wird in der Zeitzone der Planungseinheit berechnet. Die Berechnung berücksichtigt den Zeitversatz zwischen Queue und Planungseinheit.

{{ 10 | image: "Fenster zur Berechnung des Mitarbeiterbedarfs", '65%' }}
