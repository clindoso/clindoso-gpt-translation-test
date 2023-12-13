---
title: Verbinde Xlink mit injixo Forecast
toc: true
product_label:
  - advanced
  - enterprise
  - classic
description: Lerne, wie Du Xlink mit injixo Forecast verbindest, um historische Daten zu prognostizieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-installation-configuration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/forecastpro/administration/queues.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-mapping-telephony.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

In diesem Artikel lernst Du:

- wie Du Xlink mit injixo Forecast verbindest.
- die Vorteile der Erstellung von Eins-zu-Eins-Mappings.

Um die Grundlagen von Integrationen zu verstehen, lies den Artikel {% link_new Wie funktionieren Integrationen? | features/acd-integration/cloud/how-integrations-work.md %}.

## Xlink mit injixo Forecast verbinden

Um den Datenimport zu konfigurieren, {% link_new installiere Xlink | features/acd-integration/xlink-overview.md %}, wenn keine native Integration verfügbar ist. Xlink benötigt {% link_new Mappings | features/acd-integration/xlink-mapping-telephony.md %}, um Daten aus einer externen Queue mit einer injixo-Queue zu verbinden. Bevor Du Xlink-Mappings erstellen kannst, musst Du alle injixo-Queues erstellen.

### 1. Erstelle eine neue Integration für Xlink

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wähle den Typ **Universal Interfaces**.
3. Klicke auf _Integration hinzufügen_{:.doc-button} im Abschnitt _Xlink_.

<!-- this will change -->
<!-- adjust when EN is finished -->

### 2. injixo-Ziel-Queues erstellen

1. Gehe zu _WFM > Administration > Forecasting > Queues_{:.breadcrumbs}.
2. Erstelle eine neue {% link_new Ziel-Queue | features/forecast/forecastpro/administration/queues.md | #queues-erstellen %} für jede externe Queue. Es gibt mehrere Wertetypen für jeden Kanal (z. B. Anrufe, E-Mails, soziale Medien). Wertetypen sind erforderlich, um einen Forecast zu erstellen.
3. Klicke auf das {% icon item-add %}, um Wertetypen zu Deiner Ziel-Queue hinzuzufügen.
4. Wähle die **Wertetypen** für den Kanal aus. Für den Kanal _Anrufe_ wähle mindestens:
   - _Anrufe - AHT_
   - _Anrufe - Angenommene_
   - _Anrufe - Eingehende_

### 3. Mappings hinzufügen und Daten importieren

1. Öffne die Xlink-Benutzeroberfläche **isps_ul.exe** in Deiner Xlink-Installation.
2. Erstelle {% link_new Mappings | features/acd-integration/xlink-mapping-telephony.md | #mappings-erstellen %} zwischen jeder externen Queue und einer injixo-Queue.
3. Starte den {% link_new Xlink-Datenimport | features/acd-integration/xlink-import-mode.md %}.

Alle Ziel-Queues mit einem Mapping sind jetzt in Deinen Workloads verfügbar. Du kannst {% link_new Workloads erstellen oder anpassen | features/forecast/injixo-forecast/manage-workloads.md %}, nachdem der erste Datenimport abgeschlossen ist.

## Vorteile der Erstellung von Eins-zu-Eins-Mappings

Ein Eins-zu-Eins-Mapping ist eine Verbindung zwischen einer externen Queue und einer injixo-Ziel-Queue. Du kannst Eins-zu-Eins-Mappings in Deinen {% link_new workloads | features/forecast/injixo-forecast/manage-workloads.md %} gruppieren.

Durch die Erstellung von Eins-zu-Eins-Mappings in Xlink kannst Du:

- einzelne Queues in Workloads hinzufügen/entfernen.
- neue Forecasts sehen, wenn Du Deine Mappings in Workloads änderst.

Hinweis: Importierte Daten werden in injixo pro Queue gespeichert. Auch wenn Du Mappings änderst, sind Deine Daten weiterhin verfügbar. Du brauchst die Daten nicht erneut zu importieren.

Beispiel für Eins-zu-Eins-Mappings:

{{ 1 | image: 'Beispiel für Eins-zu-Eins-Mappings aus drei externen Queues', '80%'}}
