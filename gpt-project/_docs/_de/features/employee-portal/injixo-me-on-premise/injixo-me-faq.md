---
title: Häufig gestellte Fragen
redirect_from:
  - /de/vergleich-injixo-me-infothek/
redirect_reason: merged articles Dec 2020
---

Das Mitarbeiterportal injixo Me ist der moderne Nachfolger zur Infothek. Hier haben wir einige Fragen gesammelt, die vor allem von injixo Enterprise on-premise Kunden gestellt worden sind.

## Was sind die Vorteile gegenüber der Infothek?

  - Zugriff auch außerhalb des Firmennetzwerks
  - Browserunabhängig (auch auf Smartphone und Tablets nutzbar)
  - Modernes Design & intuitive Bedienung
  - Anzeige eines Teamkalenders (optional)
  - Kalender exportieren
  - Bestehende Zugangsdaten von Agenten weiterhin nutzbar

## Welche Daten von Mitarbeitern werden gespeichert und wie lange?

  - Die Nutzerdaten der Agenten (Mitarbeitername und Aktivitäten-IDs) werden übertragen und temporär für die Dauer der injixo-Me-Session vorgehalten.
  - Auf dem Client wird ein Session-Cookie erzeugt.

## Habe ich einen Einfluss auf die Anzeige der Funktionen in injixo Me?

  - Ja, als Benutzer mit *Admin-Zugriff* hast Du auch Zugriff auf die {% link_new Administration von injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %}.

## Wird mitgeloggt, wann sich welcher Mitarbeiter bei injixo Me angemeldet hat?

Die internen Logdateien enthalten Informationen über Zugriffe auf den Application-Server von injixo Me. Diese sind aber nicht öffentlich zugänglich und auch nicht für die Admin-User auf Deiner Seite einsehbar.

## Der Agent hat keinen Zugriff auf injixo Me oder sieht die Navigationsleiste nicht

Um den Mitarbeitern den vollen Zugriff auf injixo Me zu gewähren, darf durch Deine IT der Zugriff auf die Seite `amazonaws.com` nicht blockiert sein. Ist die Seite blockiert, kann der Agent in der Regel die Navigationsleiste nicht sehen und damit viele Funktionen von injixo Me nicht nutzen.

## Können injixo Me und die Infothek gleichzeitig benutzt werden?

Ja, du kannst injixo Me und die Infothek gleichzeitig nutzen. Die Anmeldung bei injixo Me erfolgt über die von dir definierte Wunsch-URL. Die Infothek ist wie gewohnt über die URL http://\*dein-enterprise-server\*/isps/infothek erreichbar.

## Besteht die Möglichkeit, einen Ping auf die Server des Mitarbeiterportals abzusetzen?

Um einen potenziellen DDoS-Angriff zu verhindern, haben wir diese Möglichkeit ausgeschlossen.
