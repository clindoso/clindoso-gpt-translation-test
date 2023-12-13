---
title: Copie des catégories - sauvegarde, comparaison et ajustement des plannings
redirect_from:
  - /fr/copie-categories/
redirect_reason: Filename changed in April 2022
---

En tant que planificateur de centres de contacts, vous avez parfois besoin d’utiliser plusieurs options pour planifier les horaires de vos employés, non seulement lors de la création de nouveaux plannings et lors de la modification de ceux-ci suite à des éléments exogènes tels que les pics d’appels ou l’augmentation du taux d’absentéisme de vos employés. Le *Centre de planification*{:.menu-item} intègre une fonction de retour arrière suite à une modification (flèche “Undo”) et vous pouvez afficher l'historique des modifications de planning pour chaque employé. Le *Centre de planification*{:.menu-item} inclut également le concept de multiples versions de planning, appelées *Catégories*{:.menu-item}. La fonction de *copie de Catégories*{:.menu-item} vous permet de conserver des copies des plannings de vos unités opérationnelles, de suivre les modifications que vous avez apportées aux plannings et d'expérimenter des changements dans une catégorie "bac à sable" avant d’appliquer la meilleure solution aux plannings définitifs.

## Pourquoi copier des Catégories ?

Rien n'est plus ennuyeux que de faire une erreur dans vos plannings et de ne pas avoir la possibilité de restaurer rapidement l'état précédent. Par exemple, si vos plannings contiennent les congés validés et que vous les écrasez ou les supprimez, ces congés seront perdus et vous aurez beaucoup de mal à récupérer toutes ces données. Il est donc judicieux de conserver une copie de sauvegarde à partir de laquelle vous pouvez restaurer l'état d'origine de vos plannings. Nous vous recommandons de conserver une copie de vos plannings contenant les congés validés dans la Catégorie `Sauvegarde 1` par exemple.

L'écart entre le volume d'appels ou le Temps moyen de traitement réel et les prévisions est une réalité dans la planification des centres de contacts. Lorsque cela se produira, vous voudrez bien évidemment ajuster vos plannings pour faire face à la nouvelle demande. Afin de ne pas mettre à la poubelle les plannings publiés en expérimentant des changements, nous vous recommandons de faire une copie de ceux-ci dans la Catégorie `Etat actuel`. Vous pouvez ainsi voir d'un coup d'œil les avantages et les inconvénients qui découlent des changements que vous proposez, par exemple l'impact sur la couverture de vos activités dans la Heatmap.

Les écarts par rapport aux prévisions et donc les corrections de planification font partie des activités quotidiennes des planificateurs. Le plus important est de tirer les leçons des changements que vous devez apporter à vos plannings. Afin de comprendre quels ajustements sont effectués chaque jour par l'équipe d’hypervision ou les superviseurs, vous devez copier vos plannings dans la catégorie `Etat actuel`et effectuer tous vos autres ajustements et ré-optimisations intrajournaliers sur celle-ci. En comparant les Catégorie `Planning` et `Etat actuel`, vous pouvez ensuite identifier les facteurs qui ont eu le plus d'impact sur votre planification, afin que vous puissiez apprendre et améliorer vos plannings futurs. Par exemple, si vous constatez à maintes reprises que vous devez ajuster les horaires pour couvrir un taux d’absentéisme trop élevé, vous pourriez augmenter le Shrinkage que vous utilisez dans votre dimensionnement ou suggérer des mesures managériales comme des réunions individuelles pour réduire ce taux.

## Comment copier des Catégories ?

Dans la section WFM, allez dans *Planification > SchedulePro > Périodes de planification*{:.breadcrumbs}.

{{ 1 | image: "Liste période de planification", '80%' }}

Vous pouvez créer ou modifier une période de planification existante de type `Standard`, en spécifiant les dates de début et de fin sur lesquelles vous souhaitez copier les Catégories.

{{ 2 | image: "création d'une période de planification", '75%' }}

Une fois la Période de planification créée ou modifiée, dans la partie droite de l’écran, vous trouverez toutes les actions que vous pouvez effectuer sur celle-ci. Cliquez sur *Copier*{:.doc-button} dans l’encart `Catégorie`

{{ 3 | image: "menu catégorie - copier - supprimer", '30%' }}

{{ 4 | image: "écran de copie de catégorie", '75%' }}

Choisissez la période et les Catégories Source et Cible et cliquez sur *OK*{:.doc-button}. Vous avez la possibilité de filtrer les employés par groupe, toutefois, nous vous recommandons de copier les plannings pour tous les employés de votre Unité opérationnelle.

Cochez la case `Vider après la copie` si vous voulez recommencer purger les données de la Catégorie après la copie. Si, par contre, vous voulez sauvegarder vos plannings dans la Catégorie `Etat actuel`et laisser le contenu de la Catégorie `Planning` inchangé, assurez-vous que cette case n'est pas cochée

> Remarque
>
> N'oubliez pas que les données de la Catégorie cible seront écrasées pendant la copie. Et il ne sera pas possible de revenir en arrière. Faites donc bien attention à sélectionner la bonne Catégorie de destination.
