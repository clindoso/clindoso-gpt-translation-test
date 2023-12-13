---
title: Richtzeitkonten
---

Im Menüpunkt *Richtzeitkonten*{:.menu-item} berechnest und kontrollierst Du für jede Planperiode die zu leistende Arbeitszeit Deiner Mitarbeiter. Nicht zutreffende Werte lassen sich manuell korrigieren. Für mehrere Mitarbeiterkonten können gleichzeitig Auf- oder Abschläge vorgenommen werden, z.B. zum Arbeitszeitausgleich bei saisonalen Schwankungen. Die Richtzeit entspricht der Sollarbeitszeit eines Mitarbeiters, die sich aus dessen Vertrag ableitet.

Berechne die Richtzeit zu Beginn jeder neuen Planperiode. Die Richtzeitberechnung ist sowohl im Menüpunkt *Richtzeitkonten*{:.menu-item} als auch im Menüpunkt *Scheduling > SchedulePro > Planperioden*{:.breadcrumbs} möglich. Die Ergebnisbearbeitung lässt sich dagegen nur im Menüpunkt Richtzeitkonten vornehmen. Nach dem Öffnen des Menüpunkts erscheint die Parameterauswahl für die Richtzeitkontenübersicht.

## Richtzeitkonten - Parameterauswahl

Im Bereich Parameter legst Du zunächst die Mitarbeiter fest, deren Richtzeitkonten angezeigt werden sollen.

| Einstellung | Beschreibung |
| ------- | ------- |
| Planungseinheit | Wähle die Planungseinheit für die Richtzeitkontenanzeige aus. Die zuletzt verwendete Planungseinheit ist voreingestellt. |
| Auswahl | Die Mitarbeiterauswahl für die Richtzeitkontenanzeige lässt sich durch die Angabe einer Auswahlgruppe eingrenzen. |
| Planperiode | Wähle die Planperiode für die Richtzeitkontenanzeige aus. Es stehen alle Planperioden des Typs `Standard` aus dem Menüpunkt Planperioden zur Verfügung. |

Bestätige Deine Eingaben nach jeder Änderung mit *Anwenden*{:.doc-button}, um die Richtzeitkontenübersicht einzublenden bzw. zu aktualisieren. Sobald der Job abgeschickt wurde, beginnt der JobProcessor mit der Verarbeitung der Schichtfolgen.

Sobald die Übersicht erscheint, kannst Du Richtzeitkontenwerte berechnen oder bearbeiten. Die Übersicht enthält keine Werte, wenn für den angegebenen Tag noch keine Richtzeit berechnet wurde.

## Berechnung der Richtzeitkonten

Die zu leistende Sollarbeitszeit der Mitarbeiter wird normalerweise vor jeder neuen Planperiode ermittelt. Um die Richtzeit für eine Planperiode zu berechnen oder vorliegende Werte zu aktualisieren, klicke im Bereich Parameter auf *Berechnen*{:.doc-button}. Sobald der Job abgeschickt wurde, beginnt der JobProcessor mit der Verarbeitung. Die aktualisierten Richtzeitwerte werden nach kurzer Zeit eingeblendet.

> Hinweis
>
> Die Richtzeitkontenberechnung erfolgt nur für Mitarbeiter, denen ein Vertrag zugeordnet ist. Für die ordnungsgemäße Funktionsweise sind zudem ausreichende Angaben in den Bearbeitungskategorien Arbeitszeitvorgaben und Wochentagsarbeitszeit erforderlich.

In der Übersicht lässt sich für jeden Mitarbeiter eine geänderte Richtzeit für die Planperiode angeben.

| Einstellung | Beschreibung |
| ------- | ------- |
| Mitarbeiter | Die Namen der Mitarbeiter der Planungseinheit oder Auswahlgruppe werden aufgelistet. |
| Berechneter Wert | Fehlende Werte bedeuten, dass für die Planperiode noch kein Richtzeitkonto ermittelt worden ist. Nach der Berechnung erscheint für alle Mitarbeiter die Richtzeit. Der Wert wird in Stunden angezeigt. Die berechnete Richtzeit selbst ist nicht änderbar. |
| Geänderter Wert | Für jeden Mitarbeiter kannst Du einen neuen Richtzeitwert angeben. Zuteilung und Verlosung berücksichtigen zuerst die in dieser Spalte eingetragenen Werte. Im Verlosungs- bzw. Zuteilungsprotokoll findest Du den verwendeten Richtzeitwert. Sowohl im Schicht Center als auch in der Spalte `Berechneter Wert` erscheint jedoch weiterhin die aus den vertraglichen Angaben vom Programm ermittelte Sollarbeitszeit bzw. Richtzeit.

**Richtzeitkonten anpassen**
Rechts vom Parameterbereich befindet sich der Bereich Konten anpassen. Du kannst die berechneten Richtzeiten um einen Wert (Prozent oder Stunden) erhöhen oder verringern. Wähle zunächst die Konten in der Mitarbeiterübersicht aus, die Du anpassen möchtest.

| Einstellung | Beschreibung |
| ------- | ------- |
| Prozentwert | Aktiviere die Option, um die Zeit der ausgewählten Konten prozentual herauf- oder herabzusetzen. |
| Stunden | Aktiviere die Option, um die Stundenzahl der ausgewählten Konten zu erhöhen oder zu verringern. |
| Anpassung | Gib an, ob Du den Wert addieren oder subtrahieren möchtest. |
| Wert | Trage einen numerischen Wert größer als 0 ein. Es werden Prozentwerte bis 100 % und maximal zwei Dezimalstellen unterstützt oder bis zu 9999:00 Stunden. |

Um die Richtzeitkonten anzupassen, klicke auf *Übernehmen*{:.doc-button}. Sobald der Job abgeschickt wurde, beginnt der JobProcessor mit der Verarbeitung. Die aktualisierten Richtzeitwerte werden nach kurzer Zeit in der Spalte Geänderter Wert eingeblendet.
