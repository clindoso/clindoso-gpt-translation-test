---
title: Télécharger les données de prévision
redirect_from:
  - /fr/telecharger-prevision/
redirect_reason: Updated filename on 21 April 2022
---

Il est possible de télécharger les données de prévision au format CSV si vous souhaitez les utiliser en dehors d'injixo.

Vous pouvez sélectionner une plage de date allant d'une journée à l'année entière.
La granularité des données dépend de l'intervalle du Workload.
Les données exportées correspondent au fuseau horaire du Workload.

Vous pouvez sélectionner les données des {% link_new Versions | features/forecast/injixo-forecast/store-forecast-versions.md %}. _Forecast_, _Opérationnel_ et/ou _Stratégique_.

## Comment télécharger les données

1. Sélectionnez le Workload concerné
2. Affichez la période de votre choix (jour, semaine, mois, année)
3. Cliquez sur _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} puis sur **Télécharger au format CSV**.
4. Choisissez les Versions parmi _Forecast_, _Opérationnel_ et/ou _Stratégique_.
5. Confirmez votre choix en cliquant sur _Démarrer le téléchargement_{:.doc-button}.

## Exemple de fichier CSV

Si vous téléchargez les données de prévision du Workload "SAV", vous obtiendrez un fichier CSV nommé _SAV-Appels.csv_
Le nom du fichier contient donc le nom du Workload et le type d'opération.

Si vous sélectionnez les Versions _Forecast_ et _Opérationnel_, le fichier sera constitué ainsi :

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
...
2020-05-17 16:30;40;180;35;175
2020-05-17 16:45;41;181;37;183
2020-05-17 17:00;40;180;35;175
2020-05-17 17:15;41;181;37;183
...
```

Le fichier CSV contient donc l'intervalle horaire et les données par type de valeur pour chaque prévision.

> Remarque
>
> Ne sont pas incluses dans le téléchargement :
>
> - Les informations concernant les jours de congés ou les événements attachés au Workload
> - Les données historiques
