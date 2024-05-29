---
title: Freshchat-Integration hinzufügen
description: Erfahre, wie du dein Freshchat-CRM mit injixo verbinden kannst, um Daten zu importieren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
redirect_from:
  - de/add-freshdesk-messaging-integration/
redirect_reason: Updated filename on 15 September 2023
---

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Freshchat-Integration hinzufügen

Um eine neue Freshchat-Integration in injixo hinzuzufügen, benötigst du einen Pro- oder einen Enterprise-Account bei Freshchat.

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Freshworks**-Kachel auf _Modell wählen_{:.doc-button}.
4. Klicke im Abschnitt **Freshchat** auf _Integration hinzufügen_{:.doc-button}.

## Freshchat-Integration einrichten

1. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Gib im Abschnitt **Zugangsdaten** deinen vollständigen Freshchat-Domainnamen einschließlich der Subdomain ein, z.&nbsp;B. example.freshchat.com.
3. Gehe zu Freshchat und kopiere einen gültigen API-Schlüssel eines Benutzers mit der Rolle Account Administrator.
4. Gehe zurück zu injixo und füge den API-Key in das Feld **API-Schlüssel** ein.
5. Klicke auf _Integration speichern_{:.doc-button}.

### injixo-App installieren

Die Freshchat-Integration benötigt eine Client-Anwendung. Nachdem du deine Konfiguration gespeichert hast, kannst du auf den Abschnitt **Installiere injixo-App** am Ende der Seite zugreifen.

Generiere und kopiere dort den **injixo API-Key**.

Um die injixo-App in deinem Freshchat-Account einzurichten, folge den Anweisungen auf dem Bildschirm. Weitere Informationen findest du auf dem [Freshworks Marketplace](https://www.freshworks.com/apps/injixo_connect).

## Freshchat-Daten in injixo

### Kontakte

In Freshchat enthält ein Chat in der Regel mehrere Unterhaltungen, die zwischen deinen Mitarbeitern und deinen Kunden stattfinden. In injixo zählt jeder gelöste Chat als ein Kontakt, unabhängig von der Anzahl der Unterhaltungen.

Beispiel: Ein Kunde erstellt einen Chat auf der Website. Der Mitarbeiter antwortet daraufhin, löst das Problem aber erst einen Tag später, da er weitere Informationen benötigt. Dies würde in injixo als ein Kontakt gezählt werden.

### Namenskonvention für Quell-Queues

Die Quell-Queues, die injixo aus deinen Chats erstellt, folgen dieser Konvention:

"Gruppenname"

Beispiele:

- Kundensupport
- Undefined_Queue

### Gelöschte Chats und Spam-Chats

Ein Chat kann gelöscht oder als Spam markiert werden, wenn er aktualisiert wird. In diesem Fall kann die Integration den Gruppenamen nicht ermitteln. Die Quell-Queues, die solche Chats zählen, sind mit Undefined_Queue gekennzeichnet. Normalerweise spielen diese Queues bei der Schichtplanerstellung für deine Mitarbeiter keine Rolle.

## Häufig gestellte Fragen

| Frage                                                                                                                                                                                                  | Antwort                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| injixo zeigt plötzlich keine neuen Freshchat-Daten mehr an. Unter **Account > Integrationen** wird aber immer noch der Status Operational für meine Freshchat-Integration angezeigt. Was kann ich tun? | Die injixo-App erhält Freshchat-Daten und sendet Ereignisse an injixo. Bei einem Kommunikationsfehler zwischen der injixo-App und injixo können Freshchat-Daten eventuell nicht mehr angezeigt werden. Die Freshchat-Integration kann solche Kommunikationsfehler nicht erkennen.<br><br>Überprüfe, ob der injixo API-Schlüssel, den du beim Einrichten deiner injixo-App in deinem Freshchat-Account eingegeben hast, noch gültig ist. Wenn der API-Schlüssel ungültig ist, aktualisiere den injixo API-Schlüssel auf der Installationsseite der injixo-App. Wenn der API-Schlüssel noch gültig ist, wende dich an den injixo-Support. |
