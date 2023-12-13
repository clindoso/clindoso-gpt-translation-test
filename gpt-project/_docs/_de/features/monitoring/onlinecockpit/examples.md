---
title: Beispiele
product_label:
  - on-premise
---

Hier findest Du Beispiele für die Verwendung des *OnlineCockpit*{:.menu-item}, die zeigen, was alles möglich ist und die Dich für Deine eigenen Vorlagen inspirieren sollen.

Wir unterteilen die Beispiele in Ansichten zu Tageswerten und Tagesintervallwerten.

## Tageswerte

### Schichtbedarf und Anmeldungen

Das Diagramm zeigt, wie viele Schichten in der Planperiode für einen bestimmten Tag aus einem Tagesmodell erzeugt worden sind (rote Balken) und wie viele Anmeldungen es dafür bereits in injixo Me gibt (grüne Linie).

{{ 1 | image: 'Schichtbedarf und Anmeldungen', '75%' }}

### Schichtbedarf, Anmeldungen und Besetzung

#### Nach Verlosung

Das Diagramm zeigt den Zustand nach der Verlosung. Die Anmeldungen (grüne Linie) sind zu im Schichtplan disponierten Schichten (blaue Linie) geworden. Die grüne Linie zeigt, dass an mehreren Tagen ein Teil der gewünschten Schichten nicht verlost werden konnte. Aus welchen Gründen die Schichten nicht verlost werden konnten und welche Planungsregeln die Verlosung verhindert haben, wird aus dem Verlosungsprotokoll ersichtlich, welches Dir nach der Verlosung angezeigt wird, wenn Du die Option `Verlosungsprotokoll erzeugen` vor der Verlosung aktiviert hast.

Um die größtmögliche Besetzung der Schichten mit Mitarbeitern zu erreichen, werden die bei der Verlosung nicht besetzten Schichten zugeteilt.

{{ 2 | image: 'Schichtbedarf, Anmeldungen und Besetzung nach Verlosung', '75%' }}

#### Nach Zuteilung

Das Diagramm zeigt die Besetzung der benötigten Schichten nach der Zuteilung. Der erzeugte Schichtbedarf für diese Schicht kann somit nach Verlosung und Zuteilung annähernd gedeckt werden. Aus welchen Gründen nicht alle Schichten zugeteilt werden konnten und welche Planungsregeln die Zuteilung verhindert haben, wird aus dem Zuteilungsprotokoll ersichtlich, welches Dir nach der Zuteilung angezeigt wird, wenn Du die Option `Zuteilungsprotokoll erzeugen` vor der Zuteilung aktiviert hast.

{{ 3 | image: 'Schichtbedarf, Anmeldungen und Besetzung nach Zuteilung', '75%' }}

### Mitarbeiterbedarf, Besetzung und Nettomaximalkapazität

Im Beispieldiagramm wird der Mitarbeiterbedarf (hellblaue Balken) mit der Besetzung (rote Linie) und der Maximalkapazität (Linie mit roten Markierungen) pro Aktivität und pro Tag verglichen. Der Wert auf der linken Achse entspricht dabei der auf den Tag verteilten durchschnittlichen Mitarbeiteranzahl.

{{ 4 | image: 'Mitarbeiterbedarf, Besetzung und Nettomaximalkapazität', '75%' }}


## Tagesintervallwerte

### Schichtbedarf und Besetzung mit Deckungsdifferenz

Im Diagramm wird der Schichtbedarf (hellblaue Balken) mit der Besetzung (rote Linie) verglichen. Die Deckungsdifferenz wird durch die grüne Linie dargestellt. Die Schichten unterhalb der Nulllinie bis zur grünen Linie konnten nicht besetzt werden

{{ 5 | image: 'Schichtbedarf und Besetzung mit Deckungsdifferenz', '75%' }}

### Mitarbeiterbedarf, Besetzung, Nettomaximalkapazität pro Aktivität

In den beiden Diagrammen wird für jeweils eine Aktivität der Mitarbeiterbedarf mit der Besetzung und der Maximalkapazität an einem Tag verglichen.

{{ 6 | image: 'Mitarbeiterbedarf, Besetzung, Nettomaximalkapazität pro Aktivität', '75%' }}

Für alle Kennzahlen kannst Du Dir auch die Gesamtwerte aller Aktivitäten einer Planungseinheit in einem Diagramm anzeigen lassen.

{{ 7 | image: 'Gesamt-Bedarf, Gesamt-Besetzung Plan und Gesamt-Besetzung lt. Schichtbedarf und Gesamt-Deckung lt. Schichtbedarf', '75%' }}

## Weitere Beispiele:

### Vergleich mehrerer Freitage

{{ 8 | image: 'Vorgangsvolumen für mehrere Wochen', '75%' }}

Die folgende Abbildung zeigt die Diagramme von importierten Vorgangskurven für zwei Wochen, in denen jeweils am Freitag eine Werbeaktion stattgefunden hat und für Wochen, in denen keine Werbeaktion stattgefunden hat. Auf diese Weise lässt sich die gleiche Kennzahl für beliebige, nicht aufeinanderfolgende Zeiträume vergleichen.

### Reale historisch Daten vs. Forecast

{{ 9 | image: 'Historisches und prognostiziertes Vorgangsvolumen als aktuelle Intervallwerte', '75%' }}

Die grafische Darstellung vergleicht das geplante Vorgangsvolumen der Forecast-Version (blaue Linie) mit den importierten (aktuell vom externen System in der Version Historisch registrierten) Daten. Dieser Vergleich ermöglicht eine schnelle Reaktion, falls die Realität erheblich von der Planung abweicht. Die Daten werden in der Tabelle als Summenwerte im Intervall von 30 Minuten dargestellt. Die aktuelle Uhrzeit im Diagramm ist 16:30 Uhr.
