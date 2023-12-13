---
title: Importer les données de prévision
redirect_from:
  - /fr/import-donnees-prevision/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Forecast vous permet d'importer vos prévisions vers un Workload depuis un fichier CSV.

## Comment importer les données ?

Les étapes suivantes permettent de charger vos données de prévision :

1. Sélectionnez le Workload concerné
2. Cliquez sur _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} et sélectionnez **Importer les données de prévision**
3. Sélectionnez votre fichier CSV
4. Confirmez en cliquant sur _Valider l'import_{:.doc-button}

## Format du fichier CSV

Le format du fichier CSV est unique et ne peut être modifié. Il doit respecter les contraintes suivantes :

- L'intervalle de prévision peut être 15, 30 ou 60 minutes. Cet intervalle doit être identique à celui de la ou des files d'attente affectées au Workload.
- Il faut une ligne d'en-tête et 3 colonnes comportant respectivement la période, les volumes et le TMT. La période doit obligatoirement être au format `YYYY-MM-DD HH:MM`.
- Une ligne par intervalle est nécessaire et ce même s'il n'y a aucune valeur sur un intervalle.
- Le séparateur peut être la virgule (`,`) ou le point virgule (`;`).
- Les données importées peuvent être des nombres entiers ou décimaux à condition d'utiliser le point (par exemple 10.8 ou 354.23).
- Les données importées doivent être sur le même fuseau horaire que le Workload (et donc le même que celui de la ou des files d'attente).

## Exemple de fichier CSV

Le format du fichier CSV doit correspondre au modèle suivant :

```
Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:15;34;234
2020-05-17 15:30;31;231
2020-05-17 15:45;44;221
2020-05-17 16:00;42;200
2020-05-17 16:15;54;300
2020-05-17 16:30;40;180
2020-05-17 16:45;41;181
2020-05-17 17:00;40;180
2020-05-17 17:15;29;241
2020-05-17 17:30;31;205
2020-05-17 17:45;33;233
2020-05-17 18:00;40;180
2020-05-17 18:15;29;190
2020-05-17 18:30;25;198
2020-05-17 18:45;12;180
2020-05-17 19:00;;
2020-05-17 19:15;;
2020-05-17 19:30;;
2020-05-17 19:45;;
...
```

Il n'est pas nécessaire d'importer tous les intervalles d'une journée, un intervalle peut ne pas contenir de données (par exemple en dehors des heures d'ouverture de la file d'attente, comme après 19h dans l'exemple ci-dessus).

Il est possible de soit :
- Laisser l'intervalle sans données de volume.
- Ne pas mettre de ligne correspondant à ces intervalles.

Ces intervalles resteront vides et ne seront pas remplacés par des 0 lors de l'import.

Il est possible d'utiliser les données téléchargées depuis une Version (*Auto-Forecast*, *Opérationnel* ou *Stratégique*) pour ensuite les importer. Le format du fichier CSV peut alors suivre le modèle suivant :

```
Timestamp;Offered_auto;AHT_auto
2020-05-17 16:30;40;180
...
```

```
Timestamp;Offered_operational;AHT_operational
2020-05-17 16:30;40;180
...
```

> Remarque
>
> 1. La taille maximale du fichier doit être de 20Mo.
> 2. Nous recommandons de limiter l'import à un fichier CSV de 20K lignes.
> 3. L'import des données historiques n'est actuellement pas possible.
