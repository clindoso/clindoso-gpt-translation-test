---
title: Utiliser les compétences
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Découvrez comment les compétences de votre équipe sont reflétées dans injixo. Créez, modifiez et supprimez les compétences et les niveaux de compétence.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/configure-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
redirect_from:
  - fr/skills/
redirect_reason: Updated filename on 24 July 2023
---

Les compétences vous permettent de vous assurer que les employés sont planifiés uniquement pour les activités pour lesquelles ils sont qualifiés. Les compétences associent les qualifications de vos employés (connaissance du produit, langues parlées, canaux de communication, etc.) aux activités sur lesquelles ils peuvent travailler et à planifier dans injixo.

Pour configurer les compétences, accédez à _Plan > Configuration > Compétences_{:.breadcrumbs}.

## Créer des compétences

Créez au moins une compétence pour chaque activité nécessitant une qualification spécifique. Lorsque vous créez une compétence, injixo lui attribue un niveau de compétence de 100&nbsp;% par défaut. Les niveaux de compétence reflètent le degré de qualification requis pour travailler sur une activité, par exemple avoir 100&nbsp;% de compétences en anglais mais seulement 50&nbsp;% en espagnol. Vous pouvez créer différents niveaux de compétence pour une même compétence. 

> Si les employés n’ont pas besoin de compétences spécifiques pour travailler sur une activité, il n’est pas nécessaire de créer de compétence.

1. Cliquez sur _Nouvelle compétence_{:.doc-button}.
2. Entrez un **Nom**.
   L’abréviation est générée automatiquement, mais vous pouvez la modifier.
3. (Facultatif) Cliquez sur _Ajouter un niveau de compétence_{:.doc-button} pour modifier le **niveau** de compétence par défaut, ou pour ajouter des niveaux de compétence supplémentaires si certains employés sont moins compétents dans cette activité. Voir aussi&nbsp;: [Calculer l’aptitude en utilisant le niveau et la pondération](#calculer-laptitude-en-utilisant-le-niveau-et-la-pondération).
4. Cliquez sur _Créer la compétence_{:.doc-button}.  

 Vous pouvez ensuite [assigner un niveau de compétence à un employé](#ajouter-des-niveaux-de-compétence-à-un-employé) et [attribuer cette compétence à une activité](#assigner-des-compétences-à-des-activités).

## Dupliquer des compétences

Pour créer une nouvelle compétence avec les mêmes niveaux qu’une compétence existante, suivez ces étapes&nbsp;:

1. Dans la liste des **compétences**, cliquez sur la compétence que vous souhaitez dupliquer.
2. Cliquez sur **Dupliquer la compétence** sous le nom de la compétence.  
   Une fenêtre **Créer une nouvelle compétence** s’ouvre avec des niveaux de compétence pré-remplis.
3. Entrez le **Nom** de la nouvelle compétence.
4. (Facultatif) Modifiez les niveaux de compétence.
5. Cliquez sur _Créer une compétence_{:.doc-button}.

## Modifier les compétences et les niveaux de compétence

1. Sélectionnez une compétence dans la liste.
2. Modifiez la compétence ou les niveaux de compétence.
   Pour supprimer un niveau de compétence, cliquez sur l’{% icon trash %} à côté de celle-ci.
3. Cliquez sur _Enregistrer les modifications_{:.doc-button}.

## Supprimer des compétences

1. Sélectionnez une compétence dans la liste.
2. Cliquez sur _Supprimer la compétence_{:.doc-button} et confirmez.

## Assigner des compétences à des activités

1. Accédez à _Plan > Configuration > Activités_{:.breadcrumbs}.
2. Sélectionnez une activité dans la liste et faites défiler jusqu’à la section **Compétences**.
3. Sélectionnez une compétence dans la liste déroulante.
4. (Facultatif) Modifiez la **pondération**. Si vous n’ajoutez qu’une seule compétence, cette valeur doit rester à 100 (valeur par défaut).  
   Pour les activités qui nécessitent plus d’une compétence, vous pouvez [utiliser la pondération](#calculer-laptitude-en-utilisant-le-niveau-et-la-pondération) pour déterminer quelle compétence est la plus importante.
5. Cliquez sur _Enregistrer les modifications_{:.doc-button}.

## Ajouter des niveaux de compétence à un employé

1. Accédez à _Plan > Configuration > Employés_{:.breadcrumbs}.
2. Sélectionnez un employé dans la liste et naviguez vers la section **Niveaux de compétence**.
3. Cliquez sur l’{% icon item-add %} et sélectionnez un ou plusieurs niveaux de compétence dans la liste.
   Pour sélectionner plusieurs éléments, pressez et maintenez la touche **Shift** ou **CTRL** lors de la sélection.
4. (Facultatif) Ajoutez une {% link_new période de validité | features/administration/set-a-validity-period.md %} pour le niveau de compétence en sélectionnant les dates **À partir du** et **Jusqu’au**.
   Vous ne pouvez pas attribuer différents niveaux de compétence pour la même compétence à un employé pendant la même période de validité.
 5. Cliquez sur _OK_{:.doc-button}.  
   Les activités qui nécessitent les compétences assignées apparaîtront dans la section **Activités** pour cet employé.

Une activité peut nécessiter une ou plusieurs compétences. Pour travailler sur une activité qui nécessite plusieurs compétences, les employés assignés doivent posséder toutes les compétences.

Conseil&nbsp;: pour assigner une compétence à plusieurs employés à la fois, vous pouvez utiliser la <!-- {% link_new -->mise à jour en masse<!-- | features/administration/employee-overview.md | #use-mass-update %}-->. 

## Calculer l’aptitude en utilisant le niveau et la pondération

injixo peut calculer une valeur d’aptitude basée sur&nbsp;:

- le niveau de compétence d’un employé,
- les valeurs de pondération lorsque une activité nécessite plusieurs compétences.

Exemple&nbsp;: vous avez une activité Appels en Espagnol qui nécessite deux compétences, Espagnol et Appels. La compétence Espagnol est deux fois plus importante que la compétence Appels. Les valeurs de pondération sont de 100 pour Espagnol et de 50 pour Appels.

- L’employé 1 a un niveau de compétence de 50&nbsp;% pour Espagnol et de 100&nbsp;% pour Appels.
- L’employé 2 a un niveau de compétence de 100&nbsp;% pour Espagnol et de 50&nbsp;% pour Appels.

Cela se traduit par une valeur d’aptitude de 66,66&nbsp;% pour l’employé 1 et de 83,33&nbsp;% pour l’employé 2.

La valeur d’aptitude est calculée à l’aide de cette formule&nbsp;:<br> `(Somme(Pondération de chaque compétence * niveau de compétence individuel pour cette compétence) / (Somme de toutes les pondérations)`

Si une activité ne nécessite qu’une seule compétence, la valeur d’aptitude est égale au niveau de compétence de l'employé.

Pour que la valeur d’aptitude soit prise en compte lors de {% link_new l’optimisation du planning | features/scheduling/schedules/schedules-optimized-schedules.md %} (plutôt que d’utiliser le nombre total d’employés), configurez le paramètre _48069_{:.id-label} _Prendre en compte l’aptitude des employés à exécuter les activités_. Dans le {% link_new Centre de planification | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %} et {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}, la couverture et l’occupation ne peuvent pas être affichées en fonction de l’aptitude des employés. Dans ces cas, la couverture et l’occupation sont toujours affichées avec une valeur de 100&nbsp;% pour indiquer le nombre total d’employés.
