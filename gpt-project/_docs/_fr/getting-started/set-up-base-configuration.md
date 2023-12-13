---
title: Configuration minimale
description: Données de configuration requises pour créer un planning.
redirect_from:
  - /fr/configuration-hints/
  - /fr/quickstart-base-configuration/
redirect_reason: Updated filename on 24 July 2023
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
---

Avant de commencer la planification, vous devez paramétrer la configuration minimale dans injixo. Certains éléments de la configuration minimale sont indispensables pour créer un planning, tandis que d’autres sont facultatifs, en fonction des {% link_new méthodes de planification | features/scheduling/scheduling-methods.md %} que vous souhaitez utiliser.

## Ordre de configuration

Nous vous recommandons de définir les éléments de configuration dans l’ordre présenté dans la section suivante. Les éléments de configuration sont interdépendants et peuvent être assignés les uns aux autres. Suivez les liens dans le tableau pour en savoir plus sur chaque élément de configuration et apprendre à les configurer.
Aucune configuration n’est identique, l’ordre optimal de configuration peut donc être différent pour votre organisation. Utilisez cet article pour vérifier que toutes les étapes ont bien été suivies lors de l’onboarding. N’hésitez pas à contacter votre consultant si vous avez des questions.

### Éléments de configuration requis

Le tableau ci-dessous présente un aperçu des éléments de configuration que vous devez configurer dans injixo, indépendamment de la méthode de planification que vous souhaitez utiliser.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Élément de configuration</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Compétences | features/administration/work-with-skills.md %}</td>
      <td>Les compétences représentent les qualifications de vos employés. En attribuant des compétences aux employés, ils deviennent qualifiés pour travailler sur certaines activités. Dans injixo, vous devez attribuer des compétences aux activités sur lesquelles seules certains employés peuvent travailler. Il n’est pas nécessaire d’ajouter des compétences aux activités sur lesquelles tout le monde peut travailler.</td>
    </tr>
    <tr>
      <td>{% link_new Activités | features/administration/activities.md %}</td>
      <td>Les activités sont les tâches, les réunions et les congés à planifier et à suivre dans votre organisation.<br> Les activités sont ajoutées aux modèles horaires et aux unités opérationnelles.</td>
    </tr>
    <tr>
      <td>{% link_new Modèles horaires | features/administration/daymodels/daymodel-creation.md %}</td>
      <td>Les modèles horaires sont des journées types. Les modèles horaires définissent les heures de début et de fin d’une journée, ainsi que le nombre d'heures travaillées par jour par un employé. Ils contiennent toutes les activités de présence, de pause et d’absence dans une journée.<br>Les modèles horaires sont assignés aux unités de planification. Ils peuvent également être regroupés en modèles hebdomadaires (facultatif).</td>
    </tr>
    <tr>
      <td>{% link_new Unités opérationnelles | features/administration/create-and-manage-planning-units.md %}</td>
      <td>Les unités opérationnelles représentent vos sites physiques ou virtuels. Elles sont utilisées pour regrouper les employés à des fins de planification.</td>
    </tr>
    <tr>
      <td>{% link_new Contrats | features/administration/create-contracts.md %}</td>
      <td>Les contrats contiennent des informations sur les contraintes de travail contractuelles pour vos employés, y compris leurs heures de travail cibles, minimales et maximales par jour, semaine ou mois.<br>Les contrats sont assignés aux employés.</td>
    </tr>
    <tr>
      <td>{% link_new Employés | features/administration/employee-overview.md %}</td>
      <td>Dans la section Employés, saisissez des informations sur chaque employé à planifier. Sur cette base et à partir de la configuration assignée (modèles horaires, unités opérationnelles, contrats, compétences), injixo détermine quand vos employés peuvent travailler et sur quelles activités.</td>
    </tr>
  </tbody>
</table>


### Éléments de configuration facultatifs

Le tableau ci-dessous propose un aperçu des éléments de configuration facultatifs que vous pouvez configurer dans injixo, en fonction de la configuration de votre organisation et de la méthode de planification que vous souhaitez utiliser.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Élément de configuration</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Rotations d’horaires | features/administration/shift-sequences.md %} (requises pour la planification fixe)</td>
      <td>Une rotation d’horaires est un cycle de modèles horaires ou d’activités.<br>Les rotations d’horaires sont assignées aux employés.</td>
    </tr>
    <tr>
      <td>{% link_new Groupes | features/administration/selections.md %}</td>
      <td>Les groupes vous permettent de filtrer et de grouper ou planifier les employés en fonction de critères donnés, par exemple les employés de la même équipe ou ayant le même type de contrat.<br> Les groupes sont assignés aux employés.</td>
    </tr>
    <tr>
      <td>{% link_new Modèles de planification et modèles hebdomadaires | features/administration/work-time-pattern-models.md %}</td>
      <td>Les modèles de planification et les modèles hebdomadaires vous aident à organiser les journées en garantissant une répartition équitable des journées (en rotation) parmi les employés que vous planifiez. Les modèles de planification contiennent au moins un modèle hebdomadaire. Les modèles hebdomadaires regroupent les postes selon des paramètres tels que l’heure de début, la durée de la journée ou les activités. Ils contiennent des ensembles de modèles horaires.<br>Les modèles hebdomadaires sont assignés aux modèles de planification. Les modèles de planification sont assignés aux employés.</td>
    </tr>
    <tr>
      <td>{% link_new Calendriers de planification et types de jours | features/administration/planning-calendar.md %}</td>
      <td>Les calendriers de planification contiennent des jours avec des horaires d’ouverture et un besoin en personnel différents (par exemple, les jours de campagne marketing ou les jours fériés nationaux). Ces jours spéciaux sont configurés à l’aide de types de jours. Cela permet de s’assurer qu’ils sont automatiquement pris en compte lors de la planification sans aucun effort manuel supplémentaire.<br> Les calendriers de planification sont assignés aux unités de planification.</td>
    </tr>
  </tbody>
</table>


## Et ensuite&nbsp;?

Félicitations&nbsp;! Vous pouvez maintenant {% link_new créer votre première prévision | getting-started/calculate-a-forecast.md %}. Bonne planification&nbsp;!
