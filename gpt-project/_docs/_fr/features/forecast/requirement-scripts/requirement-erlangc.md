---
title: Appels - Mono activité
toc: false
redirect_from:
  - /fr/besoin-erlangC/
redirect_reason: Updated filename on 21 April 2022
---

Le script du besoin en personnel "Scénario du besoin iWFM Erlang C" utilise la méthode Erlang C pour déterminer le besoin en personnel requis pour atteindre un niveau de service donné. Le calcul est basé sur les volumes d'appels prévus et les temps de traitement moyens.

Tout d'abord, vous sélectionnez la **File d'attente** dont les données doivent être utilisées pour le calcul. Dans **Opérations**, sélectionnez le type de valeur qui contient le volume d'appels, par exemple 'Appels Reçus'. Sélectionnez une valeur pour la prévision **Temps de traitement moyen** (TMT). Si vous n'avez pas prévu de TMT, sélectionnez [Aucun] ici, puis entrez le temps de traitement moyen présumé (en secondes) dans le champ **Temps de traitement moyen constant**.

Spécifiez la **Version** dont les valeurs doivent être utilisées, par exemple Prévision ou Auto-Forecast. Notez que le module ForecastPro doit contenir une prévision pour la combinaison file d'attente/type de valeur/version sélectionnée.

Ensuite, sélectionnez l'**Unité Opérationnelle** et l'**Activité** dans lesquelles le besoin en personnel sera sauvegardé.

Dans **Niveau de service %** et **Service en Sec.**, vous spécifiez l'objectif de service, par exemple 80% des appels doivent être traités en 20 secondes.

Vous avez la possibilité de spécifier **% supplémentaire** pour augmenter le besoin en personnel, par exemple pour tenir compte du shrinkage.

Avec les paramètres **Ressources minimums** et **Ressources maximums** vous déterminez le nombre minimum et maximum d'employés à planifier.

Enfin, vous définissez l'intervalle de dates pour lequel le besoin en personnel sera généré à l'aide de **Date de début** et **Nombre de jours**.

> Remarque
>
> Dans la plupart des cas, la date de début et le nombre de jours doivent correspondre à une période de planification.
