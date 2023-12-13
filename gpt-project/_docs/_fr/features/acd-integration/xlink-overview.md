---
title: Vue d'ensemble
product_label:
  - on-premise
promote-service: acd-integration-support
redirect_from:
  - /fr/xlink-vue-ensemble/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-installation-configuration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-import-mode.md
---

Xlink permet d'importer deux types de données provenant de systèmes tiers tels que des systèmes de téléphonie (ACD).
Le premier type de données à importer est la volumétrie d'opérations qui servira ensuite à prévoir et planifier : appels, sessions de chat, e-mails, documents, etc.
Le second type de données à importer est le statut des agents : connexion/déconnexion, activité en cours, pause, retrait, etc.

L'intégration est possible directement avec l'ACD (ODBC) ou via un fichier plat (format CSV).

<div markdown="1" class="hint-box-default hint-box-red">

Xlink est obsolète

Si vous utilisez actuellement Xlink pour votre abonnement injixo Cloud WFM, veuillez passer immédiatement à injixo Cloud Link ou à une solution qui respecte les normes d’intégration les plus récentes. N’hésitez pas à solliciter l’aide de nos experts [ici](https://www.injixo.com/fr/contact/).

</div>

## Informations générales

_Xlink Suite_{:.menu-item} est disponible en téléchargement à la page [Downloads](https://downloads.injixo.com/fr).

Xlink peut être installé soit sur un serveur soit sur un poste utilisateur.

## Prérequis technique

- Système d'exploitation : Windows Server 2012/Windows 7 (ou supérieur)
- CPU : 2 coeurs @2,2GHz (ou supérieur)
- RAM : 2Go hors système d'exploitation
- Disque dur : 20Go de disque dur hors système d'exploitation

Notez que XLink peut être déployé sur un environnement virtualisé.

## Service ISPS Xlink

Le **service ISPS Xlink (isps_uls.exe)** réalise l'import des données. Toutes les données d'une journée entière sont toujours importées. L'import des données ne fonctionne que si le service `ISPS XLink` est démarré.

Le service Windows installé porte toujours le nom `ISPS XLink`. Ce service ne peut être installé qu'une seule fois sur la même machine.

Le service démarre automatiquement après l'installation. La configuration du paramètre _Type de démarrage_ du service est en `Automatique` par défaut afin d'assurer un redémarrage immédiat après un redémarrage serveur.

Une aide vous est proposée lorsque vous saisissez `isps_uls.exe` en ligne de commande. Les paramètres disponibles sont les suivants :

- Le paramètre _-install_/_-remove_ permet d'installer/désintaller le service Xlink
- Le paramètre _-console_ permet de démarrer le service en mode console. Cela vous permet d'utiliser le compte de l'utilisateur lié à la session Windows contrairement au mode service qui utilise le compte dédié aux services Windows. Cette option permet d'identifier les problèmes de configuration.

#### Modifier le compte utilisateur

Dans la fenêtre de configuration du service Windows, spécifiez le compte utilisateur qui doit être utilisé pour exécuter le service. Si _Ouvrir une session en tant que_{:.menu-item} est sélectionné, vous devez laisser l'option _Compte système local_{:.menu-item} sélectionné pour les installations en local du service. Lors de cas exceptionnels, par exemple quand aucune valeur n'est importée même si la configuration est correcte ou que le dossier d'import n'est pas accessible, il est nécessaire de créer un nouveau compte utilisateur. Dans ce cas, créez un compte local appartenant au groupe Administrateurs.

### Interface ISPS Xlink

{{ 1 | image: 'Xlink Interface'}}

L'**interface utilisateur Xlink (isps_ul.exe)** permet la configuration globale du service Xlink, des systèmes externes et du mapping entre les données ACD et injixo.
L'interface permet également de déclencher un import manuel.

L'interface Xlink se compose de 3 sections :

1. _Interface_{:.menu-item} affiche la liste des systèmes externes créés dans _WFM_{:.menu-item}.
2. _Files d'attente iWFM_{:.menu-item} affiche les files d'attente et les types de valeur liées à votre environnement. Ces éléments doivent être créés au préalable dans le menu _Administration_{:.menu-item}.
3. _Mapping_{:.menu-item} affiche les données du système externe lié à la file d'attente. Ce champ doit être vide tant que le mapping n'a pas été réalisé.

### Fichiers de configuration

**ISPS.CFG**

Le fichier `isps.cfg` permet de configurer la connexion à injixo en utilisant une adresse IP ou un nom DNS. Pour injixo en mode Cloud, vous pouvez trouver cette valeur en cliquant sur le menu _WFM_{:.menu-item} et en récupérant l'URL affichée dans le navigateur. Copier la partie centrale de l'URL, dans notre exemple 'abcdefg' -> https://**abcdefg**.injixo.com/iwfm/.

**ISPS_UL.INI**

Le fichier `isps_ul.ini` permet de configurer l'utilisateur et le mot de passe Xlink. Vous pouvez également configurer les paramètres d'import et les éléments spécifiques des connecteurs.

### Sauvegarde des données

Les fichiers suivants devront être sauvegardés périodiquement ou à chaque modification, ce qui vous permettra de restaurer la configuration de Xlink en cas de perte de données.

- `isps_ul.ini`
- `acd_map.ini`
- `isps.cfg`
- `*.bas`

> Remarque
>
> Si vous modifiez la configuration des fichiers manuellement, vous devez redémarrer le service `ISPS XLink`.
