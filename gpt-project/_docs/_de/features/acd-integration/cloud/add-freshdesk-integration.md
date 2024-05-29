---
title: Freshdesk-Integration hinzufügen
description: Erfahre, wie du dein Freshdesk-CRM mit injixo verbinden kannst, um Daten zu importieren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Eine Freshdesk-Integration ist eine Cloud-Integration, die Kontaktvolumen für E-Mail, Webformulare, Chat und Social Messaging importiert.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Eine Freshdesk-Integration hinzufügen

Um eine neue Freshdesk-Integration in injixo hinzuzufügen, benötigst du einen Pro- oder einen Enterprise-Account bei Freshdesk.

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Freshworks**-Kachel auf _Modell wählen_{:.doc-button}.
4. Klicke im Abschnitt **Freshdesk** auf _Integration hinzufügen_{:.doc-button}.

## Freshdesk-Integration einrichten

1. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Gib im Abschnitt **Zugangsdaten** deinen vollständigen Freshdesk-Domainnamen einschließlich der Subdomain ein, z.&nbsp;B. example.freshdesk.com.
3. Gehe zu Freshdesk und kopiere einen gültigen API-Schlüssel eines Benutzers mit der Rolle Account Administrator.
4. Gehe zurück zu injixo und füge den API-Schlüssel in das Feld **API-Schlüssel** ein.
5. Klicke auf _Integration speichern_{:.doc-button}.

## injixo-App installieren

Die Freshdesk-Integration benötigt eine Client-Anwendung. Nachdem du deine Konfiguration gespeichert hast, kannst du auf den Abschnitt **Installiere injixo-App** am Ende der Seite zugreifen.

Um den injixo API-Schlüssel zu erzeugen und zu kopieren, klicke auf _Generieren_{:.doc-button}.

Um die injixo-App in deinem Freshdesk-Konto einzurichten, folge den Anweisungen auf dem Bildschirm. Weitere Informationen findest du auf dem [Freshworks Marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## Freshdesk-Daten in injixo

injixo importiert alle Ticket-Daten aus Freshdesk. Tickets enthalten in der Regel mehrere Unterhaltungen, die zwischen deinen Mitarbeitern und Kunden stattfinden.<br>
Hinweis: injixo kann keine Ticket-Dauer aus Freshdesk importieren. Deshalb siehst du in injixo Forecast keinen AHT-Graphen für Workloads mit Freshdesk-Queues.

### Tickets und Unterhaltungen

In injixo werden alle Unterhaltungen nach dem Freshdesk-Kommunikationskanal, also der Quelle (Source), gruppiert. Eine Unterhaltung kann ein neues Ticket oder eine Antwort auf ein bestehendes Ticket sein.

In injixo werden die Unterhaltungen in einem Freshdesk-Ticket jeweils als eingehende Kontakte gezählt.

Beispiel: Ein Benutzer erstellt ein Ticket per E-Mail. Der Mitarbeiter antwortet und schließt das Ticket. Zwei Tage später wird das Ticket aufgrund einer weiteren E-Mail erneut geöffnet, was zu einer neuen Unterhaltung führt.

Die Anzahl der eingehenden Kontakte in injixo ist normalerweise höher als die Anzahl der in Freshdesk gezählten Tickets.

### Ereignisse aus verschiedenen Kanälen

In einem Freshdesk-Ticket können Antworten in verschiedenen injixo-Queues über den Kanal Cases erfasst werden.

Beispiel: Wenn eine E-Mail-Antwort auf ein Ticket eingeht, wird der Kontakt in einer injixo-Queue angezeigt, die der Freshdesk-Gruppe und dem Source-Namen entspricht. Ein Chat zum gleichen Ticket wird in einer separaten Queue gezählt.

### Namenskonvention für Quell-Queues

injixo erstellt Quell-Queues aus deinen Tickets. Die Namenskonvention dieser Queues hängt davon ab, wie der Datenimport abläuft (initial oder kontinuierlich). Während dieses ersten Imports wird Quell-Queue entsprechend dieser Konvention benannt:

- "Gruppenname + Quellenname + Tickets"
- "Gruppenname + Quellenname + Replies"

Beispiele:

- CustomerService chat Tickets
- CustomerService email Replies
- Unknown group/source Tickets

Ein neues Ticket erzeugt eine Tickets-Queue. Eine Antwort auf eine Anfrage erzeugt eine Replies-Queue, in der auch alle anderen Antworten erfasst werden. Um alle Informationen zu einer Anfrage zu erhalten, musst du sowohl die Anfrage als auch die Replies-Queue durchsuchen.

### Gelöschte Tickets und Spam-Tickets

Der Gruppenname und der Quellenname können nicht bestimmt werden, wenn ein Ticket geändert wird, das bereits gelöscht oder als Spam markiert wurde. Die Quell-Queues mit solchen Tickets werden mit Unknown group/source Tickets oder Unknown group/source Replies gekennzeichnet. Normalerweise spielen diese Queues bei der Schichtplanerstellung für deine Agenten keine Rolle.

## Häufig gestellte Fragen

| Frage                                                                                                                                                                                                  | Antwort                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| injixo zeigt plötzlich keine neuen Freshdesk-Daten mehr an. Unter **Account > Integrationen** wird aber immer noch der Status Operational für meine Freshdesk-Integration angezeigt. Was kann ich tun? | Die injixo-App erhält Freshdesk-Daten und sendet Ereignisse an injixo. Bei einem Kommunikationsfehler zwischen der injixo-App und injixo können Freshdesk-Daten eventuell nicht mehr angezeigt werden. Die Freshdesk-Integration kann solche Kommunikationsfehler nicht erkennen.<br><br>Überprüfe, ob der injixo API-Schlüssel, den du beim Einrichten deiner injixo-App in deinem Freshdesk-Account eingegeben hast, noch gültig ist. Wenn der API-Schlüssel ungültig ist, aktualisiere den injixo API-Schlüssel auf der Installationsseite der injixo-App. Wenn der API-Schlüssel noch gültig ist, wende dich an den injixo-Support. |
