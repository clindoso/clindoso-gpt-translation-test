---
title: Tageskurven bearbeiten
product_label:
  - on-premise
---

In *Prognose > ForecastPro > Tageskurven bearbeiten*{:.breadcrumbs} kannst Du aus externen Systemen importierte Intervallwerte anpassen, die Du als untypisch betrachtest. Das können beispielsweise Tage mit einem abweichenden Aufkommen oder aber auch Nullwerte durch Ausfälle der ACD sein. Auf dieser Grundlage kannst Du neue typische Tageskurven erstellen. Du kannst die Funktion auch verwenden, um prognostizierte Tageskurven aus dem Forecast der Tageswerte an kurzfristige Änderungen des Vorgangsvolumens bzw. der Vorgangsdauer anzupassen. Die Bedarfsberechnung kann über denselben Menüpunkt gestartet werden, wobei die geänderten Werte berücksichtigt werden.

## Bearbeitungskategorie 'Parameter'

| Queue | Wähle die Queue aus, deren Tageskurven Du kontrollieren oder bearbeiten möchtest. |
| Wertetyp | Wähle den Wertetyp aus, dessen Tageskurven Du kontrollieren oder bearbeiten möchtest. |
| Version | Wähle die Version aus, deren Tageskurven Du kontrollieren oder bearbeiten möchtest. |
| Startdatum | Gib das Startdatum an, ab dem die Tageskurven angezeigt werden sollen. |
| Enddatum | Gib das Enddatum an, bis zu dem die Tageskurven angezeigt werden sollen. |

Bestätige Deine Auswahl mit *Anwenden*{:.doc-button}. Das `Tabellenfenster` und `Diagrammfenster` werden eingeblendet. Alle innerhalb des ausgewählten Zeitraums liegenden Intervallwerte werden in aufsteigender Reihenfolge angezeigt.

Wenn Du Dir mehrere Tageskurven in einem Diagramm anzeigen lässt, sind nicht mehr alle Intervallpunkte einer Tageskurve sichtbar. Sobald Du in der Tabelle eine einzelne Tageskurve zur Bearbeitung auswählst, werden wieder alle zugehörigen Intervallzeiten eingeblendet. Klick auf *Gesamtwerte*{:.doc-button}, um zur Ansicht aller Tageskurven zurückzukehren.

Die Tabelle addiert in der Spalte `Gesamtwerte` für jedes Intervall die Werte aller Kurven. In der Zeile `Summe` werden alle Tagesintervallwerte einer Tageskurve addiert. Die Spalte Gesamtwerte zeigt in der Zeile Summe die Tagesintervallwerte aller Tageskurven. Sie entspricht der Summe aller Vorgänge (bzw. der durchschnittlichen Vorgangsdauer) im Anzeigezeitraum.


> Hinweis
>
> Die Änderungen am Verlauf der Tageskurven werden nicht automatisch gespeichert.

Die Werte der bearbeiteten Tageskurven können in der ausgewählten Version gespeichert werden, indem Du auf *Speichern*{:.doc-button} klickst.

Achtung: Durch Speichern der Versionsdaten in der Version 'Historisch' überschreibst Du Deine importierten Daten.

### Tageskurve erstellen

Du kannst Tageskurven im `Tabellenfenster` sowie im `Diagrammfenster` erstellen oder in der Bearbeitungskategorie `Berechnung` ermitteln. Hierbei bietet sich die Berechnungsfunktion als schnellste Lösung an.

Für Zeilen, in denen der Gesamtwert eines Intervalls 0 beträgt und für Spalten, in denen die Summe aller Intervalle einer Tageskurve ebenfalls 0 beträgt, kannst Du nur Tagesintervallwerte für ein Intervall einer beliebigen Tageskurve eingeben. Die Zeile Summe, die Spalte Gesamtwerte sowie die Summe der Gesamtwerte werden dementsprechend aktualisiert.

Der Kurvenverlauf wird im `Diagrammfenster` angezeigt.

> Hinweis
>
> Um eine Kurve im Diagrammfenster zu bearbeiten, wähle zunächst den entsprechenden Tag in der Tabelle aus. Sobald Du einen Tag in der Tabelle markiert hast, wird im Diagrammfenster nur noch die Kurve dieses Tages angezeigt.

Leg anschließend den Verlauf und die Intervallwerte der Tageskurve fest, indem Du die Intervallpunkte an die gewünschte Position ziehst. Die Tabellenwerte werden dabei aktualisiert.

## Bearbeitungskategorie Berechnung

> Hinweis
>
> Um eine Tageskurve in der Bearbeitungskategorie `Berechnung` zu bearbeiten, wähle zunächst den Tag in der Tabelle aus, für den die Berechnung ausgeführt werden soll.

Die folgenden Optionspaare können für die Berechnung miteinander kombiniert werden.

**Optionspaar 1**

Verwende diese Option für die Erstellung neuer Tageskurven. Gibst Du z.B. für eine Kurve mit Nullwerten die Optionen 'Intervall', 'Überschreiben' und 'Absolut' und den Wert 50 ein, wird für jedes Tagesintervall im angegebenen Intervall der Wert 50 geschrieben.

  - `Intervall`: Aktiviere diese Option, wenn der Wert jedem Tagesintervallwert im angegebenen Intervall in voller Höhe zugeschlagen werden soll.
  - `Tag`: Aktiviere diese Option, wenn der angegebene Wert anteilig auf alle Tagesintervallwerte verteilt werden soll. Diese Option kannst Du nicht zum Erstellen von neuen Tageskurven verwenden.

Für jede Option kannst Du das Kontrollkästchen `Betriebszeiten beachten` aktivieren, wenn die Tageskurve nur innerhalb der Betriebszeiten Deiner Queue erstellt werden soll.

Hast Du Dich für die Berechnung von Intervallen entschieden, führe die Berechnung aus (nacheinander für jedes Intervall unter Angabe der entsprechenden Startzeit und Endzeit). Die Eingabe 00.00 Uhr im Feld Endzeit wird als 24.00 Uhr interpretiert.

> Hinweis
>
> Beachte, dass die Option `Intervall` den angegebenen Wert jedem Tagesintervall in voller Höhe zuschlägt, während die Option `Tag` den Wert anteilig auf alle Tagesintervalle aufteilt. Kurven, die lediglich Null-Werte enthalten, können deshalb nur mit der Option `Intervall` berechnet werden.

**Optionspaar 2**

  - `Aufschlag/Abschlag`: Aktiviere diese Option, wenn der angegebene Wert, entsprechend der gewählten Option Intervall oder Tag in voller Höhe oder anteilig, zu den vorhandenen Tagesintervallwerten addiert bzw. von diesen Werten subtrahiert werden soll.
  - `Überschreiben`: Aktiviere diese Option, wenn jeder Tagesintervallwert, entsprechend der gewählten Option `Intervall` oder `Tag` in voller Höhe oder anteilig, durch den angegebenen Wert überschrieben werden soll.

**Optionspaar 3**

Diese Option kann nicht für die Erstellung neuer Kurven verwendet werden.

  - `Prozentual`: Aktiviere diese Option, wenn der angegebene Wert ein Prozentwert ist, der entsprechend der gewählten Option `Intervall` oder `Tag` auf die Tagesintervallwerte angerechnet werden soll.
  - `Absolut`: Aktiviere diese Option, wenn der angegebene Wert jedem Tagesintervallwert, entsprechend der gewählten Option `Intervall` oder `Tag` in voller Höhe oder anteilig, zugeschlagen werden soll.

Wenn Du die Bedarfsermittlung im Anschluss an die Bearbeitung einer Tageskurve im Menüpunkt *Tageskurven bearbeiten*{:.menu-item} startest, werden die gespeicherten Versionsdaten für die Bedarfsermittlung und Skriptausführung zugrunde gelegt.

Speicher Deine angelegten Kurven in der Version 'Historisch', wenn sie im Menüpunkt *Typische Tageskurve*{:.menu-item} für die Erstellung einer Typischen Tageskurve zur Verfügung stehen sollen.

### Tageskurven bearbeiten

Eine Tageskurve kannst Du im `Tabellenfenster`, im `Diagrammfenster` oder in der Bearbeitungskategorie `Berechnung` bearbeiten.

Folgende Werte können bearbeitet werden:

  - Der Intervallwert einer beliebigen Tageskurve. Die Zeile `Summe` wird aktualisiert. Die Spalte `Gesamtwerte` wird ebenfalls aktualisiert.
  - Die Summe aller Intervallwerte eines Tages, wenn diese nicht gleich 0 beträgt. Alle Intervallwerte des Tages werden aktualisiert. Der Wert wird so auf die Tagesintervalle aufgeteilt, dass das Verhältnis der Werte zueinander gewahrt bleibt. Beträgt der Wert für ein Intervall 0, so bleibt dieser Wert erhalten. Alle Werte in der Spalte Gesamtwerte, einschließlich des Gesamtwertes für alle Summen, werden ebenfalls aktualisiert.
  - Der Gesamtwert aller Summen, sofern dieser nicht gleich 0 beträgt. Alle Intervallwerte aller Kurven werden aktualisiert. Der Wert wird auf alle Intervalle so aufgeteilt, dass das Verhältnis der Wert zueinander gewahrt bleibt. Beträgt der Wert für ein Intervall 0, so bleibt dieser Wert erhalten. Alle Werte in der Zeile `Summe` sowie in der Spalte `Gesamtwerte` werden ebenfalls aktualisiert.
  - Der Gesamtwert aller Kurven für ein Intervall in der Spalte `Gesamtwerte`, sofern dieser nicht gleich 0 beträgt. Alle Tagesintervallwerte werden aktualisiert. Der Gesamtwert wird so auf die Tagesintervallwerte aufgeteilt, dass das Verhältnis der Werte zueinander gewahrt bleibt. Beträgt der Wert für das Intervall für eine Kurve 0, so bleibt dieser Wert erhalten. Alle Werte in der Spalte `Gesamtwerte`, einschließlich des Gesamtwertes für alle Summen, werden ebenfalls aktualisiert.

> Hinweis
>
> Um eine Kurve im `Diagrammfenster` zu bearbeiten, musst Du zunächst den entsprechenden Tag in der Tabelle auswählen. Um zur Übersicht aller Tageskurven zurückzukehren, klick auf die Spaltenüberschrift *Gesamtwerte*{:.doc-button}. Für die Spalte `Gesamtwerte` kann keine Kurve bearbeitet werden. Sobald Du einen Tag in der Tabelle markiert hast, wird im `Diagrammfenster` nur noch die Kurve des ausgewählten Tages angezeigt.

Leg anschließend den Verlauf und die Intervallwerte der Tageskurve fest, indem Du die Intervallpunkte an die gewünschte Position ziehst. Die Tabellenwerte werden dabei aktualisiert.
