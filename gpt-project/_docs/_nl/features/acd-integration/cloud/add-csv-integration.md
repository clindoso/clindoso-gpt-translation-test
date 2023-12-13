---
title: Een CSV-integratie toevoegen
navigation_title: CSV
description: Historische gegevens uit CSV-bestanden in injixo importeren.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - nl/csv-format/
redirect_reason: /csv-format/ used on in injixo UI (injixo.com/csv-importer)
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
---

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Wat is een CSV-integratie?

Een CSV-integratie importeert historische contact- of agentstatusgegevens uit CSV-bestanden. Gebruik een CSV-integratie als je systeem geen verbinding kan maken met een andere integratie.

Hier volgt een overzicht van hoe een CSV-integratie in zijn werk gaat:

- Maak in injixo een CSV-integratie aan.
- Maak een CSV-schema aan.
- Wijs de kolommen toe (via het vervolgkeuzemenu of een SQL-query).
- Importeer CSV-bestanden automatisch of handmatig.

## Een CSV-integratie toevoegen

Om verschillende CSV-bestandsformaten te importeren (bijvoorbeeld met verschillende scheidingstekens, datumformaten of kolomnamen) stel je voor elke bestandsformaat een aparte integratie in. Afhankelijk van het CSV-bestand dat door je externe systeem wordt gegenereerd, kunnen de verwachte kolommen in injixo afwijken van die van je CSV. [Lees meer](#de-kolommen-toewijzen) over de verwachte kolommen in injixo en hoe je deze toewijst als je CSV-bestand andere kolommen of kolomnamen bevat.

Voeg als volgt een CSV-integratie toe in injixo:

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Universal interfaces**-tegel op _Kies een model_{:.doc-button}.
4. Klik in de sectie **CSV** op _Voeg integratie toe_{:.doc-button}.

## Een nieuwe CSV-integratie configureren

1. Voer een unieke naam in voor de integratie die naar de gegevensbron verwijst.
2. Installeer in de sectie **injixo Cloud Link** {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md | #injixo-cloud-link-installeren %} en breng een verbinding tot stand. Als je de gegevens liever [handmatig uploadt](#handmatige-bestandsimport), dan kun je deze stap overslaan.
3. Selecteer in de sectie **CSV-schemaconfiguratie** het **importgegevenstype**:
   - **Contactgegevens**: De geüpload gegevens bevatten alle binnenkomende en verwerkte volumes die door je externe systeem zijn geregistreerd, zoals oproepen, chats, sociale media, tickets, e-mails en documenten.
   - **Agentstatus**: De geüploade gegevens bevatten alle activiteiten van agenten die door je externe systeem zijn geregistreerd, zoals aanmelden, afmelden, in gesprek, nawerk, pauze, gereed, etc.
4. Klik op _Nieuw CSV-schema aanmaken_{:.doc-button}.
5. Configureer de instellingen van het CSV-schema, zoals:
   - voorbewerkingsopties
   - kolomtoewijzing (standaard via [drop-downmenu's](#de-kolommen-toewijzen); alternatief via [SQL-query](#de-kolommen-toewijzen-sql-query))  
      Lees meer over hoe je een [CSV-schema aanmaakt](#een-csv-schema-aanmaken) met de eerder genoemde configuratieopties.
6. Klik op _Integratie opslaan_{:.doc-button} om de integratie in te stellen.

Nadat je de integratie hebt opgeslagen, kun je de [handmatige gegevensimport](#handmatige-bestandsimport) gebruiken of de [automatische gegevensimport](#automatische-bestandsimport) instellen.

## Een CSV-schema aanmaken

Elke CSV-integratie heeft een eigen CSV-schema. Het CSV-schema beschrijft de layout en de kolomtoewijzing van het CSV-bestand. Als je externe systeem een CSV-bestand genereert dat niet de exacte kolomnamen bevat die in injixo worden weergegeven, dan kun je ze in injixo toewijzen via de [vervolgkeuzemenu's (standaard)](#de-kolommen-toewijzen) of een [SQL-query](#de-kolommen-toewijzen-sql-query).  
[Lees meer](#de-kolommen-toewijzen) over de verwachte kolommen in injixo en hoe je deze toewijst als je CSV-bestand andere kolommen of namen bevat.

Voordat je een CSV-schema kunt aanmaken, moet je [een CSV-integratie toevoegen](#een-csv-integratie-toevoegen) en het importgegevenstype selecteren. De parameters die je voor het CSV-schema configureert zijn afhankelijk van het soort geselecteerde importgegevens (contactgegevens of agentstatus).

### Voorbewerkings- en instellingsopties

1. Upload in de sectie **Setup** een CSV-voorbeeldbestand dat door je externe systeem is gegenereerd. Zo kun je zien hoe injixo je bestanden tijdens het importeren behandelt.
2. Stel de volgende parameters in. De parameters verschillen afhankelijk van het importgegevenstype.<br><br>

   | Parameter                                                     | Beschrijving                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Kolomscheidingsteken van CSV-bestand**                              | Het scheidingsteken dat in het geüploade CSV-bestand wordt gebruikt, bijvoorbeeld een puntkomma                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | **Tijdzone**                                                 | Tijdzone waarin je externe systeem de gegevens opslaat, bijvoorbeeld America/Chicago (UTC-05:00)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | **Layout van gegevens**<br>(Alleen contactgegevens)                     | De gegevenslayout is afhankelijk van de manier waarop je CSV-bestand is gegenereerd:<br>**Op contactbasis**: Voor records met contactgegevens die voor elk afzonderlijk contact een regel bevatten. Omdat geïmporteerde contactgegevens worden samengevoegd in intervallen van 15 minuten, moet het interval van de eenheid ook 15 minuten zijn. Nieuwe gegevensimports overschrijven de gegevens die eerder zijn geïmporteerd voor het interval. Als je bestand meermaals dezelfde tijdstempel bevat, dan worden deze gegevens bij elkaar opgeteld voor het interval.<br><br>**Op intervalbasis**: Voor verzamelde gegevens die een regel bevatten met alle contactinformatie per interval. Selecteer ook de juiste intervallengte die overeenkomt met de intervallengte van je CSV-bestand. Als je een interval selecteert dat langer is dan de intervallen van de geüploade bestanden, dan verschijnt er een foutmelding. Als je andersom te werk gaat, en bijvoorbeeld een interval 15 minuten voor een bestand met grotere intervallen (bijv. 30 minuten) selecteert, dan wordt elke ontbrekende (hier: elke tweede) interval, gevuld met een 0 of de tekst “Geen gegevens”, afhankelijk van je selectie bij de optie **Behandel ontbrekende waarden in intervallen**.
   | **Behandel ontbrekende waarden in intervallen**<br>(Alleen contactgegevens) | Geef aan hoe ontbrekende waarden in de beoogde queue op andere plaatsen in injixo worden weergegeven:<br>**Vullen met nul**: Ontbrekende waarden worden vervangen door een nul.<br>**Leeg laten**: Ontbrekende waarden worden verbangen door de tekst: geen gegevens.<br>**Leeg laten** is in de meeste gevallen geschikt. Bestaande gegevens worden met geïmporteerde gegevens overschreven.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

3. (Optioneel) Selecteer in de sectie **Voorbewerkingsopties** een of meer opties die van toepassing zijn op je CSV-bestandsformaat:<br><br>

   | Voorbewerkingsopties       | Beschrijving                                                                                                                                                                                             |
   | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Kopregel toevoegen**         | Bij bestanden zonder kopregel noemt injixo de kolommen A, B, C, etc. op de pagina [kolomtoewijzing](#de-kolommen-toewijzen).                                                                        |
   | **Lege regels overslaan**        | injixo negeert regels die alleen scheidingstekens bevatten                                                                                                                                                  |
   | **Eerste ... regels overslaan**        | injixo verwijdert extra regels aan het begin van een bestand Voer het aantal rijen in dat genegeerd wordt.                                                                                               |
   | **Regel(s) overslaan die de volgende inhoud bevatten** | injixo negeert regels waarin bepaalde tekens voorkomen. Voer een string in (hoofdlettergevoelig). injixo negeert regels die deze string bevatten. Je kunt meerdere strings toevoegen door op _String toevoegen_{:.doc-button} te klikken. |

4. Om verder te gaan met het toewijzen van kolommen, klik je op _Ga naar toewijzing_{:.doc-button}.

### De kolommen toewijzen

Je kunt standaard de vervolgkeuzemenu's in de sectie **Kolommen toewijzen** om aan te geven hoe de kolommen van je CSV-bestanden worden gekoppeld aan de kolommen die injixo vereist. Voordat je kolommen kunt mappen, moet je de [configuratie](#voorbewerkings--en-instellingsopties) afronden.
Als je externe systeem CSV-bestanden genereert die niet de verwachte kolommen bevatten, dan kun je ze [toewijzen met behulp van een SQL-query](#de-kolommen-toewijzen-sql-query).

Op de toewijzingspagina wordt een preview van je geüploade CSV-bestand weergegeven.

1. Gebruik de vervolgkeuzemenu's om de kolommen en formaten van het CSV-bestand toe te wijzen.

2. Vul elk veld in.  
   Lees in de volgende tabellen meer over de opties voor [contactgegevens](#vervolgkeuzemenus-contactgegevens) en [agentstatusgegevens](#vervolgkeuzemenus-agentstatus).

3. Klik op _Schema opslaan_{:.doc-button} om je configuratie op te slaan.

#### Vervolgkeuzemenu's contactgegevens

Als je het importgegevenstype **Contactgegevens** hebt geselecteerd, dan worden de volgende elementen op de standaard toewijzingspagina weergegeven:

| Veld          | Beschrijving                                                                                                                                                                                                                                          | Vereist voor gegevens op intervalbasis | Vereist voor gegevens op contactbasis |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------: | :-----------------------------: |
| **Naam van queue** | Naam van de queue waaruit gegevens worden geïmporteerd                                                                                                                                                                                                        |               Ja                |               Ja               |
| **Datum**       | Datumwaarden en -formaat<br>Je kunt als standaard een datumformaat uit het vervolgkeuzemenu kiezen dat overeenkomt met het CSV-formaat. Om een [aangepast datumformaat](#aangepast-datumformaat) te configureren, klik je op het {% icon gear %} en voer je je formaat in het tekstveld in. |               Ja                |               Ja               |
| **Tijdnotatie**       | De tijdwaarden en het tijdformaat dat wordt gebruikt                                                                                                                                                                                                                          |               Ja                |               Ja               |
| **Tijdstempel**  | Tijdstempelwaarden met een [aangepast tijdstempelformaat](#aangepast-tijdstempelformaat-met-datum-en-tijd)<br>De kolom verschijnt als je **Datum en tijd in een kolom** selecteert.                                                                              |               Ja                |               Ja               |
| **Aangeboden**    | Aangeboden contacten (per interval voor gegevens op intervalbasis)<br>Ondersteunt hele getallen of decimale getallen met een punt.                                                                                                                                            |               Ja                |               Ja               |
| **Behandeld**    | Beantwoorde contacten (per interval voor gegevens op intervalbasis)<br>Ondersteunt hele getallen en decimale getallen met een punt.<br>Voor gegevens op contactbasis kan de waarde voor behandelde contacten alleen 0 of 1 zijn (of decimalen).                                              |               Ja                |               Ja               |
| **AHT**        | Gemiddelde afhandeltijd per interval<br> Ondersteunde formaten zijn seconden (heel getal) of ss:hh:mm:ss (bijvoorbeeld 00:05:00).<br>Als er geen AHT-kolom is, selecteer dan **Geen kolom**.<br>Het veld wordt alleen weergegeven voor gegevens op intervalbasis.                           |                Nee                |               Nee                |
| **Tijdsduur**   | Duur van de opname in seconden (geheel getal).<br>Het veld wordt alleen weergegeven voor gegevens op contactbasis.                                                                                                                                                                        |                Nee                |               Ja               |
| **Kanaal**    | Vaste kanaalnaam (eerste vervolgkeuzemenu) of selecteerbare kolom met kanaalnaam (tweede vervolgkeuzemenu)<br>Toegestane waarden: calls, chats, emails, social_media, documents, cases                                                        |               Ja                |               Ja               |

#### Vervolgkeuzemenu's agentstatus

Als je **Agentstatussen** hebt geselecteerd als het importgegevenstype, dan worden de volgende elementen op de standaard toewijzingspagina weergegeven:

| Veld                   | Beschrijving                                                                                                                                                                                                                                                                          | Vereist |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **Agenten-ID**    | Unieke ID voor de agent, bijv. ID of naam                                                                                                                                                                                                                                     | Ja      |
| **Activiteiten-ID** | Activiteit waar de agent aan werkt                                                                                                                                                                                                                                                     | Ja      |
| **Startdatum**          | Datum waarop de agent met de activiteit is begonnen<br>Je kunt als standaard een formaat uit het vervolgkeuzemenu kiezen dat overeenkomt met het formaat van je CSV-bestand. Om een [aangepast datumformaat](#aangepast-datumformaat) te configureren, klik je op het {% icon gear %} en voer je je formaat in het tekstveld in.   | Ja      |
| **Starttijd**          | Tijd waarop de agent met de activiteit is begonnen                                                                                                                                                                                                                                         | Ja      |
| **Start tijdstempel**     | [Tijdstempel met aangepast formaat](#aangepast-tijdstempelformaat-met-datum-en-tijd) met de datum en de tijd waarop de agent met de activiteit is begonnen<br>De kolom verschijnt als je **Datum en tijd in een kolom** selecteert.                                                                 | Ja      |
| **Einddatum**            | Datum waarop de agent met de activiteit is gestopt<br>Je kunt als standaard een vast datumformaat uit het vervolgkeuzemenu kiezen dat overeenkomt met je formaat. Om een [aangepast datumformaat](#aangepast-datumformaat) te configureren, klik je op het {% icon gear %} en voer je je formaat in het tekstveld in. | Nee       |
| **Eindtijd**            | Tijd waarop de agent met de activiteit is gestopt                                                                                                                                                                                                                                         | Nee       |
| **Einde tijdstempel**       | [Tijdstempel met aangepast formaat](#aangepast-tijdstempelformaat-met-datum-en-tijd) met de datum en de tijd waarop de agent met de activiteit is gestopt<br>De kolom verschijnt als je **Datum en tijd in een kolom** selecteert.                                                                 | Nee       |

#### Aangepast datumformaat

Je kunt een aangepast datumformaat instellen dat overeenkomt met de datum in je CSV-bestanden. Voer de volgende tekens in het invoerveld van **Aangepast datumformaat** in:

- voor de dag: **D** (enkele getallen 1-9) of **DD** (voor voorloopnul)
- voor de maand: **M** (enkele getallen 1-9) of **MM** (voor voorloopnul)
- voor het jaar: **YY** of **YYYY**

Alle overige tekens gelden als scheidingsteken.

Voorbeelden:

| Datum     | Aangepast datumformaat |
| -------- | ------------------ |
| 13/1,22  | D/M,YY             |
| 010122   | DDMMYY             |
| 13012022 | DDMMYYYY           |

#### Aangepast tijdstempelformaat met datum en tijd

Om een aangepast tijdstempelformaat toe te voegen, dien je eerst de optie **Datum en tijd in één kolom** te activeren.
Behalve het [aangepaste datumformaat](#aangepast-datumformaat) moet je nog een tijdformaat instellen. Gebruik hiervoor alleen kleine letters.

- voor uren: **h** (enkele getallen 1-9) of **hh** (voor voorloopnul)
- voor minuten: **m** (enkele getallen 1-9) of **mm** (voor voorloopnul)
- (optioneel) voor seconden: **s** (enkele getallen 1-9) or **ss** (voor voorloopnul)

Voorbeelden:

| Datum en tijd  | Tijdstempelformaat |
| -------------- | ---------------- |
| 13/1,22 9:15:8 | D/M,YY h:m:s     |
| 010122 09-15   | DDMMYY hh-mm     |

### De kolommen toewijzen (SQL-query)

Voor de meeste CSV-bestanden kun je de standaardtoewijzing gebruiken via de vervolgkeuzemenu's. Als je externe systeem CSV-bestanden genereert waarin bepaalde door het standaard toewijzingsformulier vereiste kolommen ontbreken (als ze bijvoorbeeld aanvullende berekeningen vereisen of niet-ondersteunde formaten bevatten), dan werkt de [standaard toewijzingsmethode](#de-kolommen-toewijzen) wellicht niet voor je. Wijs de kolommen in dat geval toe met een SQL-query SQLite). Zo kun je bijvoorbeeld totaalwaarden omzetten in gemiddelden of een oproepvolume berekenen aan de hand van meerdere kolommen. Deze toewijzingsmethode is alleen beschikbaar voor contactgegevens, en kan niet worden gebruikt voor agentstatusgegevens.

#### Vereisten

Houd rekening met de volgende vereisten bij het schrijven van een SQL-query voor kolomtoewijzing:

- Gebruik `uploaded_file` als tabelnaam.
- Gebruik kleine letters voor kolomnamen.
- Gebruik datumtijd als gegevenstype voor de tijdstempelkolom `YYYY-MM-DD hh:mm:ss`).
- Gebruik de [SQLite](https://www.sqlite.org)-querysyntax.

De SQL-query [SQLite](https://www.sqlite.org) ondersteunt wiskundige operaties, dataconversies en kolomaliassen (om afwijkende kolomnamen toe te wijzen). Op sqlite.org vind je meer informatie over de beperkingen van de volgende items:

- [numerieke nauwkeurigheid](https://www.sqlite.org/datatype3.html)
- [wiskundige functies](https://www.sqlite.org/lang_mathfunc.html)
- [impliciete dataconversies](https://www.sqlite.org/datatype3.html#affinity)
- [datum- en tijdfuncties](https://www.sqlite.org/lang_datefunc.html)
- [stringmanipulatie](https://www.sqlite.org/lang_corefunc.html#string_functions)

Ga als volgt te werk om de kolommen via SQL-query toe te wijzen:

> Als de toewijzingsmethode wordt gewijzigd, wordt een bestaand CSV-schema overschreven.
>
> Als je al leen CSV-schema hebt aangemaakt, wordt het bestaande schema door het nieuwe overschreven zodra je de toewijzingsperiode wijzigt. Je kunt een CSV-schema niet herstellen nadat het is overschreven.

1. Activeer het schuifje bij **SQL-query gebruiken om kolommen toe te wijzen** rechtsboven op de kolomtoewijzingspagina.
2. Voer een SQL-query (SQLite) in het tekstveld in. Tip: Kopieer en plak de onderstaande voorbeeldquery's, op basis van je behoefte.

Als je contactgegevens op interval- en contactbasis wilt uploaden, dan dien je een afzonderlijke integratie toe te voegen en twee afzonderlijke SQL-query's aan te maken.

### Kolommen vereist in SQL-query

In de volgende tabel vind je een overzicht van de vereiste kolommen in een SQL-query:

> Afhankelijk van je [WFM-plan](https://www.injixo.com/pricing/) zijn mogelijk niet alle kanalen voor de injixo-bronqueue beschikbaar.

| Kolomnaam | Gegevenstype | Vereist | Gegevens                                                                                                                                                                                                  |
| ----------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| queue       | String    | Ja      | ID voor de queue                                                                                                                                                                                 |
| timestamp   | Datetime  | Ja      | Start van het interval in het formaat YYYY-MM-DD hh:mm:ss                                                                                                                                                  |
| offered     | Heel getal   | Ja      | Aantal contacten (bijv. oproepen of e-mails) tijdens de interval                                                                                                                                               |
| answered    | Heel getal   | Ja      | Op intervalbasis: Aantal contacten dat tijdens de interval is verwerkt<br>Op contactbasis: De waarde 1 geeft aan dat het contact is verwerkt. Dew aarde 0 geeft aan dat het contact niet is verwerkt. |
| aht         | Float     | Nee       | Gemiddelde afhandeltijd voor alle contacten in het interval                                                                                                                                                   |
| duration    | Heel getal | Ja      | Totale afhandeltijd voor een enkel contact                                                                                                                                                                  |
| channel     | String    | Ja      | ID voor het kanaal van de injixo-bronqueue<br>Toegestane waarden: calls, chats, emails, social_media, documents, cases                                                                            |

#### Basisvoorbeeldquery's

Contactgegevens op intervalbasis:

```sql
SELECT
   queue, timestamp,
   offered, handled, aht,
   channel
FROM uploaded_file
```

Contactgegevens op contactbasis:

```sql
SELECT
   queue, timestamp,
   offered, handled, duration,
   channel
FROM uploaded_file
```

De volgende geavanceerde voorbeelden laten zien hoe je wiskundige operaties en SQLite-functies toepast:

#### Geavanceerde voorbeeldquery 1

- Deel HandleTime door HandledCalls voor de vereiste gemiddelde afhandeltijd (AHT).
- Gebruik SUBSTR om datum en tijd te combineren voor het vereiste tijdstempelformaat YYYY-MM-DD HH:MM:SS.

|   Queue    |    Date    | Time  | Received | HandledCalls | Aband | HandleTime | HoldTime |
| :--------: | :--------: | :---: | :------: | :----------: | :---: | :--------: | :------: |
| test queue | 06/03/2023 | 07:30 |    5     |      5       |   -   |   1324.6   |    -     |
| test queue | 06/03/2023 | 08:00 |    2    |      2       |   -   |    1548    |    -     |

```
SELECT
  Queue as queue,
  SUBSTR(Date, 7, 4) || '-'|| SUBSTR(Date, 1, 2) || '-' || SUBSTR(Date, 4,2) || ' ' || Time || ':00' as timestamp,
  Received as offered,
  HandledCalls as handled,
  HandleTime/HandledCalls as aht,
  'chats' as channel
FROM uploaded_file
```

#### Geavanceerde voorbeeldquery 2

- Gebruik `date('now')` in SQLite om de actuele datum te verkrijgen en deze met de tijd uit het bestand te combineren.
- Rond decimalen af tot gehele getallen.
- Gebruik SUBSTR om datum en tijd te combineren voor het vereiste tijdstempelformaat YYYY-MM-DD HH:MM:SS.

In dit voorbeeld bevatten de kolomkoppen lege tekens 

| Queue Name | Hour in hh:mm | Offered calls | Handled Calls | Average Handling Time       |
| :--------: | :-----------: | :-----------: | :-----------: | :-------------------------: |
| demo queue |     07:00     |      3.4      |      2.9      |          00:05:30           |
| demo queue |     08:30     |      5.7      |      5.2      |          00:10:15           |

Je kunt de kopregel vervangen door de opties voor Voorbewerken van de integratie te gebruiken:

- Sla de eerste regel(s) over: verwijdert de oorspronkelijke kopregel
- Kopregel toevoegen: Voegt kolomkoppen met letters toe

```
 SELECT
   A as queue,
   DATE('now')||' '|| "B"||':00' as timestamp,
   FLOOR(C) as offered,
   FLOOR (D) as handled,
   (CAST(substr(E, 1, 1) AS INTEGER) * 3600) +
   (CAST(substr(E, 3, 2) AS INTEGER) * 60) +
   CAST(substr(E, 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

Als je de kopregel niet vervangt, verwijs dan naar de kolomnamen en gebruik daarbij dubbele aanhalingstekens: 

```
 SELECT
   "Queue Name" as queue,
   DATE('now')||' '|| "Hour in hh:mm"||':00' as timestamp,
   FLOOR("Offered Calls") as offered,
   FLOOR ("Handled Calls") as handled,
   (CAST(substr("Average Handling Time", 1, 1) AS INTEGER) * 3600) +
   (CAST(substr("Average Handling Time", 3, 2) AS INTEGER) * 60) +
   CAST(substr("Average Handling Time", 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

#### Geavanceerde voorbeeldquery 3

- Bereken de afgehandelde oproepen door AbandonedCalls van OfferedCalls af te trekken.
- Zet de speciaal geformatteerde Start string om in het vereiste tijdstempelformaat YYYY-MM-DD HH:MM:SS.

|  Name  |       Start       | OfferedCalls | AbandonedCalls | AverageHandlingTime |
| :----: | :---------------: | :----------: | :------------: | :-----------------: |
| queue1 | 20230613 15:30:00 |      10      |       2        |         300         |
| queue2 | 20230613 15:35:00 |      15      |       3        |         450         |
| queue3 | 20230613 15:40:00 |      12      |       2        |         350         |

<!-- notes for database integrations -->
<!-- In this example, the date time format in the Start column is not supported by built-in SQLite `datetime()` and `strftime()` functions. You need to change the string first. -->
<!-- changed the example from datetime(substr(Start, 1, 4) || '-' || to substr(Start, 1, 4) || '-' || -->
<!-- `datetime` is not required here, but in database integrations it would be needed due to the reqiured datetime datatype in the table around line 210 -->

```
SELECT
  Name as queue,
    substr(Start, 1, 4) || '-' ||
    substr(Start, 5, 2) || '-' ||
    substr(Start, 7, 2) || ' ' ||
    substr(Start, 10, 8) as timestamp,
  Offered as offered,
  (Offered - Abandoned) as handled,
  AverageHandlingTime as aht,
  'calls' as channel
FROM uploaded_file
```

<!-- do not change the heading, used in the integrations UI -->

## Een CSV-schema bewerken

Als de gegevensstructuur van een CSV-bestand verandert, dan moet het CSV-schema van een CSV-integratie worden bewerkt.

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Klik op het pictogram Bewerken {% icon pencil | icon-only %} naast de integratie die je wilt verwijderen.
3. Klik op _CSV-schema bewerken_{:.doc-button}.
   Je kunt de opties in de sectie **Setup** wijzigen. Om de voorbewerkingsopties te wijzigen, klik je op _Bestand opnieuw uploaden_{:.doc-button} en upload je een bewerkt of het originele CSV-bestand.
4. Klik op _Ga naar toewijzing_{:.doc-button}. Indien gewenst, kun je de toewijzing van je kolommen wijzigen.
5. Klik op _Schema opslaan_{:.doc-button}.

> Layout van gegevens kan niet worden gewijzigd.
>
> Als je een CSV-schema bewerkt, dan kun je de eerder ingestelde layout van gegevens (bijvoorbeeld, op contact- of intervalbasis) niet wijzigen.

## Voorbeelden van toewijzingen

In deze sectie vind je voorbeelden van CSV-bestanden en bijbehorende toewijzingen. Je kunt de voorbeelden gebruiken als sjabloon voor je eigen CSV-bestanden.

### Contactgegevens (op intervalbasis)

CSV-bestand:

```

Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
My Inbound Queue;25/05/2020;08:00;15;14;230
My Inbound Queue;25/05/2020;08:15;16;15;210
My Inbound Queue;25/05/2020;08:30;20;18;235
My Inbound Queue;25/05/2020;08:45;18;15;215

```

<!-- left-align all tables -->
<style>
table {
   margin-left: 0px;
}
</style>

Kolomtoewijzingen:

| Kolom      | Toegewezen kolom/waarde |
| ----------- | ------------------- |
| Naam van queue  | Queue               |
| Datum        | Date                |
| Datumformaat | dd/mm/yyyy          |
| Tijd        | Time                |
| Tijdformaat | hh:mm               |
| Binnenkomend     | IncomingCalls       |
| Behandeld     | AnsweredCalls       |
| AHT         | AHT                 |
| AHT-formaat  | Seconds             |

In dit voorbeeld is geen kanaalkolom opgenomen. Selecteer in de CSV-schemaconfiguratie de optie **Kanaal**. Om het kanaal in te stellen voor bijv. oproepen, selecteer je **Oproepen** in het vervolgkeuzemenu.

### Contactgegevens (op contactbasis)

CSV-bestand:

```

Queue;Date;Time;Offered;Answered;Duration
My Inbound Queue;25/05/2020;08:00;1;1;100
My Inbound Queue;25/05/2020;08:03;1;0;0
My Inbound Queue;25/05/2020;08:04;1;1;120
My Inbound Queue;25/05/2020;08:07;1;0;0

```

Kolomtoewijzingen:

| Kolom      | Toegewezen kolom/waarde |
| ----------- | ------------------- |
| Naam van queue  | Queue               |
| Datum        | Date                |
| Datumformaat | dd/mm/yyyy          |
| Tijd        | Time                |
| Tijdformaat | hh:mm               |
| Binnenkomend     | Offered             |
| Behandeld     | Answered            |
| Tijdsduur    | Duration            |

In dit voorbeeld is geen kanaalkolom opgenomen. Selecteer in de CSV-schemaconfiguratie de optie **Kanaal**. Om het kanaal in te stellen voor bijv. oproepen, selecteer je **Oproepen** in het vervolgkeuzemenu.

### Agentstatus

CSV-bestand:

```

StartDate;StartTime;AgentID;AgentActivityID
2022-04-22;08:34:29;816;1013;
2022-04-22;08:34:42;816;1015;
2022-04-22;08:34:48;816;1015;
2022-04-22;08:39:11;816;1015;

```

Kolomtoewijzingen:

| Kolom              | Toegewezen kolom/waarde |
| ------------------- | ------------------- |
| Agenten-ID    | AgentID             |
| Activiteiten-ID | AgentActivityID     |
| Startdatum          | StartDate           |
| Datumformaat         | yyyy-mm-dd          |
| Starttijd          | StartTime           |
| Tijdformaat         | hh:mm:ss            |

## CSV-bestanden importeren

Zodra je je CSV-integratie hebt opgeslagen, kun je CSV-bestanden importeren.
De volgende bestandscoderingen worden ondersteund:

- UTF-8
- ISO-8859-1/Latin-1
- ISO-8859-9
- Windows-1252

Gebruik UTF-8 om algemene foutmeldingen te voorkomen.

### Automatische bestandsimport

[Configureer een CSV-integratie](#een-nieuwe-csv-integratie-configureren) en maak verbinding met injixo Cloud Link. injixo Cloud Link uploadt nieuwe gegevens naar injixo. Telkens wanneer er een nieuw CSV-bestand in de installatiemap van injixo Cloud Link wordt opgeslagen, wordt er standaard een nieuwe upload gestart. De standaard installatiemap (C:\\Program Files\\injixo Cloud Link) kan tijdens de installatie worden gewijzigd.

Als alternatief kun je ook een afzonderlijke {% link_new importmap | features/acd-integration/cloud/install-cloud-link.md | #importmap-configureren %} instellen voor bestanduploads. Sla de nieuwe bestanden daarna in de importmap op.

Nadat er gegevens zijn geüpload, kun je {% link_new nieuwe queues aan een workload toevoegen | features/forecast/injixo-forecast/manage-workloads.md %} in Forecast, of de geüpdate gegevens worden in je bestaande workloads weergegeven. Als er geen gegevens worden geüpload, gebruik dan de handmatige bestandsimport die hieronder wordt beschreven om te controleren of je bestandsformaat geldig is. 

### Handmatige bestandsimport

Je kunt gegevens handmatig in injixo uploaden met een webpagina.

Zodra je [een CSV-integratie hebt toegevoegd](#een-nieuwe-csv-integratie-configureren), kun je handmatig gegevens uploaden (je kunt de installatie van injixo Cloud Link overslaan).

1. Ga naar [https://www.injixo.com/csv-importer](https://www.injixo.com/csv-importer).
2. Klik op de link **open je bestandsverkenner** en selecteer een CSV- of TXT-bestand dat je wilt importeren (of sleep het in de browser).
3. Selecteer in het vervolgkeuzemenu linksonder je CSV-integratie.
4. Klik op _Bestand importeren_{:.doc-button}.
   Om foutmeldingen te voorkomen, moet het bestandsformaat overeenkomen met het [CSV-schema](#een-csv-schema-aanmaken).
5. Klik op _Gegevens verwerken_{:.doc-button} om de gegevens te uploaden.

Nadat je gegevens zijn verwerkt, kun je {% link_new de queues aan een workload toevoegen | features/forecast/injixo-forecast/manage-workloads.md %} in injixo Forecast. De maximale bestandsgrootte is 7 MB.

## Veelgestelde vragen

| Vraag                                                                  | Antwoord                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kan ik hetzelfde bestand twee keer importeren?                                         | Ja, maar alleen als je handmatig gegevens importeert. Niet als je Cloud Link gebruikt. Om duplicaten te vinden, berekent injixo tijdens het importeren controlesommen. Geïmporteerde bestanden met dezelfde controlesum worden niet opnieuw geïmporteerd. Als het bestand dezelfde naam heeft, maar een andere inhoud, dan wordt het gewoon geïmporteerd. |
| Verwijdert injixo de automatisch geïmporteerde CSV-bestanden na het importeren? | Nee. Geïmporteerde bestanden blijven in de clientmap van injixo Cloud Link Je kunt ze handmatig verwijderen of zelf een terugkerende taak instellen.                                                                                                                                              |
| Kan ik een CSV-bestand importeren dat toekomstgegevens bevat?                        | Dat is mogelijk, maar houd er rekening mee dat injixo toekomstgegevens niet overslaat, maar deze opslaat als historische gegevens. Je kunt nog steeds een forecast berekenen, maar de grafieken voor geschiedenis en forecast zullen elkaar overlappen.                                               |
