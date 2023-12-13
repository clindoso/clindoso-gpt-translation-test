---
title: Gestion des heures supplémentaires
product_label:
  - advanced
  - enterprise
  - classic
description: Découvrez comment configurer les activités de manière optimale pour planifier les heures supplémentaires et les documenter de manière transparente.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

Les employés ont parfois besoin d’effectuer des heures supplémentaires pour maintenir un niveau de service raisonnable. Les heures supplémentaires sont parfois nécessaires en raison d’une augmentation inattendue de la charge de travail, d’une situation de sous-effectif causée par des taux d’absence élevés dus à une maladie ou aux congés.  
Dans de nombreux cas, les contrats de vos employés stipulent que les heures supplémentaires sont payées à des taux plus élevés, ou que toute heure supplémentaire travaillée doit être compensée sous forme de congé supplémentaire. Il est également important de respecter les autres contraintes contractuelles, telles que le temps de repos entre les journées lorsque les personnes effectuent des heures supplémentaires. Si vous êtes un fournisseur de services, vous pouvez également être obligé d’informer les clients de tout travail supplémentaire planifié. 

Dans cet article, vous trouverez des conseils sur la configuration des activités et des multi-activités pour planifier facilement les heures supplémentaires et les afficher correctement dans le panneau des activités et vos rapports.

Les heures supplémentaires doivent être planifiées manuellement dans le Centre de planification ou Schedules en complément du planning existant.

## Créer des activités pour les heures supplémentaires

L'exemple ci-dessous utilise une nouvelle activité nommée Appels. Suivez ces étapes pour toutes les activités que vous souhaitez pouvoir planifier comme heures supplémentaires, c'est-à-dire pour les appels ou les e-mails, mais pas pour les congés maladie ou les congés.

1. {% link_new Créez et configurez l'activité | features/administration/activities.md %} **Appels**. 
2. Dupliquez l'activité **Appels** et nommez la nouvelle activité **Appels - heures supplémentaires**. Vous n’avez pas besoin d’ajouter de compétences à cette activité.  
  - Cochez la case **Traitement spécial pour la planification optimisée**.
  - Assurez-vous que la case **Autoriser les demandes dans Me** n'est pas cochée.
3. Dans **Appels - heures supplémentaires**, ajoutez **Appels** comme sous-activité.  
  **Appels - heures supplémentaires** est maintenant une multi-activité.
4. Ajoutez les deux activités à l'unité opérationnelle concernée. N’ajoutez pas l’activité pour les heures supplémentaires à un modèle horaire.

Avec cette configuration, l'activité Appels - heures supplémentaires ne peut être planifiée que manuellement et ne peut pas être remplacée lors de l'optimisation du planning. Les employés ne pourront pas demander cette activité dans injixo Me.

En ajoutant «&nbsp;heures supplémentaires&nbsp;» au nom de la multi-activité, vous et vos employés pouvez clairement voir les heures supplémentaires, leur durée et leurs tâches dans leur planning.

## Planifier les heures supplémentaires

Vous pouvez planifier manuellement les heures supplémentaires dans _Plan > Centre de planification_{:.breadcrumbs} ou dans _Plan > Schedules_{:.breadcrumbs}.

Pour ajouter des activités supplémentaires dans le Centre de planification, suivez ces étapes&nbsp;:

1. Choisissez l'unité opérationnelle et le groupe (facultatif) auxquels appartient l’employé pour lequel vous souhaitez planifier les heures supplémentaires.
2. Double-cliquez sur le jour pour lequel cet employé doit effectuer des heures supplémentaires. Cliquez sur l'onglet **Multiactivités** et sélectionnez **Appels - heures supplémentaires**.
3. Définissez une heure de début et de fin pour l'activité.
4. Cliquez sur _OK_{:.doc-button}.

Les heures supplémentaires planifiées sont immédiatement reflétées dans la fenêtre de planification et sur l'onglet Activités dans la {% link_new fenêtre des paramètres | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %}. Si vous configurez l’onglet Activités pour afficher la couverture, le panneau des activités se mettra à jour et reflétera les heures supplémentaires planifiées.

Pour ajouter des activités supplémentaires dans _Plan > Schedules_{:.breadcrumbs}, suivez ces étapes&nbsp;:

1. Double-cliquez sur une cellule du planning pour ouvrir la vue d’édition.
2. Cliquez sur _Insérer une nouvelle activité_{:.doc-button}.  
  Une nouvelle ligne avec l'activité est ajoutée à droite.
3. Dans la nouvelle ligne, sélectionnez **Appels - heures supplémentaires** dans le menu déroulant.
4. Définissez une heure de début et de fin pour l'activité.
5. Cliquez sur _Sauvegarder_{:.doc-button}.

## Rapports

Le rapport **Activités en heures...** affiche les heures supplémentaires effectuées par l’employé, grâce au nom de l’activité incluant cette information. Ainsi, toutes les heures supplémentaires effectuées sont documentées et peuvent être consultées par toutes les personnes concernées, par exemple le service financier qui doit gérer la rémunération supplémentaire.
