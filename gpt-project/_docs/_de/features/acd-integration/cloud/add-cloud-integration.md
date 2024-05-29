---
title: Cloud-Integration hinzufügen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Verbinde deine ACD mit injixo, um Daten zu importieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-five9-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Was sind Cloud-Integrationen?

Cloud-Integrationen importieren Daten direkt aus einem Cloud-System. injixo unterstützt eine Vielzahl von Cloud-Integrationen.

## Cloud-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}. Die Seite zeigt alle verfügbaren Integrationen an.
2. Klicke auf _Integration hinzufügen_{:.doc-button} und gib die erforderlichen Informationen ein. In diesem Beispiel richten wir die Five9-Integration ein, aber der Einrichtungsprozess für andere Cloud-Integrationen ist ähnlich.
3. Wähle einen eindeutigen Namen für deine Integration. Der Name sollte die Quelle der Daten angeben.
4. Gib den **Benutzernamen** und das **Passwort** von einem Benutzer ein, der in deinem Five9-Konto die Administratorrolle besitzt.
5. Konfiguriere weitere integrationsspezifische Details (z.&nbsp;B. die Region deines Five9-Kontos und wie du die Queues gruppieren möchtest).
6. Klicke auf _Speichern_{:.doc-button}, um die Integration mit den angegebenen Informationen zu erstellen.

{{ 1 | image: 'Five9-Integration', '80%' }}

Die Integration importiert nun Daten in injixo. Der erste Import kann bis zu 15 Minuten dauern. Alle Queues aus dem verbundenen System werden automatisch für das Mapping auf dem {% link_new Workload-Konfigurationsbildschirm | features/forecast/injixo-forecast/create-workloads.md | #workloads-erstellen %} in injixo Forecast verfügbar sein.

Wenn deine Integration den Import von Agentenstatus-Daten unterstützt, musst du noch {% link_new externe Benutzerkennungen und Aktivitäten zuordnen | features/acd-integration/cloud/import-agent-status-data.md %}, bevor die Agentenstatus-Daten importiert werden können.
