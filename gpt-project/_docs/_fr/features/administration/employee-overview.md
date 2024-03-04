---
title: Configurer les employés
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Créer et configurer les employés à inclure dans la planification.
redirect_from:
  - /fr/employes/
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

Dans injixo, vous pouvez créer et modifier un employé de trois façons différentes, selon votre utilisation. Le tableau ci-dessous propose un aperçu des différentes fonctionnalités à partir desquelles vous pouvez configurer les employés dans injixo et décrit la configuration possible dans chacune d'entre elles.

| Fonctionnalité                                           | Description              |
| ----------------------------------------------- | ------------------------ |
| _Plan > Configuration > Employés_{:.breadcrumbs}   | {% link_new Configurez un employé pour la planification | features/administration/employee-overview.md | #aperçu-des-paramètres-employés %}. Les employés qui ne sont assignés à aucune unité opérationnelle n’apparaîtront pas dans la liste.      |
| _Account > Utilisateurs_{:.breadcrumbs}                                 | Gérez les droits utilisateur en ajoutant des {% link_new rôles utilisateur | getting-started/configure-user-roles.md | #créer-un-nouveau-rôle-utilisateur %}, {% link_new débloquez les utilisateurs verrouillés | getting-started/manage-user-accounts.md | #débloquer-les-utilisateurs %}, {% link_new définissez un nouveau mot de passe pour les utilisateurs | getting-started/manage-user-accounts.md | #définir-un-nouveau-mot-de-passe-utilisateur %} et {% link_new vérifiez les utilisateurs facturés | getting-started/how-does-billing-work.md | #voir-les-utilisateurs-facturés-et-non-facturés %} et non facturés. Vous pouvez également {% link_new supprimer des utilisateurs | getting-started/manage-user-accounts.md | #supprimer-un-compte-utilisateur %} pour éviter leur facturation. |
| **People**                                                           | {% link_new Créez et gérez | features/people/manage-people.md %} le compte d’un employé et gérez les informations de contact et les adresses. |

Dans _Plan > Configuration > Employés_{:.breadcrumbs}, les utilisateurs sans accès administrateur ne peuvent voir que les employés assignés aux unités opérationnelles sur lesquelles ils ont des droits. Les employés non assignés à une unité opérationnelle n’apparaissent pas dans la liste, même si Tous est sélectionné dans l’unité opérationnelle et les menus de sélection. Seuls les utilisateurs disposant d’un accès administrateur peuvent voir tous les employés.

Les employés et les utilisateurs sont synchronisés, il vous suffit donc de ne créer un employé qu’une seule fois et vous ne serez facturé qu’une seule fois.

> Pour chaque employé ou utilisateur créé à partir de l’une de ces fonctionnalités, votre organisation sera {% link_new facturée | getting-started/how-does-billing-work.md %} jusqu’à leur {% link_new désactivation ou leur suppression | features/administration/deactivate-employees.md %}.

## Créer un employé

Pour créer un employé et sa configuration de base, vous devez remplir tous les champs obligatoires. Avant de pouvoir configurer l’employé pour la planification, vous devez [configurer](#configurer-les-paramètres-employés) plusieurs autres [paramètres de l’employé](#aperçu-des-paramètres-employés).
Pour créer un employé et sa configuration de base, suivez ces étapes&nbsp;:

1. Accédez à _Plan > Configuration > Employés_{:.breadcrumbs}.
2. Cliquez sur l’{% icon item-add %} dans la barre d’action.
3. Dans la section **Généralités**, ajoutez un **Matricule** unique.
4. Dans la section **Données personnelles**, ajoutez le **Nom** de l’employé.
5. Dans le champ **injixo Connexion (Adresse électronique)**, entrez l’adresse e-mail que l’employé utilisera pour se connecter à injixo. Un identifiant de connexion à injixo Me est automatiquement créé. 
6. {% link_new Définissez un mot de passe | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %} pour l’employé, afin qu’il puisse se connecter à injixo.<br>Vous pouvez définir le mot de passe après avoir terminé la configuration minimale de l’employé.
7. Cliquez sur _OK_{:.doc-button}.<br>Le système définit automatiquement la date d’entrée comme la date actuelle. Vous pouvez la modifier manuellement ultérieurement dans la [section Périodes d’emploi](#autres-paramètres).

Lorsque vous créez un employé, injixo crée automatiquement un utilisateur avec le rôle standard agent.

<!-- In injixo Enterprise on-premise, you need to set the correct join date for the employee in the Employment Period section manually. To automatically create a linked user in the Users section, you need to add a User name and a Password in the Employee section. The injixo Login (Email) field is called Email 1 here and is not mandatory. --->

## Configurer les paramètres employés

Après avoir créé un employé avec les paramètres de base obligatoires, vous pouvez configurer les paramètres relatifs à la planification. Pour ce faire, suivez les étapes ci-dessous&nbsp;:

Prérequis&nbsp;: {% link_new avoir configuré tous les éléments requis pour la planification | getting-started/set-up-base-configuration.md | #éléments-de-configuration-requis %}.

1. Cliquez sur un employé dans la liste.<br>
Vous pouvez utiliser les liens rapides bleus en haut à droite pour accéder rapidement à une section.
2. Cliquez sur l’{% icon item-add %} dans une section pour ajouter un nouveau paramètre. Pour modifier un paramètre existant, cliquez sur l’{% icon item-edit %}.<br>Pour en savoir plus, lisez la section sur les [options des paramètres individuels](#aperçu-des-paramètres-employés).
3. (Facultatif) Dans certaines sections, vous pouvez configurer des {% link_new dates de validité | features/administration/set-a-validity-period.md %} pour limiter la période de validité d’un paramètre.
4. Pour enregistrer vos modifications, cliquez sur _OK_{:.doc-button}.


## Aperçu des paramètres employés

Dans les sections suivantes, vous trouverez des informations sur les paramètres de planification obligatoires et facultatifs pour la configuration des employés.

### Paramètres de planification obligatoires

La liste suivante indique les éléments de configuration obligatoires à assigner aux employés pour les planifier. Pour en savoir plus à propos de chaque élément de configuration, suivez les liens.

> Remarque
>
> Vous ne pouvez pas ajouter d’assignations dont les {% link_new périodes de validité | features/administration/set-a-validity-period.md %} se chevauchent.
> Les assignations passées et futures sont masquées par défaut. Pour les afficher, cliquez sur l’icône Afficher tout {% icon assignment-history | icon-only %}.


- {% link_new Contrats | features/administration/create-contracts.md %}&nbsp;: le menu déroulant affiche tous les contrats disponibles. Sélectionnez le contrat correspondant à votre employé et assignez-le à l’employé.
- {% link_new Niveaux de compétence | features/administration/work-with-skills.md %}&nbsp;: les niveaux de compétence reflètent les qualifications d’un employé à travailler sur une tâche particulière. Sélectionnez un ou plusieurs niveaux de compétence dans le menu déroulant.
- {% link_new Activités | features/administration/activities.md %}&nbsp;: les activités sont les tâches sur lesquelles un employé peut travailler selon ses compétences. La section Activités est remplie automatiquement après avoir assigné un niveau de compétence à un employé. Les activités sur lesquelles tous les employés peuvent travailler ne nécessitent pas de compétence, par exemple les activités système Présent et Congé.
- {% link_new Unités opérationnelles | features/administration/create-and-manage-planning-units.md %}&nbsp;: les unités opérationnelles regroupent les employés. Un employé peut être assigné à plusieurs unités opérationnelles mais doit être assigné à au moins une unité opérationnelle de priorité 1. Vous pouvez assigner une valeur comprise entre 1 et 100 aux autres unités opérationnelles pour chaque employé. 1 correspond à la priorité la plus élevée.

### Paramètres de planification facultatifs

Les paramètres suivants ne sont pas obligatoires mais peuvent également être utilisés pour la planification. Pour en savoir plus à propos de chaque élément de configuration, suivez les liens.

- {% link_new Disponibilité | features/administration/availabilities.md %}&nbsp;: définissez les jours et les heures auxquels un employé est disponible pour être planifié. Si vous souhaitez toujours exclure un employé de la planification certains jours de la semaine, définissez la disponibilité pour le {% link_new type de jour | features/administration/day-types.md %} concerné sur une minute. Pour limiter la disponibilité de plusieurs employés à la fois, utilisez des modèles horaires de type {% link_new Cadre de disponibilité | features/administration/daymodels/daymodel-creation.md | #cadre-de-disponibilité %} dans les rotations d’horaires. Si un employé est disponible sans limitations, vous n’avez pas besoin d’ajouter de disponibilités.

- {% link_new Modèles horaires | features/administration/daymodels/daymodel-creation.md %}&nbsp;: par défaut, injixo utilise tous les modèles horaires attribués à l’unité opérationnelle pour créer des plannings pour vos employés. Si vous attribuez des modèles horaires personnels à un employé, l’optimisation du planning n’utilisera que ces modèles horaires spécifiques pour l’employé. Si vous ne souhaitez planifier que les employés qui ont été assignés à des modèles horaires personnels, vous pouvez activer la règle de planification _2661_{:.id-label} _Respecter les attributions de modèles horaires aux employés_.

- {% link_new Rotations d’horaires | features/administration/shift-sequences.md %}&nbsp;: les rotations d’horaires contiennent des modèles horaires ou des activités suivant un cycle hebdomadaire. Si vous souhaitez utiliser des rotations d’horaires pour créer des horaires pour vos employés, vous devez d'abord créer et [assigner des rotations à un employé](#assigner-une-rotation-dhoraires). Vous pouvez également choisir d’assigner plusieurs rotations d’horaires à un employé, par exemple si vous souhaitez utiliser une rotation d’horaires différente pour les week-ends et les jours de semaine. 

- {% link_new Groupes | features/administration/selections.md %}&nbsp;: les groupes servent de filtre, que vous pouvez utiliser pour afficher un groupe d'employés filtré dans une vue d’ensemble ou pour effectuer une action simultanément pour un groupe spécifique d’employés. Vous pouvez créer un ou plusieurs groupes à partir du menu déroulant Groupes. Par exemple, les groupes peuvent être un ensemble d'employés toujours planifiés de la même manière, ont le même contrat, travaillent en rotations d’horaires, font du covoiturage pour se rendre au travail ou planifiés en premier en raison de leur statut à temps plein.

- {% link_new Modèles de planification | features/administration/work-time-pattern-models.md %}&nbsp;: utilisez les modèles de planification pour limiter la planification automatique à un sous-ensemble de tous les modèles horaires disponibles. Vous pouvez assigner plusieurs modèles de planification à un employé, à condition que leurs périodes de validité ne se superposent pas. Définissez une date de référence pour définir la date de début du modèle de planification.


- Systèmes externes&nbsp;: assignez des {% link_new identifiants utilisateur externes | features/acd-integration/cloud/import-agent-status-data.md | #mapper-les-identifiants-utilisateur-externes-aux-employés-dans-injixo %} qui sont nécessaires pour l'importation du statut agent à partir de votre ACD.

### Autres paramètres

La section suivante présente un aperçu des autres paramètres dans la configuration de l'employé. La plupart d'entre eux ne sont pas pertinents pour la planification. Pour plus d’informations sur ces paramètres, vous pouvez également faire passer votre curseur sur chacun d’eux dans l’interface utilisateur pour afficher les détails du paramètre.

- Périodes d’emploi&nbsp;: lorsque vous [créez un employé et sa configuration de base](#créer-un-employé), la date d’entrée est automatiquement définie. Ici, vous pouvez modifier la date d’entrée et définir une date de départ, si nécessaire.

- Données personnelles&nbsp;: saisissez les données personnelles de votre employé, par exemple l’adresse, le numéro de téléphone et le pays.

- Numéros internes d’identification&nbsp;: entrez le numéro de la carte d’identification de l’entreprise ou d’autres cartes d’identification personnelles de votre employé.

- Autres informations

Certains paramètres de la section Autres informations sont pertinents pour la planification, et d’autres non. Le tableau suivant propose un aperçu des détails de configuration.

| Paramètre        | Pertinent pour la planification | Description                |
|----------------| ------------------------|----------------------------|
|Couleur       | Non                      | Sélectionnez une couleur permettant d’identifier rapidement l’employé dans le planning.  |
|Date et lieu de naissance  |       Non |  Ajoutez la date et le lieu de naissance de l’employé.  |
|Position dans le planning  | Oui | Définit l'ordre de tri pour la fonctionnalité {% link_new Tri par position dans le planning | features/scheduling/shiftcenter/sort-and-filter-items.md | #sort-the-items-of-a-level %} dans le Centre de planification. La valeur par défaut est 0 et le Centre de planification triera par ordre croissant.  |
|Attribution de missions | Oui | La case est cochée par défaut. Elle est obligatoire si vous souhaitez planifier automatiquement les employés. Si vous ne souhaitez pas planifier automatiquement les employés, décochez la case. Vous pouvez toujours attribuer les missions et insérer des séquences de postes manuellement pour cet employé.  |

## Utiliser la mise à jour en masse

Dans injixo Advanced et Enterprise WFM, vous pouvez utiliser la fonctionnalité de {% link_new mise à jour en masse | features/administration/mass-update.md %} pour modifier plusieurs employés en une seule fois.

## Assigner une rotation d’horaires

Une rotation d’horaires est un cycle régulier de modèles horaires ou d’activités. Découvrez comment {% link_new créer des rotations d’horaires | features/administration/shift-sequences.md %} et les insérer dans votre planning.

Pour assigner une rotation d’horaires, suivez les étapes ci-dessous&nbsp;:

1. Dans la section **Rotations d’horaires**, cliquez sur l’{% icon item-add %}.
2. Sélectionnez une rotation d’horaires.
3. Dans le menu déroulant de la ligne des employés, sélectionnez la ligne de la {% link_new rotation d’horaires | features/administration/shift-sequences.md %} qui s’applique à l’employé.
4. Précisez la rotation.<br>Ce paramètre n’est pertinent que si vous avez besoin d’attribuer plus d’une rotation d’horaires à un employé. Les rotations d’horaires de valeur inférieure sont insérées en premier et peuvent être remplacées par les suivantes.
5. Définissez une date de référence qui définit le premier jour de la rotation d’horaires.
6. Cliquez sur _OK_{:.doc-button}.
Vous pouvez maintenant {% link_new insérer des rotations d’horaires | features/scheduling/schedules/schedules-insert-shift-sequences.md %} au planning.

## Muter temporairement des employés

Si vos employés travaillent souvent dans d'autres unités opérationnelle pour une durée limitée, vous pouvez utiliser la fonctionnalité Muter temporairement pour affecter des employés à une autre unité opérationnelle de manière temporaire.

Pendant la période de mutation, la nouvelle unité opérationnelle prend automatiquement la priorité pour la planification. Lorsque la période définie se termine, l'employé est automatiquement programmé dans son ancienne unité opérationnelle. La fonctionnalité Muter temporairement permet de gagner du temps par rapport à la réassignation manuelle à l'unité opérationnelle.

Pour muter temporairement un employé, suivez les étapes ci-dessous.

1. Sélectionnez un employé.
2. Accédez à la section **Unités opérationnelles**.
3. Dans l'en-tête de la section, cliquez sur l’icône Muter temporairement {% icon delegate-employees | icon-only %}.
4. Sélectionnez l’unité opérationnelle dans laquelle l’employé est muté.
5. Entrez une date de début et de fin pour la période de mutation.
6. Cliquez sur _OK_{:.doc-button}.

> Remarque
>
> Un employé affecté à plusieurs unités opérationnelles en même temps sera toujours muté de l'unité opérationnelle ayant la priorité la plus élevée.
