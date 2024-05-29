---
title: Verträge erstellen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erstelle Verträge, um die Arbeitszeiten pro Woche und andere Regeln für deine Mitarbeiter festzulegen.
redirect_from:
  - de/contracts-overview/
  - de/contract-creation/
redirect_reason: Updated filename on 08 December 2023
---

In _Plan > Konfiguration > Verträge_{:.breadcrumbs} kannst du Verträge für die Mitarbeiter erstellen, die du planen möchtest. Du kannst beliebig viele Verträge erstellen. Mit Verträgen kannst du zeitliche Einschränkungen für die Schichtplanung festlegen:

- Das Minimum und Maximum an Arbeitstagen pro Woche
- Das Minimum, Soll und Maximum an Arbeitsstunden pro Tag
- Das Minimum, Soll und Maximum an Arbeitsstunden pro Woche
- Das Maximum an Arbeitsstunden pro Monat

Mit Verträgen bildest du auch Informationen über Arbeitszeitrichtlinien in deinem Unternehmen ab, z.&nbsp;B. die Anzahl der Ruhetage zwischen Schichten. Außerdem kannst du Planungsparameter für die Funktionalität **Optimierten Plan erstellen** festlegen.

## Verträge erstellen

Um einen neuen Vertrag zu erstellen, gehe zu _Plan > Konfiguration > Verträge_{:.breadcrumbs} und führe folgende Schritte aus:

1. Klicke auf das {% icon item-add %} oben links.
2. Gib im Abschnitt **Allgemein** die grundlegenden Informationen zu deinem Vertrag ein:<br>
   - **Name**: Gib einen eindeutigen Namen (max. 50 Zeichen) ein.
   - **Kurzbezeichnung**: Gib den Namen oder eine Kurzversion davon ein (max. 25 Zeichen).
   - **Farbe**: Die Farbe kann dir helfen, den Vertrag leichter zu identifizieren.
3. Wähle aus dem Dropdown-Menü **Arbeitstage pro Woche** die gewünschte Anzahl aus.
4. Wähle aus dem Dropdown-Menü **Berechnung Arbeitstage** eine Berechnungsmethode aus: <br>
   - **Standard**: Die vorgegebene Reihenfolge der Tage in der Planungswoche wird eingehalten.<br>
   - **Flexibel**: Die Arbeitstage werden flexibel innerhalb der Öffnungszeiten der Planungseinheit gewählt.
5. Gib die [**Arbeitszeitvorgaben**](#arbeitszeitvorgaben) und die [**Wochentagsarbeitszeit**](#wochentagsarbeitszeit) ein.
6. (Optional) Konfiguriere die [**AutoScheduler-Parameter**](#autoscheduler-parameter) oder die [**Planungsparameter**](#planungsregeln).
7. Um deinen Vertrag zu speichern, klicke auf _OK_{:.doc-button}.

## Arbeitszeitvorgaben

Arbeitszeitvorgaben für das Minimum, Soll und Maximum an Arbeitsstunden spielen eine zentrale Rolle für die Schichtplanung. Arbeitszeitvorgaben werden mit Planungsparametern und AutoScheduler-Parametern kombiniert.

### Tag

- **Minimum**: Gib die Mindestarbeitsstunden pro Tag ein. Wenn du keinen Wert eingibst, werden die Sollarbeitsstunden als Minimum verwendet. Dieser Parameter wird durch den Planungsparameter _2615_{:.id-label} verifiziert.
- **Soll**: Gib die Sollarbeitsstunden pro Tag ein. Gib einen Wert zwischen 0 und 24 Stunden ein und beachte die Standardarbeitszeiten.
- **Maximum**: Gib die Höchstarbeitsstunden pro Tag ein. Wenn du keinen Wert eingibst, werden die Sollarbeitsstunden als Maximum verwendet. Dieser Parameter wird durch den Planungsparameter _2614_{:.id-label} verifiziert.

### Woche

- **Minimum**: Gib die Mindestarbeitsstunden pro Woche ein.
- **Soll**: Gib die Sollarbeitsstunden pro Woche ein. Dieser Wert ist erforderlich, wenn du im Abschnitt **Wochentagsarbeitszeit** keine Werte eingegeben hast.
- **Maximum**: Gib die Höchstarbeitsstunden pro Woche ein. Dieser Parameter wird durch die Planungsparameter _2618_{:.id-label} und _2629_{:.id-label} verifiziert.

> Beginn der Arbeitswoche ändern
>
> Standardmäßig ist der Beginn deiner Arbeitswoche auf Sonntag bzw. Montag festgelegt, je nachdem, in welcher Region du dich befindest. Falls du einen anderen Tag dafür festlegen möchtest, wende dich an deinen Consultant.

### Monat

- **Maximum**: Gib die Höchstarbeitsstunden pro Monat ein. Dieser Parameter wird durch den Planungsparameter _2619_{:.id-label} verifiziert.

## Wochentagsarbeitszeit

Du kannst für Mitarbeiter die Anzahl an Arbeitsstunden pro Tag im Vertrag festlegen.

Beispiel:
Ein Mitarbeiter arbeitet 40&nbsp;Stunden pro Woche mit je 8&nbsp;Stunden pro Tag und hat immer mittwochs und sonntags frei. Um sicherzustellen, dass die Arbeitsstunden in der Arbeitswoche korrekt verteilt werden, gib in den Feldern für Montag, Dienstag, Donnerstag, Freitag und Samstag jeweils 8:00 ein und in den Feldern für Mittwoch und Sonntag jeweils 0:00. Wenn dieser Mitarbeiter sich krank meldet oder bezahlten Urlaub nimmt, werden seine Arbeitsstunden weiterhin auf Grundlage der von dir hier festgelegten Werte berechnet.

Bei einem leeren Feld wird standardmäßig diese Formel verwendet: [Wöchentliche Sollstunden/Anzahl der Arbeitstage]. Dies kann zu Fehlberechnungen führen, weil injixo eine gleichmäßige Verteilung der Arbeitsstunden auf alle Arbeitstage annimmt.

## AutoScheduler-Parameter

- **Max. Anz. aufeinander folgender Arbeitstage**: Fülle dieses Feld aus, wenn deine Planungseinheit an 7 von 7 Tagen geöffnet ist. Gib die maximale Anzahl aufeinanderfolgender Arbeitstage ein, die die Funktionalität **Optimierten Plan erstellen** beachten muss. Wenn ein Mitarbeiter beispielsweise fünf Tage pro Woche arbeitet, verwende diesen Parameter, um zu verhindern, dass er an zehn aufeinanderfolgenden Tagen arbeiten muss.
- **Min. Anz. freier Tage pro Woche**: Fülle dieses Feld aus, wenn deine Planungseinheit an den Wochenenden geöffnet ist. Gib die Mindestanzahl aufeinanderfolgender arbeitsfreier Tagen ein, die die Funktionalität **Optimierten Plan erstellen** je Planungswoche beachten muss.
- **Min. Anz. aufeinander folgender freier Tage pro Woche**: Fülle dieses Feld aus, wenn du sicherstellen möchtest, dass deine Mitarbeiter mindestens einen zusammenhängenden Zeitraum an arbeitsfreien Tagen pro Woche haben. Gib die Mindestanzahl aufeinanderfolgender arbeitsfreier Tage pro Woche ein, die die Funktionalität **Optimierten Plan erstellen** je Planungswoche beachten muss.
- **Max. Anz. aufeinander folgender freier Tage**: Fülle dieses Feld aus, wenn du die Anzahl aufeinanderfolgender arbeitsfreier Tage für deine Mitarbeiter einschränken möchtest, um eine konsistente Besetzung sicherzustellen und lange Unterbrechungen zu vermeiden. Gib die maximale Anzahl aufeinanderfolgender arbeitsfreier Arbeitstage ein, die die Funktionalität **Optimierten Plan erstellen** beachten muss. Der Wert wird nicht pro Woche geprüft, sondern über mehrere Wochen hinweg.
- **Min. Ruhezeit (Stunden) zwischen zwei Schichten**: Fülle dieses Feld aus, wenn du laut Arbeitsgesetz Ruhezeiten zwischen Schichten einhalten musst. Gib die Mindestruhezeit ein, die die Funktionalität **Optimierten Plan erstellen** beachten muss.
- **Mindestanzahl Arbeitstage pro Woche**: Fülle dieses Feld aus, um eine wöchentliche Mindestbesetzung in deiner Planungseinheit sicherzustellen, damit immer genügend Mitarbeiter das prognostizierte Anrufvolumen bearbeiten können. Gib die Mindestanzahl der Arbeitstage an, die pro Planungswoche geplant werden sollen.
- **Richtzeitkonto statt Soll pro Woche laut Vertrag**: Aktiviere diese Checkbox, wenn du möchtest, dass die Funktionalität **Optimierten Plan erstellen** die Werte aus den berechneten Richtzeitkonten verwendet. Erfahre mehr über {% link_new Richtzeitkonten | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Max. ein Arbeitstag am Samstag alle n Wochen**: Fülle dieses Feld aus, wenn du eine gerechte Verteilung von Wochenendarbeit unter Mitarbeitern sicherstellen möchtest und um zu verhindern, dass dieselben Mitarbeiter ständig samstags arbeiten müssen. Gib die maximale Anzahl an Wochen (1-5) an, an denen ein Mitarbeiter samstags arbeiten soll. Zum Beispiel bedeutet ein Wert von 2 jeden zweiten Samstag.
- **Zuweisen eines Arbeitstages nach einem ganztägigen Urlaub**: Fülle dieses Feld aus, wenn du erzwingen möchtest, dass die Funktionalität **Optimierten Plan erstellen** einen Arbeitstag nach einem ganztägigen Urlaub plant. Wenn der Mitarbeiter mehrere aufeinanderfolgende Tage abwesend ist, wird der Arbeitstag nach dem letzten Abwesenheitstag geplant.

## Planungsregeln

Planungsregeln legen allgemeine und vertragsbezogene Regeln für deinen Planungsprozess fest. In der Vertragskonfiguration heißen Planungsregeln Planungsparameter.

Um die Liste aller verfügbaren Planungsregeln aufzurufen, gehe zu _WFM > Administration > System > Planungsregeln_{:.breadcrumbs}. Um Details zu einer Regel aufzurufen, wähle die entsprechende Regel in der Liste aus. Üblicherweise werden Planungsregeln während deines injixo-Onboardings gemeinsam mit deinem Consultant konfiguriert.

Benutzer mit Admin-Zugriff können jede Regel bearbeiten, Ausnahmen festlegen und benutzerdefinierte Werte auf die Standardeinstellungen zurücksetzen.

> Potenzielles Risiko für Planungsfehler
>
> Änderungen an den Planungsregeln sind komplex und können zu Planungsfehlern führen, wenn sie nicht korrekt durchgeführt werden. Ändere keine Planungsregeln selbst, wenn du unsicher bist, welche Konsequenzen dies hat. Wenn du eine Planungsregel ändern möchtest, wende dich an deinen Consultant.

Vertragsbezogene Planungsregeln sorgen dafür, dass die Bedingungen jedes Vertrags bei der Schichtplanung beachtet werden. Wenn beispielsweise ein Vertrag einen bestimmten Ruhezeitraum oder eine Höchstanzahl von Arbeitsstunden pro Tag vorgibt, stellen die Planungsregeln sicher, dass diese Bedingungen erfüllt werden. Gegen diese Regeln zu verstoßen kann Planungskonflikte, Unzufriedenheit unter den Mitarbeitern und potentielle Vertragsverletzungen zur Folge haben.

### Statusanzeige

Du kannst den Status jeder Planungsregel in der Liste erkennen:

- Grau: Die Regel ist deaktiviert und wird bei der Schichtplanung nicht berücksichtigt.
- Gelb: Die Regel ist im Soft-Modus. Wenn gegen diese Regel verstoßen wird, wird bei der Schichtplanung eine Warnung angezeigt, der Vorgang wird aber fortgesetzt.
- Rot: Die Regel ist vollständig aktiviert. Jede Verletzung des Vertrags führt zu einer Fehlermeldung, die den Regelverstoß beschreibt.
