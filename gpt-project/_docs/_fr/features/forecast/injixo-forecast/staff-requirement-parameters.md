---
title: Paramètres de calcul du besoin
redirect_from:
  - /fr/parametres-besoin-en-personnel/
redirect_reason: Updated filename on 21 April 2022
---

En fonction de la méthode choisie pour le calcul du besoin en personnel, plusieurs paramètres sont à renseigner.

## Paramètres communs à toutes les méthodes

### Unité opérationnelle et Activité

Sélectionnez l'**Unité opérationnelle** et l'**Activité** à dimensionner. Les horaires d'ouverture de ces 2 objets sont pris en compte lors du calcul.

### Shrinkage

Vos agents ne peuvent pas être productifs à 100%, même à pleine capacité. En effet, les pauses non prévues, les retards ou les problèmes informatiques peuvent impacter leur productivité. Le **Shrinkage** vous permet de prendre en compte ces temps non productifs dans le calcul du besoin.

Saisissez la valeur souhaitée pour le Shrinkage. Si vous ne souhaitez pas prendre en compte le Shrinkage dans votre dimensionnement, vous pouvez laisser la valeur définie par défaut (0).

> Remarque  
>  
> Pour une valeur du **Shrinkage** de x%, le besoin en personnel calculé est divisé par `(1-x%)`.  
>
> **Exemple**  
>
> Pour un besoin de 70 agents l'impact du Shrinkage est le suivant :  
>
> - Shrinkage à 0% : 70 agents  
> - Shrinkage à 10% : 77,78 agents  
> - Shrinkage à 30% : 100 agents  

### Personnel minimum - maximum requis

Les champs **Personnel minimum requis** et **Personnel maximum requis** vous permettent de définir respectivement des valeurs planchers et plafonds à respecter lors du calcul du besoin en personnel.

Saisissez une valeur à respecter dans le champ **Personnel minimum requis** ou **Personnel maximum requis**. Si vous ne souhaitez pas prendre en compte ces paramètres dans votre dimensionnement, vous pouvez laisser le champ vide (valeur par défaut).

Les champs **Personnel minimum requis** et **Personnel maximum requis** peuvent être utilisés conjointement ou individuellement.

### Temps Moyen de Traitement (TMT) fixe

Si vous souhaitez définir un TMT fixe ou si le TMT associé au Workload n'est pas disponible, renseignez la valeur dans le champ associé. Cette valeur est affichée dans le détail par intervalle.

> Remarque  
>  
> Vous devez configurer obligatoirement une **Unité opérationnelle et une Activité**. Les paramètres **Shrinkage**, **Personnel minimum requis**, **Personnel maximum requis** et **TMT fixe** sont optionnels.

## Erlang-C

Cette méthode est utilisée pour le calcul du besoin en personnel pour les Workloads de type Appels. Elle prend en compte un objectif de Qualité de Service cible.<br>

Une fois les paramètres communs renseignés, indiquez le **Niveau de Service** qui correspond à un pourcentage d'appels entrants répondus par les conseillers en un temps défini.

Le **Niveau de Service** proposé par défaut est 80/20. Cela signifie que 80% des appels seront répondus en moins de 20 secondes.

## Chat

Cette méthode est utilisée pour le calcul du besoin en personnel pour les Workloads de type Chat. Basée sur la méthode de calcul Erlang-C, elle permet également de configurer le nombre maximum de conversations simultanées par conseiller.

Une fois les paramètres communs renseignés, indiquez :

- le **Nombre de sessions maximum** qui permet de configurer le nombre de conversations simultanées par conseiller.
- l'**Overhead** qui permet de configurer le pourcentage du Temps Moyen de Traitement qu'un employé dédie à une tâche qui ne peut être traitée en parallèle (comme par exemple annoter une fiche client dans le CRM).

> Remarque  
>   
> Si le paramètre **Nombre de sessions maximum** a pour valeur 1, alors le paramètre **Overhead** n'aura pas d'effet.  

## Productivité

Cette méthode de calcul est utilisée pour calculer le besoin en personnel de médias asynchrones (e-mails, documents, dossiers, ...) ou pour les Workloads de type Appels qui n'ont pas d'objectif de Qualité de Service.

Seul les paramètres communs doivent être renseignés.
