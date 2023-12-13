---
title: Fichiers Log
product_label:
  - on-premise
toc: false
redirect_from:
  - /fr/xlink-fichiers-log/
redirect_reason: Updated filename on 21 April 2022
---

<div markdown="1" class="hint-box-default hint-box-red">

Xlink est obsolète

Si vous utilisez actuellement Xlink pour votre abonnement injixo Cloud WFM, veuillez passer immédiatement à injixo Cloud Link ou à une solution qui respecte les normes d’intégration les plus récentes. N’hésitez pas à solliciter l’aide de nos experts [ici](https://www.injixo.com/fr/contact/).

</div>

L'application Xlink fournit des fichiers logs pour vous aider à résoudre les problèmes rencontrés.

Lorsque vous rencontrez un dysfonctionnement lors de l'utilisation de Xlink, veuillez vérifier les fichiers de logs pour analyser les avertissements (warnings) et les erreurs (errors).

Dans le fichier de configuration `isps_ul.ini`, vous trouverez dans les sectionss _General_{:.menu-item} et _Nom de votre système externe_{:.menu-item} le paramètre _Protocol_{:.menu-item}.

Configurer la valeur à 1 pour générer les fichiers logs suivants :

- _Isps_ul.log_ : informations concernant le chargement des paramètres, du mapping et des modifications de scripts.
- _Isps_uls.log_ : informations concernant les imports.
- _Interfaces - Logfiles_ : informations concernant les requêtes et les données retournées.

> Remarque
>
> Les fichiers de logs ne sont pas supprimés par Xlink et peuvent attendre une taille de 4Gb. Dans ce cas, Xlink n'importera plus de données. Vous pouvez soit désactiver les fichiers de logs soit les supprimer manuellement régulièrement.
