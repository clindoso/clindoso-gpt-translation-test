---
title: Ajuster aux horaires d’ouverture
product_label:
  - advanced
  - enterprise
  - classic
toc: false
description: Découvrez comment activer les heures d’ouverture et leur impact sur les prévisions.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Vous débutez avec injixo Forecast&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

Par défaut, les workloads ne prennent pas en compte les horaires d’ouverture et les prévisions prennent en compte l’ensemble des volumes sur toute la journée.

injixo Classic supporte uniquement les horaires d’ouverture pour les workloads Smart.

## Quel est l’impact des horaires d’ouverture sur le calcul de la prévision&nbsp;?

Si vous activez les horaires d’ouverture sur un workload, injixo&nbsp;:

- superpose les horaires d’ouverture de l’unité opérationnelle et de l’activité assignée. Tout intervalle compris dans cette période est comptabilisé comme intervalle ouvert.
- redistribue tous les volumes non compris dans les horaires d’ouverture sur une période incluse dans les horaires d’ouverture. Le volume total journalier reste le même. La distribution est relative aux valeurs des intervalles existants et suit donc le modèle intra-journalier prévu. Les volumes en dehors des horaires d’ouverture sont supprimés.
- définit les valeurs du temps moyen de traitement prévu en dehors des horaires d’ouverture comme étant égales à 0.

## Ajuster aux horaires d’ouverture

Pour inclure les volumes en dehors des horaires d’ouverture dans le calcul de la prévision, activez les horaires d’ouverture sur chaque workload individuellement.

1. Accédez à _Forecast_{:.menu-item}.
2. Sélectionnez un workload à l’aide des options suivantes&nbsp;:
   - Sélectionnez le workload depuis la liste déroulante en haut de la page.
   - Saissez le nom du workload dans le champ de recherche.
   - Cliquez sur le workload dans la liste.
3. Cliquez sur _Éditer_{:.doc-button}.
4. Sélectionnez une **unité opérationnelle** et une **activité**.
5. Cochez la case **Prévision ajustée aux horaires d’ouverture**.
6. Cliquez sur _Sauvegarder_{:.doc-button}.
   injixo calculera alors une nouvelle prévision. Le calcul peut prendre un certain temps.

Remarque importante&nbsp;: pour garantir le bon calcul de la prévision, paramétrez des horaires d’ouverture et des activités valides dans l’unité opérationnelle sélectionnée pour la prévision. Supprimez ou modifiez les {% link_new champs valide du/jusqu’au | features/administration/set-a-validity-period.md %} si nécessaire.

## Comment s’affichent les horaires d’ouverture&nbsp;?

injixo Forecast affiche les horaires d’ouverture à l’aide d’une barre horizontale orange dans la vue journalière&nbsp;:

{{ 1 | image: "Barre orange indiquant l’activation des horaires d’ouverture dans un workload", '80%' }}

Remarque&nbsp;: des {% link_new droits utilisateur  | getting-started/configure-user-roles.md %} supplémentaires sur l’unité opérationnelle peuvent être nécessaires pour afficher la barre orange indiquant les horaires d’ouverture. Accédez à _WFM > Administration > Système > Droits d’accès des rôles d’utilisateurs_{:.breadcrumbs} et ajoutez des droits sur le calendrier de planification à l’utilisateur ou au groupe d’utilisateurs concerné.
