---
title: Génération de missions
redirect_from:
  - /fr/generation-missions/
redirect_reason: Updated filename on 21 April 2022
---

La Génération de missions est une méthode de planification permettant à vos Employés de participer à l'élaboration de leur planning en s'inscrivant aux horaires (missions) de leur choix. Les missions sont générées pour couvrir le besoin en personnel calculé lors du dimensionnement. Les desiderata des Employés sont ensuite traités manuellement ou automatiquement lors de l'étape finale.

{{ 1 | image: "Période de planification" }}

## Création des missions

Le processus de création génère des missions pour chaque jour de la Période de planification concernée.

Le système détermine le nombre de Modèles horaires requis pour que le besoin issu du processus de dimensionnement soit couvert le mieux possible.

La Génération de missions est un processus basé sur le besoin et non sur les Employés. Alors que le moteur d'optimisation utilise tous les Employés disponibles pour construire les plannings, la Génération de missions quant à elle essaie de couvrir le mieux possible le besoin à l'aide des Modèles horaires disponibles.

Les Rotations d'horaires déjà insérées et les Activités déjà inscrites manuellement dans les plannings sont prises en compte pour générer les missions. La Génération de missions n'utilise que les Modèles horaires sur lesquels un Besoin en missions à été renseigné.

La Génération de missions ne peut être exécutée que pour une Unité opérationnelle à la fois (ou un Groupe) et est exécutée en cliquant sur le bouton *Générer*{:.doc-button} du bloc `Missions` à droite de l'écran. La Génération des missions est disponible uniquement pour les Périodes de planification de type *Standard*.

> Remarque
>
> La Génération de missions est un processus complexe et, lors du traitement, une optimisation des tâches et des pauses est déjà réalisée en arrière plan. Le temps de calcul dépend donc de la quantité de données à traiter et de la complexité de l'optimisation.
> 
> Les plannings sont verrouillés lors de la Génération de missions sur la période concernée, vous ne pouvez donc pas les modifier lors de ce processus.

{{ 2 | image: "Paramètres de la Génération de missions", '50%' }}

Sélectionner la Période de planification concernée puis cliquer sur *Générer*{:.doc-button} dans le bloc `Missions`.

Par défaut, les dates de début et de fin affichées sont celles paramétrées pour la Période de planification. Elles peuvent être modifiées si besoin.

Saisissez le pourcentage du **Besoin en personnel** que vous souhaitez couvrir à l'aide de la Génération de missions. Vous pouvez renseigner une valeur supérieure à 100% si vous souhaitez par exemple anticiper le Shrinkage (absentéisme,...). De la même façon, vous pouvez saisir une valeur inférieure à 100% si vous savez d'ores et déjà que vous êtes en sous-effectif sur la période concernée.

Les 2 options **du besoin en personnel** et **des heures contractuelles** permettent de définir sur quelle base ce pourcentage est appliqué.

Cliquer sur *OK*{:.doc-button} pour confirmer la saisie et démarrer la Génération de missions. Vous pouvez fermer la boite de dialogue, le processus continuera en tâche de fond.

### Résultat

En cochant la case *Afficher le résultat du traitement*{:.menu-item} un rapport PDF s'affiche à la fin du processus. Ce rapport contient :

- **Vérification des données de base** liste les données initiales (Unité opérationnelle, Modèles horaires) et recense si des erreurs sont survenues.
- **Informations sur l'optimisation** indique le temps total du traitement et le nombre d'itérations réalisées.
- **Informations sur l'export** détaille le temps de chargement des données vers le Centre de planification.
- **Vérification du résultat** indique pour chaque jour de la Période de planification si le processus s'est déroulé correctement et si des erreurs sont survenues.

## Tirage au sort

Cette option permet d'attribuer de façon aléatoire les horaires aux Employés si le nombre d'inscrits est supérieur au Besoin en missions.

Lors de ce tirage au sort, le Modèle horaire sur lequel s'est inscrit l'Employé est copié depuis la catégorie `Desiderata` ou `Desiderata de réserve` vers la catégorie `Planning`.

Pour tirer au sort les missions, sélectionner la Période de planification concernée et cliquer sur *Tirer au sort*{:.doc-button}. La boite de dialogue suivante s'ouvre.

{{ 3 | image: "Paramètres du Tirage au sort", '50%' }}

### Fonctionnement du tirage au sort

Si la case **Créer un protocole de Tirage au sort** est cochée un rapport PDF s'ouvre à la fin du processus. Ce rapport contient :

- **Paramètres du protocole** liste les paramètres affichés : l'utilisateur, l'Unité opérationnelle, la date de début et la date de fin.

- **Employés concernés par le Tirage au sort** affiche le Matricule, l'Employé, le Compte temps dû et le nombre d'heures assignées.

- **Desiderata normaux** (1er choix de l'Employé) fournit des informations sur les Missions tirées au sort et les raisons pour lesquelles d'autres n'ont pu être attribuées. Les informations affichées sont : l'heure de début de la Mission, le nom de la Mission, le Besoin en personnel, l'Occupation, le Matricule, l'Employé concerné, la Mission assignée, l'ID du motif du refus et le motif du refus.

- **Desiderata de réserve** (2ème choix de l'Employé) fournit les mêmes informations que la section précédente mais pour les Desiderata de réserve.

- **Résultat du tirage au sort par Employé** détaille la date du Desiderata ou de l'attribution, le type de Desiderata, l'heure de début de la Mission, la Mission désirée et le pourcentage journalier de Desiderata exaucés. La dernière ligne de cette section affichera le pourcentage total de Desiderata exaucés pour tous les Employés.

## Attribution

Cette option attribue les missions pour lesquelles il n'y a pas eu suffisamment de Desiderata exprimés par les Employés permettant de couvrir le Besoin en missions.

Les missions attribuées sont visibles dans la Catégorie `Planning` du Centre de planification.

Pour lancer le processus d'attribution, sélectionner la Période de planification concernée et cliquer sur *Attribuer*{:.doc-button}.

Sélectionner ensuite les Employés concernés.

{{ 4 | image: "Paramètres de l'Attribution de missions", '50%' }}

### Fonctionnement de l'attribution

Si la case **Créer un protocole d'attribution** est cochée un rapport PDF s'ouvre à la fin du processus. Ce rapport contient :

- **Paramètres du protocole d'attribution** liste les paramètres tels que l'utlisateur, l'Unité opérationnelle, la date de début et la date de fin.

- **Employés concernés par l'attribution de Missions** affiche le Matricule, l'Employé, le Compte temps dû et le nombre d'heures assignées.

- **Résultat de l'attribution** fournit des informations sur les Missions attribuées et les raisons pour lesquelles d'autres n'ont pu l'être. Les informations affichées sont : l'heure de début de la Mission, le nom de la Mission, le Besoin en personnel, l'Occupation, le Matricule, l'Employé concerné, la Mission assignée, l'ID du motif du refus et le motif du refus.

## Paramètres

Dans cette section vous trouverez le détails des paramètres à renseigner pour le *Tirage au sort*{:.doc-button} ou l'*Attribution de Missions*{:.doc-button} car ceux-ci sont identiques.

Dates : Par défaut, les dates de début et de fin de la Période de planification sont renseignées. Vous pouvez si vous le souhaitez limiter le processus à une période comprise dans la Période de planification.

Employés : vous pouvez choisir d'appliquer le processus à tous les Employés, un ou plusieurs Groupes ou même sélectionner les Employés individuellement dans la liste.

Cocher la case **Créer un protocole de Tirage au sort** pour qu'un rapport soit généré à la fin du processus.

Cocher la case **Prendre en compte un créneau horaire pour le début de la mission** pour définir une `Tolérance` sur le début de la mission (au format hh:mm). La valeur définit si la mission peut ou non dévier du Desiderata de l'Employé et empêche ainsi le système d'attribuer une mission trop éloignée de la première attribuée.

La valeur sera utilisée de 2 manières différentes selon que les missions aient été ou non déjà insérées dans le planning.

1\. Si aucune mission n'a été insérée dans le planning de l'Employé sur la Période de planification, la valeur sera prise en compte pour toutes les missions suivant la première mission attribuée. Par exemple, si la première mission débute à 9h et que la tolérance est de 1h, les suivantes débuteront entre 8h et 10h.

2\. Si des missions ont déjà été attribuées sur la Période de planification, une heure de début moyenne sera définie et utilisée pour appliquer la tolérance.

Sélectionner les paramètres souhaités et cliquer sur *OK*{:.doc-button} pour démarrer le processus.

> Remarque
>
> Avant l'exécution d'un des processus ci-dessus, nous vous conseillons d'analyser la couverture du Besoin en missions à partir des données déjà renseignées dans le *Centre de planification*{:.menu-item} (Desiderata, Desiderata de réserve et Modèles horaires).
