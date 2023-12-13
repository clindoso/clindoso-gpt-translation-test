---
title: Erstellen von Diagrammen
product_label:
  - on-premise
---

In der Baumstruktur links, dem sogenannten Kennzahlenverzeichnis, kannst Du Kennzahlen zur Anzeige auswählen. Diese werden auf der untersten Ebene der Baumstruktur angezeigt. Sind der Planungseinheit keine Aktivitäten oder der Queue keine Wertetypen zugeordnet, lässt sich die Baumstruktur an dieser Stelle nicht weiter öffnen.

Unter Queues werden alle in der *Administration*{:.menu-item} angelegten Queues mit deren zugeordneten Wertetypen angezeigt. Für jeden Wertetyp werden die Versionen Historisch und (Auto-)Forecast angezeigt.

Unter Planungseinheiten werden alle Planungseinheiten und, wenn vorhanden, untergeordnete Einheiten angezeigt. Zu jeder Planungseinheit werden die in der *Administration*{:.menu-item} zugeordneten Aktivitäten sowie alle in der Administration angelegten Tagesmodelle als Schichten angezeigt.

> Hinweis
>
> Wenn eine Aktivität im OnlineCockpit angezeigt werden soll, muss sie in der *Administration*{:.menu-item} definiert und der Planungseinheit zugeordnet sein. Das gilt auch für die Auswertung von Daten für die Aktivitätstypen `Pause`, `Urlaub`, `Krankheit` und `Meeting`. Auch virtuellen Planungseinheiten müssen die Aktivitäten zugeordnet sein, für die eine Anzeige gewünscht wird.

## Einzelnen Tag darstellen

Um eine Kennzahl auszuwählen, gehe wie folgt vor:

1. Öffne mit *Neue Vorlage öffnen*{:.doc-button} eine Vorlage mit einem neuen leeren Diagrammfenster.
2. Wähle für die Ansicht Tagesintervallwerte aus und stelle das Datum des gewünschten Tages im Feld Startdatum ein.
3. Klicke auf *+*{:.doc-button} vor dem entsprechenden Verzeichnis der Baumstruktur, bis die gewünschte Kennzahl auf der untersten Ebene angezeigt wird.
4. Klicke mit der linken Maustaste auf die Kennzahl, halte die Maustaste gedrückt und ziehe damit die ausgewählte Kennzahl per Drag & Drop in das Diagrammfenster.
5. Es öffnet sich ein Dialog mit den Eigenschaften für die Kennzahl.
6. Bestätige die Auswahl mit *Ok*{:.doc-button}.

Nach Anzeige der ersten Kennzahl kannst Du jede weitere Kennzahl, für die der gleiche Zeitraum gilt, per Drag & Drop im selben Diagrammfenster anzeigen lassen, oder diese für einen anderen Zeitraum in jeweils einem weiteren Diagrammfenster pro Anzeigezeitraum darstellen.

**Eigenschaften zur Darstellung**  

Eigenschaften sind z.B. die Farbe, der Grafiktyp oder die Achsenanordnung bzw. die Skalierung, bei Queues zusätzlich der Wertetyp und die Version.

Die Option `Skalierung` ermöglicht es Dir, dass Du für jede vertikale Diagrammachse einen Faktor eingeben kannst, mit dem die Tabellenwerte multipliziert werden sollen. Standardeinstellung ist 1. Die vertikalen Achsen passen sich bei Änderung der Skalierung automatisch an. Damit kannst Du ein Verhältnis für den Wertebereich der linken zur rechten Achse angeben. Der Wert 2 in Verbindung mit der Auswahl der linken Achse bedeutet z.B., dass der Wertebereich der linken Achse doppelt so hoch ist, wie der der rechten Achse.

### Verschiedene Tage vergleichen

Du kannst auch Kennzahlen unterschiedlicher Tage übereinander legen und miteinander vergleichen, z.B. die importierten Datenvolumina für jeden Tag einer Woche oder für jeweils den Montag aus unterschiedlichen Wochen.

Gehe wie folgt vor:

1. Aktiviere `Verschiedene Tage vergleichen`.
2. Gib bei Startdatum das Anzeigedatum der nächsten Kennzahl an.
3. Füge die nächste Kennzahl in das Diagrammfenster ein.
4. Für weitere Tage gehst Du analog vor.

{{ 1 | image: 'Historisches Vorgangsvolumen von verschiedenen Tagen'}}

Das Diagramm zeigt die importierten Vorgänge für drei Freitage im Oktober. Auf diese Weise lässt sich die gleiche Kennzahl für beliebige, nicht aufeinanderfolgende Tage oder Ereignistypen im selben Diagramm vergleichen.

## Zeitraum ansehen (Einzelwerte pro Tag)

Diagramme und Tabellen kannst Du für einen Zeitraum von mehreren Tagen, Wochen oder Monaten erstellen. Der Zeitraum, den Du für die Ansicht auswählen kannst, ist auf maximal 3 Jahre beschränkt. Erstelle ein Diagram wie für einen Einzeltag, aber wähle die Option `Tageswerte`.

Es wird ein Wert pro Tag als Tagessumme bzw. Tagesdurchschnitt angezeigt. Dieser wird nur anhand der Werte innerhalb der Öffnungszeiten berechnet.

1. Öffne mit *Neue Vorlage öffnen*{:.doc-button} eine Vorlage mit einem neuen leeren Diagrammfenster.
2. Wähle als Ansicht Tageswerte aus und gib Start- und Enddatum an.
3. Wähle anschließend die anzuzeigende Kennzahl und ziehe sie in das aktive Diagrammfenster.
4. Wähle im geöffneten Dialog die gewünschten Eigenschaften für die Anzeige aus.
5. Teile anschließend das Diagrammfenster horizontal und/oder vertikal. Wiederhole die Teilung, bis Du über ein Diagrammfenster für jeden Zeitraum verfügst.
6. Definiere nacheinander für jedes Diagrammfenster die Parameter und füge die Kennzahlen ein.

{{ 2 | image: 'Historisches und prognostiziertes Vorgangsvolumen als Tageswerte'}}

Im Diagramm siehst Du das geplante Vorgangsvolumen der Version Forecast und die tatsächlich vom externen System registrierten Werte der Version Historisch im Wochenverlauf. Im Gegensatz zur Darstellung eines einzelnen Tages werden hier für jeden Tag kumulierte Werte angezeigt.

Wenn Du Kennzahlen aus unterschiedlichen Zeiträumen vergleichen möchtest, kannst Du dies in derselben Vorlage, aber in unterschiedlichen Diagrammen tun, denn der eingestellte Zeitraum gilt immer für das aktive Diagrammfenster. Wenn Du Diagrammfenster teilst, kannst Du für jedes Diagrammfenster einen anderen Zeitraum wählen.

Die folgende Abbildung zeigt die Diagramme von importierten Vorgangskurven für zwei Wochen, in denen jeweils am Freitag eine Werbeaktion stattgefunden hat und für Wochen, in denen keine Werbeaktion stattgefunden hat. Auf diese Weise lässt sich die gleiche Kennzahl für beliebige, nicht aufeinanderfolgende Zeiträume vergleichen.

{{ 3 | image: 'Vorgangsvolumen für mehrere Wochen'}}

## Aktuellen Tag darstellen

Daten für den heutigen Tag kannst Du Dir einfach in der Ansicht `Aktuelle Intervallwerte` ansehen. Die vertikale, rote Linie, die Du im Diagramm siehst, zeigt die aktuelle Tageszeit an, die Anzeige aktualisiert sich alle 60 Sekunden.

## Mehr Platz? Komponenten ausblenden

Sind mehrere Diagrammfenster geöffnet, kannst Du den Anzeigebereich für eine bessere Übersicht vergrößern, indem Du über die entsprechenden Buttons den Navigator oder das Kennzahlenauswahlfenster ausblendest. Alternativ kann Du das aktive Diagrammfenster in den Vordergrund stellen.

{{ 4 | image: 'Vordergrund'}}

## Bezeichnung ändern

Die Bezeichnung des Diagramms siehst Du oben auf der linken Seite. Wenn Du einen neuen Titel vergeben möchtest, überschreibst Du den bestehenden Text in der Überschriftszeile. Die Benennung wird automatisch gespeichert.

## Bereits eingefügte Kennzahlen ändern

Du kannst für bereits im Diagramm eingefügte Wertetypen oder Kennzahlen die Eigenschaften wie die Farbe, die Linienart oder die Achsenanordnung bzw. die Skalierung ändern. Wähle die zu verändernde Kurve aus, um den Dialog zum Ändern der Eigenschaften für bereits eingefügte Wertetypen oder Kennzahlen aufzurufen. Die Kennzahl kannst Du sowohl in der Diagramm- als auch in der Tabellenansicht auswählen.

In der Diagrammansicht klickst Du mit der rechten Maustaste auf die Kurve oder auf das dazugehörende Farbfeld in der Legende.

{{ 5 | image: 'Kontextmenü zum Anpassen der Kennzahlen'}}

Wenn Du die Maus über die Überschriftszelle einer Tabellenspalte bewegst, zeigt der Tooltip den dazugehörigen Wertetyp oder die Kennzahl an. Klicke mit der rechten Maustaste in die Überschriftszelle der entsprechenden Tabellenspalte. Wähle im Kontextmenü den Eintrag Eigenschaften, um den Dialog für die Eigenschaften zu öffnen.

## Zeitzonendarstellung

Ein Planer in einer Planungszentrale kann z.B. Schichten aus Planungseinheiten auf mehreren Kontinenten in seiner Ortszeit sehen. Für Kennzahlen gilt die Zeitzone der Planungseinheit bzw. der Queue.

Kennzahlen aus unterschiedlichen Zeitzonen lassen sich in dasselbe Diagramm einfügen. Die Darstellung im Diagramm erfolgt in der Ortszeit des Benutzers.

{{ 6 | image: 'OnlineCockpit mit Zeitversatz'}}

Falls es eine Abweichung zur der Ortszeit des Benutzers gibt, wird diese im Kennzahlenverzeichnis neben dem Namen der Queue/Aktivität angezeigt. In der Aktionsleiste erscheint außerdem die Zeitdifferenz des Benutzers zur UTC.

Schichten, die nach Umrechnung in die Ortszeit des Planers die Tagesgrenze überschreiten, erscheinen auch am Folgetag im Diagramm.
