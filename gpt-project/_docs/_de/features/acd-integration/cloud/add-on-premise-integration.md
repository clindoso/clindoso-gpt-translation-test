---
title: On-Premise-Integration hinzufügen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Verbinde deine on-premise Datenbank mit injixo, um Kontaktvolumen, AHT und Agentenstatus-Daten zu importieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Was sind On-premise-Integrationen?

On-premise-Integrationen nutzen {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}, um eine Verbindung zu einem System in deinem lokalen Netzwerk herstellen zu können. Ist die Verbindung hergestellt, versuchen On-Premise-Integrationen, historische Daten von bis zu drei Jahren zu importieren.

## On-Premise-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wähle dein externes System aus und klicke auf _Integration hinzufügen_{:.doc-button}. Wenn es verschiedene Modelle deines externen Systems gibt, klicke auf _Modell wählen_{:.doc-button} und dann auf _Integration hinzufügen_{:.doc-button}.
3. Trage die erforderlichen Informationen in das Formular ein. Um die Quelle für die Daten später zu identifizieren, gib einen eindeutigen Namen für deine Integration ein.
4. Installiere den {% link_new injixo Cloud Link Client | features/acd-integration/cloud/install-cloud-link.md %}.
5. Klicke auf _Integration speichern_{:.doc-button}.

{{ 1 | image: 'Genesys Engage-Integration', '85%' }}

Die Integration importiert nun Kontaktdaten in injixo. Der erste Import kann einige Zeit dauern. Alle Queues aus dem verbundenen System werden automatisch für das Mapping auf dem {% link_new Workload-Konfigurationsbildschirm | features/forecast/injixo-forecast/manage-workloads.md | #workloads-erstellen %} in injixo Forecast verfügbar sein.

Wenn deine Integration den Import von Agentenstatus-Daten unterstützt, {% link_new ordne externe Benutzerkennungen und Aktivitäten zu | features/acd-integration/cloud/import-agent-status-data.md %}. Die Integration kann dann Agentenstatus-Daten importieren.
