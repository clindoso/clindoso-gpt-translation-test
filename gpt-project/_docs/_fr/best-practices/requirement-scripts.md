---
title: Choisir la méthode de calcul du besoin en personnel
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Découvrez quelle méthode de calcul du besoin en personnel convient le mieux à vos besoins.
redirect_from:
  - /fr/script-besoin/
toc: true
---

injixo propose des méthodes de calcul et des scripts pour calculer le besoin en personnel. 

## Méthodes de calcul

- Erlang-C&nbsp;: méthode de calcul pour les contacts entrants basée sur l’objectif de volume et de qualité de service.
- Chat&nbsp;: méthode de calcul basée sur Erlang-C avec un paramètre supplémentaire pour définir un nombre de sessions de chat consécutives.
- Productivité&nbsp;: méthode de calcul pour les contacts qui n'ont pas besoin d'être traités en temps réel (par exemple, lettres, e-mails, tickets ou commandes). Le résultat du calcul est basé sur le volume prévu et éventuellement sur le TMT.

Apprenez à {% link_new configurer les méthodes de calcul | features/forecast/injixo-forecast/calculate-staff-requirements.md %}.

## Scripts de calcul du besoin

- {% link_new Besoin constant | features/forecast/requirement-scripts/requirement-constant.md %}&nbsp;: pour les activités pour lesquelles vous n'avez pas de prévision, mais pour lesquelles vous connaissez le nombre d’employés nécessaires pour chaque plage horaire. Vous pouvez saisir vos propres valeurs de besoin en personnel. Vous pouvez définir des valeurs pour plusieurs plages horaires et activités.
- {% link_new Multi-Activités | features/forecast/requirement-scripts/requirement-multiactivity.md %}&nbsp;: pour planifier des employés polyvalents et combiner différents canaux (par exemple plusieurs lignes directes, ou une combinaison de chats et d'appels).
- {% link_new Appels sortants | features/forecast/requirement-scripts/requirement-outbound.md %}&nbsp;: pour les campagnes avec appels sortants. Vous pouvez définir des paramètres qui définissent la durée de la campagne, le taux de rappel, le taux de contacts aboutis, etc.
- Backoffice - Productivité&nbsp;: pour les communications indirectes, comme les lettres ou les e-mails, qui doivent être traités dans un délai prédéfini. Pour accéder à ce script, contactez votre consultant.
- Temps moyen de décroché (ASA)&nbsp;: script basé sur Erlang-C qui se concentre sur le délai moyen de réponse. Pour accéder à ce script, contactez votre consultant.
- Taux d'appels abandonnés&nbsp;: script basé sur Erlang-C vous permettant de définir votre objectif de service comme taux d'appels abandonnés maximum. Vous pouvez également l'utiliser si votre objectif est basé sur le taux de décroché. Pour accéder à ce script, contactez votre consultant.

## Types de données et méthodes de calcul du besoin en personnel pertinents

Le tableau suivant affiche les méthodes de calcul et les scripts adaptés à chaque type de données lors du calcul du besoin en personnel&nbsp;:

| Type de données ou paramètre  | Erlang-C (méthode) | Chat (méthode)  | Productivité (méthode) | Besoin constant (script) | Multi-activité (script) | Appels sortants (script) |
| ----------------------- |-------------------| -------- |--------  | -------- |   ------- | ------- |
| Données qui peuvent être stockées (par exemple, e-mails, tickets, commandes)   | Non        | Non | Non  | Non |  Oui | Oui |
| Appels                   | Oui       | Non | Non  | Non |  Oui | Non |
| chat                   | Non       | Oui | Non  | Oui |  Oui | Non |
| Contacts entrants                   | Oui       | Oui | Oui  | Oui |  Oui | Non |
| Contacts sortants                   | Non       | Non | Non  | Non |  Non | Oui |
| Une seule ligne                       | Oui     | Oui | Oui  | Oui |  Non | Oui |
| Plusieurs lignes                | Non       | Non | Non  | Non |  Oui | Non |
| Données historiques               | Oui     | Oui | Oui  | Non |  Oui | Oui |
| Type d'objectif de service               | Oui   | Oui | Non  | Non |  Oui | Oui |
| Qualité de service (par exemple 80/20)          | Oui     | Oui | Non  | Non |  Oui | Oui |
