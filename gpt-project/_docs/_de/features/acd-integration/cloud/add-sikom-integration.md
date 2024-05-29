---
title: Sikom-Integration hinzufügen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du dein Sikom-CRM mit injixo verbinden kannst, um Daten zu importieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Eine Sikom-Integration ist eine On-premise-Integration, die Anruf-Historie, Agentenstatus-Daten und Daten zur Planeinhaltung in Echtzeit importiert.

Die Integration verwendet {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Sikom-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Sikom**-Kachel auf _Integration hinzufügen_{:.doc-button}.

## Sikom-Integration einrichten

1. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Installiere und verbinde {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Richte deine Integration im Abschnitt **Datenbankzugangsdaten** ein:

   - Wähle die Zeitzone deiner Datenbank aus.
   - Gib den Host und den Port deiner Datenbank ein.
   - Gib den Benutzernamen und das Passwort für deine Datenbank ein.

4. Wenn du Agentenstatus-Daten importieren möchtest, aktiviere im Abschnitt **Konfiguration** die Checkbox **Agentenstatus-Daten importieren**.<br>Hinweis: Wenn du Agentenstatus-Daten importieren möchtest, musst du zunächst {% link_new externe Benutzerkennungen und Aktivitäten | features/acd-integration/cloud/import-agent-status-data.md %} zuordnen.
5. Klicke auf _Integration speichern_{:.doc-button}.

Die Integration beginnt, Daten zu injixo zu importieren.

## Sikom-Integration bearbeiten

Wenn sich etwas an den Details deiner Integration ändert, z.&nbsp;B. die Zugangsdaten zum Datenbankserver, kannst du die Konfiguration deiner Integration bearbeiten und aktualisieren. Der Datenimport läuft unter der aktualisierten Konfiguration weiter.
