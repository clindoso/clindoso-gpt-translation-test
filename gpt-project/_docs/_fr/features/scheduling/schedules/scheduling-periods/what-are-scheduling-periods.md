---
title: Périodes de planification
description: Découvrez comment sont utilisées les périodes de planification, comment les modifier et les supprimer (Schedules).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
  - overwrite_title: Permettre aux employés d’échanger des missions
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
---

En lisant cet article, vous apprendrez&nbsp;:
- ce que sont les périodes de planification et comment les utiliser,
- comment afficher, modifier et supprimer les périodes de planification.

## Périodes de planification

Les périodes de planification sont des périodes de quelques jours, semaines ou mois. Vous pouvez les utiliser si vous souhaitez&nbsp;:

- permettre aux employés de {% link_new consulter leur planning | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %},
- permettre aux employés {% link_new d’échanger des journées | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} entre eux,
- autoriser la {% link_new génération de missions | features/scheduling/schedules/schedules-shift-bidding.md %} pour les employés.

Pour permettre aux employés de créer des desiderata d’absences, utilisez les {% link_new périodes de congés | features/scheduling/time-off/time-off-periods.md %}.

### Statut

Chaque période de planification a un statut, qui autorise ou limite certaines options pour les employés sur la période de planification. En général, le statut d’une période de planification sera modifié plusieurs fois pendant le processus de planification, par exemple après avoir finalisé le planning ou lorsque la période de desiderata de missions a expiré.

Statut | Explication
------- | -------
Non publiée | Les employés ne peuvent ni voir le planning publié, ni participer à la {% link_new génération de missions | features/scheduling/schedules/schedules-shift-bidding.md %}, ni échanger de journées entre eux. Utilisez ce statut si vous ne souhaitez pas partager le planning avec vos employés pour le moment.
Missions disponibles | Les employés peuvent voir le planning publié, participer à la génération de missions et échanger leurs journées entre eux. Vous ne pouvez pas définir ce statut si la période de planification a déjà expiré.
Publiée | Les employés peuvent voir le planning publié et échanger leurs journées entre eux. Ils ne peuvent pas participer à la génération de missions.
Clôturée | Ce statut indique que le planning est définitif. Les employés peuvent continuer à échanger des journées entre eux.

## Filtrer et afficher des périodes de planification

1. Accédez à *Plan > Schedules*{:.breadcrumbs}.
2. Cliquez sur *Périodes de planification*{:.doc-button}.
3. Sélectionnez une **Unité opérationnelle** depuis la première liste déroulante. Commencez à saisir le nom de l’unité opérationnelle pour filtrer la liste.
4. (Facultatif) Sélectionnez un **Groupe** depuis la seconde liste déroulante. Commencez à saisir le nom de l’unité opérationnelle pour filtrer la liste.

Toutes les périodes de planification de l’unité opérationnelle sélectionnée et/ou du groupe apparaitront dans les onglets ci-dessous&nbsp;: 
- l’onglet **En cours** affiche les périodes de planification en cours ou à venir,
- l’onglet **Expirée(s)** indique les périodes de planification dont les dates de début et de fin se situent dans le passé.
Les deux onglets seront vides si vous n’avez créé aucune période de planification ou si les critères du filtre ne correspondent à aucune période de planification.

Le tableau des périodes de planification est composé de six colonnes&nbsp;:
- **Statut**&nbsp;: statut de la période de planification, 
- **Groupe**&nbsp;: groupe d’employés concernés par la période de planification,
- **Valide du**&nbsp;: date de début de la période de planification,
- **Jusqu’au**&nbsp;: date de fin de la période de planification,
- **Date limite**&nbsp;: date jusqu’à laquelle les employés peuvent participer à la génération de missions et échanger des journées,
- **Héritée de**&nbsp;: lorsque vous créez une période de planification pour une unité opérationnelle supérieure, toutes les unités opérationnelles inférieures héritent de son statut. Cette colonne indique le nom de l’unité opérationnelle supérieure, le cas échéant.

Vous pouvez trier la liste par colonne en cliquant sur **l’en-tête** de la colonne concernée. Cliquez à nouveau pour inverser l’ordre de tri.

## Créer une nouvelle période de planification

Pour créer une nouvelle période de planification, cliquez sur *Créer une période de planification*{:.doc-button} en haut à droite. Dans la fenêtre qui s’ouvre, vous pouvez sélectionner une unité opérationnelle, ainsi qu’un groupe, une plage de dates, une date limite et un statut pour celle-ci. Étant donné que ces informations dépendent du statut de la période de planification, vous trouverez plus d’informations dans les articles listés [en haut de la page](#périodes-de-planification).

## Modifier une période de planification

Pour mettre à jour le statut d’une période de planification, sélectionnez un nouveau statut depuis la liste déroulante dans la colonne **Statut**. Le nouveau statut sera sauvegardé automatiquement.

Pour modifier tous les paramètres d’une période de planification (y compris son statut), passez votre curseur dessus et cliquez sur _![l’icône crayon](/assets/img/common/item-edit.gif)_{:.doc-button-icon} à droite.

## Supprimer des périodes de planification

Pour supprimer des périodes de planification, cochez les **cases** à gauche de la liste. La case située tout en haut de la liste permet de sélectionner toutes les entrées affichées. Cliquez sur *Supprimer la sélection*{:.doc-button} sous la liste.
