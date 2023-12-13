---
title: Five9-Integration hinzufügen
description: Verbinde deine Five9-ACD mit injixo und erstelle einen benutzerdefinierten Report, um Queue-Gruppierungen entsprechend der Qualifikationen zu nutzen.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /de/five9-grouping-by-skills/
redirect_reason: Datei umbenannt im Feb 2021
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Eine Five9-Integration ist eine Cloud-Integration, die Anrufhistorie, Agentenstatus-Daten und Daten zur Planeinhaltung in Echtzeit importiert.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Voraussetzungen

Wenn du deine Queues nach Kampagnen gruppierst, liest die Integration den Standard-Logbericht für Anrufe von Five9.

Wenn du deine Queues nach Qualifikationen gruppierst, benötigt die Integration einen benutzerdefinierten Logbericht für Anrufe von Five9, der Qualifikationen enthält. Um Daten aus Queues zu importieren, die nach Qualifikationen gruppiert sind, führe in Five9 folgende Schritte aus:

 1. Erstelle einen neuen geteilten Ordner für Reports.
 2. Passe den Standard-Logbericht für Anrufe an, indem du die „SKILL“-Spalte hinzufügst.
 3. Speichere den benutzerdefinierten Report als „Call Log with Skills“ im geteilten Ordner.

Um mehr darüber zu erfahren, wie du Reports anpassen kannst, sieh dir das Five9-Help Center an.

## Five9-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Five9**-Kachel auf _Integration hinzufügen_{:.doc-button}.
4. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
5. Gib den Benutzernamen und das Passwort einer Person ein, die Admin-Zugriff auf das Five9-Konto hat.
6. Wähle im Abschnitt **Konfiguration** deine Kontoregion aus und wie du Queues gruppieren möchtest.
7. Klicke auf _Integration speichern_{:.doc-button}.

Die Integration importiert nun Daten in injixo. Der erste Import kann bis zu 15 Minuten dauern. Alle Queues aus dem verbundenen System werden automatisch für das Mapping auf dem {% link_new Workload-Konfigurationsbildschirm | features/forecast/injixo-forecast/manage-workloads.md | #workloads-erstellen %} in injixo Forecast verfügbar sein.

## Was passiert, wenn für einen Agenten mehrere Status gleichzeitig vorliegen?

Manchmal zeigt Five9 mehrere Status für einen Agenten gleichzeitig an, zum Beispiel:

| Status   | Startzeit | Endzeit |
| ------- | ---------- | -------- |
| Ready   | 13:00:00   | 13:00:05 |
| Inbound | 13:00:00   | 13:03:00 |

Um zu vermeiden, dass ein Status durch einen anderen überschrieben wird, ändert die Integration den Beginn des länger andauernden Status. Der Beginn des längeren Status wird dabei gleichzeitig das Ende des kürzeren Status:

| Status   | Startzeit | Endzeit |
| ------- | ---------- | -------- |
| Ready   | 13:00:00   | 13:00:05 |
| Inbound | 13:00:05   | 13:03:00 |
