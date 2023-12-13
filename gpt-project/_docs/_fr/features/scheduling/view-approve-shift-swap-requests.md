---
title: Voir et valider les demandes d’échanges
product_label:
  - essential
  - advanced
  - enterprise
description: Voir et valider/refuser les demandes d’échanges de journées en attente et les échanges passés.
archive_ref: 20210802-en-shift-exchange-overview
redirect_from:
  - /fr/shift-exchange-overview/
redirect_reason: Updated filename on 19 April 2023
---

Dans injixo Me, les utilisateurs avec le rôle agent peuvent {% link_new échanger leurs journées | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #échanger-des-journées %} ou congés entre eux, le même jour ou sur des jours différents.

Voici comment fonctionne la bourse d’échanges&nbsp;:

1. Une personne propose un échange de journée dans injixo Me.
2. Les autres personnes peuvent voir la journée proposée et offrir leur journée en échange.
3. La personne qui propose sa journée choisit la contre-proposition qui convient le mieux à ses besoins. 
4. injixo confirme la sélection et crée la demande de validation si nécessaire.
5. Un utilisateur avec le rôle planificateur vérifie, valide ou refuse la demande d’échange. Pour permettre la validation automatique, configurez le paramètre _48152_{:.id-label} _Mode de déroulement des échanges de plannings_ sur la valeur 1.

Pour découvrir comment les membres de votre équipe peuvent utiliser injixo, lisez l’article sur la {% link_new bourse d'échange | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #échanger-des-journées %}.

Conseil&nbsp;: dans le {% link_new Calendrier de l’équipe | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %}, les personnes peuvent voir les horaires de leurs collègues et demander des échanges dans la bourse d’échanges.

## Prérequis

Les personnes avec le rôle agent peuvent proposer une journée, si les conditions suivantes sont remplies&nbsp;:

- L’option {% link_new Bourse d’échanges | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} est activée dans la configuration d’injixo Me.
- L’option {% link_new Bourse d’échanges | features/administration/activity-types-and-properties.md %} est activée pour toutes les activités de la journée.
- Une {% link_new période de planification | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} existe avec le statut Missions disponibles, Publiée ou Clôturée.
- La Date limite paramétrée pour l’unité opérationnelle n’a pas encore été atteinte.
- La valeur du paramètre _48151_{:.id-label} autorise l’utilisation de la bourse d’échanges. La valeur du paramètre définit la date de démarrage possible pour les échanges à compter de la date actuelle, pour éviter de créer des conflits avec le planning actuel.
- Ces personnes ont accès en lecture à injixo Me.

## Valider ou refuser des échanges

Pour vérifier, valider ou refuser les demandes d’échange de journées dans _Plan > Schedules_{:.breadcrumbs}, suivez les étapes ci-dessous&nbsp;:

1. Cliquez sur _Actions de planification_{:.doc-button}.
2. Sélectionnez **Gérer les échanges de planning**.
3. Sélectionnez une **unité opérationnelle**.
4. (Facultatif) Sélectionnez un **Groupe**.
5. Sélectionnez une **Plage de dates**. Si vous n’avez pas encore sélectionné de plage de dates dans Schedules, la plage de dates sélectionnée par défaut est la date actuelle + sept jours.
6. Cochez les **cases** en face des entrées que vous souhaitez valider ou refuser. Utilisez la première case de la liste pour sélectionner toutes les demandes.
7. Cliquez sur _Accepter la sélection_{:.doc-button} ou _Refuser la sélection_{:.doc-button}.  
   Une fois les demandes en attente validées ou refusées, elles seront déplacées vers l’onglet Information.

Le rapport Statistiques des échanges dans _WFM > Supervision > Reports_{:.breadcrumbs} contient une liste des statuts des échanges (Offres, Échanges en attente, Refus, Échanges validés) sur une période personnalisable.

## Créer une liste des échanges passés

Sur la page **Gérer les échanges de planning**, l’onglet Information indique quelle personne a échangé sa journée et à quelle heure. La liste montre les demandes validées, refusées ou annulées. Pour plus d’informations sur les demandes annulées, faites passer votre curseur sur l’{% icon info_circle %}.

## Paramètres de la bourse d’échanges

Dans _WFM > Administration > Système > Configuration_{:.breadcrumbs}, plusieurs paramètres sont disponibles pour adapter le processus d’échange de planning aux besoins de votre organisation&nbsp;:

- _48151_{:.id-label} _Date pour le blocage des échanges dans la Bourse d'échanges_&nbsp;: nombre de jours à partir de la date en cours pendant lesquels un échange de planning ne peut avoir lieu (par exemple&nbsp;: 3 jours),
- _48152_{:.id-label} _Mode de déroulement des échanges de planning_&nbsp;: permet de déterminer si un utilisateur disposant de droits admin ou du rôle planificateur doit valider les échanges de planning (la valeur par défaut est de 0, la valeur 1 active la validation automatique des échanges),
- _48153_{:.id-label} _Déterminer les employés habilités à échanger leurs plannings_&nbsp;: autorise les personnes d’une unité opérationnelle (valeur par défaut, 0), d’un groupe (valeur 1) ou de différentes unités opérationnelles (valeur 2, non recommandé) à échanger leurs plannings,
- _48555_{:.id-label} _Autoriser les échanges de jours planifiés avec des jours libres_&nbsp;: autorise les personnes à échanger des journées contre des congés (valeur par défaut&nbsp:0, non),
- _48556_{:.id-label} _Autoriser les échanges pour des dates non concordantes_&nbsp;: autorise les personnes à échanger des journées sur différents jours de la semaine (valeur par défaut&nbsp;: 0, non),
- _48999_{:.id-label} _Activer des contrôles spécifiques pour les sous-activités de multiactivités en association avec la règle de planification 2605_&nbsp;: injixo vérifie les compétences pour chaque sous-activité lors de l’échange de multi-activités (valeur par défaut&nbsp;: 0, pas de vérification). 

## Pourquoi les échanges de planning sont-ils bloqués&nbsp;?

Les membres de votre équipe peuvent voir les échanges offerts dans injixo Me si les demandes sont conformes aux règles de leur contrat (heures de travail contractuelles) et s’ils disposent des compétences nécessaires.

Pour savoir pourquoi l’échange est bloqué dans injixo Me, simulez l’échange dans le _Centre de planification_{:.menu-item}. Lorsque vous copiez et collez les journées, la {% link_new fenêtre | features/scheduling/shiftcenter/shift-center-overview.md | #message-window %} en bas de l’écran affichera la {% link_new règle de planification | features/administration/create-contracts.md %} et le motif d’erreur. Par exemple, l’absence de compétences ou autres contraintes contractuelles.
