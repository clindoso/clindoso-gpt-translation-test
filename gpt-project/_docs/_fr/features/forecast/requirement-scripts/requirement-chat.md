---
title: Chat - Webchat
toc: false
redirect_from:
  - /fr/besoin-chat/
redirect_reason: Updated filename on 21 April 2022
---

Le script du calcul du besoin "Scénario de besoin Discussion" calcule le nombre d'employés nécessaires pour gérer l'ensemble des sessions de chat (par exemple sur les réseaux sociaux) tout en maintenant un certain niveau de service. Les canaux de communication tels que les chats, Facebook et Twitter ont connu une forte croissance ces dernières années. Si le chat est utilisé efficacement via les médias sociaux, il est plus rapide et moins cher que le service client par téléphone ou par e-mail.

Le script du calcul du besoin "Chat - WebChat" est basé sur le script standard Erlang C. Le calcul est effectué sur la base d'un volume d'interactions connu et de leur durée moyenne. Le temps d'attente prévu pour les sessions de chat est pris en compte.

Tout d'abord, vous sélectionnez la **File d'attente** dont les données doivent être utilisées pour le calcul. Dans **Opérations**, sélectionnez le type de valeur qui contient le volume des chats, par exemple 'Chats reçus'. Sélectionnez une valeur pour le **Temps de traitement moyen** (TMT) prévu. Si vous n'avez pas prévu de TMT, sélectionnez [Aucun] ici, puis entrez le temps de traitement moyen présumé (en secondes) dans le champ **Temps de traitement moyen constant**.

Spécifiez la **Version** dont les valeurs doivent être utilisées. Notez que le module ForecastPro doit contenir une prévision pour la combinaison file d'attente/type de valeur/version sélectionnée.

Vous devez également sélectionner une **Unité opérationnelle** et une **Activité** pour lesquelles les besoins du salarié sont saisis dans SchedulePro.

Dans **Niveau de service (%)** et **Service en Sec.**, vous définissez le pourcentage de chats à répondre dans un laps de temps donné, par exemple 80% des chats en 20 secondes.

Vous avez la possibilité de spécifier **% supplémentaire** pour augmenter les besoins en personnel, par exemple pour tenir compte de la réduction. 

Avec les paramètres **Ressources minimums** et **Ressources maximums** vous déterminez le nombre minimum et maximum d'employés à planifier.

Le champ **Seq (%)** vous permet de définir une valeur pour le pourcentage de temps pendant lequel les employés doivent se concentrer sur une seule conversation (par exemple, lors de la saisie de notes dans votre CRM). Dans **Sessions Max**, vous définissez le nombre maximum de sessions de chat simultanées par employé.

Enfin, vous définissez l'intervalle de dates pour lequel le besoin en personnel sera généré à l'aide de **Date de début** et **Nombre de jours**.

> Remarques
>
> Dans la plupart des cas, la date de début et le nombre de jours doivent correspondre à une période de planification.
