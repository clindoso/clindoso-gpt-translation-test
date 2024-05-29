---
title: Analysiere Deckung, Besetzung und den Bedarf
product_label:
  - advanced
  - enterprise
  - classic
description: Analysiere die Deckung, die Besetzung und den Bedarf für Deine Aktivitäten, verwende den Tab Tagesmodelle richtig.
---

In diesem Artikel lernst Du, wie Du:

- die Deckung, die Besetzung und den Bedarf für Deine Aktivitäten analysierst.
- Bedarf und Besetzung als Diagramme anzeigen kannst.
- Aktivitäten bestimmter Aktivitätstypen ausblenden kannst.
- den Tab _Tagesmodelle_ im Schichtwunsch-Verfahren verwendest. <!-- break down into use cases -->

Neu im Schicht Center? Lerne zuerst {% link_new die Grundlagen | features/scheduling/shiftcenter/shift-center-overview.md %} - insbesondere was das {% link_new Kennzahlenfenster | features/scheduling/shiftcenter/shift-center-overview.md | #kennzahlenfenster %} ist und wie man {% link_new die Anzeige der Daten | features/scheduling/shiftcenter/shift-center-overview.md | #die-darstellung-von-daten-anpassen %} anpasst.

## Deckung analysieren

Die Deckung zeigt, wie die aktuelle Besetzung den Bedarf für Deine Aktivität oder Aktivitätstypen deckt. Sie ist die Differenz zwischen der Anzahl der geplanten und der benötigten Mitarbeiter. Du kannst die Deckung (und andere Kennzahlen) bis auf 15-Minuten-Intervalle für jede der Planungseinheit zugeordneten Aktivitäten und pro Aktivitätstyp analysieren:

1. Klicke auf den Tab **Aktivitäten** und klappe eine Planungseinheit mit einen Klick auf _+_{:.doc-button} auf. Du siehst alle Aktivitäten der Planungseinheit. Multiaktivitäten werden fett gedruckt dargestellt, ihre Unteraktivitäten sind darunter eingerückt. Die Liste zeigt auch Aktivitätstypen an, z.B. fasst die Zeile _Gesamtwerte 'Anwesenheit'_ alle Aktivitäten vom Typ _Anwesenheit_ zusammen.
2. Klicke mit der rechten Maustaste auf eine **Tageszelle** und wähle die Kennzahl **Deckung**. Du siehst dann die Deckung für die verschiedenen Aktivitäten.
3. Wenn Du auf eine **Spaltenüberschrift eines Tages** klickst, klappt dieser auf und zeigt die detaillierte Deckung für die Tagesintervalle. Zoome hinein, um die Werte für noch kleinere Intervalle zu sehen.

Die Zahlen in den Zellen zeigen Dir die Differenz zwischen Bedarf und Besetzung für den jeweiligen Zeitraum. Wenn eine Zelle z.B. -2 anzeigt, dann bist Du um zwei Mitarbeiter unterbesetzt.

Die Farbcodierung der Zellen zeigt Dir sofort, wie gut Deine Deckung ist. Rot zeigt Unterbesetzung, Blau zeigt Überbesetzung und Grün signalisiert ideale Deckung. Je intensiver die Farbe, desto größer ist die Abweichung von der idealen Besetzung.

{{ 2 | image: 'Schicht Center Tab Aktivitäten im Kennzahlenfenster' }}

## Besetzung analysieren

Die Besetzung zeigt die Anzahl der geplanten Mitarbeiter für eine bestimmte Aktivität. Folge den gleichen Schritten wie unter [_Deckung analysieren_](#deckung-analysieren), wähle aber bei Schritt 2 die Kennzahl **Besetzung**.

## Bedarf analysieren

Der Bedarf ist die Anzahl der Mitarbeiter, die Du brauchst, um den Bedarf für ein bestimmtes Intervall und eine bestimmte Aktivität zu decken. Folge den gleichen Schritten wie unter [_Deckung analysieren_](#deckung-analysieren), wähle aber bei Schritt 2 die **Bedarf**-Kennzahl aus.

## Eine Aktivität über mehrere Tage und Wochen analysieren

Du kannst den Tab _Aktivitätsübersicht_ verwenden, um die Deckung, die Besetzung und den Bedarf einer einzelnen Aktivität oder eines Aktivitätstyps über mehrere Tage und Wochen zu analysieren.

1. Klicke auf den Tab **Aktivitätsübersicht** und klappe eine eine Planungseinheit auf, indem Du auf _+_{:.doc-button} klickst. Die Intervalle werden in einer vertikal scrollbaren Ansicht angezeigt.
2. Klicke mit der rechten Maustaste auf eine **Tageszelle**, dann
   - Klicke auf **Aktivität**, und dann auf die Aktivität oder den Aktivitätstyp, den Du analysieren möchtest.
   - Klicke auf **Parameter**, und dann auf die Kennzahl, die Du analysieren möchtest.
   - Klicke auf **Ebene** und dann auf die Ebene, für die Du die gewählte Aktivität und Kennzahl analysieren willst.
3. Nach jeder Auswahl wird die Ansicht auf Deinen Filter aktualisiert. Wiederhole diesen Schritt 2, wenn nötig.

Am Ende kannst Du vertikal durch die Intervalle scrollen und die Werte für die gewählte Aktivität und Kennzahl prüfen. Du kannst auch zusätzliche Wochen aufklappen, um mehr Daten nebeneinander anzuzeigen.

{{ 5 | image: 'Schicht Center Tab Aktivitätsübersicht im Kennzahlenfenster'}}

## Bedarf und Besetzung als Diagramme anzeigen

In den beiden Tabs _Tagesmodelle_ und _Aktivitäten_ kannst Du die Bedarfs- und Besetzungswerte als Diagramme anzeigen.

1. Klicke mit der rechten Maustaste auf eine **Zelle** und wähle **Grafische Darstellung**. Anstelle der Zellen wird ein Diagramm angezeigt. Die gestrichelte Linie stellt die Bedarfswerte dar, die durchgezogene Linie die Besetzungswerte.
2. Um das Diagramm zu vergrößern, fahre mit der Maus über die Ränder der Zelle oben oder unten, bis ein **schwarzer Doppelpfeil** erscheint, der nach oben und unten zeigt. Klicke und ziehe, um die Zelle und damit auch das Diagramm zu vergrößern.
3. Um die Zelle wieder auf ihre ursprüngliche Größe zu verkleinern, doppelklicke auf den **schwarzen Doppelpfeil**.

## Aktivitäten bestimmter Typen ausblenden

Im Tab _Aktivitäten_ zeigt die zweite Spalte links die Aktivitätstypen an. Du kannst bestimmte Aktivitätstypen ausblenden:

1. Rechts-Klicke auf die **leere Spaltenüberschrift der Aktivitätstypen**, um ein Kontextmenü zu öffnen. Standardmäßig ist _Alle_ vorausgewählt.
2. Klicke auf einen oder mehrere **Aktivitätstypen**, um alle Aktivitäten dieses Typs aus der Liste auszublenden.

{{ 4 | image: 'Schicht Center Tab Deckung im Kennzahlenfenster'}}

## Tab Tagesmodelle

Benutze den Tab _Tagesmodelle_, wenn Du mit dem {% link_new Schichtwunsch-Verfahren | features/scheduling/shift-bidding.md %} arbeitest und die Deckungs-, Besetzungs- und Bedarfswerte für eingefügte Schichten sehen möchtest. Die Zahlen basieren auf den Tagesmodellen im Planfenster.

Auf der linken Seite siehst Du eine Liste mit allen Deinen Planungseinheiten. Klicke auf _+_{:.doc-button}, um alle Tagesmodelle der jeweiligen Planungseinheit anzuzeigen.

Um die angezeigten Kennzahlen zu ändern, klicke mit der rechten Maustaste auf eine **Datenzelle** und wähle **Deckung**, **Bedarf**, **Besetzung** oder **Bedarf**. Hier ist, was sie bedeuten:

| Parameter   | Beschreibung                                                                                                                          |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Deckung     | Differenz zwischen der Anzahl der den Mitarbeitern zugewiesenen Tagesmodelle und der Anzahl der erzeugten Schichten.                  |
| Anmeldungen | Anzahl der von Mitarbeitern im Schichtwunsch-Verfahren gewünschten Schichten. Die Werte sind die gleichen wie auf der Ebene _Wunsch_. |
| Besetzung   | Zeigt an, wie viele der erzeugten Schichten durch Mitarbeiter besetzt sind.                                                           |
| Bedarf      | Ergebnis der {% link_new Schichterzeugung                                                                                             | features/scheduling/shift-bidding.md %}. Zeigt an, wie viele Schichten benötigt werden. |

{{ 3 | image: 'Schicht Center Tagesmodell Tab im Kennzahlenfenster'}}

<!-- Separate section for separate use cases?  -->
<!-- Not often used. See how the shift generation covers your requirements before activities have been assigned. Good indicator for the shift generation result.
| Parameter | Beschreibung |
| ----------- | ----------- |
| Maximale Nettokapazität | Maximal verfügbare Anzahl von Mitarbeitern, die bereits für die Aktivität geplant und qualifiziert sind. Zählt nur Mitarbeiter mit einer zugewiesenen Aktivität vom Typ *Anwesend*. |
| Besetzung nach Schichtbedarf | Anzahl der von der Schichtgenerierung generierten Tagesmodelle zur Deckung des Mitarbeiterbedarfs für die Aktivität. Du kannst bewerten, wie gut die Schichtgenerierung funktioniert hat. |
| Deckung gemäß Schichtbedarf | Differenz zwischen den Schichten, die benötigt werden, um 100% des Schichtbedarfs zu decken und den tatsächlich durch die Schichtgenerierung generierten Schichten. | -->
