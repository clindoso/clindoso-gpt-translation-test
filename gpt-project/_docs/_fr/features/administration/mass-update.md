---
title: Mise à jour en masse
product_label:
  - advanced
  - enterprise
  - classic
---

Utilisez la mise à jour en masse pour modifier l’affectation de données de configuration pour plusieurs employés en même temps.
Vous pouvez utiliser la fonctionnalité de mise à jour en masse pour les éléments de configuration suivants&nbsp;:

- contrats,
- compétences,
- unités opérationnelles,
- groupes,
- rotations d’horaires,
- modèles de planification.

## Prérequis

Avant de pouvoir utiliser la mise à jour en masse, vous devez {% link_new paramétrer votre configuration minimale | getting-started/set-up-base-configuration.md %}.

## Lancer la mise à jour en masse

> Remarque
>
> Vous ne pouvez pas annuler une mise à jour en masse. Lancez une nouvelle mise à jour en masse pour remplacer les données mises à jour de façon incorrecte, ou modifiez les données pour chaque employé séparément.  

Pour lancer une mise à jour en masse, suivez ces étapes&nbsp;: 

1. Accédez à _Plan > Configuration > Employés_{:.breadcrumbs}.
2. Pour sélectionner les employés dont vous souhaitez modifier les données de configuration, sélectionnez un groupe ou cliquez sur l’icône Filtre avancé {% icon employee-filter | icon-only %}.
3. Dans la barre d’action, cliquez sur l’icône Modification massive {% icon mass-update | icon-only %}.<br>La page de mise à jour en masse s’ouvre. 
4. Dans la section **Paramètres**, utilisez le menu déroulant **Donnée de base** pour sélectionner l’élément de configuration que vous souhaitez modifier pour plusieurs employés en même temps.<br>(Facultatif)&nbsp;: utilisez les champs **Du** et **Au** pour limiter la durée de validité de la mise à jour en masse.
5. Sélectionnez une **Commande**.
6. Selon votre choix, les sections suivantes apparaissent sur la droite&nbsp;: **Attributions actuelles**, **Nouvelle attribution** ou **Nouvelle période de validité**. Dans chaque section, sélectionnez les éléments que vous souhaitez ajouter, supprimer ou remplacer.
7. Pour lancer la mise à jour en masse, cliquez sur **OK**.<br>L’écran de traitement de la tâche s’ouvre.<br>Une page affichant les résultats de votre mise à jour en masse s’ouvre.

| Question                                                                          | Réponse                                                                                                                                                                                      |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------- |
| À la suite d’une mise à jour en masse, pourquoi des contrats sont assignés à mes employés pour une période plus courte qu’avant&nbsp;?                              | Si vous assignez un élément de configuration qui dépasse la période de traitement à un employé, il peut y avoir des périodes sans assignation.<br>Exemple&nbsp;: un contrat est assigné à un employé du 1er mars au 31 mai. Vous saisissez une nouvelle période de validité du 1er mars au 15 avril. Après la mise à jour en masse, il n’y aura aucune assignation entre le 16 avril et le 31 mai.                                                                                                                                           |


