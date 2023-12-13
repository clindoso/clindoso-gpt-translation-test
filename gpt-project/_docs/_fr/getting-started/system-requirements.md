---
title: Prérequis techniques
description: Navigateur et configuration pris en charge pour les intégrations, les agents et les postes de travail des planificateurs.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

injixo est une solution SaaS de Workforce management (WFM) sur navigateur, disponible en plusieurs [offres WFM](https://www.injixo.com/fr/pricing)&nbsp;: injixo Essential WFM, injixo Advanced WFM et injixo Enterprise WFM.

## Navigateurs compatibles

injixo est compatible avec les deux dernières versions des navigateurs suivants&nbsp;:

- Microsoft Edge
- Google Chrome
- Mozilla Firefox
- Apple Safari

## Bloqueur de fenêtres contextuelles

injixo utilise des fenêtres contextuelles pour afficher des fenêtres de dialogue supplémentaires. Pour autoriser les fenêtres contextuelles pour injixo, suivez ces étapes&nbsp;:

- Désactivez le bloqueur de fenêtres contextuelles dans [Microsoft Edge](https://support.microsoft.com/fr-fr/microsoft-edge/bloquer-les-fen%C3%AAtres-contextuelles-dans-microsoft-edge-1d8ba4f8-f385-9a0b-e944-aa47339b6bb5).
- Définissez une exception pour le bloqueur de fenêtres pop-up dans [Google Chrome](https://support.google.com/chrome/answer/95472?hl=fr&co=GENIE.Platform%3DDesktop#zippy=%2Callow-pop-ups-and-redirects-from-a-site), [Mozilla Firefox](https://support.mozilla.org/fr/kb/parametres-exceptions-depannage-blocage-popup) et [Apple Safari](https://support.apple.com/fr-fr/guide/safari/sfri40696/mac).

## Microsoft Edge en mode de compatibilité Internet Explorer (IE)

Les fonctionnalités avec des composants ActiveX dans WFM nécessitent {% link_new Microsoft Edge avec le mode Internet Explorer | support/faq/configure-edge-internet-explorer-mode.md %}. Pour configurer le mode Internet Explorer, vous avez besoin d'un [fichier XML de liste de sites](https://learn.microsoft.com/fr-fr/deployedge/edge-ie-mode-local-site-list).

<style>
table {
  width: 100%;
}
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

| Offre WFM                               | Mode IE requis dans Microsoft Edge         |
| -------------------------------------- | ------------------------------------------ |
| Essential WFM                          | Non                                         |
| Advanced WFM                           | Non                                         |
| Enterprise WFM                         | Uniquement pour les fonctionnalités personnalisées            |
| Classic <sup>1</sup>                   | Oui                                        |
| Enterprise WFM on-premise <sup>1</sup> | Oui. S’il n’est pas configuré, vous ne pourrez pas vous connecter. |

<sup>1</sup> Versions plus anciennes (anciennes offres WFM toujours utilisés actuellement)

Si vous utilisez un navigateur non compatible ou si votre configuration du mode IE est incorrecte, le symbole IE dans le menu de navigation WFM permet d’identifier les fonctionnalités qui nécessitent ce mode (Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} fonctionne avec n’importe quel navigateur indiqué, sur les ordinateurs, les smartphones et les tablettes.

## Client injixo

Les fonctionnalités avec des composants ActiveX dans WFM nécessitent l’installation du {% link_new client injixo | getting-started/browser-setup.md %}.

Vous trouverez la configuration requise du système d’exploitation dans la description du client sur [downloads.injixo.com](https://downloads.injixo.com/fr).

| Offre WFM                      | Client injixo requis                |
| ------------------------- | ----------------------------------------- |
| Essential WFM             | Non                                        |
| Advanced WFM              | Non                                        |
| Enterprise WFM            | Uniquement pour les fonctionnalités personnalisées           |
| Classic                   | Oui                                       |
| Enterprise WFM on-premise | Oui. S’il n’est pas installé, vous ne pourrez pas vous connecter. |

Si le client n’est pas installé, les symboles IE dans le menu de navigation de gauche indiquent les fonctionnalités qui nécessitent le mode IE (Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} ne nécessite pas le client injixo.

## Exceptions du pare-feu

Pour accéder aux page web d’injixo, autorisez le trafic Web vers et depuis *.injixo.com via le port 443.

Si vous utilisez des fonctionnalités avec des composants ActiveX, ajoutez une autre exception au pare-feu. Ces applications utilisent le port 45054 pour le trafic sortant (port 80 pour les environnements injixo avant 2019) et nécessite un accès direct à Internet par TCP (Transmission Control Protocol). Les serveurs proxy configurés dans le navigateur ne sont pas pris en charge.

Pour obtenir l’adresse de l’exception du pare-feu, cliquez sur _WFM_{:.menu-item} et utilisez le nom de votre environnement injixo visible dans la barre d’adresse du navigateur, par exemple wfm-123abc.injixo.com&nbsp;:

Pour en savoir plus sur les exceptions de pare-feu dans Windows, consultez la [documentation Microsoft](https://support.microsoft.com/fr-fr/windows/ajouter-une-exclusion-%C3%A0-s%C3%A9curit%C3%A9-windows-811816c0-4dfd-af4a-47e4-c301afe13b26#:~:text=Go%20to%20Start%20%3E%20Settings%20%3E%20Update,%2C%20file%20types%2C%20or%20process).

### URL de partage pour WebSockets

Pour envoyer des mises à jour en temps réel aux utilisateurs, par exemple dans le {% link_new Centre de planification | features/scheduling/shiftcenter/shift-center-overview.md %} ou pour l’adhérence en temps réel, les fonctionnalités utilisent le protocole WebSocket (basé sur TCP) sur le port 443\. injixo ouvre une page Web qui établit une connexion WebSocket. Ajoutez les URL suivantes à la liste d’URL autorisées&nbsp;:

- https://shiftcenter.injixo.com
- wss://shiftcenter.injixo.com
- https://www.injixo.com
- wss://ws.injixo.com

Pour les offres injixo Advanced et injixo Enterprise WFM, le Centre de planification utilise WebSockets pour fonctionner à vitesse maximale. La technologie intégrée propose un mécanisme de secours plus lent si les WebSockets ne sont pas disponibles. Les autres fonctionnalités d’injixo ne proposent aucun mécanisme de secours.

## Bande passante réseau requise

injixo est conçu et optimisé pour être performant tout en utilisant une faible quantité de ressources. Lors du premier accès, les graphismes sont téléchargés et stockés localement dans des fichiers temporaires. Ensuite, seules les informations de base sont transférées, de manière sécurisée, vers le poste de travail.

Un centre de contact de 200 postes peut prévoir un transfert de données d’environ 25 à 50 Mo par heure lorsque tous les utilisateurs sont connectés.

## Exigences relatives à l’intégration

Configurez des {% link_new intégrations | features/acd-integration/cloud/how-integrations-work.md %} pour permettre à injixo d’importer des données historiques de contact et les statuts agents de vos systèmes externes, comme votre système de téléphonie (ACD) ou votre outil de gestion clients (CRM).
injixo prend en charge une large gamme d'intégrations cloud et on-premise.

Installez {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} pour importer régulièrement des données à partir d'intégrations on-premise et par fichier CSV.

Les requêtes de données n’interfèrent pas avec les fonctions principales des outils de communication, telles que la téléphonie ou les plateformes e-mail.

Les demandes d’informations en temps réel sur le statut agent peuvent utiliser des flux de socket directs. Ces flux transmettent uniquement les changements d’activité des agents (y compris la date et l’heure, un identifiant agent et un code de statut) et sont d’environ 1&nbsp;Ko chacun.

## Dispositions relatives aux data centers et à la sécurité

injixo opère à partir de centres de données dans l’infrastructure Amazon EC2. [Les politiques de sécurité d’Amazon](https://aws.amazon.com/fr/security/?nc1=h_ls) s’appliquent donc à injixo, par exemple SOC 1 Type 2, ISO 27001 et PCI DSS Level 1.

Toutes les données sont stockées dans l’UE (pour les clients européens) et aux États-Unis (pour les clients basés aux États-Unis). injixo est donc conforme à toutes les lois relatives à la protection des données, y compris le RGPD en Europe. En savoir plus sur [la sécurité et la conformité du Cloud d’injixo](https://www.injixo.com/fr/security/).
