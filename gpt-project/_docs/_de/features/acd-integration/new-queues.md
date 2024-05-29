---
title: Neue Rufnummer in den Xlink-Datenimport aufnehmen
product_label:
  - on-premise
---

In diesem Artikel lernst Du, wie Du injixo, Xlink und injixo Forecast anpassen musst, wenn Du eine neue Rufnummer mit einem planungsrelevanten Volumen anbinden möchtest.

## Neue Queue anlegen

Handelt es sich um eine neue Rufnummer für deren Volumen Du einen eigenen Forecast erstellen möchtest, lege für die neue Rufnummer eine {% link_new neue Queue | features/forecast/forecastpro/administration/queues.md %} an. Dies gilt auch, wenn Du injixo Forecast verwendest.

Hinweis: Du benötigst keine neue Queue, wenn das Volumen der Rufnummer ein bestehendes Xlink-Queue-Mapping erweitern soll.

## CSV-Schnittstellen anpassen

Um einem CSV-Import eine neue Rufnummer hinzuzufügen, muss die CSV-Datei (gemäß Deiner aktuellen Schnittstellen-Konfiguration) Daten wie Name, Datum, Zeit und Volumen enthalten. Zusätzlich musst Du die Konfiguration der CSV-Schnittstelle anpassen.

Du benötigst Administrator-Rechte auf dem Computer, auf dem Xlink läuft.

1. Öffne die Datei _isps_ul.ini_ im Xlink-Ordner.
2. Gehe zum Abschnitt mit dem Namen Deines externen Systems, z. B. _[CSV-Import]_.
3. Der Parameter _Groups=_ enthält alle Namen der Rufnummern aus Deiner CSV-Datei. Füge dem Parameter _Groups=_ den Namen der neuen Rufnummer hinzu (genau wie in der CSV-Datei enthalten), getrennt mit Semikolon.
   Hinweis: Setze kein Semikolon ganz am Ende der Zeile.
4. Speichere und schließe die Datei _isps_ul.ini_.
5. Starte den _ISPS Xlink_-Dienst neu, um die Änderungen in der Datei _isps_ul.ini_ zu übernehmen.

Der Xlink kennt jetzt die neue Rufnummer. Stelle für einen Nachimport historischer Daten sicher, dass eine CSV-Datei mit Daten für die neue Rufnummer im konfigurierten Quellverzeichnis liegt.

## ODBC-Schnittstellen anpassen

Starte die _isps_ul.exe_ im Xlink-Ordner neu. Die neue Rufnummer erscheint links in der Baumstruktur im Xlink, wenn diese in der Datenbank hinzugefügt wurde. Du musst an der Konfiguration in der Datei _isps_ul.ini_ nichts ändern.

## Mapping erweitern (Xlink)

Um Daten für die neue Queue zu importieren, musst Du in der Datei _isps_ul.exe_ {% link_new Anrufdaten mappen | features/acd-integration/xlink-mapping-telephony.md %}.

Soll das Volumen der Rufnummer eine bestehende Queue erweitern, suche auf der rechten Seite zuerst die vorhandene Queue und erweitere das Mapping für die einzelnen Wertetypen. Handelt es sich um eine neue Rufnummer für einen separaten Forecast, erstelle ein neues Mapping für die neu erstellte Queue.

Nutzt Du Xlink mit injixo Forecast, erstelle im Xlink ein Eins-zu-Eins-Mapping.

## Daten nachimportieren

1. Klicke in der Xlink-Oberfläche oben links auf das **Flaggen-Symbol**.
2. Wähle einen Zeitraum für den Nachimport.
3. Klicke _OK_{:.doc-button}.

Hinweis: Die Option _Nullwerte schreiben_ sollte im Xlink ausgeschaltet sein, um Zeiträume, für die keine Daten vorliegen, nicht mit Nullen zu überschreiben.

## Workloads in injixo Forecast bearbeiten

{% link_new Bearbeite Deine Workloads | features/forecast/injixo-forecast/create-workloads.md %} und füge die neue Queues hinzu, um das Volumen der neue Queues in einen bestehenden Forecast einfließen zu lassen.

Erstelle einen neuen Workload, wenn Du basierend auf dem Volumen der neuen Queue einen komplett eigenen Forecast erstellen möchtest.
