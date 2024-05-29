---
title: Zwei-Faktor-Authentifizierung (2FA) verwenden
product_label:
  - essential
  - advanced
  - enterprise
description: Erfahre, wie du die Zwei-Faktor-Authentifizierung für deinen Account aktivieren und deaktivieren kannst.
---

## Was ist die Zwei-Faktor-Authentifizierung?

Die Zwei-Faktor-Authentifizierung (2FA) fügt deinen Online-Accounts eine Sicherheitsebene hinzu. Um dich bei deinem Account anzumelden, wenn 2FA aktiv ist, benötigst du:

- deine Anmeldedaten
- ein zusätzliches Passwort, das von einem anderen Gerät erzeugt wurde

> Aktiviere schnellstmöglich 2FA für deinen injixo-Account, um die Sicherheit zu erhöhen.

## Voraussetzung: Installiere eine Authenticator-App

injixo unterstützt die in der folgenden Tabelle aufgeführten Authenticator-Apps.  
Wenn du ein Android-Smartphone verwendest, lade die gewünschte App aus dem Google Play Store herunter. Wenn du ein iPhone verwendest, lade die gewünschte App aus dem Apple App Store herunter.

|-------|--------|---------|
| Google Authenticator | [Apple App Store](https://apps.apple.com/us/app/google-authenticator/id388497605) | [Google Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) |
| Microsoft Authenticator | [Apple App Store](https://apps.apple.com/us/app/microsoft-authenticator/id983156458) | [Google Play Store](https://play.google.com/store/apps/details?id=com.azure.authenticator) |
| Authy | [Apple App Store](https://apps.apple.com/us/app/authy/id494168017) | [Google Play Store](https://play.google.com/store/apps/details?id=com.authy.authy) |

## 2FA für deinen Account aktivieren

Um 2FA für deinen Account zu aktivieren, benötigst du Zugriff auf ein Hauptgerät (z.&nbsp;B. einen Computer) und auf dein privates Gerät.  
Gehe auf deinem Computer bzw. Hauptgerät wie folgt vor:

1. Melde dich bei injixo an und klicke oben rechts in der Navigationsleiste auf deinen Benutzernamen.
2. Klicke auf den Tab **Sicherheit**.
3. Klicke auf _2FA aktivieren_{:.doc-button}.
4. Gib dein Passwort ein.
5. Klicke auf _Fortfahren_{:.doc-button}.  
   Die Seite **Zwei-Faktor-Authentifizierung aktivieren** öffnet sich. Dort siehst du, welche Schritte du als nächstes ausführen musst.

Führe auf deinem privaten Gerät die Schritte aus, die auf der Seite Zwei-Faktor-Authentifizierung aktivieren aufgeführt sind:

1. Installiere eine der [unterstützten Authenticator-Apps](#voraussetzung-installiere-eine-authenticator-app).
2. Öffne die Authenticator-App auf deinem Gerät und füge ein neues Konto für injixo hinzu.  
    Wähle dazu eine der folgenden Optionen:
   - Scanne mit der Authenticator-App den QR-Code auf der Seite **Zwei-Faktor-Authentifizierung aktivieren**.
   - Gib den Setup-Key, der auf der Seite **Zwei-Faktor-Authentifizierung aktivieren** angezeigt wird, in die Authenticator-App ein.  
     Deine Authenticator-App ist nun eingerichtet und beginnt, Einmal-Passwörter zu erzeugen.

Gehe auf deinem Computer bzw. Hauptgerät wie folgt vor:

1. Gib auf der Seite **Zwei-Faktor-Authentifizierung aktivieren** ein Einmal-Passwort in das Feld **Einmal-Passwort** ein.
2. Klicke auf _Fortfahren_{:.doc-button}.
3. Speichere die Backup-Codes oder lade sie als Datei herunter. Klicke auf _Herunterladen_{:.doc-button} oder _Kopieren_{:.doc-button}. Wenn du keine Backup-Codes siehst, wurden sie für dein Unternehmen deaktiviert. <!-- feature flag -->

   > Bewahre deine Backup-Codes an einem sicheren Ort auf
   >
   > Wenn du den Zugriff auf dein privates Gerät verlierst, kannst du dich nur noch mit einem Backup-Code bei deinem Account anmelden.<br>Verwahre deine Backup-Codes an einem sicheren Ort, z.&nbsp;B. einem Passwort-Manager oder drucke sie aus und sorge dafür, dass nur du darauf zugreifen kannst.

4. Aktiviere die Checkbox **Ich habe meine Backup-Codes sicher abgespeichert.**
5. Klicke auf _2FA aktivieren_{:.doc-button}.  
    Du erhältst eine Bestätigungsmail, die dich über die 2FA-Aktivierung informiert.  
   Ab sofort brauchst du sowohl deine Anmeldedaten als auch ein Einmal-Passwort, um dich bei injixo anzumelden.

## Anmeldung bei aktivierter 2FA

1. Gib deine E-Mail-Adresse und dein Passwort auf der Anmeldeseite von injixo ein.
2. Gib das von deiner Authenticator-App erzeugte Einmal-Passwort ein.  
   Jedes Einmal-Passwort ist 30&nbsp;Sekunden lang gültig. Danach erzeugt die App ein neues.
3. Klicke auf _Überprüfen_{:.doc-button}, um den Anmeldevorgang abzuschließen.

Wenn du dich nicht anmelden kannst, überprüfe auf der Authenticator-App, ob das von dir eingegebene Einmal-Passwort noch gültig ist. Falls es nicht mehr gültig ist, gib einfach ein neues Einmal-Passwort ein.  
Solltest du dich dann immer noch nicht anmelden können, führe folgende Schritte aus, um dich mit einem Backup-Code anzumelden.

### Mit einem Backup-Code anmelden

Wenn du 2FA für deinen Account einrichtest, erhältst du 10&nbsp;Backup-Codes. Wenn du keinen Zugriff auf dein privates Gerät hast, kannst du dich mit einem deiner Backup-Codes bei injixo anmelden.

> Hinweis
>
> Melde dich nur im Notfall mit einem Backup-Code an. Du kannst jeden Backup-Code nur einmal verwenden. Standardmäßig solltest du dich immer mit einem Einmal-Passwort anmelden.

Um dich mit einem Backup-Code statt eines Einmal-Passworts anzumelden, gehe wie folgt vor:

1. Gib deine E-Mail-Adresse und dein Passwort auf der Anmeldeseite von injixo ein.
2. Klicke auf den Backup-Code-Link unterhalb des Feldes **Einmal-Passwort**.
3. Gib einen der 10-stelligen Backup-Codes in das Feld **Backup-Code** ein, um die Anmeldung abzuschließen.
4. Klicke auf _Überprüfen_{:.doc-button}, um den Anmeldevorgang abzuschließen.

<!-- a tag required. configured name used in injixo UI link -->

### Ohne privates Gerät und Backup-Codes anmelden

Wenn du dich nicht mit 2FA anmelden kannst und auch keinen Zugriff auf deine Backup-Codes hast, wende dich an einen Benutzer mit Admin-Zugriff. Diese können 2FA für deinen Account deaktivieren. Dann kannst du dich ohne Einmal-Passwort bei deinem Account anmelden und die 2FA-Einstellungen neu einrichten.

## 2FA auf einem neuen privaten Gerät verwenden

Um ein neues Gerät verwenden zu können, über das du Einmal-Passwörter erzeugst, musst du 2FA für deinen Account vorübergehend deaktivieren und dann mit deinem neuen Gerät&nbsp;[erneut aktivieren](#2fa-für-deinen-account-aktivieren).

Wenn du die Zwei-Faktor-Authentifizierung nicht selbst deaktivieren kannst, bitte einen Benutzer mit Admin-Zugriff, sie für deinen Account zu deaktivieren.

## 2FA für deinen Account deaktivieren

> Hinweis
>
> Die Deaktivierung von 2FA wird nicht empfohlen. Wenn die Zwei-Faktor-Authentifizierung für deinen Account erzwungen wurde, kannst du sie nicht selbst deaktivieren.

1. Melde dich bei injixo an und klicke oben rechts in der Navigationsleiste auf deinen Benutzernamen.
2. Klicke auf den Tab **Sicherheit**.  
   Oben auf der Seite siehst du den aktuellen Status deiner 2FA-Einstellungen.
3. Klicke auf _2FA deaktivieren_{:.doc-button}.
4. Gib dein Passwort ein.
5. Klicke auf _Fortfahren_{:.doc-button}, um die Deaktivierung zu bestätigen.

Du erhältst eine Bestätigungsmail, die dich über die 2FA-Deaktivierung informiert. Von nun an kannst du dich wieder ohne Einmal-Passwort anmelden.

> Du hast die 2FA-Deaktivierungsmail erhalten, aber 2FA nicht selbst deaktiviert?
>
> Prüfe deinen Account gemeinsam mit einem Admin aus deinem Unternehmen. Ändere ggf. dein Passwort.
