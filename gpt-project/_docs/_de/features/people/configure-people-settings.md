---
title: Mitarbeitereinstellungen konfigurieren
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du Mitarbeiter entsperrst, die sich selbst ausgesperrt haben, ein neues Passwort für Mitarbeiter setzt, die Rolle eines Mitarbeiters änderst und wie du Adminrechte für bereits angelegte Mitarbeiter vergibst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/people/configure-people-settings.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-2fa.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/configure-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/single-sign-on.md
---

> Hinweis
>
> Dieser Artikel dokumentiert den aktuellen Status der neuen **People**-App. Bis alle hier beschriebenen Funktionalitäten vollständig von bisherigen Features übertragen wurden, findest du sie weiterhin an der gewohnten Stelle.

Mitarbeiter mit Adminrechten haben standardmäßig Zugriff auf _People_{:.breadcrumbs}. Je nachdem, wie dein Unternehmen Rollen und Adminrechte verwaltet, musst du möglicherweise {% link_new Zugriffsrechte für **People** an andere Mitarbeiter in deinem Unternehmen vergeben | getting-started/configure-user-roles.md %}.

Neu bei People? Lerne zuerst {% link_new die Grundlagen | features/people/configure-people.md %}.

In den folgenden Abschnitten erfährst du, wie du die Einstellungen für einen einzelnen Mitarbeiter ändern kannst.

## Adminrechte vergeben

1. Gehe zu _People_{:.breadcrumbs}.<br>
2. Verwende das Suchfeld, um nach dem Mitarbeiter zu suchen, für den du Adminrechte vergeben möchtest und klicke auf dessen Kachel.
3. Klicke im Tab **Zugriffsrechte** des Konfigurationsfensters im Abschnitt **Rollen und Adminrechte** auf {% icon pencil | icon-only %} **Bearbeiten**.
4. Aktiviere oben die Checkbox **Adminrechte vergeben**.
5. Klicke auf _Speichern_{:.doc-button}.

## Rolle ändern

1. Gehe zu _People_{:.breadcrumbs}.<br>
2. Verwende das Suchfeld, um nach dem Mitarbeiter zu suchen, für den du die Rolle ändern möchtest und klicke auf dessen Kachel.
3. Klicke im Tab **Zugriffsrechte** des Konfigurationsfensters im Abschnitt **Rollen und Adminrechte** auf {% icon pencil | icon-only %} **Bearbeiten**.
4. Aktiviere bzw. deaktiviere die Checkbox neben den Rollen, die dem Mitarbeiter zugewiesen bzw. nicht mehr zugewiesen sein sollen.
5. Klicke auf _Speichern_{:.doc-button}.

## Neues Passwort festlegen

1. Gehe zu _People_{:.breadcrumbs}.<br>
2. Verwende das Suchfeld, um nach dem Mitarbeiter zu suchen, für den du ein neues Passwort festlegen möchtest und klicke auf dessen Kachel.
3. Klicke im Tab **Zugriffsrechte** des Konfigurationsfensters im Abschnitt **Authentifizierung und Passwort** auf {% icon pencil | icon-only %} **Bearbeiten**.
4. Gib im Bereich **Passwort** ein neues Passwort ein und klicke auf {% icon check_circle | icon-only %} **Speichern**.

Du musst dem Mitarbeiter das neue Passwort mitteilen. Aus Sicherheitsgründen sollte der Mitarbeiter sein Passwort sofort ändern und an einem sicheren Ort speichern.

## Mitarbeiter entsperren

Mitarbeiter werden nach drei fehlgeschlagenen Anmeldeversuchen mit einem falschen Passwort gesperrt. Um Mitarbeiter zu entsperren, gehe wie folgt vor:

1. Gehe zu _People_{:.breadcrumbs}.
2. Suche nach dem Mitarbeiter, den du entsperren möchtest.<br>
   Die Mitarbeiterliste zeigt ein {% icon lock %} neben dem Namen jedes gesperrten Mitarbeiters an.
3. Klicke auf die Kachel des gesperrten Mitarbeiters.
4. Klicke im Tab **Zugriffsrechte** des Konfigurationsfensters im Abschnitt **Authentifizierung und Passwort** auf {% icon pencil | icon-only %} **Bearbeiten**.
5. Klicke unten im Fenster auf _Passwort wiederherstellen_{:.doc-button}.

Der Mitarbeiter kann sich jetzt wieder mit dem vorherigen Passwort anmelden. Wenn der Mitarbeiter sein Passwort nicht mehr weiß, kannst du für ihn [ein neues Passwort festlegen](#neues-passwort-festlegen).

## 2FA aktivieren

Erfahre, wie du für einen oder alle Mitarbeiter in deinem Unternehmen {% link_new 2FA verwalten | getting-started/manage-2fa.md %} kannst.

## Benutzerprinzipalnamen für Single Sign-On ändern

Unter _People_{:.breadcrumbs} kannst du den Benutzerprinzipalnamen (User Principal Name, UPN) für einzelne Mitarbeiter ändern, wenn deren E-Mail-Adresse für die Anmeldung bei injixo von der UPN abweicht, die beim Identity Provider für das Single Sign-On verwendet wird.
Erfahre, wie du für einen oder alle Mitarbeiter in deinem Unternehmen {% link_new Single Sign-On konfigurierst | getting-started/single-sign-on.md %}.

1. Gehe zu _People_{:.breadcrumbs}.
2. Suche nach dem Mitarbeiter, für den du den Benutzerprinzipalnamen ändern möchtest und klicke auf dessen Kachel.<br>
3. Klicke im Tab **Zugriffsrechte** des Konfigurationsfensters im Abschnitt **Single Sign-On** auf {% icon pencil | icon-only %} **Bearbeiten**.
4. Gib einen neuen Benutzerprinzipalnamen ein.
5. Klicke auf _Speichern_{:.doc-button}.

## Sprache und Zeitzone ändern

1. Gehe zu _People_{:.breadcrumbs}.
2. Suche nach dem Mitarbeiter, für den du die Sprache bzw. Zeitzone ändern möchtest und klicke auf dessen Kachel.<br>
3. Klicke im Tab **Profil** des Konfigurationsfensters im Abschnitt **Sprache und Zeitzone** auf {% icon pencil | icon-only %} **Bearbeiten**.
4. Wähle aus dem Dropdown-Menü eine Sprache bzw. Zeitzone aus.
5. Klicke auf _Speichern_{:.doc-button}.
