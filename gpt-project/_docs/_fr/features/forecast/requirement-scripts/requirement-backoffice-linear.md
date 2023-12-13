---
title: Back office - Productivité
toc: false
redirect_from:
  - /fr/besoin-backoffice/
redirect_reason: Updated filename on 21 April 2022
---

Le script "Scénario du besoin linéaire au bureau administratif" calcule le besoin en personnel pour le traitement des activités non liées aux appels dans le backoffice, telles que les lettres, e-mails et fax.

> Remarque
>
> Il existe une distinction importante entre le traitement des appels et le traitement des documents. Les appels doivent être traités en temps réel, tandis que les documents peuvent être traités en dehors des heures de pointe.

Ce besoin en personnel est basée sur un calcul linéaire. Tous les documents entrants (un volume de transactions connu) qui sont rassemblés dans une file d'attente sont pris en compte. Pour la période de calcul, le total de tous les documents est réparti sur la journée, de nouveaux documents sont ajoutés dans chaque intervalle, qui sont ensuite répartis à nouveau avec le temps de traitement spécifié, de sorte que la courbe augmente au cours de la journée jusqu'à ce que plus aucun nouveau document ne soit ajouté.

Tout d'abord, vous sélectionnez la **File d'attente** dont les données doivent être utilisées pour le calcul. Dans **Opérations**, sélectionnez le type de valeur qui contient le volume de documents, par exemple 'Documents reçus'. Sélectionnez une valeur pour le **Temps de traitement moyen** (TMT). Si vous n'avez pas prévu de TMT, sélectionnez [Aucun] ici, puis entrez le temps de traitement moyen présumé (en secondes) dans le champ **Temps de traitement moyen constant**.

Spécifiez la **Version** dont les valeurs doivent être utilisées. Notez que le module ForecastPro doit contenir une prévision pour la combinaison file d'attente/type de valeur/version sélectionnée.

Vous devez également sélectionner une **Unité opérationnelle** et une **Activité** pour lesquelles les besoins du salarié sont saisis dans SchedulePro.

Vous avez la possibilité de spécifier **Addition (%)** pour augmenter les besoins en personnel, par exemple pour tenir compte du shrinkage.

Avec les paramètres **Ressources maximums** et **Ressources Minimums** vous déterminez le nombre minimum et maximum d'employés à planifier.

Les autres paramètres du script backoffice sont **Additionner au besoin existant**, qui ajoute le résultat calculé pour le besoin calculé précédemment enregistré pour le besoin en personnel.

> Remarque
>
> Si cette case à cocher est désactivée, le besoin en personnel sauvegardé précédemment est écrasé par le calcul en cours.

Si vous sélectionnez l'option **Tâches à traiter en moins de X heures**, vous devez saisir le nombre total d'heures requises pour cette activité.

* Exemple : 100 documents doivent être traités dans les 8 heures. Bien entendu, vous définissez un niveau de service pour cette durée.

Vous pouvez également sélectionner **Tâches à traiter avant x y**. Vous pouvez paramétrer le niveau de service sur une durée maximale de sorte que, par exemple, le nombre de documents reçus par _X_ heures dans la file d'attente doit être traité avant _Y_ heures.

* Exemple : 230 documents sont arrivés dans la file d'attente pendant la nuit et avant 8 h... Ceux-ci doivent être traités avant la fermeture des bureaux, c'est-à-dire avant 17h00 ce jour-là, afin que les niveaux de service soient respectés.

La case à cocher **A répartir entre les heures d'ouverture uniquement** permet de répartir le résultat du calcul soit dans les heures d'ouverture de la file d'attente, soit sur une période de 24 heures.

Enfin, vous définissez l'intervalle de dates pour lequel le besoin en personnel sera généré à l'aide de **Date de début** et **Nombre de jours**.

> Remarque
>
> Dans la plupart des cas, la date de début et le nombre de jours doivent correspondre à une période de planification.
