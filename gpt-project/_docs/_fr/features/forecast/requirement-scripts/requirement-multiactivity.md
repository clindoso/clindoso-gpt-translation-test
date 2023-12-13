---
title: Appels - Multi-Activités
toc: false
redirect_from:
  - /fr/besoin-multi-activites/
redirect_reason: Updated filename on 21 April 2022
---

Le script "Scénario du besoin de Multiactivités" est utilisé pour la planification d'une multi-activité, si le besoin en personnel doit être couvert par des employés ayant des compétences multiples.

Il détermine les besoins en personnel pour chaque sous-activité d'une multi-activité afin d'atteindre un niveau de service souhaité.
Le calcul est effectué selon Erlang C sur la base d'un volume de transactions connu pour chaque sous-activité et du temps moyen de traitement, en tenant compte des temps d'attente prévus.

Dans le script, vous pouvez utiliser une prévision existante pour déterminer les besoins en salariés pour chaque **sous-activité** de la multi-activité.

> Remarque
>
> La période maximale d'exécution du script est de 365 jours, mais nous vous recommandons de choisir la période qui correspond à votre période de planification.
> 
> Le script ne peut être exécuté que s'il y a au moins une multi-activité dans le système.

First, you define the date range for which the staff requirements will be generated using **Start Date** and **Number of Days**.

Sélectionnez une **Unité opérationnelle** et une **Multi-activité** pour lesquelles les besoins du salarié sont saisis dans SchedulePro.

Différents paramètres de calcul peuvent être définis pour chaque sous-activité assignée.

Sélectionnez la **File d'attente** dont les données doivent être utilisées pour le calcul. Dans **Opérations**, sélectionnez le type de valeur qui contient le volume de contacts, par exemple 'Appels reçus'. Sélectionnez une catégorie de valeur pour la prévision **Temps de traitement moyen** (TMT). Si vous n'avez pas prévu de TMT, sélectionnez [Aucun] ici, puis entrez le temps de traitement moyen présumé (en secondes) dans le champ **Temps de traitement moyen constant**.

Spécifiez la **Version** dont les valeurs doivent être utilisées. Notez que le module ForecastPro doit contenir une prévision pour la combinaison file d'attente/type de valeur/version sélectionnée.

Dans **Niveau de service (%)** et **Service en Sec.**, vous enregistrez le pourcentage des processus et le temps de service dans lequel les appels doivent être traités, par ex. 80% des appels en 20 secondes.

Vous avez la possibilité de spécifier **% supplémentaire** pour augmenter les besoins en personnel, par exemple pour tenir compte de la réduction.

Avec les paramètres **Ressources minimums** et **Ressources maximums**, vous déterminez le nombre minimal et maximal d'employés à planifier pour chaque sous-activité.

Pour le files d'attente de type _Chat, pouvez-vous définir une valeur pour **Seq (%)** en pourcentage du temps passé par les employés sur un seul chat et **Sessions max.** en nombre maximum de sessions de chat parallèles.
