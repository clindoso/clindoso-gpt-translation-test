---
title: Xlink Skripte erstellen
product_label:
  - on-premise
redirect_from:
  - /support/xlink/xlink-import-skripte-erstellen/
---

Import-Skripte legen fest, wie der Xlink mit den zu importierenden Daten umgeht.

Beim Mapping für Anrufdaten kannst Du automatisch Skripte erstellen, die alle zugeordneten ACD-Kennzahlen aufsummieren und diese in die zugeordnete _WFM_{:.menu-item}-Queue-Wertetyp Kombination schreiben.

Import-Skripte werden in der Programmiersprache _BASIC_ erstellt. Der Xlink unterstützt den Dialekt "Enable Basic".

Wenn Du besondere Skripte erstellen möchtest, z.B. für Wochentags- oder Uhrzeit-abhängige Ergebnisse oder die Berechnung von Durchschnittswerten, kannst Du nicht einfach die automatisch erstellte Vorlage nutzen, sondern Du musst selbst Anpassungen vornehmen.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

## Anlegen eigener Skripte

Um ein eigenes Import-Skript zu erstellen, verwende immer _Erstellen_{:.doc-button}. Die Skriptvorlage stellt eine ideale Ausgangsbasis auch für eigene Skripte dar.

### Beispiel für Standard-Skript mit einer zugeordneten Kennzahl

```
Dim Ergebnis As Long
Dim Wochentag As Long
Dim Minuten As Long
Dim Para1 As Long

Sub Main()
  Ergebnis = Para1 * 100
End Sub
```

## Prozedurbereich

Den Prozedurbereich leitest Du mit der Zeile `Sub Main()` ein und mit `End Sub` beendest Du die Prozedur. Innerhalb des Prozedurbereichs kannst Du im Rahmen der von der Skriptsprache Enable Basic verfügbaren Möglichkeiten frei programmieren.

## Variablen

Im Deklarationsbereich (mit `Dim` beginnende Zeilen) werden alle Variablen definiert, die innerhalb des Skriptes verwendet werden. Durch das Definieren werden die Variablen dem System "bekannt gemacht".

### Vordefinierte Variablen

Es gibt ein paar vordefinierte Variablen, die unterhalb beschrieben werden, deren Namen nicht verändert werden dürfen, da der Xlink das Ergebnis der Skriptprozedur sonst nicht auswerten kann.

#### Ergebnis

Hier wird das Ergebnis aus der Skriptprozedur zugeordnet. Um Speicherplatz in der Datenbank zu sparen, kann die Variable nur ganzzahlige Werte enthalten. Nachkommastellen werden nicht berücksichtigt, sondern abgeschnitten. Das Ergebnis wird vor dem Speichern ins _WFM_{:.menu-item} mit 100 multipliziert (`Ergebnis = Para1 * 100`). Auf diese Weise werden Werte wie z.&nbsp;B. "80,23" in "8023" umgewandelt und können dadurch als Ganzzahl gespeichert werden.

#### Para... (Para1, Para2 usw.)

Hier werden die Werte der ACD-Kennzahlen für das Zeitintervall zugeordnet, für dass das Skript ausgeführt wird. Dies geschieht genau in der Reihenfolge, in der ACD-Kennzahlen dem WFM-Wertetyp zugewiesen sind. Die Anzahl der Para-Variablen muss der Anzahl zugeordneter ACD-Kennzahlen entsprechen.

#### Wochentag

Diese Variable wird vom Xlink mit einem Zahlenwert befüllt, der den Wochentag des importierten Datums darstellt. Die Zählung der Wochentage beginnt bei Sonntag mit 1. Mit diesen Variablen lassen sich wochentagsabhängige Auswertungen realisieren; so kannst Du z.B. die Formel zur Auswertung der zugeordneten ACD-Kennzahlen vom Wochentag abhängig machen.

##### Beispiel für wochentagsabhängige Berechnung:

```
Dim Ergebnis As Long
Dim Wochentag As Long
Dim Minuten As Long
Dim Para1 As Long
Dim Para2 As Long

Sub Main ()
  If (Wochentag = 2) Then
    Ergebnis = Para1 * 100
  Else
    If (Wochentag = 3) Then
      Ergebnis = Para2 * 100
    Else
      Ergebnis = (Para1 + Para2) * 100
    End If
  End If
End Sub
```

- Montag ist das Ergebnis nur die erste zugeordnete Kennzahl
- Dienstag ist das Ergebnis nur die zweite zugeordnete Kennzahl
- An allen anderen Tagen ist das Ergebnis die Summe der beiden Kennzahlen.

#### Minuten

Diese Variable wird vom Xlink mit dem Startzeitpunkt des Intervalls befüllt, für welches die ACD-Kennzahlen importiert werden. Die Zeitangabe ist "Minuten seit Mitternacht" (also 0 für 00:00 Uhr, 60 für 01:00 Uhr usw.). Der Name der Variablen ist vordefiniert und darf von Dir nicht geändert werden. Mit dieser Variablen kannst Du zeitabhängige Auswertungen realisieren. So kannst Du z.B. Anrufe, die außerhalb eines bestimmten Zeitfensters eingingen, in der Auswertung ignorieren.

##### Beispiel für minutenabhängige Berechnung:

```
Dim Ergebnis As Long
Dim Wochentag As Long
Dim Minuten As Long
Dim Para1 As Long

Sub Main ()
  If (Minuten < 360) or (Minuten >= 1200) Then
    Ergebnis = 0
  Else
    Ergebnis = Para1 * 100
  End If
End Sub
```

- Zwischen 6 und 20 Uhr wird das Ergebnis der zugeordneten Kennzahl verwendet.
- Vor 6 und nach 20 Uhr ist das Ergebnis 0.

#### Weitere Beispiele

##### Beispiel für Schwellwerte

Schwellwerte kannst Du z.B. nutzen, um bestimmte Volumina nicht anzuzeigen, oder bei einer bestimmten Anzahl von Anrufen eine bestimmte Berechnung auszuführen, im Beispiel unterhalb werden beispielhaft nochmal 20% aufgeschlagen.

```
Sub Main ()
  If Para1 < 10 Then
    Ergebnis = 0
  Else
    If Para1 > 1000
      Ergebnis = Para1 * 100 * 1.2
    else
      Ergebnis = Para1 * 100
    End If
  End If
End Sub
```

##### Durchschnittliche Gesprächszeiten

Meistens wird diese Art der Berechnung genutzt, wenn die Gesprächszeit als Gesamtwert vorliegt. Dabei wird die Gesamtgesprächszeit durch die Anzahl der bearbeiteten Anrufe geteilt.

Wenn Du Divisionen verwendest, stelle sicher, dass nicht durch null dividiert wird. Dies kann durch eine Wenn-dann-Abfrage erreicht werden. Der Versuch, im Rahmen der Skriptausführung durch null zu dividieren, würde zum Abbruch des Importvorgangs und möglicherweise zu einem Paradox im Raum-Zeit-Kontinuum führen!

```
Sub Main ()
  If Para2 = 0 Then
    Ergebnis = 0
  Else
    Ergebnis = (Para1/Para2) * 100
  End If
End Sub
```

### Eigene Variablen

Natürlich kannst Du auch eigene Variablen definieren, z.B. um Zwischenergebnisse o.ä. zu speichern. Die Deklaration beginnst Du mit dem Schlüsselwort `Dim`, z.B. (`Dim Zwischenergebnis As Long`) Der Variablenname muss mit einem Buchstaben beginnen, darf neben Buchstaben auch Zahlen enthalten und darf nicht identisch mit einem reservierten Wort der Programmiersprache BASIC sein. Details zu den verfügbaren Variablentypen findest Du in der Sprachreferenz zu Enable Basic.

## Syntaxprüfung

Um für das erstellte Skript eine Syntaxprüfung durchzuführen, klicke _Testen_{:.doc-button}. Das Skript wird nur auf syntaktische Korrektheit geprüft, eine Prüfung auf mathematisch unzulässige Aktionen wie die Division durch Null findet nicht statt.

> Abschließende Hinweise
>
> Klammersetzung
>
> Bei gemischter Verwendung von Additionen, Subtraktionen, Multiplikationen und Divisionen musst Du besonders auf korrekte Klammersetzung achten. Die Anweisung `Ergebnis = Para1 + Para2 * 100` wird Dich zu einem anderen Ergebnis führen, als z.B. `Ergebnis (Para1 + Para2) * 100`.
>
> Skript-Ausgaben nur im Test verwendet
>
> Beim Erscheinen eines Dialogs oder Hinweisfensters wird die Skriptausführung und damit der Import bis zur Bestätigung durch den Anwender angehalten und erst danach fortgesetzt.
