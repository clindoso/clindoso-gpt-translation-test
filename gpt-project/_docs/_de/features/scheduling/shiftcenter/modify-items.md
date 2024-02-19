---
title: Elemente ändern
product_label:
  - advanced
  - enterprise
  - classic
description: Kopiere, bewege, verlängere und verkürze Elemente im Schichtplan, mach Aktionen rückgängig, konvertiere Tagesmodelle in Aktivitäten & mehr.
redirect_from: /de/changing-assignments/
redirect_reason: renamed file in March 2021
---

In diesem Artikel lernst Du, wie Du:
- Elemente im Schichtplan, d.&nbsp;h. Aktivitäten und Tagesmodelle, kopierst und einfügst.
- Elemente verschiebst, erweiterst und verkürzt.
- Aktionen rückgängig machst.
- Tagesmodelle in Aktivitäten umwandelst.
- ganztägige Aktivitäten wieder aus dem Schichtplan entfernst, um den ursprünglichen Schichtplan wiederherzustellen.

Normalerweise erstellst Du einen Schichtplan nicht komplett manuell, da die volloptimierte Planung dies für Dich übernimmt. Aber von Zeit zu Zeit kann es sein, dass Du Deinen Schichtplan bearbeiten musst. Mit dem Schicht Center ist dies möglich.

Neu im Schicht Center? Lerne zuerst {% link_new die Grundlagen | features/scheduling/shiftcenter/shift-center-overview.md %}.

## Kopieren und einfügen

Du kannst eine oder mehrere Tageszellen oder einzelne Elemente im Schicht Center ausschneiden, kopieren und einfügen.

### Tageszellen

Der gesamte Tag wird kopiert, wenn Du eine oder mehrere Tageszellen kopierst. Wenn Du sie einfügst, wird der Inhalt der Ziel-Tageszelle(n) überschrieben.

1. Wähle eine **Zelle** oder mehrere Zellen aus, indem Du **SHIFT** drückst.
2. Klicke mit der rechten Maustaste auf Deine Auswahl, um das Kontextmenü zu öffnen. Wähle dann **Kopieren** oder **Ausschneiden**. Du kannst auch die Tastaturkürzel **STRG + C** und **STRG + X** verwenden.
3. Wähle eine oder mehrere andere Zellen aus.
4. Klicke mit der rechten Maustaste auf Deine Auswahl und wähle **Einfügen**. Du kannst auch **STRG + V** drücken.

### Einzelne Elemente

1. Klappe einen Tag auf, indem Du auf die Spaltenüberschrift des Tages klickst.
2. Klicke mit der rechten Maustaste auf ein Element im Tagesverlauf, das Du kopieren möchtest, z.B. eine Aktivität, und wähle **Kopieren**. Du kannst auch auf das Element klicken und **STRG + C** drücken.
3. Klicke mit der rechten Maustaste auf eine der aufgeklappten Tageszellen eines Mitarbeiters, in die Du die Aktivität einfügen möchtest, und wähle **Einfügen**. Du kannst auch auf eine aufgeklappte Tageszelle eines Mitarbeiters klicken, um sie auszuwählen, und dann **STRG + V** drücken.

## Verschieben, verlängern und verkürzen

In einem aufgeklappten Tag kannst Du Elemente im Schichtplan mit der Maus verschieben, verlängern oder verkürzen. Öffne zunächst die Zelle, in der Du Elemente verändern willst:

1. Klicke auf die **Spaltenüberschrift eines Tages**, um die Aktivitäten oder Tagesmodelle des Tages anzuzeigen.
2. Benutze die kleinen **schwarzen Pfeiltasten** in der Zeitleiste, um bei Bedarf hinein- oder hinauszuzoomen.
3. Klicke auf die **Zelle** mit den Aktivitäten oder Tagesmodellen, die Du ändern möchtest.

### Variable Tagesmodelle

Du kannst Tagesmodelle vom Typ *Variable Schicht* entsprechend der verfügbaren Startpositionen verschieben. Du kannst Pausen in Tagesmodellen verschieben, wenn diese als Pausenkorridor definiert sind. Fahre mit der Maus über ein Element, bis ein **weißer Doppelpfeil** erscheint, der nach links und rechts zeigt. Klicke, halte und ziehe, um das Element zu verschieben.

### Aktivitäten

Bei Aktivitäten gibt es verschiedene Möglichkeiten, ein Element anzupassen:  

* Verschiebe ein Element nach links oder rechts, ohne seine Länge zu verändern:  
    1. Fahre mit der Maus über ein Element, bis ein **weißer Doppelpfeil** erscheint, der nach links und rechts zeigt.
    2. Klicke, halte und ziehe. Wenn es benachbarte Elemente gibt, werden sie entsprechend verkürzt oder erweitert.

* Verkürze und erweitere die Elemente links und rechts:  
    1. Bewege Deine Maus über das Ende eines Elements oder den Kontaktpunkt zwischen zwei Elementen. Es erscheint ein **schwarzer Doppelpfeil**.
    2. Klicke, halte und ziehe.

### Tipps

- Drücke **STRG** bevor Du ein Element verschiebst, um es von den benachbarten Elementen zu lösen.
- Drücke die **Umschalttaste**, um alle vorhandenen Elemente zusammen zu verschieben, ohne sie zu verändern.
- Wenn Du Elemente verschiebst, verlängerst oder verkürzt, erscheint ein *gelber Tooltip* unter dem Element, der die resultierende Startzeit, Endzeit und Länge des Elements anzeigt. So kannst Du das Element genau positionieren.

### Verwende den Eingabedialog

Alternativ kannst Du auch den Eingabedialog verwenden, um Elemente zu ändern. Um den Eingabedialog zu öffnen, doppelklicke auf eine **Zelle**. Klicke auf einen der Tabs mit den Namen **Aktivitäten**, **Multiaktivitäten**, **Tagesmodelle** oder **Ganztägige Aktivitäten**.

- Um die *Start- oder Endzeit* zu ändern, klicke auf ein **Zeitfeld**, gib die neue Zeit ein oder ändere die Zeit mit den Pfeiltasten.
- Verwende **-/0/+**, um anzugeben, ob die Start- oder Endzeit der Aktivität an einem anderen Tag liegt. Behalte **0** bei, wenn die Start- oder Endzeit am ausgewählten Tag liegt. Klicke auf **-**, wenn die Start- oder Endzeit am vorherigen Tag liegt. Verwende **+**, wenn sie am folgenden Tag liegt.
- Um das *Aktivitäts- oder Tagesmodell* zu ändern, klicke auf den **Namen einer Aktivität oder eines Tagesmodells** auf der linken Seite. Wähle die Aktivität oder das Tagesmodell, das Du verwenden möchtest, aus dem Dropdown-Menü aus.

## injixo löst Bearbeitungskonflikte automatisch auf

Wenn Du mit dem Eingabedialog Aktivitäten oder Tagesmodelle änderst oder hinzufügst, können sich die Zeitbereiche der neuen und alten Elemente zunächst überschneiden. Wenn Du das Fenster mit *OK*{:.doc-button} schließt, löst injixo diese Konflikte auf folgende Weise auf:

Wenn Du eine *einzelne Aktivität* einfügst oder bearbeitest, die eine Überlappung erzeugt, überschreibt diese Aktivität (Teile von) anderen Schichten innerhalb des Überlappungszeitraums.

Wenn Du *mehrere Aktivitäten* einfügst oder bearbeitest, werden alle Aktivitäten, einschließlich derer, die zuvor bereits geplant waren, in der Reihenfolge ihrer Startzeiten neu eingefügt. Im Falle von Überschneidungen werden Aktivitäten mit einer späteren Startzeit die Aktivitäten mit einer früheren Startzeit (teilweise) überschreiben. In diesem Szenario können daher bestehende Planinhalte neu eingefügte Aktivitäten (teilweise) überschreiben.

Öffne den Eingabedialog erneut, um zu überprüfen, ob der resultierende Schichtplan Deinen Bedürfnissen entspricht. Hier ein Beispiel:

Vorhandene Aktivitäten  
- 08:00 bis 09:00 `Verkauf`
- 09:00 bis 11:00 `Service`

Neue Aktivität
- 07:00 bis 10:00 `Schulung`

Bearbeitete Aktivität
- 09:00 bis 12:00 `Service`

Resultierende Aktivitäten:  
- 07:00 bis 08:00 `Schulung`
- 08:00 bis 09:00 `Verkauf`
- 09:00 bis 12:00 `Service`

Bewegliche Korridorelemente, wie z.B. Korridorelemente für Pausen in Tagesmodellen, bleiben über neuen oder bearbeiteten Nicht-Korridorelementen stehen. Erfahre mehr über solche {% link_new Korridorelemente | features/administration/daymodels/daymodel-basics.md | #feste-elemente-vs-korridore %}.

## Deine Aktionen rückgängig machen

Wenn Du das {% link_new ActiveX-freie Schicht Center | features/scheduling/shiftcenter/shift-center-overview.md | #zwei-versionen-des-schicht-centers %} unter *Plan > Schicht Center*{:.breadcrumbs} verwendest, kannst Du Deine letzte Änderung durch Drücken von **STRG + Z** rückgängig machen.

Wenn Du das Schicht Center mit ActiveX unter *WFM > Scheduling > SchedulePro > Schicht Center*{:.breadcrumbs} verwendest, kannst Du den **Button mit dem blauen Pfeil**<!-- Screenshot?--> in der Aktionsleiste klicken oder **STRG + Z** drücken. Die Option, eine einzelne Aktion rückgängig zu machen, verfällt nach dem Abmelden oder nach dem Öffnen eines anderen Menüpunktes.

### Vorherige Aktionen anzeigen und rückgängig machen

Doppelklicke auf eine **Tageszelle** und klicke auf den Tab **Verlauf**. Es wird der aktuelle Stand des Mitarbeiterplans für das ausgewählte Datum in der ersten Zeile angezeigt. In den anderen Zeilen kannst Du frühere Versionen des Tagesmodells oder der Aktivitäten in absteigender zeitlicher Reihenfolge sehen.

{{ 1 | image: 'Vorherigen Planungsstand zurücksetzen', '75%' }}

Um eine frühere Version für den gewählten Tag und Mitarbeiter wiederherzustellen:

1. Klicke auf die **numerierte Schaltfläche** links neben einem Eintrag. Du kannst keine Zeilen wiederherstellen, deren Inhalt bereits in der Administration gelöschte Elemente enthält.
2. Klicke auf *OK*{:.doc-button}, um die Daten in der ausgewählten Zeile wiederherzustellen.

Du kannst jeweils nur den Verlauf eines einzelnen Mitarbeiters und eines einzelnen Tages wiederherstellen.

## Tagesmodelle in ihre Aktivitäten zerlegen

Du kannst ein Tagesmodell in die Abfolge seiner einzelnen Aktivitäten zerlegen. Anschließend kannst Du die Aktivitäten des Tagesmodells einzeln bearbeiten.

Um ein Tagesmodell in seine Aktivitäten aufzuteilen:  

1. Klicke mit der rechten Maustaste auf ein **Tagesmodell**.
2. Wähle **Schichtbezug lösen** im Kontextmenü.

Hinweis: Automatische Planungsprozesse wie der *Volloptimierte Plan* zerlegen Tagesmodelle immer in ihre Einzelaktivitäten. Verschiebbare Korridorelemente, z.B. für die flexible Positionierung von Pausen, bleiben unverändert als Korridorelemente erhalten. <!-- see setting 48134, activated by default -->

## Ganztägige Aktivitäten entfernen, um Schichtpläne wiederherzustellen

Du kannst ganztägige Aktivitäten verwenden, um Urlaube und andere ganztägige Abwesenheiten in den Schichtplan einzufügen. Wenn Du sie einfügst, ersetzen sie den ursprünglichen Mitarbeiterplan. Du kannst die manuell hinzugefügten ganztägigen Aktivitäten auch wieder entfernen, um den ursprünglichen Schichtplan des Mitarbeiters wiederherzustellen:

1. Wähle **eine oder mehrere Zellen** aus, die ganztägige Aktivitäten enthalten. Klicke mit der rechten Maustaste auf die ausgewählten Zellen.
2. Wähle **Ganztägige Aktivität zurücknehmen** im Kontextmenü. Dadurch werden die ursprünglichen Mitarbeiterpläne wiederhergestellt.
