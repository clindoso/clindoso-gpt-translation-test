---
title: Besoin Productivité
toc: false
redirect_from:
  - /fr/besoin-lineaire/
redirect_reason: Updated filename on 21 April 2022
---

Le script "Scénario du besoin linéaire" détermine le besoin en personnel sur la base d'un calcul linéaire. Le besoin est calculé à l'aide des opérations sur chaque intervalle et du temps de traitement moyen.

La relation entre la durée d'intervalle de la _file d'attente_ et l'_unité opérationnelle_ est prise en compte dans le calcul : si le temps de traitement est supérieur à la durée de l'intervalle, les processus sont ajoutés à l'intervalle suivant. Le résultat du calcul est sauvegardé dans le menu besoin en personnel de _SchedulePro_.

Sélectionnez d'abord la **File d'attente** dont les données doivent être utilisées pour le calcul. Dans **Opérations**, sélectionnez le type de valeur qui contient le volume d'appels, par exemple 'Appels reçus'. Sélectionnez une valeur pour la prévision **Temps de traitement moyen** (TMT). Si vous n'avez pas prévu de TMT, sélectionnez [Aucun] ici, puis entrez le temps de traitement moyen présumé (en secondes) dans le champ **Temps de traitement moyen constant**.

Spécifiez la **Version** dont les valeurs doivent être utilisées, par exemple Prévision ou Auto-Forecast. Notez que le module ForecastPro doit contenir une prévision pour la combinaison file d'attente/type de valeur/version sélectionnée.

Ensuite, sélectionnez l'**Unité Opérationnelle** et l'**Activité** dans lesquelles le besoin en personnel sera sauvegardé. 

Vous avez la possibilité de spécifier **% supplémentaire** pour augmenter le besoin en personnel, par exemple pour tenir compte du shrinkage. 

Avec les paramètres **Ressources minimums** et **Ressources maximums** vous déterminez le nombre minimum et maximum d'employés à planifier.

Enfin, vous définissez l'intervalle de dates pour lequel le besoin en personnel sera généré à l'aide de **Date de début** et **Nombre de jours**.

> Remarque
>
> Dans la plupart des cas, la date de début et le nombre de jours doivent correspondre à une période de planification.
