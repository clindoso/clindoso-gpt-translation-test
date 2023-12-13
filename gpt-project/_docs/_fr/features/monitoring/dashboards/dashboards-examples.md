---
title: Exemples de Dashboards
description: Quelques exemples de Dashboards.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /fr/dashboards-exemples/
redirect_reason: Updated filename on 21 April 2022
---

Le menu *Analyze > Dashboards*{:.breadcrumbs} vous permet de consulter en détail les données relatives à vos Workloads et vos Unités opérationnelles à l’aide de tableaux de bord intra et interjournalier.

Suivez les étapes suivantes pour créer un nouveau tableau de bord :

1. Allez à *Analyze > Dashboards*{:.breadcrumbs}
2. Cliquez sur _![Context menu](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon}
3. Sélectionnez **Créer un nouveau tableau de bord**

Voici quelques exemples de tableaux de bords utiles pour la gestion quotidienne et facilement réalisables dans **Dashboards**.

## Occupation vs. Besoin par Activité

Le tableau de bord suivant permet de contrôler que le besoin en personnel d'une Activité est correctement couvert.

1. Dans l'arborescence située à gauche de la zone de graphe, choisissez l'*Unité opérationnelle* concernée puis allez à *Activités > Présence*{:.breadcrumbs}.
2. Sélectionnez l'**Activité** concernée.
3. Glissez-déposez **Besoin** et **Planning occupation** dans la zone de graphe à droite.

{{ 1 | image: 'requirement vs staffing weekly' }}

## Occupation totale vs. Besoin total

Le tableau de bord suivant permet de contrôler que le besoin total de toutes les *Activités* de type *Présence* d'une *Unité opérationnelle* est correctement couvert.

1. Dans l'arborescence située à gauche de la zone de graphe, choisissez l'*Unité opérationnelle* concernée puis allez à *Activités > Présence > Totaux Présence*{:.breadcrumbs}.
2. Glissez-déposez **Besoin** et **Planning occupation** dans la zone de graphe à droite.

{{ 5 | image: 'Total Presences vs. Requirement with Coverage' }}

## Appels prévus vs. Appels reçus

Le tableau de bord suivant permet de contrôler la qualité de la prévision en comparant *Appels prévus* et *Appels reçus*. La *Couverture* de l'activité est également utilisée ici pour contrôler si vous avez assez d'employés pour couvrir d'éventuels pics d'appels. Avant de créer ce graphique, nous avons sauvegardé la prévision dans la version *Opérationnel*.

1. Dans l'arborescence située à gauche de la zone de graphe, cliquez sur **Workloads** et sélectionnez le Workload concerné.
2. Glissez-déposez **Appels reçus Historique** et **Appels reçus - Opérationnel** dans la zone de graphe à droite.
3. Dans l'arborescence située à gauche de la zone de graphe, cliquez sur **Unités opérationnelles**.
4. Choisissez l'*Unité opérationnelle* concernée puis allez à *Activités > Présence*{:.breadcrumbs}.
5. Sélectionnez l'*Activité* d'appels planifiée pour en lien avec le *Workload* puis glissez-déposez la **Couverture** dans la zone de graphe.

{{ 2 | image: 'Forecasted Calls', '50%' }}

## Absences par Unité opérationnelle

Le tableau de bord suivant permet de contrôler les absences, congés ou réunions renseignés pour chaque Unité opérationnelle sur une période définie par l'utilisateur.

1. Dans l'arborescence située à gauche de la zone de graphe, cliquez sur **Unités opérationnelles**.
2. Choisissez l'*Unité opérationnelle* concernée puis allez à *Activités*{:.breadcrumbs}.
3. Sélectionnez le type d'activité puis l'**Activité** concernée.
4. Glissez-déposez **Planning occupation** dans la zone de graphe à droite.
5. Faire de même pour toutes les autres *Activités* concernées.

{{ 3 | image: 'Absences, breaks, vacation, illnesses', '50%' }}

## Appels reçus vs. Appels répondus

Le tableau de bord suivant permet de contrôler le nombre d'appels reçus et le nombre d'appels répondus.

1. Dans l'arborescence située à gauche de la zone de graphe, cliquez sur **Workloads** et sélectionnez le Workload concerné.
2. Glissez-déposez **Appels reçus Historique** et **Appels répondus Historique** dans la zone de graphe à droite.

{{ 4 | image: 'Comparison incoming and answered calls', '50%' }}

> Remarque
> 
> N'oubliez pas de sauvegarder vos graphiques. Renseigner un **Nom** pour votre tableau de bord puis cliquez sur **Sauvegarder**.
