---
title: Passwortregeln und Session-Timeout festlegen
description: Lerne, wie Du Passwortregeln definierst und das Session-Timeout erhöhst.
product_label:
  - on-premise
---

In diesem Artikel lernst Du:

- welche Passwortregeln für injixo Enterprise on-premise existieren.
- wie Du die Passwortregeln anpasst.
- wie Du das Session-Timeout festlegst.

In injixo Enterprise on-premise kannst Du eigene Passwortregeln festlegen. injixo Essential, Advanced und Enterprise WFM bieten diese Möglichkeit aktuell nicht.

## Passwortregeln anpassen

1. Öffne die Datei **isps.cfg** im Server-Verzeichnis Deiner Installation.
2. Suche folgenden Abschnitt:

   ```
   [4b6b22f0-c50d-11d3-8441-00a0c9d6cabb]
   ShortName               = "eSystem"
   ```

3. Füge die Parameter und Werte für die gewünschten Passwortregeln hinzu.<br><br>

   | Parameter             | Details                                                                                                                                                                         | Wertebereich |
   | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
   | PasswordMinLength     | Minimale Passwort-Länge. Wert 0 (Standardwert) schaltet die Einstellung aus und erlaubt 1 bis 12 Zeichen)                                                                       | 0 - 12       |
   | PasswordMinAlphaChar  | Minimale Anzahl alphabetischer Zeichen (A-Z und a-z)                                                                                                                            | 0 - 12       |
   | PasswordMinNumChar    | Minimale Anzahl Ziffern                                                                                                                                                         | 0 - 9        |
   | PasswordMinCtrlChar   | Minimale Anzahl Sonderzeichen (nicht numerischen Zeichen oder Buchstaben). Die Zeichen `:` und `@` sind nicht erlaubt.                                                          | 0 - 12       |
   | PasswordUserNameCheck | Legt fest, ob das Passwort den Benutzernamen enthalten darf. Groß- und Kleinschreibung wird nicht geprüft.                                                                      | 0 - 1        |
   | EnableMultipleLogon   | Legt fest, ob ein Benutzer sich bei verschiedenen Rechnern gleichzeitig anmelden darf.                                                                                          | 0 - 1        |
   | MaxFailLogon          | Anzahl fehlgeschlagener Anmeldeversuche, bevor der Benutzer gesperrt wird. Administratoren können nur durch andere Administratoren oder einen Dienst-Neustart entsperrt werden. | 0 - 10       |
   | PasswordMaxAge        | Gültigkeit des Passwort in Tagen. Wenn das Passwort abgelaufen ist, wird der Benutzer informiert. Passwörter für Benutzer der Gruppe Administratoren laufen nicht ab.           | 0 - 3650     |
   | PasswordForceChange   | Legt fest, ob ein Passwort nach Ablauf der Gültigkeit geändert werden muss.                                                                                                     | 0 - 1        |
   | UserMaxNoLoginDays    | Zeitraum in Tagen, nach dem der Benutzerzugriff deaktiviert wird, wenn dieser sich nicht mehr angemeldet hat. Nur Administratoren können den Zugriff wieder aktivieren.         | 0 - 3650     |
   | PasswordHistoryLength |  Anzahl unterschiedlicher Passwörter, bevor ein altes Passwort wiederverwendet werden kann.                                                                                     | 0 - 100      |

4. Speichere die Änderungen.
5. Starte den InVision Enterprise Dienst neu, um die Änderungen zu übernehmen.

## Session-Timeout festlegen

1. Öffne die Datei **isps.cfg** im Server-Verzeichnis Deiner Installation.
2. Suche folgenden Abschnitt:

   ```
   [4b6b22f0-c50d-11d3-8441-00a0c9d6cabb]
   ShortName               = "eSystem"
   ```

   Folgende Parameter sind in der Datei _isps.cfg_ voreingestellt:

   | Parameter       | Details                                                                                             | Wertebereich |
   | --------------- | --------------------------------------------------------------------------------------------------- | ------------ |
   | MaxSessionTime  |  Zeit in Sekunden, die ein Benutzer inaktiv sein kann. Standardwert: 1800 (30 Minuten)              | 0 - 86400    |
   | MaxInfothekTime | Zeit in Sekunden, die ein Benutzer in der Infothek inaktiv sein kann. Standardwert: 300 (5 Minuten) | 0 - 86400    |

3. Passe die Werte an, um das Session-Timeout für Planer und Infothek-Benutzer festzulegen.
4. Speichere die Änderungen.
5. Starte den InVision Enterprise Dienst neu, um die Änderungen zu übernehmen.

## Beispiel (Session-Timeouts und Passwortregeln)

```
[4b6b22f0-c50d-11d3-8441-00a0c9d6cabb]
ShortName = "eSystem"
MaxSessionTime = 30
MaxInfothekTime = 300
PasswordMinLength = 8
PasswordMinAlphaChar = 1
PasswordMinNumChar = 1
PasswordMinCtrlChar = 1
PasswordUserNameCheck = 1
PasswordMaxAge = 28
PasswordForceChange = 1
UserMaxNoLoginDays = 28
PasswordHistoryLength = 3
EnableMultipleLogon = 0
MaxFailLogon = 5
```
