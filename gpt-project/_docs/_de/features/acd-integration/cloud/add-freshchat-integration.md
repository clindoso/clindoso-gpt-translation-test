---
title: Freshchat-Integration hinzufügen
description: Verbinde Dein Freshchat CRM mit injixo und nutze die importierten Daten in injixo Forecast.
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
redirect_from:
  - /de/add-freshdesk-messaging-integration/
redirect_reason: Updated filename on 15 September 2023
---

In diesem Artikel lernst Du, wie:
- Du eine Freshchat-Integration hinzufügst.
- Du die erforderliche injixo App erhältst und installierst.
- injixo Freshchat-Daten anzeigt.

Die Freshchat-Integration liefert Kontaktvolumina für Chats.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Eine Freshchat-Integration hinzufügen

Um eine neue Freshchat-Integration in injixo hinzuzufügen, folge dem Prozess wie in {% link_new Cloud-Integration hinzufügen | features/acd-integration/cloud/add-cloud-integration.md %} beschrieben:

1. Gib einen **eindeutigen Namen** für die neue Integration ein, der noch nicht verwendet wurde.
2. Fülle das Formular mit den erforderlichen Freshchat-spezifischen Informationen aus:
    1. Gib Deinen vollständigen Freshchat-Domainnamen einschließlich der Subdomain ein, z. B. *example.freshchat.com*.
    2. Kopiere einen gültigen API-Key von Freshchat:
      1. Melde Dich bei Freshchat mit einem Benutzer mit der Rolle _Account Administrator_ an.
      2. Gehe zum Admin-Modul. Du findest die [API Tokens](https://support.freshchat.com/en/support/solutions/articles/50000000011-api-tokens) im Abschnitt *Configure* in Freshchat.
      3. Kopiere den **API-Key** auf der Seite.
      4. Gehe zurück zu injixo und füge den API-Key in das Feld _API-Schlüssel_ ein.
3. Speichere Deine Konfiguration.

## Die injixo App installieren

Die Freshchat-Integration benötigt eine Client-Anwendung. Nachdem Du Deine Konfiguration gespeichert hast, kannst Du auf den Abschnitt _injixo App installieren_ zugreifen.

Erzeuge und kopiere dort den **injixo API-Schlüssel**.  

Um die *injixo* App in Deinem Freshdesk-Konto einzurichten, folge den Anweisungen auf dem Bildschirm. Weitere Informationen findest Du auf dem [Freshworks marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## Freshchat-Daten in injixo

### Kontakte

In Freshchat enthält ein Chat in der Regel mehrere Unterhaltungen, die zwischen Deinen Mitarbeitern und Deinen Kunden stattfinden. In injixo zählt jeder gelöste Chat als ein Kontakt, unabhängig von der Anzahl der Unterhaltungen.

Beispiel: Ein Kunde erstellt einen Chat auf der Website. Der Mitarbeiter antwortet daraufhin, löst das Problem aber erst einen Tag später, da er weitere Informationen benötigt. Dies würde in injixo als ein Kontakt gezählt werden.

### Namenskonvention für Quell-Queues

Die Quell-Queues, die injixo aus Deinen Chats erstellt, folgen dieser Konvention:

"_Gruppenname_"

Beispiele:

- Kundenbetreuung
- Undefined_Queue

#### Gelöschte Chats und Spam-Chats

Ein Chat kann gelöscht oder als Spam markiert werden, wenn er aktualisiert wird. In diesem Fall kann die Integration den Gruppenamen nicht ermitteln. Die Quell-Queues, die solche Chats zählen, sind mit _Undefined_Queue_ gekennzeichnet. Normalerweise sind diese Queues für die Planung der Arbeitsaufkommen Deiner Agenten irrelevant.
