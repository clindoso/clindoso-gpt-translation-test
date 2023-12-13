---
title: Récupération des données historiques
product_label:
  - on-premise
redirect_from:
  - /fr/xlink-mapping-historique/
redirect_reason: Updated filename on 21 April 2022
---

Après avoir configuré le Système externe, vous pouvez maintenant importer les données historiques dans vos différentes files d'attente.

Pour indiquer quelles données doivent être importées, il est nécessaire de réaliser un mapping entre les données du Système externe (appels reçus, TMT,...) et les types de valeur d'injixo. Ce mapping est réalisé dans la console Xlink.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink est obsolète

Si vous utilisez actuellement Xlink pour votre abonnement injixo Cloud WFM, veuillez passer immédiatement à injixo Cloud Link ou à une solution qui respecte les normes d’intégration les plus récentes. N’hésitez pas à solliciter l’aide de nos experts [ici](https://www.injixo.com/fr/contact/).

</div>

## Présentation de la console Xlink

Exécutez le fichier `isps_ul.exe` disponible dans le répertoire d'installation de Xlink pour lancer la console Xlink.

{{ 1 | image: "Console Xlink"}}

La console Xlink est divisée en 3 parties :

- La section **Interface** présente les files d'attente et types de valeur des Systèmes externes
- La section **Files d'attente iWFM** affiche les files d'attente paramétrées dans injixo
- La section **Mapping** détaille la liaison réalisée entre le Système externe et le type de valeur sélectionné

> Remarque
>
> Nous vous conseillons de lancer l'application en mode administrateur. Pour cela, faites un clic droit sur le fichier isps_ul.exe puis sélectionnez `Exécuter en tant qu'administrateur`.

## Création d'un mapping

La création d'un mapping entre un Système externe et une file d'attente injixo doit suivre les étapes suivantes :

1. Cliquer sur le type de valeur de la file d'attente injixo dans la section _Files d'attente iWFM_
2. Double cliquer sur le type de valeur de la file d'attente du Système externe dans la section _Interface_. Le détail de la liaison apparaît dans la section _Mapping_
3. Double cliquer à nouveau sur le type de valeur de la file d'attente injixo dans la section _Files d'attente iWFM_
4. Une fenêtre pop-up apparaît. Cliquer sur _Appliquer_{:.doc-button} pour générer le script par défaut dans la section _Scénario_
5. Cliquer sur _Oui_{:.doc-button}
6. Cliquer sur _OK_{:.doc-button} pour valider le mapping

{{ 2 | image: "mapping Xlink" , '500' , 'gif' }}

Cette opération est à réaliser pour toutes les données que vous souhaitez importer depuis votre Système externe vers injixo.

A la création de chaque mapping, le fichier système `acd_map.ini` est automatiquement complété et des fichiers avec l'extension .BAS sont créés dans le répertoire d'installation de Xlink.

## Import des données historiques

Une fois le mapping réalisé, vous pouvez importer les données historiques de votre Système externe. Pour ce faire, cliquez sur _![Context Menu in xlink](/assets/img/{{ page.lang }}/features/xlink-mapping-telephony/image-3.png)_{:.doc-button-icon} en haut à gauche de la console Xlink pour initier le processus. Renseignez les dates de début et de fin puis cliquez sur _OK_ pour démarrer l'import.
