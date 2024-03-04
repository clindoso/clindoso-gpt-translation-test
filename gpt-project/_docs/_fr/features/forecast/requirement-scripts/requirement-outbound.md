---
title: Appels sortants
description: Calculer le besoin en personnel pour les appels sortants.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

Pour déterminer le besoin en personnel pour les campagnes d’appels sortants, utilisez le script Besoin d’appel sortant.  Le calcul est basé sur le nombre total de contacts dans la campagne, la durée de la campagne et le temps moyen de traitement prévu pour chaque appel.

## Prérequis

Si vous ne souhaitez pas utiliser de valeur fixe pour vos appels sortants, exportez d’abord votre prévision&nbsp;:

1. Accédez à _Forecast_{:.menu-item}.
2. Sélectionnez un **Workload** depuis la liste déroulante en haut de la page.
3. Sélectionnez une **période**.
4. Dans la section **Volume et TMT**, cliquez sur _Transférer la prévision_{:.doc-button}. 
5. Dans la fenêtre **Transférer la prévision**, sélectionnez la version de votre prévision.
6. Cliquez sur _Transférer_{:.doc-button}.
7. Cliquez sur _Fermer_{:.doc-button}.

## Sélectionner le script

1. Accédez à _Forecast_{:.menu-item}.
2. Sur la droite, cliquez sur **Scripts de dimensionnement pour les multi-activités, les activités sans prévision et les appels sortants**.
3. Cliquez sur _Sélectionner un script_{:.doc-button}.
4. Sélectionnez **Calls - Outbound** depuis la liste déroulante.
   Une nouvelle fenêtre s’ouvre et affiche le Besoin d’appel sortant.

## Configurer le script
 
Dans la fenêtre du script, vous pouvez configurer les paramètres suivants&nbsp;:

| Paramètre                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File d'attente                        | Sélectionnez la file d’attente pour laquelle vous voulez utiliser le script.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Données                      | Objectif total de contacts de votre campagne.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Taux de contact (%)             | Pourcentage d’appels sortants répondus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Taux de recomposition (%)              | Plusieurs tentatives de recomposition sont effectuées et réparties sur la plage de dates sélectionnée. Exemple&nbsp;: vous souhaitez atteindre 5&nbsp;000 contacts pendant une campagne. Un taux de recomposition de 10&nbsp;% signifie que 500 contacts non aboutis seront recomposés (deuxième tentative). Puis, 50 recompositions seront effectuées (troisième tentative) et ainsi de suite. Ce processus continue jusqu’à ce que le nombre d’appels non aboutis soit inférieur à 1. Dans cet exemple de 5&nbsp;000 contacts, le nombre total de contacts est 5&nbsp;555. |
| Date de début                   | Début de la période du calcul.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Date de fin                     | Fin de la période du calcul.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Taux de mise en relation (RPC) avec le correspondant requis (%) | Le taux de mise en relation avec le correspondant requis (RPC) détermine le pourcentage d’appels qui permettent de joindre le contact cible. En effet, un automate ne fait pas la différence entre un appel répondu par la personne souhaitée, par la mauvaise personne (par exemple un conjoint) ou un répondeur. Sélectionnez fixe et entrez une valeur fixe dans le champ situé en-dessous, ou sélectionnez variable et sélectionnez un type de valeur avec les taux de mise en relation prévus.                                                                                                              |
| Contraction (%)                | (Facultatif) Indique les pertes du centre de contacts en termes de période de productivité en raison de pauses non prévues, de congés maladie, etc. Cette valeur compense le temps perdu afin que l’objectif de service reste atteignable.                                                                                                                                                                                                                                                                           |
| Temps de traitement  moyen      | Sélectionnez fixe ou variable                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RPC en secondes               | Temps moyen de traitement (en secondes), y compris le traitement post-appel pour un appel ayant permis de joindre la bonne personne.                                                                                                                                                                                                                                                                                                                                                                                                           |
| WPC en secondes               | Temps moyen de traitement (en secondes), y compris le traitement post-appel pour un appel avec la mauvaise personne à contacter.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Unité opérationnelle                | L’unité opérationnelle à laquelle appliquer le calcul. Si vous modifiez l’unité opérationnelle, le champ Activité sera mis à jour et affichera toutes les activités assignées à l’unité opérationnelle et pouvant être sélectionnées.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Activité                     | Activité pour laquelle vous souhaitez définir le besoin en personnel.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Ressources minimums                | Nombre minimum de personnes par intervalle. Saisissez une valeur pour remplacer les intervalles avec des valeurs inférieures.                                                                                                                                                                                                                                                                                                                                                                            |
| Ressources maximums                | Nombre maximum de personnes par intervalle. Saisissez une valeur pour remplacer les intervalles avec des valeurs supérieures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Exécuter le script

Une fois le script configuré, cliquez sur _OK_{:.doc-button} pour lancer le calcul. Une fenêtre affichera vos paramètres définis et le résultat de l’exécution du script. Vérifiez le besoin en personnel {% link_new sauvegardé dans le Centre de planification | features/scheduling/edit-or-delete-staff-requirements.md %}.

{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %} <!-- keep this or move to classic article? -->

{{ 1 | image: 'Interface Script d’appels sortants', '80%' }}
