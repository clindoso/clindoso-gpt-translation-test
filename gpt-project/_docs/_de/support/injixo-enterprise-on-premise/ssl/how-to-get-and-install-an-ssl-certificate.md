---
title: SSL-Zertifikat erzeugen und installieren
product_label:
  - on-premise
---

Ein Zertifikat für den Server bzw. Deine Domäne wird normalerweise von Deiner IT bereitgestellt und installiert. Natürlich kannst Du, falls Dein Unternehmen noch keines nutzt, ein Zertifikat bei einer Zertifizierungsstelle käuflich erwerben. Alternativ kannst Du ein selbst erstelltes Zertifikat für Deinen Server nutzen.

## Erstellung eines Zertifikats via OpenSSL

1. Lade Dir [OpenSSL](https://www.openssl.org) herunter.
2. Erstelle einen [privaten Schlüssel](https://www.openssl.org/docs/man1.1.1/man1/genrsa.html) mit einer Länge von 2048 bits:  
   `openssl.exe genrsa -des3 -out test.key`
3. Erstelle ein [Zertifikat](https://www.openssl.org/docs/man1.1.1/man1/openssl-req.html):  
   `openssl.exe req -new -x509 -days 1001 -key test.key -out test.cer`
4. Exportiere das Zertifikat im [PKCS12 Format](https://www.openssl.org/docs/man1.1.1/man1/openssl-pkcs12.html):  
   `openssl.exe pkcs12 -export -in test.cer -inkey test.key -out test.pfx`

> Hinweis
>
> Selbst erstellte Zertifikate müssen im vertrauenswürdigen Zertifikatsspeicher (Trusted Certificate Store) gespeichert werden.

## Installation eines Zertifikats

Installiere das erstellte pkcs12 Zertifikat (.pfx Datei) im Zertifikatsspeicher.

Nutze dazu `mmc.exe` bzw. `certmgr.msc`, gehe wie folgt vor:

1. Öffne die Microsoft Management Console (Start > Ausführen > mmc.exe).
2. Wähle Datei und klicke auf Add/Remove Snap-in.
3. Wähle Hinzufügen und dann das Zertifikat-Snap-In.
4. Wähle das Computer-Konto und dann lokaler Computer im Assistenten aus.
5. Navigiere zu den Zertifikaten (LocalComputer).
6. Selektiere einen Store, z.B. Vertrauenswürdige Stamm-Zertifikate.
7. Mit einem Rechtsklick auf den Store hast Du die Möglichkeit unter _All Tasks_ nun _Import_ auszuwählen, folge dann dem Assistenten und installiere die .pfx Datei.
