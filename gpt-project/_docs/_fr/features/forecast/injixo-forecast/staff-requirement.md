---
title: Besoin en personnel
redirect_from:
  - /fr/besoin-en-personnel/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-backoffice-linear.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-asa.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-abandoned-calls.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-outbound.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/employee-requirement.md
---

Forecast vous permet de calculer automatiquement le besoin en personnel de tous vos canaux. La méthode utilisée dépend du type d'opérations. Les méthodes de calcul disponibles dans Forecast sont :

- Erlang C (Workloads basés sur des appels avec un objectif de Qualité de Service)
- Chat (Workloads basés sur le chat avec un objectif de Qualité de Service)
- Productivité (pour tous types d'opérations sans objectif de Qualité de Service)

### Paramètres de calcul

_Editer la méthode de calcul_{:.doc-button} en bas de la page Workload vous permet de définir les paramètres de la méthode de calcul ou la modifier.
Vous trouverez les détails sur les paramètres à définir {% link_new ici | features/forecast/injixo-forecast/staff-requirement-parameters.md %}.

### Calcul du besoin en personnel

Le besoin en personnel est calculé automatiquement sur la base des données prévisionnelles (volume et TMT) et des paramètres définis.
Il est recalculé à chaque modification de paramètre ou si vous effectuez des {% link_new ajustements manuels | features/forecast/injixo-forecast/manual-adjustments.md %}.

### Affichage du besoin

Le besoin en personnel est affiché sous forme de graphique en bas de la page du Workload. Il est disponible dans les vues jour, semaine et mois.
Vous pouvez basculer entre les {% link_new Versions | features/forecast/injixo-forecast/store-forecast-versions.md %} _Auto-Forecast_, _Opérationnel_ ou _Stratégique_.
La **Qualité de Service**, le **Shrinkage** et le **total des heures-homme** requis sur la journée sont affichés au-dessus de ce graphique.
Le détail complet par intervalle (besoin en personnel, volume et TMT) est visible lorsque vous positionnez le curseur dessus.

{{ 1 | image: "Graphique du besoin en personnel" }}

### Utiliser le besoin en personnel

Vous pouvez utiliser le besoin en personnel pour votre planification en sélectionnant la Version de votre choix puis en cliquant sur _Utiliser le besoin_{:.doc-button}.

### Multi-activités, appels sortants et besoin constant

Pour utiliser ces différentes méthodes, cliquez sur **Scripts de calcul du besoin pour les multi-activités, le besoin constant et les appels sortants**. Dans la liste déroulante, sélectionnez la méthode de calcul, puis saisissez les paramètres et cliquez sur _OK_{:.doc-button}. Le résultat du calcul s'affiche et est également disponible dans le menu _WFM > Planification > SchedulePro > Besoin en personnel_{:.breadcrumbs}.

> Remarque
>
> Avant de calculer le besoin d'une multi-activité, cliquez sur _Utiliser Forecast_{:.doc-button} pour exporter la prévision de chaque sous-activités. Utilisez ensuite la version Auto-Forecast dans le script de calcul du besoin.
