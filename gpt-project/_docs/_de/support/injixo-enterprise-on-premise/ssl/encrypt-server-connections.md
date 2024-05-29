---
title: Server-Verbindungen verschlüsseln
redirect_from:
  - /de/ies-ssl-encryption/
  - /de/ihs-ssl-encryption/
  - /de/ssl/
redirect_reason: Renamed file in April 2023
product_label:
  - on-premise
---

Du kannst sichere TLS-Verbindungen für den InVision-Enterprise-Server und den InVision-HTTP-Server konfigurieren. Der Enterprise-Server ist dann zusätzlich oder ausschließlich über iwfms:// erreichbar, der HTTP-Server über https://.

Installiere ein {% link_new Zertifikat | support/injixo-enterprise-on-premise/ssl/how-to-get-and-install-an-ssl-certificate.md %} im PKCS12-Format (Dateiendung .pfx) auf dem Server und passe deine Konfiguration an.

Details zu notwendigen Konfigurationsänderungen und Parametern findest du im [Administrator Compendium](https://downloads.injixo.com).

## Enterprise-Server-Konfiguration anpassen

1. Öffne die Datei isps.cfg im Server-Verzeichnis.

2. Passe den Abschnitt **[InVision Enterprise Server]** an. Die folgende Beispielkonfiguration kann dir dabei helfen:

   ```
   ; ServerPort existiert bereits, der Wert 0 lässt keine normalen Verbindungen mehr zu
   ; SSLCertificateStore definiert den Windows-Zertifikatsspeicher. Erlaubte Werte: MY, ROOT, TRUST, CA
   ; Standardmäßig verwendet der Server den SHA1-Algorithmus. Andere Werte findest du im Administor Compendium.

   [InVision Enterprise Server]
   ServerPort                  = 0
   SSLPort                     = 45054
   SSLCertificateStore         = "ROOT"
   SSLCertificateStoreLocation = "LocalMachine"
   SSLCertificate              = "myTestCertificate"
   SSLProtocols                = "TLS11, TLS12"
   SSLAlgorithms               = "SHA1"
   ```

3. Füge in den Abschnitten **[IES System Local]** und **[InVision JobProcessor]** iwfms:// hinzu:

   ```
   [IES System Local]
   Url = "iwfms://*myservernameOrIpAdress*:45054"
   ```

   ```
   [InVision JobProcessor]
   Url = "iwfms://*myservernameOrIpAdress*:45054"
   ```

4. Speichere deine Änderungen.

5. Um die Konfiguration anzuwenden, starte den InVision-Enterprise-Dienst neu.

## JobProcessor, Xlink und andere Komponenten ändern

Wie oben beschrieben, musst du auch für andere Komponenten, die sich mit dem Server verbinden, die Konfigurationsdatei anpassen. Dazu gehören z.&nbsp;B. Xlink, AutoScheduler Server oder Report- und Importserver. Füge iwfms:// vor einem Servernamen oder einer IP-Adresse ein.

```
[IES System Local]
Url = "iwfms://*myservernameOrIpAdress*:45054"
```

## Fehlermeldungen

Mögliche Fehlermeldungen in der Logdatei des Servers (ies64.log):

|                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| unable to finish SSL handshake (code 0x80090331)                                                       | Der Fehler bedeutet SEC\*E_ALGORITHM_MISMATCH. Der konfigurierte Algorithmus passt nicht zum Zertifikat. Vergleiche den konfigurierten Algorithmus (Parameter SSLAlgorithms) und den Algorithmus des Zertifikats.                                                                                                                                                                                                                             |
| unable to finish SSL handshake (code 0x80090308)                                                       | Komponenten versuchen ohne SSL auf den Server zuzugreifen. Füge bei der betroffenen Komponente iwfms:// vor der aktuellen URL ein.                                                                                                                                                                                                                                                                                                            |
| unable to load credentials (code 0x8009030e)                                                           | Mögliche Ursachen:<br>- Das Zertifikat hat nicht das PKCS12-Format, aber du kannst [das Zertifikat konvertieren](https://social.technet.microsoft.com/Forums/en/configmgrgeneral/thread/26d35e34-c6b6-4161-9964-b306fa8c0bfe).<br>- Der für den Dienst konfigurierte Benutzer kann nicht auf Zertifikatsspeicher zugreifen.<br>- Der Parameter _SSLMaxCipherLength_ in der Datei isps.cfg ist falsch konfiguriert, ändere den Wert auf 0.<br> |
| unable to find certificate named "xyz" in store "ROOT" - The object or the property could not be found | Mögliche Ursachen::<br>- Das Zertifikat wurde nicht importiert.<br>- Das Zertifikat wurde in den falschen Zertifikatsspeicher importiert.<br>- Die Datei isps.cfg enthält nicht den korrekten Namen des Zertifikats. Nutze den den Wert des Feldes issued_by oder den Friendly Name.<br>                                                                                                                                                      |

OpenSSL stellt mit dem [OpenSSL s_client Parameter](https://www.openssl.org/docs/man1.0.2/man1/openssl-s_client.html) eine Art generischen SSL Client zur Verfügung, mit welchem du im Fehlerfall das Zertifikat prüfen kannst. `openssl s_client -connect ip:port`

## InVision-HTTP-Server anpassen

1. Öffne die Datei isps.cfg im Server-Verzeichnis.

2. Passe den Abschnitt **[InVision HTTP Server]** an. Die folgende Beispielkonfiguration kann dir dabei helfen:

   ```
   ; HTTPPort existiert bereits, der Wert 0 heißt, dass keine normalen Verbindungen zulässig sind.
   ; SSLCertificateStore definiert den Store, unterstützt werden MY, ROOT, TRUST, CA
   ; Standardmäßig verwendet der Server den SHA1-Algorithmus. Andere Werte findest du im Administor Compendium.

   [InVision HTTP Server]
   HTTPPort                    = 0
   HTTPSPort                   = 443
   HTTPSBackLog                = 200
   SSLAlgorithms               = "SHA1"
   SSLCertificateStore         = "ROOT"
   SSLCertificateStoreLocation = "CurrentUser"
   SSLCertificate              = "certificatename"
   SSLMaxCipherLength          = 0
   SSLMinCipherLength          = 0
   SSLProtocols                = "TLS1, TLS12"
   ```

3. Speichere deine Änderungen.

4. Starte den Dienst neu, um die Konfiguration anzuwenden.  
   Die Anmeldung funktioniert jetzt über https (https://dein-servername:port).
