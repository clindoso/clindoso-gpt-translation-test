---
title: Script pour les multi-activités
description: Calculez le besoin en personnel pour les multi-activités.
toc: true
redirect_from:
  - /fr/besoin-multi-activites/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

Utilisez le script Multi-activités pour calculer le besoin en personnel pour vos multi-activités. Le calcul est basé sur la méthode Erlang-C et un niveau de service.

## Prérequis

- Créez au moins une {% link_new multi-activité | features/administration/activity-types-and-properties.md | #sous-activités %} et attribuez-la à votre unité opérationnelle.
- Créez un {% link_new workload | features/forecast/injixo-forecast/manage-workloads.md | #créer-un-workload %} pour chaque sous-activité de la multi-activité.

## Exporter la prévision pour tous les workloads des sous-activités

Avant de pouvoir exécuter le script Multi-activité, exportez les prévisions des workloads créés pour toutes les sous-activités&nbsp;:

1. Dans _Forecast > Workloads_{:.breadcrumbs}, sélectionnez le workload que vous avez créé pour une sous-activité.
2. Sélectionnez la période à l’aide du sélecteur de dates. Cliquez sur le numéro d’une semaine pour sélectionner toute la semaine, ou cliquez sur n’importe quel jour et faites glisser pour sélectionner une période supérieure ou inférieure à une semaine.
3. Depuis l’{% icon ellipsis_v %} en haut à droite, sélectionnez **Utiliser la prévision**.
4. Dans la fenêtre qui s'ouvre, sélectionnez la prévision que vous souhaitez utiliser.
5. Cliquez sur _Utiliser la prévision_{:.doc-button}.
6. Cliquez sur _Fermer_{:.doc-button}.
7. Répétez les étapes 1 à 6 pour tous les workloads créés pour vos sous-activités.

injixo enregistre les données requises pour le calcul du besoin en personnel dans les files d'attente de _WFM > Administration > Prévision > Files d'attente_{:.breadcrumbs}. Les files d'attente ont le nom du workload correspondant avec un astérisque en tête, par exemple *votreWorkload.

## Configurer le script

1. Accédez à _Forecast > Calcul du besoin_{:.breadcrumbs}.
2. Dans la section **Appels - Multi-activités**, cliquez sur _Ouvrir_{:.doc-button}.  
3. Dans la fenêtre de configuration du script, configurez les paramètres suivants&nbsp;:
   - Dans la section **Date**&nbsp;:
     - **Date de début**&nbsp;: saisissez la date de début pour le calcul du besoin en personnel.
     - **Nombre de jours**&nbsp;: saisissez le nombre de jours après la date de début pour lequel vous souhaitez calculer le besoin en personnel.
   - Dans la section **Paramètres unité opérationnelle**&nbsp;:
     - **Unité opérationnelle** et **Multi-activité**.<br>
     La fenêtre de configuration du script met à jour et affiche les paramètres de calcul pour les sous-activités concernées.
   - Dans la section **Sous-activité**, vous pouvez configurer différents paramètres de calcul pour chaque sous-activité. Commencez par les paramètres dans la section **Paramètres file d'attente**&nbsp;:
    - **Calculation method**&nbsp;: sélectionnez **Erlang-C**, **Linear** ou **Chat**.<br>La fenêtre de configuration du script met à jour et affiche les paramètres configurables concernés. Consultez le [tableau ci-dessous](#paramètres-de-calcul-dans-la-section-erlang-c) pour savoir quels paramètres sont configurables pour chaque méthode de calcul.
    - **File d’attente**&nbsp;: sélectionnez la file d'attente qui contient les données que vous souhaitez utiliser pour le calcul.
    - **Opérations**&nbsp;: sélectionnez le type de valeur du volume de contact, par exemple, Appels entrants.
    - **Temps de traitement moyen**&nbsp;: si vos workloads ont un temps moyen de traitement attendu (AHT), sélectionnez le type de valeur pertinent. Sinon, sélectionnez **[Aucun]**.
    - **Version**&nbsp;: sélectionnez **Auto-Forecast**. Dans injixo Enterprise on-premise, vous pouvez sélectionner une version différente.

## Paramètres de calcul dans la section Erlang C

| Paramètre                         | Description                                                                                                            | Configurable dans Erlang-C | Configurable dans Linear | Configurable dans Chat |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |--------  | -------- |
| Niveau de service (%)             | Pourcentage de contacts à traiter dans le délai configuré dans le paramètre **Service en sec**.                                                                                                                                                                    | Oui | Non | Oui |
| Service en sec.            | Temps dans lequel le pourcentage de contacts que vous configurez dans le paramètre **Niveau de service (%)** doit être traité.                                                                                                                                                                                            | Oui | Non | Oui |
| % supplémentaire                         | La valeur en pourcentage par laquelle vous souhaitez augmenter le besoin en personnel calculé. Découvrez comment [configurer ce paramètre](#configurer-le-paramètre--supplémentaire-pour-tenir-compte-du-shrinkage) pour tenir compte du shrinkage. | Oui | Oui | Oui |
| Ressources minimums            | Saisissez une valeur pour remplacer les valeurs de besoin en personnel inférieures.                                                                                                                                                                                                                                                     | Oui | Oui | Oui |
| Ressources maximums            | Saisissez une valeur pour remplacer les valeurs de besoin en personnel supérieures.                              | Oui | Oui | Oui |
| Temps de traitement moyen constant | Si vous avez sélectionné un type dans le paramètre **Temps de traitement moyen** dans la section **Paramètres file d'attente**, gardez la valeur par défaut ici.<br> Si vous avez sélectionné **[Aucun]** dans le paramètre **Temps de traitement moyen**, saisissez une valeur en secondes.                                 | Oui | Oui | Oui |
| Seq (%)                  | Pourcentage du TMT que les employés passent sur des tâches qu'ils ne peuvent pas faire en parallèle, comme le traitement post-appel.                                                                                                                                                                                                                                                                                   | Non | Non | Oui |
| Sessions max.                          | Nombre maximum de sessions de chat parallèles que les employés peuvent traiter à la fois.                                                                                                                                             | Non | Non | Oui |

### Configurer le paramètre % supplémentaire pour tenir compte du shrinkage.

Pour configurer le paramètre **% supplémentaire** pour tenir compte du shrinkage, utilisez la formule suivante, où s% est votre taux de shrinkage&nbsp;: 1/(1-s%)-1. Le résultat exprimé en pourcentage est la valeur à saisir dans le paramètre **% supplémentaire**. Par exemple, pour tenir compte d'un shrinkage de 20&nbsp;%, le calcul est 1/(1-0.2)-1, ce qui équivaut à 25&nbsp;%.

## Exécuter le script

- Pour lancer le calcul, cliquez sur _OK_{:.doc-button}.<br>Une fenêtre s'ouvre et affiche les paramètres d'entrée sélectionnés et les résultats du script. <br>

## Voir les résultats du calcul

Vous pouvez voir le besoin en personnel mis à jour pour l'unité opérationnelle sélectionnée et la multi-activité dans les {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %} ou dans la fenêtre des paramètres dans le {% link_new Centre de planification | features/scheduling/edit-or-delete-staff-requirements.md %} ou {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}.
