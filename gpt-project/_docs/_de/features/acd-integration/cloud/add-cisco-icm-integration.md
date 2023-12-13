---
title: Cisco ICM-Integration hinzufügen
description: Erfahre, wie du dein Cisco ICM mit injixo verbinden kannst, um Daten zu importieren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Die Cisco ICM-Integration importiert Daten zur Planeinhaltung in Echtzeit. Die Integration verwendet {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Cisco ICM-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der Kachel **Cisco ICM** auf _Integration hinzufügen_{:.doc-button}.

## Cisco ICM-Integration einrichten

1. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Klicke im Abschnitt **injixo Cloud Link** auf den **Download-Link** für dein Betriebssystem.<br>
   > Hinweis
   >
   > Auch wenn du Cloud Link bereits für eine andere Integration herunterladen hast, musst du hier die Cisco-spezifische Version herunterladen.
3. Installiere und verbinde {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.<br>
4. Richte im Abschnitt **Konfiguration** deine Integration ein:

   - Gib einen **Connection String** mit den erforderlichen Parametern ein, um die Verbindung zu deiner Cisco-Datenbank herzustellen:   
   `DRIVER={MS SQL Server};Server=myServerAddress;Database=myDataBase;UserId=myUsername;Password=myPassword;`
   - Wähle die **Zeitzone der Datenbank** aus dem Dropdown-Menü aus.
   - Gib deine Cisco **Client-ID** und dein **Passwort** ein.
   - Gib dein **Peripherie-Gateway 1** ein.
   - (Optional) Gib dein **Peripherie-Gateway 2** ein.

4. Klicke auf _Integration speichern_{:.doc-button}.

injixo beginnt mit dem Import von RTA-Daten. Allerdings sind die Daten erst sichtbar, nachdem du deinen Mitarbeitern die externen Benutzerkennungen zugeordnet hast.

## Mitarbeitern externe Benutzerkennungen zuordnen

1. Gehe zu _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs}.
2. Ordne deinen Mitarbeitern externe Benutzerkennungen zu.
   > Hinweis
   >
   > Die externen Benutzerkennungen entsprechen den Unified CCE Skill Target IDs.

Erfahre mehr darüber, wie du {% link_new deinen Mitarbeitern externe Benutzerkennungen zuordnest | features/acd-integration/cloud/import-agent-status-data.md | #mitarbeitern-externe-benutzerkennungen-in-injixo-zuordnen %}.

## Agentenstatus den Aktivitäten in injixo zuordnen

1. Gehe zu _WFM > Administration > Scheduling > Aktivitäten_{:.breadcrumbs}.
2. Ordne Cisco ICM-Aktivitäten den entsprechenden injixo-Aktivitäten zu.

Erfahre mehr darüber, wie du {% link_new externe Aktivitäten den injixo-Aktivitäten zuordnest | features/acd-integration/cloud/import-agent-status-data.md | #aktivitäten-aus-externen-systemen-den-aktivitäten-in-injixo-zuordnen %}.
