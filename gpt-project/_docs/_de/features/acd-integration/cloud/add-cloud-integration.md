---
title: Cloud-Integration hinzufügen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lerne, wie Du eine Cloud-Integration hinzufügst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-five9-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

In diesem Artikel lernst Du, wie Du eine Cloud-Integration hinzufügst.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Was sind Cloud-Integrationen?

Cloud-Integrationen importieren Daten direkt aus einem Cloud-System. injixo unterstützt eine Vielzahl von Cloud-Integrationen.

## Cloud-Integration hinzufügen

1. Gehe zu *Account > Integrationen*{:.breadcrumbs}.
2. Klicke auf *Integration hinzufügen*{:.doc-button} und trage die erforderlichen Informationen in das Formular ein. In diesem Beispiel richten wir die Five9-Integration ein, aber der Einrichtungsprozess für andere Cloud-Integrationen ist ähnlich.
3. Wähle einen eindeutigen Namen für Deine Integration. Der Name sollte die Quelle der Daten genau benennen.
4. Gib den **Benutzernamen** und das **Passwort** von einem Benutzer ein, der in Deinem Five9-Konto die Administratorrolle besitzt.
5. Konfiguriere weitere integrationsspezifische Details, in diesem Fall die Region Deines Five9-Kontos und wie Du die Queues gruppieren möchtest. Erfahre mehr über den [benutzerdefinierten Five9-Report][2], der für die Gruppierung nach Skills bei Five9 benötigt wird.
6. Klicke auf *Speichern*{:.doc-button}, um die Integration mit den angegebenen Informationen zu erstellen.

{{ 1 | image: 'Five9 integration', '80%' }}

Die Integration importiert nun Daten in injixo. Der erste Import kann bis zu 15 Minuten dauern. Alle Queues aus dem verbundenen System werden automatisch für das Mapping auf dem {% link_new Workload-Konfigurationsbildschirm | features/forecast/injixo-forecast/manage-workloads.md %} in injixo Forecast verfügbar sein.

Wenn Deine Integration den Import von Agentenstatus-Daten unterstützt, musst Du noch {% link_new externe Benutzerkennungen und Aktivitäten zuordnen | features/acd-integration/cloud/import-agent-status-data.md %}, bevor die Agentenstatus-Daten importiert werden können.
