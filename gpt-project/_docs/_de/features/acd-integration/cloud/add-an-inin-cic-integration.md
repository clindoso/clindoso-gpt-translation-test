---
title: Interactive Intelligence CIC-Integration hinzufügen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du dein Interactive Intelligence CIC mit injixo verbinden kannst, um Daten zu importieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Eine Interactive Intelligence CIC-Integration ist eine On-premise-Integration, die Daten zur Planeinhaltung in Echtzeit importiert.

Die Integration verwendet {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Interactive Intelligence CIC-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Genesys**-Kachel auf _Modell wählen_{:.doc-button}.
4. Klicke im Abschnitt **Interactive Intelligence CIC** auf _Integration hinzufügen_{:.doc-button}.

## Interactive Intelligence CIC-Integration konfigurieren

1. Gib einen eindeutigen Namen für die neue Integration ein.
   Dieser Name hilft dir, die Datenquelle zu identifizieren und die Queue zu bestimmen, zu der die Integration gehört.<br>Beispiel: CIC - Customer Support Team
2. Installiere und verbinde {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Richte im Abschnitt **Konfiguration** deine Integration ein:

   - **Zeitzone**: Wähle die Zeitzone deiner ACD aus dem Dropdown-Menü aus.
   - **ACD-Serveradressen**: Gib den DNS-Namen bzw. die IP-Adresse und mit Doppelpunkt getrennt den Port deiner ACD ein, z.&nbsp;B.: acd.example.com:8080.<br>Wenn du mehrere ACDs angeben möchtest, trenne sie mit Kommas voneinander.

4. Klicke auf _Speichern_{:.doc-button}, um die Integration zu erstellen.

Die Integration beginnt, Daten zu injixo zu importieren. Um Agentenstatus-Daten zu importieren, musst du zunächst {% link_new externe Benutzerkennungen und Aktivitäten zuordnen | features/acd-integration/cloud/import-agent-status-data.md %}, sobald deine Interactive Intelligence CIC-Integration eingerichtet ist.

## Interactive Intelligence CIC-Integration bearbeiten

Wenn sich etwas an den Details deiner Integration ändert, z.&nbsp;B. die Zugangsdaten zum ACD-Port, kannst du die Konfiguration deiner Integration bearbeiten und aktualisieren. Der Datenimport läuft unter der aktualisierten Konfiguration weiter.
