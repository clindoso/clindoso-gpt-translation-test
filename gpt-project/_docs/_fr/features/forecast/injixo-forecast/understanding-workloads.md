---
title: Comprendre les Workloads
toc: false
redirect_from:
  - /fr/comprendre-workloads/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

## Qu'est-ce qu'un Workload ?

Avec injixo, vous planifiez des activités dans le planning de vos employés, comme par exemple l’activité _Appels entrants Vente_. Pour chaque activité que vous souhaitez optimiser vous devez créer un besoin en personnel, ce besoin étant réparti sur l’ensemble de la journée, tous les 1/4h ou 1/2h par exemple. Lorsque vous utilisez injixo Forecast, vous spécifiez la ou les files d’attente à utiliser pour le calcul du besoin en personnel, qui sont appelés _Workloads_. Un seul Workload est utilisé pour créer le dimensionnement d’une activité planifiée. Chaque Workload peut donc lire les données historiques d'une ou plusieurs files d'attente, par exemple, les files d'attente _Appels entrants Vente Ouest_ et _Appels entrants Vente Est_ déterminent les besoins en personnel pour l'activité _Appels entrants Vente_.

Prenons un exemple.

Imaginez que dans votre système téléphonique, vous avez configuré cinq files d'attente :

- **Vente Est** : Ventes de nouveaux produits pour la région Est
- **Vente Centre**: Vente de nouveaux produits pour la région centrale
- **Vente Ouest** : Ventes de nouveaux produits pour la région Ouest
- **Support niveau 1** : Connaissance générale du produit ou questions client faciles à traiter
- **Support niveau 2** : Questions client plus compliquées

Il est important pour votre centre de contacts de séparer vos files d'attente de Support niveau 1 et niveau 2, car en effet il est beaucoup plus facile pour vous de former des agents pour le Support de niveau 1. Et comme vous avez en plus beaucoup plus de volume, vous ne voulez pas que vos agents Support niveau 2 soient sollicités pour répondre aux questions dites plus faciles, au détriment des cas les plus complexes.

Il est clair que les volumes d'appels pour le Support de niveau 1 et le Support de niveau 2 représentent deux types de sollicitations différentes pour vos employés et tous vos agents ne peuvent pas faire les deux (vous ne voulez pas que vos agents de niveau 1 traitent les questions de niveau 2 pour lesquelles ils ne sont pas formés et vous ne voulez pas que vos agents de niveau 2 traitent les appels de niveau 1 pour qu’ils soient disponibles pour les cas client complexes).

Concernant les appels Vente, il est important pour votre entreprise de séparer vos files d'attente entre l'Est, le Centre et l'Ouest. En effet vous voulez pouvoir monitorer séparément les appels provenant de ces régions, de sorte que vous puissiez suivre les campagnes de marketing de façon indépendante dans ces régions. Cependant, pour le service clients que vous êtes, ce n'est pas une distinction importante car n'importe quel agent qui peut répondre à un appel Vente pour la région de l'Est du Centre ou de l'Ouest..

En effet, une fois que vos appels de vente sont entrés dans leurs files d'attente régionale, la provenance n'a plus d'importance pour vos agents. N'importe quel agent qui peut gérer un appel de la région de l'Est peut gérer les deux autres régions tout aussi facilement, et vice versa. Les appels qui arrivent dans la file d'attente des ventes de l'Est sont somme toute les mêmes que ceux qui arrivent dans les files d'attente de la région du Centre ou de l'Ouest. Et comme il serait inefficace de n'avoir que quelques agents de Vente qui s'occupent des files d'attente de la région de l'Est, vous configurez votre système téléphonique pour que tous vos agents de Vente prennent les appels des trois régions.

Les Workloads sont conçus pour tenir compte du fait que les appels qui arrivent dans des files d'attente différentes peuvent représenter le même type de traitement de vos agents. Dans l’exemple explicité ci-dessus,, vous avez donc cinq files d'attente, mais seulement trois Workloads à créer : Support de niveau 1, Support de niveau 2 et Appels entrants Ventes (qui est la consolidation des appels des régions de l'Est, du Centre et de l'Ouest).

Il faudra donc créer ces 3 Workloads:

{{ 1 | image: "exemple oragnisation workloads", '70%' }}

Comme la typologie d’appels, et donc le traitement de vos agent est différent pour les Support niveau 1 et niveau 2, vous devrez prévoir ces flux séparément, de sorte que vous sachiez combien d'agents de niveau 1 et de niveau 2 vous avez besoin. Mais vous pouvez prévoir les appels de Vente de l'Est, du Centre et de l'Ouest en même temps, puisque ces appels sont finalement les mêmes.
injixo Forecast vous permet donc de regrouper ces trois files d'attente en un seul et même Workload.

Par la suite, lorsque vous mettrez en place vos activités, toutes vos activités productives seront “associées” au Workload qui permet le calcul de leur prévisions et leur besoin en personnel.

> Planifier des activités à partir de Workloads multiples
>
> Dans notre exemple, nous avons statué que les agents de Support niveau 1 ne pouvaient pas traiter les appels de niveau 2, et que les agents de Support niveau 2, même si ils pouvaient traiter les appels de niveau 1, n’étaient pas planifiés sur cette activité. Bien que vous souhaitiez réserver vos agents de niveau 2 pour leurs appels de niveau 2 qui sont plus complexes à traiter, il pourrait être utile de leur acheminer des appels de niveau 1, peut-être avec une priorité moindre ou en débordement. Comme le traitement de ce type d’appel est différent, vous pouvez prévoir et dimensionner les appels de niveau 1 et de niveau 2 basés sur leurs propre Workload, et vous pouvez prendre en compte la compétence des agents de niveau 2 sur la couverture de l’activité de niveau 1 dans la planification.
>
> Dans injixo, vous le ferez à l'aide de la {% link_new multi-activités | features/administration/activity-types-and-properties.md | #sous-activités %}.
