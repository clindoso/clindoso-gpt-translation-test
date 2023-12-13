---
title: Administration des Congés/Absences
redirect_from:
  - /fr/administration-conges-absences/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-entitlement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md
---

Le menu _Congés/Absences_{:.menu-item} vous apporte une vue globale des demandes d'absences de vos Employés qui ont été saisies dans la partie _Absences_{:.menu-item} du portail Me.

Les utilisateurs disposant du rôle `Superviseur (basique)` peuvent visualiser les demandes, les utilisateurs disposant des rôles `Planificateur` et `Superviseur (avancé)` peuvent accepter ou refuser celles-ci.

Dans le menu _Plan > Congés/Absences_{:.breadcrumbs} vous pouvez filtrer les demandes selon les paramètres suivants :

| Unité opérationnelle | Sélectionnez une Unité opérationnelle ou `[Tous]` pour afficher les demandes de congés/absences des Employés concernés. |
| Groupe | Sélectionnez un groupe ou `[Tous]` pour restreindre le résultat. |
| Statut | Filtrer par statut de la demande ou `[Tous]` pour afficher l'intégralité des demandes. |
| Date de début | Sélectionnez la date de début. |
| Date de fin | Sélectionnez la date de fin. |

Après avoir cliqué sur _Appliquer filtres_{:.doc-button}, les résultats correspondants s'affichent. Vous pouvez trier le tableau par Statut, ID, nom, début, fin et Activité. Par défaut, les demandes sont affichées par ordre croissant.

Vous pouvez utiliser le champs de recherche pour filtrer les demandes par Employé ou par Activité.

| Statut | Affiche le statut actuel de la demande. Les statuts disponibles sont : <br/>- En attente<br/>- En attente, accepté<br/>- En attente<br/>- En attente, refusé<br/>- Accepté<br/>- Refusé |
| ID | Affiche l'ID des demandes de congés/absences, numérotées par ordre chronologique de saisie dans le système. |
| Nom | Nom de l'Employé. |
| NJ (Nombre de Jours) | Affiche le nombre de jours de la demande. |
| JR (Jours restants) | Affiche le solde de congés restants de l'Employé, calculé annuellement. Uniquement disponible pour les Activités de type `Congés`. |
| Début | Affiche la date de début de la demande. |
| Fin | Affiche la date de fin de la demande. |
| Activité | Affiche le type de Congés/Absences. |
| Commentaire | Affiche une icône quand la demande a reçu un commentaire. Pour visualiser le commentaire le curseur doit être positionné sur l'icône de la colonne. |

Pour une meilleure vue globale, les demandes sont également affichées dans un calendrier à droite du tableau. Cliquer sur Début ou Fin d'une demande pour aller vers le jour concerné dans le calendrier.
Les demandes en attente sont affichées en blanc, celles acceptées en vert et celles refusées en rouge.

En dessous du calendrier vous disposez de deux lignes qui précisent le nombre de demandes acceptées (**Quotas pris**) et le **Quota cible** d'absences. Le quota cible peut être défini dans l'écran de gestion des quotas décrit ci-dessous. Le quota pris prend en compte toutes les activités de type congé, absence et maladie. Grâce aux boutons vous pouvez décider d'afficher le quota en pourcentage ou en valeur absolue. Lorsque vous passez la souris sur les quotas, une infobulle affiche le nombre d'Employés disponibles et le nombre de demandes en attente pour cette journée.

### Définition des quotas et des paramètres

Cliquez sur _Définir un quota_{:.doc-button} pour ouvrir l'écran de paramétrage. Si vous cliquez sur le bouton _Retour à la gestion des congés_{:.menu-item} les modifications ne seront pas sauvegardées.

#### Règles d'approbation

Les règles d'approbation suivantes peuvent être configurées :

- Droit aux congés : vérifie si l'agent dispose de suffisamment de jours restants.
- Besoin : vérifie si le besoin en personnel journalier moyen est couvert.
- Quota : vérifie si le quota d'absences pour l'Unité opérationnelle n'a pas été atteint.

Après avoir configuré les règles d'approbation, cliquez sur _Sauvegardez les règles_{:.doc-button}.

#### Paramètres des quotas

Le quota cible est un pourcentage d'Employés autorisés à être absents sur une journée spécifique.

{{ 1 | image: "Paramètres Quota", '75%' }}

Dans la partie supérieure de cette section, vous pouvez définir les paramètres généraux concernant les quotas. Si vous souhaitez utiliser des quotas basés sur les ETPs (Equivalent Temps Plein), vous pouvez activer le bouton et définir un nombre d'heures à la journée pour un Employé à temps plein. Si ce paramètre est activé, la durée de la demande est prise en compte dans le quota d'un Employé à temps plein. Par exemple, si vous définissez un temps plein à 8h par jour, une demande d'absence de 4h représentera 1/2 ETP alors que si vous définissez un temps plein à 4h par jour, la même demande représentera 1 ETP.

Grâce à la liste déroulante `Unité de Quota`, vous pouvez choisir si le quota doit être affiché en pourcentage ou en nombre d'Employés. Un quota affiché en nombre d'Employés est indépendant de la taille de l'Unité opérationnelle.

Lorsque le type de valeur du quota est modifié, toutes les valeurs des quotas sont calculées selon la taille moyenne des Unités opérationnelles sur l'année sélectionnée. Sans modification des périodes ou des quotas journaliers, le quota de base s'applique sur toutes les journées. Par exemple, un quota défini à 10% est fixé à 5 employés pour une Unité Opérationnelle de 50 employés disponibles. A contrario, un quota défini à 5 employés ne change pas.

Sur la partie gauche de la section, vous pouvez ajouter, supprimer ou réorganiser des périodes de quota. Une période permet de définir un quota pour certaines plages de dates et peut avoir une dénomination spécifique. Il est également possible de configurer si les changements hebdomadaires s'appliquent à la période concernée. Les quotas définis sur une période écrasent le quota de base. De plus, l'ordre des périodes détermine quel quota doit être utilisé si plusieurs périodes se chevauchent. Les périodes en haut du tableau sont prioritaires. Vous pouvez glisser/déplacer les périodes pour les réorganiser.

Sur la partie droite de la section, vous pouvez définir un facteur pour chaque journée. Un facteur est un pourcentage appliqué au quota pour s'aligner sur une courbe hebdomadaire par exemple. Une valeur de 100% n'aura aucun effet sur le quota final.

Dans la partie inférieure de la section, un calendrier annuel affiche le quota pour chaque journée. C'est une visualisation de ce qui est actuellement configuré. Vous pouvez identifier le quota grâce à des codes couleur et visualiser la valeur exacte en cliquant sur la journée.

Une fois que vous avez terminé la configuration, cliquez sur _Sauvegarder le quota_{:.doc-button}.

### Suggestion de décisions

Cliquez sur _Suggérer une décision_{:.doc-button} pour que le système présélectionne des demandes à approuver. Le logiciel prendra en compte le nombre d'Employés dans l'Unité opérationnelle, le besoin en personnel, les absences déjà planifiées et le quota cible. Les requêtes sont traitées dans l'ordre d'arrivée ("premier arrivé, premier servi").

> Astuce
>
> Le bouton _Suggérer une décision_{:.doc-button} peut être indisponible pour plusieurs raisons. Les conditions suivantes doivent être remplies :
>
> D'abord, une Unité Opérationnelle doit être sélectionnée. Ensuite, il n'est pas autorisé d'avoir des requêtes en attente qui soient marquées comme acceptées ou rejetées. Pour résoudre cela, cliquez sur le bouton _Initialiser le groupes_{:.doc-button} ou validez les changements en cliquant sur le bouton _Appliquer_{:.doc-button}.
>
> De plus, notez que les suggestions sont désactivées lors d'une recherche parmi les demandes.

### Validation/Rejet des demandes

Il est possible d'accepter ou de refuser les demandes, aussi bien unitaires que multiples.

En utilisant les symboles correspondant dans la colonne "Statut" vous pouvez noter les demandes comme approuvées ou rejetées. A cette étape, les statuts peuvent être modifiés autant de fois que nécessaire car les changements ne sont pas sauvegardés automatiquement.

{{ 2 | image: "Validation ou refus des desiderata", '200', 'gif' }}

De plus, vous pouvez choisir de cliquer sur les boutons _Tout accepter_{:.doc-button} ou _Tout refuser_{:.doc-button} pour traiter toutes les demandes en une seule passe.

Une fois que les décisions ont été prises, il suffit de cliquer sur le bouton _Appliquer_{:.doc-button} en bas de la page. Dans le champ de commentaires vous pouvez ajouter une note expliquant la décision. Lorsque vous validez ou rejetez des demandes multiples, le même commentaire est associé à chaque demande. Cliquez sur le bouton _Approuver X demandes_{:.doc-button} pour continuer le processus de validation. Ces demandes feront alors l'objet d'une validation consistant à vérifier que l'Employé dispose de suffisamment de jours restants.

En cas de réussite, les demandes sont mises à jour dans le tableau.
S'il y a des échecs, vous pouvez les rejeter en cliquant sur le bouton _Rejeter X demandes_{:.doc-button}.

Si des erreurs surviennent, elles sont affichées dans une bannière avec l'ID de la demande et restent inchangées dans le tableau.

> Astuce
>
> Cochez la case `Contournement des règles d'approbation` si vous voulez forcer la validation ou le rejet de requêtes et passer outre les vérifications du système.

Un Employé est automatiquement notifié par e-mail lorsqu'une demande est approuvée ou rejetée. Si le planificateur insère un commentaire, il sera également affiché dans l'e-mail.

> Astuce
>
> Pour les Utilisateurs injixo Cloud, les notifications par e-mail sont automatiquement envoyées.
>
> Pour les Utilisateurs injixo Enterprise On Premise, vous devez saisir une adresse e-mail dans le champ `E-Mail 1` de la fiche Employé.
