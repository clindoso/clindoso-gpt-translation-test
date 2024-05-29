---
title: Umstieg auf eine neue ACD
product_label:
  - on-premise
redirect_from:
  - /de/xlink-acd-system-update/
promote-service: acd-integration-support
---

Bei einem Update/Austausch Deiner ACD musst Du je nach Ausgangssituation auch ein paar Dinge für die Xlink-Konfiguration beachten.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

## Update der ACD-Version/Server-Adresse

Ändert sich nur die Version der eingesetzten ACD ohne Änderungen am Datenbanksystem oder der Datenstruktur (beispielsweise Avaya Contact Center Version 6.4 auf 7.0), gibt es nur zwei Dinge, die Du bei einer Änderung anpassen musst:

- Die Server-Adresse in der ODBC-Verbindung
- Benutzer und Passwort in der ODBC-Verbindung

## Aktualisiertes Datenbanksystem

Wenn sich das Datenbanksystem ändert (beispielsweise Avaya CIE Version 3.2 auf Version 3.3, vorher Informix, jetzt Postgresql), muss auf dem Xlink-Server eine neue ODBC-Verbindung (System-DSN) mit einem neuen ODBC-Treiber erstellt und diese in der Xlink-Konfiguration hinterlegt werden.

### Update von ODBC-Verbindungsdaten im Xlink

ODBC-Verbindungsinformationen wie Name, Benutzer und Passwort kannst Du über die Benutzeroberfläche `isps_ul.exe` anpassen. Dort auf der linken Seite die ACD markieren, dann über den Menüeintrag _ACD > Konfiguration_{:.breadcrumbs} die ODBC-Informationen ändern.

### Ist ein neues Mapping erforderlich?

Neue bzw. geänderte IDs oder Namen auf ACD-Seite erfordern ggf. eine Anpassung des Mappings über die `isps_ul.exe` oder auch durch Suchen & Ersetzen in der `acd_map.ini`. Mehr zum Thema Mapping findest Du {% link_new hier | features/acd-integration/xlink-mapping-telephony.md %}.

## Änderung ACD-Hersteller

Ändert sich die komplette ACD, beispielsweise durch einen Hersteller-Wechsel, überprüfe als erstes, wie dieser Hersteller die Daten bereitstellt. Teile uns dies mit, zusammen mit dem Namen des neuen Herstellers und der ACD-Version.

Neben der frei konfigurierbaren Universal-Schnittstelle und einer CSV-Schnittstelle, stellen wir einige Standard-Schnittstellen bereit.
Bei Nutzung der Universal-Schnittstelle kannst Du die notwendigen Daten auch in einem Datenbank-View konsolidieren und diesen View abfragen, ein Beispiel findest Du {% link_new hier | features/acd-integration/universal-with-views.md %}.
Als Xlink-Ersatz bietet die injixo Cloud eine dateibasierte Integration (CSV) sowie native Integrationen. Erfahre mehr darüber {% link_new wie Integrationen funktionieren | features/acd-integration/cloud/how-integrations-work.md %}.

Erstelle ein komplett neues externes System unter _Administration > System > Externe Systeme_{:.breadcrumbs} für die neue ACD-Anbindung über den Xlink. Anschließend kannst Du die Konfiguration entsprechend der Beschreibung für {% link_new ODBC | features/acd-integration/xlink-configuration-import-odbc.md %} oder {% link_new CSV | features/acd-integration/xlink-configuration-import-csv.md %} durchführen.

## Parallelbetrieb mit ACD-Testsystem

Wenn ein Parallelbetrieb der alten und neuen Umgebung gewünscht ist, kannst Du die neue ACD parallel als weiteres externes System unter _Administration > System > Externe Systeme_{:.breadcrumbs} hinterlegen. Führe die Konfiguration entsprechend der Beschreibung für {% link_new ODBC | features/acd-integration/xlink-configuration-import-odbc.md %} oder {% link_new CSV | features/acd-integration/xlink-configuration-import-csv.md %} durch.

Die neue ACD erscheint dann auf der linken Seite im Xlink als zusätzliches externes System.

Die einzige Besonderheit ist, dass die Daten nicht in die bereits bestehenden WFM-Queues fließen sollten, sondern in eine _Testqueue_. Lege dazu eine oder mehrere neue WFM-Queues an und erstelle ein {% link_new Mapping | features/acd-integration/xlink-mapping-telephony.md %} für die neue Telefonanlage. Ein {% link_new Testmapping für Aktivitäten | features/acd-integration/xlink-mapping-activities.md %} kannst Du erstellen, indem Du die externen IDs aus dem neuen System zuordnest.

Entferne zum Tag der Live-Schaltung das alte Mapping und die alte Konfiguration und verknüpfe dann die neuen ACD-Queues auf die bestehenden WFM-Queues über das Mapping.

1. Erstelle ein Backup der `acd_map.ini` und `isps_ul.ini`.
2. Lösche Referenzen zur alten ACD aus `acd_map.ini`.
3. Lösche die Sektion für das alte externe System aus der `isps_ul.ini`.
4. Lösche die alte ODBC-Verbindung (wenn diese nicht weiterverwendet wird).
5. Starte den `ISPS Xlink`-Dienst neu.
6. Erstelle ein neues Mapping für {% link_new Queues | features/acd-integration/xlink-mapping-telephony.md %} bzw. {% link_new Aktivitäten | features/acd-integration/xlink-mapping-activities.md %} für die neue Telefonanlage.

Der ganze Prozess ist nicht zeitkritisch, da die ACD Daten für einige Wochen vorhält. Ein Nachimport von Daten von dem Zeitpunkt an, wo die neue Telefonanlage mit realen Daten bespielt wird, ist daher auch später möglich.
