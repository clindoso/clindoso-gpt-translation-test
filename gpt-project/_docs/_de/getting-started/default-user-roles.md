---
title: Standard-Benutzerrollen
description: Erfahre, welche Zugriffsrechte die Standard-Benutzerrollen in injixo haben.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /de/user-roles-in-detail/
redirect_reason: Updated filename on 05 December 2022
---

## Standard-Benutzerrollen

In jeder Rollenkategorie bietet injixo eine Standard-Benutzerrolle mit bereits definierten Zugriffsrechten. In injixo Advanced und Enterprise WFM kannst du die Standard-Benutzerrollen anpassen bzw. {% link_new eigene Benutzerrollen hinzufügen | getting-started/configure-user-roles.md %}.<br>Hinweis: Die Rollenkategorie Sonstige hat keine Standard-Benutzerrolle.

| **Rollenkategorie**        | **Standardzugriffsrechte**                                                                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Agent                      | Zugriff auf injixo Me, um Schichten einzusehen, Abwesenheiten zu beantragen, Wünsche für Schichten abzugeben und Schichten zu tauschen.                                                                       |
| Planer                     | Voller Zugriff auf alle Funktionalitäten rund um Forecasting, Schichtplanung, Tagessteuerung und Stammdaten.                                                                                                  |
| Supervisor (eingeschränkt) | Lesezugriff auf die Ebene Plan in {% link_new Schedules                                                                                                                                                       | features/scheduling/schedules/schedules-overview.md %} und im {% link_new Schicht Center | features/scheduling/shiftcenter/shift-center-overview.md %}. Zugriff auf die {% link_new Tauschübersicht | features/scheduling/view-approve-shift-swap-requests.md %} und auf {% link_new Urlaub/Abwesenheiten | features/scheduling/time-off/vacation-absences-management.md %}, um Schichttauschanfragen und Abwesenheitsanträge zu verwalten. |
| Supervisor (erweitert)     | Zugriff auf dieselben Funktionalitäten wie Supervisor (eingeschränkt), voller Zugriff auf das Schicht Center und Schedules zum Ändern des Schichtplans in der Tagessteuerung. Nur Lesezugriff auf Stammdaten. |
| Buchhaltung                | Zugang zu Benutzer- und Abrechnungsinformationen sowie zu Rechnungen für injixo-Dienste.                                                                                                                      |
| Trainer                    | Keine Standardberechtigungen.                                                                                                                                                                                 |

Um einem Benutzer Admin-Zugriff zu gewähren, {% link_new bearbeite einen Benutzer | getting-started/manage-user-accounts.md %} und aktiviere die Checkbox **Admin-Zugriff gewähren**. Damit werden alle anderen Rollen überschrieben und der Benutzer erhält alle Zugriffsrechte.

Hinweis: Die Tabellen in diesem Artikel listen Komponenten und Features für die jeweiligen Standard-Benutzerrollen auf. Das grüne Häkchen-Icon <i class="fa fa-check" style="color:#1cb396"></i> steht für vollen (Lese- und Schreib-) Zugriff. Deine Zugriffsrechte hängen auch von deinem WFM-Plan ab. Deshalb ist es möglich, dass du nicht auf jedes aufgeführte Element zugreifen kannst.

## <a name="access-to-modules-and-features"></a>Zugriff auf Komponenten und Features

In der Hauptnavigation findest du die Hauptkomponenten und unter jedem Menüpunkt die dazugehörigen Features. Im folgenden sind beide in fett hervorgehoben.

Hinweis: In injixo Classic findest du alle planungsbezogenen Features unter _Scheduling > SchedulePro_{:.breadcrumbs}. Im Abschnitt [Zugriff auf WFM-Features](#zugriff-auf-wfm-features) erfährst du mehr über weitere Features von injixo Classic.

<div class="table__wrapper table__with-subsections" markdown="1">

|                                         |          Admin          |         Planer          | Supervisor (erweitert)  | Supervisor (eingeschränkt) |
| --------------------------------------- | :---------------------: | :---------------------: | :---------------------: | :------------------------: |
| **Forecast**                            |                         |                         |                         |                            |
| **Forecast**                            | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |      Nur Lesezugriff       |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- |  -----------------------   |
| **Intraday**                            |                         |                         |                         |                            |
| **Echtzeit Adherence**                  | <i class="fa fa-check"> |     Nur Lesezugriff     |     Nur Lesezugriff     |      Nur Lesezugriff       |
| **Intraday Adherence**                  | <i class="fa fa-check"> |     Nur Lesezugriff     |     Nur Lesezugriff     |      Nur Lesezugriff       |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- |  -----------------------   |
| **Plan**                                |                         |                         |                         |                            |
| **Schedules**                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |      Nur Lesezugriff       |
| **Schicht Center**                      | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |      Nur Lesezugriff       |
| **Planperioden**                        | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |                            |
| Schichten erzeugen                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Schichten verlosen                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Schichten zuteilen                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Schichterzeugung anpassen               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| **Planungsaktionen**                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Schichtfolgen einfügen                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Optimierten Plan erstellen              | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Joboptimierung                          | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Pausen optimieren                       | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Extra-Aktivitäten planen                | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Aktivitäten ersetzen                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Ebenen leeren                           | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Ebeneninhalte kopieren                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Tauschanfragen genehmigen               | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |      Nur Lesezugriff       |
| **Meetings**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                            |
| **Urlaub/Abwesenheiten**                | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |      Nur Lesezugriff       |
| Urlaubsperioden                         | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |                            |
| Urlaubsansprüche bearbeiten             | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |                            |
| **Konfiguration**                       |                         |                         |                         |                            |
| Qualifikationen                         | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |                            |
| --------------------------------------- | ----------------------- | ----------------------- | ----------------------- |  -----------------------   |
| **Analyze**                             |                         |                         |                         |                            |
| **Dashboards**                          | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |  <i class="fa fa-check">   |

</div>

## Zugriff auf Konto, Benutzer und integrationsbezogene Informationen

Klicke in der Hauptnavigation auf _Account_{:.menu-item}, um auf folgende Features zuzugreifen.

<div class="table__wrapper table__with-subsections" markdown="1">

|                    |          Admin          |         Planer          |       Buchhaltung       |
| ------------------ | :---------------------: | :---------------------: | :---------------------: |
| **Account**        |                         |                         |                         |
| **Benutzer**       | <i class="fa fa-check"> |                         |                         |
| **Rollen**         | <i class="fa fa-check"> |                         |                         |
| **Abrechnung**     |                         |                         |                         |
| Abonnement         | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Rechnungen         | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Kontakte           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Details            | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| **Administration** |                         |                         |                         |
| Details            | <i class="fa fa-check"> |                         |                         |
| **Integrationen**  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Sicherheit**     | <i class="fa fa-check"> |                         |                         |

</div>

## Zugriff auf WFM-Features

Klicke in der Hauptnavigation auf _WFM_{:.menu-item}, um auf folgende Features zuzugreifen.

Hinweis: In injixo Advanced und Enterprise WFM sind **Controlling** und **Administration** verfügbar. Alle weiteren planungsbezogenen Funktionalitäten unter _Scheduling > Schedule Pro_{:.breadcrumbs} wurden in _Plan > Schedules_{:.breadcrumbs} und _Plan > Urlaub/Abwesenheiten_{:.breadcrumbs} verschoben. Erfahre mehr unter [Zugriff auf Komponenten und Features](#access-to-modules-and-features).

<div class="table__wrapper table__with-subsections" markdown="1">

|                                      |          Admin          |         Planer          | Supervisor (erweitert)  | Supervisor (eingeschränkt) |
| ------------------------------------ | :---------------------: | :---------------------: | :---------------------: | :------------------------: |
| **Scheduling**                       |                         |                         |                         |                            |
| **SchedulePro**                      |                         |                         |                         |                            |
| Schicht Center                       | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |      Nur Lesezugriff       |
| Optimierung                          | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Planperioden                         | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |                            |
| Meeting Planner                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Schichtfolgen einfügen               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Schichtbedarf                        | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Tauschübersicht                      | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |      Nur Lesezugriff       |
| **TimeManager**                      |                         |                         |                         |                            |
| Richtzeitkonten                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Zeitkonten                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |      Nur Lesezugriff       |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- |  -----------------------   |
| **Controlling**                      |                         |                         |                         |                            |
| Reports                              | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |  <i class="fa fa-check">   |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- |  -----------------------   |
| **Administration**                   |                         |                         |                         |                            |
| **Scheduling**                       |                         |                         |                         |                            |
| Aktivitäten                          | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                            |
| Tagesmodelle                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                            |
| Wochenmodelle                        | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |                            |
| Planungsmodelle                      | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |                            |
| Schichtfolgen                        | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                            |
| Tagestypen                           | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Planungseinheiten                    | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                            |
| Planungskalender                     | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Auswahl                              | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                            |
| Verträge                             | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |                            |
| Mitarbeiter                          | <i class="fa fa-check"> | <i class="fa fa-check"> |     Nur Lesezugriff     |                            |
| **Prognose**                         |                         |                         |                         |                            |
| Ereignistypen                        | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                            |
| Queues                               | <i class="fa fa-check"> |     Nur Lesezugriff     |                         |                            |
| **System**                           |                         |                         |                         |                            |
| Planungsregeln                       | <i class="fa fa-check"> |     Nur Lesezugriff     |                         |                            |
| Einstellungen                        | <i class="fa fa-check"> |                         |                         |                            |
| Externe Systeme                      | <i class="fa fa-check"> |                         |                         |                            |
| Benutzerrollenrechte                 | <i class="fa fa-check"> |                         |                         |                            |
| Benutzerrechte                       | <i class="fa fa-check"> |                         |                         |                            |
| JobProcessor                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                            |

</div>

## Zugriff auf injixo Me

Benutzer mit der Benutzerrolle Agent können in der Hauptnavigation auf _Me_{:.menu-item} klicken, um ihren Kalender einzusehen, Abwesenheiten zu beantragen und Schichten zu tauschen. Standardmäßig ist nur der Zugriff auf das Feature **Mein Kalender** freigegeben.

Benutzer mit Admin-Zugriff können auf _Me_{:.menu-item} klicken und {% link_new injixo Me konfigurieren | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %}, um Benutzern mit der Benutzerrolle Agent Zugriff auf weitere Features zu erlauben.
