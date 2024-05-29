---
title: Freshdesk Contact Center-Integration hinzufügen
description: Erfahre, wie du dein Freshdesk Contact Center-CRM mit injixo verbinden kannst, um Daten zu importieren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Eine Freshdesk Contact Center-Integration ist eine Integration, die Daten zur Anrufhistorie und zur Planeinhaltung in Echtzeit importiert.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Freshdesk Contact Center-Integration hinzufügen

Um eine neue Freshdesk Contact Center-Integration in injixo hinzuzufügen, benötigst du einen Pro- oder einen Enterprise-Account bei Freshdesk Contact Center.

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Freshworks**-Kachel auf _Modell wählen_{:.doc-button}.
4. Klicke im Abschnitt **Freshdesk Contact Center** auf _Integration hinzufügen_{:.doc-button}.

## Freshdesk Contact Center-Integration einrichten

1. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Gib im Abschnitt **Zugangsdaten** deinen vollständigen Freshdesk Contact Center-Domainnamen (einschließlich der Subdomain) ein, z.&nbsp;B. example.freshcaller.com.
3. Gehe zu Freshdesk Contact Center und kopiere einen gültigen API-Schlüssel eines Benutzers mit der Rolle Account Administrator.
4. Gehe zurück zu injixo und füge den API-Schlüssel in das Feld **API-Schlüssel** ein.
5. Wähle die [Gruppierungsstrategie für importierte Queues](#queue-namen-nach-gruppierungsstrategie).
6. Klicke auf _Integration speichern_{:.doc-button}.

Nachdem du deine Konfiguration gespeichert hast, kannst im Abschnitt **injixo App installieren** fortfahren.

## injixo-App installieren

1. Generiere und kopiere den **injixo API-Key** im Abschnitt **Installiere die injixo-App**.
2. Richte die erforderliche injixo-App in deinem Freshdesk Contact Center-Account im [Freshworks Marketplace](https://www.freshworks.com/apps/injixo_1) ein.
3. Füge auf der Installationsseite für die injixo-App den kopierten API-Schlüssel ein.
4. Um Daten in Echtzeit zu importieren, aktiviere die Checkbox **Export real-time agent status data** auf der Installationsseite für die injixo-App im Freshworks Marketplace.

## Queue-Namen nach Gruppierungsstrategie

Beim Importieren von Daten wirkt sich die Gruppierungsstrategie auf die Namen der in injixo erstellten Queues aus:

| Gruppierungsstrategie | Queue-Name                                      | Beispiel          |
| --------------------- | ----------------------------------------------- | ----------------- |
| Telefonnummer         | Telefonnummer                                   | +49123456789      |
| Routing (Team/Agent)  | Teamname                                        | Tech Support Team |
| Routing (Team/Agent)  | Agentenname (wenn kein Teamname zugewiesen ist) | Agent 1           |

Für Anrufe, die keine Gruppe im Freshdesk Contact Center haben, lautet der Queue-Name Undefined_Queue.

## Häufig gestellte Fragen

| Frage                                                                                                                                                                                                                                | Antwort                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| injixo zeigt plötzlich keine neuen Freshdesk Contact Center-Daten mehr an. Unter **Account > Integrationen** wird aber immer noch der Status Operational für meine Freshdesk Contact Center-Integration angezeigt. Was kann ich tun? | Die injixo-App erhält Freshdesk Contact Center-Daten und sendet Ereignisse an injixo. Bei einem Kommunikationsfehler zwischen der injixo-App und injixo können Freshdesk Contact Center-Daten eventuell nicht mehr angezeigt werden. Die Freshdesk Contact Center-Integration kann solche Kommunikationsfehler nicht erkennen.<br><br>Überprüfe, ob der injixo API-Schlüssel, den du beim Einrichten deiner injixo-App in deinem Freshdesk Contact Center-Account eingegeben hast, noch gültig ist. Wenn der API-Schlüssel ungültig ist, aktualisiere den injixo API-Schlüssel auf der Installationsseite der injixo-App. Wenn der API-Schlüssel noch gültig ist, wende dich an den injixo-Support. |
