---
title: Xlink-Sicherheitseinstellungen
product_label:
  - on-premise
---

Der Xlink ist das Verbindungsglied zwischen der ACD und injixo. Alle Konfigurationsoptionen des Xlinks sind lokal im Xlink-Ordner selbst gespeichert. Der Benutzer, der den Xlink startet, hat jedoch nicht immer auch Schreibrechte auf die Dateien im Xlink-Ordner.

Bei strikten Sicherheitsrichtlinien in Deinem Unternehmen, musst Du ggf. die lokale Sicherheitsrichtlinie des Computers angepassen, auf dem der Xlink installiert ist.

## Sicherheitseinstellungen konfigurieren

Suche zuerst den _Xlink_ Ordner. Oft ist der Xlink im Ordner `Programme (x86)` oder direkt auf Laufwerk `C:\` oder `D:\` installiert.

{{ 1 | image: 'Xlink Ordner auswählen', '75%' }}

Rechts-klicke auf den _Xlink Ordner_ und wähle den Menüpunkt _Eigenschaften_{:.menu-item}.

{{ 2 | image: 'Wähle Eigenschaften aus', '75%' }}

Als nächstes wählst Du den Tab _Sicherheit_{:.menu-item} und klickst danach auf _Bearbeiten_{:.doc-button}.

{{ 3 | image: 'Gehe auf den Tab Sicherheit', '75%' }}

{{ 4 | image: 'Klicke auf Bearbeiten', '75%' }}

Hier wählst Du die Option _Benutzer_{:.menu-item} aus. Der Benutzername mit dem Du aktuell bei Windows angemeldet bist, sollte in den Klammern hinterlegt sein.

{{ 5 | image: 'Wähle die Option Benutzer', '75%' }}

Wähle die Checkbox _Vollzugriff_{:.menu-item} aus und bestätige die Auswahl mit dem _Übernehmen_{:.doc-button}-Button.

{{ 6 | image: 'Vollzugriff auswählen', '75%' }}

{{ 7 | image: 'Abschließend die Änderungen übernehmen', '75%' }}

Anschließend kannst Du die Dialoge mit dem _OK_{:.doc-button}-Button schließen.
