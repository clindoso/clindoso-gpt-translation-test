---
title: Freshdesk Contact Center-Integration hinzufügen
description: Verbinde Dein Freshdesk Contact Center CRM mit injixo und nutze die importierten Daten.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

In diesem Artikel lernst Du, wie:

- Du eine Freshdesk Contact Center-Integration hinzufügst.
- Du die erforderliche injixo App erhältst und installierst.
- injixo Daten aus Freshdesk Contact Center anzeigst.

Die Freshdesk Contact Center-Integration liefert das Volumen der angebotenen Anrufe.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Eine Freshdesk Contact Center-Integration hinzufügen

Um eine neue Freshdesk Contact Center-Integration in injixo hinzuzufügen, folge dem Prozess wie in {% link_new Cloud-Integration hinzufügen | features/acd-integration/cloud/add-cloud-integration.md %} beschrieben:

1. Gib einen eindeutigen **Namen** für die Integration ein.
2. Fülle das Formular mit den erforderlichen Freshdesk Contact Center-spezifischen Informationen aus:

   - Gib Deinen Freshdesk Contact Center-Domainnamen ein (einschließlich der Subdomain), z. B. _example.freshcaller.com_.
   - Kopiere einen gültigen API-Key von Freshdesk Contact Center:
     1. Melde Dich bei Freshdesk Contact Center mit einem Benutzer mit der Rolle _Account Administrator_ an.
     2. Gehe in Freshdesk Contact Center zu den [_Profileinstellungen_](https://support.freshdesk.com/support/solutions/articles/215517-how-to-find-your-api-key)
     3. Kopiere den **API-Key**.
     4. Gehe zurück zu injixo und füge den API-Key in das Feld _API-Schlüssel_ ein.
   - Wähle die [Gruppierung für importierte Queues](#queuenamen-nach-gruppierung).

Nachdem Du die Konfiguration gespeichert hast, fahre im Abschnitt **injixo App installieren** fort.

## Die injixo App installieren

1. Erzeuge und kopiere den **injixo API-Schlüssel** im Abschnitt **injixo App installieren**.
2. Richte die erforderliche _injixo_ App in Deinem Freshdesk-Konto im [Freshworks Marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect) ein.
3. Füge den kopierten API-Schlüssel auf der Installationsseite der injixo-App ein.
4. Um Daten in Echtzeit zu importieren, aktiviere auf der Installationsseite der injixo-App die Checkbox **Export real-time agent status data**.

### Queuenamen nach Gruppierung

Beim Datenimport beeinflusst die Gruppierung die Namen der Queues, die in injixo erzeugt werden:

| Gruppierung         | Queuename                                       | Beispiel                 |
| ------------------- | ----------------------------------------------- | ------------------------ |
| Telefonnummer       | Telefonnummer                                   | +49123456789             |
| Routing(Team/Agent) | Teamname                                        | Technisches Support-Team |
| Routing(Team/Agent) | Agentenname (wenn kein Teamname zugewiesen ist) | Agent 1                  |

Für Anrufe, die in Freshdesk Contact Center keine Gruppe haben, ist der Queuename _Undefined_Queue_.
