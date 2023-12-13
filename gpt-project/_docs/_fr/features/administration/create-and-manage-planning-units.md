---
title: Créer et gérer les unités opérationnelles
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Découvrez comment créer, configurer et supprimer les unités de planification.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-use-virtual-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
redirect_from:
  - /fr/planning-unit-configuration/
  - /fr/unites-operationnelles/
redirect_reason: Updated filename on 21 August 2023
---

Les unités opérationnelles regroupent les employés et les données de configuration à des fins de planification. Vos sites physiques ne correspondent pas nécessairement à vos unités opérationnelles. Par exemple, des employés travaillant à deux endroits différents peuvent être {% link_new affectés | features/administration/employee-overview.md | #configurer-les-paramètres-employés %} à une même unité opérationnelle. Nous recommandons d’utiliser une seule unité opérationnelle, sauf si&nbsp;:

- les employés travaillent sur des fuseaux horaires différents. Dans ce cas, utilisez une unité opérationnelle par fuseau horaire.
- les planificateurs de votre entreprise sont responsables de différents groupes d’employés, par exemple en fonction des différents services.

injixo Advanced et Enterprise WFM proposent des rôles utilisateur personnalisés pour restreindre l’accès des utilisateurs à différentes unités opérationnelles.

Si vous travaillez avec plusieurs unités opérationnelles, vous pouvez temporairement changer l’affectation d’un employé d’une unité opérationnelle à une autre. En savoir plus sur la {% link_new mutation temporaire des employés | features/administration/employee-overview.md | #muter-temporairement-des-employés %}.

## Créer une unité opérationnelle

1. Accédez à _Plan > Configuration > Unités opérationnelles_{:.breadcrumbs}.
2. Cliquez sur l’icône Créer {% icon item-add | icon-only %} en haut à gauche.  
   Un panneau de configuration s’ouvre à droite.
3. Remplissez les champs suivants&nbsp;:

   - **Nom**&nbsp;: nom unique pour l’unité opérationnelle (max. 50 caractères).
   - **Abréviation**&nbsp;: abréviation du nom (max. 25 caractères).
   - **Couleur**&nbsp;: couleur facultative pour l’unité opérationnelle. Vous verrez la couleur dans Schedules.
   - **Intervalle**&nbsp;: influence le niveau de détail avec lequel les données, par exemple la couverture et le besoin en personnel, sont affichées dans Schedules. L’intervalle de l’unité opérationnelle ne doit pas être plus long que l’intervalle de vos importations de données de contact et de statut agent. Le menu déroulant affiche les intervalles de l’unité opérationnelle en minutes. Nous recommandons d’utiliser un intervalle de **15 minutes**. L’intervalle ne peut plus être changé après avoir été sauvegardé. En savoir plus sur l’{% link_new import de données à l’aide d’intégrations | features/acd-integration/cloud/how-integrations-work.md %}.
   - **Unité opérationnelle supérieure**&nbsp;: unité opérationnelle facultative contenant l’unité opérationnelle que vous créez. En savoir plus sur les {% link_new unités opérationnelles de niveau supérieur | best-practices/how-to-use-virtual-planning-units.md %}.
   - **Fuseau horaire**&nbsp;: fuseau horaire de l’unité opérationnelle. Le fuseau horaire ne peut pas être modifié après avoir sauvegardé l’unité opérationnelle. En savoir plus sur les {% link_new fuseaux horaires | best-practices/working-with-timezones.md %}.

     > Remarque
     >
     > Le fuseau horaire sélectionné doit correspondre au fuseau horaire de vos workloads dans Forecast. Sinon, vous pouvez transférer le besoin en personnel pour la planification. Une intégration ajustera les données importées en fonction du fuseau horaire de vos workloads.

4. Cliquez sur _OK_{:.doc-button}.  
   Vous pouvez désormais ajouter des horaires d’ouverture, des activités ou {% link_new limiter les modèles horaires | features/administration/create-and-manage-planning-units.md | #limiter-les-modèles-horaires %}.

### Ajouter des horaires d’ouverture

Pour ajouter des horaires d’ouverture à une unité opérationnelle, vous devez d’abord créer l’{% link_new unité opérationnelle | features/administration/create-and-manage-planning-units.md | #créer-une-unité-opérationnelle %}.

Pour la planification, vous devez ajouter des heures d’ouverture à votre unité opérationnelle. Les heures d’ouverture limitent les heures quotidiennes pendant lesquelles vous pouvez {% link_new calculer le besoin en personnel | features/forecast/injixo-forecast/staff-requirement.md %} et {% link_new optimiser le planning | features/scheduling/schedules/schedules-optimized-schedules.md %}. <!-- special public holiday day types or part of the linked article? -->

1. Dans la section **Horaires d’ouverture** du panneau de configuration de l’unité opérationnelle, cliquez sur l’{% icon item-add %} pour ajouter les horaires d’ouverture pour certains types de jours.  
   Une fenêtre s’ouvre.
2. Dans la section **Types de jours**, sélectionnez un ou plusieurs {% link_new types de jours | features/administration/day-types.md %}.
3. Entrez l’heure de début et de fin dans les champs **De** et **À** (format 24 heures). Si votre centre de contacts est ouvert 24&nbsp;heures sur 24, entrez 00:00 dans les deux champs.
4. (Facultatif) Dans les champs **Valide du** et **Jusqu’au**, entrez une plage de dates à laquelle s’appliquent les horaires d’ouverture du centre de contacts. Si les horaires d’ouverture s’appliquent toujours, laissez les champs vides. En savoir plus sur les {% link_new périodes de validité | features/administration/set-a-validity-period.md %}.
5. Cliquez sur _OK_{:.doc-button}.

Pour modifier ou supprimer les horaires d’ouverture, cliquez sur l’{% icon item-edit %} ou l’{% icon item-delete %}.

### Ajouter des activités

Pour ajouter des activités à une unité opérationnelle, vous devez d’abord créer l’{% link_new unité opérationnelle | features/administration/create-and-manage-planning-units.md | #créer-une-unité-opérationnelle %}.

Pour créer un planning, vous devez ajouter des activités aux unités de planification. Vous ne pouvez planifier des employés que pour les activités ajoutées à l’unité opérationnelle. Par défaut, toutes les unités de planification incluent l’activité Présent. Vous ne pouvez pas supprimer l’activité Présent.

Pour ajouter des activités à une unité opérationnelle, procédez comme suit&nbsp;:

1. Dans la section **Activités** du panneau de configuration de l’unité opérationnelle, cliquez sur l’{% icon item-add %}.  
   Une fenêtre s’ouvre.
2. Cliquez sur l’activité que vous souhaitez ajouter.
3. (Facultatif) Entrez une plage horaire dans les champs **De** et **À**. La fonctionnalité {% link_new Optimiser le planning | features/scheduling/schedules/schedules-optimized-schedules.md %} prendra en compte cette activité dans la plage horaire que vous avez saisie. Lorsque les deux champs ont la valeur 00:00, injixo prend en compte les horaires d’ouverture de l’unité opérationnelle. Les utilisateurs ayant un accès administrateur peuvent modifier ce comportement par défaut dans le paramètre _48408_{:.id-label} _Sélection des horaires d’ouverture à respecter_.
4. (Facultatif) Entrez une heure dans les champs **Valide du** et **Jusqu’au** pour limiter la disponibilité de l’activité dans la création du planning. Laissez les champs **Valide du** et **Jusqu’au** vides pour la rendre toujours valide.
5. Cliquez sur _OK_{:.doc-button}.

Pour modifier ou supprimer une activité, cliquez sur l’{% icon item-edit %} ou sur l’{% icon item-delete %} .

### Ajouter des multi-activités

Pour ajouter une {% link_new multi-activité | features/administration/activity-types-and-properties.md | #sous-activités %} à une unité opérationnelle, vous devez d’abord ajouter toutes les sous-activités respectives. Dans la liste des activités, la multi-activité est marquée en gras. Les multi-activités ne sont pas disponibles dans injixo Essential WFM.

### Limiter les modèles horaires

Par défaut, tous les {% link_new modèles horaires | features/administration/daymodels/daymodel-creation.md %} sont assignés à votre unité opérationnelle. Si vous n’utilisez pas tous les modèles horaires dans une unité opérationnelle, vous pouvez limiter le nombre de modèles horaires pour cette unité opérationnelle.

La limitation des modèles horaires peut accélérer la planification avec la fonctionnalité Optimiser le planning. Cependant, vous ne pouvez utiliser que les modèles horaires restants pour générer des journées, créer des rapports ou créer des plannings optimisés. Cela peut nécessiter un effort plus important pour maintenir les autres données de configuration, par exemple les modèles hebdomadaires. Supprimer un modèle horaire en cours d’utilisation n’affecte pas les horaires et les journées créés avec ce modèle horaire.

> Remarque
> 
> Si vous supprimez tous les modèles horaires dans l’unité opérationnelle, vous ne pourrez planifier les journées qu’en ajoutant manuellement des activités au planning ou en {% link_new insérant des activités dans les rotations d’horaires | features/administration/shift-sequences.md %}. Toutes les autres approches de planification, par exemple l’utilisation de la fonctionnalité Optimiser le planning ou les modèles de planification, ne fonctionneront pas.

Pour limiter le nombre de modèles horaires, procédez comme suit&nbsp;:

1. Accédez à _Plan > Configuration > Unités opérationnelles_{:.breadcrumbs}.
2. Sélectionnez l’unité opérationnelle que vous souhaitez modifier et faites défiler vers le bas jusqu’à la section **Modèles horaires**.
3. Cliquez sur l’{% icon item-edit %} à côté de l’option de configuration par défaut **[Tous]** et sélectionnez un modèle horaire. Vous pouvez également cliquer sur l’{% icon item-delete %} pour supprimer l’option **[Tous]**. Pour limiter le nombre de modèles horaires, vous devez soit remplacer, soit supprimer l’option **[Tous]**. Vous ne pouvez pas ajouter des modèles horaires à une unité opérationnelle plus d’une fois.  
   Ignorez l’étape 3 si vous souhaitez attribuer à l’unité opérationnelle d’autres modèles horaires ultérieurement.
4. Cliquez sur l’{% icon item-add %} pour attribuer un ou plusieurs modèles horaires.
5. Cliquez sur _OK_{:.doc-button}.

Pour modifier ou supprimer un modèle horaire, cliquez sur l’{% icon item-edit %} ou sur l’{% icon item-delete %} .

## Supprimer des unités opérationnelles

> Attention
> 
> Si vous supprimez une unité opérationnelle, les plannings correspondants sont également supprimés.

1. Accédez à _Plan > Configuration > Unités opérationnelles_{:.breadcrumbs}.
2. Dans la liste, cliquez sur l’unité opérationnelle que vous souhaitez supprimer.
3. Pour vous assurer que les données de planification sont toujours affichées correctement, supprimez les activités et retirez les modèles horaires assignés de l’unité opérationnelle avant de la supprimer.
4. Cliquez sur l’{% icon item-delete %} en haut à gauche.
5. Pour confirmer, cliquez sur _Oui_{:.doc-button}.
