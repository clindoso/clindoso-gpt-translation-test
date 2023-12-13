---
title: Files d'attentes
redirect_from:
  - /fr/files-attente/
redirect_reason: Updated filename on 21 April 2022
---

## Définition

Une file d'attente est une représentation de vos canaux dans lequel des données de flux peuvent être importées.

Pour créer une file d'attente, cliquer sur le "+" en haut à gauche de la page

<div markdown="1" class="hint-box-default hint-box-red">

Xlink est obsolète

Si vous utilisez actuellement Xlink pour votre abonnement injixo Cloud WFM, veuillez passer immédiatement à injixo Cloud Link ou à une solution qui respecte les normes d’intégration les plus récentes. N’hésitez pas à solliciter l’aide de nos experts [ici](https://www.injixo.com/fr/contact/).

</div>

## Rubrique Généralités

Les champs à remplir lors de la création d'une file d'attente sont les suivants :

- Nom : saisissez le nom que vous souhaitez donner à la file d'attente (50 caractères max.)
- Abréviation : saisissez l'abréviation que vous souhaitez donner à la file d'attente et qui sera utilisée dans les autres modules (25 caractères max.)
- Active : activez cette case à cocher si vous souhaitez que le programme prenne en compte cette file d'attente au cours de l'importation de données à partir de l'Application Xlink
- Intervalle de temps : sélectionnez l'intervalle selon lequel les valeurs journalières de la prévision ainsi que le besoin en personnel prévisionnel seront répartis. Vous avez le choix entre 15, 30 et 60 minutes
- Description : saisissez dans ce champ une description pour la file d'attente, qui sera affichée dans d'autres modules
- File d'attente supérieure : sélectionnez une file d'attente dans ce champ si vous souhaitez créer une hiérarchie ou si vous souhaitez, par exemple, regrouper dans la file d'attente supérieure les types de valeurs similaires de plusieurs files d'attente en tant que types de valeurs virtuels
- Fuseau horaire : un fuseau horaire peut être attribué une fois lors de la création de la file d'attente

{{ 1 | image: "file_creation", '75%' }}

## Rubrique Types d'événements

Vous pouvez attribuer ici des types d'événements et des horaires d'ouverture à la file d'attente. Ce n'est qu'une fois attribué que le type d'événement peut être inséré dans le calendrier de prévision, qu'il peut être pris en compte lors de la prévision dans le module ForecastPro et qu'un besoin en personnel peut être déterminé.

En saisissant des horaires d'ouverture pour le type d'événement, vous déterminez une plage pour la prise en compte des données importées pour la courbe journalière type, pour le volume hebdomadaire du type de valeur, pour le besoin prévisionnel et enfin pour le besoin en personnel.

Les attributions des types d'événements et de leurs horaires d'ouverture dans la rubrique "Types d'événements" seront pris en compte de la manière suivante :

- lors de la création de la courbe journalière type : seules les données de la courbe journalière situées à l'intérieur des horaires d'ouverture seront sélectionnées,
- lors de la détermination du volume de base pour la prévision : les volumes hebdomadaires à l'origine du volume de base ont été déterminés uniquement pour la période comprise dans les horaires d'ouverture,
- lors de la prévision : la prévision sera uniquement exécutée pour la période comprise dans les horaires d'ouverture,
- lors du dimensionnement. Dans ce cas, les horaires d'ouverture de la file d'attente ainsi que les horaires d'ouverture de l'unité opérationnelle seront pris en compte

> Remarque
>
> La prise en compte des horaires d'ouverture n'a pas lieu lors d'une importation de données via Xlink : toutes les données seront importées indépendamment de l'attribution du type d'événement et des horaires d'ouverture.

Pour attribuer à une file d'attente des types d'événements avec des horaires d'ouverture, cliquez, dans la rubrique Types d'événements, sur le "+". La boite de dialogue d'édition s'ouvre.

{{ 2 | image: "file_evenement2", '75%' }}

- Types d'événements : sélectionnez le ou les types d'événements que vous souhaitez attribuer à la file d'attente
- Heure de début : indiquez l'heure à partir de laquelle les types d'événements seront pris en compte dans injixo
- Heure de fin : indiquez l'heure jusqu'à laquelle les types de valeurs du type d'événement seront pris en compte dans injixo

{{ 3 | image: "file_evenement1", '75%' }}

En enregistrant la saisie, tous les types d'événement attribués ainsi que leurs horaires d'ouverture seront affichés dans la rubrique.

## Rubrique Types de valeurs

Dans cette rubrique, vous pouvez attribuer à votre file d'attente les types de valeurs que vous souhaitez utiliser pour la prévision de la charge de travail, ou que vous souhaitez tout simplement suivre dans le menu OnlineCockpit.

Pour attribuer à une file d'attente des types de valeurs, cliquez sur le "+" de cette section. La boite de dialogue s'ouvre :

- Types de valeurs : sélectionnez le ou les types de valeurs que vous souhaitez attribuer à la file d'attente

{{ 4 | image: "file_type_valeur", '75%' }}

Après avoir enregistré vos saisies, tous les types de valeurs seront affichés dans la rubrique.
