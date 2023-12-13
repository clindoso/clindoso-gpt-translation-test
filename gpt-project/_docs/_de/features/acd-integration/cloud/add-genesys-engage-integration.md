---
title: Genesys Engage-Integration hinzufügen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du dein Genesys Engage-CMS mit injixo verbinden kannst, um Daten zu importieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Eine Genesys Engage-Integration ist eine On-premise-Integration, die Anrufhistorie und Agentenstatus-Daten importiert.

Die Integration verwendet {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Genesys Engage-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Genesys**-Kachel auf _Modell wählen_{:.doc-button}.
4. Klicke im Abschnitt **Genesys Engage** auf _Integration hinzufügen_{:.doc-button}.

## Genesys Engage-Integration einrichten

1. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Installiere und verbinde {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Richte deine Integration im Abschnitt **Datenbank-Zugangsdaten** ein:
 - Wähle deinen Datenbankadapter.
 - Gib den Host und den Port deiner Datenbank ein.
 - Gib den Benutzernamen und das Passwort für deine Datenbank ein.
 - Gib den Namen der ETL-Datenbank ein.
 - Gib den Namen der Konfigurationsdatenbank ein.
4. Wenn du Agentenstatus-Daten importieren möchtest, aktiviere im Abschnitt **Konfiguration** die Checkbox **Agentenstatus-Daten importieren**.<br>
Hinweis: Um Agentenstatus-Daten erfolgreich zu importieren, musst du zunächst {% link_new externe Benutzerkennungen und Aktivitäten | features/acd-integration/cloud/import-agent-status-data.md %} zuordnen.
5. Klicke auf _Integration speichern_{:.doc-button}.

Die Integration beginnt, Daten zu injixo zu importieren. 

## Genesys Engage-Integration bearbeiten

Wenn sich etwas an den Details deiner Integration ändert, z.&nbsp;B. die Zugangsdaten zum Datenbankserver, kannst du die Konfiguration deiner Integration bearbeiten und aktualisieren. Der Datenimport läuft unter der aktualisierten Konfiguration weiter.
