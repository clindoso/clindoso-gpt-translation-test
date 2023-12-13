---
title: 2FA verwalten
product_label:
  - essential
  - advanced
  - enterprise
description: Erfahre, wie du 2FA für die Accounts deiner Mitarbeiter aktivierst und deaktivierst.
redirect_from:
  - /de/2fa/
redirect_reason: Updated filename on 14 July 2023
---

> Nur Benutzer mit Admin-Zugriff können die Zwei-Faktor-Authentifizierung (2FA) für andere Benutzer verwalten.

## 2FA-Einstellungen anderer Benutzer einsehen

Um den aktuellen 2FA-Status anderer Benutzer einzusehen, gehe wie folgt vor:
1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. In der **2FA**-Spalte auf der rechten Seite zeigt ein Schild-Icon den 2FA-Status für jeden Benutzer an. Bewege den Mauszeiger darüber, um weitere Informationen anzuzeigen.
  - Rotes Icon {% icon 2FA-red | icon-only %}: 2FA ist nicht aktiv.
  - Oranges Icon mit Ausrufezeichen {% icon 2FA-orange | icon-only %}: 2FA wurde für den Benutzer erzwungen. Der Benutzer muss 2FA bei der nächsten Anmeldung aktivieren.
  - Grünes Icon mit Häkchen {% icon 2FA-green | icon-only %}: 2FA ist aktiv.

## 2FA-Aktivierung für andere Benutzer erzwingen
Du kannst erzwingen, dass andere Benutzer 2FA aktivieren. Dies hat folgende Konsequenzen:

- Benutzer können sich nicht anmelden, wenn sie 2FA nicht aktivieren.
- Benutzer können 2FA für ihre eigenen Accounts nicht mehr deaktivieren.

Bevor du 2FA für andere Benutzer erzwingst, stelle sicher, dass sie auf eine der unterstützten {% link_new Authenticator-Apps | getting-started/use-two-factor-authentication.md | #voraussetzung-installiere-eine-authenticator-app %} zugreifen können.

### 2FA-Aktivierung für einzelne Benutzer erzwingen

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf den Namen des Benutzers, für den du 2FA erzwingen möchtest.  
   Die Accountseite des Benutzers öffnet sich.
3. Aktiviere im Abschnitt **Sicherheit** die Checkbox **Zur 2FA-Aktivierung verpflichten**.
4. Klicke auf _Speichern_{:.doc-button}, um die Aktivierung zu bestätigen.

### 2FA-Aktivierung für alle Benutzer erzwingen

1. Gehe zu _Account > Sicherheit_{:.breadcrumbs}. Auf dieser Seite kannst du sehen, wie viele Benutzer aktuell 2FA verwenden.
2. Klicke auf _2FA für alle Benutzer erzwingen_{:.doc-button}.  
   Eine grüne Erfolgsmeldung wird angezeigt. Der Text des Buttons ändert sich zu _2FA nicht mehr erzwingen_{:.doc-button}.

### 2FA für einzelne Benutzer deaktivieren

In bestimmten Fällen kann es sein, dass du 2FA für einzelne Benutzer zeitweise deaktivieren oder Benutzer komplett vom 2FA-Zwang ausschließen möchtest.

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf den Namen des Benutzers, für den du 2FA deaktivieren möchtest.  
   Die Accountseite des Benutzers öffnet sich.
3. Deaktiviere im Abschnitt **Sicherheit** die Checkbox **Zur 2FA-Aktivierung verpflichten**.
4. Klicke auf _Speichern_{:.doc-button}, um die Deaktivierung zu bestätigen.
