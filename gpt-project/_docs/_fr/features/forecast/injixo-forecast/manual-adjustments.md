---
title: Ajustements manuels
redirect_from:
  - /fr/ajustements-manuels/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/events-and-holidays.md
---

Forecast vous permet d'ajuster le volume ou le TMT prévisionnel. Par exemple, pour répondre aux cas suivants :
- Vous savez que les données historiques sont incomplètes ou incorrectes et la prévision sera par conséquent erronée.
- Vous avez reçu un nombre important d'appels supplémentaires sur une période et vous souhaitez ne pas prendre en compte cette anomalie.
- Vous avez réorganisé votre service et l'historique ne correspond plus à la charge de travail à prévoir.

## Remplacer le volume

Dans les vues journalière, hebdomadaire et mensuelle, cliquez sur le bouton _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} pour accéder aux options _Ajuster le volume_{:.doc-button} et _Ajuster le TMT_{:.doc-button}. Sélectionner une des 2 options pour ajuster la valeur correspondante sur une plage de dates ou sur un intervalle horaire. La zone de modification des données apparaît sous le graphique.

Tout d'abord, sélectionnez la plage de dates ou l'intervalle horaire sur lequel vous souhaitez ajuster les valeurs. Vous pouvez modifier  uniquement les données de prévision mais pas les données historiques. Ensuite, choisissez si vous souhaitez effectuer un ajustement en pourcentage (`Modifier (%)`) ou en valeur absolue (`Écraser`) dans la liste déroulante.

L'option `Modifier (%)` permet d'**augmenter ou de diminuer le volume** en fonction d'une valeur positive ou négative.
L'option `Ecraser` permet de saisir une nouvelle valeur (positive) qui remplacera l'existante.

Enfin sélectionnez la raison pour laquelle vous avez effectué cet ajustement. Cette information nous aide à améliorer nos algorithmes.

Pour appliquer les modifications, cliquez sur _Sauvegarder_{:.doc-button}.

Pour modifier un ajustement manuel, suivez les mêmes étapes.

## Identifier un ajustement de volume

Le graphique de volume est mis à jour immédiatement après avoir enregistré une modification. L'aire hachurée sur le graphique correspond à la différence entre la prévision initiale et le volume final modifié manuellement. La couleur changera selon la nature de la modification (augmentation ou diminution).

{{ 1 | image: "Ajustement Manuel dans injixo Forecast" }}

> Remarque
>
> Attention, après modification, le volume que vous avez saisi ne sera plus mis à jour par Forecast. Ne saisissez que les valeurs que vous souhaitez définitivement utiliser comme référence.

Les valeurs modifiées sont visibles sur toutes les vues (journalière, hebdomadaire, mensuelle et annuelle) pour visualiser les dates auxquelles la prévision a été changée.
Dans la vue journalière, le volume modifié sera distribué selon la même répartition que la prévision initiale.

## Supprimer les ajustements

Si vous souhaitez supprimer ou modifier un ajustement, cliquez sur _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} et sélectionnez l'option _Ajuster le volume_{:.doc-button} ou _Ajuster le TMT_{:.doc-button}.

Pour supprimer un ajustement, sélectionnez la plage de dates ou l'intervalle horaire souhaité puis cliquez sur *Réinitialiser les modifications sélectionnées*{:.doc-button}. La modification sera immédiatement supprimée. En cliquant sur *Réinitialiser tous les ajustements*{:.doc-button}, vous supprimez toutes les modifications de la période affichée.

## Utiliser le volume ajusté

Une fois la modification effectuée, le besoin en personnel est automatiquement mis à jour.
Vous pouvez l'utiliser pour votre planification en cliquant sur _Utiliser le Besoin_{:.doc-button}.
Vous pouvez également transférer uniquement la prévision en cliquant sur _Utiliser Forecast_{:.doc-button}.
