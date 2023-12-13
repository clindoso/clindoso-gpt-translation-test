---
title: Configurer les modèles horaires
redirect_from:
  - fr/day-models-overview/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Apprenez à créer des modèles horaires de type mission à horaires fixes, mission à horaires variables et cadre de disponibilité. Découvrez comment ajouter des activités aux modèles horaires.
related_articles:
  - overwrite_title: Ajouter des activités à des modèles horaires
    filepath: features/administration/daymodels/daymodel-basics.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
---

Vous débutez avec les modèles horaires&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/administration/daymodels/daymodel-basics.md %}.

## Créer des modèles horaires

Vous pouvez créer et modifier des modèles horaires dans _Plan > Configuration > Modèles horaires_{:.breadcrumbs}.

> Remarque
> 
> - Les modèles horaires de type Mission à horaires fixes sont également appelés modèles horaires fixes.<br> 
> - Les modèles horaires de type Mission à horaires variables sont également appelés modèles horaires variables.

1. Pour ajouter un nouveau modèle horaire, cliquez sur l’{% icon item-add %}.
2. Dans le menu déroulant **Type**, sélectionnez le type de modèle horaire que vous souhaitez configurer.
3. Configurez votre modèle horaire.<br>Pour en savoir plus sur les options de configuration pour chaque type de modèle horaire, consultez les sections suivantes.
4. Pour sauvegarder le modèle horaire, cliquez sur _OK_{:.doc-button}.

Vous pouvez maintenant {% link_new ajouter des activités | features/administration/daymodels/daymodel-creation.md | #ajouter-des-activités-aux-modèles-horaires %} au nouveau modèle horaire. 

> Remarque
> 
> Si vous travaillez avec un nombre limité de modèles horaires dans votre unité opérationnelle<!-- add link when translated, see EN -->, vous devrez peut-être attribuer de nouveaux modèles horaires à votre unité opérationnelle. Si vous utilisez des modèles de planification, mettez à jour les modèles hebdomadaires.

### Mission à horaires fixes
   
| **Paramètre** | **Description** |
|:-----|:-----|
| Nom | Nom unique décrivant le modèle horaire. Nous recommandons de préciser le type de modèle horaire ainsi que ses heures de début et de fin, par exemple 8-16h30-fixe. |
| Abréviation | Cette version du nom est affichée dans les rapports et Schedules. Nous recommandons d’utiliser le nom spécifié ou une version plus courte de celui-ci. |
| Raccourci-clavier | Raccourci clavier facultatif vous permettant d’insérer ce modèle horaire plus rapidement dans le Centre de planification. Pour en savoir plus, lisez notre article sur les {% link_new raccourcis | best-practices/tips-on-shift-center-usage.md %}. |
| Couleur |  La couleur apparaît dans le planning et les pages des données de configuration.<br>Elle peut vous aider à identifier rapidement la durée, le type de modèle horaire ou les activités associées. |
| Valide du/Jusqu’au | Période facultative durant laquelle le modèle horaire peut être utilisé.<br>Pour en savoir plus, lisez l’article {% link_new Périodes de validité | features/administration/set-a-validity-period.md %}. |
| Début | Heure à laquelle la journée fixe commence. |
| Fin | Heure à laquelle la journée fixe se termine. |
| Durée brute de la mission | Durée de la journée en heures.<br>Si vous configurez cette valeur, elle remplacera l’heure de fin.<br>Remarque&nbsp;: les modèles horaires de type Mission à horaires fixes peuvent couvrir jusqu’à deux journées. Pour créer des horaires de nuit, ajoutez jusqu’à 24&nbsp;heures à l’heure de fin lors de la création du modèle horaire, ou utilisez la durée totale de la mission. La durée maximum est 48:00 (h). |
| Activité | La première activité est l’activité de base<!-- add link when translated, see EN -->.<br>Remarque&nbsp;: vous ne pourrez plus la modifier après avoir sauvegardé le modèle horaire.


### Mission à horaires variables
   
| **Paramètre** | **Description** |
|:---------------------|:---------------------|
| Nom | Nom unique décrivant le modèle horaire. Nous recommandons de préciser le type de modèle horaire ainsi que ses heures de début et de fin, par exemple 8-20-8-var. |
| Abréviation | Cette version du nom est affichée dans les rapports et Schedules. Nous recommandons d’utiliser le nom spécifié. |
| Couleur |  La couleur apparaît dans le planning et les pages des données de configuration.<br>Elle peut vous aider à identifier rapidement la durée, le type de modèle horaire ou les activités associées. |
| Valide du/Jusqu’au | Période facultative durant laquelle le modèle horaire peut être utilisé.<br>Pour en savoir plus, lisez l’article {% link_new Périodes de validité | features/administration/set-a-validity-period.md %}. |
| Début du cadre temporel | Heure de début minimale de la journée. |
| Fin du cadre temporel | Heure de fin maximale de la journée. |
| Durée du cadre temporel | Le nombre d’heures entre l’heure de début minimale et l’heure de fin maximale de la journée.<br>Elle remplace l’heure de fin du cadre temporel. |
| Durée brute de la mission | Durée totale de la journée, pauses comprises. La durée doit être inférieure à celle du cadre temporel. Si la durée de la mission est égale au cadre temporel, le modèle horaire fonctionne comme une Mission à horaires fixes. |
| Intervalle | Intervalle sur la base duquel injixo peut définir une heure de début et de fin dans le cadre temporel défini. |
| Activité | La première activité est {% link_new l’activité de base | features/administration/daymodels/daymodel-basics.md | #activité-de-base-et-durée-de-la-journée %}.<br>Remarque&nbsp;: vous ne pourrez plus la modifier après avoir sauvegardé le modèle horaire. |

### Cadre de disponibilité

Vous pouvez par exemple utiliser ce modèle horaire dans les rotations d’horaires pour configurer les disponibilités de plusieurs employés en même temps. Remarque&nbsp;: les disponibilités du modèle horaire remplacent les disponibilités saisies par les employés dans injixo Me, ainsi que les disponibilités ajoutées manuellement dans le Centre de planification. Pour en savoir plus, lisez notre article sur les {% link_new disponibilités | features/administration/availabilities.md %}.

| **Paramètre** | **Description** |
|:---------------------|:---------------------|
| Nom | Nom unique décrivant le modèle horaire. Nous recommandons de préciser le type de modèle horaire ainsi que ses heures de début et de fin, par exemple 8-16-dispo. |
| Abréviation | Cette version du nom est affichée dans les rapports et Schedules. Nous recommandons d’utiliser le nom spécifié. |
| Couleur |  La couleur apparaît dans le planning et les pages des données de configuration.<br>Elle peut être utile lors de la configuration de rotations d’horaires, par exemple. |
| Valide du/Jusqu’au | Période facultative durant laquelle le modèle horaire peut être utilisé.<br>Pour en savoir plus, lisez l’article {% link_new Périodes de validité | features/administration/set-a-validity-period.md %}. |
| Début du cadre de disponibilité | Heure de début minimale de la journée. |
| Fin du cadre de disponibilité | Heure de fin maximale de la journée. |
| Durée du cadre de disponibilité | Le nombre d’heures entre l’heure de début minimale et l’heure de fin maximale de la journée. La durée maximum est 48&nbsp;heures.<br>Elle remplacera la fin de la période de disponibilité. |

## Ajouter des activités aux modèles horaires

Pour affiner davantage un modèle horaire existant, vous pouvez y ajouter des pauses ou d'autres activités. Configurez d’autres activités si vous avez besoin de représenter des tâches spécifiques sur lesquelles les employés doivent travailler à un moment donné pendant une journée. Il peut s’agir notamment de vérifier les canaux de réseaux sociaux de l’organisation ou d’effectuer des tâches de back-office. 

Pour ajouter des activités, vous devez d'abord {% link_new créer le modèle horaire | features/administration/daymodels/daymodel-creation.md | #créer-des-modèles-horaires %}.

La fonction Optimiser le planning peut remplacer les activités de type Présence configurées comme Remplaçables. Si vous ne souhaitez pas planifier les employés pour travailler sur des activités spécifiques, l’activité de base est la seule activité de type Présence dans votre modèle horaire. Gardez à l’esprit que la configuration des activités dans les modèles horaires limitera la flexibilité des fonctionnalités d’optimisation (par exemple, l’optimisation complète, les activités supplémentaires, les réunions). Pour maintenir une optimisation aussi flexible que possible et éviter les erreurs de planification, nous recommandons de limiter au minimum la configuration des activités de type Présence dans les modèles horaires.

> Remarque
> 
> La première activité que vous ajoutez à un modèle horaire est automatiquement l’activité de base. Vous ne pourrez plus la modifier après avoir sauvegardé le modèle horaire.
> Nous recommandons d’utiliser l’activité Présent comme activité de base. Pour en savoir plus, lisez la section sur {% link_new l’activité de base | features/administration/daymodels/daymodel-basics.md | #activité-de-base-et-durée-de-la-journée %}.

### Ajouter une activité Présence ou Absence

Pour ajouter une activité Présence ou Absence à un modèle horaire existant, suivez ces instructions&nbsp;:

1. Sélectionnez un modèle horaire.
2. Dans la section **Présences et absences**, cliquez sur l’{% icon item-add %}.<br>Une fenêtre s’ouvre.
3. Configurez l’activité&nbsp;:
- **Début** et **Fin**&nbsp;:<br>Si la case **Relatif au début de la mission** est cochée&nbsp;: définissez le nombre d’heures/minutes après le début de la journée auquel vous souhaitez que l'activité commence et se termine (par exemple, pour 1,5 heures, saisissez 1:30).<br>Si la case **Relatif au début de la mission** est décochée&nbsp;: définissez l’heure exacte après le début de la journée à laquelle vous souhaitez que l’activité commence et se termine.
- **Durée**&nbsp;: si vous configurez une durée plus longue que celle qui sépare les heures de début et de fin configurées, vous créez un {% link_new corridor | features/administration/daymodels/daymodel-basics.md | #éléments-fixes-et-corridors %} à l’intérieur duquel l’activité peut être déplacée.
- **Intervalle de temps**&nbsp;: nous recommandons d’utiliser le même intervalle que votre ACD. Notez que la durée de l’activité doit être divisible par l’intervalle sélectionné.<br>Si vous saisissez 0, l'heure de début de l’activité est fixe et l’activité ne peut pas être déplacée dans un corridor.
- **Relatif au début de la mission**&nbsp;:<br>Si cette case est cochée (par défaut), l’activité démarre au nombre d’heures/minutes défini après le début de la journée. Si la journée est déplacée, l’activité est également déplacée.<br>Si cette case est décochée, l’activité commence à l’heure exacte configurée. Lorsque vous déplacez une journée variable, les activités ne se déplaceront pas. Cela peut être utile, par exemple lorsque des employés travaillant sur des horaires différents doivent assister à une réunion d’équipe en même temps.
4. Sélectionnez une **activité** depuis la liste déroulante en haut de la page.
5. Cliquez sur _OK_{:.doc-button}.

### Ajouter une activité Pause

Dans les modèles horaires flexibles et fixes, vous pouvez ajouter des pauses pour une planification optimisée et la génération de missions.  
Pour ajouter une activité Pause à un modèle horaire existant, suivez ces instructions&nbsp;:

1. Sélectionnez un modèle horaire.
2. Dans la section **Pauses (Création des missions)**, cliquez sur l’{% icon item-add %}.<br>Une fenêtre s’ouvre.
3. Configurez le script&nbsp;:
- **Début** et **Fin**&nbsp;:<br>Si la case **Relatif au début de la mission** est cochée&nbsp;: définissez le nombre d’heures/minutes après le début de la journée auquel vous souhaitez que la pause commence et se termine (par exemple, pour 4,5 heures, saisissez 4:30). Par défaut, les pauses sont entrées par rapport au début de la journée, car elles commencent généralement après un certain temps de travail.<br>Si la case **Relatif au début de la mission** est décochée&nbsp;: définissez l’heure exacte après le début de la journée à laquelle vous souhaitez que la pause commence et se termine.
- **Durée**&nbsp;: si vous configurez une durée plus longue que celle qui sépare les heures de début et de fin configurées, vous créez un {% link_new corridor | features/administration/daymodels/daymodel-basics.md | #éléments-fixes-et-corridors %} à l’intérieur duquel la pause peut être déplacée.
- **Intervalle**&nbsp;: nous recommandons d’utiliser le même intervalle que votre ACD. Notez que la durée de la pause doit être divisible par l’intervalle sélectionné.<br>Si vous saisissez 0, l'heure de début de l’activité est fixe et l’activité ne peut pas être déplacée dans un corridor.
- **Relatif au début de la mission**&nbsp;:<br>Si cette case est cochée (par défaut), la pause démarre au nombre d’heures/minutes défini après le début de la journée. Si la journée est déplacée, la pause est également déplacée.<br>Si cette case est décochée, la pause démarre à l’heure exacte configurée. Lorsque vous déplacez une journée variable, les pauses ne se déplaceront pas. Par exemple, cela peut être utile, si la cantine de votre centre de contacts n’est ouverte que pendant une durée limitée.
4. Sélectionnez une option dans le menu déroulant **Pause**.
5. Cliquez sur _OK_{:.doc-button}.

Remarque&nbsp;: dans injixo Enterprise WFM on-premise, le paramètre _48134_{:.id-label} détermine si les corridors de pause restent ou s’ils sont convertis en éléments fixes.

## Conséquences du changement des modèles horaires utilisés

Le changement des modèles horaires déjà utilisés dans vos plannings peut avoir différentes conséquences. Vous pouvez modifier les données de configuration non pertinentes pour la planification, telles que le nom, l'abréviation ou la couleur.

Cependant, nous vous recommandons de ne modifier que les données pertinentes pour la planification, telles que les heures de début et de fin, la durée totale de la journée, les présences, les absences et les pauses, avant de créer votre prochain planning. Lorsque vous modifiez un modèle horaire existant, injixo crée en interne une copie du modèle horaire original. De cette façon, les journées déjà planifiées sont conservées et seront toujours affichées.

Après avoir modifié un modèle horaire existant ou en avoir ajouté un nouveau, nous recommandons d’exécuter le processus de planification depuis le début afin que les nouveaux modèles horaires modifiés soient utilisés correctement.

Les modèles horaires affectés sont échangés dans les rotations d’horaires et les modèles hebdomadaires. Les modèles horaires déjà planifiés seront affichés avec une ligne en pointillés au bas du  Centre de planification et dans Schedules. Les journées avec ce modèle horaire ne peuvent plus être planifiées ou modifiées. Elles peuvent uniquement être supprimées du planning.

Si vous avez généré des journées à partir d'un modèle horaire et que des employés ont déjà demandé ces journées dans injixo Me dans le cadre de la génération de missions, vos employés ne peuvent plus voir ni demander de journées avec ce modèle horaire.
Les journées déjà demandées ne seront pas utilisées lors des tirages au sort ou des affectations ultérieures.

Remarque&nbsp;: les valeurs minimales et maximales saisies en tant que besoin en missions s’appliquent toujours au modèle horaire modifié.
