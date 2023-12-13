---
title: Créer des rotations d’horaires
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Utilisez les rotations d’horaires pour définir des cycles de planification
redirect_from:
  - /fr/shift-sequence-overview/
redirect_reason: filename used in old product onboarding
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/capacity/capacity-insert-shift-sequences.md
---


Une rotation d’horaires est un cycle hebdomadaire de modèles horaires ou d’activités. Avec les rotations d’horaires, vous pouvez rapidement insérer ces cycles dans votre planning. injixo optimisera le reste du planning.

Les rotations d’horaires vous permettent de gagner un temps important, car vous n’avez pas à planifier les cycles manuellement.

Voici quatre cas d’utilisation des rotations d’horaires&nbsp;:

1. Spécifier quand certaines journées doivent être planifiées
2. Planifier des activités récurrentes
3. Spécifier les jours de repos des employés
4. Spécifier quand des journées peuvent être planifiées selon les disponibilités des employés

Les rotations d’horaires sont composées d’une ou plusieurs lignes. Chaque ligne est un cycle distinct qui peut être inséré dans le planning.<br>
Chaque ligne contient des cellules qui représentent les jours de la semaine. Dans les cellules, insérez les modèles horaires ou les activités que vous souhaitez planifier à l’aide de la rotation d’horaires.<br>
Chaque ligne représente un cycle hebdomadaire de votre planning, le nombre de cellules sur chaque ligne doit donc être un multiple de 7. Le nombre de lignes maximum est de 53 car une rotation d’horaires ne peut pas dépasser un an.

## Prérequis

Pour créer des rotations d’horaires, vous devez d’abord créer des {% link_new activités | features/administration/activities.md %} ou des {% link_new modèles horaires | features/administration/daymodels/daymodel-creation.md %}.<br>
Après avoir créé des rotations d’horaires, vous devez les {% link_new assigner à vos employés | features/administration/employee-overview.md | #assigner-une-rotation-dhoraires %} avant de pouvoir les insérer dans votre planning.

>Remarque
>
>La semaine de travail commence le lundi par défaut.
>
>Vous pouvez modifier le premier jour de la semaine à l’aide du paramètre _48420_{:.id-label} _Début de la semaine de planification_.

## Créer des rotations d’horaires

Avant de créer votre première rotation d’horaires, déterminez le nombre de rotations d’horaires dont vous aurez besoin, ainsi que le nombre de lignes et de cellules dans chacune d’elles. Cela dépendra entièrement des besoins de votre organisation, c’est-à-dire le nombre de journées que vous planifiez, les éventuelles réunions récurrentes, etc.

Pour créer une rotation d’horaires, accédez à _Plan > Configuration > Rotations d’horaires_{:.breadcrumbs} et suivez les étapes ci-dessous&nbsp;:

1. Cliquez sur l’icône Créer {% icon item-add | icon-only %} dans la barre d’action.
2. Configurez les paramètres de la rotation d’horaires&nbsp;:<br>
  **Nom**&nbsp;: saisissez un nom unique (50 caractères maximum).<br>
  **Abréviation**&nbsp;: saisissez le nom ou une version plus courte de celui-ci (25 caractères maximum).<br>
  **Séquence(s)**&nbsp;: saisissez le nombre de lignes pour la rotation d’horaires (53 maximum).<br>Un numéro sera assigné à chaque ligne. Double-cliquez sur une ligne pour la renommer. Vous aurez besoin du numéro ou du nom de la ligne pour l’assigner à un employé par la suite.<br>
  **Durée**&nbsp;: saisissez une valeur comprise entre 1 et 371 jours. La durée doit être un multiple de 7.
6. Cliquez sur _OK_{:.doc-button}.

>Remarque
>
>La durée d’une rotation d’horaires doit toujours être un multiple de 7, même si votre centre de contacts n’est ouvert que cinq ou six jours par semaine. Les rotations d’horaires se répètent automatiquement. Avec une rotation d’horaires de cinq jours, la journée du lundi serait placée dans la cellule du samedi, la journée du mardi dans la cellule du dimanche, etc.
>
>Si vous souhaitez planifier des cycles avec une durée différente (par exemple, un pour les réunions hebdomadaires, un pour les réunions prévues toutes les deux semaines), vous devez créer des rotations d’horaires séparément.

Une fois que vous avez créé une rotation d’horaires, vous pouvez définir des {% link_new périodes de validité | features/administration/set-a-validity-period.md %} pour celle-ci&nbsp;:

1. Cliquez sur {% icon item-edit %} au-dessus du tableau.
2. Saisissez ou sélectionnez des dates dans les champs **Valide du** et **Jusqu’au**.
3. Cliquez sur _OK_{:.doc-button}.

### Insérer des modèles horaires

1. Dans la section **Options**, sélectionnez **Insertion d’un modèle horaire** depuis le menu déroulant à gauche.
2. Sélectionnez le modèle horaire que vous souhaitez insérer depuis le menu déroulant **Modèle horaire**.
3. Saisissez un **nombre**. Il s’agit du nombre de jours consécutifs dans lequels vous insérez le modèle horaire.
4. Dans le tableau, cliquez sur la première cellule dans laquelle vous souhaitez insérer le modèle horaire.<br>
  Si vous saisissez un chiffre supérieur à 1, le modèle horaire sera inséré dans cette cellule et dans autant de cellules que nécessaire pour atteindre ce chiffre.

La rotation d’horaires est sauvegardée automatiquement.

> Conseil
>
> Utilisez des activités ou des modèles horaires fixes. Si vous insérez des modèles horaires variables dans une rotation d’horaires, la journée commencera toujours le plus tôt possible.

### Insérer des activités

1. Dans la section **Options**, sélectionnez **Insertion d’une activité** depuis le menu déroulant à gauche.
2. Sélectionnez l’activité que vous souhaitez insérer depuis le menu déroulant **Activité**.
3. Saisissez un **nombre**. Il s’agit du nombre de jours consécutifs dans lequels vous insérez l’activité.
4. Pour spécifier l’heure à laquelle l’activité est planifiée, saisissez une période (au format 24 heures) dans les champs **De** et **À**, ou cochez la case **Pour la journée entière**.
5. Dans le tableau, cliquez sur la première cellule dans laquelle vous souhaitez insérer l’activité.<br>
  Si vous saisissez un chiffre supérieur à 1, l’activité sera inséréee dans cette cellule et dans autant de cellules que nécessaire pour atteindre ce chiffre.

> Activités prenant fin après minuit
>
> Si vous souhaitez insérer des activités se terminant après minuit, ajoutez 24 à l’heure de fin. Par exemple, si l’activité se termine à 1h le jour suivant, saisissez 25:00.

## Modifier des rotation d’horaires

1. Dans la section **Rotation d’horaires**, sélectionnez une rotation d’horaires depuis le menu déroulant.
2. Cliquez sur _Appliquer_{:.doc-button}.
3. Cliquez sur {% icon item-edit %} dans la barre d'action supérieure pour modifier le nom, l’abréviation, le nombre de lignes pour les employés ou la durée.<br>Une fois vos modifications terminées, cliquez sur _OK_{:.doc-button}.
4. Cliquez sur {% icon item-edit %} dans la barre d'action au-dessus de la grille pour modifier les périodes de validité.<br>Une fois vos modifications terminées, cliquez sur _OK_{:.doc-button}.

### Supprimer des éléments d’une rotation d’horaires

Pour supprimer un ou plusieurs éléments d’une rotation d’horaires, suivez les étapes ci-dessous&nbsp;:
1. Dans la section **Rotation d’horaires**, sélectionnez une rotation d’horaires depuis le menu déroulant.
2. Cliquez sur _Appliquer_{:.doc-button}.
3. Dans la section **Options**, sélectionnez **Suppression** depuis le menu déroulant.
4. Cliquez sur les cellules dont vous souhaitez supprimer les éléments.<br>
  Les éléments sont supprimés automatiquement.

Pour supprimer tous les éléments d’une rotation d’horaires, suivez les étapes ci-dessous&nbsp;:

1. Dans la section **Rotation d’horaires**, sélectionnez une rotation d’horaires depuis le menu déroulant.
2. Cliquez sur _Appliquer_{:.doc-button}.
3. Dans la section **Options**, cochez la case **Supprimer tout** et cliquez sur _Appliquer_{:.doc-button}.

Les éléments sont supprimés automatiquement.

## Supprimer une rotation d’horaires

1. Dans la section **Rotation d’horaires**, sélectionnez une rotation d’horaires depuis le menu déroulant.
2. Cliquez sur _Appliquer_{:.doc-button}.
3. Cliquez sur l’{% icon item-delete %} dans la barre d’action.
4. Dans la fenêtre de confirmation, cliquez sur _Oui_{:.doc-button}.

## Exemples d’utilisation

Vous pouvez utiliser les rotations d’horaires dans différents cas.

### Exemple 1&nbsp;: spécifier quand certaines journées doivent être planifiées

Cet exemple s’applique lorsque vous devez planifier des journées du matin et du soir pour différents groupes d’employés. Il peut également s’appliquer si un de vos conseillers ne peut pas commencer sa journée à 11h les lundis, mais peut commencer plus tôt les autres jours de la semaine. 
 
Pour savoir si cet exemple s’applique à votre situation et découvrir comment configurer les rotations d’horaires conformément, regardez la vidéo Academy suivante (en anglais)&nbsp;:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4" type="video/mp4">
   Votre navigateur ne prend pas en charge la balise vidéo. Vous pouvez <a href="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4">télécharger la vidéo</a> pour la regarder hors ligne.
   </video>
</div>
<br>

### Exemple 2&nbsp;: planifier des activités récurrentes

Cet exemple s’applique notamment si vous devez planifier des réunions ayant lieu chaque semaine, ou si vous souhaitez planifier un employé pour travailler une heure chaque jour en back-office à une heure spécifique.

Pour savoir si cet exemple s’applique à votre situation et découvrir comment configurer les rotations d’horaires conformément, regardez la vidéo Academy suivante (en anglais)&nbsp;:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-2.mp4" type="video/mp4">
  </video>
</div>
<br>

### Exemple 3&nbsp;: spécifier les jours de repos des employés

Cet exemple s’applique notamment si vous souhaitez définir des cycles de jours de congés spécifiques pour certains employés. 

Pour savoir si cet exemple s’applique à votre situation et découvrir comment configurer les rotations d’horaires conformément, regardez la vidéo Academy ci-dessous (en anglais)&nbsp;:

  <div class="inline-video-container">
    <video class="inline-video-player-v" controls> 
     <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-3.mp4" type="video/mp4">
    </video>
  </div>
<br>

### Exemple 4&nbsp;: spécifier quand des journées peuvent être planifiées selon les disponibilités des employés

Cet exemple s’applique lorsque vous souhaitez planifier des employés dont les disponibilités varient.

Pour savoir si cet exemple s’applique à votre situation et découvrir comment configurer les rotations d’horaires conformément, regardez la vidéo Academy ci-dessous (en anglais)&nbsp;:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-4.mp4" type="video/mp4">
  </video>
</div>
<br>

## Générer un rapport

Vous pouvez générer un rapport regroupant toutes les données d’une rotation d’horaires au format PDF. Pour générer le rapport, suivez les étapes ci-dessous&nbsp;:

1. Dans la section Rotations d’horaires à gauche, sélectionnez la rotation d’horaires pour laquelle vous souhaitez générer un rapport.
2. Cliquez sur _Appliquer_{:.doc-button}.
3. Cliquez sur _Rapport_{:.doc-button} en haut du tableau.
4. Dans la fenêtre, vous pouvez cocher la case pour envoyer le rapport à l’adresse e-mail utilisée pour votre compte injixo.

Le rapport indique les heures de début et de fin des activités ou des modèles horaires inclus dans la rotation d’horaires, ainsi que leur durée nette en heures. Le rapport est structuré par semaine.
Le rapport indique également les totaux et moyennes suivants de la durée nette&nbsp;:

- Ligne Somme&nbsp;: durée nette de toutes les activités ou modèles horaires dans la rotation d’horaires
- Colonne Somme&nbsp;: total de la durée nette des activités ou modèles horaires par semaine
- Ligne Moyenne&nbsp;: valeur moyenne pour toutes les valeurs de la colonne Total
