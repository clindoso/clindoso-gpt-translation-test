---
title: Voraussetzungen & Einrichtung
---

Bei der Einrichtung von _injixo Me_{:.menu-item} für die WFM-Pläne **injixo Enterprise on-premise** müssen wir bei jeder Anmeldung eines Mitarbeiters mit der Agenten-Rolle aus der Cloud auf dein Netzwerk zugreifen. Damit fragen wir Daten aus der lokal installierten injixo-Instanz ab, um diese im Browser des Agenten anzuzeigen.

## Netzwerkzugriff konfigurieren

Hier ein Schaubild wie die Kommunikation genau abläuft:

{{ 1 | image: 'Funktionsweise injixo Me und Enterprise Server', '75%' }}

Ein Cluster mit drei möglichen Quell-IP-Adressen steht zur Verfügung:

- 52.16.236.93
- 52.210.14.224
- 52.214.91.145

Teile uns mit, auf welche öffentlich erreichbare IP-Adresse und welchen Port der injixo Me Cloud Server eine TCP-Verbindung öffnen soll. Diese Requests müssen dann zu Deinem lokalen injixo Enterprise Server auf Port 45054 (URL Parameter in isps.cfg) weitergeleitet werden.

## SSL konfigurieren

Um Deine Daten sicher zu übertragen, erlaube ausschließlich {% link_new sichere Verbindungen zum Enterprise Server | support/injixo-enterprise-on-premise/ssl/encrypt-server-connections.md %}. Jegliche Kommunikation zwischen injixo Me und Deinem Firmennetzwerk wird verschlüsselt.

## Wunsch-URL

injixo Me ist über die URL _wunschname.me.injixo.com_ erreichbar. Teile uns Deinen Wunschnamen mit, den wir dann für Dich konfigurieren. Die URL können wir jederzeit anpassen, z.B. wenn sich der Firmennamen ändert.

## Benutzer einrichten

Damit sich der injixo Me Cloud-Server bei Deinem lokalen injixo Enterprise anmelden kann, musst Du in _Administration > System > Benutzerrechte_{:.breadcrumbs} einen Benutzer erstellen. Wähle einen beliebigen Namen und ein starkes Passwort. Ein Hinweis im Kommentarfeld bei der Erstellung hilft, damit dieser Benutzer später nicht unabsichtlich verändert oder gelöscht wird. Ordne dem Benutzer die Benutzergruppe _System_{:.menu-item} zu.
