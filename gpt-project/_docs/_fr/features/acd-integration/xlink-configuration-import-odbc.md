---
title: Import ODBC
product_label:
  - on-premise
redirect_from:
  - /fr/xlink-import-odbc/
redirect_reason: Updated filename on 21 April 2022
---

Xlink vous permet d’importer automatiquement ou manuellement les données de votre ACD depuis une base de données. Une interface ODBC est requise pour réaliser cet import.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink est obsolète

Si vous utilisez actuellement Xlink pour votre abonnement injixo Cloud WFM, veuillez passer immédiatement à injixo Cloud Link ou à une solution qui respecte les normes d’intégration les plus récentes. N’hésitez pas à solliciter l’aide de nos experts [ici](https://www.injixo.com/fr/contact/).

</div>

## Prérequis

Xlink doit être installé sur le poste utilisateur ou le serveur sur lequel le paramétrage sera fait.

Un Système externe (par exemple _Avaya CMS_, _Bosch BCC (Avaya CIE)_, _Nortel Symposium (Avaya Aura)_ ou Universal.) doit être préalablement créé dans le menu _WFM > Administration > Système > Systèmes externes_{:.breadcrumbs}.

Une source de données système doit être configurée dans l'outil _Admistrateur de source de données ODBC (32 bits)_ de Windows pour vous connecter à la base de données de votre ACD. L'utilisateur de la base de données doit avoir un accès en lecture sur les tables ou les vues utilisées par l'interface.
Il est nécessaire de télécharger les drivers spécifiques sur le site du fournisseur de votre ACD.

## Configuration

Nous distinguons 2 types d'interfaces :

- Une interface standard est disponible pour certains ACD, cette interface dispose d'une logique implémentée en native dans l'outil.
- Une interface universelle permet de réaliser l'interface avec les autres ACD.

Votre Customer Success Manager est là pour vous accompagner dans le choix d'intégration le plus pertinent dans votre contexte.

### Interface Standard

1. Lancer Xlink grâce au fichier `isps_ul.exe`.
2. Faire un clic droit sur le système externe sélectionné et cliquer sur _Configuration..._{:.menu-item}.
3. Dans la boîte de dialogue, entrer le nom de la source ODBC définie dans Windows, le nom de l'utilisateur et le mot de passe dans les champs correspondants.
4. Cliquer sur _Ok_{:.doc-button} pour sauvegarder la configuration.

> Remarque
>
> Lors de l'étape 3, _Tester ODBC_{:.doc-button} permet de valider la conformité des informations saisies.

Une nouvelle entrée correspondant à cette interface sera créée dans le fichier `isps_ul.ini`.

Si la connexion à la base de données est réussie, une arborescence apparaît dans la section `Interfaces`. Si l'arborescence n'apparaît pas, vérifiez le fichier `call_tree.log` dans le répertoire d'installation de Xlink.

### Interface Universelle

1. Lancer Xlink grâce au fichier `isps_ul.exe`.
2. Faire un clic droit sur le système externe sélectionné et cliquer sur _Configuration..._{:.menu-item}.
3. Dans la boîte de dialogue, entrer le nom de la source ODBC définie dans Windows, le nom de l'utilisateur et le mot de passe dans les champs correspondants.
4. Cliquer sur _Ok_{:.doc-button} pour sauvegarder la configuration.
5. Ajouter les lignes suivantes dans le fichier de configuration `isps_ul.ini` à la section du système externe voulu :

```
QueueSQL = select queue_name from queue_table order by queue_name
ValueTypes = valuetype_1;valuetype_2;valuetype_3
TimeStampColumn = start_date_column
QueueNameColumn = queue_name_column
CallDataTable = source_table_name

ActivitySQL = SELECT DISTINCT activiy_name_column, activity_ID_column FROM source table
ActivityTimeSpanType = 1 ;(start and end time only)
ActivityColumn = activity_name_column
AgentColumn = agent_login_id_column
ActivityStartTimeStampColumn = start_time_column
ActivityStartTimeStampType = 2 ;(date/time field)
ActivityEndTimeStampColumn = end_time_column
ActivityEndTimeStampType = 2 ;(date/time field)
AgentActivityTable = source table name
```

6. Ajuster les colonnes, la table ou la vue pour correspondre à l'architecture de votre base de données. L'exemple donné est pour information uniquement. Vous devez remplacer les valeurs par les champs de la base de données correspondants pour `queue_name`, `queue_table`, `valuetype_*`, `start_date_column`, `queue_name_column` et `source_table_name`. Cela s'applique aussi à tous les paramètres `Activity*`
7. Sauvegarder les changements.
8. Redémarrer le service Windows `ISPS XLink`
9. Exécuter à nouveau le fichier `isps_ul.exe`.

Si la connexion à la base de données est réussie, une arborescence apparaît dans la section `Interfaces`. Si l'arborescence n'apparaît pas, vérifiez le fichier `call_tree.log` dans le répertoire d'installation de Xlink.

> Remarque
>
> Une fois la connexion établie, les activités de l'ACD sont automatiquement mappées avec l'Activité _Présent_ dans injixo. Ces informations ne sont pas disponibles sous la forme d'une arborescence mais peuvent être consultées dans le menu _Affichage > Activitiés_{:.breadcrumbs} de Xlink.
