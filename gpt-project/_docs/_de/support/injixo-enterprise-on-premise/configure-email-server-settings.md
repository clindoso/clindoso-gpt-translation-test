---
title: E-Mail-Server-Einstellungen konfigurieren
product_label:
  - on-premise
promote-service: general
---

In injixo Enterprise on-premise musst du einen einen E-Mail-Server konfigurieren, wenn du Reports als E-Mails senden möchtest. injixo Cloud-Versionen sind bereits für den E-Mail-Versand vorkonfiguriert.

## Server-Konfiguration anpassen

1. Öffne die Datei isps.cfg im Server-Verzeichnis deiner Installation.
2. Füge die folgenden Zeilen in die Datei isps.cfg ein:

   ```
   [22bafe6c-fc65-44a4-aeb6-b60281e0b2fc]
   ShortName = ivemail
   SMTPServer = smtp.yourprovider.com
   SMTPTimeout = 60
   SMTPFromEmail = YourValidSenderMailAdress@yourprovider.com
   SMTPSecureMode = TLS
   SMTPPort = 465
   SMTPUser = yourValidSMTPUser@yourprovider.com
   SMTPPwd = yourValidPassword
   SMTPTag = "Custom Subject"
   SMTPVerifyCert = 1
   ```

3. Ersetze die Werte mit den Daten deines E-Mail-Servers.
4. Um die Einstellungen zu übernehmen, starte den Enterprise-Server-Dienst neu.

   Wenn du jetzt einen Report per E-Mail versendest, öffnet sich ein Status-Report. Wenn die E-Mail versendet werden konnte, wird der Status OK angezeigt. Der versendete Report befindet sich im Anhang der E-Mail. Wenn die E-Mail nicht versendet werden konnte, enthält der Report die [Fehlermeldungen](#fehlermeldungen) des E-Mail-Servers.

## E-Mail-Server-Parameter

| Parameter      | Details                                                                                       |
| -------------- | --------------------------------------------------------------------------------------------- |
| SMTPServer     | Adresse des E-Mail-Servers                                                                    |
| SMTPTimeout    | Timeout für die Verbindung zum E-Mail-Server                                                  |
| SMTPFromEmail  | Absender-E-Mail-Adresse, die in E-Mails aus injixo verwendet wird.                            |
| SMTPSecureMode | Gültige Werte für die Verschlüsselung sind SSL, TLS, PLAIN (keine Verschlüsselung)            |
| SMTPPort       | Port des E-Mail-Servers, abhängig vom SMTPSecureMode: TLS nutzen 465 oder 587, PLAIN nutzt 25 |
| SMTPUser       | Benutzer zur Anmeldung am E-Mail-Server                                                       |
| SMTPPwd        | Passwort für den SMTPUser                                                                     |
| SMTPTag        | (Optional) Präfix für den Betreff der gesendeten E-Mails                                      |
| SMTPVerifyCert | (Optional) Wert 0 schaltet die Verifizierung der Zertifikatskette aus.                        |

## Eigenes Zertifikat für den E-Mail-Versand

Erfordert dein E-Mail-Server ein eigenes Zertifikat, füge das Zertifikat als Text in die Datei .\\certificates\\cacert.pem ein. Speichere die bearbeitete Datei.

> Warnung
>
> Server-Updates überschreiben die Datei cacert.pem. Deshalb musst du die Datei nach jedem Update erneut bearbeiten.<br>Um daran erinnert zu werden, wenn du neue Updates entpackst, aktiviere den Schreibschutz für die Datei cacert.pem. Kopiere nach der Bearbeitung die gesicherte Datei cacert.pem wieder in den Ordner /certificates.

## Fehlermeldungen

Konnte die E-Mail mit dem ausgewählten Report nicht versendet werden, enthält der erzeugte Status-Report WSA_SELECT Meldungen. Eindeutige Fehlermeldungen, wie z.&nbsp;B. darüber, dass die Parameter SMTPUser oder SMTPPwd nicht gesetzt sind, werden in der folgenden Übersicht nicht aufgeführt.

| Fehler                                            | Details                                                                                                                                                            |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| certificate check failed (19) self signed certificate in certificate chain | Selbst-signierte Zertifikate des E-Mail-Servers können nicht auf Echtheit überprüft werden. Um die Prüfung zu umgehen, setze den Parameter SMTPVerifyCert auf den Wert 0. |
| certificate check failed (20) unable to get local issuer certificate | Ein Zertifikat konnte nicht aus dem Zertifikatsspeicher gelesen werden. Der Grund dafür ist meist eine unvollständige Zertifikatskette. Stelle sicher, dass die gesamte Zertifikatskette vorhanden ist. |
| address evaluation from hostname failed           | Allgemeiner Netzwerkfehler. Die aktuell konfigurierte Adresse des E-Mail-Servers stimmt nicht.                                                                     |
| keyword STARTTLS unsupported                      | Dein E-Mail-Server unterstützt STARTTLS nicht. Prüfe den E-Mail-Server oder verwende SMTPSecureMode=PLAIN.                                                                            |
| SSL error - unable to find CA root certificate file           | Du hast SMTPSecureMode=TLS (oder SSL) und SMTPVerifyCert=1 konfiguriert, aber das Zertifikat wurde in der Datei cacert.pem nicht gefunden.                         |
