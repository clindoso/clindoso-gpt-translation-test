---
title: Adhérence temps réel
toc: true
product_label:
  - advanced
  - enterprise
description: Vérifiez l’adhérence de vos employés à leur planning en temps réel.
archive_ref: 20210422-en-adherence
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
redirect_from:
  - /fr/adherence/
redirect_reason: Updated filename on 07 December 2022
---

Dans _Intraday > Adhérence Temps Réel_{:.breadcrumbs}, vous pouvez comparer en temps réel les activités planifiées avec le statut réel de l’employé. Lorsque vos agents enregistrent leur statut dans un système externe (par exemple un ACD), une intégration configurée dans injixo importera les données de statut agent. Vous verrez si les activités sur lesquelles les employés travaillent actuellement respectent le planning. Cela vous permet d’identifier les écarts des employés par rapport au planning et d’agir si nécessaire.

## Prérequis

Configurez l’{% link_new import des statuts agent en temps réel | features/acd-integration/cloud/import-agent-status-data.md %}.

Après l’importation des données externes, vous devez ajouter les identifiants utilisateur externes à vos employés dans injixo. Remappez les activités externes aux activités existantes ou nouvelles d’injixo pour obtenir plus de détails sur l’adhérence.

Vous pouvez associer une ou plusieurs activités externes à une activité d’injixo. Pour définir une correspondance plus détaillée, utilisez {% link_new Matches | features/intraday/adherence-matches.md %}.

## Premiers pas

Après avoir sélectionné une **unité opérationnelle** et un **groupe** (facultatif), la page affichera les données. Vous pouvez voir un aperçu général ou des détails sur le statut individuel d’un employé dans le système externe et dans injixo.

Conseil&nbsp;: limitez les droits sur certaines unités opérationnelles ou certains groupes en configurant les {% link_new rôles utilisateur | getting-started/configure-user-roles.md | #définir-les-autorisations-sur-les-fonctionnalités-wfm %}.

### Statut

Chaque employé a un statut basé sur la comparaison entre l’activité planifiée et l'activité réelle&nbsp;:

| Statut           | Description                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| En adhérence     | Le type de l’activité planifiée est le même que le type de l’activité réelle. La ligne n’est pas mise en évidence. |
| En dépassement | Les types d’activité de l’activité planifiée et de l’activité réelle ne correspondent pas. La ligne est surlignée en rouge.                |

> Remarque
>
> Sans intégration ni identifiants utilisateur externes mappés&nbsp;:
> - Un employé planifié apparaît comme étant en adhérence, et son activité réelle apparaît comme étant hors ligne. 
> - Un employé non planifié mais qui participe à une activité apparaît comme non planifié. 
> - Un employé non planifié et qui est hors ligne n’est pas affiché.

Veuillez noter la spécificité suivante pour les employés planifiés&nbsp;:

- Les employés sans identifiant utilisateur externe attribué apparaissent comme hors ligne. Aucun statut ne peut être importé. Vous ne verrez aucune donnée dans la catégorie système externe dans Schedules ou le Centre de planification.
- Les employés planifiés pour des activités de type Congé ou Maladie et connectés au système externe apparaissent comme Non planifiés.

### Types de dépassement

Les types et les couleurs suivants sont affichés dans le [tableau des employés](#vue-densemble-de-ladhérence-tableau-des-employés)&nbsp;:

| Type           | Couleur  | Description                                                                                                                                                                   |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Non présent    | Rouge    | L’employé est planifié pour travailler sur une activité spécifique, mais aucune information du système externe n’est disponible. Les données ne sont pas importées ou ne sont pas correctement mappées.          |
| Activité incorrecte | Jaune | Selon le système externe, l’employé travaille sur une activité qui ne correspond pas à l’activité planifiée dans injixo.                                                   |
| Non planifié  | Bleu   | L’employé n'est pas planifié pour une activité dans injixo mais le système externe a envoyé un statut. Ce type de dépassement n’affecte pas négativement le score d’adhérence. |

### Seuil de tolérance

Le seuil de tolérance définit la durée après laquelle un statut de dépassement prend effet. Découvrez comment [modifier le seuil de tolérance par défaut](#ajuster-le-seuil-de-tolérance). 

Dans des conditions réelles, les employés sont rarement en mesure de respecter leur planning à la seconde près. Cela peut entraîner un affichage chargé. Le seuil de tolérance vous aide à vous concentrer sur les employés qui ont besoin de votre attention.

Si un employé se trouve dans seuil de tolérance défini, la valeur de temps affichée pour la durée de dépassement augmente déjà et&nbsp;:

- la ligne de l’employé n’est pas mise en évidence et seul le statut change,
- le statut de l’employé n’a aucun effet négatif sur le score d’adhérence,
- la ligne de l’employé n’est pas affichée si le filtre Afficher uniquement les dépassements est activé.

## Suivre l’adhérence temps réel

La page Adhérence temps réel est composée de différentes sections.

### Scores d’adhérence en pourcentage

À gauche, vous pouvez voir deux sections avec des valeurs en pourcentage&nbsp;:

- Adhérence temps réel&nbsp;: le pourcentage d'employés actuellement en adhérence ou dans le seuil de tolérance.
- Adhérence intrajournalière&nbsp;: le score d’adhérence agrégé pour les intervalles passés de la journée.

Faites passer votre curseur sur les graphiques dans la section **Adhérence intrajournalière** pour voir les valeurs des intervalles individuels&nbsp;:

- Gris&nbsp;: score d’adhérence pour les intervalles passés de la journée. Heures de la journée avec forte ou faible adhérence.
- Bleu&nbsp;: tendance du score d’adhérence intrajournalière. Elle indique la tendance générale de la journée à ce stade.
- Rose&nbsp;: l’objectif d’adhérence actuellement configuré. Les valeurs plus faibles sont mises en évidence.

{{ 3 | image: 'Graphiques d’adhérence intrajournalière','45%' }}

Remarque&nbsp;: les heures sont affichées dans le fuseau horaire de l’unité opérationnelle sélectionnée. Si vous avez seulement sélectionné un groupe et que vous utilisez plusieurs fuseaux horaires dans injixo, les heures apparaissent dans le fuseau horaire configuré dans le compte de votre entreprise. Les graphiques indiquent les horaires d’ouverture de l’unité opérationnelle sélectionnée le cas échéant.

### Vue d’ensemble
<!-- still agent in the UI - october 2023 -->
Dans la section Vue d’ensemble, vous pouvez voir le nombre d’agents pour trois types de dépassement et le nombre d’agents en adhérence, sous le seuil de tolérance et en dépassement.

### Pauses et Présence

La section Pauses affiche le nombre d’agents planifiés et actuellement connectés, ainsi que la différence numérique entre eux pour toutes les activités de type Pause. La section Présence affiche les mêmes informations pour les activités de type Présence.

### Détail par activité

Dans la section Détail par activité, vous pouvez voir le nombre d’employés planifiés pour une activité dans injixo et le nombre d’employés qui travaillent actuellement sur cette activité. Vous pouvez trier le tableau en cliquant sur l’un des en-têtes. Faites passer votre curseur sur une activité pour modifier les matches pour cette activité ou filtrer la liste des employés à droite par cette activité.

### Vue d’ensemble de l’adhérence&nbsp;: tableau des employés

Ce tableau indique les employés en adhérence ou en dépassement. Vous pouvez trier le tableau en cliquant sur l’un des en-tête. Cochez la case Afficher uniquement les dépassements à côté de la barre de recherche pour afficher uniquement les employés en dépassement.

Le tableau contient les colonnes suivantes&nbsp;:

| Colonne                    | Description                                                                                                |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Nom                      | Nom de l’employé                                                                                          |
| Activité réelle           | Nom de l’activité sur laquelle l’employé travaille actuellement (sur la base des données de la catégorie Système externe) |
| Statut                    | Statut sous la forme d’un marqueur de couleur et d’une infobulle pour le nom du statut                                        |
| Activité planifiée        | Nom de l’activité pour laquelle l’employé est actuellement planifié (le cas échéant)                                      |
| Durée du dépassement | Durée pendant laquelle l’employé a été en dépassement                                                                   |
| Durée de l’activité en cours | Temps écoulé depuis le début de l’activité en cours                                                        |

### Recherche et filtre

Pour filtrer le contenu du tableau, utilisez l’une des options suivantes&nbsp;:

| Élément             | Action                                               | Informations                                                                               |
| ----------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Barre de recherche        | Saisissez des **termes de recherche (partiels)**                   | Recherchez les noms, les activités ou les statuts des employés.  Utilisez des virgules pour séparer plusieurs termes de recherche. |
| Vue d’ensemble    | Cliquez sur un **statut**                                   | Vous pouvez ajouter plusieurs statuts. Cliquez à nouveau pour supprimer le statut de la recherche.          |
| Détail par activité | Faites passer votre curseur sur une ligne du tableau et cliquez sur la **loupe** | Vous pouvez ajouter plusieurs activités. Cliquez à nouveau pour supprimer l’activité de la recherche.      |

<!-- {{ 5 | image: "Table with details per agent", '75%' }} -->

### Informations d’adhérence pour un employé

Pour afficher une vue chronologique sous le tableau, cliquez sur le nom d’un employé. Vous verrez les activités planifiées de l’employé et un historique des statuts en dépassement pour la journée. Vous pouvez également voir la durée pour laquelle l’employé est planifié et la durée du dépassement. Le score d’adhérence dédié affiche la relation entre ces deux nombres.

{{ 6 | image: 'Détails employé','100%' }}

Cliquez sur un statut en dépassement pour ouvrir une vue détaillée des activités réelles effectuées par un employé. Vous pouvez également voir le type et la durée de l’activité. La vue détaillée groupe sur un même bloc plusieurs statuts en dépassement de courte durée qui ont lieu à la suite.

{{ 7 | image: 'Détails du dépassement','100%' }}

## Configuration

L’Adhérence temps réel peut être configurée selon vos besoins.

### Modifier l’Objectif d’adhérence

L’Objectif d’adhérence est affiché sous la forme d’un graphique dans la section Adhérence Intrajournalière. Le score par défaut est de 90&nbsp;%.

Les utilisateurs disposant d’un accès administrateur peuvent modifier l’Objectif d’adhérence en suivant ces étapes&nbsp;:

1. Cliquez sur l’{% icon ellipsis_v %}.
2. Sélectionnez **Modifier l’objectif d’adhérence**.
3. Saisissez une nouvelle valeur.
4. Cliquez sur _Appliquer_{:.doc-button}.

> Le score configuré s’applique à tous les employés de votre tenant injixo.

### Ajuster le seuil de tolérance

Les utilisateurs disposant d’un accès administrateur peuvent définir un seuil de tolérance différent pour chaque statut en dépassement&nbsp;:

1. Cliquez sur l’{% icon ellipsis_v %}.
2. Sélectionnez **Ajuster le seuil de tolérance**.
3. Sélectionnez les mêmes valeurs ou des valeurs différentes dans les menus déroulants **Non présent**, **Activité incorrecte** et **Non planifié**.
4. Cliquez sur _Appliquer_{:.doc-button}.

> Le seuil de tolérance configuré s’applique à tous les employés de votre tenant injixo.

## Résoudre les problèmes d’informations de statut externe incorrectes ou manquantes dans injixo

Les employés sans identifiant utilisateur externe attribué apparaissent comme hors ligne. Aucun statut ne peut être importé en raison de ce mapping manquant. Vous ne verrez aucune donnée dans la catégorie système externe dans Schedules ou le Centre de planification. Ajoutez l’identifiant utilisateur externe correct et attendez le prochain import de données. Vérifiez la présence de fautes de frappe dans les identifiants utilisateur externes configurés.  

Si vous constatez des écarts inattendus de données dans la catégorie système externe dans le Centre de planification ou Schedules, assurez-vous que toutes les activités externes pertinentes sont mappées sur l’activité Présent (ID 1) ou sur les activités individuelles. Pour en savoir plus, lisez notre section sur les {% link_new mappings | features/acd-integration/cloud/import-agent-status-data.md %}. <!-- Add new article about activity mapping, update naming -->

Si le problème n’est pas résolu, générez un rapport indiquant le statut réel dans le système externe, faites une capture d’écran des données de la catégorie système externe et contact notre équipe Support.

