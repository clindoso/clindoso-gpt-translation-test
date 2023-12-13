---
title: Gérer les employés
product_label:
  - advanced
  - enterprise
description: Découvrez comment créer, voir, modifier et supprimer les profils des employés.
beta-feature: true
redirect_from: /fr/people-overview/
redirect_reason: Renamed from /people-overview/ to /manage-people/ in Jan 2023
---

People vous permet de gérer les données les plus importantes des employés de votre organisation&nbsp;:

- créer, modifier et supprimer les profils personnels,
- envoyer une invitation injixo à un nouvel employé (e-mail de bienvenue),
- accéder aux paramètres du compte utilisateur d’un employé,
- accéder aux données de configuration d’un employé dans WFM.

> Les utilisateurs disposant d’un accès admin peuvent accéder à People par défaut.
>
> Pour {% link_new accorder des droits sur People à d’autres utilisateurs | getting-started/configure-user-roles.md %}, accédez à _Account > Rôle utilisateur_{:.breadcrumbs}.

## Créer un nouvel employé

1. Accédez à _People_{:.breadcrumbs}.
2. Cliquez sur _\+ Nouvel employé_{:.doc-button}.
3. Dans **Informations générales**, saisissez les informations obligatoires pour l’employé&nbsp;:
   - **Nom** et **prénom**, et **deuxième prénom** (facultatif). 
   - **Matricule**&nbsp;: identifiant unique de l’employé de votre organisation.
   - **E-mail (identifiant injixo)**&nbsp;: saisissez l’adresse e-mail utilisée par l’employé pour se connecter à injixo.
4. Pour inviter l’employé à se connecter à injixo, cochez la case **Envoyer l’e-mail de bienvenue**.  
   Vous ne pouvez envoyer l’e-mail de bienvenue que lors de la création d’un employé. L’e-mail contient des instructions pour la création du mot de passe et un lien vers la page de connexion à injixo.
5. (Facultatif) Dans **Informations supplémentaires**, vous pouvez ajouter des informations facultatives sur l’employé, comme son état civil ou d’autres informations de contact.
Le contenu du champ Civilité n’est utilisé nulle part dans injixo. Vous pouvez utiliser le contenu de ce champ pour vous adresser aux employés, par exemple lorsque vous leur envoyez des newsletters.
6. Cliquez sur _Créer un employé_{:.doc-button}.  
   Si vous avez coché la case **Envoyer l’e-mail de bienvenue**, injixo enverra l’e-mail de bienvenue à l’employé.

## Inviter un employé à se connecter à injixo

Vous pouvez uniquement {% link_new inviter un employé à se connecter à injixo via l’e-mail de bienvenue | features/people/manage-people.md | #créer-un-nouvel-employé %} lorsque vous créez un nouvel employé.

## Voir ou modifier le profil d’un employé

1. Accédez à _People_{:.breadcrumbs}.
2. (Facultatif) Pour rechercher un employé, utilisez le champ **Rechercher**.
3. Cliquez sur le nom d’un employé dans la liste.  
   Les informations sur cet employé s’affichent à droite. Pour masquer les informations, cliquez sur _Annuler_{:.doc-button} ou appuyez sur la touche **Esc** de votre clavier.
4. Modifiez les informations de l’employé.

   > Remarque
   >
   > Si vous modifiez son adresse e-mail, l’employé ne pourra plus se connecter à injixo avec son adresse e-mail précédente. Assurez-vous de communiquer la nouvelle adresse e-mail à l’employé. injixo ne l’informera pas de ce changement.

5. Cliquez sur _Enregistrer les modifications_{:.doc-button}.

## Supprimer le profil d’un employé

> Attention
>
> Une fois le profil d’un employé supprimé, vous ne pourrez plus le réactiver. Il sera supprimé de tous les plannings actuels et futurs. La suppression du profil d’un employé n’impacte pas les données historiques d’adhérence dans {% link_new Intraday | features/intraday/adherence-intraday.md %}.

1. Accédez à _People_{:.breadcrumbs}.
2. Cliquez sur le nom d’un employé dans la liste.  
   Les informations de l’employé s’affichent.
3. Cliquez sur _Supprimer l’employé_{:.doc-button}.
4. Dans la fenêtre de confirmation, cliquez sur _Supprimer l’employé_{:.doc-button}.

Pour que votre planning reste à jour après avoir supprimé le profil d’un employé, lancez l’optimisation des activités.
