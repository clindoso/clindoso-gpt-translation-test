---
title: Optimisation des activités
description: Optimisation des activités.
product_label:
  - advanced
  - enterprise
redirect_from:
  - /fr/schedules-optimisation-activites/
redirect_reason: Updated filename on 21 April 2022
---

Le menu *Plan > Schedules*{:.breadcrumbs} vous permet d'optimiser les plannings de vos employés. Trois options d'optimisation sont possibles :

- *Création d'un planning optimisé* : le système crée les plannings en utilisant tous les **modèles horaires** à sa disposition pour assurer la meilleure couverture du besoin en personnel de chaque activité.
- *Optimisation des activités* : le système optimise uniquement les **activités** des employés. Les heures de début et de fin des journées de travail ne sont donc pas modifiées. Les activités déjà inscrites dans le planning sont modifiées si nécessaire et si la configuration le permet. Toutes les activités sont optimisées, y compris les activités de type Pause.
- *Optimisation des pauses* : le système positionne les **pauses** et toutes autres activités à corridor de telle sorte que la couverture du besoin en personnel soit optimisée.

## Optimisation des activités

L'Optimisation des activités est utilisée lorsque des Modèles horaires et des Activités sont déjà inscrits dans le planning, soit parce qu'une optimisation a déjà été réalisée, soit parce que des Rotations d'horaires ont été insérées.

Lors de ce processus, des Activités peuvent être remplacées par d'autres pour couvrir au mieux le besoin en personnel. Les heures de début et de fin des journées planifiées restent inchangées.

L'*Optimisation des activités* inclut également l'*Optimisation des pauses*. Les pauses variables sont déplacées au moment le plus pertinent, tout en respectant les contraintes spécifiées dans le Modèle horaire.

**Exemple**

Le planning d'un Employé contient déjà l'Activité *E-mail* de 8h à 12h, une pause déjeuner de 12h à 13h et l'Activité *Présent* de 13h à 17h. L'Activité *Présent* est remplaçable, mais pas l'Activité *E-mail*.
Entre 13h et 17h il y a un besoin non couvert sur l'Activité *Téléphone*.
En lançant une *Optimisation des activités*, le système vérifiera que l'Employé possède bien la Compétence sur l'Activité *Téléphone* et remplacera l'Activité *Présent* par l'Activité *Téléphone* en conséquence.

### Paramétrer injixo pour des résultats optimaux

Cette option utilise les objets d'administration suivants :

- **Employés** : seuls les plannings des Employés avec les bonnes Compétences seront modifiés.
- **Activités** :
  - *Planifiable automatiquement* : seules les activités dont la case *Planifiable automatiquement* est cochée sont optimisées.
  - *Remplaçable* : les activités dont la case *Remplaçable* est cochée peuvent être remplacées lors de l'optimisation.
  - *Ordre d'importance* : l'optimisation tient compte de l'ordre d'importance des activités entre elles.
  - *Priorité* : si la règle de planification *2660*{:.id-label} *Respecter les priorités des activités* est activée, seules les Activités avec une Priorité plus élevée pourront remplacer des Activités déjà planifiées.

### Optimiser les activités

Suivez les étapes suivantes pour optimiser les activités :

1. Aller à *Plan > Schedules*{:.breadcrumbs}.
2. Cliquer sur **Actions de planification** puis **Optimisation des activités**.
3. Définir **la période** (la période sélectionnée dans *Schedules* est affichée par défaut).
4. Sélectionner **l'Unité opérationnelle** et éventuellement **le Groupe** dans la fenêtre de dialogue. Si vous sélectionnez un Groupe, seuls les plannings des Employés appartenant à ce Groupe seront générés.
5. Cliquer sur *Démarrer l'optimisation*{:.doc-button} pour lancer le processus.

{{ 1 | image: "paramètres optimisation", '70%' }}

Les plannings sont verrouillés lors de l'Optimisation sur la période concernée, vous ne pouvez donc pas les modifier lors de ce processus.

Vous pouvez suivre l'état d'avancement de l'optimisation au menu *WFM > Administration > Système > JobProcessor*{:.breadcrumbs}.

> Remarque
>
> L'optimisation est un processus complexe. C'est grâce à un nombre très élevé d'itérations que le système peut trouver la meilleure combinaison possible respectant les contraintes de planification et le besoin en personnel des différentes Activités. Le temps de calcul dépend de la quantité de données à traiter, c'est à dire le nombre d'Activités, de Compétences, d'Employés, la période, etc.
