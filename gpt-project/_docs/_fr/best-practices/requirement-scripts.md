---
title: Quel script de calcul du besoin utiliser ?
toc: false
redirect_from:
  - /fr/script-besoin/
redirect_reason: Filename changed in April 2022
---

injixo permet de dimensionner le nombre d'employés nécessaires aux traitements de vos différentes activités.
Plusieurs méthodes de calcul du besoin en personnel sont disponibles.
Selon le canal à prendre en compte et votre indicateur de service, il convient d'utiliser des scripts de calcul différents.

Cet article vous apporte les outils pour déterminer quel script de calcul du besoin est le plus pertinent selon vos spécificités.

## Diagramme de décision

Le diagramme suivant vous aide à décider quel script de besoin utiliser :

{{ 1 | image: 'Workflow'}}

## Scripts de calcul du besoin en personnel

Les scripts disponibles sont les suivants :

- {% link_new Besoin constant | features/forecast/requirement-scripts/requirement-constant.md %}: Pour tout type d'activité sur laquelle vous ne disposez pas de données historiques mais pour laquelle vous souhaitez définir le nombre d'employés nécessaires par intervalle.
- {% link_new Besoin Productivité | features/forecast/requirement-scripts/requirement-linear.md %}: Pour tous les canaux asynchrones tels que les e-mails, courrier, tickets à traiter en mode séquentiel. Ce script peut également être utilisé pour calculer le besoin liée à une activité d'appels entrants pour laquelle vous n'avez d'objectif de Qualité de Service.
- Backoffice - Productivité : Pour tous les canaux asynchrones tels que les e-mails, courrier, tickets à traiter dans un délai prédéfini.
- {% link_new Chat - Webchat | features/forecast/requirement-scripts/requirement-chat.md %}: Script basé sur la méthode Erlang C prenant en compte le nombre de sessions de chat simultanées par employé.
- {% link_new Appels - Mono Activité | features/forecast/requirement-scripts/requirement-erlangc.md %}: Script basé sur la méthode Erlang C permettant de calculer le besoin en fonction d'un objectif de Qualité de Service.
- {% link_new Appels - Multi Activités | features/forecast/requirement-scripts/requirement-multiactivity.md %}: Script basé sur les méthodes Erlang C, Productivité et Chat permettant de calculer le besoin en personnel pour planifier des activités à des agents disposant de plusieurs compétences.
- Appels - Temps moyen de réponse : Script basé sur la méthode Erlang C permettant de calculer le besoin en fonction d'un objectif de temps de décroché.
- Appels - Taux d'abandon : Script basé sur la méthode Erlang C permettant de calculer le besoin en fonction d'un objectif de taux d'abandon ou d'appels répondus (80% d'appels répondus équivaut à 20% d'appels abandonnés).
- {% link_new Appels sortants | features/forecast/requirement-scripts/requirement-outbound.md %}: Script de prise en compte des campagnes d'appels sortants.

Vous hésitez encore sur le script à utiliser ? Le tableau ci-dessous vous aidera à prendre une décision :

{{ 2 | image: 'Tableau' }}
