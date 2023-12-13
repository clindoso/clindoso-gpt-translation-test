---
title: Schichtfolgen anlegen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/capacity/capacity-insert-shift-sequences.md
---

Eine Schichtfolge ist ein Set von Tagesmodellen oder Aktivitäten, das regelmäßig wiederholt wird. Schichtfolgen können Dir stundenlangen Aufwand ersparen, indem Du diese mit wenigen Klicks in den Schichtplan einfügst.

In diesem Artikel lernst Du:
- wie Du Schichtfolgen erstellst.
- wie Du sie bearbeitest und löschst.
- einige praktische Beispiele für die Anwendung von Schichtfolgen.

Es gibt eine Vielzahl unterschiedlicher Verwendungsmöglichkeiten für Schichtfolgen, hier einige Beispiele:

* Erstelle einen fixen Schichtplan mit Tagesmodellen vom Typ *Fixe Schicht*.
* Erstelle sich wiederholende oder rotierende Muster, wie z.B. Früh-, Spät- und Nachtschichten.
* Plane wiederkehrende Aktivitäten wie Teambesprechungen oder 1:1 Meetings.
* Decke einen konstanten Mitarbeiterbedarf.
* Füge Verfügbarkeitszeiträume für Mitarbeiter ein.
* Plane freie Tage an Wochentagen oder Wochenenden.

Zum Anlegen von Schichtfolgen sind [Aktivitäten][1] oder [Tagesmodelle][2] erforderlich, die [Mitarbeitern zugeordnet][3] werden.

## Schichtfolgen erstellen

Navigiere zu *WFM > Administration > Scheduling > Schichtfolgen*{:.breadcrumbs} und folge diesen Schritten:

1. Klicke auf das grüne *+*{:.doc-button} in der Aktionsleiste.
2. Trage den **Namen** ein (max. 50 Zeichen).
3. Gib eine **Kurzbezeichnung** ein (max. 25 Zeichen).
4. Lege die **Anzahl der Mitarbeiterzeile(n)** fest (max. 53). Jede Zeile stellt eine eigene Rotation dar; auswählbar bei der Mitarbeiterzuordnung.
5. Bestimme über die **Länge** die Dauer der Schichtfolge in Tagen (max. 371 Tage = 53 Wochen). Die kürzeste Länge sollte 7 Tagen entsprechen. Die Länge sollte *immer* durch 7 teilbar sein.
6. Speichere Deine Angaben mit *OK*{:.doc-button}.

Füge nach dem Speichern ggf. **Gültigkeitszeiträume** hinzu. Dadurch ist es möglich, diese Schichtfolge für einen bestimmten Zeitraum zu verwenden. Klicke dazu auf den *Stift*{:.doc-button} oberhalb der Tabelle.

> Vielfaches von 7 als Länge der Schichtfolge
>
> Es ist wichtig, die Länge einer Schichtfolge immer als ein Vielfaches von 7 zu definieren, auch wenn Dein Contact Center nur an fünf oder sechs Tagen in der Woche geöffnet ist.
> Da sich die Schichtfolge sofort und nicht jede Woche Montag wiederholt, wird bei einer fünftägigen Schichtfolge die zweite Montagsschicht auf Samstag, die Dienstagsschicht auf Sonntag usw. gelegt.

### Tagesmodelle einfügen

Ordne einer Schichtfolge Tagesmodelle oder Aktivitäten zu. Tue dies im Bereich **Optionen**.

> Verwende Aktivitäten oder fixe Tagesmodelle
>  
> Der Schichtbeginn von variablen Tagesmodellen wird beim Einfügen in den Schichtplan fest auf die frühestmögliche Startzeit gesetzt.

1. Wähle **Tagesmodell einfügen** aus dem Auswahlfeld.
2. Wähle das gewünschte Tagesmodell aus dem Dropdown-Menü **Tagesmodell**.
3. Ändere den Wert im Feld **Anzahl**, um die Anzahl der aufeinander folgenden Tage anzugeben, um mehrere Tage automatisch auszufüllen.
4. Weise ein Tagesmodell mit einem **Klick in eine Zelle** der Tabelle zu (z.B. Montag - Woche 1).
5. Wiederhole diesen Vorgang, um die gesamte Schichtfolge aufzubauen.

Es gibt keine *Speichern*-Option. Die Schichtfolge wird *automatisch* gespeichert.

### Aktivitäten einfügen

1. Wähle **Aktivität einfügen**.
2. Wähle die gewünschte Aktivität aus dem Dropdown-Menü **Aktivität** aus.
3. Ändere den Wert im Feld **Anzahl**, um die Anzahl der aufeinander folgenden Tage anzugeben, um mehrere Tage automatisch auszufüllen.
4. Gib eine **von** und **bis** Zeit ein, um den Zeitraum der Aktivität zu definieren oder hake **ganztägig** an.

> Aktivitäten, die nach 24:00 Uhr enden
>  
> Füge für solche Aktivitäten einfach die Endzeit zu 24 hinzu. Gib für eine Endzeit von 1:00 Uhr am nächsten Morgen beispielsweise 25:00 Uhr ein.

### Inhalt anpassen oder löschen

Lösche Tagesmodelle oder Aktivitäten aus einer Schichtfolge im Abschnitt *Optionen*; führe dazu die folgenden Schritte aus:

1. Wähle **Löschen** aus dem Dropdown-Menü.
2. **Klicke auf eine Zelle**, um den entsprechenden Eintrag zu löschen.
3. Setze das Häkchen bei *Alle löschen*{:.doc-button}, um bei Bedarf alle Einträge auf einmal zu entfernen.

### Zeilennamen anpassen

Nach dem Speichern kannst Du die vorgegebene Bezeichnung jeder Mitarbeiterzeile ändern, z.B. in *Früh/Spät* bzw. *Spät/Früh* oder nutze einfach den Namen des Mitarbeiters. Dies erleichtert die Identifizierung der richtigen Zeile bei der Zuordnung zum Mitarbeiter und beim [Schichtfolgen einfügen][4]. Klicke dazu in die erste Zelle der Zeile und passe den Namen an. Wiederhole dies für alle gewünschten Zellen.

## Schichtfolgen bearbeiten

Befolge diese Schritte:

1. Wähle die zu bearbeitende Schichtfolge aus der Auswahlliste aus.
2. Klicke auf *Anwenden*{:.doc-button}.
3. Klicke auf den *Stift*{:.doc-button} in der oberen Aktionsleiste, um den Namen, die Abkürzung, die Anzahl der Mitarbeiterzeilen und die Länge zu bearbeiten.
4. Klicke in der Aktionsleiste über der Tabelle auf den *Stift*{:.doc-button}, um die Gültigkeitsdauer zu bearbeiten.

Eine Verkürzung der Länge löscht Teile der Schichtfolge, beginnend mit dem letzten Tag. Eine Verlängerung der Schichtfolge fügt am Ende leere Tage hinzu.

Wenn Du den Wert für Mitarbeiterzeilen änderst, werden die Zeilen ebenfalls gelöscht oder hinzugefügt, beginnend mit der letzten.

## Schichtfolgen löschen

Um die gesamte Schichtfolge zu löschen, öffne die entsprechende Schichtfolge und wähle *Löschen*{:.doc-button} in der Aktionsleiste am oberen Rand.

## Anwendungsbeispiele

Verwende Schichtfolgen für diverse Szenarien.

### Früh- und Spätschichten

Definiere den wöchentlichen Wechsel von Früh- und Spätschichten mit einer Schichtfolge mit einer Dauer von 14 Tagen.

Fülle die erste Zeile. Füge in der ersten Woche Tagesmodelle für Frühschichten und in der zweiten Woche Tagesmodelle für Spätschichten ein. Verfahre umgekehrt in der zweiten Zeile.

Weise die erste Mitarbeiterzeile den Mitarbeitern zu, die die Schichtfolge in der Frühschicht beginnen sollen. Die zweite Mitarbeiterzeile wird den Mitarbeitern zugewiesen, die mit der Spätschicht beginnen sollen. Nutze einen Montag als Referenzdatum.

Das folgende Beispiel zeigt eine 2-wöchige frühe/späte Rotation wie beschrieben.

<iframe width="960" height="136" data-original-width="1426" data-original-height="202" src="https://www.thinglink.com/card/1368166556416081922" type="text/html" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen scrolling="no"></iframe><script async src="https://cdn.thinglink.me/jse/responsive.js"></script>

 Nutze mehr als 2 Wochen, um andere Rotationen zu erstellen.

### Fixe Schichtplanung

Erstelle Tagemodelle vom Typ *Fixe Schicht*, die sich für Mitarbeiter mit bestimmten Arbeitsanforderungen wiederholen. Im Beispiel unten hat Mike darum gebeten, feste Frühschichten (09:00-17:00 Uhr) zu arbeiten, und Sheena möchte jede Woche feste Spätschichten (12:00-20:00 Uhr) bekommen.

{{ 2 | image: 'Schichtfolge mit Tagesmodellen vom Type Fixe Schicht' }}

### Verfügbarkeiten für Teilzeit

Lege die Verfügbarkeit von Mitarbeitern für die Arbeit fest, indem Du Tagesmodelle vom Typ *Verfügbarkeitsrahmen* einfügst. Damit kannst Du Flexibilität in die Schichtfolge einbauen. Bei der Optimierung werden dem Mitarbeiter nur Tätigkeiten und Schichten zugewiesen, die innerhalb dieses Zeitraums liegen.

Im unten stehenden Beispiel ist Barry von Mo bis Fr 10:00-14:00 Uhr verfügbar, Eliza ist von 12:00-16:00 Uhr an Mo, Do, Sa und So verfügbar. Rishi hat gemischte Verfügbarkeiten. Wenn an einem Tag keine Verfügbarkeit in der Schichtfolge hinterlegt ist, sind die Mitarbeiter ohne Einschränkungen planbar.

{{ 3 | image: 'Schichtfolge mit Verfügbarkeitsrahmen' }}

### Ganztägige Blocker für nicht geplante Tage

Füge einen **Blocker** in Form einer ganztägigen, unbezahlten Aktivität hinzu, um nicht geplante Tage zu erzwingen. Das untenstehende Beispiel zeigt eine Schichtfolge, um nicht geplante Tage (AUS) an Wochenenden in Reihe 1, am Montag und Dienstag in Reihe 2 und am Donnerstag und Freitag in Reihe 3 zu erzwingen. Ordne die betreffende Mitarbeiterzeile im Mitarbeiterdatensatz zu.

Mitarbeiter mit ganztägigen Abwesenheiten in der Schichtfolge werden an diesen Tagen nicht geplant.

{{ 4 | image: 'Blocker in einer Schichtfolge' }}

### Wiederkehrende Meetings

Füge Aktivitäten ein und gib eine **von**- und **bis**-Zeit an, um wiederkehrende Besprechungen zu planen. Das Beispiel unten zeigt eine Schichtfolge, die jeden Donnerstag zwischen 09:00-10:00 Uhr eine **Teambesprechung** für Scotts Team und eine **121**-Besprechung (Einzelbesprechung) für jedes Teammitglied um 10:00 Uhr während der Woche vorsieht.

{{ 1 | image: 'Plane wiederkehrende Meetings' }}

> Setze das Referenzdatum immer auf den Beginn der Planungswoche (in der Regel Montag)...
>  
> ... wenn Du {% link_new Mitarbeitern eine Schichtfolge zuweist | features/administration/employee-overview.md | #eine-schichtfolge-zuweisen %}. Andernfalls könnten die Schichtfolgen beim Einfügen versetzt werden und nicht mehr beginnend mit Tag 1 in der jeweiligen Woche eingefügt werden.

## PDF-Report

Der verfügbare Report im PDF-Format dient der Kontrolle Deiner Eingaben. Er zeigt pro Wochentag die Aktivitäten oder Tagesmodelle mit Beginn, Ende und Nettodauer in Stunden an. Generiere den Report über *Report*{:.doc-button} im Bereich *Schichtfolge*. Jede Mitarbeiterzeile erscheint auf einer neuen Seite.

Zusätzlich findest Du Summen- und Durchschnittswerte zur Nettodauer:
* Zeile Summe: Nettodauer aller Aktivitäten oder Tagesmodelle der Schichtfolge.
* Spalte Summe: Summe der Nettodauer der Aktivitäten oder Tagesmodelle pro Woche.
* Zeile Durchschnitt: Durchschnittswert für alle Werte der Spalte Summe an.
