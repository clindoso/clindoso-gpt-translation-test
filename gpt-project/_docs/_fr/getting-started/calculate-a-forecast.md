---
title: Calculer une prévision
description: Suivez les étapes principales pour calculer une prévision
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
redirect_from:
  - /fr/quickstart-forecasting/
redirect_reason: Updated filename on 29 November 2023
---

Cet article décrit les étapes nécessaires à la création de votre première {% link_new prévision | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}. Forecast calcule le nombre d’employés requis pour prendre en charge les volumes de contacts entrants pour une activité dans une unité opérationnelle, sur la base des données historiques.
Cet article donne un aperçu de la procédure à suivre pour créer une prévision. Pour en savoir plus sur chaque étape, suivez les liens dans cet article.

Utilisez cet article pour vérifier que toutes les étapes ont bien été suivies lors de l’onboarding. N’hésitez pas à contacter votre consultant si vous avez des questions.

## Prérequis

Avant de créer un planning, assurez-vous que votre {% link_new configuration minimale est correcte | getting-started/set-up-base-configuration.md %}.
## 1\. Configurer une intégration

Dans _Account > Intégrations_{:.breadcrumbs}, configurez une intégration avec votre système externe pour importer les données historiques. L’intégration importera les données vers injixo et créera des files d’attente.

## 2\. Configurer un workload

Dans _Forecast_{:.breadcrumbs}, créez {% link_new un workload à partir des files d’attente créées par votre intégration | features/forecast/injixo-forecast/manage-workloads.md %}. Une prévision sera générée en quelques minutes.

Remarque&nbsp;: pour {% link_new importer des prévisions externes | features/forecast/injixo-forecast/import-forecast.md %}, vous devez sélectionner au moins une file d'attente. S’il n’existe aucune file d’attente, vous devez importer au moins un point de données à l’aide d’une {% link_new intégration par fichier CSV | features/acd-integration/cloud/add-csv-integration.md %}.

## 3\. Créer et ajouter des événements

Créez tous les {% link_new événements | features/forecast/injixo-forecast/events-and-holidays.md %} pouvant impacter le calcul de votre prévision. Ajoutez les événements créés à l’historique et la prévision à vos workloads pour affiner le calcul.

## 4\. Enregistrer une version de la prévision

Une {% link_new version de prévision | features/forecast/injixo-forecast/store-forecast-versions.md %} est un instantané du calcul actuel. Enregistrez la version de la prévision pour la modifier ultérieurement ou pour comparer votre prévision avec le volume de la journée en cours, par exemple dans {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %}.

## 5\. Calculer le besoin en personnel

Pour optimiser le planning ou les activités, vous devez d’abord {% link_new calculer les besoins en personnel | features/forecast/injixo-forecast/calculate-staff-requirements.md %} pour les activités correspondantes dans vos workloads.


## Et ensuite&nbsp;?

Vous avez réussi&nbsp;! Vous pouvez maintenant {% link_new créer votre premier planning | getting-started/create-a-schedule.md %} en fonction de votre prévision et du besoin en personnel.
