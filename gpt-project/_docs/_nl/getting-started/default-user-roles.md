---
title: Standaard gebruikersrollen
description: Lees meer over de toegangsrechten van standaard gebruikersrollen in injixo.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - nl/user-roles-in-detail/
redirect_reason: Updated filename on 05 December 2022
---
## Standaard gebruikersrollen

Voor elke gebruikersrol heeft injixo een standaard gebruikersrol met vooraf gedefinieerde toegangsrechten. In injixo Advanced en Enterprise WFM kun je de standaard gebruikersrollen aanpassen en/of {% link_new je eigen gebruikersrollen toevoegen | getting-started/configure-user-roles.md %}. Opmerking: De rolcategorie Overigen heeft geen standaard gebruikersrol.

| **Rolcategorie**                | **Standaard toegangsrechten**                                                                                                                                                                      |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Agent                 | Toegang tot injixo Me, bijvoorbeeld diensten bekijken, verlof aanvragen, inschrijven op diensten, diensten ruilen.                                                                           |
| Planner               | Volledige toegang tot alle functionaliteiten die relevant zijn voor het maken van forecasts, planningen, intraday management en configuratiegegevens.                                                                    |
| Supervisor (basis)    | Alleen-lezen-toegang tot het niveau **Planning** in {% link_new Schedules                                                                                                               | features/scheduling/schedules/schedules-overview.md %} en {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/shift-center-overview.md %}. Toegang tot {% link_new het overzicht Diensten ruilen | features/scheduling/view-approve-shift-swap-requests.md %} en {% link_new Vakantie/afwezigheid | features/scheduling/time-off/vacation-absences-management.md %} om dienstruilingen en verlofaanvragen te behandelen. |
| Supervisor (geavanceerd) | Alle functionaliteiten van Supervisor (basis), volledige toegang tot het Dienstrooster-Center en Schedules, rechten om planningen in intraday management te wijzigen en alleen-lezen-teogang tot configuratiegegevens. |
| Trainer               | Toegang tot Academy om training over injixo Me mogelijk te maken.                                                                                                                            |
| Financiën               | Toegang tot informatie over de gebruiker en facturatie, en tot facturen voor injixo-services.                                                                                                  |


Om een gebruiker admintoegang te geven, {% link_new kun je de gebruiker bewerken | getting-started/manage-user-accounts.md %} en het selectievakje **Geef admin toegang** aanvinken. Hierdoor worden alle overige rollen overschreven en krijgt de gebruiker volledige toegang.

Opmerking: De tabellen in dit artikel laten een overzicht van componenten en features voor de relevante standaard gebruikersrollen zien. Het groene vinkje <i class="fa fa-check" style="color:#1cb396"></i> geeft aan dat de gebruiker volledige lees- en schrijfrechten heeft. Omdat je WFM-plan ook bepaalt welke rechten je hebt, heb je mogelijk geen toegang tot alle genoemde items.

## Toegang tot componenten en features

Je vindt de componenten in de hoofdnavigatie en de features met gerelateerde functionaliteiten onder de menu-opties, zie de vetgedrukte tekst hieronder

Opmerking: In injixo Classic zijn alle planningsgerelateerde features te vinden onder _Scheduling > SchedulePro_{:.breadcrumbs}. Ga naar de sectie [Toegang tot features onder WFM](#toegang-tot-componenten-en-features) voor meer injixo Classic-features.

<div class="table__wrapper table__with-subsections" markdown="1">

|                                         |          Beheerder          |         Planner         |  Supervisor (geavanceerd)  |   Supervisor (basis)    |
| --------------------------------------- | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Forecast**                            |                         |                         |                         |                         |
| **Forecast**                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |        Alleen lezen        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Intraday**                            |                         |                         |                         |                         |
| **Real-Time Adherence**                 | <i class="fa fa-check"> |        Alleen lezen        |        Alleen lezen        |        Alleen lezen        |
| **Intraday Adherence**                  | <i class="fa fa-check"> |        Alleen lezen        |        Alleen lezen        |        Alleen lezen        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Plan**                                |                         |                         |                         |                         |
| **Schedules**                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |
| **Dienstrooster-Center**                        | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |
| **Roosterperiodes**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |                         |
| Diensten genereren                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Start diensten verloten                     | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Diensten toewijzen                           | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Aanpassen diensten genereren                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| **Planningsacties**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Dienstenseries toevoegen                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Geoptimaliseerde planning maken               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Job-optimalisatie                        | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Pauzes optimaliseren                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Extra activiteiten plannen               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Activiteiten vervangen                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Lege niveaus                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Niveau-inhoud kopiëren                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Dienstruilingen goedkeuren                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |        Alleen lezen        |
| **Meetings**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Vakantie/Afwezigheid**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |
| Verlofperiodes                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |                         |
| Recht bewerken                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |                         |
| **Configuratie**                       |                         |                         |                         |                         |
| Kwalificaties                                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |                         |
| --------------------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Analyze**                             |                         |                         |                         |                         |
| **Dashboards**                          | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

## Toegang tot gegevens over account, gebruiker en integratie

Klik op _Account_{:.menu-item} in de hoofdnavigatie om toegang te krijgen tot de hieronder genoemde features.

<div class="table__wrapper table__with-subsections" markdown="1">

|                    |          Beheerder          |         Planner         |         Financiën         |
| ------------------ | :---------------------: | :---------------------: | :---------------------: |
| **Account**        |                         |                         |                         |
| **Gebruiker**           | <i class="fa fa-check"> |                         |                         |
| **Gebruikersrollen**     | <i class="fa fa-check"> |                         |                         |
| **Facturatie**        |                         |                         |                         |
| Abonnement       | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Facturen           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Contacten           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Gegevens            | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| **Administratie** |                         |                         |                         |
| Bedrijfsdetails    | <i class="fa fa-check"> |                         |                         |
| **Integraties**   | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Beveiliging**       | <i class="fa fa-check"> |                         |                         |

</div>

## Toegang tot features in WFM

Klik op _WFM_{:.menu-item} in de hoofdnavigatie om toegang te krijgen tot de hieronder genoemde features.

Opmerking: In injixo Advanced en Enterprise WFM zijn **Monitoren** en **Administratie** beschikbaar. Alle overige planningsgerelateerde functionaliteiten onder _Scheduling > SchedulePro_{:.breadcrumbs} zijn naar _Plan > Schedules_{:.breadcrumbs} en _Plan > Vakantie/Afwezigheid_{:.breadcrumbs}. Lees meer in [Toegang tot componenten en features](#toegang-tot-componenten-en-features).

<div class="table__wrapper table__with-subsections" markdown="1">

|                                      |          Beheerder          |         Planner         |  Supervisor (geavanceerd)  |   Supervisor (basis)    |
| ------------------------------------ | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Planning**                       |                         |                         |                         |                         |
| **SchedulePro**                        |                         |                         |                         |                         |
| Dienstrooster-Center                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |
| Optimalisatie                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Planningsperioden                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |                         |
| Meeting Planner                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Dienstenseries toevoegen               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Dienstenbehoefte                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Ruiloverzicht                    | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |        Alleen lezen        |
| **TimeManager**                        |                         |                         |                         |                         |
| Richttijdcontingenten                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Vakantierecht                 | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Monitoren**                       |                         |                         |                         |                         |
| Rapporten                              | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Administratie**                   |                         |                         |                         |                         |
| **Planning**                         |                         |                         |                         |                         |
| Kwalificaties                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Activiteiten                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Dagmodellen                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Weekmodellen                   | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |                         |
| Planningsmodellen             | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |                         |
| Dienstenseries                      | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Dagtypes                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Eenheden                       | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Planningskalender                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Groepen                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Contracten                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |                         |
| Medewerkers                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Alleen lezen        |                         |
| **Forecast**                      |                         |                         |                         |                         |
| Gebeurtenistypen                          | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Queues                               | <i class="fa fa-check"> |        Alleen lezen        |                         |                         |
| **Systeem**                           |                         |                         |                         |                         |
| Planningsregels                     | <i class="fa fa-check"> |        Alleen lezen        |                         |                         |
| Instellingen                             | <i class="fa fa-check"> |                         |                         |                         |
| Externe systemen                     | <i class="fa fa-check"> |                         |                         |                         |
| Rolrechten                   | <i class="fa fa-check"> |                         |                         |                         |
| Gebruikersrechten                   | <i class="fa fa-check"> |                         |                         |                         |
| JobProcessor                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |

</div>

## Toegang tot injixo Me

Gebruikers met de rol Agent kunnen in de hoofdnavigatie op _Me_{:.menu-item} klikken om hun agenda te bekijken, verlof aan te vragen en diensten te ruilen. Alleen **Mijn agenda** is standaard toegankelijk.

Gebruikers met admintoegang kunnen op _Me_{:.menu-item} klikken en {% link_new injixo Me configureren | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %}, zodat gebruikers met de rol Agent toegang hebben tot overige features.
