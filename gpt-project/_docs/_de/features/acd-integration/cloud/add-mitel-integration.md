---
title: Mitel-Integration hinzufügen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du dein Mitel-CRM mit injixo verbinden kannst, um Daten zu importieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Eine Mitel-Integration ist eine On-premise-Integration, die historische Daten aus Anrufen, E-Mails, Chats und Social Media sowie Agentenstatus-Daten importiert.

Die Integration verwendet {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Mitel-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Mitel**-Kachel auf _Integration hinzufügen_{:.doc-button}.

## Mitel-Integration einrichten

1. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Installiere und verbinde {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Wähle im Abschnitt **Regionale Einstellungen** die Zeitzone deiner ACD aus.
4. Richte deine Integration im Abschnitt **Datenbankzugangsdaten** ein:
   Just a note: On the Integrations page, we write Datenbankzugangsdaten.

   - Gib den Host und den Port deiner Datenbank ein.
   - Gib den Benutzernamen und das Passwort für deine Datenbank ein.

5. Wenn du Agentenstatus-Daten importieren möchtest, aktiviere im Abschnitt **Konfiguration** die Checkbox **Agentenstatus-Daten importieren**.<br>Hinweis: Wenn du Agentenstatus-Daten importieren möchtest, musst du zunächst {% link_new externe Benutzerkennungen und Aktivitäten | features/acd-integration/cloud/import-agent-status-data.md %} zuordnen.
6. Klicke auf _Integration speichern_{:.doc-button}.

Die Integration beginnt, Daten zu injixo zu importieren.

## Mitel-Integration bearbeiten

Wenn sich etwas an den Details deiner Integration ändert, z.&nbsp;B. die Zugangsdaten zum Datenbankserver, kannst du die Konfiguration deiner Integration bearbeiten und aktualisieren. Der Datenimport läuft unter der aktualisierten Konfiguration weiter.
