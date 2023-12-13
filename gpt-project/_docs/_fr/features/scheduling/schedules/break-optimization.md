---
title: Optimisation des pauses
product_label:
  - advanced
  - enterprise
permalink: /fr/optimisation-pauses/
redirect_from:
  - /fr/schedules-optimisation-pauses/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
---

<!-- permalink reason: /optimisation-pauses/ used in email and in Intercom message-->

L'optimisation des pauses permet au système de positionner les pauses et toutes autres activités à corridor de telle sorte que la couverture du besoin en personnel soit optimisée. L'utilisation de modèles mathématiques garantit une couverture optimale et vous fera gagner un temps précieux en évitant de multiples ajustements manuels.

## Fonctionnalité

Pour utiliser cette fonctionnalité, il faut qu'un planning ait été préalablement créé sur la période concernée. L'optimisation des pauses ajuste les pauses à l'intérieur du corridor créé dans le Modèle horaires. Les heures de début et de fin de la pause peuvent être modifiées, mais les heures de début et de fin de journée seront conservées.
Lors de l'optimisation, le système ne peut positionner la pause que sur des Activités de type _Présence_. Des Activités d'un autre type limiteront les possibilités d'optimisation.

## Optimiser les pauses

Suivez les étapes suivantes pour démarrer une optimisation des pauses :

1. Aller à _Plan > Schedules_{:.breadcrumbs}.
2. Cliquer sur **Actions de planification** puis **Optimisation des pauses**.
3. Sélectionner **l'Unité opérationnelle** et éventuellement **le Groupe**.
4. Définir **la période**.
5. Cliquer sur _Optimiser_{:.doc-button} pour démarrer le processus.

Une fois le processus lancé, une ligne apparaît à la section **Récapitulatif** et affiche la date de l'optimisation, l'identifiant de l'utilisateur ayant lancé l'optimisation, l'Unité opérationnelle, le Groupe et la période concernée. La colonne **Statut** précise que l'optimisation est en cours.

## Statut de l'optimisation

La colonne **Statut** indique à l'utilisateur l'état de l'optimisation. L’optimisation est un processus complexe, et c’est grâce à un nombre très élevé d’itérations que le système peut trouver la meilleure combinaison possible respectant les contraintes de planification et le besoin en personnel des différentes Activités. Le temps de calcul dépend donc de la quantité de données à traiter, c’est à dire le nombre de pauses à optimiser, le nombre d’Employés, la période, etc.
La durée totale peut aller de quelques secondes à plusieurs minutes.

Une fois le processus terminé, la colonne **Statut** se met à jour automatiquement et affiche un des statuts détaillés ci-dessous.

### Optimisation complète

L'optimisation a été réalisée avec succès et le résultat a été automatiquement inscrit dans la catégorie _Planning_.

### Optimisation partielle

Certaines pauses n'ont pu être optimisées.

Il peut y avoir 2 causes :

1. Certaines pauses n'ont pu être écrites dans le planning de certains employés, elles ont donc été laissées à leur position initiale.
2. Certaines pauses ont été exclues de l'optimisation car, soit leur durée est inférieure à 5 minutes, soit leur durée n'est pas compatible avec l'intervalle de planification de l'Unité opérationnelle.

### L'optimisation a échoué. Merci d'essayer à nouveau.

Une erreur interne a fait échouer l'optimisation. Vous pouvez essayer à nouveau de lancer une optimisation. Créez un {% link_new Ticket | support/create-ticket.md %} si le problème persiste.

{{ 1 | image: "Vue résultats"}}

## Visualiser les résultats de l'optimisation

Cliquer sur **Voir les résultats** de la colonne **Statut** pour afficher les résultats de l'optimisation.

Les informations affichées dans la section supérieure de la page sont :

- La date à laquelle le processus a été lancé
- L'identifiant de l'utilisateur qui a lancé le processus
- L'Unité opérationnelle et éventuellement le Groupe
- La période d'optimisation
- Dans le cas d'une optimisation partielle, le nombre de pauses optimisées

La section principale de la page affiche l'écart total (+/- 0 employés) par rapport à une couverture parfaite des plannings avant (ligne jaune) et après (ligne verte en pointillés) l'optimisation. Le but de l'optimisation est d'obtenir une couverture la plus proche de 0.
Chaque intervalle du graphique représente l'écart total de toutes les Activités de type _Présence_. Les 2 courbes du graphique montrent les intervalles sur lesquels l'optimisation des pauses a amélioré votre couverture.

Pour une période inférieure à 3 jours, le graphique affiche les intervalles de chaque journée. Pour une période supérieure à 4 jours, une valeur consolidée par jour est affichée. Cliquer sur une journée en particulier pour afficher le détail de celle-ci. Cliquer sur _Retour à la vue journalière_{:.doc-button} pour revenir à l'écran précédent.

{{ 2 | image: "Graphique couverture"}}

Prenons par exemple une Unité opérationnelle avec 2 Activités planifiées, "Appels entrants" et "E-mails".

| Activités       | Couverture     | Ecart par rapport à 0 |
| --------------- | -------------- | --------------------- |
| Appels entrants | [0, -2, -1, 0] | [0, 2, 1, 0]          |
| E-mails          | [3, 2, 2, 0]   | [3, 2, 2, 0]          |
|                 | **Total**      | [3, 4, 3, 0]          |

La couverture de ces 2 Activités entre 10h et 11h est [0, -2, -1, 0] pour "Appels entrants" et [3, 2, 2, 0] pour "E-mails". L'écart par rapport à une couverture parfaite est donc de [0, 2, 1, 0] pour "Appels entrants" et [3, 2, 2, 0] pour "E-mails". Le graphique montre ces valeurs pour les 2 Activités et également l'écart total par rapport à 0 qui est ici [3, 4, 3, 0].
