---
title: Kombinieren von Planungsmethoden
product_label:
  - advanced
  - enterprise
  - classic
description: Kombiniere die verschiedenen Planungsmethoden, um den Anforderungen Deines Unternehmens gerecht zu werden.
---

Alle verfügbaren {% link_new Planungsmethoden | features/scheduling/scheduling-methods.md %} können auf verschiedene Weise kombiniert werden, um die Bedürfnisse Deiner Agenten und die Ziele Deines Unternehmens zu berücksichtigen.

Die folgenden Beispiele veranschaulichen einige der üblichen Kombinationsmöglichkeiten von Planungsmethoden, die Du direkt einsetzen oder als Inspiration für Deine eigenen Kombinationen verwenden kannst.

## Fixe Schichtplanung und rotierende bzw. voll flexible Schichten

Wenn Du hauptsächlich mit flexiblen Schichtplänen arbeiten möchtest, kannst Du Deinen flexiblen Mitarbeitern Planungsmodelle zuweisen. Wenn einige Mitarbeiter strikte zeitlichen Einschränkungen für den Schichtplan haben oder Du Top-Performer und leitende Mitarbeiter belohnen möchtest, kannst Du für diese Mitarbeiter Schichtfolgen definieren.

Bei der Planung fügst Du zuerst Deine Schichtfolgen ein und führst dann eine Optimierung durch. Deine rotierenden oder flexiblen Schichten werden um die bereits hinterlegten Schichtfolgen geplant.

Wenn Du Mitarbeiter hast, die nur an bestimmten Wochentagen einen festen Schichtplan benötigen, kannst Du eine Schichtfolge erstellen, in welcher Du diese Tage hinterlegst. Der Rest der Woche bleibt frei und der Mitarbeiter wird durch das zugewiesene Planungsmodell geplant.

Wenn Du die Schichtfolge einfügst und eine vollständige Optimierung durchführst, werden die leeren Tage durch die flexiblen oder rotierenden Schichten aufgefüllt. Dabei werden die Vorgaben aus dem Vertrag eingehalten, um einen gültigen Schichtplan zu erstellen.

## Rotierende flexible und vollständig flexible Schichten

Wenn Du möchtest, dass einige Mitarbeiter einem rotierenden Schichtplan folgen, während andere flexibler sind oder während einer bestimmten Tageszeit immer eine flexible Schicht erhalten können, weise den Mitarbeitern für rotierende Schichten einfach Planungsmodelle vom Typ B oder D zu und allen anderen Planungsmodelle vom Typ A.
Die Mitarbeiter mit den Planungsmodellen vom Typ B oder D werden ihren Rotationen folgen und die flexiblen Mitarbeiter werden so optimiert, dass sie den Rest der Bedarfe bestmöglich decken.

## Rotierende flexible Schichten und Verfügbarkeit

Wenn ein Mitarbeiter in einer rotierenden Schicht arbeitet, aber an bestimmten Tagen zeitlich eingeschränkt ist (z.B. darf er an einem Mittwoch nicht länger als 17 Uhr arbeiten), hinterlege einfach die entsprechende Verfügbarkeit beim Mitarbeiter und weise ihm ein Planungsmodell zu.

In den Wochen, in denen der Mitarbeiter in der Frühschicht arbeitet, ermöglicht seine Verfügbarkeit die Planung am Mittwoch. In Wochen, in denen der Mitarbeiter in der Spätschicht arbeitet, blockiert die Verfügbarkeit jedoch die Planung am Mittwoch und die Optimierung wird ihm Schichten für andere Wochentage geben.

## Fixe Schichtplanung und Verfügbarkeit

Du kannst Tagesmodelle vom Typ *Verfügbarkeitsrahmen* in Schichtfolgen hinzufügen, um das Ergebnis der Planung an bestimmten Tagen zu beeinflussen. Unterhalb zwei Beispiele. 

**Schichten an jedem zweiten Wochenende**:  
1. Erstelle ein Tagesmodell vom Typ *Verfügbarkeitsrahmen* mit einem Zeitrahmen von 0 Uhr bis 00:01 Uhr als Blocker. 
2. Füge das Tagesmodell in einer Schichtfolge an jeden zweiten Wochenende ein (alle anderen Tage bleiben frei).  
3. Weise die Schichtfolge Mitarbeitern zu und füge die Schichtfolge ein, bevor Du einen optimierten Plan erstellst.

injixo plant für den Mitarbeiter an jedem zweiten Wochenende keine Schichten und optimiert die anderen Tage.

**Nachtschichten in einem zwei-Wochen-Zyklus**:  
1. Erstelle ein Tagesmodell vom Typ *Verfügbarkeitsrahmen* mit einem Zeitrahmen von 12:00 Uhr bis 00:00 Uhr. 
2. Füge das Tagesmodell für jeden Tag einer Woche in einer Schichtfolge ein (alle anderen Tage bleiben frei).
3. Weise die Schichtfolge Mitarbeitern zu und füge die Schichtfolge ein, bevor Du einen optimierten Plan erstellst.

injixo plant für den Mitarbeiter in den Wochen mit Verfügbarkeit (gemäß des Planungsmodells) eine Nachtschicht. In den anderen Wochen plant injixo eine beliebige Schicht.