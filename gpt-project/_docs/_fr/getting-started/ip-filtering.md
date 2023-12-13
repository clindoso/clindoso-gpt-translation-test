---
title: Filtrage IP
product_label:
  - enterprise
  - advanced
description: Apprenez à configurer le filtrage IP pour votre tenant injixo.
toc: true
---

Le filtrage IP est une fonctionnalité payante. Il n’est pas inclus dans votre offre WFM Enterprise ou Advanced par défaut.
Si vous souhaitez l’ajouter à votre organisation, veuillez contacter votre consultant.

Le filtrage IP permet de garantir que vos utilisateurs accèdent à votre tenant injixo uniquement depuis des plages d’adresses IP spécifiques. Les utilisateurs se connectant depuis d’autres adresses IP ne pourront pas accéder à injixo. injixo propose une [liste de contrôle d’accès](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) (ACL réseau). Activez l’ACL réseau si vous souhaitez autoriser l’accès à injixo depuis les réseaux sélectionnés uniquement (par exemple, le réseau de votre organisation).

## Activer le filtrage IP

Seuls les utilisateurs disposant d’un accès admin peuvent activer le filtrage IP.

> Remarque
> 
> Lorsque vous activez le filtrage IP, tous les utilisateurs actifs sont déconnectés. Le cadre temporel varie selon le produit&nbsp;:
> - La déconnexion peut être immédiate.
> - La déconnexion se produit lors du chargement ou du stockage suivant des données.
> - La déconnexion est programmée (uniquement dans le Centre de planification, accessible via _Plan > Centre de planification_{:.breadcrumbs}).
> 
> Pour continuer à travailler dans injixo, les utilisateurs devront se reconnecter.

1. Accédez à _Account > Sécurité_{:.breadcrumbs} et sélectionnez l’onglet **Filtrage IP**.
2. Dans les champs **Plage d’adresses IP**, saisissez les plages d’adresses IP au [format CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#:~:text=CIDR%20notation%20specifies%20an%20IP,bits). Vous pouvez ajouter jusqu’à trois plages d’adresses IP.
3. Cliquez sur _Activer le filtrage_{:.doc-button}.

Le filtrage IP affecte uniquement les interactions avec l’interface utilisateur. Actuellement, le Centre de planification disponible par URL directe (facultatif) n’est pas affecté par le filtrage IP.
 
## Modifier les plages d’adresses IP

> Remarque
> 
> Si vous modifiez les plages d’adresses IP, tous les utilisateurs seront déconnectés lors de leur prochain accès à injixo. Pour continuer à travailler dans injixo, les utilisateurs devront se reconnecter.

1. Accédez à _Account > Sécurité_{:.breadcrumbs} et faites défiler jusqu'à la section **Filtrage IP**.
2. Modifiez les plages d’adresses IP.
3. Cliquez sur _Enregistrer_{:.doc-button}.

## Désactiver le filtrage IP

1. Accédez à _Account > Sécurité_{:.breadcrumbs} et faites défiler jusqu'à la section **Filtrage IP**.
2. Modifiez les plages d’adresses IP.
3. Cliquez sur _Désactiver le filtrage_{:.doc-button}.

Une fois le filtrage IP désactivé, les utilisateurs pourront accéder à injixo depuis n’importe quelle adresse IP.

> Remarque
> 
> Si vous désactivez le filtrage IP, tous les utilisateurs seront déconnectés. Pour continuer à travailler dans injixo, les utilisateurs devront se reconnecter.
