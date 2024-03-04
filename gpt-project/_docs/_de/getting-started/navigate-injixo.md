---
title: Finde dich in injixo zurecht
product_label:
  - essential
  - advanced
  - enterprise
description: Erhalte einen Überblick über die Features und Funktionalitäten von injixo.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/the-wfm-cycle-in-injixo.md
redirect_from:
  - /de/after-first-login/
redirect_reason: Updated filename on 25 July 2023
---

Lies diesen Artikel, um einen Überblick über injixo zu erhalten.

Je nach Benutzerrolle können Benutzer auf verschiedene Produkte und Features von injixo zugreifen.
Dir stehen möglicherweise nicht alle in diesem Artikel beschriebenen Funktionalitäten zur Verfügung. Erfahre mehr über den {% link_new Zugriff auf Funktionalitäten | getting-started/default-user-roles.md | #access-to-modules-and-features %} für die jeweiligen Standard-Benutzerrollen.  

## Produkte und Features

Klicke auf die Elemente oben in der Navigationsleiste, um auf die Produkte und Features von injixo zuzugreifen.

------- | --------
**WFM** | Lege die erforderlichen Stammdaten an, um {% link_new dein Unternehmen abzubilden | getting-started/set-up-base-configuration.md %}, {% link_new erstelle Reports | features/reporting/standard-reports/creating-reports.md %} und konfiguriere Einstellungen und {% link_new Planungsregeln | features/administration/create-contracts.md %}.
**Forecast** | {% link_new Erstelle Workloads | features/forecast/injixo-forecast/manage-workloads.md %}, um auf Grundlage historischer Daten {% link_new Forecasts zu erstellen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.
**Plan** | {% link_new Erstelle Schichtpläne | features/scheduling/schedules/schedules-overview.md %}, {% link_new verwalte Abwesenheitsperioden und -anträge | features/scheduling/time-off/time-off-periods.md %} und {% link_new plane Meetings | features/scheduling/meetings/meetings-overview.md %}. Rufe das {% link_new Schicht Center | features/scheduling/shiftcenter/shift-center-overview.md %} auf, um deine Schichtpläne einzusehen und manuell anzupassen. Füge Konfigurationselemente wie {% link_new Qualifikationen | features/administration/work-with-skills.md %} hinzu.
**Intraday** | Unter {% link_new Echtzeit Adherence | features/intraday/real-time-adherence.md %} kannst du Details zum aktuellen Status der Planeinhaltung jedes Mitarbeiters einsehen. Dies hilft dir, unvorhergesehene Ereignisse zu erkennen und darauf zu reagieren, um dein Service-Level zu erreichen.
**Analyze** | Gehe zur Ansicht {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %}, um historische und prognostizierte Daten einzusehen, deine Daten in Grafen darzustellen und sie abzugleichen.
**People**<span class="beta-icon">Beta</span> | {% link_new Erstelle, bearbeite oder lösche Profile | features/people/manage-people.md %} für Mitarbeiter in deinem Unternehmen.
**Me** | Mitarbeiter können {% link_new ihre Schichtpläne einsehen, Abwesenheiten beantragen, Schichten tauschen und Wünsche für Schichten abgeben | features/injixo-me/use-injixo-me/explore-injixo-me.md %}. Benutzer mit Admin-Zugriff können {% link_new Features aktivieren bzw. deaktivieren | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %}.

## Account

Benutzer mit Admin-Zugriff können unter _Account_{:.menu-item} auf die folgenden Funktionalitäten zugreifen.  
Erfahre mehr über die {% link_new Zugriffsrechte für Standard-Benutzerrollen | getting-started/default-user-roles.md | #zugriff-auf-konto-benutzer-und-integrationsbezogene-informationen %}.

---------- | --------
**Benutzer** | {% link_new Verwalte Benutzerkonten | getting-started/manage-user-accounts.md %}. Entsperre gesperrte Benutzer.
**Rollen** | {% link_new Erstelle neue Benutzerrollen oder verwalte bestehende | getting-started/configure-user-roles.md %}.
**Abrechnung** | {% link_new Konfiguriere die Abrechnung | getting-started/how-does-billing-work.md %}, überprüfe die aktuelle Anzahl an Benutzern und verwalte Rechnungen.
**Administration** | Ändere den Namen oder das Land deines Unternehmens. Ändere die Zeitzone oder Sprache deines Tenants.
**Integrationen** | {% link_new Richte Integrationen ein | features/acd-integration/cloud/how-integrations-work.md %}, um Daten zu injixo zu importieren.
**Sicherheit** | {% link_new Erzwinge die Zwei-Faktor-Authentifizierung | getting-started/manage-2fa.md %} für alle Benutzer. {% link_new Aktiviere Single Sign-on | getting-started/single-sign-on.md %} für deinen Account und für die Accounts aller Benutzer.
**Benachrichtigungen** | {% link_new Konfiguriere E-Mail- und Browser-Benachrichtigungen | getting-started/notifications.md %} für die Accounts anderer Benutzer.

> Wir empfehlen, Admin-Zugriff für einen weiteren Benutzer zu aktivieren. Du kannst dies unter _Account > Benutzer_{:.breadcrumbs} tun.

## Dein Benutzerprofil

Klicke oben rechts auf deinen **Benutzernamen**, um dein Benutzerprofil zu öffnen.

---------- | --------
**Mein Profil** | Ändere deinen Namen und die E-Mail-Adresse, mit der du dich bei injixo anmeldest. Lege deine Sprache fest. Lege die Zeitzone zur korrekten Anzeige der Planungsdaten fest (diese Änderung ist nach der nächsten Anmeldung wirksam). Erlaube {% link_new Browser-Benachrichtigungen | getting-started/notifications.md | #browser-benachrichtigungen-erlauben %} von injixo.
**Sicherheit** | Ändere dein Passwort. Aktiviere die {% link_new Zwei-Faktor-Authentifizierung | getting-started/use-two-factor-authentication.md %}.
**Persönliche Zugangstoken** | Erstelle einen Token für den Zugriff auf die {% link_new injixo API | features/reporting/injixo-api/injixo-api.md %}.<br>Standardmäßig können nur Benutzer mit Admin-Zugriff persönliche Zugangstoken erstellen. Benutzer mit Admin-Zugriff können {% link_new anderen Benutzerrollen erlauben, persönliche Zugangstoken zu erstellen | features/reporting/injixo-api/injixo-api.md | #autorisierung-persönlicher-zugangstoken %}.

## Academy

Klicke neben deinem Benutzernamen auf das {% icon graduation_cap %}, um {% link_new Academy | getting-started/e-learning.md %} aufzurufen, die Self-Service-Lernplattform von injixo.

## Support

Klicke oben rechts auf das {% icon circle_question %}, um das Help Center aufzurufen, wo du folgendes tun kannst:

- Auf eine Sammlung von Artikeln zugreifen, die dir helfen, dein injixo-Wissen zu erweitern.
- Das Glossar durchsuchen, um Definitionen für Terme und Abkürzungen zu finden, die in injixo und in Help-Center-Artikeln verwendet werden.
- Ein Support-Ticket erstellen oder technische Handbücher herunterladen.
- Weitere injixo-Services und Lernressourcen entdecken.