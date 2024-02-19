---
title: Konstanter Bedarf
toc: false
description: Schreibe einen konstanten Mitarbeiterbedarf auf Grundlage von Benutzereingaben mithilfe des Skripts 'Allgemein - Konstanter Bedarf'
---

Das Bedarfsskript *Allgemein - Konstanter Bedarf* schreibt einen konstanten Mitarbeiterbedarf auf Grundlage von Benutzereingaben. Speichere einen Mitarbeiterbedarf für mehrere Aktivitäten und mehrere Wochen in einem Arbeitsschritt oder korrigiere diesen nur für einzelne Aktivitäten und einzelne Tage. Historische Daten wie Vorgänge oder die durchschnittliche Vorgangsdauer spielen dabei keine Rolle.

Der Einsatz des Skripts ist sinnvoll, wenn

* bestimmte Aktivitäten einen festen Bedarf voraussetzen, z. B. wenn Du für die Bearbeitung von E-Mails jeden Nachmittag zwei Mitarbeiter benötigst.
* Du eine (Test-)Planung durchführen möchtest und (noch) keine historischen Werte vorliegen.

<!-- @cadamini: I put these in comments because they were showing in EN. Pls show me how the "includes" work. -->
{% include reusables/{{ page.lang }}/scripts/cloud-special-method.md %} 
{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}

## Das Skript starten 

1. Gib ein **Startdatum** und eine **Anzahl Tage** an, um den Zeitraum festzulegen.  

    Abhängig vom Wert des Felds **Wochentagsabhängig** erscheinen im Dialog die angegebene Anzahl **Tage mit Zeitabschnitten** als Tag 1...n oder als Wochentage. Wird das Skript mit Wochentagen ausgeführt, berücksichtigt es die Einstellung für den Start der Planungswoche.

2. Wähle für jede Aktivität einzeln eine **Planungseinheit** und eine **Aktivität**.

3. Gib den Bedarf für einen oder mehrere Zeitabschnitte des Tages in die entsprechenden Felder ein. Möglich sind Eingaben mit einer maximalen Dauer von 24 Stunden, d.&nbsp;h. von *00:00* bis *00:00*. Die Werte für die ausgefüllten Zeitabschnitte werden nur geschrieben, wenn die entsprechenden Checkboxen angehakt sind.

4. Klicke *Ok*{:.doc-button}, um die Daten zu schreiben.

## Erläuterungen zu weiteren Eingabefeldern

* **Zu bestehendem Bedarf addieren**  
  Die Option addiert die eingetragenen Werte zum bereits vorhandenen Mitarbeiterbedarf. Ist die Option deaktiviert, wird bereits gespeicherter Mitarbeiterbedarf überschrieben.

* **Bedarf im Überschneidungsbereich addieren**  
  Die Option legt fest, wie Werte, die sich teilweise mit einem bereits vorhandenen Mitarbeiterbedarf überschneiden, behandelt werden. Die Zeitabschnitte können sich ebenfalls überschneiden. Bei aktivierter Option wird der Bedarf aufaddiert, sonst überschrieben.

* **Öffnungszeiten der Planungseinheit beachten**  
  Die Option legt fest, ob der Bedarf nur innerhalb der Öffnungszeiten der Planungseinheit geschrieben wird.

* **Tage mit Zeitabschnitten**  
  Das Auswahlfeld legt die Anzahl der Tage fest, für welche die Eingabefelder für die Zeitabschnitte angezeigt werden. Der Mitarbeiterbedarf für die angegebenen Tage wiederholt sich ab dem *Startdatum* in dem unter **Anzahl Tage** angegebenen Zeitraum.  
  Ein Wert von 5 bedeutet, dass Mitarbeiterbedarf für die ersten fünf Tage der Planungswoche (Mo, Di, Mi, Do und Fr) eingetragen wird. Für fehlende Tage (Sa und So) wird nichts geschrieben.

* **Zeitabschnitte pro Tag**  
  Das Auswahlfeld legt die Anzahl der Zeitabschnitte pro Tag fest, für die Du einen Mitarbeiterbedarf angeben willst. Es werden entsprechend viele Eingabefelder im Dialog angezeigt.

* **Anzahl Aktivitäten**  
  Das Feld legt die Anzahl der Aktivitäten fest. Der Dialog enthält entsprechend viele Spalten.  
