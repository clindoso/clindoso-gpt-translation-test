---
title: Feiertage planen
redirect_from:
  - /de/best-practice-planning-with-holidays/
---

Erfahre, wie Du Feiertage mit der volloptimierten Planung abbildest.

Grundsätzlich ist hierfür die Nutzung des _Planungskalenders_{:.menu-item} gedacht, beachte aber, dass es unter Umständen auch leichter sein kann, auf den _Planungskalender_{:.menu-item} zu verzichten.

Warum das so ist, erfährst Du in diesem Artikel. Außerdem erhältst Du einige Planungsempfehlungen.

## Der Planungskalender

Um Feiertage in Deiner Planung zu berücksichtigen, kann der _Planungskalender_{:.menu-item} verwendet werden. Diesen kannst Du unter _Administration > Scheduling > Planungskalender_{:.breadcrumbs} anlegen.

{{ 1 | image: 'Ansicht des Planungskalenders', '75%' }}

Durch die Auswahl der passenden Kalendervorlage werden alle Feiertage einer Region/eines Landes in den Kalender aufgenommen. Speichere den _Planungskalender_{:.menu-item} und vergib einen Namen.

Anschließend kannst Du den gespeicherten _Planungskalender_{:.menu-item} der Planungseinheit unter _Administration > Scheduling > Planungseinheit_{:.breadcrumbs} zuweisen. Hier kannst Du auch die Öffnungszeiten eines Feiertags hinterlegen, sollte Deine Planungseinheit nicht geschlossen sein.

> Hinweis
>
> Planungskalender können system-seitig einem einzelnen Mitarbeiter zugeordnet werden, dies hat allerdings keine Auswirkungen auf die Planung. Für die Planung ist allein der Planungskalender der Planungseinheit relevant.

## Tagestypen - Feiertagsmodus

Für jeden Feiertag, der in einem Planungskalender gespeichert ist, existiert unter _Administration > Scheduling > Tagestypen_{:.breadcrumbs} ein Tagestyp, für den der Feiertagsmodus standardmäßig aktiviert ist.

{{ 2 | image: "Tagestyp 'Tag der Arbeit' mit aktivierten Feiertagsmodus", '50%' }}

Hierdurch wird der jeweilige Tag bei Zeitberechnungen als Feiertag behandelt, was dazu führt, dass die wöchentliche Soll-Arbeitszeit reduziert wird.

> Tipp: Feiertag fällt auf das Wochenende
>
> Wenn Du mit dem _Planungskalender_{:.menu-item} inkl. aktiver Feiertagsmodi arbeitest und Deine Planungseinheit am Wochenende grundsätzlich geschlossen ist, solltest Du überprüfen, ob Feiertage auf ein Wochenende fallen und diese aus dem _Planungskalender_{:.menu-item} entfernen. Damit stellst Du sicher, dass die korrekte Anzahl an Arbeitstagen geplant werden kann. Tust Du dies nicht, schreibt der AutoScheduler den Mitarbeitern einen Arbeitstag gut, obwohl an dem Tag ohnehin keine Arbeit erfolgt wäre.

Der Feiertagsmodus wird außerdem von der Planungsregel _2631_{:.id-label} _Keine Zuordnungen an Feiertagen (Tagesmodelle und Aktivitäten) gemäß Vertrag_ berücksichtigt. Wenn Du diese Regel auf rot (hart) stehen und das entsprechende Kontrollkästchen im Vertrag aktiviert hast, ist es nicht möglich Mitarbeitern an Feiertagen Aktivitäten oder Tagesmodelle zuzuordnen.

## Planungsempfehlungen

### Szenario 1: Keine Planung der Mitarbeiter am Feiertag

Wenn Deine Planungseinheit an Feiertagen geschlossen ist und daher keine Mitarbeiter an diesem Tag benötigt werden, gibt es grundsätzlich zwei Optionen die Feiertage bei der Planung zu berücksichtigen - einmal mit und einmal ohne den _Planungskalender_{:.menu-item}.

Um beide Möglichkeiten aufzuzeigen, nehmen wir ein Szenario mit folgenden Parametern als Beispiel zur Hilfe:

- Vertrag mit 40 Stunden Mindestarbeitszeit pro Woche
- Vertragliche Tagessollzeit von 8 Stunden
- Vertrag mit 5 Arbeitstagen pro Woche (ggf. sogar Mindestanzahl Arbeitstage auf 4 gestellt)
- An Feiertagen hat die Planungseinheit geschlossen. In der Planungseinheit haben Feiertage also keine Öffnungszeiten.

#### Option 1 - Planung mit Planungskalender: Reduzierung der minimalen wöchentlichen Arbeitszeit

Grundsätzlich bietet sich die Verwendung des _Planungskalenders_{:.menu-item} an, wenn Deine Planungseinheit an Feiertagen geschlossen ist. Nutzt man jedoch unter den oben angegebenen Beispielparametern den _Planungskalender_{:.menu-item} und führt eine volloptimierte Planung durch, stößt der AutoScheduler auf widersprüchliche Bedingungen.

Gehen wir davon aus, dass in der Planungswoche ein Feiertag auf einen Wochentag fällt. Hierdurch reduziert sich die wöchentliche Soll-Arbeitszeit auf 32 Stunden.

**Berechnung der abgeänderten Soll-Arbeitszeit**

`(Soll-Arbeitszeit/Anzahl Arbeitstage) * (Anzahl Arbeitstage -
Feiertage)`

`(40 Stunden/5) * (5-1) = 32 Stunden`

Der AutoScheduler kann nur 4 Arbeitstage mit je 8 Stunden erzeugen. Auch wenn hierbei die Mindestanzahl Arbeitstage von 4 Tagen eingehalten werden könnte, kommt es zu keiner Planerstellung, da die minimale wöchentliche Arbeitszeit von 40 Stunden nicht erreicht werden kann.

Um dem AutoScheduler die Planerstellung zu ermöglichen, kann man die im Vertrag festgelegte wöchentliche minimale Arbeitszeit reduzieren. In unserem Beispiel müsste dieser Wert von 40 Stunden auf 32 Stunden reduziert werden. Damit kann der AutoScheduler wieder einen Schichtplan erstellen (sofern er auch nur 4 Arbeitstage nutzen darf).

Der Nachteil besteht jedoch darin, dass der AutoScheduler auch in Wochen ohne Feiertage bei zu wenig Bedarf davon Gebrauch macht und die Mitarbeiter weniger als 40 Stunden geplant. Dies kann insbesondere bei Planungseinheiten mit einer standardmäßigen Überdeckung problematisch werden. Bedenkt man zudem, dass es in vielen Ländern auch Wochen mit 2 Feiertagen in einer Woche geben kann (z.B. Weihnachten), müsstest Du die minimale Wochenarbeitszeit noch weiter auf 24 Stunden reduzieren.

Möchte man ungern die minimale Arbeitszeit in allen Verträgen (regelmäßig) umzustellen, bietet sich Option 2 an, die wir Dir im nächsten Abschnitt erläutern.

#### Option 2 - Planung ohne Planungskalender: Planung mit einer ganztägigen, bezahlten Abwesenheit

Sollte Deine Planungseinheit an Feiertagen geschlossen sein, kannst Du alternativ bei Deiner Feiertagsplanung auch auf den _Planungskalender_{:.menu-item} verzichten und mit einer Aktivität vom Typ Abwesenheit arbeiten.

Lege hierzu eine ganztägige, bezahlte Aktivität vom Typ Abwesenheit, wie bspw. "feiertagsfrei", an und weise diese der Planungseinheit zu. Da diese Abwesenheit bezahlt ist, entspricht sie sozusagen einem Arbeitstag und Du musst keine Änderung im Vertrag in Bezug auf die minimale wöchentliche Arbeitszeit vornehmen.

{{ 3 | image: 'Aktivität feiertagsfrei', '50%' }}

Du kannst die Aktivität _feiertagsfrei_ zu Beginn des Jahres allen Mitarbeitern an Feiertagen im Schicht Center zuordnen. Verwende dazu den Tab _Mitarbeiter_ des Mitarbeiterdialogs.

{{ 4 | image: 'Schicht Center Dialog zum Eintragen einer Aktivität bei allen Mitarbeitern', '75%' }}

> Hinweis: Planung mit Wochentagsarbeitszeiten
>
> Sollte bei Dir die vertragliche Arbeitszeit eines Mitarbeiters über die Bearbeitungskategorie und nicht über die Bearbeitungskategorie Arbeitszeitvorgaben definiert sein, empfehlen wir ebenfalls ohne einen _Planungskalender_{:.menu-item} und stattdessen mit einer ganztägigen bezahlten Abwesenheit zu arbeiten. Der Grund hierfür liegt darin, dass die sogenannte Basisplanerstellung durch den AutoScheduler für Mitarbeiter mit solchen Verträgen in Wochen mit Feiertagen aufgrund von zwei gegensätzlichen Bedingungen in der Zielfunktion fehlschlagen würde. Einerseits wird der AutoScheduler gezwungen, eine bestimmte Anzahl von Arbeitsstunden an bestimmten Tagen zu planen und andererseits existieren an einem dieser Tage keine Öffnungszeiten. Diese Einschränkung verhindert die Planung von Arbeitszeit. Das Resultat ist, dass Mitarbeiter mit solchen Verträgen in Wochen mit einem Feiertag überhaupt nicht geplant werden.

### Szenario 2: Normale Planung am Feiertag

Wenn Deine Planungseinheit an Feiertagen ganz reguläre Öffnungszeiten hat, kannst Du die Planung ganz normal durchführen. Die Verwendung des Planungskalenders ist nicht zu empfehlen.

Solltest Du bei der Arbeit ohne _Planungskalender_{:.menu-item} die Kennzeichnung der Feiertage im Schicht Center vermissen, lege eine Planungseinheit mit dem Namen `Allgemeiner Kalender` an und ordne dieser keine Mitarbeiter zu.
Ordne aber einen _Planungskalender_{:.menu-item} zu.

Die Planungseinheit steht dann im Schicht Center aufgrund ihres Namens ganz oben und zeigt die Feiertage in den Tagesübersichtszellen an.

{{ 5 | image: 'Planungseinheit zum Anzeigen von Feiertagen'}}

### Szenario 3: Abweichende Öffnungszeiten am Feiertag

Solltest Du an einem Feiertag nicht geschlossen, sondern abweichende Öffnungszeiten haben, ist die Verwendung des _Planungskalenders_{:.menu-item} zu empfehlen. Unter _Administration > Scheduling > Planungseinheiten_{:.breadcrumbs} kannst Du die Öffnungszeiten des Feiertags in der entsprechenden Planungseinheit hinterlegen. Füge hierzu einfach den entsprechenden Feiertag unter _Öffnungszeiten_{:.menu-item} hinzu und gib die Öffnungszeiten an.

{{ 6 | image: 'Planungseinheit mit geänderten Öffnungszeiten an Feiertagen', '50%'}}

Achte bei abweichenden Öffnungszeiten darauf, dass ein entsprechendes Tagesmodell besteht, welches der AutoScheduler für den Feiertag planen kann.

Zudem solltest Du sicherstellen, dass die geänderten Öffnungszeiten mit den Arbeitszeitvorgaben in Deinen Mitarbeiterverträgen vereinbar ist. Sollte die reduzierte Öffnungszeit an einem Feiertag dazu führen, dass die im Vertrag vorgegebene minimale wöchentliche Arbeitszeit nicht eingehalten werden kann, wird es aufgrund der widersprüchlichen Vorgaben zu keiner Planerstellung kommen (Ausführlicher zu dieser Problematik siehe unter [Szenario 1 - Option 1](#option-1---planung-mit-planungskalender-reduzierung-der-minimalen-wöchentlichen-arbeitszeit)).

Solltest Du bei Deinen Verträgen generell mit Wochentagsarbeitszeiten anstatt von Arbeitszeitvorgaben arbeiten, die nicht mit den abgeänderten Öffnungszeiten vereinbar sind, ist von einer Verwendung des _Planungskalenders_{:.menu-item} abzusehen (siehe auch [Szenario 1 - Option 2](#option-2---planung-ohne-planungskalender-planung-mit-einer-ganztägigen-bezahlten-abwesenheit)).
