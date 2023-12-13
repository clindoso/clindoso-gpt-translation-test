---
title: Appels - Taux d'abandon
toc: false
redirect_from:
  - /fr/besoin-appels-abandonnes/
redirect_reason: Updated filename on 21 April 2022
---

Le script "Scénario de besoin d'Erlang C des appels abandonnés" calcule le besoin en personnel en fonction du volume d'appels annulés et du temps jusqu'à ce que l'appelant raccroche (appels non décrochés). Il est très similaire au script standard Erlang C.

Le calcul est basé sur les utilisateurs qui raccrochent après un temps d'attente de _X_ secondes. Il tient également compte du fait que _Y_% des appels des clients doivent être traités avant que les clients ne raccrochent. Ainsi, _Y_% des appels doivent être traités dans un délai de _X_ secondes, comme calculé dans le script de calcul Erlang C standard.

Tout d'abord, vous sélectionnez la **File d'attente** dont les données doivent être utilisées pour le calcul. Dans **Opérations**, sélectionnez le type de valeur qui contient le volume d'appels, par exemple 'Appels Reçus'. Sélectionnez une catégorie de valeur pour la prévision du **Temps de traitement moyen** (TMT). Si vous n'avez pas de prévision sur le TMT, sélectionnez [Aucun], puis entrez le temps moyen de traitement présumé (en secondes) dans le champ **Temps de traitement moyen constant**.

Spécifiez la **Version** dont les valeurs doivent être utilisées. Notez que le module ForecastPro doit contenir une prévision pour la combinaison file d'attente/type de valeur/version sélectionnée.

Vous devez également sélectionner une **Unité opérationnelle** et une **Activité** pour lesquelles le besoin en personnel seront envoyés dans SchedulePro.

Dans **Taux d'abandon (%)** et **Temps avant l'abandon (s.)**, entrez le pourcentage d'appels abandonnés et le temps d'attente avant de raccrocher, par exemple, un  taux d'abandon acceptable serait 20% et vous pensez que les appelants restent en ligne 20 secondes avant de raccrocher.

> Déterminer le niveau de patience de l'appelant
>
> La plupart des systèmes téléphoniques (ACD) recueillent des informations sur les appels entrants, comme le temps moyen avant que l'appelant raccroche. Ces informations peuvent servir de base au calcul de vos besoins en fonction des appels abandonnés.

Vous avez la possibilité de spécifier le champ **(%) supplémentaire** pour augmenter le besoin en personnel, par exemple pour tenir compte du shrinkage.

Avec les paramètres **Ressources minimums** et **Ressources maximums** vous déterminez le nombre minimum et maximum d'employés à planifier.
Enfin, vous définissez l'intervalle de dates pour lequel le besoin en personnel sera généré à l'aide de **Date de début** et **Nombre de jours**.

> Note
>
> Dans la plupart des cas, la date de début et le nombre de jours doivent correspondre à une période de planification.

