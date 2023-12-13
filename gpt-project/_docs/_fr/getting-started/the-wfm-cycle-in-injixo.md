---
title: Le cycle du WFM dans injixo
description: Découvrez comment injixo vous soutient tout au long du cycle du WFM.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

L’objectif du Workforce management (WFM) est d’optimiser l’affectation des effectifs pour atteindre les objectifs et les niveaux de service cibles de votre organisation. injixo vous accompagne efficacement tout au long du cycle du WFM.

  {{ 1 | image: "Cycle du WFM: Prévision, Planification, Optimisation des plannings, Gestion intrajournalière, Analyse", '60%' }}

- Prévision&nbsp;: prévoyez votre charge de travail à court, moyen et long terme.
- Planification&nbsp;: décidez des stratégies de recrutement, de budget et de formation à venir.
- Optimisation des plannings&nbsp;: créez les meilleurs plannings possibles pour vos employés, conformément aux exigences de votre entreprise.
- Gestion intra-journalière&nbsp;: adaptez vos plannings aux imprévus en temps réel.
- Analyse&nbsp;: exploitez les données pour comprendre, anticiper et améliorer les performances de votre entreprise.

Dans cet article, découvrez comment injixo vous accompagne tout au long du cycle du WFM.
L'étape initiale consiste à fournir à injixo les données nécessaires pour générer une prévision fiable. Pour ce faire, vous devez configurer une intégration avec vos systèmes de téléphonie (ACD) ou de gestion des relations client (CRM).

Vous débutez dans le WFM&nbsp;? Découvrez les concepts et les définitions clés dans notre [glossaire](https://help.injixo.com/fr/glossary/overview/).

## 1. Prévision

### Configurer une intégration

Pour prédire la charge de travail de votre organisation à tout moment à l’avenir, injixo doit accéder à vos données de contact et/ou aux données de statut agents provenant de systèmes externes (par exemple, ACD ou CRM). Pour permettre à injixo d'importer et de traiter ces données, vous devez {% link_new intégrer vos systèmes externes à injixo | features/acd-integration/cloud/how-integrations-work.md %}. injixo propose des intégrations natives spécifiques aux fournisseurs et des intégrations universelles. En fonction de l’intégration, injixo récupère les données toutes les 15, 30 ou 60&nbsp;minutes (import de données historiques), voire en quelques secondes (import de données en temps réel). 

Une fois que vous avez ajouté une intégration, elle enverra automatiquement les données à injixo, en continu.
Les données de contact importées sont stockées dans des files d’attente, qui sont toujours associées à un canal. Vous avez besoin de files d’attente pour créer des workloads sur lesquels baser vos prévisions.

Vous pouvez configurer vos intégrations dans _Account > Intégrations_{:.breadcrumbs}.

### Créer un workload  

Pour utiliser injixo Forecast, vous devez d’abord {% link_new créer un workload | features/forecast/injixo-forecast/manage-workloads.md | #créer-un-workload %} à l’aide des files d'attente importées par votre intégration. Les workloads contiennent toutes vos données historiques et les prévisions associées. Pour créer un workload, votre ACD doit être correctement connecté et les files d'attente importées doivent être disponibles.

Vous pouvez créer des workloads dans _Forecast > Workloads_{:.breadcrumbs}. 

### Calculer une prévision

{% link_new injixo Forecast | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} combine vos données historiques à l’algorithme le mieux adapté pour générer des prévisions de haute qualité sur une durée pouvant aller jusqu’à 365 jours.

Chaque nouvelle importation de données met à jour la prévision générée. Vous pouvez également {% link_new ajouter des événements | features/forecast/injixo-forecast/events-and-holidays.md %} qui influenceront votre prévision.

### Calculer le besoin en personnel

Une fois que vous avez généré une prévision, vous pouvez {% link_new calculer votre besoin en personnel | features/forecast/injixo-forecast/staff-requirement.md %}, c'est-à-dire le nombre d’employés à planifier pour couvrir la charge de travail prévue. Vous pouvez utiliser plusieurs {% link_new méthodes de calcul | best-practices/requirement-scripts.md %} pour déterminer votre besoin en personnel, qui prennent en compte des facteurs tels que le niveau de service et le temps de réponse cibles, le shrinkage, etc. Vous pouvez également créer un besoin en personnel constant sans prévision, si nécessaire.

Vous pouvez utiliser votre besoin en personnel lors du processus de planification pour créer des plannings optimisés pour des périodes, des unités de planification et des activités spécifiques.

## 2. Planification

Utilisez les données générées par injixo Forecast pour comparer votre besoin en personnel avec les ressources disponibles. La prévision à long terme vous permet de prendre plus rapidement les meilleures décisions, par exemple sur les demandes de congé, la publication d’offres d’emploi ou les programmes de formation que vos employés doivent suivre pour se préparer aux projets à venir.

## 3. Optimisation des plannings

### Créer des plannings

Une fois que vous avez calculé votre besoin en personnel, injixo propose différentes {% link_new méthodes de planification | features/scheduling/scheduling-methods.md %} que vous pouvez choisir ou combiner pour mieux organiser vos ressources et répondre aux besoins de votre organisation.

Dans _Plan > Schedules_{:.breadcrumbs}, vous pouvez configurer des règles et des contraintes de planification pour respecter la réglementation du travail, les accords contractuels et les préférences des employés.

injixo propose plusieurs fonctionnalités de planification, telles que la {% link_new planification optimisée | features/scheduling/schedules/schedules-optimized-schedules.md %}, la {% link_new notification des employés des changements de planning | features/scheduling/schedules/schedules-notify-scheduling-changes.md %}, ou la {% link_new possibilité d'échanger des journées | features/scheduling/planning-periods/enable-employees-to-swap-shifts.md %} entre collègues.

### Prévision des absences

{% link_new Congés/Absences | features/scheduling/time-off/vacation-absences-management.md %} vous permet de gérer les soldes de congés et les demandes de congés pour les vacances, les jours de repos, les congés maladie et autres types d'absences. Les employés peuvent soumettre leurs demandes de congé via {% link_new injixo Me | features/injixo-me/use-injixo-me/explore-injixo-me.md %}. Vous pouvez approuver ou rejeter les demandes en fonction du besoin en personnel, de la disponibilité des employés et de règles ou contraintes prédéfinies.

Configurez les congés dans _Plan > Congés/Absences_{:.breadcrumbs}.

## 4. Gestion intrajournalière

Dans {% link_new Adhérence Intrajournalière | features/intraday/adherence-intraday.md %}, vous pouvez comparer les activités prévues avec les activités réelles et identifier les écarts. Vous obtiendrez des statistiques détaillées et un score d’adhérence.

La gestion en temps réel est également possible avec {% link_new Adhérence Temps Réel | features/intraday/real-time-adherence.md %}, qui offre une vue d’ensemble complète, des options de filtrage et un score d'adhérence cible ajustable.

Ces informations vous permettent d’apporter des ajustements à court terme au planning pour faire face aux imprévus et éviter les situations de sous-effectif ou de sureffectif.

## 5. Analyse
 
injixo vous permet de {% link_new créer des tableaux de bord | features/monitoring/dashboards/dashboards-overview.md %} contenant des graphiques pour mieux visualiser différents indicateurs, par exemple une comparaison des besoins en personnel et de la couverture réelle, ou des appels entrants prévus par rapport aux appels réels pour différentes séries temporelles.

injixo peut également {% link_new générer plusieurs types de rapports | features/reporting/standard-reports/creating-reports.md %} qui vous aident à garder une visibilité  sur les indicateurs pertinents, telles que la capacité selon le type de contrat, le temps de travail par unité opérationnelle ou un aperçu des congés.
