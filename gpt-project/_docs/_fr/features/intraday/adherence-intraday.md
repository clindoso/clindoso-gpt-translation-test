---
title: Adhérence Intrajournalière
toc: true
product_label:
  - advanced
  - enterprise
description: Intraday vous permet d’avoir une vue d’ensemble de l’adhérence des employés à leur planning au cours d’une journée.
archive_ref: 20210422-de-adherence
---

L’Adhérence Intrajournalière vous permet de comparer les activités planifiées des employés avec les activités réelles afin d’identifier les périodes de dépassement tout au long de la journée.

L’Adhérence Intrajournalière affichera les données une fois que vous aurez configuré l’{% link_new import des statuts agent en temps réel | features/acd-integration/cloud/import-agent-status-data.md %}.

Vous débutez avec l’Adhérence Temps Réel&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/intraday/real-time-adherence.md %}.

## Afficher et rechercher des données

1. Accédez à _Intraday > Adhérence intrajournalière_{:.breadcrumbs}
2. Pour afficher les données agent, sélectionnez une **unité opérationnelle** et/ou un **groupe**.
3. Pour changer le jour affiché, cliquez sur _Aujourd’hui_{:.doc-button} ou _Hier_{:.doc-button} ou sélectionnez une date.

Le tableau affiche les détails des écarts par employé. Dans l'en-tête du tableau, vous pouvez identifier les périodes de faible adhérence. Vous pouvez trier le tableau ou utiliser le champ de recherche en haut du tableau pour filtrer la vue. En savoir plus sur les {% link_new filtres et le tri | features/intraday/real-time-adherence.md | #recherche-et-filtre %}.

{{ 1 | image: 'Adhérence Intrajournalière','100%' }}

> Limiter la vue pour certains employés à certains utilisateurs
>
> Configurez les droits sur certaines unités opérationnelles ou certains groupes par {% link_new utilisateur ou rôle utilisateur | getting-started/configure-user-roles.md | #-définir-les-droits-sur-wfm %}.

## Score d’adhérence

Le score indique les éventuels écarts entre les activités planifiées et effectuées par les employés.

Vous pouvez analyser l’adhérence au cours de la journée à l’aide du graphique. Si la journée n’est pas terminée, le score est calculé jusqu’à la date et l’heure de la dernière mise à jour, affichée au-dessus du score d'adhérence.

L'objectif d'adhérence est indiqué par la ligne en pointillés. Vous pouvez {% link_new ajuster l'objectif | features/intraday/real-time-adherence.md | #modifier-lobjectif-dadhérence %}.

{{ 2 | image: 'Score d’adhérence','100%' }}

## Tableau d’adhérence agent

Ce tableau affiche les informations d’adhérence pour les employés planifiés sur la journée en cours. Vous pouvez trier les colonnes par nom de l’employé et par score d'adhérence.

Chaque ligne du tableau contient l’historique de la journée d’un employé. Vous pouvez voir les différences entre les activités planifiées et réelles d’un employé. Un score d'adhérence individuel est attribué à chaque employé. Les scores individuels s’ajoutent au score total de l’unité opérationnelle (affichée dans l’en-tête du tableau). Les écarts sont mises en évidence lorsque le score est inférieur à  {% link_new l’objectif d’adhérence configuré | features/intraday/real-time-adherence.md | #modifier-lobjectif-dadhérence %}.

Les couleurs représentent trois types d’écarts&nbsp;:

- Non présent (rouge),
- Activité incorrecte (jaune),
- Non planifié (bleu).

Cliquez sur le nom d’un employé pour voir son {% link_new adhérence intrajournalière | features/intraday/adherence-intraday.md | #adhérence-intrajournalière-agent %}. Les {% link_new Matches | features/intraday/adherence-matches.md %} et le {% link_new seuil de tolérance | features/intraday/real-time-adherence.md | #seuil-de-tolérance %} influencent les changements de statut et le type d’adhérence. En savoir plus sur les {% link_new statuts et les types d’activité | features/intraday/real-time-adherence.md | #statut %}.

{{ 3 | image: 'Tableau d’adhérence agent','100%' }}

## Adhérence intrajournalière agent

La vue Adhérence intrajournalière agent permet d’obtenir des informations détaillées sur les incidents d’adhérence.




 Vous pouvez voir à quel moment les employés n’ont pas adhéré à leur planning. Pour comprendre les tâches effectuées par un employé pendant la journée, cliquez sur une entrée du planning. La vue affichera les activités individuelles à l’aide du code couleurs configuré.

Dans l’historique, vous pouvez comparer les activités planifiées et effectuées et voir les statuts en dépassement. Le tableau ci-dessous continent une ligne pour chaque période de dépassement.

Pour changer la journée affichée, vous pouvez utiliser&nbsp;:

- le **sélecteur de mois** en haut de la page et la **vue d’ensemble journalière** à gauche,
- les **flèches de navigation** à côté de la date en cours au-dessus du tableau.

La vue d’ensemble journalière affiche le score d’adhérence pour chaque jour du mois sélectionné. Au-dessus de la vue d’ensemble journalière, vous pouvez voir différents indicateurs pour le mois sélectionné&nbsp;; par exemple, le score d’adhérence ou la durée planifiée.

{{ 4 | image: 'Détails Adhérence Intrajournalière Agent','100%' }}

## Rapport d’adhérence (fichier CSV)

Dans certains cas, vous pouvez avoir besoin d’analyser les données d’adhérence aux activités et au temps de travail pour des employés sur une période plus longue, par exemple pour calculer les paiements de bonus. Le rapport d’adhérence est un fichier CSV qui inclut des données d’adhérence agrégées pour les activités et le temps de travail. Pour le télécharger, suivez ces étapes&nbsp;:

1. Accédez à _Intraday > Adhérence Intrajournalière_{:.breadcrumbs}.
2. Sélectionnez au moins une unité opérationnelle et/ou un groupe.
3. Cliquez sur _Télécharger le rapport_{:.doc-button}.  
   Une fenêtre s’ouvre.
4. Sélectionnez une plage de dates pour le rapport. Vous pouvez sélectionner n’importe quelle plage de dates, pouvant aller d’un jour à six mois dans le passé.
5. Cliquez sur _Télécharger le rapport_{:.doc-button}.

Le tableau ci-dessous explique les colonnes du rapport.

| Colonne             | Explication                                                                     | Calcul                                                                |
| ------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Minutes in adherence | Minutes en adhérence (activités)&nbsp;: temps passé sur les activités conformément au planning      | -- |
| Minutes out of adherence  | Minutes en dépassement (activités)&nbsp;: temps passé sur des activités non conformes au planning        | -- |                  
| Adherence in %   | Adhérence (activités) en %&nbsp;: pourcentage du temps de travail passé sur les activités conformément au planning       | Minutes en adhérence (activités)/minutes planifiées * 100% |
| Minutes out of conformance  | Minutes en dépassement (temps de travail)&nbsp;: différence entre le temps de travail effectif et planifié             | Minutes de travail effectives - minutes planifiées |
| Conformance in % | Adhérence (temps de travail)&nbsp;: pourcentage du temps de travail en adhérence par rapport au temps de travail planifié | Temps effectif/temps planifié * 100&nbsp;% |
| Scheduled in %  | Planifié en %&nbsp;: pourcentage du temps de travail planifié pour une activité d'un certain type | Temps planifié pour le type d’activité pertinent / temps total planifié * 100&nbsp;%              |
| Actual in %  | Effectif en %&nbsp;: pourcentage du temps de travail effectif planifié pour une activité d'un certain type | Temps effectif pour le type d’activité pertinent / temps total effectif * 100&nbsp;%              |

Chaque ligne de données comprend un lien pour afficher les données associées dans _Intraday > Adhérence Intrajournalière_{:.breadcrumbs}.

## Foire aux questions

| Question                            | Réponse                                                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Pourquoi certains ou tous les employés sont-ils absents&nbsp;? | Essayez d’effacer le champ de recherche. Vérifiez si les employés que vous recherchez sont planifiés aujourd’hui dans l'unité opérationnelle ou le groupe sélectionné.           |
| Pourquoi ne puis-je pas sélectionner de date spécifique&nbsp;? | Vous pouvez accéder aux données d’adhérence historiques des six derniers mois précédant la date actuelle, ainsi que du mois en cours (par exemple, si la date actuelle est le 15 juillet, vous pouvez sélectionner des dates entre le 1er janvier et le 15 juillet). |
