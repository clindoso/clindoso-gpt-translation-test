---
title: Configuration du navigateur
description: Configurez votre navigateur pour l’utiliser avec injixo.
product_label:
  - on-premise
  - classic
related_articles:
  - overwrite_title: Résoudre les erreurs d’installation du client
    filepath: support/faq/client-installer-errors.md
  - overwrite_title: Expiration de la session lors de l’accès au module WFM
    filepath: support/faq/session-timeout-message.md
redirect_from:
  - /fr/setup-guide/
redirect_reason: Updated filename on 27 July 2023
---

Pour utiliser les fonctionnalités avec des composants ActiveX dans WFM, utilisez {% link_new Microsoft Edge en mode Internet Explorer | support/faq/configure-edge-internet-explorer-mode.md %}. Vous trouverez une liste des navigateurs compatibles dans les {% link_new Prérequis techniques | getting-started/system-requirements.md | #navigateurs-compatibles %}.

Si vous ne disposez pas des droits suffisants pour modifier les paramètres de votre navigateur ou pour installer des applications, contactez le service informatique de votre entreprise.

## Configurer les sites de confiance et les paramètres de la zone de sécurité

injixo Classic et injixo Enterprise WFM utilisent des contrôles ActiveX. Vous devez autoriser le navigateur (Edge en mode IE) à exécuter ces contrôles ActiveX.

Dans les paramètres du navigateur, ajoutez toutes les pages d’injixo (_*.injixo.com_) aux sites de confiance&nbsp;:

1. Ouvrez le menu démarrer de Windows, tapez options internet et appuyez sur la touche Entrée.
2. Dans l’onglet **Sécurité**, sélectionnez la zone **Sites de confiance** et cliquez sur _Sites_{:.doc-button}.
3. Dans le champ **Ajouter ce site web à la zone**, entrez https://\*.injixo.com.
4. Cochez la case **Exiger la vérification du serveur (https:) pour tous les sites de cette zone**.
5. Cliquez sur **Ajouter**.
6. Cliquez sur **Fermer**.

{{ 1 | image:  'paramètres de sécurité', '45%', 'png'  }}

Ajustez le niveau de sécurité de la zone pour les sites de confiance&nbsp;:

1. Dans le menu démarrer de Windows, tapez options internet et appuyez sur la touche Entrée.
2. Dans l’onglet **Sécurité**, sélectionnez la zone **Sites de confiance**.
3. Décochez la case **Activer le mode protégé**.  
   Remarque&nbsp;: cette case à cocher n’est plus disponible dans Windows 11 et versions ultérieures.
4. Dans l'onglet **Sécurité**, ajustez le niveau de sécurité pour les **sites de confiance** sur **Moyen** ou **Moyen-bas**. Moyen-bas vous permet de passer les étapes 6 à 9.
5. Cliquez sur _OK_{:.doc-button}.
6. Cliquez sur _Personnaliser le niveau..._{:.doc-button}.
7. Dans la fenêtre de dialogue **Paramètres de sécurité**, modifiez les paramètres suivants&nbsp;:

   | Paramètre                                           | État             |
   | ------------------------------------------------- | ----------------- |
   | Contrôles ActiveX reconnus sûrs pour l’écriture de scripts | ACTIVÉ           |
   | Exécuter les contrôles ActiveX et les plug-ins                  | ACTIVÉ           |
   | Télécharger les contrôles ActiveX signés                  | DEMANDER ou ACTIVÉ |
   | Demande automatique pour les contrôles ActiveX          | ACTIVÉ           |

8. Cliquez sur _OK_{:.doc-button}.
   Le message suivant apparaît&nbsp;: Êtes-vous sûr de vouloir modifier les paramètres de cette zone&nbsp;?
9. Cliquez sur _Oui_{:.doc-button}.
10. Pour fermer la fenêtre de dialogue, cliquez sur _OK_{:.doc-button}.

## Installation du client injixo

injixo Classic et injixo Enterprise WFM contiennent des contrôles ActiveX, qui nécessitent {% link_new Microsoft Edge en mode IE | support/faq/configure-edge-internet-explorer-mode.md %}et le client injixo.

Si vous voyez un message d’erreur lors de la connexion ou dans injixo&nbsp;:

- utilisez un navigateur {% link_new compatible | getting-started/system-requirements.md | #navigateurs-compatibles %}.
- installez le client injixo (comme décrit ci-dessous).

### Installation automatique du client (page d’accueil WFM)

Si vous utilisez les paramètres de navigateur ci-dessus, le client s’installe automatiquement lorsque vous accédez à WFM.

1. Accédez à _WFM_{:.menu-item}.
2. Attendez que le téléchargement soit terminé et que l’installation du client commence.
3. Le navigateur affiche le message&nbsp;: Cette page Web souhaite exécuter le module complémentaire suivant&nbsp;: 'injixo Enterprise' de 'InVision AG'.<br>Si l’invite n’apparaît pas, demandez de l’aide au service informatique de votre entreprise.
4. Cliquez sur _Installer_{:.doc-button} pour installer les modules complémentaires nécessaires.
5. Cliquez sur _Installer_{:.doc-button} pour installer le client.

Une fois l’installation réussie, vous pourrez accéder aux composants ActiveX.

### Installation manuelle du client

Installez le client manuellement, par exemple dans injixo WFM Enterprise on-premise ou lorsque l’installation automatique ne fonctionne pas.

Remarque&nbsp;: si vous utilisez un outil de distribution de logiciels, exécutez le programme d’installation pour l’utilisateur qui se connectera à l’ordinateur, par exemple en utilisant msiexec.exe de Microsoft avec l’option runas /user.

1. Téléchargez le [client injixo le plus récent](https://downloads.injixo.com/en#client-components).
2. Pour exécuter le programme d’installation MSI, cliquez sur _Exécuter_{:.doc-button}.
3. Pour continuer, cliquez sur _Suivant_{:.doc-button}.
4. (Facultatif) Modifiez le chemin d’installation.
5. Si l’ordinateur est partagé par plusieurs utilisateurs, sélectionnez **Tout le monde**.
6. Pour continuer, cliquez sur _Suivant_{:.doc-button}.
7. Pour démarrer l’installation, cliquez sur _Installer_{:.doc-button}.
   Le message suivant apparaît&nbsp;: Voulez-vous autoriser le programme suivant provenant d’un éditeur inconnu à apporter des modifications à cet ordinateur&nbsp;?
8. Cliquez sur _Oui_{:.doc-button} pour confirmer.

Une fois l’installation réussie, vous pourrez accéder aux composants ActiveX.
