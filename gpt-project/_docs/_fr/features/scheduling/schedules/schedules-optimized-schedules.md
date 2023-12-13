---
title: Création d'un planning optimisé
description: Création d'un planning optimisé.
product_label:
  - advanced
  - enterprise
redirect_from:
  - /fr/schedules-creation-planning-optimise/
redirect_reason: Updated filename on 21 April 2022
---

Le menu *Plan > Schedules*{:.breadcrumbs} vous permet d'optimiser les plannings de vos employés. Trois options d'optimisation sont possibles :

- *Création d'un planning optimisé* : le système crée les plannings en utilisant tous les **modèles horaires** à sa disposition pour assurer la meilleure couverture du besoin en personnel de chaque activité.
- *Optimisation des activités* : le système optimise uniquement les **activités** des employés. Les heures de début et de fin des journées de travail ne sont donc pas modifiées. Les activités déjà inscrites dans le planning sont modifiées si nécessaire et si la configuration le permet. Toutes les activités sont optimisées, y compris les activités de type Pause.
- *Optimisation des pauses* : le système positionne les **pauses** et toutes autres activités à corridor de telle sorte que la couverture du besoin en personnel soit optimisée.

## Création d'un planning optimisé

L'option *Création d'un planning optimisé*{:.doc-button} vous permet de créer automatiquement les plannings de vos employés pour assurer la meilleure couverture du besoin en personnel de chaque activité. Pour se faire, le système utilise les Modèles horaires et les Activités préalablement configurés.

### Paramétrer injixo pour des résultats optimaux

Cette option utilise les objets d'administration suivants :

- **Employés** : date de début et de fin de Période d'emploi, Contrat, Compétence(s), Unité(s) opérationnelle(s) et Disponibilités.
- **Contrats** : indication des temps de travail ou répartition des heures sur les jours de la semaine, paramètres de l'AutoScheduler et Règles de planification.
- **Activités** :
    - *Planifiable automatiquement* : seules les activités dont la case *Planifiable automatiquement* est cochée sont optimisées.
    - *Remplaçable* : les activités dont la case *Remplaçable* est cochée peuvent être remplacées lors de l'optimisation.
    - *Ordre d'importance* : l'optimisation tient compte de l'Ordre d'importance des Activités entre elles.
- **Modèles horaires** : seuls les Modèles horaires attribués à l'Unité Opérationnelle sont utilisés lors de l'optimisation.
- **Modèles de planification** : seuls les Modèles de planification attribués à un employé sont utilisés lors de l'optimisation.

### Créer un planning optimisé

Suivez les étapes suivantes pour créer un planning optimisé :

1. Aller à *Plan > Schedules*{:.breadcrumbs}.
2. Cliquer sur **Actions de planification** puis **Création d'un planning optimisé**.
3. Définir **la période**. La période sélectionnée dans *Schedules* est affichée par défaut.
4. Sélectionner **l'Unité opérationnelle** et éventuellement **le Groupe** dans la fenêtre de dialogue. Si vous sélectionnez un Groupe, seuls les plannings des Employés appartenant à ce Groupe seront générés.
5. Cocher la case *Optimisation renouvelée* si vous souhaitez renouveler l'optimisation en cas de modification du besoin en personnel par exemple.
6. Cliquer sur *Démarrer l'optimisation*{:.doc-button} pour lancer le processus.

{{ 1 | image: "paramètres optimisation", '70%' }}

Les plannings sont verrouillés lors de l'Optimisation sur la période concernée, vous ne pouvez donc pas les modifier lors de ce processus.

Vous pouvez suivre l'état d'avancement de l'optimisation au menu *WFM > Administration > Système > JobProcessor*{:.breadcrumbs}.

> Remarque
>
> L'optimisation est un processus complexe. C'est grâce à un nombre très élevé d'itérations que le système peut trouver la meilleure combinaison possible respectant les contraintes de planification et le besoin en personnel des différentes Activités. Le temps de calcul dépend de la quantité de données à traiter, c'est à dire le nombre d'Activités, de Compétences, d'Employés, la période, etc.
