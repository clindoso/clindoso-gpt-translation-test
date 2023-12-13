---
title: Freshdesk-Integration hinzufügen
description: Lerne, wie Du eine Integration für Dein Freshdesk-CRM hinzufügst.
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

In diesem Artikel lernst Du, wie:
- Du eine Freshdesk-Integration hinzufügst.
- Du die erforderliche injixo App erhältst und installierst.
- injixo Freshdesk-Daten angezeigt.

Die Freshdesk-Integration liefert Kontaktvolumen für E-Mail, Webformulare, Chat und Social Messaging.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Eine Freshdesk-Integration hinzufügen

Um eine neue Freshdesk-Integration in injixo hinzuzufügen, folge dem Prozess wie in {% link_new Cloud-Integration hinzufügen | features/acd-integration/cloud/add-cloud-integration.md %} beschrieben:

1. Gib einen **eindeutigen Namen** für die neue Integration ein, der noch nicht verwendet wurde.
2. Fülle das Formular mit den erforderlichen Freshdesk-spezifischen Informationen aus:
   1. Gib Deinen vollständigen Freshdesk-Domainnamen einschließlich der Subdomain ein, z. B. *example.freshdesk.com*.
   2. Kopiere einen gültigen API-Key von Freshdesk:
      1. Melde Dich bei Freshdesk mit einem Benutzer mit der Rolle _Account Administrator_ an.
      2. Gehe zu den [_Profileinstellungen_](https://support.freshdesk.com/support/solutions/articles/215517-how-to-find-your-api-key).
      3. Kopiere den **API-Key** auf der Seite.
      4. Gehe zurück zu injixo und füge den API-Key in das Feld _API-Schlüssel_ ein.
3. Speichere Deine Konfiguration.

## Die injixo App installieren

Die Freshdesk-Integration benötigt eine Client-Anwendung. Nachdem Du Deine Konfiguration gespeichert hast, kannst Du auf den Abschnitt _injixo App installieren_ zugreifen.

Erzeuge und kopiere dort den **injixo API-Schlüssel**.  

Um die *injixo* App in Deinem Freshdesk-Konto einzurichten, folge den Anweisungen auf dem Bildschirm. Weitere Informationen findest Du auf dem [Freshworks marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## Freshdesk-Daten in injixo

injixo importiert alle Ticket-Daten aus Freshdesk. Tickets enthalten in der Regel mehrere Unterhaltungen, die zwischen Deinen Mitarbeitern und Kunden stattfinden.

### Tickets und Unterhaltungen

In injixo werden alle Unterhaltungen nach dem Freshdesk-Kommunikationskanal (_Source_) gruppiert. Eine Unterhaltung kann ein neues Ticket oder eine Antwort auf ein bestehendes Ticket sein.

In injixo werden die Unterhaltungen in einem Freshdesk-Ticket separat als angebotene Kontakte gezählt.

Beispiel: Ein Benutzer erstellt ein Ticket per E-Mail. Der Mitarbeitende antwortet und schließt das Ticket. Zwei Tage später wird das Ticket aufgrund einer weiteren E-Mail erneut geöffnet, was zu einer neuen Unterhaltung führt.

### Ereignisse aus verschiedenen Kanälen

In einem Freshdesk-Ticket können Antworten in verschiedenen injixo-Queues über den Kanal *Cases* erfasst werden.

Beispiel: Wenn eine E-Mail-Antwort auf ein Ticket eingeht, wird der Kontakt in einer injixo-Queue angezeigt, die der Freshdesk-Gruppe und dem Source-Namen entspricht. Ein Chat zum gleichen Ticket wird in einer separaten Queue gezählt.

### Konvention für die Benennung von Queues

Die Queues, die injixo aus Deinen Tickets erstellt, folgen dieser Konvention:

- "*Gruppenname* + *Source-Name* + _Tickets_"
- "*Gruppenname* + *Source-Name* + _Replies_"

Beispiele:

- Kundenbetreuung chat Tickets
- Kundenbetreuung email Replies
- Unknown group/source Tickets

Ein neues Ticket erzeugt eine Tickets-Queue. Eine Antwort auf eine Anfrage erzeugt eine Replies-Queue, in der auch alle anderen Antworten erfasst werden. Um alle Informationen über eine Anfrage zu erhalten, musst Du sowohl die Anfrage als auch die Antwort-Queue durchsuchen.

#### Gelöschte Tickets und Spam-Tickets

Der Gruppenname und der Source-Name können nicht bestimmt werden, wenn ein Ticket geändert wird, das bereits gelöscht oder als Spam markiert wurde. Die Quell-Queues, die solche Tickets zählen, werden mit _Unknown group/source Tickets_ oder _Unknown group/source Replies_ gekennzeichnet. Normalerweise sind diese Queues für die Planung der Arbeitsaufkommen Deiner Agenten irrelevant.
