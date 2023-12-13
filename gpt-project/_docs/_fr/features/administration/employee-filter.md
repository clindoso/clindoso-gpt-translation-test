---
title: Configurer les filtres avancés
description: Utilisez l'éditeur de filtre avancé pour filtrer les employés en combinant différents critères.
product_label:
  - advanced
  - enterprise
  - classic
---

Avec les filtres avancés, vous pouvez créer des listes d’employés sur la base de plusieurs critères. Les options d’édition dépendent de vos droits d’utilisateur.

Les filtres avancés fonctionnent de manière similaire aux {% link_new groupes | features/administration/selections.md %}. Différences entre le filtre employé et les groupes&nbsp;:

- Pour les filtres avancés, les critères de regroupement sont basés sur des éléments de configuration, tels que l’unité opérationnelle, les compétences et le contrat.
- Pour les groupes, vous pouvez créer vos propres critères de regroupement.

Les filtres avancés sont disponibles uniquement dans injixo Classic, Advanced et Enterprise.
  
Pour accéder à l'éditeur de filtres, accédez à _Plan > Centre de planification_{:.breadcrumbs} et cliquez sur **Éditeur de filtres**.

   {{ 1 | image: 'Filtre avancé', '70%' }}

## Créer un filtre

1. Dans la section **Filtre avancé**, cliquez sur l’icône Créer un filtre {% icon item-add | icon-only %}.
2. Sélectionnez une **Période**&nbsp;:<br>
    - **Librement sélectionnable**&nbsp;: spécifiez la période manuellement. Sélectionnez une date de début (**Du**) et de fin (**Au**).<br>
    - **Relative**&nbsp;: spécifiez une période pour la semaine, le mois ou l’année suivant(e), en cours ou précédent(e).<br>
    - **Prédéfinie**&nbsp;: la date de la période est automatiquement définie sur la journée en cours.
3. Créez une [**requête**](#créer-une-requête).
4. Pour voir les résultats, cliquez sur _Afficher_{:.doc-button}.
5. Cliquez sur _Appliquer_{:.doc-button}.
6. Pour sauvegarder, cliquez sur l’icône Enregistrer un filtre {% icon save | icon-only %}.<br>Pour enregistrer un filtre existant sous un autre nom, cliquez sur l’icône Enregistrer un filtre sous... {% icon saveas | icon-only %}.

## Créer une requête

Une requête est un ensemble de conditions permettant de filtrer et de récupérer des données sur un ensemble de données plus large. Vous pouvez définir des critères et récupérer une liste d’employés qui satisfont ces critères.

1. Dans la section **Définir la requête**, cliquez sur l’{% icon item-add %}.
2. Dans le **premier menu déroulant**, sélectionnez un type de données de configuration.
3. Dans le **second menu déroulant**, sélectionnez une condition.
4. (Facultatif) Sélectionnez des [options et des opérateurs relationnels](#utiliser-la-priorité-et-les-opérateurs-relationnels) pour les unités opérationnelles, les catégories d’employés ou les compétences.
5. Cliquez sur _Appliquer_{:.doc-button}.

Pour modifier une requête, cliquez sur l’{% icon item-edit %}.

## Utiliser les conditions

### IS IN

La condition **IS IN** affiche les résultats qui correspondent strictement à la requête.
 
1. Sélectionnez un type de données de configuration dans le **premier menu déroulant**.
2. Sélectionnez **IS IN** dans le **second menu déroulant**.
3. Cliquez sur _Critères avancés_{:.doc-button} pour voir les critères disponibles et les sélectionner dans la liste.
4. Pour ajouter des critères à votre sélection, cliquez sur l’{% icon right-arrow-blue %}.
5. Dans la fenêtre **Sélectionner des critères avancés**, cliquez sur _Appliquer_{:.doc-button}.
6. (Facultatif) Sélectionnez des [options et des opérateurs relationnels](#utiliser-la-priorité-et-les-opérateurs-relationnels) pour les unités opérationnelles, les catégories d’employés ou les compétences.
7. Cliquez sur _Appliquer_{:.doc-button}.

### IS LIKE

La condition **IS LIKE** affiche les résultats qui correspondent partiellement à la requête.

1. Sélectionnez un type de données de configuration dans le **premier menu déroulant**.
2. Sélectionnez **IS LIKE** dans le **second menu déroulant**.
3. Saisissez le texte correspondant à votre recherche dans le **champ de texte**.
    - Pour remplacer plusieurs caractères, utilisez le caractère générique *.
    - Pour remplacer un caractère spécifique, utilisez le caractère générique ?.
4. (Facultatif) Sélectionnez des [options et des opérateurs relationnels](#utiliser-la-priorité-et-les-opérateurs-relationnels) pour les unités opérationnelles, les catégories d’employés ou les compétences.
5. Cliquez sur _Appliquer_{:.doc-button}.

## Utiliser la priorité et les opérateurs relationnels

Avec la case Priorité et les opérateurs relationnels, vous pouvez inclure des employés selon leur priorité et leur appartenance à l’unité opérationnelle/catégorie d’employé séléctionnée&nbsp;:  

1. Sélectionnez **Unité opérationnelle** ou **Catégorie d’employé** dans le premier menu déroulant. 
2. Cochez la case **Priorité**.
3. Sélectionnez un opérateur relationnel dans la liste.
4. Saisissez une valeur de priorité dans le champ de saisie.

Avec l’élément de configuration Compétence, vous pouvez utiliser des opérateurs relationnels pour inclure uniquement les employés possédant un certain niveau de compétence&nbsp;:  

1. Sélectionnez **Compétence** dans le premier menu déroulant.
2. Cochez la case **Niveau de qualification**.
3. Sélectionnez un opérateur relationnel dans la liste.
4. Saisissez la valeur du niveau de compétence dans le champ de saisie.

## Associer des requêtes

Vous pouvez associer des requêtes entre elles&nbsp;:

1. Créez ou sélectionnez un [filtre](#créer-un-filtre).
2. Créez une [requête](#créer-une-requête).
3. Sélectionnez un opérateur conditionnel&nbsp;:<br>
  - **AND**&nbsp;: inclut les employés qui satisfont toutes les conditions.  
  - **OR**&nbsp;: inclut les employés qui satisfont au moins une condition.  
  - **NOT**&nbsp;: exclut les employés qui satisfont la condition suivant NOT.
4. Créez une deuxième requête.
5. Cliquez sur _Appliquer_{:.doc-button}.

Pour créer un groupe, ouvrez une parenthèse. Pour refermer le groupe, refermez la parenthèse. Utilisez les flèches vers le haut et vers le bas pour déplacer et trier les requêtes à tout moment.

## Exemple de requête

Pour filtrer les employés de l’unité opérationnelle New York qui n’ont pas de contrat Temps Plein 40&nbsp;h et ne font pas partie du groupe Heures Supplémentaires, la requête doit suivre cette structure&nbsp;:


```
Unité opérationnelle IS IN "New York"
AND
NOT
(
Contrat IS IN "Temps Plein 40&nbsp;h"
AND
Groupe IS IN "Heures Supplémentaires"
)
```

Cette requête sélectionne tous les employés de l’unité opérationnelle, puis exclut les employés ayant un contrat Temps Plein 40&nbsp;h et appartiennent au groupe Heures Supplémentaires&nbsp;:

- **IS IN** définit la condition pour l’unité opérationnelle.
- **AND** combine les conditions de la requête.
- **NOT** exclut les conditions suivantes.
- Les parenthèses regroupent les conditions à exclure.
- **IS IN** sélectionne les employés ayant le contrat Temps Plein 40&nbsp;h.
- **AND** combine les conditions à l’intérieur des parenthèses.
- **IS IN** sélectionne les employés appartenant au groupe Heures Supplémentaires.

## Modifier les filtres

1. Dans le menu déroulant **Filtre avancé**, sélectionnez un filtre.
2. Modifiez les informations que vous souhaitez changer.
3. (Facultatif) Pour renommer votre filtre, cliquez sur le bouton.
4. Pour sauvegarder, cliquez sur l’icône Enregistrer un filtre {% icon save | icon-only %}.<br>Pour enregistrer votre filtre sous un autre nom, cliquez sur l’icône Enregistrer un filtre sous... {% icon saveas | icon-only %}.
