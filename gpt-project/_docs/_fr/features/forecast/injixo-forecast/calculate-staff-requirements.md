---
title: Calculer le besoin en personnel
redirect_from:
  - /fr/staff-requirement/
redirect_reason: Updated filename on 04 March 2024
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Calculez le besoin en personnel pour les appels, le chat, les e-mails et plus.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-outbound.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
---

Après avoir généré une prévision, vous pouvez calculer le besoin en personnel. Vous pouvez choisir parmi plusieurs scripts de calcul du besoin en personnel et méthodes de calcul disponibles dans injixo. Vous pouvez également créer un besoin en personnel constant sans prévision, si nécessaire.

Vous débutez avec injixo Forecast&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Méthodes de calcul et scripts de calcul du besoin en personnel

injixo propose des méthodes de calcul et scripts de calcul du besoin en personnel.
Découvrez quel {% link_new script ou méthode de calcul est approprié | best-practices/requirement-scripts.md %} pour votre scénario d’utilisation.<br>
Apprenez à [configurer ces méthodes de calcul](#configurer-les-méthodes-de-calcul) dans la section suivante.<br>
Pour apprendre à configurer les scripts de calcul du besoin en personnel, cliquez sur les liens suivants&nbsp;:

- {% link_new Script multi-activités | features/forecast/requirement-scripts/requirement-multiactivity.md %}
- {% link_new Script pour les appels sortants | features/forecast/requirement-scripts/requirement-outbound.md %}
- {% link_new Script de besoin constant | features/forecast/requirement-scripts/requirement-constant.md %}

## Configurer les méthodes de calcul

Les méthodes de calcul permettent de calculer le besoin en personnel selon les nouveaux imports de données, la modification des paramètres de calcul ou les {% link_new ajustements manuels | features/forecast/injixo-forecast/manual-adjustments.md %}.
Vous pouvez modifier votre méthode de calcul à tout moment.

1. Dans _Forecast > Workloads_{:.breadcrumbs}, sélectionnez un workload.
2. Dans la section **Besoin en personnel**, cliquez sur _Modifier le besoin en personnel_{:.doc-button}.
3. Depuis le menu déroulant **Méthode de calcul**, sélectionnez une option&nbsp;:
   - **Erlang-C**
   - **Chat**
   - **Linear**
4. Dans la section **Paramètres de calcul**, configurez les [paramètres de calcul](#paramètres-de-calcul).
5. Dans la section **Unité opérationnelle et activité associées**, sélectionnez l’unité opérationnelle et l’activité pour laquelle vous souhaitez utiliser le besoin en personnel.  
   En savoir plus sur l’[utilisation du besoin en personnel pour la planification](#utiliser-le-besoin-en-personnel-pour-la-planification).
6. Cliquez sur _Sauvegarder_{:.doc-button}.

Le graphique dans la section **Besoin en personnel** affiche le besoin en personnel calculé.<br> Sous le graphique, vous verrez les valeurs configurées pour les paramètres et le total d’heures-personnes requises pour la période sélectionnée.  <br> Faites passer votre curseur sur le graphique pour afficher des informations détaillées sur le volume, le TMT, le besoin en personnel, les ajustements manuels et les événements ajoutés par intervalle.

### Paramètres de calcul

Le tableau suivant inclut les paramètres que vous pouvez configurer pour chaque méthode de calcul&nbsp;:

| Paramètre                         | Description                                                                                                                                                                                                                                                                                                           | Configurable dans Erlang-C | Configurable dans Chat | Configurable dans Linear |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |--------  | -------- |
| Objectif de qualité de service              | Pourcentage d’appels ou de chats entrants à traiter dans le temps de réponse cible.                                                                                                                                                                                                                                                                          | Oui | Oui | Non |
| Objectif de temps de réponse                | Temps pendant lequel le pourcentage d’appels ou de chats spécifiés dans le paramètre de qualité de service cible doit être traité.                                                                                                                                                                                            | Oui | Oui | Non |
| Shrinkage                         | Le pourcentage de temps rémunéré pendant lequel les employés ne peuvent pas travailler, par exemple en raison de pauses, de retards, de congés maladie imprévus ou de problèmes techniques. | Oui | Oui | Oui |
| Besoin minimum            | Saisissez une valeur pour remplacer les intervalles avec des valeurs de besoin en personnel inférieures.                                                                                                                                                                                                                                                     | Oui | Oui | Oui |
| Besoin maximum            | Saisissez une valeur pour remplacer les intervalles avec des valeurs de besoin en personnel.                              | Oui | Oui | Oui |
| Temps moyen de traitement (TMT) fixe | Saisissez une valeur pour remplacer la prévision de TMT.<br>Cochez la case **Appliquer le TMT fixe uniquement si aucune valeur de TMT n’est disponible** pour utiliser la valeur de TMT fixe uniquement pour les périodes sans données de TMT. Par défaut, le calcul du besoin en personnel utilise les valeurs de TMT de la prévision.                                  | Oui | Oui | Oui |
| Nombre de sessions maximum                  | Nombre maximum de sessions de chat parallèles que les employés peuvent traiter à la fois.                                                                                                                                                                                                                                                                                   | Non | Oui | Non |
| Overhead                          | Pourcentage du TMT qu’un employé doit consacrer à des tâches qu’il ne peut effectuer en parallèle, par exemple l’ajout de notes post-appel dans le système CRM. Ce paramètre ne sera pas pris en compte si vous saisissez la valeur 1 dans le champ **Nombre de sessions maximum**.                                                                                                                                             | Non | Oui | Non |

## Utiliser le besoin en personnel pour la planification

Pour créer un planning basé sur le besoin en personnel, vous devez d’abord sauvegarder le besoin. Pour sauvegarder le besoin en personnel, suivez les étapes ci-dessous.

Vous ne pouvez utiliser le besoin en personnel calculés que pour les versions de la prévision ou les prévisions importées que vous avez sauvegardées pour la période sélectionnée. <br>
En savoir plus sur les {% link_new versions de la prévision | features/forecast/injixo-forecast/store-forecast-versions.md %} ou {% link_new l’import de prévisions | features/forecast/injixo-forecast/import-forecast.md %}.

1. Dans _Forecast > Workloads_{:.breadcrumbs}, sélectionnez un workload.
2. Sélectionnez la période pour laquelle vous souhaitez utiliser le besoin en personnel.
3. Dans la section **Besoin en personnel**, sélectionnez une version de la prévision depuis le menu déroulant à gauche.
4. Cliquez sur _Sauvegarder le besoin_{:.doc-button}.
5. Dans la fenêtre **Sauvegarder le besoin en personnel**, cliquez sur _Sauvegarder_{:.doc-button}.

injixo enregistre le besoin en personnel pour l’unité opérationnelle et l’activité que vous avez sélectionnée pendant la configuration de la méthode de calcul.

> Remarque
>
> Vous pouvez utiliser le besoin en personnel pour une unité opérationnelle ou une activité différente. <br> Pour ce faire, répétez la procédure pour [configurer la méthode de calcul](#configurer-les-méthodes-de-calcul) et sélectionnez une unité opérationnelle ou une activité différente. Puis, suivez la procédure pour utiliser le besoin en [personnel pour la planification](#utiliser-le-besoin-en-personnel-pour-la-planification).
