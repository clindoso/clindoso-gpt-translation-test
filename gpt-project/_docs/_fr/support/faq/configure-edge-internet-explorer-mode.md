---
title: Utiliser Microsoft Edge en mode Internet Explorer
product_label:
  - advanced
  - enterprise
  - classic
description: Utiliser Microsoft Edge en mode Internet Explorer.
redirect_from:
  - /fr/support-edge/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

Le mode Internet Explorer de Microsoft Edge permet d'afficher des pages utilisant des contrôles ActiveX utilisés dans injixo. Consultez le site [Microsoft](https://docs.microsoft.com/fr-fr/deployedge/edge-ie-mode) pour en savoir plus sur le mode Internet Explorer de Microsoft Edge.

Le mode Internet Explorer a été testé avec succès sur *Microsoft Edge 89.0.774.54* sur *Windows 10 Pro 64 bit Version 1909 (Build 18363.1379)*.
Pour les installations Microsoft Windows Server, le mode Internet Explorer n'est disponible que via l'extension IE Tab (cf. option 2).

## Installer les applications

1. Télécharger Microsoft Edge sur le site de [Microsoft](https://support.microsoft.com/fr-fr/microsoft-edge/t%C3%A9l%C3%A9charger-le-nouveau-microsoft-edge-bas%C3%A9-sur-chromium-0f4a3dd7-55df-60f5-739f-00010dba52cf) et installer le navigateur
2. [Télécharger](https://downloads.injixo.com/fr#client-injixo) et {% link_new installer | getting-started/browser-setup.md %} la dernière version du client injixo
3. Rechercher **Options internet** dans la barre de recherche Windows en bas à gauche de l'écran
4. Ajouter *\*.injixo.com* en tant que *site de confiance* à l'onglet **Sécurité**

## Utiliser le mode Internet Explorer de Microsoft Edge (recommandé - dernière version de Edge)

Dans le dernière version de Edge, il est nécessaire de configurer le mode Internet Explorer grâce au gestionnaire de listes de sites du mode entreprise. Ce paramétrage a été testé avec succès sur la version 97.0.1072.76.

1. Créer une [liste de sites](https://docs.microsoft.com/fr-fr/deployedge/edge-ie-mode-site-list-manager) du mode Enterprise.
Exemple de fichier :

    ```
    <site-list version="1.0">
      <site url="https://yourhost.injixo.com/iwfm/">
        <compat-mode>Default</compat-mode>
        <open-in>IE11</open-in>
      </site>
      <shared-cookie 
        domain=".injixo.com" 
        name="injixo_session" 
        source-engine="MSEdge">
      </shared-cookie>
      <shared-cookie 
        domain=".injixo.com" 
        name="iwfm_language_id" 
        source-engine="MSEdge">
      </shared-cookie>
    </site-list>
    ```

2. Ajouter 2 nouvelles entrées au registre Windows. Un administrateur informatique peut être nécessaire pour réaliser cette manipulation :

    1. Taper **regedit** dans la barre de recherche du menu Démarrer puis sélectionner **Editeur de registre**.
    2. Aller à **HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft**.
    3. Créer un nouveau dossier nommé **Edge** (s'il n'existe pas déjà).
    4. Ajouter les valeurs ci-dessous dans le dossier **Edge** précedemment créé :
        - **InternetExplorerIntegrationLevel** (REG_DWORD) avec la valeur 1 (ou 0x00000001 en hexadécimal)
        - **InternetExplorerIntegrationSiteList** (REG_SZ). Renseigner le chemin d'accès de votre fichier XML de *liste de sites*. Il est possible de renseigner une URL (par exemple https://test.company.com/list.xml) ou un chemin d'accès local (file:///c:/path/to/list.xml).

3. Redémarrer Edge pour valider ces modifications.

Pour en savoir plus sur la configuration de Microsoft Edge ou la résolution d'anomalie, aller à :
- [edge://policy/](edge://policy/) — aide relative aux entrées de registre et à la configuration des stratégies dans Edge.
- [edge://compat/enterprise](edge://compat/enterprise) — visualiser, mettre à jour, exporter ou importer votre fichier XML de liste de sites.

## Utiliser le mode Internet Explorer de Microsoft Edge (recommandé - anciennes versions de Edge)

1. Ouvrir **Microsoft Edge**
2. Cliquer sur **Paramètres et plus** (...) en haut à droite du navigateur
    {{ 1 | image: "Settings menu ",  '30%' }}
    
3. Cliquer sur **Paramètres** et sélectionner **Navigateur par défaut**
4. Activer l'option **Autoriser le rechargement des sites en mode Internet Explorer** à la section *Compatibilité d'Internet Explorer*
    {{ 2 | image: "Settings screen reload activation",  '70%' }}

5. Cliquer sur **Redémarrer**

Une fois le mode Internet Explorer activé :
1. Se connecter à injixo
2. Cliquer sur **Paramètres et plus** (...) en haut à droite du navigateur
3. Cliquer sur **Recharger en mode Internet Explorer**
    {{ 3 | image: "page reload",  '50%' }}
    
Les contrôles ActiveX seront chargés correctement après votre reconnexion.
