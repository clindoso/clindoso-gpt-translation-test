---
title: Een database-integratie toevoegen
navigation_title: Database
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Verbind je database met injixo om gegevens te importeren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Wat is een database-integratie?

Een database-integratie is een speciaal soort on-premise-integratie. Gebruik een database-integratie als je systeem geen verbinding kan maken met een cloud of een andere on-premise-integratie.

Je kunt een SQL-query definiëren om gegevens uit een database uit te lezen. Database-integraties maken gebruik van {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

## Een database-integratie toevoegen

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Universal interfaces**-tegel op _Kies een model_{:.doc-button}.
4. Klik in de sectie **Database** op _Voeg integratie toe_{:.doc-button}.

## Je nieuwe database-integratie instellen

1. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
2. Installeer en maak verbinding met {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Selecteer je **databasetype**.
4. Voer je aanmeldgegevens in, afhankelijk van je selectie.


   | Databasetype:                                  | Aanmeldgegevens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | MS SQL Server<br>MySQL<br>PostgreSQL | **Databasenaam**<br>**Host**<br>**Poort**: Als je een MS SQL Server-verbinding met een naam gebruikt, voer dan geen poort in. Open in plaats daarvan UDP-poort 1434 in je firewall zodat de SQL Server-browserservice de poort voor injixo Cloud Link kan vaststellen.<br>**Gebruikersnaam**<br>**Wachtwoord**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | Overige (ODBC)                                   | **Connection string**: Connection strings bevatten parameters die de integratie nodig heeft om verbinding te maken met je database-server. Hier vind je de geschikte connection strings voor je databasetype en ODBC-stuurprogramma: [https://www.connectionstrings.com](https://www.connectionstrings.com).<br><br>Voorbeeld voor een InterSystems Caché-database:<br>`DRIVER={InterSystemsODBC};SERVER=myServerAddress;` `PORT=12345;DATABASE=myDataBase;UID=myUsername;PWD=myPassword;` <br><br>SQL-ID wordt in queries gescheiden met dubbele aanhalingstekens. Als je ODBC-stuurprogramma dit niet standaard ondersteunt, voeg dan aanvullende opties toe aan de connection string.<br><br>Voorbeeld voor een IBM Informix-database:<br>`DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;`<br><br>Je kunt ook een ODBC-gegevensbron aanmaken om het stuurprogramma, de server, de database, etc. te configureren. Je kunt de onderstaande DSN-optie dan als connection string gebruiken en hoeft geen verbindingsgegevens aan de connection string toe te voegen. Wel moet je de opties toevoegen die niet in de ODBC-gegevensbron kunnen worden geconfigureerd, zoals `DELIMIDENT=y`.<br><br>DSN-voorbeelden:<br> `DSN=myODBCDatasourceName;`<br>`DSN=myODBCDatasourceName;DELIMIDENT=y;` |

## Je importgegevens configureren

1. Selecteer in de sectie **Configuratie** het importgegevenstype dat je vanuit je database wilt importeren:
   - **Contactgebaseerd** voor historische contactgegevens met een regel voor elk contact
   - **Intervalgebaseerd** voor historische contactgegevens die in intervallen van 15 or 30 minuten zijn samengevoegd (ingesteld als intervallengte)
   - **Agentstatussen** voor agentstatusgegevens  
    Gegevens worden standaard om de 15 minuten geïmporteerd, maar je kunt de volgende twee selectievakjes gebruiken om het importgedrag aan te passen:
        - **Realtime gegevens importeren**: Gegevens worden om de 10 seconden geïmporteerd. Alleen beschikbaar in injixo Advanced en Enterprise WFM.
        - **Afstemming van gegevens**: Regelt welke tijdsperiode van agentstatusgegevens om de 15 minuten wordt geïmporteerd. Standaardinstelling: gegevens van de afgelopen 24 uur (aanbevolen).  

2. Selecteer in het vervolgkeuzemenu **tijdzone database**.
3. Voer de **SQL-query** in die wordt gebruikt om gegevens uit je database te importeren. Lees meer over de [SQL-query](#sql-query).
4. Klik op _Integratie opslaan_{:.doc-button} om de integratie aan te maken.  
   De integratie importeert vanaf nu gegevens in injixo. Het importeren kan tot 15 minuten duren.  
   Alle queues die uit de gekoppelde database zijn geïmporteerd, zijn automatisch beschikbaar op het {% link_new workload-configuratiescherm | features/forecast/injixo-forecast/manage-workloads.md | #workloads-aanmaken %} in injixo Forecast.  
   Externe activiteiten zijn beschikbaar in de activiteit Aanwezig (ID 1). Om agentstatusgegevens te importeren, moet je {% link_new medewerker-ID's en activiteiten van het externe systeem toewijzen | features/acd-integration/cloud/import-agent-status-data.md %}.

### Afstemming van gegevens

Soms is het noodzakelijk om eerder geïmporteerde agentstatusgegevens handmatig te corrigeren. Als een een medewerker bijvoorbeeld vergeten is zichzelf uit te klokken en je de gewerkte tijd in je database hebt gecorrigeerd.

Het selectievakje **Afstemming van gegevens** is standaard geactiveerd.

- van de laatste 24 uur
- om de 15 minuten

Je hebt altijd toegang tot de meest recente gegevens van de afgelopen 24 uur. Alleen gewijzigde gegevens die ouder zijn dan 24 uur worden niet in de nieuwe import opgenomen.

Je database kan problemen ondervinden met het volume van continue nieuwe gegevensimports. Als je de functie Afstemming van gegevens uitschakelt, dan importeert injixo alleen de nieuwste gegevens vanaf de laatste geslaagde import (meestal gegevens van de afgelopen 15 minuten). In dat geval moeten gegevens die meer dan 15 minuten geleden zijn geïmporteerd mogelijk handmatig worden bijgewerkt. Het is aanbevolen om het selectievakje aangevinkt te laten, omdat handmatige gegevensupdates aanzienlijk meer tijd in beslag nemen en foutgevoelig zijn.

Als je je integratie minder dan 24 uur pauzeert, dan importeert injixo alle gegevens opnieuw zodra de integratie opnieuw wordt gestart. Het is hiervoor irrelevant of het selectievakje is aan- of uitgevinkt.  
Als je de integratie voor langere tijd pauzeert, worden alle gegevens ouder dan 24 uur niet opnieuw geïmporteerd.

## SQL-query

De SQL-query voor een database-integratie moet bepaalde kolomnamen bevatten. Het geselecteerde importgegevenstype bepalen de verwachte kolommen. Je kunt de tabelnaam zelf instellen. Hieronder staan de eenvoudigste SQL-query's die je kunt uitvoeren:

<style>
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Importgegevenstype | Voorbeeldquery                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| Intervalgebaseerd   | SELECT queueidentifier, queuename, timestamp, offered, answered, handlingtime, channel FROM table |
| Contactgebaseerd    | SELECT queueidentifier, queuename, timestamp, answered, duration, channel FROM table              |
| Agentstatussen     | SELECT agentidentifier, starttime, endtime, activity FROM table                                   |

> Opmerking 
> 
> Waarschijnlijk komen de kolomnamen in je database niet overeen met de verwachte kolomnamen. Om dit te omzeilen, kun je de vereiste kolomnamen als kolom-alias gebruiken of een weergave aanmaken in je database.

Breid de voorbeeldquery's uit om gegevens op te halen en te filteren uit je aangepaste tabel:

```
SELECT
  Start as "timestamp",
  Id as queueidentifier,
  Name as queuename,
  SUM(CASE countId WHEN 1000 THEN val ELSE 0 END) as offered,
  SUM(CASE countId WHEN 1001 THEN val ELSE 0 END) as answered,
  SUM(CASE countId WHEN 1002 THEN val ELSE 0 END) as handlingtime,
  calls as channel
FROM table
WHERE countId IN (1000, 1001, 1002)
GROUP BY Start, Name
```

## Kolomgegevens

De volgende tabellen geven de gegevens weer voor de verwachte kolommen, gescheiden door het importtype.

### Agentstatussen

<style>

table {
   width: 100%;
}  
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Kolom                    | Gegevenstype | Vereist | Gegevens                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| agentidentifier           | String    | Ja      | Unieke ID voor de agent                                                                                                                                          |
| starttime                 | Datum en tijd  | Ja      | Begin agentstatusactiviteit                                                                                                                                       |
| endtime                   | Datum en tijd  | Nee       | Begin agentstatusactiviteit<br>Alleen gebruiken als de activiteit al is afgerond.                                                                                               |
| activity                  | String    | Ja      | ID voor de externe activiteit                                                                                                                                     |

### Intervalgebaseerd

| Kolom                    | Gegevenstype | Vereist | Gegevens                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | String    | Ja      | Unieke ID voor de queue<br>Je kunt de queue een andere naam geven door de queuenaam te wijzigen, maar de queue-ID blijft hetzelfde.                                        |
| queuename                 | String    | Ja      | ID voor de queue                                                                                                                                                 |
| timestamp                 | Datum en tijd  | Ja      | Begin van de interval                                                                                                                                                    |
| offered                   | Integer   | Ja      | Aantal contacten (bijvoorbeeld oproepen of e-mails) tijdens de interval                                                                                                                 |
| answered                  | Integer   | Ja      | Aantal contacten dat tijdens de interval is behandeld                                                                                                                |
| handlingtime              | Integer   | Ja      | Totale verwerkingstijd voor alle contacten tijdens de interval                                                                                                                       |
| channel                   | String    | Nee       | ID voor het kanaal van de injixo-bronqueue<br>Indien niet gedefinieerd, wordt deze standaard ingesteld op oproepen<br>Geldige waarden: calls, chats, emails, social_media, documents, cases. |

### Contactgebaseerd

| Kolom                    | Gegevenstype | Vereist | Gegevens                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | String    | Ja      | Unieke ID voor de queue<br>Je kunt de queue een andere naam geven door de queuenaam te wijzigen, maar de queue-ID blijft hetzelfde.                                        |
| queuename                 | String    | Ja      | ID voor de queue                                                                                                                                                 |
| timestamp                 | Datum en tijd  | Ja      | Begin van de interval                                                                                                                                                    |
| offered                   | Integer   | Ja      | Aangeboden contact (waarde 1)<br>Geen aangeboden contact (waarde 0)                                                                                                                |
| answered                  | Integer   | Ja      | Afgehandeld contact (waarde 1)<br>Geen afgehandeld contact (waarde 0)                                                                                                                |
| duration                  | Integer   | Ja      | Totale afhandeltijd voor een enkel contact                                                                                                                                    |
| channel                   | String    | Nee       | ID voor het kanaal van de injixo-bronqueue<br>Indien niet gedefinieerd, wordt deze standaard ingesteld op oproepen<br>Geldige waarden: calls, chats, emails, social_media, documents, cases. |

## Een database-integratie bewerken

Als je database-gegevens of de gegevensstructuur verandert, dan kun je de configuratie van je database-integratie bewerken. De volgende gegevensimport wordt op dezelfde manier uitgevoerd als voorheen. Als je alle beschikbare gegevens uit het verleden opnieuw wilt importeren, maak dan een nieuwe integratie aan.

## Bekende problemen met ODBC-stuurprogramma's

Zorg ervoor dat je versie [Athena ODBC 2.x](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver.html) van het besturingsprogramma gebruikt om het aantal TCP-verbindingen in Cloud Link te beperken wanneer gegevens van Amazon Athena worden opgevraagd.

