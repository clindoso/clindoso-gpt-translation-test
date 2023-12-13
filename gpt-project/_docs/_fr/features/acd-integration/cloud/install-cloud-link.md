---
title: Installer injixo Cloud Link
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Installer le client injixo Cloud Link pour importer des données dans injixo.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Qu’est-ce qu’injixo Cloud Link&nbsp;?

injixo Cloud Link est un logiciel client requis pour la configuration des intégrations on-premise. injixo Cloud Link importe régulièrement des données vers injixo. Vous pouvez également installer injixo Cloud Link lors de la configuration de vos intégrations par fichier CSV pour importer régulièrement de nouveaux fichiers depuis un dossier.

Le dossier d’installation du client contient&nbsp;:

- un fichier exécutable injixo-cloud-link,
- un ou plusieurs fichiers injixo-cloud-link.*.log,
- un fichier de configuration injixo-cloud-link.toml,
- un dossier licences contenant des licences de bibliothèques open source.

## Prérequis

- Windows&nbsp;: injixo Cloud Link fonctionne sous Windows 10 et versions ultérieures, et sur Windows Server 2016 et versions ultérieures.
- Linux&nbsp;: le package unixODBC doit être installé.
- Pare-feu/Proxy&nbsp;: autorisez le trafic Web via le port 443\. injixo Cloud Link utilise le chiffrement TLS avec connexion TCP sur le port 443.

Remarque&nbsp;: les intégrations on-premise accèdent à un système local à partir duquel elles récupèrent des données, par exemple un ACD ou un CRM. En fonction du type de base de données, vous devez installer un pilote de base de données.

## Installer injixo Cloud Link

Lorsque vous ajoutez une {% link_new intégration on-premise | features/acd-integration/cloud/add-on-premise-integration.md %}, une {% link_new intégration CSV | features/acd-integration/cloud/add-csv-integration.md %} ou une {% link_new intégration de base de données | features/acd-integration/cloud/add-database-integration.md %}, la section **Injixo Cloud Link** fournit des liens pour télécharger l’installateur client (pour Windows) ou l’archive (pour Linux).

### Installation du service Windows

Installez le premier service à l’aide du programme d’installation du client Windows&nbsp;:

1. Cliquez sur **Télécharger pour Windows 64-bit** et exécutez le programme d’installation.
2. Cliquez sur **Next**.
3. (Facultatif) Modifiez le dossier d’installation.
4. Cliquez sur **Next**, puis **Install**.  
   Une fenêtre de console affiche un PIN valide pour 5 minutes.  
   Pour [connecter Cloud Link à votre intégration](#connecter-injixo-cloud-link-à-votre-intégration), suivez les instructions de la console. 
5. Cliquez sur **Finish** dans le programme d’installation.  
   Le programme d’installation crée le service Windows **injixo Cloud Link**.

### Installer plusieurs services Windows

Vous pouvez installer jusqu’à huit services supplémentaires pour gérer des intégrations distinctes. Pour éviter de remplacer les instances de service précédemment installées, installez-les dans des dossiers différents. 

Pour installer un deuxième service Cloud Link sur Windows, ajoutez une nouvelle intégration et procédez comme suit&nbsp;:

1. Cliquez sur **Télécharger pour Windows 64-bit**.
2. Ouvrez une invite de commande Windows (cmd).
3. Pour la deuxième instance, exécutez la commande suivante&nbsp;:

   ```
   msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS=":instance.1"
   ```

   > Augmentez l’ID de l’instance dans le paramètre TRANSFORMS lorsque vous installez des instances supplémentaires.
   >
   > Par exemple, utilisez `":instance.2"` pour la troisième instance, `":instance.3"` pour la quatrième instance, et ainsi de suite.

  
4. Suivez les instructions de la procédure d’installation.  
   Le programme d’installation suggérera un nouveau dossier d’installation par défaut qui inclut l’instance, par exemple instance.1"  
   Conseil&nbsp;: pour identifier à quelle intégration appartient l’installation, vous pouvez ajouter les détails de l’ACD et du type d’importation, par exemple (ACD - import statut agent) au dossier d’installation par défaut.  
   Vous verrez le nouveau dossier et un nouveau service Windows nommé injixo Cloud Link (Instance {id}).

### Installation du service Linux

Installez le premier service selon l’exemple suivant&nbsp;:

1. Cliquez sur **Télécharger pour Linux 64-bit** et décompressez l’archive dans le dossier d’installation de votre choix.
2. Ouvrez un terminal.
3. Installez le service injixo Cloud Link&nbsp;:  
   `sudo ./injixo-cloud-link service install`
4. Lancez le service installé&nbsp;:  
   `sudo ./injixo-cloud-link service start`
5. Affichez un PIN à l’aide de la commande&nbsp;:  
   `sudo ./injixo-cloud-link pin`  
   Une fenêtre de console affiche un PIN valide pour 5 minutes.  
   Pour [connecter Cloud Link à votre intégration](#connecter-injixo-cloud-link-à-votre-intégration), suivez les instructions de la console. 

### Installer plusieurs services Linux

Vous pouvez installer plusieurs services pour gérer des intégrations distinctes. Pour éviter de remplacer les services précédemment installés, utilisez des dossiers différents.

Pour installer des services Linux supplémentaires, ajoutez une nouvelle intégration et procédez comme suit&nbsp;:

1. Créez un nouveau dossier et copiez les fichiers du dossier d’installation d’origine.
2. Ouvrez le ficher injixo-cloud-link.toml.
3. Modifiez la valeur **name** dans la section **[app]** avec un nouvel ID&nbsp;:

   ```
   [app]
name = "com.injixo.cloud-link.instance.1"
   ```

4. Installez et lancez le nouveau service depuis le nouveau dossier comme décrit précédemment.

## Connecter injixo Cloud Link à votre intégration

L’installation de Cloud Link affiche le message suivant et inclut un PIN&nbsp;:

```
** Avant de pouvoir lancer le client,
** reliez-le à votre compte injixo&nbsp;:
**  1) Connectez vous à injixo.com.
**  2) Ouvrez https://www.injixo.com/account/integrations.
**  3) Sélectionnez une intégration à laquelle vous souhaitez connecter le client.
**  4) Entrez votre PIN&nbsp;: 424242 (expire dans 5 minutes).
```

1. Retournez à la page **Ajouter une nouvelle intégration** dans votre navigateur.
2. Dans la section **injixo Cloud Link**, saisissez votre PIN dans le champ à six chiffres **PIN shown during installation**.
3. Cliquez sur _Connect_{:.doc-button}.
   Cloud Link se connecte à injixo. Continuez la configuration de votre {% link_new intégrationon-premise | features/acd-integration/cloud/add-on-premise-integration.md %} ou {% link_new CSV | features/acd-integration/cloud/add-csv-integration.md %}.

## Se connecter via un serveur proxy

Pour vous connecter via un serveur proxy, ajoutez le nom d’hôte ou l’adresse IP à la variable d’environnement **https_proxy**&nbsp;:

- Windows&nbsp;: ajoutez la variable d’environnement à la section **Variables système**. Si les services ne sont pas exécutés via le compte LocalSystem, configurez une variable utilisateur.
- Linux&nbsp;: configurez la variable d’environnement dans /etc/environment ou dans /etc/profile.d

Exemple&nbsp;: `https_proxy=http://your.proxy.example`

Si nécessaire, ajoutez le numéro de port (pour un port autre que 80) et les identifiants utilisateur pour l’authentification&nbsp;:

Exemple&nbsp;: `https_proxy=http://username:password@your.proxy.example:8080`

## Partager les adresses IP injixo de destination

Pour permettre à injixo Cloud Link de se connecter aux serveurs injixo cloud, partagez les URL suivantes&nbsp;:

- injixo-*.s3-eu-west-1.amazonaws.com,
- www.injixo.com.

Vous ne pouvez pas partager d’adresse IP unique. L’adresse IP du serveur change régulièrement lors du processus de déploiement et de mise à jour. Envisagez d’installer Injixo Cloud Link dans la DMZ. Si la connexion au serveur échoue, des [messages d’erreur de socket Windows](https://learn.microsoft.com/fr-fr/windows/win32/winsock/windows-sockets-error-codes-2) apparaissent dans le fichier journal.

## Journalisation

injixo Cloud Link change de fichier quotidiennement et après un redémarrage, sans supprimer les fichiers journaux. Les journaux actuels sont conservés dans injixo-cloud-link.log. Les fichiers en rotation incluent la date de rotation dans le nom du fichier. Vous devez les supprimer manuellement ou configurer une tâche récurrente.

### Activer la journalisation détaillée

injixo Cloud Link prend en charge un mode de journalisation détaillé pour les intégrations par base de données. Lorsque le mode détaillé est activé, le fichier journal affiche le nombre total de lignes récupérées et les dix premières lignes de données pour chaque requête.

Vous pouvez activer la journalisation de la façon suivante&nbsp;:

1. Arrêtez injixo Cloud Link.
2. Dans le dossier d’installation, ouvrez le fichier injixo-cloud-link.toml.
3. Dans la section **[app]**, définissez **verbose** sur true&nbsp;:

   ```
   [app]
verbose = true
   ```

4. Sauvegardez le fichier et redémarrez injixo Cloud Link.

## Configurer le dossier d’import

Par défaut, injixo Cloud Link importe les fichiers sauvegardés dans son dossier d’installation. Pour les intégrations CSV, vous pouvez configurer un dossier d’importation personnalisé de la façon suivante&nbsp;:

1. Arrêtez injixo Cloud Link.
2. Dans le dossier d’installation, ouvrez le fichier injixo-cloud-link.toml.
3. Dans la section **[app]**, définissez la valeur **importDirectory** sur votre dossier d’importation.
   - Utilisez des chemins d’accès relatifs ou absolus.
   - Échappez les barres obliques inverses avec une deuxième barre oblique inverse.
4. Sauvegardez le fichier et redémarrez injixo Cloud Link.

## Foire aux questions

<style>
table th:first-of-type {
    width: 25%;
}
table th:nth-of-type(2) {
    width: 75%;
}
</style>

| Question                                                                        | Réponse                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Comment obtenir un nouveau PIN si le premier a expiré&nbsp;?                              | Redémarrez injixo Cloud Link. Entrez le nouveau PIN du fichier journal dans le champ à six chiffres dans la section **injixo Cloud Link** de la page de configuration.                                                                                                                                                                                                                                                      |
| Comment supprimer Cloud Link de mon système&nbsp;?                                      | 1\. Exécutez à nouveau le programme d’installation d’injixo Cloud Link ou accédez à _Programmes > Programmes et fonctionnalités_{:.breadcrumbs} dans Windows.<br>2\. Cliquez avec le bouton droit sur l’entrée **injixo Cloud Link** dans la liste et sélectionnez **Désinstaller** ou **Désinstaller/Modifier**.<br>3\. Suivez les instructions à l’écran.<br><br>Pour désinstaller d’autres instances, accédez à _Programmes > Programmes et fonctionnalités_{:.breadcrumbs} dans Windows et suivez les étapes 2 et 3. |
| Comment déplacer injixo Cloud Link vers un nouveau serveur&nbsp;?                                | 1\. Cliquez sur l’{% icon pencil %} à droite d’une intégration pour la modifier.<br>2\. Cliquez sur **Connecter une nouvelle installation à injixo Cloud Link**.<br>3\. Téléchargez à nouveau injixo Cloud Link et installez le programme sur un nouveau serveur.                                                                                                                                                                          |
| Comment modifier l’intégration pour une installation d’injixo Cloud Link existante&nbsp;? | 1\. Accédez au dossier d’installation et copiez le PIN depuis le fichier journal.<br>2\. Supprimez l’intégration existante et créez une nouvelle intégration.<br>3\. Connectez votre service injixo Cloud Link en cours à la nouvelle intégration. Pour ce faire, entrez le PIN pendant la configuration de la nouvelle intégration.                                                                                                               |
