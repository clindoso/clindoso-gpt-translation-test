---
title: Désactiver, réactiver et supprimer des employés
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Découvrez quand et comment désactiver, réactiver ou supprimer des employés.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/how-does-billing-work.md
---

Si vous souhaitez interrompre la planification de certains employés ou si ceux-ci n’ont plus besoin d’accéder à injixo, vous pouvez les désactiver ou les supprimer. Les conséquences sont les suivantes&nbsp;:

- Les employés désactivés perdent leur accès à injixo.
- Votre organisation ne sera plus {% link_new facturée | getting-started/how-does-billing-work.md %} pour ces employés (à partir du mois suivant).

## Désactiver un employé

Si certains employés ne sont pas disponibles pour travailler pendant une période prolongée, par exemple lors d’un congé sabbatique ou parental, vous pouvez les désactiver temporairement. Votre organisation ne sera pas facturée pour les employés désactivés. Vous pouvez réactiver les employés lorsqu’ils sont de nouveau disponibles. Dans certains cas, le Règlement général sur la protection des données (RGPD) européen peut vous obliger à supprimer les données d’un employé. Si tel est le cas, [supprimez](#supprimer-un-employé) l’employé.

Pour désactiver un employé, suivez ces étapes&nbsp;:

1. Accédez à _Plan > Configuration > Employés_{:.breadcrumbs}.
2. Dans la liste des employés, cliquez sur l’employé que vous souhaitez désactiver.
3. Dans la section **Périodes d’emploi** de la boîte de dialogue de configuration de l'employé, cliquez sur l’{% icon item-edit %}.
4. Entrez une date de départ.<br>Une date de départ située dans le passé désactivera immédiatement l’employé. Une date de départ située dans le futur désactivera l’employé à la date spécifiée.
5. Cliquez sur _OK_{:.doc-button}.<br>Un message de confirmation apparaît.
6. Pour supprimer les plannings futurs mais conserver les données de planification historiques, cliquez sur _Oui_{:.doc-button}. Pour conserver toutes les données de planification de l’employé désactivé, cliquez sur _Non_{:.doc-button}.

### Créer une liste des employés désactivés

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur l’onglet **Utilisateurs non facturés**.<br>Le tableau affiche tous les utilisateurs désactivés pour lesquels votre organisation n’est pas facturée.

### Réactiver un employé

Pour réactiver un employé, par exemple lorsqu’il revient après une longue absence, suivez ces étapes&nbsp;:

1. Accédez à _Plan > Configuration > Employés_{:.breadcrumbs}.
2. Utilisez le champ de recherche en haut à gauche pour rechercher l’employé que vous souhaitez réactiver.<br>Une fenêtre s’ouvre. Si vous avez saisi le nom complet de l’employé et que la recherche ne renvoie qu’un seul résultat, la fenêtre affiche la fiche de l’employé. Si la recherche renvoie plusieurs résultats, la fenêtre affiche une liste d’employés.
3. Si la fenêtre affiche une liste, cliquez sur l’employé que vous souhaitez réactiver.
4. Dans la section **Périodes d’emploi** de la fiche employé, cliquez sur l’{% icon item-add %}.
5. Entrez une date d’entrée. 
6. Cliquez sur _OK_{:.doc-button}.

## Supprimer un employé

> Attention
>
> Vous ne pouvez pas réactiver un employé supprimé. Il sera supprimé de tous les plannings actuels et futurs dont il fait partie. La suppression d’un employé n’impacte pas les données historiques d’adhérence dans {% link_new Intraday | features/intraday/adherence-intraday.md %}.

Nous recommandons de supprimer les employés uniquement lorsque leur période d’emploi a pris fin de manière permanente. Lorsque les employés sont absents pendant une période prolongée, par exemple lorsqu’ils prennent un congé sabbatique ou parental, nous recommandons de les [désactiver](#désactiver-un-employé).

Pour supprimer un employé, suivez ces étapes&nbsp;:

1. Accédez à _Plan > Configuration > Employés_{:.breadcrumbs}.
2. Dans la liste des employés, cliquez sur l’employé que vous souhaitez supprimer.
3. Cliquez sur l’{% icon item-delete %} dans la barre d’action.<br>Un message de confirmation apparaît.
4. Cliquez sur _Oui_{:.doc-button}.<br>L’employé et tous ses plannings actuels et futurs sont supprimés d’injixo.

Lorsque vous supprimez un employé d’injixo, ses données personnelles sont anonymisées afin de garantir sa confidentialité. injixo conserve l’identifiant de l’employé mais le marque comme supprimé, et remplace son nom par des astérisques. injixo modifie également les données personnelles comme les noms, le matricule, les adresses, les numéros de téléphone et les adresses e-mail. Si la configuration de l’employé incluait des numéros internes d’identification, injixo les supprime entièrement.
