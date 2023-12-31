---
title: Créer et gérer les groupes
description: Créez des groupes et attribuez des employés à chacun d’entre eux.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from: fr/selections-overview/
redirect_reason: renamed file in April 2022
---

Les groupes sont des critères de regroupement auxquels vous pouvez assigner des employés à des fins de filtrage. Les groupes fonctionnent de manière similaire aux {% link_new filtres avancés | features/administration/employee-filter.md %}.<br>

Différences entre les filtres avancés et les groupes&nbsp;:

- Pour les groupes, vous pouvez créer vos propres critères de regroupement.
- Pour les filtres avancés, les critères de regroupement sont basés sur des éléments de configuration dans injixo, tels que l’unité opérationnelle, les compétences et le contrat.

De plus, les filtres avancés sont disponibles uniquement dans injixo Classic, Advanced et Enterprise.

Les groupes sont couramment utilisés pour regrouper les employés qui&nbsp;:

- rapportent à un superviseur spécifique,
- sont en télétravail,
- ont été embauchés récemment et ont éventuellement besoin d’un soutien ou d’un suivi supplémentaire,
- peuvent remplacer d'autres employés à court terme,
- ont des responsabilités supplémentaires qui ne concernent pas la planification mais qui peuvent être importantes, par exemple, les employés qui ont une formation aux premiers secours.

Si vous utilisez injixo Essential, vous pouvez utiliser les groupes pour regrouper les employés en fonction d’éléments de configuration, tels que l’unité opérationnelle, les compétences et le contrat.

## Créer un groupe

1. Accédez à _Plan > Configuration > Groupes_{:.breadcrumbs}.
2. Cliquez sur l’{% icon item-add %} en haut à gauche.  
    Un panneau de configuration s’ouvre à droite.
3. Remplissez les champs suivants&nbsp;:
    - **Nom**&nbsp;: nom unique pour le groupe (max. 50 caractères).
    - **Abréviation**&nbsp;: abréviation du nom (max. 25 caractères).
    - **Description**&nbsp;: description facultative permettant aux autres utilisateurs de comprendre ce que représente le groupe.
4. Cliquez sur _OK_{:.doc-button}.

## Assigner des employés aux groupes

Pour assigner des employés à des groupes, vous devez d’abord {% link_new créer un groupe | features/administration/selections.md | #créer-un-groupe %}.

1. Accédez à _Plan > Configuration > Employés_{:.breadcrumbs}.
2. Cliquez sur l’employé que vous souhaitez assigner à un groupe.  
   Un panneau de configuration s’ouvre à droite.
3. Dans la section **Groupes**, cliquez sur l’{% icon item-add %}.
4. Cliquez sur le groupe auquel vous souhaitez assigner l’employé.
5. (Facultatif) Entrez une plage de dates dans les champs **Valide du** et **Jusqu’au** pour limiter la période de validité du groupe. Laissez les champs **Valide du** et **Jusqu’au** vides pour rendre le groupe toujours valide. En savoir plus sur les {% link_new périodes de validité | features/administration/set-a-validity-period.md %}.
6. Cliquez sur _OK_{:.doc-button}.

Pour modifier un groupe auquel un employé est assigné, cliquez sur l’{% icon item-edit %}. Pour supprimer l'affectation au groupe, cliquez sur l’{% icon item-delete %}.

## Combiner les groupes

Les clients injixo Classic, Advanced et Enterprise peuvent attribuer des groupes à un groupe existant. Le groupe auquel d’autres groupes sont attribués devient un groupe supérieur. Les groupes assignés sont des groupes subordonnés au groupe supérieur. Cela vous permet de filtrer les employés de tous les groupes subordonnés en une seule fois en utilisant le groupe supérieur.

Pour créer une hiérarchie de groupes entre des groupes subordonnés et un groupe supérieur, {% link_new créez d’abord le groupe supérieur et les groupes subordonnés | features/administration/selections.md | #créer-un-groupe %}.

Pour attribuer un groupe à un autre groupe, procédez comme suit&nbsp;:

1. Cliquez sur le groupe que vous souhaitez utiliser comme groupe supérieur dans la liste des groupes.  
   Un panneau de configuration s’ouvre à droite.
2. Dans la section **Groupes**, cliquez sur l’{% icon item-add %}.
3. Cliquez sur le groupe auquel vous souhaitez assigner l’employé.
4. (Facultatif) Entrez une plage de dates dans les champs **Valide du** et **Jusqu’au** pour attribuer les groupes subordonnés au groupe supérieur pendant une durée limitée. Laissez les champs **Valide du** et **Jusqu’au** vides pour rendre l’affectation toujours valide.
5. Cliquez sur _OK_{:.doc-button}.

Pour modifier ou supprimer un groupe subordonné, cliquez sur l’{% icon item-edit %} ou l’{% icon item-delete %}.

> Hiérarchie de groupe
>
> La hiérarchie entre les groupes supérieurs et subordonnés n’est pas visible dans _Plan > Configuration > Employés_{:.breadcrumbs}. Pour vérifier si un groupe est de niveau supérieur, allez dans _Plan > Configuration > Groupes_{:.breadcrumbs} et cliquez sur un groupe dans la section **Groupes**. Vous pouvez également nommer les groupes supérieurs de manière à rendre la hiérarchie entre les groupes évidente.

## Supprimer un groupe

1. Accédez à _Plan > Configuration > Groupes_{:.breadcrumbs}.
2. Dans la liste, cliquez sur le groupe que vous souhaitez supprimer.
3. Cliquez sur l’{% icon item-delete %} en haut à gauche.
4. Pour confirmer, cliquez sur _Oui_{:.doc-button}.
