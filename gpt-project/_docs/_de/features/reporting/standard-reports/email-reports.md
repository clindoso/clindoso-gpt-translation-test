---
title: Reports per E-Mail versenden
redirect_from:
  - /de/controlling-reports-via-email/
---

Reports können ganz einfach per E-Mail an bestimmte Gruppen oder einzelne Mitarbeiter versendet werden. Im Artikel {% link_new Erstellen von Reports | features/reporting/standard-reports/creating-reports.md %} haben wir Dir bereits erklärt, wie Du die Parameter für die Reporterstellung definierst. Als letzten Schritt vor dem eigentlichen Erzeugen des Reports kannst Du den E-Mail-Versand konfigurieren.

injixo Enterprise User können Reports per E-Mail versenden, wenn ein E-Mail-Server konfiguriert ist. Weitere Informationen zur SMTP Server Konfiguration findest Du {% link_new hier | support/injixo-enterprise-on-premise/configure-email-server-settings.md %}

Nach dem Senden der E-Mail erhältst Du anstelle des Reports einen Statusbericht mit Empfangsbestätigung.

## Report als E-Mail verschicken an

Konfiguriere, ob und wie der Report per E-Mail verschickt werden soll, die verfügbaren Optionen sind:

- **Kein E-Mail-Versand**, standardmäßig ausgewählt.
- **Ausgewählte Empfänger**, wähle die gewünschten Mitarbeiter als Empfänger aus. Wähle die E-Mail-Adressen der Mitarbeiter aus oder gib eine oder mehrere E-Mail-Adressen manuell ein. Jeder Adressat erhält einen identischen Report.
- **Mitarbeiter der Auswahlliste**, wähle Mitarbeiter aus der Auswahlliste aus, um den Report an ihre hinterlegte E-Mail-Adresse zu senden. Diese Option ist nur für Tages- und Wochenpläne verfügbar.
- **Jeden Mitarbeiter persönlich**, wähle Mitarbeiter aus der Auswahlliste aus, um einen bestimmten Bericht an ihre hinterlegte E-Mail-Adresse zu senden. Jeder Mitarbeiter erhält separat einen individuellen Bericht, der nur die persönlichen Mitarbeiterdaten enthält. Diese Option ist für die folgenden Berichte verfügbar:
  - Mitarbeiterarbeitsplan I (Liste)
  - Mitarbeiterarbeitsplan I (Liste) (ohne Pausen)
  - Mitarbeiterarbeitsplan II (Liste)
  - Mitarbeiterarbeitsplan III (Graph)
  - Wochenplan II (ohne Pausen)
  - Wochenplan II (ohne Pausen) (ohne Ganztagsaktivitäten)

## E-Mail-Adresse

Hier bestimmst Du, an welche E-Mail-Adresse der Report verschickt werden soll. Mögliche Optionen sind `injixo Login (E-Mail)`/E-Mail 1, E-Mail 2 oder beide einem Mitarbeiter unter _Administration > Scheduling > Mitarbeiter_{:.breadcrumbs} eingetragenen E-Mail-Adressen.

In injixo Enterprise on-premise heisst das `injixo Login (E-Mail)` Feld `E-Mail 1`.

## Anonyme Auswertung

Hier bestimmst Du, ob Reports anonymisiert ausgegeben werden sollen.
Bei Auswahl des Eintrages _Ja_{:.doc-button} erscheinen in den Reports keine Mitarbeiternamen und Personalnummern.
Sie werden durch Platzhalter ersetzt. Die Sortierung innerhalb der Reports erfolgt nach Mitarbeiter-ID.
