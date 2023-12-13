---
title: Vertragsbeispiele
---

Unterhalb findest Du Beispiele für verschiedene Verträge und die empfohlene Konfiguration für die Nutzung mit dem AutoScheduler.

### 5-Tages-Vertrag mit 32 Stunden Wochensoll

Astrid hat einen 5-Tages-Vertrag mit 32 Stunden Wochensoll. Sie kann täglich zwischen 6 und 8 Stunden eingesetzt werden und kann auch nur für 4 Tage geplant werden.

Ihr Soll pro Woche muss immer eingehalten werden, da es dem Minimum und Maximum entspricht. Daher sind mögliche Schichtpläne

- 1x 7,5 Std., 1x 6,5 Std., 3x 6,0 Std.
- 1x 7,0 Std., 2x 6,5 Std., 2x 6,0 Std.
- 2x 7,0 Std., 3x 6,0 Std.
- 1x 8,0 Std., 4x 6,0 Std.
- 1x 6,0 Std., 4x 6,5 Std.
- 4x 8,0 Std.

Bei einem Planungsmodell vom Typ B (Starre Rotation) oder Typ C (Variable Rotation) schlägt die Basisplanerstellung fehl, da der AutoScheduler bei diesen Typen immer nur ein und dasselbe Tagesmodell verwenden darf.

Falls Astrid einzelne Urlaubstage genommen hat oder im Vorfeld der Planung einzelne ganztägige Aktivitäten im Schicht Center hinterlegt wurden, schlägt die Basisplanerstellung ebenfalls fehl, da die Ist-Zeit für ganztägige, bezahlte Aktivitäten 06:24 Stunden beträgt und diese anteilige Arbeitszeit aufgrund der Netto-Schichtlänge der Tagesmodelle und der vertraglichen Vorgaben nicht ausgeglichen werden kann.

Daher sollte das angegebene Wochenminimum in ihrem Vertrag reduziert werden, da Astrid sonst in Wochen mit vorgeplanten Aktivitäten oder Feiertagen nicht korrekt vom AutoScheduler geplant werden kann.

### 5-Tages-Vertrag mit 35 Stunden Wochensoll

Bernd hat einen 5-Tages-Vertrag mit 35 Stunden Wochensoll. Er kann täglich zwischen 6 und 8 Stunden eingesetzt werden und kann auch nur für 4 Tage geplant werden. Sein Wochensoll muss immer eingehalten werden. Mögliche Schichtpläne sind u.a.

- 5x 7,0 Std.
- 1x 6,0 Std., 3x 7,0 Std., 1x 8,0 Std.
- 2x 6,0 Std., 1x 7,0 Std., 2x 8,0 Std.
- 1x 6,0 Std., 2x 7,0 Std., 2x 7,5 Std.
- 2x 6,5 Std., 2x 7,0 Std., 1x 8,0 Std.
- 1x 6,5 Std., 3x 7,0 Std., 1x 7,5 Std.
- 1x 6,0 Std., 1x 6,5 Std., 1x 7,0 Std., 1x 7,5 Std., 1x 8,0 Std.

Sollte ein Planungsmodell für Bernd angelegt werden, können dafür alle Planungsmodell-Typen verwendet werden, wobei sich die Anzahl der möglichen Schichtpläne je nach Typ reduziert. Solange in Bernds Vertrag das Wochenminimum 35 Stunden beträgt, wird er immer für 5 Tage eingesetzt, da der AutoScheduler nur Tagesmodelle mit einer Netto-Schichtdauer von 6 bis 8 Stunden verwenden darf und keine mögliche Kombination aus nur 4 Tagesmodellen das Wochenminimum erreicht.

### 4-Tages-Vertrag mit 20 Stunden Wochensoll

Christina hat einen 4-Tages-Vertrag mit 20 Stunden Wochensoll. Sie kann nur an festen Tagen unterschiedlich lange Schichten leisten, daher wurde in ihrem flexiblen Vertrag die Wochentagsarbeitszeit (Montag bis Donnerstag, 3,0 Std., 4,0 Std., 5,0 Std., 8,0 Std.) Ihr Wochensoll ist die Summe der Wochentagsarbeitszeit und muss vom AutoScheduler stets eingehalten werden.

Christina kann nur in Feiertagswochen an weniger als 4 Tagen pro Woche vom AutoScheduler geplant werden, da das Wochensoll durch Feiertage reduziert wird, d.h. fällt ein Feiertag auf einen Wochentag, stehen von den 20 Stunden nur noch 16 Stunden für die Planung zur Verfügung.

Für Wochen ohne Feiertag gibt es nur eine mögliche Arbeitszeitkombination:

- 1x 3,0 Std., 1x 4,0 Std., 1x 5,0 Std., 1x 8,0 Std.

Dabei muss der AutoScheduler montags immer auf ein Tagesmodell mit einer Netto-Schichtdauer von 8 Stunden zurückgreifen und donnerstags ein Tagesmodell mit einer Netto-Schichtdauer von 5 Stunden planen.

Immerhin kann Christina innerhalb der gesamten Öffnungszeit der Planungseinheit eingesetzt werden, falls ihre Verfügbarkeit und zugewiesene Tagesmodelle dem nicht widersprechen.

Sollte ein Planungsmodell für Christina angelegt werden, muss dafür entweder der Typ A (Flexible Auswahl) oder der Typ D (Kombi-Rotation) gewählt werden. Bei einem Planungsmodell vom Typ B (Starre Rotation) oder Typ C (Variable Rotation) schlägt die Basisplanerstellung fehl, da der AutoScheduler bei diesen Typen immer nur ein und dasselbe Tagesmodell verwenden darf.

Falls eine explizite Zuordnung von Tagesmodellen erfolgt, ist darauf zu achten, dass die Wochentagsarbeitszeit weiterhin eingehalten werden kann. Wenn Christina nur Tagesmodelle mit einer Netto-Schichtdauer von 5 Stunden zugewiesen werden, könnte der AutoScheduler zwar das Wochensoll erreichen, würde aber die vertraglichen Bedingungen nicht einhalten. Daher schlägt bereits die Basisplanerstellung fehl und Christina wird nicht durch den AutoScheduler geplant.

### 1-5-Tages-Vertrag ohne vertragliches Tages- und Wochensoll (Student)

David ist Student und soll wirklich nur dann geplant werden, wenn der Aktivitätsbedarf mit anderen Mitarbeiterkapazitäten nicht gedeckt werden kann. Er kann zwischen 1 und 5 Tagen geplant werden und hat weder ein vertragliches Tages- noch Wochensoll.

Kann der AutoScheduler mit diesen Angaben Schichtpläne für David erstellen? Kann es vorkommen, dass er gar nicht geplant wird? Ist so ein Vertrag überhaupt gültig?

Sowie die Anzahl der Arbeitstage pro Woche und das Wochensoll hinterlegt wurden, kann der AutoScheduler den Vertrag verwenden und Schichtpläne für den Mitarbeiter erstellen, daher handelt es sich bei dem abgebildeten Vertrag um einen gültigen Vertrag, auch wenn das Wochensoll mit 00:00 Stunden angegeben wurde. David erhält also auf jeden Fall einen Schichtplan.

Dabei kann es nicht vorkommen, dass der Mitarbeiter überhaupt nicht geplant wird, denn für den AutoScheduler gilt ein Planungszwang. Jeder Mitarbeiter, für den das Schichtzuteilungshäkchen gesetzt und dem ein gültiger Vertrag zugewiesen wurde, muss während der Optimierung berücksichtigt und vertragskonform geplant werden.

In Wochen mit geringem Aktivitätsbedarf handelt es sich um einen vertragskonformen Schichtplan, wenn der AutoScheduler David für mindestens einen Arbeitstag in der Woche plant. Da im Vertrag keinerlei Angaben zur Arbeitszeit pro Tag gemacht wurden, kann der AutoScheduler auf das kürzeste Tagesmodell zurückgreifen, das der Planungseinheit zugewiesen wurde. Im Beispiel, das das Schicht Center mit der Darstellung der Ist-Zeit zeigt, ist dies ein Tagesmodell mit einer Netto-Schichtdauer von 3 Stunden.

{{ 1 | image: 'Verträge 0-Stunden', '75%' }}

In Wochen mit hohem Aktivitätsbedarf oder vielen Urlaubs- und Abwesenheitstagen kann der AutoScheduler David für maximal 5 Arbeitstage planen. Aufgrund der fehlenden Angaben zur Arbeitszeit pro Tag kann der AutoScheduler auf alle Tagesmodelle zurückgreifen, die der Planungseinheit zugewiesen wurden und so bspw. den folgenden Schichtplan schreiben, der alle vertraglichen Parameter und Planungsregeln einhält.

{{ 2 | image: 'Verträge 0-Stunden', '75%' }}

Dennoch sollten Verträge grundsätzlich konkrete und vor allen Dingen korrekte Angaben in den Bearbeitungskategorien *Arbeitszeitvorgaben* oder *Wochentagsarbeitszeit* enthalten, da im vorliegenden Beispiel ganztägige, bezahlte Aktivitäten wie bspw. Urlaube, Krankheiten oder Schulungen ohne Ist-Zeit bewertet würden, weil aufgrund des fehlenden Wochensolls keine Sollarbeitszeit für einzelne Tage ermittelt werden kann.

Sollte ein Planungsmodell für David angelegt werden, können dafür alle Planungsmodell-Typen verwendet werden, wobei der Vertrag spätestens dann konkrete Arbeitszeitvorgaben enthalten sollte.
