---
title: Genesys Cloud-Integration hinzufügen
description: Erfahre, wie du dein Genesys Cloud-CRM mit injixo verbinden kannst, um Daten zu importieren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Eine Genesys Cloud-Integration ist eine Cloud-Integration, die Anruf-, E-Mail- und Chat-Historie sowie Agentenstatus- und Real-Time-Adherence-Daten importiert.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Genesys Cloud-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Genesys**-Kachel auf _Modell wählen_{:.doc-button}.
4. Klicke im Abschnitt **Genesys Cloud** auf _Integration hinzufügen_{:.doc-button}.

## Genesys Cloud-Integration einrichten

1. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Füge im Abschnitt **API-Zugangsdaten** deinen von Genesys kopierten API-Schlüssel und dein API-Secret ein.
3. Wähle im Abschnitt **Konfiguration** deine Kontoregion aus.
4. (Optional) Aktiviere die Checkbox **Detaillierte On-Queue-Agentenstatus importieren**.<br>Der Agentenstatus on-queue umfasst mehrere Status, z.&nbsp;B. communication, interacting, idle, not responding. Beim Import von Agentenstatus unterscheidet injixo zwischen den einzelnen Status, die unter on-queue zusammengefasst sind.
5. Klicke auf _Integration speichern_{:.doc-button}.

## Häufig gestellte Fragen

| Frage                                                                                                                                                                                                    | Antwort                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Die Integration importiert Daten für abgebrochene Anrufe, durchschnittliche Antwortzeit und Anrufe, die gemäß Service-Level beantwortet wurden. Warum kann ich diese Daten in Dashboards nicht anzeigen? | Du kannst diese Daten in Dashboards anzeigen, wenn du beim Konfigurieren eines Workloads in Forecast ausschließlich Queues von deiner Genesys Cloud-Integration hinzufügst. Du kannst diese Daten nicht anzeigen, wenn du auch Queues von weiteren Integrationen miteinschließt. |
