---
title: Urlaubsanspruch anzeigen und bearbeiten
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Urlaubsanspruch anzeigen, bearbeiten, ins nächste Jahr übertragen und Daten zum Urlaubsanspruch als CSV-Datei exportieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-absences-management.md
---

In diesem Artikel lernst du:
* wie du den Urlaubsanspruch deiner Mitarbeiter einsiehst und bearbeitest.
* wie du verbleibenden Urlaubsanspruch ins Folgejahr überträgst.
* wie du Daten zum Urlaubsanspruch als CSV-Datei exportierst.

Urlaubsanspruch ist die Basis für die Urlaubsplanung mit injixo.

## Urlaubsanspruch anzeigen

1. Gehe zu *Plan > Urlaub/Abwesenheiten*{:.breadcrumbs} und klicke auf *Urlaubsansprüche bearbeiten*{:.doc-button}, um die Urlaubskonten deiner Mitarbeiter zu verwalten.
2. Wähle eine **Planungseinheit**, eine **Auswahl** (optional) und ein **Jahr**.
3. Filtere die Daten optional mit dem Textfeld **Suche**.

{{ 1 | image: 'Urlaubsanspruch', '100%' }}

Neben der Personalnummer, dem Namen und dem Vertrag der Mitarbeiter siehst du folgende Spalten:

<style>
table th:first-of-type {
    width: 20%;
}
table th:nth-of-type(2) {
    width: 80%;
}
</style>
Spalte                              | Erläuterung
----------------------------------- | ----------------
Verbleibender Urlaub in diesem Jahr | Resturlaubsanspruch im aktuellen Jahr. Ergibt sich aus dem Resturlaub aus dem Vorjahr plus dem Urlaubsanspruch im aktuellen Jahr minus den Urlaubstagen im aktuellen Jahr, die bereits in der Ebene Plan eingetragen wurden.
Resturlaub vom letzten Jahr         | Anzahl der Resturlaubstage aus dem vergangenen Jahr. Diesen Wert kannst du manuell mit einem negativen oder positiven Wert überschreiben.
Urlaubsanspruch                     | Anzahl an Urlaubstagen, die dem Mitarbeiter im aktuellen Jahr insgesamt zustehen. Diesen Wert kannst du manuell mit einem negativen oder positiven Wert überschreiben.
Genommener Urlaub                   | Prozentualer Anteil der bereits genommenen Urlaubstage am Urlaubsanspruch für das laufende Jahr. Im Spaltenkopf siehst du den Durchschnitt des genommenen Urlaubs für deine aktuelle Filterauswahl.

Gehören Mitarbeiter im Laufe eines Jahres zu mehreren Planungseinheiten, werden immer die Daten für das gesamte Jahr angezeigt, unabhängig von der Filtereinstellung. So musst du die Daten je Mitarbeiter nur einmal eingeben.

> injixo Enterprise On-Premise  
>  
> Du findest die Verwaltung des Urlaubsanspruchs unter *Scheduling > SchedulePro > Urlaubsanspruch*{:.breadcrumbs}. Die Bezeichnungen der einzelnen Felder weichen leicht ab und die Funktionalität ist eingeschränkt (kein Filter, keine Download-Option, nicht die letzten beiden Spalten in der Tabelle). Du musst deine Änderungen außerdem manuell speichern.

### Resturlaubsanspruch anzeigen

Wenn du keine Werte in der Spalte Verbleibender Urlaub in diesem Jahr siehst, musst du deine Mitarbeiter-Verträge bearbeiten:

1. Gehe zu *WFM > Administration > Scheduling > Verträge*{:.breadcrumbs}.
2. Klicke auf einen der **Verträge** von denjenigen Mitarbeitern, für die du den Resturlaubsanspruch anzeigen möchtest.
3. Fülle im Abschnitt Arbeitszeitvorgaben das Feld für die wöchentliche **Sollarbeitszeit** aus.
    {{ 2 | image: 'Wöchentliche Sollarbeitszeit hinzufügen', '60%' }}

4. Klicke *Ok*{:.doc-button}. Ändere bei Bedarf weitere Verträge.
5. Gehe zurück zu *Plan > Urlaub/Abwesenheiten*{:.breadcrumbs}, klicke auf *Urlaubsansprüche bearbeiten*{:.doc-button} und wähle deine Filtereinstellungen.

Die Spalte *Resturlaub vom letzten Jahr* zeigt nun den verbleibenden Urlaubsanspruch pro Mitarbeiter für das Jahr an.

## Urlaubsanspruch hinzufügen und bearbeiten

Du kannst Werte in den Spalten Resturlaub vom letzten Jahr und Urlaubsanspruch für jeden Mitarbeiter hinzufügen, löschen oder bearbeiten:

1. Klicke in ein **Feld** und benutze **Tab** auf deiner Tastatur, um durch die Liste zu navigieren.
2. Gib einen (neuen) **Wert** ein. Benutze **Entf**, um Werte zu löschen. Die Daten werden automatisch gespeichert.

Du kannst Werte für einen bestimmten Vertrag nicht gebündelt auf einmal anpassen. Es ist auch nicht möglich, Daten zu importieren.

## Ungenutzten Urlaubsanspruch ins Folgejahr übertragen

Du kannst den Resturlaubsanspruch des aktuellen Jahres automatisch in das Folgejahr übertragen.

1. Wähle eine **Planungseinheit** und eine **Auswahl** (optional), um nur die Mitarbeiter anzuzeigen, für die du den Urlaubsanspruch übertragen möchtest. Du kannst einzelne Mitarbeiter über das Textfeld **Suchen** auswählen.
2. Wähle das **Jahr** aus, von dem du den Anspruch in das Folgejahr übertragen möchtest.
3. Vergewissere dich, dass die Spalte Verbleibender Urlaub in diesem Jahr Daten enthält. Wenn keine Daten angezeigt werden, befolge die Schritte oben, um den {% link_new Resturlaubsanspruch anzuzeigen | features/scheduling/time-off/vacation-entitlement.md | #resturlaubsanspruch-anzeigen %}.
4. Klicke auf *Urlaubsansprüche übertragen*{:.doc-button}. Dadurch wird der Urlaubsanspruch für alle angezeigten Mitarbeiter ins nächste Jahr in die Spalte Resturlaub vom letzten Jahr übertragen.

## Urlaubsanspruch als CSV-Datei exportieren

Per Klick auf das Download-Icon neben *Urlaubsansprüche übertragen*{:.doc-button} kannst du die aktuell angezeigten Daten in eine CSV-Datei exportieren. Das Format der CSV-Datei ist wie folgt:

```
personnelNumber,name,remainingDaysCurrentYear,remainingDaysLastYear,currentYear,percentTaken,year  
0001,"Neumann, Günter",105.0,75.0,30.0,0,2019  
0003,"Neumann, Moritz",121.0,90.0,31.0,0,2019  
...
```
## Sicherstellen, dass Urlaub vom Jahresurlaubsanspruch abgezogen wird

Nur bezahlte Aktivitäten vom Typ Urlaub, die in die Ebene Plan eingetragen worden sind, verringern den Jahresurlaubsanspruch.

Die Arbeitszeit, die für einen ganzen Urlaubstag vom Jahresurlaubsanspruch abgezogen wird, hängt vom Vertrag des Mitarbeiters ab. Die Formel für die Berechnung lautet: Wochensoll geteilt durch die Anzahl der Arbeitstage pro Woche. Urlaubsanträge von weniger als einem Tag werden exakt anteilig berücksichtigt.

Du kannst Urlaube und andere Abwesenheiten ganztägig oder untertägig (als normale Aktivität mit Start- und Endzeit) manuell in die Ebene Plan eintragen.

Deine Mitarbeiter können im injixo Me Urlaub oder andere Abwesenheiten beantragen, wenn es eine {% link_new Abwesenheitsperiode | features/scheduling/time-off/time-off-periods.md %} für diesen Zeitraum gibt.  
In injixo Classic benötigst du stattdessen eine {% link_new Planperiode vom Typ Urlaub | features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md %}.
In jedem Fall muss die Aktivität vom Typ Urlaub als **Wünschbar in Me** konfiguriert und der Planungseinheit des Mitarbeiters zugewiesen sein.
