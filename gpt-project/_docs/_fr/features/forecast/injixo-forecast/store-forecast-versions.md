---
title: Versions
redirect_from:
  - /fr/forecast-versions/
  - /fr/versions/
redirect_reason: Updated filename on 29 March 2023
---

Forecast vous permet de sauvegarder la prévision à un instant T, lorsque par exemple vous exportez le besoin pour la réalisation des plannings. Ces sauvegardes sont nommées Versions.


## Introduction aux Versions

Plusieurs Versions sont disponibles dans Forecast : *Forecast*, *Opérationnel* et *Stratégique*.

La Version *Forecast* est continuellement mise à jour et affiche la prévision la plus récente calculée pour chaque Workload.

Les 2 autres Versions, *Opérationnel* et *Stratégique*, ont été créées pour vous permettre de sauvegarder la prévision *Forecast* à un instant T pour la période de votre choix. Les données de ces Versions ne seront ni écrasées ni modifiées par le système dans le futur.

Il y a de multiples façons d'utiliser les Versions, par exemple, sauvegarder la prévision annuelle dans la Version *Stratégique* et la prévision utilisée pour le dimensionnement dans la Version *Opérationnel*. Cela vous permet ensuite de comparer ces sauvegardes avec la prévision actualisée de la Version *Forecast*.

## Sauvegarder la prévision dans les Versions

Pour sauvegarder la prévision dans une Version vous devez :

1. Sélectionnez le Workload concerné
2. Affichez la période de votre choix (jour, semaine, mois ou année)
3. Cliquez sur _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} puis sur _Sauvegarder la prévision dans une Version_{:.doc-button}
4. Sélectionnez la Version de destination, *Stratégique* ou *Opérationnel*
5. Confirmez votre choix en cliquant sur _Sauvegarder_{:.doc-button}

> Remarque
>
> Si une prévision a déjà été sauvegardée dans la même Version et sur la même période, les données de cette Version seront écrasées.

## Afficher les Versions

Pour afficher les données sauvegardées dans les Versions *Stratégique* et/ou *Opérationnel*, sélectionnez une période sur laquelle la prévision a été sauvegardée. Le graphe affiche une ligne verte pour la Version *Stratégique* et une ligne rouge pour la Version *Opérationnel*.

Ces données sont toujours disponibles, peu importe l'affichage sélectionné. Si vous ne souhaitez plus les faire apparaître, cliquez sur l'icône en forme d'œil dans la légende du graphe.

Vous pouvez comparer les données de ces Versions avec celles de *Forecast* dans le futur et/ou avec les données historiques dans le passé.

{{ 1 | image: "Versions en vue hebdo"}}

## Utiliser les données des Versions

Vous pouvez utiliser les données sauvegardées dans les Versions plutôt que celles de *Forecast* lors de la création de vos plannings.

Selon la méthode de dimensionnement choisie pour le Workload, vous pouvez utiliser les données de Version de 2 façons :

### Méthode Erlang C

Le résultat du dimensionnement est affiché dans la section **Besoin en personnel**. Sélectionnez la Version à utiliser puis cliquez sur _Utiliser le besoin_{:.doc-button}.

### Autres méthodes de dimensionnement

Pour les autres méthodes de dimensionnement cliquez sur _Utiliser Forecast_{:.doc-button} puis indiquez quelle Version doit être utilisée (*Forecast*, *Opérationnel* ou *Stratégique*).
