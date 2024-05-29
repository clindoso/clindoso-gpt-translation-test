---
title: Planung unterschiedlicher Pausenlängen
redirect_from: /de/best-practice-schedule-different-break-length/
---

In Deinem Unternehmen hast Du mit Deinen Mitarbeitern unterschiedliche Pausenlängen vereinbart, um auf individuelle Bedürfnisse einzugehen. Dadurch haben Mitarbeiter mit der gleichen Sollarbeitszeit unterschiedlich lange Schichten. Nichtsdestotrotz kannst Du dies mit einem einzelnen Vertrag abbilden.

Da Du im Vertrag nur die Sollarbeitszeiten hinterlegst, musst Du einen kleinen Umweg gehen, damit die Optimierung berücksichtigt, welcher Mitarbeiter kurze und welcher lange Pausen erhält.

## Zwei Planungsmodelle mit unterschiedlichen Tagesmodellen

Schränke die verfügbaren Tagesmodelle für die Optimierung über Planungsmodelle für lange und kurze Pausen ein. Die Optimierung berücksichtigt die Planungsmodell-Zuordnung und plant nur die enthaltenen Tagesmodelle.

Falls Du bisher mit der Optimierung, aber ohne Planungsmodelle gearbeitet hast, ist die Einführung von Planungsmodellen vom Typ A (Flexible Auswahl) wahrscheinlich die einfachste Option.

So führst Du Planungsmodelle ein:

1. Weise alle Tagesmodelle mit kurzen Pausen einem Wochenmodell "kurz" zu.
2. Füge alle Tagesmodelle mit langen Pausen dem Wochenmodell "lang" hinzu.
3. Erstelle zwei Planungsmodelle vom Typ A (Flexible Auswahl).
4. Ordne den Planungsmodellen das entsprechende Wochenmodell zu.
5. Weise nun allen Mitarbeitern, die nur kurze Pausen machen, (über die Massenbearbeitung) das entsprechende Planungsmodell zu.
6. Ordne das andere Planungsmodell den verbleibenden Mitarbeiter zu.

Arbeitest Du bereits mit Planungsmodellen, musst Du Dein bisheriges Planungsmodell aufteilen und zwei neue Planungsmodelle des bisher verwendeten Typs erstellen.

## Persönliche Mitarbeiter-Tagesmodelle

Schränke die verfügbaren Tagesmodelle für die Optimierung über persönliche Tagesmodelle mit langen und kurzen Pausen ein. Die Optimierung berücksichtigt die Tagesmodell-Zuordnung zum Mitarbeiter und plant nur die zugewiesenen Tagesmodelle.

Ordne Deinen Mitarbeitern persönliche Tagesmodelle zu. Nimm die notwendigen Änderungen unter _Administration > Scheduling > Mitarbeiter_{:.breadcrumbs} in der Bearbeitungskategorie _Tagesmodelle_ vor. Mitarbeiter, die nur kurze Pausen machen, erhalten Tagesmodelle mit kurzen Pausen; die anderen Mitarbeiter Tagesmodelle mit langen Pausen.

Vorteilhaft ist, dass die Tagesmodelle des jeweiligen Mitarbeiters systemweit gelten, d.&nbsp;h. auch bei manueller Planung oder in der Infothek. Nachteilig ist, dass der Prozess der Zuweisung unter Umständen aufwändig ist, denn die Massenbearbeitung unterstützt diese leider nicht.

Hinweise zur Planungsregel _2661_{:.id-label} _Tagesmodellzuordnung zum Mitarbeiter_:

- Bei aktivierter Regel wird ein Mitarbeiter nicht geplant, wenn dieser kein persönliches Tagesmodell hat.
- Bei deaktivierter Regel nutzt die Optimierung
  - alle Tagesmodelle, wenn ein Mitarbeiter kein persönliches Tagesmodell hat.
  - trotzdem nur das zugeordnete Tagesmodell, wenn ein Mitarbeiter ein persönliches Tagesmodell hat.

## Steuerung über Qualifikationen

Mitarbeiter erhalten ihre gewünschte Pausenlänge, da die Optimierung die Qualifikation für die Aktivitäten eines Tagesmodells prüft.

Die Planungsregel _2605_{:.id-label} _Qualifikation der Mitarbeiter_ ist immer aktiviert und funktioniert nicht nur bei Aktivitäten vom Typ Anwesenheit, sondern bei allen Aktivitäten mit einer Qualifikation.

Gehe wie folgt vor:

1. Definiere eine Qualifikation für kurze Pausen und eine für lange Pausen.
2. Weise die entsprechende Qualifikation Deinen unterschiedlichen Pausen-Aktivitäten zu.
3. Passe Deine Tagesmodelle an oder erstelle neue, sodass es unterschiedliche Schichten mit den Aktivitäten für die kurzen und langen Pausen gibt.
4. Weise den Mitarbeitern, die kurze Pausen erhalten soll, (per Massenbearbeitung) die Qualifikation für kurze Pausen zu; die anderen bekommen die Qualifikation für lange Pausen.

Verwende dieses Vorgehen auch, wenn Du nicht die volloptimierte Planung einsetzt, z.B. bei der Erstellung der Schichtpläne über Schichterzeugung, Verlosung und Zuteilung, etc.
