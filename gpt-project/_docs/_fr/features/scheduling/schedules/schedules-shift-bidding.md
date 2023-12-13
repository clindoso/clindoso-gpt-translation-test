---
title: Génération de missions
product_label:
  - advanced
  - enterprise
description: Définissez les horaires disponibles pour la génération de missions, invitez les conseillers à choisir leurs missions, effectuez un tirage au sort et publiez le planning (fonctionnalité Schedules).
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/employee-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/view-approve-shift-swap-requests.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/notifications.md
---

La génération de missions permet aux personnes de votre organisation de participer au processus de planification en plaçant des demandes sur les missions disponibles. Pour commencer, définissez une période de planification et générez les missions.

## Le processus de génération de missions

Avant de lancer le processus de génération de missions, vous devez {% link_new calculer le besoin en personnel | features/forecast/injixo-forecast/staff-requirement.md %} et éventuellement {% link_new insérer des rotations d’horaires | features/administration/shift-sequences.md %}.

1. Dans Schedules, créez une {% link_new période de planification | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #créer-une-nouvelle-période-de-planification %} avec le statut Non publié.
2. Entrez les valeurs maximum et minimum pour chaque modèle horaire dans le tableau de besoin en personnel.
3. [Générez les missions](#générer-les-missions).
4. Invitez les conseillers à [demander des missions dans injixo Me](#inviter-les-conseillers-à-demander-des-missions).
5. Si la période de génération de missions est terminée, lancez le [tirage au sort](#lancer-le-tirage-au-sort) et [assignez les missions restantes](#attribuer-les-missions-restantes) (qui n’ont pas été demandées).
6. [Optimisez les activités et les pauses, et publiez le planning](#optimiser-et-publier-le-planning).

## Spécifiez les différentes missions

Avant de créer les missions qui seront disponibles pour les conseillers, déterminez quels types de missions vous souhaitez. Vous devez ajuster les valeurs pour chaque période de planification avant de commencer la génération de missions. Sinon, injixo ne créera pas les bonnes missions pour couvrir les besoins en personnel.

1. Accédez à _Plan > Schedules_{:.breadcrumbs}.
2. Cliquez sur _Périodes de planification_{:.doc-button}.
3. Pour ajuster le besoin en personnel, faites passer votre curseur sur la **période de planification**, puis cliquez sur l'{% icon ellipsis_v %} à droite.
4. Sélectionnez _Ajuster le besoin en missions_{:.doc-button} depuis le menu.
5. Dans le tableau du besoin en personnel, {% link_new entrez les valeurs **Min** et **Max** | features/scheduling/schedules/schedules-shift-requirement.md | #saisir-un-besoin-en-missions %} pour vos modèles horaires.

## Générer les missions

Le processus de génération de mission crée des missions pour chaque jour de la période de planification. injixo prend en compte à la fois les missions existantes dans le planning et le besoin en personnel pour créer la meilleure couverture possible.

1. Accédez à _Plan > Schedules_{:.breadcrumbs}.
2. Cliquez sur _Périodes de planification_{:.doc-button}.
3. Faites passer votre curseur sur la Période de planification pour laquelle vous souhaitez générer les missions et cliquez sur l'{% icon ellipsis_v %} à droite.
4. Sélectionnez _Générer les missions_{:.doc-button} depuis le menu.
   {{ 1 | image: 'Périodes de planification avec fonctions de missions', '50%' }}
5. (Facultatif) Modifiez la valeur **Besoin en missions**.

   - Option **du besoin en personnel**&nbsp;: avec une valeur de 100&nbsp;%, injixo couvrira exactement 100&nbsp;% du besoin en personnel. Une valeur supérieure à 100&nbsp;% créera plus de missions que requises par le besoin en personnel. Une valeur inférieure à 100&nbsp;% créera moins de missions (ce paramètre est utile lorsque le nombre de conseillers est trop faible pour couvrir le besoin).
   - Option **des heures contractuelles**&nbsp;: avec une valeur de 100&nbsp;%, injixo s’assurera que toutes les heures contractuelles des conseillers sont couvertes par les missions générées.

6. Pour lancer la génération de missions, cliquez sur _Générer les missions_{:.doc-button}.  
    Une fois la génération de missions terminée, vous pouvez accéder aux résultats dans JobProcessor. Le rapport contient des informations sur les informations saisies et le résultat.

   {{ 2 | image: 'Fenêtre des paramètres pour la génération de missions', '50%' }}

Remarque&nbsp;: dans le Centre de planification, vous pouvez remplacer le résultat de la génération de missions en modifiant le nombre de missions générées pour une seule journée, par exemple pour modifier un seul jour.

Le Centre de planification affiche les chiffres clés en rapport avec la génération de missions. Vous les trouverez dans la {% link_new fenêtre des paramètres | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %} au bas de la page&nbsp;:

- Besoin (dans l’onglet Modèles horaires)&nbsp;: nombre de missions générées pour chaque modèle horaire.
- Occupation par rapport au besoin en missions (dans l’onglet Activités)&nbsp;: nombre de missions générées pour l’activité sélectionnée
  <!-- You can also rate the quality of a shift generation, as you can see here how the employee requirement would be covered if all generated shifts were staffed. -->
- Couverture par rapport au besoin en missions (dans l’onglet Activités)&nbsp;: différence entre les missions requises et générées

## Inviter les conseillers à demander des missions

Après avoir généré les missions, suivez ces étapes&nbsp;:

1. Modifiez le **statut** de la {% link_new période de planification | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #statut %} sur Missions disponibles.  
   Les conseillers recevront une [notification](#notifications-par-e-mail-et-push-sur-navigateur).
2. (Facultatif) Ajoutez une **date limite** jusqu’à laquelle les conseillers peuvent proposer leurs missions.  
   Les conseillers placent une première et une seconde demande sur chaque journée. Tous les conseillers peuvent demander la même mission.  
   Pour estimer la probabilité d’obtenir la mission demandée et, si nécessaire, de trouver d’autres missions, les conseillers peuvent voir combien de missions sont nécessaires et à quelle fréquence une mission a déjà été demandée.

   > Les demandes dans injixo Me sont limitées à 100 jours maximum à l’avance (pour les périodes de planification > 100 jours).

3. Lorsque la période de demande est terminée (ou que la date limite est passée), changez à nouveau le **statut** sur Non publiée.

Pour voir les demandes des conseillers, accédez à Schedules ou au Centre de planification et ajoutez la catégorie Desiderata ou Desiderata de réserve à votre vue. Pour en savoir plus sur l’ajout de ces catégories, consultez nos articles sur le {% link_new Centre de planification | features/scheduling/shiftcenter/shift-center-overview.md | #choose-the-time-range-and-levels %} et {% link_new Schedules | features/scheduling/schedules/schedules-overview.md | #catégories %}. 

## Lancer le tirage au sort

Lorsque la période de demande est terminée, planifiez les demandes des conseillers à l’aide du tirage au sort. Il copiera les missions demandées depuis la catégorie Desiderata et Desiderata de réserve dans la catégorie Planning.

> Avant de lancer à nouveau la génération de missions, {% link_new sauvegardez toutes les demandes de mission | features/scheduling/schedules/schedules-copy-level-content.md %} dans une catégorie non utilisée, par exemple Version 1. 
>
> Une nouvelle génération de mission effacera toutes les demandes envoyées depuis les catégories Desiderata et Desiderata de réserve.

Conseil&nbsp;: si certains conseillers doivent avoir des chances plus élevées d’obtenir les missions demandées, lancez le tirage au sort par groupe. Modifiez l’ordre des groupes dans chaque période de planification pour garantir la juste répartition sur une long période.

Pour lancer le tirage au sort, suivez les étapes ci-dessous&nbsp;:

1. Accédez à _Plan > Schedules_{:.breadcrumbs}.
2. Cliquez sur _Périodes de planification_{:.doc-button}.
3. Faites passer votre curseur sur la **Période de planification** pour laquelle vous souhaitez générer les missions et cliquez sur l'{% icon ellipsis_v %} à droite.
4. Sélectionnez _Tirage au sort_{:.doc-button} dans le menu qui apparaît.
5. (Facultatif) Sélectionnez l’option **Tenir compte de l'heure moyenne de début des autres horaires** et entrez une valeur d’Écart (format hh:mm).
   - Si elle est activée, injixo prend en compte l’heure de début (moyenne) de la mission. Pour en savoir plus, lisez la section sur le [fonctionnement du paramètre Écart](#sélectionner-le-bon-paramètre-décart).
   - Si elle n’est pas activée, les conseillers peuvent obtenir des missions dont le début est aléatoire.
     {{ 3 | image: 'Fenêtre des paramètres du tirage au sort', '50%' }}
6. Pour sélectionner tous les conseillers, cochez la **case** du haut. Vous pouvez filtrer la liste par groupe ou filtre avancé et sélectionner des personnes unes par unes.
7. Cliquez sur _Démarrer le tirage au sort_{:.doc-button}.  
   Une fois le tirage au sort terminé, vous pouvez consulter le statut et le résultat du tirage au sort dans JobProcessor. Le rapport inclut les raisons pour lesquelles une demande n’a pas été planifiée, ainsi que les quotas journaliers et totaux du tirage au sort en pourcentage.

## Attribuer les missions restantes

Une fois que le tirage au sort a attribué les missions, il reste souvent des missions non assignées et non demandées. Dans cette étape, les missions seront attribuées aux personnes qui n’ont reçu aucune missions ou un nombre insuffisant de missions.

1. Accédez à _Plan > Schedules_{:.breadcrumbs}.
2. Cliquez sur _Périodes de planification_{:.doc-button}.
3. Faites passer votre curseur sur la **Période de planification** pour laquelle vous souhaitez générer les missions et cliquez sur l'{% icon ellipsis_v %} à droite.
4. Sélectionnez _Attribuer les missions_{:.doc-button} depuis le menu qui s’affiche.
5. (Facultatif) Sélectionnez l’option **Tenir compte de l'heure moyenne de début des autres horaires** et entrez une valeur d’Écart (format hh:mm).
   - Si elle est activée, injixo prend en compte l’heure de début (moyenne) de la mission. Pour en savoir plus, lisez la section sur le [fonctionnement du paramètre Écart](#sélectionner-le-bon-paramètre-décart).
   - Si elle n’est pas activée, les conseillers peuvent obtenir des missions dont le début est aléatoire.
     {{ 4 | image: 'Paramètres d’attribution des missions', '45%' }}
6. Pour sélectionner tous les conseillers, cochez la **case** du haut. Vous pouvez également filtrer la liste par groupe ou filtre avancé et sélectionner des personnes unes par unes.
7. Cliquez sur _Attribuer les missions_{:.doc-button}.  
   Une fois la mission attribuée, vous pouvez accéder au rapport dans _WFM > Administration > Système > JobProcessor_{:.breadcrumbs}, qui liste les missions attribuées et non attribuées.

Veuillez remarquer que le planning peut rester incomplet une fois le processus terminé, par exemple s’il manque des personnes ou des compétences, ou encore si l’attribution d’une mission enfreint une règle de planification. Vous pouvez modifier votre configuration et lancer à nouveau le processus ou modifier votre planning manuellement.

Conseil&nbsp;: au lieu d’attribuer des missions, vous pouvez également optimiser le planning pour assigner plus de missions et compléter le planning.

### Sélectionner le bon paramètre d’écart

Le calcul du début de la mission selon la valeur du paramètre Écart fonctionne différemment avec ou sans les missions planifiées (par exemple à partir des rotations d’horaires)&nbsp;:

- Avec des missions&nbsp;: injixo calcule l’heure de début moyenne des missions, puis assigne les missions en prenant en compte l’écart maximal défini. Par exemple, si les missions existantes commencent à 8h00 et à 12h00, la moyenne est 10h00. Lorsque vous définissez une valeur d’écart d’une heure, les autres missions peuvent commencer entre 9H00 et 11h00.
- Sans missions&nbsp;: la première mission assignée détermine l’heure de début de la mission. Par exemple, si la première mission commence à 9h00 et que vous définissez la valeur d’écart sur 1 heure, les autres missions commenceront entre 8h00 et 10h00.

## Optimiser et publier le planning

Pour optimiser les activités planifiées et les pauses, {% link_new Optimisez les activités | features/scheduling/schedules/schedules-job-optimization.md %} pour la période de planification.

Pour {% link_new publier le planning | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} et permettre aux conseillers d’échanger des journées, définissez le **statut** de la {% link_new période de planification | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #statut %} sur Publiée. Si vous avez configuré la {% link_new bourse d’échange | features/scheduling/view-approve-shift-swap-requests.md %}, les conseillers peuvent voir leurs missions et les {% link_new échanger avec leurs collègues | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.

## Notifications par e-mail et push sur navigateur

Si vous modifiez le statut d’une période de planification, injixo enverra des notifications par e-mail et sur navigateur pour informer les conseillers de l’unité opérationnelle des changements de date et leur rappeler de demander des missions.

Les utilisateurs doivent activer les {% link_new notifications push | getting-started/notifications.md %} sur leur navigateur. Par défaut, votre tenant enverra des notifications par e-mail et sur navigateur.
