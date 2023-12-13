---
title: Zendesk-Integration hinzufügen
description: Erfahre, wie du dein Zendesk-CRM mit injixo verbinden kannst, um Daten zu importieren.
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
---

Eine Zendesk-Integration ist eine Cloud-Integration, die Kontaktvolumen für E-Mail, Webformulare, Chat, Anrufe und Social Messaging durch den Import von Daten aus Zendesk Support und Zendesk Talk importiert. 

Die Integration importiert nur eingehende Anrufe, keine ausgehenden Anrufe. Die Daten für die durchschnittliche Bearbeitungszeit (AHT) sind nur für Zendesk Talk verfügbar.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen| features/acd-integration/cloud/how-integrations-work.md %}.

## Zendesk-Integration hinzufügen

Erstelle in deinem Zendesk-Account einen API-Token für einen Benutzer mit [Admin-Zugriff](https://support.zendesk.com/hc/de/articles/4408843355290-Zendesk-Integration-f%C3%BCr-Salesforce-Erforderliche-Profilberechtigungen).

Um eine neue Zendesk-Integration in injixo hinzuzufügen, gehe wie folgt vor:

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der Zendesk-Kachel auf _Integration hinzufügen_{:.doc-button}.
4. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
5. Gib im Abschnitt **Benutzer-Zugangsdaten** deine Zendesk-Zugangsdaten ein:
   * Gib deinen vollständigen Zendesk-Domainnamen einschließlich der Subdomain ein, z.&nbsp;B. example.zendesk.com.
   * Gib deinen Zendesk-Benutzernamen ein.
   * Gib deinen API-Token ein.
Wähle entweder die Option **IVR** oder **Telefonnummer**. 

   > Nachdem die Integration in injixo gespeichert wurde, kann die Gruppierungsstrategie nicht mehr geändert werden.

7. Klicke auf _Integration speichern_{:.doc-button}.

## Zendesk-Daten in injixo

### Tickets vs. Kontaktereignisse

In Zendesk enthält ein Ticket mehrere Interaktionen zwischen deinen Mitarbeitern und deinen Kunden über die verschiedenen Kommunikationskanäle.

Jede Interaktion ist eine Aufgabe, die deine Mitarbeiter bearbeiten müssen. Eine Interaktion kann ein neues Ticket oder eine Änderung an einem bestehenden Ticket sein.

Beispiel: Ein Benutzer erstellt ein Ticket, indem er eine E-Mail schreibt. Der Mitarbeiter antwortet dann und schließt das Ticket. Zwei Tage später sendet der Benutzer eine weitere E-Mail als Antwort auf die E-Mail des Mitarbeiters, die das Ticket wieder öffnet. injixo zählt dies als zwei E-Mails, obwohl der Vorgang auf einem einzelnen Ticket passiert.

### Views

injixo erstellt Queues auf der Grundlage deiner Zendesk-Views. Nach dem ersten Datenimport siehst du eine Queue für jede unterstützte View, die du in Zendesk erstellt hast. Wenn eine View Ereignisse aus verschiedenen Kanälen enthält (z.&nbsp;B. Chat und E-Mail), werden diese in separaten {% link_new Kanälen | features/forecast/injixo-forecast/manage-workloads.md | #queues-und-kanäle %} in injixo angezeigt.

Hinweis: Wenn du neue Zendesk-Views anlegst, nachdem die Integration gespeichert wurde, werden automatisch neue injixo-Queues und die dazugehörigen historischen Daten importiert.

### Nicht unterstützte Views

injixo kann Quell-Queues für die meisten Views erstellen. Aktuell werden keine Queues unterstützt, die die folgenden Ticketfelder verwenden:

- Business Hours
- SLA
- Channel
- Skills
- Bedingungen mit Benutzer-spezifischen Werten (z.&nbsp;B. Assignee is (current user))

Falls du Zendesk-Views mit Bedingungen hast, die sich auf mindestens eines der oben genannten Felder beziehen, ignoriert injixo diese Views und erstellt dafür keine Queue.

### Kanal-Mapping zwischen Zendesk und injixo

Jede Änderung an einem Ticket in Zendesk kann in mehreren injixo-Kanälen gezählt werden.

Beispiel: Eine E-Mail erstellt ein Ticket, das in einer E-Mail-Queue in injixo angezeigt wird. Wenn dasselbe Ticket in einer Chat-View angezeigt wird, wird es zudem in einer Chat-Queue in injixo gezählt.

| Zendesk-Kanal                           | injixo       |
| ----------------------------------------- | ------------ |
| email                                     | email        |
| mobile                                    | email        |
| web                                       | email        |
| chat                                      | chat         |
| native_messaging                          | chat         |
| sms                                       | social_media |
| any_channel                               | social_media |
| facebook                                  | social_media |
| twitter                                   | social_media |
| sunshine_conversations_facebook_messenger | social_media |
| instagram_dm                              | social_media |
| voice                                     | call         |
| api                                       | case         |
| answer_bot_for_web_widget                 | case         |
| chat_transcript                           | case         |
| mobile_sdk                                | case         |

### Queue-Namen für Zendesk Support

Der resultierende Queue-Name für Zendesk Support-Queues folgt dieser Konvention:

"Name der View + (injixo-Kanal)"

Beispiele:

- Support Tickets (Chat)

### Queue-Namen für Zendesk Talk

Der resultierende Queue-Name für Zendesk Talk-Queues folgt dieser Konvention:

"Calls Inbound For + Gruppierungsstrategie"

Beispiele:

- Calls Inbound For +49123456789 (Telefonnummer )
- Calls Inbound For Senior Agents (IVR)
- Calls Inbound Ungrouped
