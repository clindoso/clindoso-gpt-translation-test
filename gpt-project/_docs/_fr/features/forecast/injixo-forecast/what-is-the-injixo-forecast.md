---
title: Explorer injixo Forcast
redirect_from:
  - /fr/forecast_overview/
  - /fr/general-functionality/
redirect_reason: redirect for intercom forecast tour, 2nd link, renamed article in june 2021
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Utilisez injixo Forecast pour calculer automatiquement une prévision du volume de contacts et du temps moyen de traitement (TMT).
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manual-adjustments.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/store-forecast-versions.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/download-forecast.md
---

injixo Forecast combine vos données historiques à l’algorithme le mieux adapté pour générer des prévisions de haute qualité. L’algorithme reconnaît les tendances, les schémas et les fluctuations que contiennent vos données. injixo Forecast utilise de nombreux types d’algorithmes, comme ARIMA, la méthode de Holt-Winters, le lissage exponentiel, la régression ou l’amplification de gradient. 

injixo Forecast sélectionne automatiquement l'algorithme le mieux adapté à vos données. injixo génère une prévision pour 365 jours à venir après l'importation des données.

injixo Essential WFM utilise un algorithme simple qui utilise des valeurs moyennes simples dans les données historiques pour reconnaître une tendance linéaire à long terme et des tendances hebdomadaires.

## Calculer une prévision

Consultez notre guide de démarrage rapide pour apprendre à {% link_new générer une prévision | getting-started/calculate-a-forecast.md %}. Chaque nouvel import de données met à jour la prévision générée. injixo Essential WFM génère uniquement une nouvelle prévision une fois par semaine.

Remarque&nbsp;: même si la prévision générée affiche uniquement des tendances récurrentes hebdomadaires, elle peut être la prévision optimale. Dans ce cas, l’algorithme capture des tendances à court terme (pour les fluctuation non récurrentes) et considère les tendances à long terme comme non pertinentes. Les fluctuations des données historiques ne sont pas toujours des tendances.

## Données nécessaires

Pour utiliser injixo Forecast, vous devez importer les contacts entrants, le temps moyen de traitement (TMT) et les contacts traités.

Dans injixo Classic, les workloads Basic nécessitent au moins deux semaines de données historiques. Les workloads Smart peuvent générer une prévision basée sur un seul jour de données historiques. Si vous disposez d’un ou deux ans de données, les workloads Smart prennent en compte les fluctuations mensuelles et annuelles, comme les activités saisonnières.

Le type de workload disponible dépend de votre offre WFM (Classic, Essential, Advanced ou Enterprise WFM).

## Gérer les données de faible qualité

Pour générer une prévision, les données historiques doivent être complètes (suffisamment de données, avec le moins d’écart possible) et précises (sans tendances non pertinentes). Par exemple, les {% link_new événements ou jours fériés | features/forecast/injixo-forecast/events-and-holidays.md %} indiqués de manière incorrecte influenceront la qualité de la prévision.

Les données historiques peuvent inclure des périodes d’inactivité prolongées, ou manquer de données pour une période particulière. Plus les données manquantes sont proches de la date actuelle, moins la qualité de la prévision est influencée. 

Voici quelques conseils pour gérer des données de faible qualité selon la durée de la période avec des données de faible qualité ou manquantes&nbsp;:

| Période avec données de mauvaise qualité     | Conseil                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Quelques jours | Utilisez les {% link_new événements | features/forecast/injixo-forecast/events-and-holidays.md %} pour marquer les jours affectés comme pannes et les exclure du calcul.                                  |
| Quelques semaines    | Ajoutez des données supplémentaires sans écarts ou tendances non pertinentes. |
| Plusieurs semaines ou mois  | Supprimez les données précédant l’absence de données. Importez uniquement les données ultérieures à l’absence de données.                            |

Remarque&nbsp;: si vous ne pouvez pas ajouter de données supplémentaires ou si vous n’avez pas assez de données après un écart, les algorithmes du Forecast Smart tenteront automatiquement de minimiser l’impact négatif des données manquantes.

> Vérifiez et nettoyez vos données avant de les importer
>
> Vous ne pouvez pas supprimer les données historiques. Contactez votre équipe customer success si nécessaire.

## Prévision des faibles volumes

injixo Forecast peut générer des prévisions pour les volumes de contact faibles et élevés. Lors de la génération d’une prévision basée sur des volumes de contact faibles, injixo peut ne pas reconnaître les tendances journalières. Dans de rares cas, il est possible qu’aucune prévision ne soit générée pour certains jours. Pour les journées individuelles, ajustez la prévision manuellement. En cas de situation récurrente, vous pouvez&nbsp;:

- ajouter plusieurs files d’attente au workload (ceci entraînera des volumes plus élevés),
- utiliser une autre approche pour générer un besoin en personnel pour la planification, par exemple {% link_new générer un besoin en personnel constant | features/forecast/requirement-scripts/requirement-constant.md %}.
