---
title: injixo API verwenden
product_label:
  - advanced
  - enterprise
promote-service: enhanced-reporting
---

In diesem Artikel lernst Du:
* wo Du die Dokumentation der Endpunkte findest.
* wie Du einen persönlichen Zugangstoken erstellst.
* wie die Autorisierung funktioniert.
* wie Du Daten abfragst.
* welche Fehler auftreten können.

Die injixo API bietet Zugriff auf WFM-bezogene Daten, wie Mitarbeiterinnen und Mitarbeiter, Planungseinheiten, Schichtpläne oder Mitarbeiterbedarf.

Wenn Du mit dem REST-API-Konzept oder BI-Tools nicht vertraut bist, teile diesen Link mit den API-Spezialisten in Deiner IT-Abteilung.

> URL-Änderung: Diese API ist nun über legacy-api.injixo.com erreichbar
>
> Die URL dieser API wurde in **legacy-api.injixo.com** geändert. Die alte URL bleibt zunächst gültig, so dass Du genug Zeit hast, Deine aktuellen API-Abfragen zu ändern. Die neue injixo API-Dokumentation ist unter [https://api.injixo.com](https://api.injixo.com) verfügbar.

## API-Referenz: Verfügbare Endpunkte

Die API-Referenz [legacy-api.injixo.com](https://legacy-api.injixo.com) beschreibt alle verfügbaren Endpunkte und zugehörige Parameter. Um mehr über Abfrage-Parameter und Rückgabewerte zu erfahren, Wähle einen Endpunkt aus und klicke auf den grünen Balken in der Mitte. Um die vollständige URL anzuzeigen, klicke auf das Feld mit dem Endpunkt ganz oben rechts.

{{ 1 | image: "injixo API v1 endpoints" }}

## Autorisierung: Persönlicher Zugangstoken

injixo API nutzt ein Bearer Token für die Autorisierung.

> Standardmäßig können nur Benutzer mit *Admin-Zugriff* persönliche Zugangstoken erstellen.  
>   
> Um anderen Benutzerrollen diese Berechtigung zu erteilen, {% link_new bearbeite die Benutzerrolle | getting-started/configure-user-roles.md %}. Gehe im Abschnitt **Berechtigungen** zu *Module > Mein Profil > Persönliche Zugangstoken*{:.breadcrumbs} und aktiviere die Checkbox.

Erstelle Deinen persönlichen Zugangstoken in Deinem **Benutzerprofil**:

1. Klicke auf **Deinen Namen auf der Startseite**, um ins **Benutzerprofil** zu gelangen.
2. Klicke auf *Persönliche Zugangstoken*{:.menu-item}.
3. Klicke auf *Neuen Token anlegen*{:.doc-button}
4. Gib eine Beschreibung für Deinen persönlichen Zugangstoken ein.
5. Klicke auf *Neuen Token anlegen*{:.doc-button}.
6. Kopiere den erzeugten Token.
7. Klicke auf *Fertig*{:.doc-button}.

{{ 2 | image: 'Token kopieren', '40%' }}

Der Token wird Dir nur einmal bei der Erstellung angezeigt und kann später nicht noch einmal aufgerufen werden. Speichere den Token an einem sicheren Ort.

Alle Tokens werden automatisch ungültig, wenn Dein Benutzerkonto gelöscht/gesperrt wird oder wenn Dir der *Admin-Zugriff* entzogen wird.

## Daten abfragen

Verwende für jede Datenabfrage zwei Request-Header:

* `content-Type: application/json`  
* `authorization: Bearer {Dein persönliches Zugangs-Token}`

Der folgende Screenshot zeigt die beiden Header im [Advanced Rest Client](https://install.advancedrestclient.com/install) (ARC):

{{ 3 | image: 'ARC example GET Request - Endpunkt `/v1/planning_units` Planungseinheit ID 1001' }}

### Pfad- und Abfrage-Parameter

Die Request-URL benötigt weitere Parameter, die bestimmen, welche Daten abgefragt werden und wie das Ergebnis aussieht.

* **Pfad-Parameter sind erforderlich.**  
  Diese enthalten oft IDs oder ein Startdatum und beziehen sich auf Entitäten aus dem WFM-Bereich. Nutze injixo, um die korrekten ID zu ermitteln. Datumsparameter haben immer das Format *YYYY-MM-DD*, z.B. `/v1/planning_units/1001/planning_units/2020-01-01`.  

* **Abfrage-Parameter (Query Parameters) sind optional.**  
  Diese können das Ergebnis einer Abfrage einschränken oder erweitern, z.B. die Länge eines Zeitraums über *length* oder *end_date*. Verwende **?** für den ersten und **&** für alle anderen Parameter, z.B. `?end_date=2020-03-31&paid=true`.

  {{ 4 | image: 'Query and Path parameter example', '75%' }}

### Display= Parameter

Normalerweise enthält das Abfrage-Ergebnis alle verfügbaren Felder (die je nach Endpunkt unterschiedlich sein können). Um nur bestimmte Felder zurückzugeben, verwende den Parameter **display=**, z.b. gibt `activities?display=activity_id,name,paid` nur drei Felder zurück.

### Auf Daten in Ebenen zugreifen

Einige Endpunkte unterstützen den Parameter *level=*, um Daten aus einer Ebene zu lesen. Die Namen der Ebenen in der injixo API unterscheiden sich von den Ebenen im Schicht Center und Schedules.

injixo API         | injixo
------------------ | -------
plan               | Plan
final              | Aktueller Stand
wishes             | Wunsch
alternative_wishes | Ausweichwunsch
absence_wishes     | Urlaubs-/Abwesenheitswunsch (Schedules), Abwesenheitswunsch (Schicht Center)
acd                | Externes System
time_recording     | Zeiterfassung
availabilities     | Verfügbarkeit
backup             | Version 1
backup_version_2   | Version 2
backup_version_3   | Version 3

Um mehr über die verschiedenen Ebenen zu erfahren, lies den Artikel {% link_new Tipps zur Schicht Center Nutzung | best-practices/tips-on-shift-center-usage.md | #tipp-9-arbeiten-mit-verschiedenen-ebenen %}.

### Antwortformate

Standardmäßig liefert die injixo API die Daten in JSON zurück, unterstützt aber auch CSV und XML. Um ein anderes Antwortformat zu verwenden, füge Deiner URL neben dem Endpunkt eine Endung hinzu, z. B. `/planning_units/1001/contracts/2018-12-31.csv?length=7`.

### Timeouts

Das feste Standard-Timeout beträgt 25 Sekunden. Die Ausführungszeit von Abfragen kann abhängig von den gewählten Parametern und dem Zeitraum variieren. Läuft eine Abfrage in ein Timeout, versuche, die angeforderte Datenmenge pro Abfrage zu begrenzen, z. B. durch die Verwendung kürzerer Zeiträume oder anderer Abfrage-Parameter.

## Troubleshooting

Eine erfolgreiche Abfrage gibt den Status `200` zurück. Die häufigsten Ursachen für einen anderen Status sind fehlende Daten, falsche Abfrage-Parameter oder ein falscher Authorization-Header.

Status  | Meldung | Ursache
------- | ------- | -------
404 | `"id": "not_found"` oder `"message": "not_found"` | Die angeforderte ID existiert nicht, es sind keine Daten für abgefragten Zeitraum verfügbar oder Dein Benutzer hat unzureichende Rechte. Wiederhole die Abfrage für eine ID oder einen anderen Zeitraum.
401 | `"message": "Invalid token"` | Ungültiger/falscher Personal Access Token. Prüfe/korrigiere den verwendeten Token im Authorization-Header. Erneuere ihn, falls nötig.

## Beispiel-Abfrage mit Curl

Beispiel-Abfrage (Zeile beginnend mit *curl*) und entsprechende Antwort für JSON und CSV:

```
curl -H "Content-Type: application/json" -H "Authorization: Bearer MmU5OTM4MTAzMWfakeVjYWU4NjViACDhZWU3ZTU2NTc=" https://legacy-api.injixo.com/v1/employees

{
   "employees":[
      {
         "birth_date":"1900-01-01",
         "birth_place":"",
         "color":13026816,
         "current_identification":"",
         "deleted":false,
         "employee_id":1001,
         "last_name":"Mustermann",
         "first_name":"Max",
         "personnel_number":"1001",
         "schedule_position":0,
         "automated_shift_assignment":true
      }
   ]
}
```

```
curl -H "Content-Type: application/json" -H "Authorization: Bearer MmU5OTM4MTAzMWfakeVjYWU4NjViACDhZWU3ZTU2NTc=" https://legacy-api.injixo.com/v1/employees.csv

automated_shift_assignment;birth_date;birth_place;color;current_identification;deleted;employee_id; first_name;last_name;personnel_number;schedule_position
true;1900-01-01;"";13026816;"";false;1001;Max;Mustermann;1001;0
```

## Dein eigener Report

Die injixo API folgt der Struktur des injixo-Datenmodells. Elemente, wie z.B. Qualifikationen, Aktivitäten, Tagesmodelle, Verträge, Mitarbeiter, miteinander in Beziehung stehen. Mitarbeiter werden in Planungseinheiten und Auswahlen gruppiert. Schichtpläne, Bedarfe und viele weitere Elemente werden pro Planungseinheit zurückgegeben. Lies die {% link_new Hinweise zur Stammdaten-Erstellung | getting-started/set-up-base-configuration.md %}, um diesen Zusammenhang zu verstehen, falls Du ihn noch nicht kennst.

Beispiel: Wenn Du wissen willst, welche/wie viele Agenten in einem bestimmten Zeitraum verfügbar sind, frage  `/schedules` ab, um alle Aktivitäten und Schichten zu erhalten. Um die angezeigten IDs durch die Namen der Elemente zu ersetzen, frage auch `/activities` und `/employees` ab und kombiniere die Ergebnisse.

Planung eines Reports:  

1. Lege den Umfang Deines Reports fest.
2. Ermittle die für Dich relevanten Daten. Im Normalfall musst Du mehrere Endpunkte abfragen, um alle Informationen zu erhalten.
3. Finde in der API-Referenz die richtigen Endpunkte.
4. Frage die Daten ab
5. Verarbeite die Daten weiter, z.B. in Excel oder mit einer Programmiersprache Deiner Wahl. Rechne mit den Rohdaten, um Zahlen in Köpfe oder Stunden umzurechnen oder Daten für monatliche Statistiken zu gruppieren.
