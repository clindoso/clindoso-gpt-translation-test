---
title: Anrufdaten mappen
product_label:
description: Konfiguriere Xlink, um Daten aus Deinen ACD-Queues oder Skills in den richtigen injixo-Queues zu speichern.
redirect_from: /de/xlink-mapping-telephony/
redirect_reason: renamed file in April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/generate-xlink-scripts.md
---

In diesem Artikel lernst Du:

- wie Du Mappings für Anrufdaten in Xlink erstellst, bearbeitest und löschst.
- wie Mappings in Deiner Xlink-Installation gespeichert werden.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

Der Anrufdatenimport (PhoneLink) erfordert ein Mapping zwischen injixo-Queues und externen Kennzahlen.

Die verfügbaren Kennzahlen hängen von Deinem externen System und der injixo-Importschnittstelle ab. Typischerweise liefern die Schnittstellen Kennzahlen wie angebotene und angenommene Anrufe sowie durchschnittliche/gesamte Bearbeitungszeiten. Ein Dokument (TechDoc) für jede Schnittstelle liefert weitere Details. Die TechDocs sind im Xlink-Bereich der [Download-Seite](https://www.injixo.com/support/downloads) verfügbar.

## Mappings erstellen

Du kannst eine oder mehrere Queues aus Deinem externen System auf eine Queue-Werttyp-Kombination in injixo mappen. Um alle Vorteile von injixo Forecast zu nutzen, solltest Du Eins-zu-Eins-Mappings erstellen.

1. Gehe ins Xlink-Installationsverzeichnis und öffne die Xlink-Benutzeroberfläche **isps_ul.exe**.
2. Wähle eine **Queue** im Abschnitt _WFM-Queue_ auf der rechten Seite.
3. Klicke auf das **Plus-Symbol** neben der Queue, um die Wertetypen zu auszuklappen. Wähle einen **Werttyp**.
4. Doppelklicke auf den **Wertetyp** im Abschnitt _Schnittstelle_ auf der linken Seite, die Du dem Mapping hinzufügen möchtest. Dieser wird im Abschnitt _Zugeordnete Wertetypen_ angezeigt.
5. Doppelklicke auf den **Wertetyp** im Abschnitt _WFM-Queue_ auf der rechten Seite, um ein Berechnungsskript zu erstellen oder zu bearbeiten. Das Standardskript berechnet die Summe aller hinzugefügten Wertetypen. Du kannst es als Vorlage zum {% link_new Erstellen eigener Skripte | features/acd-integration/generate-xlink-scripts.md %} verwenden.
6. Klicke im neuen Fenster auf _Erstellen_{:.doc-button}, um ein neues Standardskript zu erstellen.
7. Klicke auf _OK_{:.doc-button}, um das Skript zu speichern.

Xlink-Importe führen nun das Berechnungsskript für das entsprechende Mapping aus und speichern die Ergebnisse in der Kombination aus Queue, Werttyp und Version in injixo.

### Wie werden Mappings gespeichert?

Die Datei _acd_map.ini_ im Xlink-Ordner enthält eine Zeile pro Mapping und eine Zeile für die zugehörige Skriptdatei (.bas-Datei). Der fortlaufende Name der .bas-Datei hängt davon ab, wie viele .bas-Dateien bereits existieren.

```
iWFM R4 Hamburg:1:1002:1003=InvisionAcd1:Service 1:Calls
iWFM R4 Hamburg:1:1002:1003=InvisionAcd2:Dienst 2:Anrufe
iWFM R4 Hamburg:1:1002:1003=$1.BAS
```

Das Gleichheitszeichen teilt jede Zeile in zwei Teile; jeder Teil wird wiederum durch Doppelpunkte getrennt. Der linke Teil enthält den Namen, der im Abschnitt _[DB]_ in der Datei _isps_ul.ini_ definiert ist, sowie ID der übergeordnete Queue, der Queue und des Werttyps aus injixo. Auf der rechten Seite werden die Namen aus der Baumansicht des externen Systems angezeigt, oder (im Falle einer .bas-Datei) der entsprechende Dateiname.

Hinweis: Die Reihenfolge der Zeilen hängt von der Reihenfolge ab, in der Du die Schritte zur Erstellung der Mappings ausgeführt hast. Vermeide es, die Datei manuell zu ändern, da dies zu falschen Werten führen oder sogar den Importprozess unterbrechen kann.

## Zuordnungen bearbeiten/entfernen

1. Gehe ins Xlink-Installationsverzeichnis und öffne die Xlink-Benutzeroberfläche **isps_ul.exe**.
2. Wähle eine **Queue** im Abschnitt _WFM-Queue_ auf der rechten Seite.
3. Klicke auf das **Plus-Symbol** neben der Queue, um die Wertetypen zu erweitern. Wähle einen **Werttyp**.
4. Doppelklicke auf einen **Mapping-Eintrag** im Abschnitt _Zugeordnete Werttypen_, um diesen zu entfernen.
5. Doppelklicke auf den **Wertetyp** im Abschnitt _WFM-Queue_ auf der rechten Seite, um das vorhandene Skript zu entfernen/bearbeiten.
6. Lösche den Skript-Inhalt vollständig, oder bearbeite diesen, wenn sich die Anzahl/Reihenfolge der zugeordneten Parameter ändert.
7. Klicke auf _OK_{:.doc-button}, um das Skript zu speichern.
