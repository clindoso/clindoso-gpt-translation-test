---
title: Vue d'ensemble
product_label:
  - advanced
  - enterprise
toc: false
description: Comment fonctionne le module Capacity
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/capacity/capacity-insert-shift-sequences.md
---

_Plan > Capacity_{:.breadcrumbs} donne un aperçu de vos futurs besoins en matière de recrutement et de formation. C'est ici que vous avez la possibilité de réaliser votre planification à long terme.

> Capacity est encore en cours de développement et d'amélioration. Toutes vos remarques et idées d'évolution peuvent nous être envoyées à *capacity-team@injixo.com*.

## Afficher le capacitaire d'une Unité opérationnelle

Sélectionnez une **Unité opérationnelle** pour afficher le capacitaire de celle-ci sur l'année entière.

Le tableau contient les informations suivantes :

- le _besoin en personnel_ : c'est la somme du besoin en personnel pour toutes les activités de l'unité opérationnelle concernée. Pour que le résultat soit le plus pertinent possible, assurez-vous d'avoir un {% link_new besoin en personnel | features/forecast/injixo-forecast/staff-requirement.md %} pour toutes les activités de votre unité opérationnelle.
- le _capacitaire contractuel_ : c'est la somme du nombre d'heures contractuelles _à effectuer_ par tous les employés de l'unité opérationnelle concernée. Seuls les employés ayant un contrat valide dans leur fiche employé sont pris en compte dans le calcul. Le système utilise la valeur hebdomadaire définie à la section {% link_new Indications des temps de travail | features/administration/create-contracts.md | #indications-des-temps-de-travail %} du contrat de l'employé. Les absences n'impactent pas le résultat.
- la _couverture potentielle_ : c'est la différence entre le _capacitaire contractuel_ et le _besoin en personnel_.

> Veuillez noter que toutes les données du tableau sont affichées en heures.

{{ 1 | image: "Capacity table", '100%' }}
