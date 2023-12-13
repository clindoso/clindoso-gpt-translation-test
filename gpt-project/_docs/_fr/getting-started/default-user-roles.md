---
title: Rôles utilisateur standard
description: Découvrez les droits d’accès des rôles utilisateur standard dans injixo.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /fr/user-roles-in-detail/
  - /fr/details-roles/
redirect_reason: Updated filename on 05 December 2022, /details-roles/ used in French Help Center
---
## Rôles utilisateur standard

Dans chaque catégorie de rôle, injixo propose un rôle utilisateur standard avec des droits d’accès prédéfinis. Dans injixo Advanced et Enterprise WFM, vous pouvez personnaliser les rôles utilisateur standard et/ou {% link_new ajouter vos propres rôles utilisateur | getting-started/configure-user-roles.md %}. Remarque&nbsp;: la catégorie Autre n’a pas de rôle utilisateur standard.

| **Catégorie de rôle**   | **Droits d'accès par défaut** |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Employé                 | Accès à injixo Me pour visualiser les journées, demander des congés, participer à la génération de missions, échanger des journées. |
| Planificateur           | Accès complet à toutes les fonctionnalités relatives aux prévisions, à la planification, à la gestion intrajournalière et aux données de configuration. |
| Superviseur (basique)     | Accès en lecture seule de la catégorie **Planning** dans {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %} et le {% link_new Centre de planification | features/scheduling/shiftcenter/shift-center-overview.md %}. Accès à {% link_new Gérer les échanges de plannings | features/scheduling/view-approve-shift-swap-requests.md %} et à {% link_new Congés/Absences | features/scheduling/time-off/vacation-absences-management.md %} pour gérer les échanges de journées et les demandes de congés. |
| Superviseur (avancé)    | Toutes les fonctionnalités Superviseur (basique), accès complet au Centre de planification et aux plannings, autorisation de modifier les plannings dans la gestion en temps réel, et accès en lecture seule aux données de configuration. |
| Formateur               | Accès à Academy pour simplifier la formation à injixo Me. |
| Finance                 | Accès aux informations sur les utilisateurs et la facturation, ainsi qu’aux factures pour les services injixo. |


Pour accorder l’accès administrateur à un utilisateur, {% link_new modifiez un utilisateur | getting-started/manage-user-accounts.md %} et cochez la case **Donner le rôle Admin à l’utilisateur**. Il remplacera les rôles précédents et lui donnera un accès complet.

Remarque&nbsp;: les tableaux de cet article répertorient les composants et les fonctionnalités des rôles utilisateur standard pertinents. L’icône verte <i class="fa fa-check" style="color:#1cb396"></i> indique un accès complet (lecture et écriture). Étant donné que votre offre WFM détermine également vos droits d'accès, il se peut que vous n’ayez pas accès à tous les éléments répertoriés.

## Accès aux composants et aux fonctionnalités

Vous pouvez accéder aux composants du menu de navigation principale et aux fonctionnalités correspondantes sous chaque élément, indiqués ci-dessous en gras.

Remarque&nbsp;: injixo Classic contient toutes les fonctionnalités liées à la planification dans _Planification > SchedulePro_{:.breadcrumbs}. Reportez-vous à la section [Accès aux fonctionnalités dans WFM](#accès-aux-fonctionnalités-dans-wfm) pour voir les autres fonctionnalités disponibles dans injixo Classic.

<div class="table__wrapper table__with-subsections" markdown="1">

|                                         |          Admin          |         Planificateur         |  Superviseur (avancé)  |   Superviseur (basique)    |
| --------------------------------------- | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Forecast**                            |                         |                         |                         |                         |
| **Forecast**                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |        Lecture seule        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Intraday**                            |                         |                         |                         |                         |
| **Adhérence en temps réel**                 | <i class="fa fa-check"> |        Lecture seule        |        Lecture seule        |        Lecture seule        |
| **Adhérence intrajournalière**                  | <i class="fa fa-check"> |        Lecture seule        |        Lecture seule        |        Lecture seule        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Plan**                                |                         |                         |                         |                         |
| **Schedules**                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |
| **Centre de planification**                        | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |
| **Périodes de planification**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |                         |
| Générer les missions                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Démarrer le tirage au sort                     | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Attribuer les missions                           | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Paramètres de la Génération de missions                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| **Actions de planification**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Insérer des rotations d’horaires                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Optimiser le planning               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Optimiser les activités                        | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Optimiser les pauses                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Planifier les activités supplémentaires               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Remplacer des activités                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Supprimer le planning                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Copier le planning                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Approuver les demandes d’échanges                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |        Lecture seule        |
| **Meetings**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Congés/Absences**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |
| Périodes de congés                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |                         |
| Modifier les droits aux congés                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |                         |
| **Configuration**                       |                         |                         |                         |                         |
| Compétences                                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |                         |
| --------------------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Analyze**                             |                         |                         |                         |                         |
| **Dashboards**                          | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

## Accès aux informations concernant le compte, les utilisateurs et les intégrations

Cliquez sur _Account_{:.menu-item} dans le menu de navigation principal pour accéder aux fonctionnalités ci-dessous.

<div class="table__wrapper table__with-subsections" markdown="1">

|                    |          Admin          |         Planificateur         |         Finance         |
| ------------------ | :---------------------: | :---------------------: | :---------------------: |
| **Account**        |                         |                         |                         |
| **Utilisateur**           | <i class="fa fa-check"> |                         |                         |
| **Rôles utilisateur**     | <i class="fa fa-check"> |                         |                         |
| **Facturation**        |                         |                         |                         |
| Abonnement       | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Factures           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Contacts           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Détails            | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| **Administration** |                         |                         |                         |
| Informations compte    | <i class="fa fa-check"> |                         |                         |
| **Intégrations**   | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Sécurité**       | <i class="fa fa-check"> |                         |                         |

</div>

## Accès aux fonctionnalités dans WFM

Cliquez sur _WFM_{:.menu-item} dans le menu de navigation principal pour accéder aux fonctionnalités ci-dessous.

Remarque&nbsp;: dans injixo Advanced et Enterprise WFM, les menus **Supervision** et **Administration** sont disponibles. Toutes les autres fonctionnalités liées à la planification dans _Planification > SchedulePro_{:.breadcrumbs} ont été déplacées dans _Plan > Schedules_{:.breadcrumbs} et _Plan > Congés_{:.breadcrumbs}. En savoir plus dans la section [Accès aux composants et aux fonctionnalités](#accès-aux-composants-et-aux-fonctionnalités).

<div class="table__wrapper table__with-subsections" markdown="1">

|                                      |          Admin          |         Planificateur         |  Superviseur (avancé)  |   Superviseur (basique)    |
| ------------------------------------ | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Planification**                       |                         |                         |                         |                         |
| **SchedulePro**                        |                         |                         |                         |                         |
| Centre de planification                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |
| Optimisation                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Périodes de planification                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |                         |
| Planificateur de meetings                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Insérer des rotations d’horaires               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Besoin en missions                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Gérer les échanges de planning                    | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |        Lecture seule        |
| **Gestion des temps**                        |                         |                         |                         |                         |
| Compte Temps dû                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Droits aux congés                 | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Supervision**                       |                         |                         |                         |                         |
| Rapports                              | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Administration**                   |                         |                         |                         |                         |
| **Planification**                         |                         |                         |                         |                         |
| Activités                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Modèles horaires                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Modèles hebdomadaires                   | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |                         |
| Modèles de planification             | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |                         |
| Rotations d’horaires                      | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Types de jours                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Unités opérationnelles                       | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Calendriers de planification                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Groupes                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Contrats                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |                         |
| Employés                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Lecture seule        |                         |
| **Prévision**                      |                         |                         |                         |                         |
| Types d’événements                          | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| File d’attente                               | <i class="fa fa-check"> |        Lecture seule        |                         |                         |
| **Système**                           |                         |                         |                         |                         |
| Règles de planification                     | <i class="fa fa-check"> |        Lecture seule        |                         |                         |
| Paramètres                             | <i class="fa fa-check"> |                         |                         |                         |
| Systèmes externes                     | <i class="fa fa-check"> |                         |                         |                         |
| Droits d’accès des rôles d’utilisateurs                   | <i class="fa fa-check"> |                         |                         |                         |
| Droits d’accès                   | <i class="fa fa-check"> |                         |                         |                         |
| JobProcessor                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |

</div>

## Accès à injixo Me

Les utilisateurs ayant le rôle agent peuvent cliquer sur _Me_{:.menu-item} dans la navigation principale pour voir leur calendrier, demander des congés et échanger des journées. Seul **Mon calendrier** est accessible par défaut.


Les utilisateurs ayant un accès administrateur peuvent cliquer sur _Me_{:.menu-item} et {% link_new configurer injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} pour permettre aux utilisateurs ayant le rôle agent d'accéder à des fonctionnalités supplémentaires.
