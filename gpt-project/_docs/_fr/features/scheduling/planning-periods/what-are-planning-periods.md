---
title: Périodes de planification
redirect_from:
  - /fr/periodes-planification/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-employees-to-see-their-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shift-bidding.md
product_label:
  - classic
---

Dans le menu *WFM > Planification > SchedulePro > Périodes de planification*{:.breadcrumbs}, vous définissez sur quelle période le planning est publié et sur quelle période les Employés peuvent effectuer des demandes de congés. Les Périodes de planification peuvent être définies par Unité opérationnelle et par Groupe.

Le menu *Périodes de planification*{:.menu-item} se découpe en deux sections. La première permet de créer une nouvelle Période de planification ou d'éditer une existante. Dans la deuxième section, vous pouvez exécuter toutes les opérations liées au type de Période de planification.

{{ 1 | image: "Écran période de planification", '100%' }}

## 1. Gestion des Périodes de planification

La première section vous permet de commencer à travailler avec les Périodes de planification, sélectionnez les éléments de la section `Périodes de planification`.

| Paramètre | Description |
| ------- | ------- |
| Unité opérationnelle | Sélectionner l'Unité opérationnelle pour afficher les périodes de planification correspondantes. La dernière Unité opérationnelle utilisée est toujours sélectionnée par défaut.|
| Type | Sélectionner le type de Période de planification à afficher dans l'Unité opérationnelle. Les Périodes de planification peuvent être de type Standard ou d'un type personnalisé.<br/>- Une Période de planification de type `Standard` permet la publication des plannings de vos Employés. <br/>- Une Période de planification de type `personnalisé` permet de définir une période sur laquelle vos Employés peuvent soumettre des `Desiderata`. Si une Activité est configurée avec l'option `Desidérata`, un Type de Période de planification correspondant sera disponible.|
| Groupe | Sélectionner le Groupe pour afficher les Périodes de planification correspondantes.|

Confirmer votre sélection en cliquant sur *Appliquer*{:.doc-button}. Les Périodes de planification disponibles pour ces paramètres apparaîtront.

### Périodes de Planification - Vue générale du type Standard

| Colonne | Description |
| ------- | ------- |
| Valide du | Date de début |
| Jusqu'à | Date de fin |
| Groupe | Groupe sélectionné |
| Statut | Statut de la Période de planification |
| Date limite | Date limite pour chaque Période de planification |
| Héritée | Cette colonne indique si la Période de planification est héritée d'une Unité opérationnelle de niveau supérieur |

### Création d'une Période de planification

Cliquer sur _!["Bouton Créer"](/assets/img/{{ page.lang }}/features/what-are-planning-periods/image-2.gif)_{:.doc-button-icon} pour créer une Période de planification et faire apparaître la section correspondante.

| Paramètre | Description |
| ------- | ------- |
| Unité opérationnelle | Nom de l'Unité opérationnelle pour laquelle la Période de planification doit être créée. Cette zone est pré-remplie par votre sélection initiale et ne peut être modifiée. |
| Groupe | Groupe pour lequel la Période de planification doit être affectée. |
| Valide du | Date de début de la Période de planification. |
| Jusqu'au | Date de fin de la Période de planification (1 an maximum). |
| Statut | Statut de la Période de planification : il détermine si les Employés peuvent visualiser leur planning pour la Période de planification donnée. Les Statuts suivants sont disponibles : <br />- `[Verrouillé]` : Si une Période de planification est verrouillée, les Employés n'ont pas la possibilité de visualiser leur planning, de saisir des desiderata (horaires ou absences) ou de faire des échanges. Ce statut permet de travailler sur vos plannings sans les diffuser.<br />- `Disponible` : Si une Période de planification est disponible, les Employés ont la possibilité de saisir des desiderata (horaires ou absences).<br />- `Lecture` : Si une Période de planification est en lecture, les Employés ont la possibilité de visualiser leur planning ou de faire des échanges.<br />- `Clôturé` : Lorsque la Date limite de la Période de planification est dépassée, le Statut passe en clôturé. Les Employés ont la possibilité de visualiser leur planning ou de faire des échanges.|
| Date limite | Date jusqu'à laquelle les Employés peuvent saisir leurs desiderata d'horaires ou d'absences. Cette date doit toujours être antérieure à la Date de début de la Période de planification. Vous pouvez également décider de ne pas définir de Date limite. |
| Type | Type de Période de planification sélectionné. Ce champ est pré-rempli par votre sélection initiale. Vous ne pouvez pas effectuer de saisie dans cette zone. |

Cliquer sur le bouton *OK*{:.doc-button} pour sauvegarder la sélection.

> Remarque
>
> Nous vous conseillons de définir une Période de planification devrait toujours commencer au premier jour de la semaine (lundi) et se terminer le dernier jour de la semaine (dimanche).

### Modifier une Période de planification

Pour modifier une Période de planification existante, sélectionnez-la dans la vue d'ensemble des Périodes de planification puis cliquez sur _!["Bouton Modifier"](/assets/img/{{ page.lang }}/features/what-are-planning-periods/image-3.gif)_{:.doc-button-icon} pour faire apparaître la section correspondante.

Les champs suivants peuvent êtres modifiés : Groupe, Valide du, Jusqu'au, Date limite, Statut.

Veuillez noter que le Statut ne peut pas être modifié en 'Disponible' si la Période de planification a une Date limite qui est expirée.

### Supprimer une Période de planification

Pour supprimer une Période de planification existante, sélectionnez-la dans la vue d'ensemble des Périodes de planification puis cliquez sur _!["Bouton Supprimer"](/assets/img/{{ page.lang }}/features/what-are-planning-periods/image-4.gif)_{:.doc-button-icon}. Une boîte de dialogue vous permet de confirmer ou d'annuler la suppression.

## 2. Opérations sur les Périodes de planification

La seconde section vous permet de réaliser des opérations sur les Périodes de planification sélectionnées.

### Missions

Le bloc "Missions" est utilisé pour Générer, Tirer au sort et Attribuer des missions. La Génération de Missions est détaillée dans une documentation séparée.

### Comptes temps dû

Le bouton *Calculer*{:.doc-button} dans la zone Comptes temps dû est disponible uniquement pour les Périodes de planification de type "Standard". Le Comptes temps dû correspond à la durée de travail `A effectuer` configurée dans le Contrat de l'Employé.

Il existe différentes méthodes de calcul pour les Comptes temps dû.

Sélectionnez la Période de planification souhaitée dans la vue générale et lancez le calcul en cliquant sur *Calculer*{:.doc-button} dans le bloc Comptes temps dû.

Dans le menu *Comptes temps dû*{:.menu-item} les valeurs requises peuvent être vérifiées et modifiées en cliquant sur *Modifier*{:.doc-button} dans le bloc Comptes temps dû ou en cliquant sur le menu *WFM > Planification > TimeManager > Comptes temps dû*{:.breadcrumbs}.

> Remarque
>
> Les Comptes temps dû ne peuvent être calculés correctement que s'il y a suffisamment d'éléments dans la section `Indications des temps de travail` du menu *Contrats*{:.menu-item} (*WFM > Administration > Planification > Contrats*{:.breadcrumbs}).
>
> Si le calcul échoue, vérifiez si un Contrat est attribué à l'Employé sur la Période de planification.

### Activité

Il est possible d'échanger une Activité avec une autre sur une période de temps définie. Sélectionnez la Période de planification et cliquez sur *Échanger*{:.doc-button} afin d'ouvrir la boîte de dialogue *Paramètres de l'échange d'activités*{:.menu-item}. Pour échanger les Activités, vous devez définir les paramètres suivants :

| Paramètre | Description |
| ------- | ------- |
| Date de début | Date de début de la période concernée (qui peut être différente mais comprise dans la Période de planification). |
| Date de fin | Date de fin de la période concernée (qui peut être différente mais comprise dans la Période de planification). |
| Sélection des employés | - Tous : Permet de sélectionner tous les Employés de l'Unité opérationnelle pour la période concernée.<br />- Groupe : Permet de sélectionner un ou plusieurs Groupes de l'Unité opérationnelle pour la période concernée.<br />- Employé : Permet de sélectionner un ou plusieurs Employés de l'Unité opérationnelle pour la période concernée.|
| Liste des groupes | Si vous avez sélectionné l'option `Groupe`, choisissez ici un ou plusieurs Groupes pour l'échange d'Activités. Pour sélectionner plusieurs Groupes, maintenez la touche `Ctrl` enfoncée tout en les sélectionnant.|
| Liste des employés| Si vous avez sélectionné l'option `Employé`, choisissez ici le ou les Employés pour l'échange d'Activités. Pour sélectionner plusieurs Employés, maintenez la touche `Ctrl` enfoncée tout en les sélectionnant.|
| Catégorie | Sélectionner une ou plusieurs Catégories dans lesquelles effectuer l'échange d'Activités. |
| Activités - Chercher | Nom de l'Activité à remplacer. |
| Activités - Remplacer | Nom de l'Activité de remplacement. |

Cliquez sur le bouton *OK*{:.doc-button} pour confirmer votre sélection ou sur *Annuler*{:.doc-button}.

### Catégorie

Il est possible de copier les Activités d'une Catégorie vers une autre, de copier les Activités d'une Catégorie vers elle-même sur une période différente ou de supprimer les données d'une Catégorie. Les deux fonctionnalités *Copier*{:.doc-button} et *Supprimer*{:.doc-button} sont disponibles uniquement pour les Périodes de planification de type `Standard`.

#### Copier le contenu d'une Catégorie

Pour effectuer cette opération, sélectionnez la Période de planification souhaitée dans la vue d'ensemble et appuyez sur *Copier*{:.doc-button} dans le bloc Catégorie. Vous devez définir les paramètres suivants :

| Paramètre | Description |
| ------- | ------- |
| Date de début | Date de début de la période concernée (qui peut être différente mais comprise dans la Période de planification). |
| Date de fin | Date de fin de la période concernée (qui peut être différente mais comprise dans la Période de planification). |
| Sélection des employés | - Tous : Permet de sélectionner tous les Employés de l'Unité opérationnelle pour la période concernée.<br />- Groupe : Permet de sélectionner un ou plusieurs Groupes de l'Unité opérationnelle pour la période concernée.<br />- Employé : Permet de sélectionner un ou plusieurs Employés de l'Unité opérationnelle pour la période concernée.|
| Liste des groupes | Si vous avez sélectionné l'option `Groupe`, choisissez ici un ou plusieurs Groupes pour l'échange d'Activités. Pour sélectionner plusieurs Groupes, maintenez la touche `Ctrl` enfoncée tout en les sélectionnant.|
| Liste des employés| Si vous avez sélectionné l'option `Employé`, choisissez ici le ou les Employés pour l'échange d'Activités. Pour sélectionner plusieurs Employés, maintenez la touche `Ctrl` enfoncée tout en les sélectionnant.|
| Catégorie source | Catégorie à partir de laquelle les données doivent être copiées. |
| Vider après la copie | Cochez cette case pour supprimer les données de la Catégorie source après la copie. |
| Catégorie cible | Catégorie vers laquelle les données doivent être copiées. |
| Date de début | Date de début pour coller les données de la période cible.|

Cliquez sur le bouton *OK*{:.doc-button} pour confirmer votre sélection ou sur *Annuler*{:.doc-button}.

#### Supprimer le contenu d'une Catégorie

Pour effectuer cette opération, sélectionnez la Période de planification souhaitée dans la vue d'ensemble et appuyez sur *Supprimer*{:.doc-button} dans le bloc Catégorie. Vous devez définir les paramètres suivants :

| Paramètre | Description |
| ------- | ------- |
| Date de début | Date de début de la période concernée (qui peut être différente mais comprise dans la Période de planification). |
| Date de fin | Date de fin de la période concernée (qui peut être différente mais comprise dans la Période de planification). |
| Sélection des employés | - Tous : Permet de sélectionner tous les Employés de l'Unité opérationnelle pour la période concernée.<br />- Groupe : Permet de sélectionner un ou plusieurs Groupes de l'Unité opérationnelle pour la période concernée.<br />- Employé : Permet de sélectionner un ou plusieurs Employés de l'Unité opérationnelle pour la période concernée.|
| Liste des groupes | Si vous avez sélectionné l'option `Groupe`, choisissez ici un ou plusieurs Groupes pour l'échange d'Activités. Pour sélectionner plusieurs Groupes, maintenez la touche `Ctrl` enfoncée tout en les sélectionnant.|
| Liste des employés| Si vous avez sélectionné l'option `Employé`, choisissez ici le ou les Employés pour l'échange d'Activités. Pour sélectionner plusieurs Employés, maintenez la touche `Ctrl` enfoncée tout en les sélectionnant.|
| Catégorie | Catégorie dans laquelle les données doivent être supprimées. |

Cliquez sur le bouton *OK*{:.doc-button} pour confirmer votre sélection ou sur *Annuler*{:.doc-button}.
