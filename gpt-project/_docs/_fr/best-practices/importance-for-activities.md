---
title: Ordre d’importance pour les activités
product_label:
  - advanced
  - enterprise
  - classic
description: Utilisez l’ordre d’importance pour prioriser certaines activités lors de l’optimisation du planning.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
---

Vous pouvez définir un ordre d’importance pour chaque activité dans _Plan > Configuration > Activités_{:.breadcrumbs}.

## À quoi sert l’ordre d’importance pour les activités&nbsp;?

Par défaut, la fonctionnalité Optimiser les activités planifie en priorité les personnes sur les activités dont le besoin en personnel est le plus faible. Le sureffectif des activités avec un besoin en personnel élevé a un impact moins négatif que le sous-effectif des activités avec un faible besoin en personnel.

Par conséquent, les activités avec un besoin en personnel élevé peuvent se retrouver en sous-effectif si le nombre de personnes disponibles est trop faible. Vous pouvez contourner cette situation en priorisant les activités avec un besoin en personnel élevé à l’aide de l’ordre d’importance (valeur par défaut&nbsp;: 100&nbsp;%). Plus l’ordre d’importance d’une activité est élevé, plus le moteur d’optimisation tentera de répondre au besoin en personnel. 
Vous pouvez utiliser cette fonction pour prioriser une activité par rapport à une autre, par exemple les contacts B2B par rapport aux contacts B2C.

Si une activité a un besoin de 5 personnes, la couverture optimale est de 5. Pour prioriser cette activité, définissez un ordre d’importance élevé (100&nbsp;%). Le moteur d’optimisation tentera alors de planifier les personnes de façon à répondre précisément au besoin en personnel.  

Les activités pouvant être en sureffectif doivent avoir un ordre d’importance inférieur. Pour un ordre d’importance de 20&nbsp;%, le moteur d’optimisation planifie le nombre exact de personnes requis ou plus, s’ils sont disponibles.

## Prérequis

Pour prioriser les activités à l’aide de l’ordre d’importance, les conditions suivantes doivent être remplies&nbsp;:
- Les activités à prioriser sont configurées comme Planifiables automatiquement et Remplaçables.
- Les personnes qui doivent travailler sur les activités priorisées sont planifiées sur l’activité Présent (ID 1).

Si les membres de votre équipe sont planifiés sur d’autres activités non-remplaçables ou si un bloc d’activités est planifié dans leur modèle horaire, l’ordre d’importance n’a aucun effet. L’optimisation ne peut donc pas modifier l’activité pour la journée ou certains intervalles.
De plus, les compétences des personnes et les propriétés des activités comme l’option Planifiable automatiquement peut empêcher l’optimisation d’assigner plus de personnes à cette activité.

## Exemple

- Vous avez créé deux activités, A et B.
- 26 personnes sont disponibles et compétents pour les deux activités.
- Le besoin en personnel est de 10 personnes pour chaque activité.
- L’ordre d’importance de l’activité A est de 20&nbsp;% et celui de l’activité B est de 100&nbsp;%.

Le moteur d’optimisation planifie 10 personnes pour chaque activité, répondant ainsi précisément au besoin. Cependant, il reste 6 personnes à planifier.
L’ordre d’importance de l’activité A est cinq fois inférieur à celui de l’activité B. Le moteur d’optimisation peut donc assigner cinq personnes supplémentaires à l’activité A avant qu’elle n’ait le même impact négatif sur la couverture totale que s’il assignait une seule personnes supplémentaire à l’activité B. Ainsi, injixo aura tendance à sur-planifier l’activité A.
