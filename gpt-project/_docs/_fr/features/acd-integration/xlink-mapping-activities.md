---
title: Récupération des activités des employés
product_label:
  - on-premise
---

injixo vous permet d'importer les données des activités des employés à partir d'un système externe comme la téléphonie.

Ces données sont de types connexion/déconnexion et éventuellement le code activité correspondant.

Chaque interface dispose d'une documentation technique dédiée qui sont disponibles dans la section _Xlink Application & Documentation_ de la page [Downloads](https://downloads.injixo.com/fr).

<div markdown="1" class="hint-box-default hint-box-red">

Xlink est obsolète

Si vous utilisez actuellement Xlink pour votre abonnement injixo Cloud WFM, veuillez passer immédiatement à injixo Cloud Link ou à une solution qui respecte les normes d’intégration les plus récentes. N’hésitez pas à solliciter l’aide de nos experts [ici](https://www.injixo.com/fr/contact/).

</div>

> Remarques
>
> Xlink importera les données complètes de la journée à chaque import. Chaque processus prendra donc un plus de temps au fur à mesure de la journée.
>
> Les activités réalisées par les employés sont importées pour tous les systèmes externes sur lesquels une configuration a été réalisée.
>
> Les données importées sont disponibles dans la catégorie _Système externe_{:.menu-item} du _Centre de planification_{:.menu-item}.

## Mapping des données agents

Le mapping entre les activités injixo et celles du système externe est réalisé dans le menu _WFM > Administration > Planification > Activités_{:.breadcrumbs}.
Le mapping entre les employés injixo et ceux du système externe est réalisé dans le menu _WFM > Administration > Planification > Employés_{:.breadcrumbs}.

### Mapping des Activités

Pour importer les données des activités des employés dans injixo, vous devez en premier déterminer quelles sont les activités qui seront affichées dans le planning quand un employé se connecte à une activité d'un système externe. L'affectation des activités du système externe s'effectue dans le menu _WFM > Administration > Planification > Activités_{:.breadcrumbs} section _Systèmes Externes_{:.menu-item}.

> Remarque
>
> Lors de l'initialisation, les activités récupérées à partir de l'ACD sont affectées à l'activité système `Présent` (_ID 1_).

Le mapping est modifiable manuellement.
Par exemple, pour modifier le mapping de l'activité `Présent` vers une autre activité, la procédure est la suivante :

1. Sélectionner l'activité `Présent` dans le menu _WFM > Administration > Planification > Activités_{:.breadcrumbs}.
2. Supprimer l'activité du système externe affectée dans la section _Systèmes Externes_{:.menu-item}.
3. Cliquer sur l'activité injixo à configurer.
4. Affecter l'activité du système externe dans la section _Systèmes Externes_{:.menu-item}.

> Remarque
>
> Plusieurs activités du système externe peuvent être associées à une activité injixo.
>
> Une activité du système externe ne peut être affectée qu'à une seule activité injixo.

### Mapping des Employés

Vous devez également affecter l'ID d'un employé du système externe à un employé injixo. L'affectation des employés du système externe s'effectue dans le menu _WFM > Administration > Planification > Employés_{:.breadcrumbs} section _Systèmes Externes_{:.menu-item}.

{{ 1 | image: "Employees - Section Systèmes Externes", '50%' }}

{{ 2 | image: "Systèmes Externes Boîte de dialogue", '50%' }}

> Remarque
>
> Plusieurs ID du système externe peuvent être associées à un employé injixo.
>
> Un ID du système externe ne peut être affectée qu'à un seul employé injixo.
