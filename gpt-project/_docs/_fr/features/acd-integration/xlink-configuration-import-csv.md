---
title: Import de fichier CSV
product_label:
  - on-premise
redirect_from:
  - /fr/xlink-import-csv/
redirect_reason: Updated filename on 21 April 2022
---

Xlink vous permet d’importer automatiquement ou manuellement vos données historiques depuis un fichier CSV.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink est obsolète

Si vous utilisez actuellement Xlink pour votre abonnement injixo Cloud WFM, veuillez passer immédiatement à injixo Cloud Link ou à une solution qui respecte les normes d’intégration les plus récentes. N’hésitez pas à solliciter l’aide de nos experts [ici](https://www.injixo.com/fr/contact/).

</div>

## Prérequis

Xlink doit être installé sur le poste utilisateur ou le serveur sur lequel le paramétrage sera fait.
Un Système externe de type `CSV files` doit être préalablement créé dans le menu _WFM > Administration > Système > Systèmes externes_{:.breadcrumbs}.

Tous les fichiers mentionnés ci-dessous se trouvent dans le répertoire d'installation `xlink-xx` (où `xx` désigne la version de l'application Xlink).

## Format du fichier CSV

Le format du fichier CSV doit répondre aux exigences suivantes :

- Les 3 premières colonnes sont utilisées pour la date, l'intervalle horaire et le nom de la file d'attente.
- Les colonnes suivantes sont utilisées pour renseigner les volumes des types de valeur à importer (appels reçus, appels répondus, chats, e-mails, TMT,...).
- Il ne peut pas y avoir de cellule vide. S'il n'y a aucune donnée sur un intervalle, la valeur doit être 0.
- Le TMT est exprimé en secondes. Seuls des nombres entiers sont importés (par exemple, 0,5 devient 0, 1,5 devient 1).

### Exemple de fichier CSV

```
Date;Intervalle;File;Appels_recus;Appels_repondus;TMT
20/04/2020;08:00;ma_file_d_attente1;2;2;280
20/04/2020;08:15;ma_file_d_attente1;4;4;363
20/04/2020;08:30;ma_file_d_attente2;9;9;191
20/04/2020;08:45;ma_file_d_attente1;26;14;266
20/04/2020;09:00;ma_file_d_attente2;32;11;314
20/04/2020;09:15;ma_file_d_attente2;40;18;246
20/04/2020;09:30;ma_file_d_attente1;48;13;257
20/04/2020;09:45;ma_file_d_attente2;47;17;296
20/04/2020;10:00;ma_file_d_attente2;50;13;400
20/04/2020;10:15;ma_file_d_attente1;53;15;330
20/04/2020;10:30;ma_file_d_attente2;50;15;376
20/04/2020;10:45;ma_file_d_attente1;43;16;315
20/04/2020;11:00;ma_file_d_attente1;39;20;295
20/04/2020;11:15;ma_file_d_attente1;30;14;289
20/04/2020;11:30;ma_file_d_attente2;35;19;272
20/04/2020;11:45;ma_file_d_attente2;40;21;336
20/04/2020;12:00;ma_file_d_attente1;23;13;237
20/04/2020;12:15;ma_file_d_attente2;16;8;300
20/04/2020;12:30;ma_file_d_attente2;20;9;269
```

### Détail des colonnes

Pour importer les données historiques, les 3 premières colonnes du fichier sont obligatoires et doivent contenir :

- La date : plusieurs formats de date sont disponibles comme par exemple :
  - JJ/MM/AA
  - JJ/MM/AAAA
  - J-M-AA
  - JJMMAAAA
  - etc
- L'intervalle horaire : il doit être exprimé par tranches de 15, 30 ou 60 minutes. Plusieurs formats sont disponibles comme par exemple :
  - HH:MM:SS
  - HH:MM
  - H:MM AM ou PM
  - HHMMSS
  - etc
- La file d'attente : indiquez dans cette colonne le nom de la file d'attente.

Les colonnes suivantes doivent contenir les volumes des données à importer, par exemple les appels reçus, les appels répondus, les sessions de chat, le TMT, etc.

> Remarque
>
> L'ordre des 3 premières colonnes n'est pas imposé, il est paramétré dans le fichier `isps_Ul.ini` décrit ci-après.

## Exemple de fichier isps_Ul.ini

Le fichier `isps_Ul.ini` est le fichier de configuration des Systèmes externes dans Xlink. Il va notamment permettre de définir précisemment le format du fichier CSV à importer.

Vous trouverez ci-dessous la description des différents champs à renseigner ainsi que le détail du paramétrage à réaliser sur la base du fichier CSV fourni en exemple ci-dessus.

```
Source=C:\xlink-xx\Fichier_CSV\Fichiers_à_importer
DeleteActivityImportFiles=1
Destination=C:\xlink-38\Fichier_CSV\Appels\Fichiers_traités
HeaderLines=1
Interval=15
TimeZone=0
Protocol=1
LogFile=Log
SeparatorCharacter=3
ColumnNames=Date;Intervalle;File;Appels recus;Appels repondus;TMT
DateColumn=1
TimeColumn=2
GroupColumn=3
AHTColumn=6
DateOrder=dmy
TimeFormat=HH:MM:SS
Groups=ma_file_d_attente1;ma_file_d_attente2
```

### Paramétrage du fichier isps_Ul.ini

La procédure suivante explique comment paramétrer le fichier isps_Ul.ini :

- Ouvrez le fichier `isps_Ul.ini` et remplacez la ligne `[Copy external system from reference folder here]` par le nom du _Système externe_ créé dans injixo, en veillant à bien laisser les `[ ]`. Dans l'exemple fourni, le Système externe est nommé _CSV_
- Source : indiquez le chemin d'accès du fichier CSV à importer.
- DeleteActivityImportFiles : indique à l'application ce qu'elle doit faire après avoir importé le fichier. Les valeurs possibles sont :
  - 0 : laisser le fichier dans le répertoire `Source`
  - 1 : supprimer le fichier
  - 2 : déplacer le fichier dans le répertoire `Destination`
- Destination : indique le répertoire de destination si le paramètre DeleteActivityImportFiles est paramétré sur 2.
- HeaderLines : indique si le fichier CSV contient une ligne d'entête ou non. Les valeurs possibles sont :
  - 0 : pas d'entête
  - 1 : entête
- Interval : indique en minutes la granularité utilisée dans le fichier CSV. Les valeurs possibles sont :
  - 15
  - 30
  - 60
- TimeZone : spécifie en heures l'écart du fuseau horaire local par rapport à l'heure universelle (UTC). 0 est le paramètre par défaut.
- Protocol : indique si l'application doit à chaque import écrire des traces dans des fichiers de log. Les valeurs possibles sont :
  - 0 : aucune écriture de log
  - 1 : écriture de log
- LogFile : indique le nom du fichier de log si le paramètre Protocol est paramétré sur 1.
- SeparatorCharacter : indique le séparateur utilisé dans le fichier CSV. Valeurs possibles :
  - 0 : espace
  - 1 : point
  - 2 : virgule
  - 3 : point virgule
  - 4 : tabulation
- ColumnNames : indique le nom des colonnes du fichier CSV (c'est à dire la ligne d'entête s'il y en a une).
- DateColumn : indique le numéro de la colonne utilisée pour la date
- TimeColumn : indique le numéro de la colonne utilisée pour l'intervalle
- GroupColumn : indique le numéro de la colonne utilisée pour la file d'attente
- AHTColumn : indique le numéro de la colonne utilisée pour le type de valeur _Temps moyen de traitement_
- DateOrder : indique l'ordre d'affichage de la date. Les valeurs possibles sont :
  - dmy
  - ymd
- TimeFormat : indiquez le format de l'intervalle horaire. Plusieurs formats sont acceptés comme par exemple HH:MM:SS ou HH:MM.
- Groups : indiquez le nom des files d'attente du fichier CSV.

Une fois les champs correctement remplis, redémarrez le service `ISPS Xlink` pour que les modifications soient bien prises en compte.

L'étape suivante consiste à réaliser le mapping entre les données du fichier CSV et injixo.
