---
title: Pausen optimieren
product_label:
  - essential
  - advanced
  - enterprise
permalink: /de/break-optimization/
permalink_reason: /break-optimization/ used in email and in Intercom message
description: Optimiere die Verteilung der Pausen in Deinem Schichtplan, um eine bessere Deckung des Mitarbeiterbedarfs bei allen Aktivitäten zu erreichen.
promote-service: schedule-optimization-workshop
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
---

In diesem Artikel lernst Du:
- wie das Feature *Pausen optimieren* Deinen Schichtplan verbessert.
- wie Du die Pausenoptimierung durchführst.
- wie Du die Ergebnisse der Optimierung anzeigst und analysierst.

## Was ist das Feature *Pausen optimieren*?

Ziel des Features *Pausen optimieren* ist es, die Pausen innerhalb Deines Schichtplans neu zu verteilen, um die Deckung von Aktivitäten, für die Mitarbeiterbedarf besteht, zu optimieren. Die Zeiten für Schichtbeginn und -ende bleiben dabei unverändert. Das Feature *Pausen optimieren* wandelt bestehende Tagesmodelle im Optimierungszeitraum in Aktivitäten um. Die Pausenkorridore in Tagesmodellen bleiben aber bestehen, so dass Du falls nötig weitere Pausenoptimierungen durchführen kannst.

Beispiel: Zwei Mitarbeiter haben eine Schicht mit einer Pause von 12:00 bis 13:00 Uhr. Die Pause kann alle 30 Minuten zwischen 12:00 und 15:00 Uhr beginnen. Um die niedrige Deckung für die Basisaktivität der Schicht zwischen 12:00 und 13:00 zu verbessern, wird injixo mindestens eine der Pausen auf eine spätere Zeit verschieben.

### Einschränkungen

Das Feature *Pausen optimieren* setzt voraus, dass bereits ein Schichtplan in der Ebene *Plan* existiert. Pausen können nur in diejenigen Zeiträume verschoben werden, die Aktivitäten vom Typ *Anwesenheit* enthalten. Es können außerdem nur bewegliche Pausen in Pausen-Korridoren optimiert werden. Feste Pausen werden nicht berücksichtigt. *Pausen optimieren* läuft maximal 60 Minuten und nutzt die beste in dieser Zeit gefundene Lösung.

## Eine Pausenoptimierung ausführen

1. Gehe zu *Plan > Schedules*{:.breadcrumbs}.
2. Klicke auf _Planungsaktionen_{:.doc-button} und wähle **Pausen optimieren** aus.
3. Wähle eine **Planungseinheit**. Die Planungseinheit ist vorausgewählt, wenn in Schedules eine Planungseinheit ausgeklappt ist.
4. Wähle eine **Auswahl** (optional) von Mitarbeitern, für die Du die Pausenoptimierung durchführen willst.
5. Wähle einen **Zeitraum** für die Pausenoptimierung. Du kannst den heutigen Tag und jedes Datum in der Zukunft wählen. Der aktuell in *Schedules* ausgewählte Datumsbereich ist standardmäßig eingetragen.
6. Klicke auf *Pausen optimieren*{:.doc-button}, um die Pausenoptimierung zu starten. <!-- do NOT explain feature-flag-based *Use Smart Optimization* checkbox--> Es erscheint eine grüne Benachrichtigung, wenn sie erfolgreich gestartet werden konnte. Andernfalls erscheint eine rote Benachrichtigung. Du kannst den Fortschritt einer laufenden Optimierung unter *WFM > Administration > System > JobProcessor*{:.breadcrumbs} verfolgen.

Der Optimierungsprozess kann einige Zeit dauern, abhängig von der Anzahl der Mitarbeiter, der Anzahl der Pausen im Schichtplan und der Länge des Optimierungszeitraums. Während die Optimierung läuft, kannst Du keine Änderungen im Datumsbereich vornehmen, der gerade optimiert wird. Wenn die Optimierung beendet ist, speichert injixo das Ergebnis automatisch. Der Status im Abschnitt *Optimierungshistorie* aktualisiert sich nach der Fertigstellung automatisch.

  {{ 5 | image: 'Übersicht Joboptimierung'}}

## Optimierungsstatus verstehen

Jede abgeschlossene Optimierung führt zu einem Eintrag im Abschnitt *Optimierungshistorie* mit einigen Details wie Startzeit, Benutzer, Planungseinheit, Auswahl und dem Optimierungszeitraum. Die Spalte *Status* enthält einen der folgenden Werte:

* *Optimierter Plan*: Die Pausenoptimierung war erfolgreich. Das Ergebnis wurde in der Ebene *Plan* gespeichert.
* *Teilweise optimierter Plan*: Die Optimierung konnte einige der Pausen nicht berücksichtigen. Erfahre unten mehr über [diesen Status](#teilweise-optimierter-plan).
* *Die Optimierung ist fehlgeschlagen*: Die Optimierung konnte nicht gestartet werden. Versuche erneut, sie zu starten. Wenn die Meldung *Die Optimierung ist fehlgeschlagen. Bitte versuche es erneut.* weiterhin erscheint, {% link_new erstelle ein Ticket | support/create-ticket.md %}, um Support zu erhalten.

### Teilweise optimierter Plan
<!-- Do not change this heading: /de/break-optimization#teilweise-optimierter-plan is used within the break optimization UI-->

Der Status *Teilweise optimierter Plan* erscheint, wenn die Optimierung einige Pausen nicht berücksichtigen konnte. Hierfür gibt es drei mögliche Gründe:
* Einige Pausen wurden von der Optimierung übersprungen, da sie sonst z. B. Meeting-Aktivitäten überlagern würden, was nicht erlaubt ist. Diese Pausen befinden sich immer noch an der Stelle, an der sie sich zu Beginn der Optimierung befunden haben.
* Einige Pausen wurden nicht berücksichtigt, weil sie zu kurz sind (< 5 Minuten) oder nicht mit dem Intervall kompatibel sind, das von der Planungseinheit genutzt wird.
* Einige Pausen konnten aufgrund von bestimmten Verletzungen der {% link_new Planungsregeln | features/administration/create-contracts.md %} nicht optimiert werden. Zum Beispiel könnte ein Mitarbeiter für eine Aktivität geplant sein, ohne die dafür erforderliche(n) Qualifikation(en) zu besitzen.

## Optimierungsergebnisse überprüfen

Um die Details einer Pausenoptimierung anzuzeigen, klicke im Abschnitt *Optimierungshistorie* in der Spalte *Status* auf **Ergebnisse anzeigen**.

{{ 2 | image: 'Optimierungshistorie' }}

Für die ausgewählte Optimierung siehst Du einige Details und wie viele Pausen optimiert wurden (nur im Falle eines {% link_new teilweise optimierten Plans | features/scheduling/schedules/break-optimization.md | #teilweise-optimierter-plan %}).

Das Diagramm veranschaulicht die Gesamtabweichung von der perfekten Deckung vor und nach der Optimierung. Es enthält zwei Graphen, die die Deckungsdaten aller geplanten Aktivitäten aufsummieren und im Zeitverlauf anzeigen:

 * Gelbe Linie: die Deckung des Schichtplans *vor* der Optimierung
 * Grüne Linie: die Deckung des Schichtplans *nach* der Optimierung

Je weiter sich die grüne Linie der 0 annähert, desto stärker hat die Optimierung die Deckung verbessert. Ein Wert von z. B. 5 für *Gesamtabweichung von 0* bedeutet, dass zu diesem Zeitpunkt eine Überbesetzung von 5 Mitarbeitern besteht.

{{ 3 | image: 'Graph für die  Optimierungsergebnisse', '70%' }}


### Wie die Graphen berechnet werden

Angenommen, Deine Planungseinheit hat zwei verschiedene Aktivitäten vom Typ *Anwesenheit*, die in einem Intervall von 15 Minuten geforecastet und geplant werden. Das ergibt vier Intervalle pro Stunde. Für diese vier Intervalle zeigt die folgende Tabelle die Deckung beider Aktivitäten, die Abweichung von der perfekten Deckung sowie die Gesamtabweichung, d.h. die Summe der Werte für die Abweichung von der perfekten Deckung:  

| Hotline  |  Deckung | Abweichung von perfekter Deckung |
| ---------|-----------| -------------------------------- |
| Kundensupport | [0, -2, -1, 0] | [0, 2, 1, 0] |
| Finanzfragen | [3,  2,  2, 0] | [3, 2, 2, 0] |
|              | **Gesamtabweichung** | [3, 4, 3, 0]  |

Im Diagramm zeigen die grünen und gelben Graphen die *Gesamtabweichung* an.

### Intervalle eines Tages anzeigen

Für einen Zeitraum von bis zu drei Tagen zeigt das Diagramm standardmäßig die Intervalle für jeden Tag an. Bei vier oder mehr Tagen zeigt das Diagramm nur die Gesamtwerte je Tag. Du kannst Dir aber die einzelnen Intervalle eines Tages bei Bedarf anzeigen lassen:

 1. Bewege den Mauszeiger über einen **Tag im Diagramm** und klicke ihn an. Die Ansicht zeigt jetzt die Intervalle für den Tag an.
 2. Klicke auf *Zurück zur Tagesansicht*{:.doc-button}, um zur Übersicht zurückzukehren.

    {{ 4 | image: 'Ansicht für die Intervalle eines Tages mit Zurück-Button', '70%' }}
