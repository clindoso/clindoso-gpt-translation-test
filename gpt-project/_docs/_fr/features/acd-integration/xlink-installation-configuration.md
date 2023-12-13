---
title: Installation et configuration
product_label:
  - on-premise
redirect_from:
  - /fr/xlink-installation/
redirect_reason: Updated filename on 21 April 2022
---

Cet article décrit les étapes pour réaliser une première installation de Xlink.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink est obsolète

Si vous utilisez actuellement Xlink pour votre abonnement injixo Cloud WFM, veuillez passer immédiatement à injixo Cloud Link ou à une solution qui respecte les normes d’intégration les plus récentes. N’hésitez pas à solliciter l’aide de nos experts [ici](https://www.injixo.com/fr/contact/).

</div>

### 1. Prérequis

Les prérequis sont les suivants :

- Avoir les droits Administrateur Windows de la machine sur laquelle Xlink sera installé.
- Ajouter une règle sur le firewall pour ouvrir le port 45054 en TCP/IP vers votre tenant injixo (pour les tenants ouvert avant le 01/01/2019, il faut utiliser le port 80 au lieu du port 45054).

### 2. Créer l'utilisateur Xlink

1. Connectez-vous sur [www.injixo.com](https://www.injixo.com/login).
2. Dans le menu _Account > Utilisateurs_{:.breadcrumbs}, cliquez sur _Nouvel utilisateur_{:.doc-button}.
3. Pour les champs **Prénom** et **Nom**, entrez le texte de votre choix, par exemple Utilisateur Xlink.
4. Remplissez le champ **Adresse électronique** qui commence par xlink, par exemple **xlink@votreentreprise.com**.
5. Ne sélectionnez aucun **Rôle**.
6. Cliquez sur _Créer un utilisateur_{:.doc-button}.
7. Entrez un nouveau mot de passe en cliquant sur _Nouveau mot de passe_{:.doc-button}. Conservez ce mot de passe pour la suite.

### 3. Télécharger l'application Xlink

Vous pouvez télécharger l'application Xlink à la page [Downloads](https://downloads.injixo.com/fr).

Dézippez le fichier téléchargé. Copiez le contenu du dossier **xlink-xx** dans votre dossier de destination (par exemple `C:/Xlink`).
xx désigne le numéro de version de l'application Xlink.

### 4. Configuration de la connexion entre Xlink et injixo

La procédure de configuration est la suivante :

1. Exécutez le fichier `Passcode.exe` dans le dossier `support-applications` de votre répertoire Xlink.

Dans le premier champ, entrez le mot de passe que vous avez assigné à l'utilisateur Xlink lors de l'étape 2.
Un mot de passe chiffré apparaît dans le second champ. Copiez-le puis cliquez sur _OK_{:.doc-button}
{{ 1 | image: 'Passcode.exe without input', '75%' }}
{{ 2 | image: 'Passcode.exe without input', '75%' }}

2.  Copiez les fichier `isps_Ul.ini`, `isps.cfg` et `acd_map.ini` depuis le dossier `sample-configurations` vers la racine de votre répertoire Xlink.

3.  Ouvrez le fichier `Isps_Ul.ini` avec un éditeur de texte (par exemple Notepad).

4.  Dans la section [DB], remplacez les élements suivants :
    a. L'utilisateur **xlink@xxxx.com** par l'utilisateur que vous avez créé lors de l'étape 2.
    b. Le texte &lt;password from generator&gt; (en incluant les &lt; &gt;) par le mot de passe chiffré que vous avez généré grâce à `Passcode.exe`.

        Vous devez obtenir un résultat similaire :
        ```

    [DB]
    1=WFM,0,xlink@injixo.com,3951BCCDDCDCAC5B4C

    ```

    ```

5.  Sauvegardez et fermez le fichier.
6.  Connectez-vous à injixo.
7.  Cliquez sur la section **WFM**.
8.  Copiez la partie en gras de l'URL https://iwfm-**nomhote**.injixo.com/iwfm/ disponible à partir de la barre d'adresse du navigateur.
9.  Ouvrez le fichier `Xlink/isps.cfg` et remplacez la partie "xxxx" par le texte copié précédement dans la ligne Url = "iwfms://iwfm-xxxx.injixo.com:45054".

        Vous devez obtenir un résultat similaire :
        ```

    [IES System WFM]  
    Name = "WFM"  
    Url = "iwfms://iwfm-5y2jgr6o.injixo.com:45054"

    ```

    ```

10. Sauvegardez les modifications et fermez le fichier.

> Remarque
>
> Pour les clients ayant souscrit à injixo avant le 01/01/2019, il faut remplacer la valeur 45054 par 80.

### 5. Enregistrer ixculcmm.dll

Copiez le fichier `register.exe` depuis le dossier `sample-configurations` vers la racine de votre répertoire Xlink.
Ensuite, ouvrez une Invite de commande Windows et déplacez vous jusqu'à votre répertoire Xlink puis tapez la commande suivante :

`register.exe ixculcmm.dll /system`

Appuyez sur Entrée pour valider. Cette action permet d'enregistrer le fichier `ixculcmm.dll` sur votre ordinateur.

Le message suivant doit apparaître : `ixculcmm.dll registered SYSTEM GLOBAL`

> Remarque
>
> Si un message d'erreur apparaît, supprimer le droit en lecture seule sur le fichier `ixculcmm.dll` (Clic droit sur le fichier > Propriétés > décocher la case "Lecture seule").
>
> Réitérez l'étape "register.exe ixculcmm.dll /system". Si cela ne fonctionne pas, vous trouverez de plus amples informations {% link_new ici | support/faq/xlink-frequent-error-messages.md %}.

### 6. Installation du service Xlink

Pour terminer l'installation de Xlink, vous devez installer le service _ISPS Xlink_.
Entrez la commande suivante dans l'Invite de commandes Windows : `isps_uls.exe -install`

L'installation s'est déroulée correctement si le message suivant apparaît :

```
ISPS Xlink installed.
Starting up ISPS Xlink.
ISPS Xlink started.
```

Après l'installation du service Xlink, vous pouvez fermer l'Invite de commande Windows.

### 7. Est-ce que tout fonctionne bien ?

Exécutez le fichier `isps_Ul.exe`. Dans la section de gauche, vous pouvez voir les systèmes externes que vous avez créés. Dans la section de droite, vous avez un dossier `WFM` qui contient toutes les files d'attentes que vous allez créer.

Si vous avez tous ces éléments, vous avez terminé l'installation et la configuration de Xlink !

> Remarque
>
> En cas de mise à jour de Xlink, reportez-vous à l'article {% link_new suivant | support/faq/xlink-update.md %}
