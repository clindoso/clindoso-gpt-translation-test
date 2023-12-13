---
title: Besoin Constant
toc: false
redirect_from:
  - /fr/besoin-constant/
redirect_reason: Updated filename on 21 April 2022
---

Le script "Scénario du besoin iWFM constant" crée un besoin constant en personnel basée sur les spécifications renseignées par l'utilisateur. Ce script peut être utilisé s'il y existe un besoin fixe sans fluctuation ou s'il y a des activités qui nécessitent toujours le même besoin fixe. Par exemple, deux employés sont toujours nécessaires pour une procédure de niveau 2 pendant la journée. Les exigences constantes peuvent également être utilisées pour tester la planification, par exemple, s'il n'y a pas de valeurs historiques disponibles pour une équipe.

Les champs de saisie sont affichés pour chaque jour. Ces périodes définissent votre besoin en personnel pour couvrir la journée entière ou une plage spécifique. Vous pouvez spécifier une ou plusieurs périodes dans la journée qui peuvent avoir une durée maximale de 24 heures. La paramètre " 00:00 à 00:00 " est interprétée comme une journée entière.

Vous pouvez calculer un besoin en personnel constant pour plusieurs activités en simultané et sur plusieurs semaines en une passe, ou des activités individuelles sur des jours spécifiques. Ce calcul ne tient pas compte du nombre de contacts prévus ni du temps moyen de traitement. Ceci permet de créer un besoin en personnel pour des activités sans données d'historiques.

Vous pouvez sélectionner une **Date de début** et un **Nombre de jours** pour la période du calcul des besoins en personnel.

En fonction de la valeur du paramètre **Respecter les jours de la semaine**, l'affichage des jours dans la section _Données_ apparaît comme _jour 1_ à _jour n_ ou bien en _jours de la semaine_. Ce nombre de jour varie en fonction de la liste déroulante **Jours avec tranches horaires**.

Pour chaque activité, vous pouvez spécifier individuellement une **Unité opérationnelle** et une **Activité** pour lesquelles le besoin en personnel est renseigné dans SchedulePro.

Les valeurs des tranches horaires complètes ne sont écrites que si les cases à cocher le sont pour ce jour.

**Autres options :**

Si l'option **Additionner au besoin déjà existant** est cochée, le besoin en personnel défini dans le script sont ajoutés au besoin en personnel déjà enregistré dans le système WFM. Si cette option n'est pas cochée, le besoin en personnel écrasera les données.

Tout comme le besoin en personnel saisi peut se chevaucher partiellement avec un besoin en personnel déjà existant, les périodes de temps définies dans le script peuvent également se chevaucher. Vous déterminez comment celles-ci doit être traitées avec l'option **Additionner le besoin des tranches horaires chevauchantes**. Si cette option est cochée, les besoins sont additionnés, sinon ils sont écrasés.

Si vous cochez l'option **Prendre en compte les horaires d'ouverture de l'unité opérationnelle**, seul le besoin dans les heures d'ouverture de l'unité opérationnelle est pris en compte.

Dans le champ du paramètre **Jours avec tranches horaires**, vous définissez le nombre de jours pendant lesquels les champs de saisie des tranches horaires sont affichés. Le besoin en personnel pour les jours spécifiés sont répétés à partir de la "date de début" pendant le **Nombre de jours** défini.

Dans la champ du paramètre **Tranches horaires par jour**, vous spécifiez le nombre de tranches horaires par jour pour lesquelles vous souhaitez renseigner un besoin en personnel et dont les zones de saisie sont affichées dans la boîte de dialogue des _Données_.

Dans la zone **Nombre d'activités**, vous définissez le nombre d'activités pour lesquelles vous souhaitez calculer le besoin en personnel et pour lesquelles des zones de saisie sont affichées dans la boîte de dialogue des _Données_.

**Exemple:**

Si, par exemple, vous souhaitez planifier pour deux semaines un besoin en personnel le matin d'un jour et l'après-midi du jour suivant : saisissez 14 jours dans la zone **Nombre de jours** et seulement deux jours dans la zone **Jours avec tranches horaires**. Le besoin en personnel pour ces deux jours sera inscrit en alternance pendant 14 jours.

Si vous avez saisi la valeur 5 dans la zone **Jours avec tranches horaires**, le système affiche les tranches horaires pour les cinq premiers jours de la semaine de planification (lun, mar, mer, mer, jeu et ven). Aucun besoin d'employé n'est écrit pour les jours manquants (samedi et dimanche).
