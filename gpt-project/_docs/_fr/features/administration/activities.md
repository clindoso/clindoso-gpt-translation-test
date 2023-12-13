---
title: Créer des activités
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
beta-feature: false
description: Créer des activités pour représenter les tâches planifiées et non planifiées dans votre société
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Pour créer, modifier et supprimer des activités, accédez à _Plan > Configuration > Activités_{:.breadcrumbs}.

Les activités représentent toutes les tâches planifiées et suivies dans votre organisation, comme les appels, les pauses, les absences ou les réunions.<br>
Vous pouvez créer un nombre illimité d’activités. Le nombre d’activités dépend du nombre de tâches que vous souhaitez distinguer et du niveau de détail souhaité.<br>
Les activités sont essentielles pour la planification dans injixo. Elles sont liées à d’autres éléments de configuration, comme les {% link_new unités opérationnelles | features/administration/create-and-manage-planning-units.md | #ajouter-des-activités %} ou les {% link_new modèles horaires | features/administration/daymodels/daymodel-basics.md %}. Elles font également partie des plannings gérés dans le {% link_new Centre de planification | features/scheduling/shiftcenter/add-and-delete-items.md %} ou dans {% link_new Schedules | features/scheduling/schedules/schedules-edit.md %}.

injixo inclut deux activités pré-configurées (qui ne peuvent être supprimées)&nbsp;:<br>
- Présent&nbsp;: cette activité est utilisée comme activité de base dans les modèles horaires. Pendant la planification, injixo remplace cette activité par d’autres activités configurées comme planifiables automatiquement.
- Congé&nbsp;: cette activité est utilisée pour planifier des congés rémunérés selon le droit aux congés de l’employé. Créez les congés non rémunérés comme activités distinctes.

## Créer une activité

1. Cliquez sur _Nouvelle activité_{:.doc-button}.
2. Ajoutez les informations générales pour votre activité&nbsp;:
   - **Nom**&nbsp;: nom unique décrivant votre activité. L’abréviation sera générée automatiquement.
   - **Type**&nbsp;: le type d’activité détermine la façon dont injixo utilise les activités dans la planification et dont elles sont affichées dans les autre modules et les rapports. Pour en savoir plus, lisez notre article sur les différents {% link_new types d’activités | features/administration/activity-types-and-properties.md | #types-dactivité %}.
   - **Couleur**&nbsp;: la couleur apparaît dans le planning et les pages des données de configuration. Elle vous aide à identifier les différentes activités.
   - **Raccourci**&nbsp;: raccourci clavier facultatif vous permettant d’insérer cette activité plus rapidement dans le Centre de planification. Pour en savoir plus, lisez notre article sur les {% link_new raccourcis | best-practices/tips-on-shift-center-usage.md | #tip-2-shortcuts-for-a-quick-assignment-of-activities %}.
   - **Nom et abréviation officiels**&nbsp;: nom alternatif pouvant être utilisé pour les rapports internes et les intégrations. injixo Me affiche toujours le nom entré dans **Nom**.
3. Cochez l’une des cases pour définir différentes {% link_new propriétés pour l’activité | features/administration/activity-types-and-properties.md | #propriétés-des-activités %}.
  Si vous cochez la case Planifiable automatiquement, vous pouvez modifier {% link_new l’ordre d’importance | best-practices/importance-for-activities.md %}.
  Si vous cochez la case Remplaçable, vous pouvez modifier la  {% link_new priorité | best-practices/priority-for-activities.md %}.
4. (Facultatif) {% link_new Assignez des compétences | features/administration/work-with-skills.md | #assigner-des-compétences-à-des-activités %} à l’activité.
5. Cliquez sur _Créer l’activité_{:.doc-button}.

Pour en savoir plus, lisez l’article sur les {% link_new types d’activités et leurs propriétés | features/administration/activity-types-and-properties.md %}.

### Identifiant de l’activité

Pour voir l’identifiant d’une activité, vous pouvez&nbsp;: 
- Cliquer sur une activité dans la liste des **Activités**. L’URL dans la barre d’adresse de votre navigateur indique l’identifiant de l’activité sélectionnée (par exemple, https://www.injixo.com/plan/configuration/activities/1234).
- Utiliser l’API injixo. Découvrez comment [gérer les activités via l’API injixo](https://api.injixo.com/resources/activities/).

## Multi-activités et sous-activités 


Les multi-activités vous permettent de planifier les employés possédant plusieurs compétences lorsque l’une de leurs compétences est requise. Une activité devient une multi-activité lorsque vous y {% link_new assignez d’autres activités | features/administration/activity-types-and-properties.md | #sous-activités %}. Les activités assignées deviennent des sous-activités. Dans la liste d’activités, les multi-activités sont marquées d’une icône <em class="multiactivity-icon"></em>.

Lorsque vous cliquez sur une sous-activité, vous pouvez voir la section **Multi-activités**, qui affiche toutes les multi-activités auxquelles elle est assignée.

Lorsque vous cliquez sur une activité qui n’est pas une sous-activité, vous pouvez voir la section **Sous-activités**, à partir de laquelle vous pouvez sélectionner d’autres activités qui pourront devenir les sous-activités de l’activité que vous modifiez. L’activité devient alors une multi-activité.
Vous pouvez uniquement assigner des sous-activités à une activité après l’avoir créée.

## Systèmes externes

<!-- will be made obsolete by the new activity mapping page. Will require a separate article -->

Vous pouvez mapper les activités de systèmes externes à une activité d’injixo.
1. Sélectionnez une activité à partir de la liste, faites défiler jusqu’à la section **Systèmes externes** et cliquez sur _Modifier dans WFM_{:.doc-button}. 
2. Accédez à la section **Systèmes externes**.
3. Cliquez sur l’{% icon item-add %}.
4. Sélectionnez un **système externe**, l'**ID de l'activité du système externe** et une **classification** à partir des menus déroulants.
5. Cliquez sur _OK_{:.doc-button}.

> Vous ne pouvez assigner une activité d’un système externe à une activité d’injixo qu’une seule fois.

## Dupliquer une activité

Pour créer une nouvelle activité avec les mêmes propriétés générales qu’une activité existante, suivez ces étapes&nbsp;:

1. Sélectionnez une activité dans la liste des **Activités**.
2. Cliquez sur **Dupliquer l’activité** sous le nom de l’activité.  
Une fenêtre **Créer une nouvelle activité** s’ouvre, avec des cases pré-cochées. Les compétences et sous-activités assignées ne sont pas dupliquées.
3. Entrez le **Nom** de la nouvelle activité.
4. (Facultatif) Modifiez la couleur et d’autres propriétés.
5. Cliquez sur _Créer l’activité_{:.doc-button}.

## Modifier ou supprimer une activité

1. Sélectionnez une activité dans la liste des **Activités**.
  - Pour modifier l’activité, changez les informations souhaitées et cliquez sur _Enregistrer les modifications_{:.doc-button}.
  - Pour supprimer l’activité, cliquez sur _Supprimer l’activité_{:.doc-button} en bas à droite.

Si l’activité supprimée a été assignée à d’autres éléments de configuration, comme des unités opérationnelles ou des modèles horaires, son nom apparaît en italique dans ces éléments. L’activité supprimée ne sera plus assignée à d’autres éléments mais restera visible dans les éléments de configuration. Vous pourrez avoir besoin de recréer les modèles horaires qui utilisaient l’activité supprimée.  
Dans le Centre de planification, les activités supprimées sont affichées {% link_new encadrées de pointillés | features/scheduling/shiftcenter/shift-center-overview.md | #how-are-items-displayed %}.  
Schedules affiche les activités supprimées en gris sans leur nom. Les informations temporelles resteront visibles, sauf en vue journalière.
