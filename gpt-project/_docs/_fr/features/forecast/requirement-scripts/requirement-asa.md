---
title: Appels - Temps Moyen de Réponse
toc: false
redirect_from:
  - /fr/besoin-vmr/
redirect_reason: Updated filename on 21 April 2022
---

Le script "Scénario du besoin ASA" calcule le nombre d'employés nécessaires pour atteindre un objectif de service en fonction de la vitesse moyenne de réponse (VMR) spécifique.

La VMR est le temps d'attente moyen avant que l'appel ne soit répondu. Le script du besoin VMR est très similaire au script standard Erlang C dans la mesure où les deux premières sections de paramètres des deux scripts contiennent les mêmes champs.

Les paramètres d'entrée et la formule Erlang C sont utilisés pour calculer l'occupation d'un nombre donné d'agents et le temps d'attente prévu pour un appelant. Cette information est utilisée pour déterminer la vitesse moyenne de réponse. Le nombre d'employés requis est le plus petit nombre d'agents pour lequel la VMR est inférieure à la valeur cible spécifiée de la VMR.

Tout d'abord, vous sélectionnez la **File d'attente** dont les données doivent être utilisées pour le calcul. Dans **Opérations**, sélectionnez le type de valeur qui contient le volume d'appels, par exemple 'Appels Reçus'. Sélectionnez une valeur pour la prévision **Temps de traitement moyen** (TMT). Si vous n'avez pas prévu de TMT, sélectionnez [Aucun] ici, puis entrez le temps de traitement moyen présumé (en secondes) dans le champ **Temps de traitement moyen constant**.

Spécifiez la **Version** dont les valeurs doivent être utilisées, par exemple Prévision ou Auto-Forecast. Notez que le module ForecastPro doit contenir une prévision pour la combinaison file d'attente/type de valeur/version sélectionnée.

Ensuite, sélectionnez l'**Unité Opérationnelle** et l'**Activité** dans lesquelles le besoin en personnel sera sauvegardé.

Le paramètre supplémentaire **ASA (sec.)** indique le temps moyen en secondes pendant lequel un employé doit répondre aux appels.

Avec les paramètres **Ressources minimums** et **Ressources maximums** vous déterminez le nombre minimum et maximum d'employés à planifier.

Enfin, vous définissez l'intervalle de dates pour lequel le besoin en personnel sera généré à l'aide de **Date de début** et **Nombre de jours**.

Vous avez la possibilité de spécifier **% supplémentaire** pour augmenter le besoin en personnel, par exemple pour tenir compte du shrinkage.

> Remarque
>
> Dans la plupart des cas, la date de début et le nombre de jours doivent correspondre à une période de planification.
