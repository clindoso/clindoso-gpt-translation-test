---
title: Historische Daten importieren
toc: true
product_label:
  - advanced
  - enterprise
  - classic
description: Lerne, wie Du historische Daten importierst, um injixo Forecast zu nutzen.
promote-service: acd-integration-support
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

In diesem Artikel lernst Du, wie Du historische Daten importierst, um Forecasts zu erstellen.

Neu in injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

Importiere historische Daten für die Eingangskanäle, die Du prognostizieren möchtest. injixo unterstützt die folgenden Kanäle:

- Anrufe
- E-Mails
- Chats
- Tickets
- Dokumente
- Social Media

Die unterstützten Kanäle hängen von der [Integration](https://injixo.com/account/integrations/catalogue) ab, die Du verwendest.

Hinweis: Wende Dich an Dein Customer Success-Team, wenn Deine aktuelle Integration nicht aufgeführt ist.

## Erforderliche Daten

injixo benötigt die folgenden Daten, um Forecasts zu erzeugen:

- eingehende Kontakte
- bearbeitete Kontakte
- Durchschnittliche Bearbeitungszeit (AHT)

Hinweis: Die bearbeiteten Kontakte sind notwendig, um die AHT in injixo Forecast anzuzeigen. Wenn Du mehrere Queues zu einem Workload hinzufügst, werden die bearbeiteten Kontakte zur Berechnung gewichteter Durchschnittswerte verwendet.

## Native Integration verwenden

Füge eine {% link_new native Integration | features/acd-integration/cloud/how-integrations-work.md %} hinzu, um Deine ACD zu verbinden. Native Integrationen importieren automatisch Daten und erstellen Queues.

## CSV-Integration verwenden

Füge eine {% link_new CSV-Integration | features/acd-integration/cloud/add-csv-integration.md %} hinzu, um CSV-Dateien zu importieren. Die CSV-Integration kann Daten (durch die Nutzung des Cloud Link-Clients) automatisch importieren und erstellt Queues auf Basis der importierten Daten.
