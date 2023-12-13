---
title: Modes d'import des données
product_label:
  - on-premise
redirect_from:
  - /fr/xlink-modes-import/
  - /fr/xlink-import-modus/
redirect_reason: Updated filename on 21 April 2022
---

Xlink vous permet d’importer automatiquement ou manuellement vos données historiques. Plusieurs modes sont disponibles et peuvent être paramétrés :

- importer les données du jour en cours toutes les n minutes
- importer quotidiennement les données du jour précédent à une heure précise
- importer manuellement les données

<div markdown="1" class="hint-box-default hint-box-red">

Xlink est obsolète

Si vous utilisez actuellement Xlink pour votre abonnement injixo Cloud WFM, veuillez passer immédiatement à injixo Cloud Link ou à une solution qui respecte les normes d’intégration les plus récentes. N’hésitez pas à solliciter l’aide de nos experts [ici](https://www.injixo.com/fr/contact/).

</div>

> Remarque
>
> Le mode d'import automatique retenu est le même pour tous les Systèmes externes paramétrés dans Xlink.

## Importation automatique des données

Pour paramétrer les modes d'import automatiques, sélectionnez _Importation automatique_{:.menu-item} du menu _Paramètres_{:.menu-item} de la console Xlink.

{{ 1 | image: "Modes import XLINK", '50%' }}

**Importer les données du jour en cours toutes les n minutes**

Ce mode permet de définir la fréquence intrajournalière d'import des données.

Lors d'une connexion ODBC, assurez-vous que les données à importer sont enregistrées dans le Système externe. Si vous observez un décalage, vous pouvez paramétrer un délai d'attente entre l'intervalle paramétré et le démarrage réel de l'import.
Par exemple, si vous souhaitez importer les données historiques toutes les 15 min avec un délai d'attente de 3 min, les processus de récupération des données démarreront à 00:03, 00:18, 00:33, 00:48, 01:03,...

> Remarques
>
> Xlink importera les données complètes de la journée à chaque import. Chaque processus prendra donc un plus de temps au fur à mesure de la journée.
>
> Assurez-vous que la durée nécessaire pour récupérer les données historiques par intervalle est plus court que l'intervalle lui même. Un import manuel vous permettra de connaitre cette durée.
>
> L'importation automatique est mise en attente lors d'un import manuel.

**Importer quotidiennement les données du jour précédent à une heure précise**

Cette option vous permet de paramétrer l'heure à laquelle les données de la journée précédente seront importées dans injixo.
Attention, l'import ne concernera que la journée précédente, pour importer les données de dates antérieures il faut réaliser un import manuel.

**Importer manuellement les données**

Si vous ne souhaitez ou ne pouvez pas automatiser l'import de vos données, sélectionnez _Aucune importation automatique_.
L'import manuel est notamment utile lors d'un nouveau mapping pour réaliser le premier import de données.

Vous pouvez importer manuellement les données sur la période de votre choix en cliquant sur _![Context Menu in xlink](/assets/img/{{ page.lang }}/features/xlink-import-mode/image-3.png)_{:.doc-button-icon} dans la barre de menu de la console Xlink ou en sélectionnant _Fichier > Importer > Import de données sur les appels_{:.breadcrumbs}.

## Inscrire des valeurs nulles\*\*

Le paramètre `Inscrire des valeur nulles`, accessible en cliquant sur _Paramètres > Inscrire des valeurs nulles_{:.breadcrumbs}, vous permet de déterminer le comportement de Xlink lors d'un import manuel sur des intervalles comportant déjà des données.
Si le paramètre est activé, Xlink réinitialise à 0 toutes les données sur la période sélectionnée puis importe les nouvelles valeurs.
Si ce paramètre est désactivé, les données existantes seront conservées.

## Importer les données en mode console

Il est possible d'importer les données en mode console. Pour ce faire :

- ouvrez une invite de commande MS DOS
- positionnez vous dans le répertoire d'installation de Xlink
- renseignez la commande suivante : `ISPS_UL.EXE -p -d DD/MM/YYYY -L 7`

Détail des paramètres :
-p = import de données sur les appels
-t = import de données sur les activités des employés
-d = indiquez après ce paramètre la date de début de l'import selon le format paramétré dans le fichier `isps_Ul.ini`
-L = indiquez à la suite de ce paramètre le nombre de jour à importer
