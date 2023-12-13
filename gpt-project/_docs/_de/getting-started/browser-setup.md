---
title: Browser einrichten
description: Erfahre, wie du deinen Browser für die Arbeit mit injixo einrichtest.
product_label:
  - on-premise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: support/faq/client-installer-errors.md
  - overwrite_title: Add title for untranslated source
    filepath: support/faq/session-timeout-message.md
redirect_from:
  - /Browser/Client Konfiguration/
redirect_reason: Updated filename on 27 July 2023
---

Um mit ActiveX-basierten Features in WFM zu arbeiten, nutze {% link_new Microsoft Edge im Internet Explorer(IE)-Modus | support/faq/configure-edge-internet-explorer-mode.md %}. Du findest eine Liste kompatibler Browser in den {% link_new Systemanforderungen | getting-started/system-requirements.md | #browser-anforderungen %}.

Wenn du nicht die nötigen Rechte hast, um die Browser-Einstellungen zu ändern oder Software zu installieren, wende dich an deine IT-Abteilung.

## Vertrauenswürdige Sites und Sicherheitszonen-Einstellungen konfigurieren

injixo Classic und injixo Enterprise WFM enthalten ActiveX-Steuerelemente. Du musst dem Browser (Edge im IE-Modus) erlauben, diese ActiveX-Steuerelemente auszuführen.

Füge in den Browsereinstellungen alle injixo-Seiten (_\*.injixo.com_) zu den vertrauenswürdigen Seiten hinzu:

1. Öffne das Windows-Startmenü, gib Internetoptionen ein und drücke die Enter-Taste.
2. Wähle auf dem Tab **Sicherheit** die Zone **Vertrauenswürdige Sites** und klicke auf _Sites_{:.doc-button}.
3. Gib im Feld **Diese Webseite zur Zone hinzufügen** https://\*.injixo.com ein.
4. Aktiviere die Checkbox **Für Sites dieser Zone ist eine Serverüberprüfung (https:) erforderlich**.
5. Klicke auf **Hinzufügen**.
6. Klicke auf **Schließen**.

{{ 1 | image: 'Sicherheitseinstellungen', '45%', 'jpg' }}

Passe die Sicherheitszone für die vertrauenswürdigen Sites wie folgt an:

1. Öffne das Windows-Startmenü, gib Internetoptionen ein und drücke die Enter-Taste.
2. Wähle auf dem Tab **Sicherheit** die Zone **Vertrauenswürdige Sites**.
3. Deaktiviere die Checkbox **Geschützten Modus aktivieren**.  
   Hinweis: Diese Checkbox ist in Windows 11 und höher nicht mehr verfügbar.
4. Ändere auf dem Tab **Sicherheit** die Sicherheitsstufe für **Vertrauenswürdige Sites** auf **Mittelhoch** bzw. **Mittel**. Wenn du Mittel wählst, kannst du die Schritte 6-9 überspringen.
5. Klicke auf _OK_{:.doc-button}.
6. Klicke auf _Stufe anpassen_{:.doc-button}.
7. Ändere im Dialogfenster **Sicherheitseinstellungen** folgende Einstellungen:

   | Einstellung                                           | Status             |
   | ------------------------------------------------- | ----------------- |
   | ActiveX-Steuerelemente ausführen, die für Skripting sicher sind | AKTIVIERT           |
   | ActiveX-Steuerelemente und Plug-Ins                  | AKTIVIERT           |
   | Signierte ActiveX Steuerelemente herunterladen                  | Eingabeaufforderung oder AKTIVIERT |
   | Automatische Eingabeaufforderung für ActiveX Steuerelemente          | AKTIVIERT           |

8. Klicke auf _OK_{:.doc-button}.
   Die folgende Meldung erscheint: Sind Sie sicher, dass Sie die Einstellungen für diese Zone ändern möchten?
9. Klicke auf _Ja_{:.doc-button}.
10. Um den Dialog zu schließen, klicke auf _OK_{:.doc-button}.

## injixo-Client-Installation

injixo Classic und injixo Enterprise WFM enthalten ActiveX-Steuerelemente, die {% link_new Microsoft Edge im IE-Modus | support/faq/configure-edge-internet-explorer-mode.md %} und den injixo-Client erfordern.

Wenn du beim Anmelden bei oder Verwenden von injixo eine Fehlermeldung siehst:

- verwende einen {% link_new kompatiblen Browser | getting-started/system-requirements.md | #browser-anforderungen %}.
- installiere den injixo-Client (wie unten beschrieben).

### Automatische Client-Installation (WFM-Startseite)

Wenn du die oben beschriebenen Browsereinstellungen verwendest, installiert sich der Client automatisch, wenn du WFM aufrufst.

1. Gehe zu _WFM_{:.menu-item}.
2. Warte bis der Download beendet ist und die Client-Installation beginnt.
3. Der Browser zeigt diese Meldung an: Diese Webseite möchte das folgende Add-on ausführen: 'injixo Enterprise' von 'InVision AG'.<br>Wenn diese Meldung nicht erscheint, wende dich an deine IT-Abteilung.
4. Klicke auf _Installieren_{:.doc-button}, um die erforderlichen Add-ons zu installieren.
5. Klicke auf _Installieren_{:.doc-button}, um den Client zu installieren.

Wenn die Installation erfolgreich war, kannst du auf ActiveX-Komponenten zugreifen.

### Manuelle Client-Installation

Installiere den Client manuell, z.&nbsp;B. in injixo WFM Enterprise On-premise oder wenn die automatische Installation nicht funktioniert.

Hinweis: Wenn du ein Programm zur Softwareverteilung verwendest, führe das Installationsprogramm für den Benutzer aus, der später auf dem Computer angemeldet sein wird, z.&nbsp;B. mit Microsofts msiexec.exe mit der Option runas /user.

1. Lade den [aktuellsten injixo-Client](https://downloads.injixo.com/de#client) herunter.
2. Um den MSI-Installer auszuführen, klicke auf _Ausführen_{:.doc-button}.
3. Um fortzufahren, klicke auf _Weiter_{:.doc-button}.
4. (Optional) Ändere den Installationspfad.
5. Wenn der Computer von mehreren injixo-Benutzern verwendet wird, wähle **Jeder**.
6. Um fortzufahren, klicke auf _Weiter_{:.doc-button}.
7. Um die Installation auszuführen, klicke auf _Installieren_{:.doc-button}.
   Die folgende Meldung erscheint: Möchten Sie zulassen, dass Software auf diesem Computer durch das folgende Programm installiert wird?
8. Klicke auf _Ja_{:.doc-button}, um die Meldung zu bestätigen.

Wenn die Installation erfolgreich war, kannst du auf ActiveX-Komponenten zugreifen.
