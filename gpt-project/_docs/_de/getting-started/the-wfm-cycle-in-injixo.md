---
title: Der WFM-Kreislauf in injixo
description: Erfahre, wie du den WFM-Kreislauf mit injixo meistern kannst.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /de/wfm-cycle/
redirect_reason: Updated filename on 27 July 2023
---

Workforce Management (WFM) zielt darauf ab, Mitarbeiter optimal einzusetzen, um angestrebte Geschäftsziele und Service-Level zu erreichen. injixo hilft dir, bei den einzelnen Schritten des WFM-Kreislaufs noch effizienter zu werden:

  {{ 1 | image: "WFM-Kreislauf: Forecasts erstellen, Planung, Schichtpläne erstellen, Tagessteuerung, Analyse", '60%' }}

- Forecasts erstellen: Prognostiziere deinen kurz-, mittel-, und langfristigen Workload.
- Planung: Entwickle Strategien zur Mitarbeitergewinnung und plane Budget und Trainings mit ausreichend Vorlauf.
- Schichtpläne erstellen: Erstelle die bestmöglichen Schichtpläne für deine Mitarbeiter und die Anforderungen deines Unternehmens.
- Tagessteuerung: Passe deine Schichtpläne in Echtzeit an unvorhergesehene Ereignisse an.
- Analyse: Analysiere die Performance deines Unternehmens, triff Prognosen für die Zukunft und verbessere sie.

In diesem Artikel erhältst du einen Überblick darüber, wie injixo dich bei allen Schritten des WFM-Kreislaufs unterstützen kann.
Als allererstes benötigt injixo Daten von deinen externen Systemen, um zuverlässige Forecasts zu erstellen. Um diese Daten für injixo bereitzustellen, musst du eine Integration zu deiner Automatic Call Distribution (ACD) bzw. deinem Customer Relationship Management (CRM) einrichten.

Neu bei Workforce Management? Sieh dir die wichtigsten Konzepte und Definitionen in unserem [Glossar](https://help.injixo.com/de/glossary/overview) an.

## 1. Forecasterstellung

### Integration einrichten

Um den Workload zu prognostizieren, den dein Unternehmen zu einem beliebigen zukünftigen Zeitpunkt erwartet, benötigt injixo Zugriff auf die Kontaktdaten bzw. Agentenstatus-Daten von deinen externen Systemen (z.&nbsp;B. ACD oder CRM). Damit injixo diese Daten importieren und verarbeiten kann, musst du deine {% link_new externen Systeme mit injixo verbinden | features/acd-integration/cloud/how-integrations-work.md %}. injixo bietet dazu native herstellerspezifische Integrationen und universelle Integrationen an. Je nach Integration empfängt injixo entweder alle 15, 30 bzw. 60 Minuten Daten (Import historischer Daten) oder sogar innerhalb von Sekunden (Echtzeit-Datenimport). 

Wenn du eine Integration hinzugefügt hast, sendet diese automatisch und kontinuierlich Daten an injixo.
Importierte Kontaktdaten werden in Queues gespeichert, die immer zu einem Kanal gehören. Du benötigst die Queues, um Workloads zu erstellen, die als Grundlage für deinen Forecast dienen.

### Workload erstellen  

Du kannst deine Integrationen unter _Account > Integrationen_{:.breadcrumbs} konfigurieren.

Um injixo Forecast zu nutzen, musst du zunächst {% link_new einen Workload erstellen | features/forecast/injixo-forecast/manage-workloads.md | #workloads-erstellen %}. Dazu nutzt du die Queues, die von deiner Integration importiert werden. Workloads enthalten alle deine historischen Daten und die damit verbundenen Forecasts. Damit du einen Workload erstellen kannst, muss deine ACD korrekt verbunden sein und die importierten Queues müssen verfügbar sein.

Du kannst Workloads unter _Forecast > Workloads_{:.breadcrumbs} erstellen. 

### Forecast erstellen

{% link_new injixo Forecast | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} vereint deine historischen Daten mit den am besten geeigneten Algorithmen, um qualitativ hochwertige Forecasts für bis zu 365 Tage zu erstellen.

Mit jedem neuen Datenimport wird der erzeugte Forecast aktualisiert. Du kannst außerdem {% link_new Ereignisse hinzufügen | features/forecast/injixo-forecast/events-and-holidays.md %}, die sich auf deinen Forecast auswirken.

### Mitarbeiterbedarf berechnen

Wenn du deinen Forecast erstellt hast, kannst du {% link_new den Mitarbeiterbedarf berechnen | features/forecast/injixo-forecast/staff-requirement.md %}, d.&nbsp;h. die Anzahl an Mitarbeitern, die geplant werden müssen, um den Bedarf zu decken, der sich aus dem Workload ergibt. Du kannst verschiedene {% link_new Berechnungsmethoden | best-practices/requirement-scripts.md %} verwenden, um deinen Mitarbeiterbedarf zu berechnen. Diese beziehen Faktoren wie angestrebte Service-Level, Antwortzeit, Shrinkage usw. mit ein. Bei Bedarf kannst du auch ein Skript für konstanten Mitarbeiterbedarf ohne einen Forecast verwenden.

Den Mitarbeiterbedarf kannst du im Planungsprozess nutzen, um optimierte Pläne für bestimmte Zeiträume, Planungseinheiten und Aktivitäten zu erstellen.

## 2. Planung

Nutze die von injixo Forecast erzeugten Daten, um deinen Mitarbeiterbedarf mit den tatsächlich verfügbaren Ressourcen abzugleichen. Mit dem langfristigen Forecast kannst du bessere Entscheidungen treffen, wenn es z.&nbsp;B. darum geht, Abwesenheitsanträge zu genehmigen, Stellenanzeigen zu veröffentlichen oder die richtigen Weiterbildungsprogramme für deine Mitarbeiter auszuwählen, um sie optimal auf anstehende Aufgaben vorzubereiten.

## 3. Schichtpläne erstellen

### Schichten planen

Wenn du deinen Mitarbeiterbedarf berechnet hast, stehen dir in injixo verschiedene {% link_new Planungsmethoden | features/scheduling/scheduling-methods.md %} zur Verfügung, die du einzeln oder kombiniert nutzen kannst, um deine Mitarbeiter optimal zu planen und die Anforderungen deines Unternehmens zu erfüllen.

Unter _Plan > Schedules_{:.breadcrumbs} kannst du Planungsregeln und Einschränkungen konfigurieren, um neben arbeitsrechtlichen Bestimmungen und vertraglichen Vereinbarungen auch die Bedürfnisse deiner Mitarbeiter zu berücksichtigen.

injixo bietet verschiedene Planungsfunktionalitäten wie z.&nbsp;B. {% link_new optimierte Planung | features/scheduling/schedules/schedules-optimized-schedules.md %}, {% link_new Mitarbeiter über Schichtplanänderungen informieren | features/scheduling/schedules/schedules-notify-scheduling-changes.md %} oder Mitarbeitern erlauben, ihre {% link_new Schichten mit anderen Mitarbeitern zu tauschen | features/scheduling/planning-periods/enable-employees-to-swap-shifts.md %}.

### Abwesenheiten planen

Unter {% link_new Time Off | features/scheduling/time-off/vacation-absences-management.md %} kannst du den Urlaubsanspruch und die Abwesenheitsanträge deiner Mitarbeiter für Urlaub oder Krankheit bzw. Anträge auf Freistellung und andere Abwesenheiten verwalten. Die Mitarbeiter können ihre Abwesenheitsanträge in {% link_new injixo Me | features/injixo-me/use-injixo-me/explore-injixo-me.md %} stellen. Du kannst auf Grundlage des Mitarbeiterbedarfs, der Verfügbarkeiten deiner Mitarbeiter und anderen vorab festgelegten Regeln und Einschränkungen entscheiden, ob du diese Anträge genehmigst oder ablehnst.

Konfiguriere Abwesenheiten unter _Plan > Time Off_{:.breadcrumbs}.

## 4. Tagessteuerung

Mit dem Feature {% link_new Intraday Adherence | features/intraday/adherence-intraday.md %} kannst du die geplanten Aktivitäten mit den tatsächlich ausgeführten Aktivitäten abgleichen und Abweichungen feststellen. Dort findest du detaillierte Statistiken und einen Adherence Score zur Bewertung der Planeinhaltung.

Diese Informationen stehen dir auch in Echtzeit zur Verfügung. Unter {% link_new Echtzeit Adherence | features/intraday/real-time-adherence.md %} erhältst du eine umfassende Übersicht, kannst die dargestellten Daten filtern und den angestrebten Adherence Score anpassen.

Mit diesen Informationen kannst du den Schichtplan kurzfristig anpassen, um auf unvorhergesehene Ereignisse einzugehen und Über- bzw. Unterbesetzung zu vermeiden.

## 5. Analyse
 
Mit injixo kannst du {% link_new Dashboards erstellen | features/monitoring/dashboards/dashboards-overview.md %}. Die darin enthaltenen Grafiken helfen dir, verschiedene Metriken besser darzustellen, z.&nbsp;B. für einen Vergleich zwischen Mitarbeiterbedarf und tatsächlicher Deckung oder zwischen prognostizierten und tatsächlich eingehenden Anrufen während verschiedener Zeitreihen.

Außerdem kannst du in injixo {% link_new verschiedene Arten von Reports erstellen | features/reporting/standard-reports/creating-reports.md %}, die dir dabei helfen, den Überblick über entscheidende Metriken zu behalten, wie z.&nbsp;B. Kapazität gemäß Vertragstyp, Arbeitszeit pro Planungseinheit oder Urlaubsübersicht.
