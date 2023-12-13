---
title: Valeur priorité pour les activités
product_label:
  - advanced
  - enterprise
  - classic
description: Découvrez comment éviter que certaines activités soient remplacées par d’autres.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

Vous pouvez définir une valeur de priorité pour chaque activité dans _Plan > Configuration > Activités_{:.breadcrumbs}.
La priorité définit quelles activités peuvent être remplacées par d’autres pendant la mise à jour manuelle ou l’optimisation du planning.

## À quoi sert la priorité pour les activités&nbsp;?

Par défaut, toutes les activités ont la même priorité. Certaines activités peuvent donc être remplacées par d’autres si leur besoin en personnel est différent. Vous pouvez protéger certaines activités pour éviter qu’elles ne soient remplacées à l’aide de la valeur Priorité (valeur par défaut&nbsp;: 1).

Une activité dont la priorité est élevée (valeur la plus élevée&nbsp;: 1) ne peut être remplacée par les activités dont la priorité est plus faible. Vous pouvez utiliser cette valeur pour vous assurer qu’une certaine activité ne soit pas remplacée par une autre.

## Prérequis

Pour prioriser les activités à l’aide de la valeur de priorité, les conditions suivantes doivent être remplies&nbsp;:

- Les activités à prioriser sont configurées comme {% link_new Remplaçables | features/administration/activity-types-and-properties.md | #propriétés-des-activités %}.
- Si les activités sont de type Présence, elles doivent avoir un besoin en personnel.
- La règle de planification _2660_{:.id-label} _Respecter les priorités des activités_ est activée.

## Exemple 1&nbsp;: activités de type Présence

- Vous avez créé deux activités&nbsp;: Hotline B2B et Hotline B2C.
- Les deux activités sont de type {% link_new Présence | features/administration/activity-types-and-properties.md | #types-dactivité %}.
- L’activité Hotline B2B est prioritaire et ne doit jamais être remplacée par l’activité Hotline B2C.

Après avoir créé un premier planning, vous recalculez votre besoin en personnel en fonction des événements actuels pour les deux activités pour vérifier que vos deux activités disposent bien de la couverture nécessaire. Si le besoin en personnel pour Hotline B2C a augmenté, optimisez les activités pour vous assurer que les activités sont correctement équilibrées. Cependant, le moteur d’optimisation risque de réassigner des employés de Hotline B2B vers Hotline B2C dans le planning.

Pour vous assurer que l’activité Hotline B2B ne soit jamais remplacée par Hotline B2C, assignez une valeur de priorité de 1 à l’activité Hotline B2B et une plus faible priorité (c’est à dire un nombre supérieur à 1) à B2C hotline.

S’il n’y a pas assez de personnel pour gérer les deux activités en même temps, injixo garantira que l’activité Hotline B2B soit toujours couverte avant Hotline B2C.

## Exemple 2&nbsp;: maladie et télétravail

- Vous avez créé deux activités&nbsp;: Maladie et Télétravail
- Les deux activités sont de type {% link_new Absence | features/administration/activity-types-and-properties.md | #types-dactivité %}.

Étant donné que les deux activités sont de type Absence, elles n’ont pas de besoin en personnel. Si vous insérez des rotations d’horaires qui incluent l’activité Télétravail sans définir de priorité, injixo risque de remplacer l’activité Maladie par Télétravail. Cela peut poser des problèmes pour les employés malades ce jour et planifiés pour l’activité Télétravail.

Pour éviter que Maladie ne soit remplacée par Télétravail, assignez une priorité de 1 à l’activité Maladie et de 2 (ou supérieur) à Télétravail. Ceci garantira que l’activité Maladie ne soit pas remplacée par l’activité Télétravail.
