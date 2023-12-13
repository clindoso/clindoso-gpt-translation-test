---
title: On-Premise-Integration hinzufügen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie Du eine On-Premise-Integration hinzufügst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

In diesem Artikel lernst Du, wie Du eine On-Premise-Integration hinzufügst.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}. 

## Was sind On-Premise-Integrationen?

On-Premise-Integrationen verwenden den {% link_new injixo Cloud Link Client | features/acd-integration/cloud/install-cloud-link.md %}, um sich mit einem System in Deinem lokalen Netzwerk zu verbinden. Ist die Verbindung hergestellt, versuchen On-Premise-Integrationen, bis zu drei Jahre historische Daten zu importieren.

## On-Premise-Integration hinzufügen

1. Gehe zu *[Account > Integrationen](https://www.injixo.com/account/integrations/)*{:.breadcrumbs}.
2. Klicke auf *Integration hinzufügen*{:.doc-button} und trage die erforderlichen Informationen in das Formular ein. In diesem Beispiel richten wir die *Genesys-Engage-Integration* ein, aber der Einrichtungsprozess für andere On-Premise-Integrationen ist ähnlich.
3. Wähle einen eindeutigen **Namen** für Deine Integration. Der Name sollte die Quelle der Daten genau benennen.
4. Installiere den {% link_new injixo Cloud Link Client | features/acd-integration/cloud/install-cloud-link.md %}.
5. Konfiguriere weitere erforderliche integrationsspezifische Details, in diesem Fall die Datenbankzugangsdaten.
6. Klicke auf *Speichern*{:.doc-button}, um die Integration mit den angegebenen Informationen zu erstellen.

{{ 1 | image: 'Genesys Engage integration', '80%' }}

Die Integration importiert nun Daten in injixo. Der erste Import kann bis zu 15 Minuten dauern. Alle Queues aus dem verbundenen System werden automatisch für das Mapping auf dem {% link_new Workload-Konfigurationsbildschirm | features/forecast/injixo-forecast/manage-workloads.md %} in injixo Forecast verfügbar sein.

Wenn Deine Integration den Import von Agentenstatus-Daten unterstützt, musst Du noch {% link_new externe Benutzerkennungen und Aktivitäten zuordnen | features/acd-integration/cloud/import-agent-status-data.md %}, bevor die Agentenstatus-Daten importiert werden können.
