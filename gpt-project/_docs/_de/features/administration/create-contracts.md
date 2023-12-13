---
title: Verträge anlegen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /de/contract-creation/
redirect_reason: Updated filename on 08 December 2023
---

Verträge enthalten Angaben zu den Arbeitszeiten, zu betrieblichen Regelungen und zu Parametern für Planungsregeln, die für die Planung Deiner Mitarbeiter von Bedeutung sind. In *WFM > Administration > Scheduling > Verträge*{:.breadcrumbs} legst Du die einzelnen Verträge an, die in Deinem Contact Center für injixo relevant sind.

Gehe wie folgt vor, um einen Vertrag anzulegen:

1. Klicke auf das grüne *+*{:.doc-button} oben links.
2. Definiere einen Namen und eine Kurzbezeichnung.
3. Wähle die Anzahl der *Arbeitstage pro Woche* aus.
4. Klicke auf *OK*{:.doc-button}, um den Vertrag zu speichern.

Du kannst beliebig viele verschiedene Verträge anlegen. Kleine Gruppen von Mitarbeitern oder sogar einzelne Mitarbeiter können für besondere Arbeitszeitregelungen eigene Verträge erhalten. Generell solltest Du Dir überlegen, welche Arbeitszeitmodelle sinnvoll zusammengeführt werden können und ob abweichende Arbeitszeiten anderweitig abgebildet werden können z.B. über Verfügbarkeiten und Schichtfolgen für einzelne Mitarbeiter.

{{ 1 | image: 'Vertrag anlegen' }}

## Berechnung Arbeitstage

injixo unterscheidet zwei Modi für die Berechnung der Arbeitstage. In unserem Beispiel gehen wir von einem Vertrag mit 5 Arbeitstagen und einem Wochensoll von 20 Stunden aus, um Dir die Funktionsweise zu erläutern.

### Standard

Die Arbeitszeitberechnung folgt den Tagen der Planungswoche, bei 5 Tagen heißt das:  

* Die Sollzeit wird auf die ersten 5 Arbeitstage der Woche verteilt.
* Die tägliche Sollzeit für Montag bis Freitag beträgt 4 Stunden, 0 Stunden am Wochenende.

> Hinweis
>
> Nicht-ganztägige Aktivitäten werden bei der Nutzung von Arbeitszeitvorgaben an allen Tagen der Planungswoche als Arbeitszeit erfasst. Dementsprechend können auch Schichten an einem Samstag oder Sonntag vergeben werden.
>
> Wochentagsarbeitszeiten bei der Nutzung der Methode *Standard* führen dazu, dass Arbeitszeiten nur an den Tagen gezählt werden, für welche Werte eingetragen sind.
>
> Eine bezahlte, ganztägige Abwesenheit wird dann mit der Zeit bewertet, die für den Wochentag eingetragen ist.

### Flexibel

Die Arbeitszeitberechnung erfolgt zufällig, bei 5 Tagen heißt das:

* Die Sollzeit wird auf 5 zufällige Wochentage mit Öffnungszeiten verteilt.
* Die tägliche Sollzeit beträgt für 5 beliebige Tage 4 Stunden und für 2 Tage 0 Stunden.

## Tägliche Arbeitszeit

Du kannst in den Verträgen die täglichen Nettoarbeitszeiten entweder als *Arbeitszeitvorgaben* oder als *Wochentagsarbeitszeit* definieren. *Arbeitszeitvorgaben* legen einen Rahmen für die tägliche und wöchentliche Arbeitszeit fest, *Wochentagsarbeitszeiten* eine exakte Dauer pro Tag. Dabei haben *Wochentagsarbeitszeiten* Vorrang und überschreiben im Zweifelsfall die *Arbeitszeitvorgaben*. Auch Richtzeitberechnungen nutzen die definierten Zeiten in der beschriebenen Reihenfolge.

### Arbeitszeitvorgaben

*Arbeitszeitvorgaben* gliedern sich in Werte für Minimum-, Soll- und Maximum für Tag, Woche und Monat. Es werden mindestens Werte in den Feldern für das Minimum und Maximum pro Tag und das Soll pro Woche benötigt. Wenn kein Minimum oder Maximum pro Tag definiert sind, wird der Sollwert genutzt. Spezifiziere Deine Angaben in diesem Fall als Planungsparameter im Vertrag für die Planungsregeln 2614 und 2615.

{{ 2 | image: 'Verträge Arbeitszeitvorgaben', '50%'}}

Im Beispiel verteilt sich eine wöchentliche Sollarbeitszeit von 40 Stunden auf 5 Arbeitstage. Es können genau 8 Stunden auf jeden Arbeitstag entfallen. Genauso sind aber auch kürzere Schichten ab 6 Stunden und längere Schichten bis zu 10 Stunden möglich.

Achte darauf, dass die Tages- und Wochenwerte eine sinnvolle Kombination ergeben. Es ergibt keinen Sinn, bei 5 Arbeitstagen pro Woche ein Tagesminimum von 6 Stunden zu erlauben und die Woche auf 25 Stunden zu beschränken. In diesem Fall müsste Dein Mitarbeiter lt. Tagesminimum mindestens 30 Stunden in der Woche arbeiten.

> Das *Wochensoll*
>
> - hat Einfluss auf die Ist-Zeit von bezahlten, ganztägigen Aktivitäten. Die Zeit berechnet sich aus Wochensoll durch Anzahl Arbeitstage.
> - muss "glatt" durch die Anzahl der Arbeitstage teilbar sein, also ohne verbleibende Minuten oder Sekunden.
> - muss zusammen mit dem Tagessoll für die Richtzeitkonten-Berechnung ausgefüllt sein.

Diese Planungsregeln spielen eine Rolle für die Prüfung von Arbeitszeiten:
- *2614*{:.id-label} *Maximale Arbeitszeit/Tag gemäß Vertrag (Tagesmodelle und Aktivitäten)*
- *2615*{:.id-label} *Minimale Arbeitszeit/Tag gemäß Vertrag (Tagesmodelle und Aktivitäten)*
- *2618*{:.id-label} *Maximale Arbeitszeit/Woche gemäß Vertrag (Tagesmodelle und Aktivitäten)*
- *2619*{:.id-label} *Maximale Arbeitszeit/Monat gemäß Vertrag (Tagesmodelle und Aktivitäten)*
- *2629*{:.id-label} *Schwellwert für die Überschreitung der Arbeitszeit in aufeinander folgenden Wochen gemäß Vertrag (Tagesmodelle und Aktivitäten)*

### Wochentagsarbeitszeit

Nutze den Abschnitt Wochentagsarbeitszeit für Verträge mit einer festen Stundenanzahl pro Wochentag für alle oder bestimmte Tage.

{{ 3 | image: 'Verträge Wochentagsarbeitszeit', '40%'}}

Mit einem Nullwert kannst Du festlegen, an welchen Wochentagen nicht gearbeitet wird. Es müssen __alle__ Felder ausgefüllt werden, da der Vertrag sonst ungültig ist und der Mitarbeiter von der Optimierung ausgeschlossen wird.

> Hinweis
>
> Nutze für Verträge mit eingetragener Wochentagsarbeitszeit zur Berechnung der Arbeitstage immer die Methode *Standard*, *nicht* die Methode *Flexibel*.  
