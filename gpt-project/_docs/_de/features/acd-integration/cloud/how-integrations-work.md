---
title: Wie funktionieren Integrationen?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie Integrationen funktionieren, welche Integrationen es gibt und wie du sie hinzufügen und löschen kannst.
promote-service: acd-integration-support
redirect_from: /de/cloud-overview/
redirect_reason: Datei umbenannt im Feb 2021
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Um dich bei deinem Workforce Management zu unterstützen, benötigt injixo Kontakt- und Agentenstatus-Daten von externen Systemen, z.&nbsp;B. einer Automatic Call Distribution (ACD) oder einem Customer Relationship Management (CRM). Damit injixo Daten empfangen und verarbeiten kann, musst du dein ACD- bzw. CRM-System in injixo integrieren.

injixo bietet sowohl native, herstellerspezifische als auch universelle Integrationen an, die sowohl für Cloud- als auch On-premise-Systeme verwendet werden können. Je nach Integration empfängt injixo entweder alle 15, 30 bzw. 60 Minuten Daten (Import historischer Daten) oder sogar innerhalb von Sekunden (Echtzeit-Datenimport).

## Bereitstellungsmodus

Der Bereitstellungsmodus einer Integration bestimmt, wie sich injixo zu dem externen System verbindet:

- Cloud-Integrationen verbinden sich mit einem Cloud-System wie z.B. Five9 oder Vonage und importieren Daten direkt von dort.
- On-premise-Integrationen nutzen {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}, um eine Verbindung zu einem System in deinem lokalen Netzwerk herstellen zu können. Beispiele: Genesys Engage oder Sikom. Ist die Verbindung hergestellt, beginnen On-Premise-Integrationen damit, historische Daten von bis zu drei Jahren zu importieren.

## Herstellerspezifische und universelle Integrationen

Herstellerspezifische Integrationen sind auf das spezifische System zugeschnitten und sollten immer die bevorzugte Option sein. Wenn keine herstellerspezifische Integration verfügbar ist, kannst du auch eine der universellen Integrationsoptionen verwenden:

- Datenbank: On-premise-Integration, die über eine SQL-Abfrage Daten aus einer Datenbank liest.
- CSV: Dateibasierte Integration, über die durch injixo Cloud Link CSV-Dateien importiert werden.
- injixo API: Cloud-Integration, die benötigt wird, um HTTP-Anfragen an die injixo&nbsp;API zu senden.

## Welche Daten werden importiert?

Je nach Integration importiert injixo Kontaktdaten, Agentenstatus-Daten oder beides:

- Zu Kontaktdaten (Anrufe, Chats, Social Media, Tickets, E-Mails oder Dokumente) gehören sowohl die eingehenden und angenommenen Kontakte als auch die durchschnittliche Bearbeitungszeit. Sie werden bei der Forecast-Erstellung verwendet.
- Agentenstatus-Daten (Anmeldung, Abmeldung, Nachbearbeitungszeit, Pausen, usw.) enthalten Informationen zu den Aktivitäten der Mitarbeiter, z.&nbsp;B. wann sie von einer Aktivität zu einer anderen wechseln. Sie werden für die Tagessteuerung verwendet.

## Integration hinzufügen

Um zu erfahren, wie du deine Integration einrichtest, sieh dir folgende Artikel an:

- {% link_new Cloud-Integration hinzufügen | features/acd-integration/cloud/add-cloud-integration.md %}
- {% link_new On-Premise-Integration hinzufügen | features/acd-integration/cloud/add-on-premise-integration.md %}
- {% link_new CSV-Integration hinzufügen | features/acd-integration/cloud/add-csv-integration.md %}
- {% link_new Datenbank-Integration hinzufügen | features/acd-integration/cloud/add-database-integration.md %}
- {% link_new API-Integration hinzufügen | features/acd-integration/cloud/import-data-with-injixo-api.md %}

Sobald du eine Integration hinzugefügt hast, sendet diese Daten an injixo.

Kontaktdaten werden automatisch importiert. Um mit Kontaktdaten zu arbeiten, musst du importierte Queues zu einem (neuen) Workload hinzufügen, um {% link_new einen Forecast zu erstellen | getting-started/calculate-a-forecast.md %}. Anschließend kannst du den Mitarbeiterbedarf berechnen und deinen Schichtplan erstellen.

> Voraussetzung zum Anzeigen von Agentenstatus-Daten
>
> Um Agentenstatus-Daten in Intraday zu sehen, {% link_new ordne die externen Benutzer- und Aktivitätskennungen zu | features/acd-integration/cloud/import-agent-status-data.md %}. Pausiere dazu als erstes den Datenimport deiner Integration.

<!-- add list of articles? or generic steps? -->

## Datenimport pausieren

Die Aktivitäten-Zuordnung wird von der laufenden Integration überschrieben. Um die Zuordnung beizubehalten und zu vermeiden, dass Aktivitäten dupliziert werden, pausiere den Datenimport. Klicke dazu auf der Übersichtsseite neben der Integration auf das {% icon pause_circle %}.

Um den Datenimport wiederaufzunehmen, wenn die Zuordnung abgeschlossen ist, klicke auf das {% icon play_circle %}. Fehlende Daten werden erneut importiert.

## Integration löschen

Wenn du eine Integration löschst, werden die importierten Daten nicht gelöscht. Die Queues bleiben deinen Workloads zugeordnet. Du kannst keine Queues löschen, die durch eine Integration erstellt wurden.

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Klicke auf das {% icon pencil %} neben der Integration, die du löschen möchtest.
3. Klicke unten rechts auf _Integration löschen_{:.doc-button}.
4. Klicke im Bestätigungsdialog auf _Ja, wirklich löschen_{:.doc-button}.
