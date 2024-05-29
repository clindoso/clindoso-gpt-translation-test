---
title: Anwendungsbeispiele für JobManager
product_label:
  - enterprise
description: Erfahre mehr über wichtige Jobtypen in injixo und wofür sie verwendet werden.
---

Unter _WFM > Administration > System > JobManager_{:.breadcrumbs} kannst du den Beginn verschiedener Jobs automatisieren. Ein Job kann z.&nbsp;B. das Erstellen von Reports sein oder das Einfügen von Schichtfolgen. Wenn du eine Vorlage für einen Job anlegst, musst du {% link_new bestimmte Parameter konfigurieren | features/reporting/jobmanager/jobmanager.md | #jobverarbeitungsparameter-konfigurieren %}.

Dieser Artikel erklärt, wie du die verschiedenen Jobtypen im JobManager konfigurierst.

<style>
table {
  width: 100%;
}

table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

## Reports erstellen

<!-- {{ 1 | image: 'Sending Job Manager Report via Email', '50%' }} -->

| Parameter       | Beschreibung                                                                              |
| --------------- | ----------------------------------------------------------------------------------------- |
| cmd             | Interner Reportname                                                                       |
| p               | Kennung der Planungseinheit                                                               |
| e               | Mitarbeiter<br>Werte: alle, einzelne Kennungen durch Bindestrich (-) voneinander getrennt |
| c               | Verträge<br>Werte: alle, einzelne Kennungen durch Bindestrich (-) voneinander getrennt    |
| se              | Auswahlen<br>Werte: alle, einzelne Kennungen durch Bindestrich (-) voneinander getrennt   |
| level           | [Ebenenkennung](#ebenenkennung)                                                           |
| lid             | [Sprachkennung](#sprachkennung)                                                           |
| targethtml      | Ausgabeformat<br>Werte: 0 (PDF), 1 (HTML)                                                 |
| targetanonymous | Standard-Reports oder anonymisierte Reports<br>Werte: 0 (Standard), 1 (Anonymisiert)      |
| jobnameid       | (Optional) Interne Kennung für den Report, die leer sein kann                             |

Alle Reports, die du mit dem JobManager automatisierst, benötigen den cmd-Parameter. Klappe die einzelnen Punkte der folgenden Liste aus, um zu sehen, welchen Wert du dem cmd-Parameter für jeden Reporttyp zuweisen musst:

<details style="padding-bottom: 20px;">
<summary><strong>Wöchentliche Reports zum Schichtplan</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Wochenplan I</td>
    <td>shiftplan</td>
  </tr>
  <tr>
    <td>Wochenplan I mit Filter</td>
    <td>shiftplan showconsel=1</td>
  </tr>
  <tr>
    <td>Wochenplan I (ohne Ganztagsaktivitäten)</td>
    <td>shiftplansel hidefda=1</td>
  </tr>
  <tr>
    <td>Wochenplan II (ohne Ganztagsaktivitäten)</td>
    <td>shiftplansel showbreaks=1 hidefda=1</td>
  </tr>
  <tr>
    <td>Wochenplan II (ohne Pausen) (nur für On-premise)</td>
    <td>shiftplansel</td>
  </tr>
  <tr>
    <td>Wochenplan (ohne Pausen) (ohne Ganztagsaktivitäten)</td>
    <td>shiftplansel hidefda=1</td>
  </tr>
  <tr>
    <td>Wochenplan III</td>
    <td>weeklyworkplan</td>
  </tr>
  <tr>
    <td>Wochenplan III (ohne Ganztagsaktivitäten)</td>
    <td>weeklyworkplan hidefda=1</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Tägliche Reports zum Schichtplan</strong>
</summary>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Tagesplan I</td>
    <td>staffworkpubar</td>
  </tr>
  <tr>
    <td>Tagesplan I mit Pausen</td>
    <td>staffworkpubarbreaks</td>
  </tr>
  <tr>
    <td>Tagesplan I (ohne Abwesenheiten, Krankheiten und Urlaub)</td>
    <td>staffworkpubarabsences</td>
  </tr>
  <tr>
    <td>Tagesplan II</td>
    <td>staffworktimebar</td>
  </tr>
  <tr>
    <td>Tagesplan II mit Pausen</td>
    <td>staffworktimebarbreaks</td>
  </tr>
  <tr>
    <td>Tagesplan II mit Schichtzusammenfassung</td>
    <td>staffworktimebartotal</td>
  </tr>
  <tr>
    <td>Tagesplan II mit Schichtzusammenfassung und mit Pausen</td>
    <td>staffworktimebartotalbreaks</td>
  </tr>
  <tr>
    <td>Tagesplan III</td>
    <td>stafffworkactbar</td>
  </tr>
  <tr>
    <td>Tagesplan III mit Pausen</td>
    <td>staffworkactbarbreaks</td>
  </tr>
  <tr>
    <td>Tagesplan IV</td>
    <td>staffworkpubarsel</td>
  </tr>
  <tr>
    <td>Tagesplan V</td>
    <td>staffworktimebarsel</td>
  </tr>
  <tr>
    <td>Tagesplan VI</td>
    <td>staffworkactbarsel</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Urlaubs- und Abwesenheitspläne</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Abwesenheitsplan</td>
    <td>absence</td>
  </tr>
  <tr>
    <td>Allgemeiner Abwesenheitsplan</td>
    <td>realabsence</td>
  </tr>
  <tr>
    <td>Abwesenheitsplan mit Tagesstatus und Ganztagsaktivitäten</td>
    <td>orgabscalendar</td>
  </tr>
  <tr>
    <td>Urlaubsplan I</td>
    <td>holiday</td>
  </tr>
  <tr>
    <td>Urlaubsplan I mit Vollzeitäquivalent</td>
    <td>vacation_fte</td>
  </tr>
  <tr>
    <td>Urlaubsplan II</td>
    <td>staffworktimebartotal</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Abwesenheits-, Krankheits- und Urlaubsstatistiken</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Abwesenheitsstatistik</td>
    <td>absence_c</td>
  </tr>
  <tr>
    <td>Abwesenheitsstatistik mit Summenspalte</td>
    <td>absence_t</td>
  </tr>
  <tr>
    <td>Abwesenheitsstatistik mit Vollzeitäquivalent</td>
    <td>absence_fte</td>
  </tr>
  <tr>
    <td>Urlaubsstatistik</td>
    <td>holiday_c</td>
  </tr>
  <tr>
    <td>Urlaubsstatistik mit Summenspalte</td>
    <td>holiday_t</td>
  </tr>
  <tr>
    <td>Urlaubsstatistik mit Vollzeitäquivalent</td>
    <td>holiday_fte</td>
  </tr>
  <tr>
    <td>Krankheitsstatistik</td>
    <td>illness_c</td>
  </tr>
  <tr>
    <td>Krankheitsstatistik mit Summenspalte</td>
    <td>illness_t</td>
  </tr>
  <tr>
    <td>Krankheitsstatistik mit Vollzeitäquivalent</td>
    <td>illness_fte</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Reports zur Arbeitszeit</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Arbeitszeiten pro Planungseinheit</td>
    <td>diff_pu</td>
  </tr>
  <tr>
    <td>Aktivitäten in Stunden</td>
    <td>activ_st</td>
  </tr>
  <tr>
    <td>Aktivitäten in Prozent</td>
    <td>aktiv_per</td>
  </tr>
  <tr>
    <td>Aktivitätsstatistik</td>
    <td>activity_stat</td>
  </tr>
  <tr>
    <td>Nettoarbeitszeit (nur für On-premise)</td>
    <td>realized_hours</td>
  </tr>
  <tr>
    <td>Aktivitätsanalyse</td>
    <td>state_train</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Pausenpläne</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Pausenplan I</td>
    <td>pause</td>
  </tr>
  <tr>
    <td>Pausenplan II</td>
    <td>pausetwo</td>
  </tr>
  <tr>
    <td>Pausenplan III</td>
    <td>pausethree</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Weitere Reports</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Arbeitszeitdifferenz zwischen Ebenen</td>
    <td>worktimes</td>
  </tr>
  <tr>
    <td>Zeitkontenreport</td>
    <td>timeacount</td>
  </tr>
  <tr>
    <td>Schichten mit Bedarf</td>
    <td>genshifts</td>
  </tr>
  <tr>
    <td>Tage mit Nacht-, Wochenend- und Feiertagsarbeit (nur für On-premise)</td>
    <td>shifttype</td>
  </tr>
  <tr>
    <td>Kapazitäten nach Vertragsart</td>
    <td>capacity</td>
  </tr>
  <tr>
    <td>Trainingsmodelle (nur für On-premise)</td>
    <td>train_camp_summary</td>
  </tr>
  <tr>
    <td>Mindestbesetzung (nur für On-premise)</td>
    <td>minimalcoverage</td>
  </tr>
  <tr>
    <td>Einstellungen der Planungsregeln</td>
    <td>schedulingrules</td>
  </tr>
  <tr>
    <td>Urlaubsübersicht</td>
    <td>vacationoverview</td>
  </tr>
  <tr>
    <td>Schichtübersicht</td>
    <td>monthlyshiftplan</td>
  </tr>
  <tr>
    <td>Jährliche Arbeitszeitanalyse</td>
    <td>work_time_analysis</td>
  </tr>
  <tr>
    <td>Planeinhaltung (Arbeitszeit)</td>
    <td>conformance</td>
  </tr>
  <tr>
    <td>Planeinhaltung (Aktivität)</td>
    <td>adherence</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Reports zu Tauschaktionen</strong>
</summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Tauschaktionen I (nur für On-premise)</td>
    <td>shiftexchdetails</td>
  </tr>
  <tr>
    <td>Tauschaktionen II (nur für On-premise)</td>
    <td>shiftexchnodetails</td>
  </tr>
  <tr>
    <td>Tauschstatistik (nur für On-premise)</td>
    <td>shiftexchstats</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Mitarbeiterarbeitspläne</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Mitarbeiterarbeitsplan I (Liste)</td>
    <td>staffwork showbreaks=1</td>
  </tr>
  <tr>
    <td>Mitarbeiterarbeitsplan I (Liste) (ohne Pausen)</td>
    <td>staffwork</td>
  </tr>
  <tr>
    <td>Mitarbeiterarbeitsplan II (Liste)</td>
    <td>staffworkabsill</td>
  </tr>
  <tr>
    <td>Mitarbeiterarbeitsplan III (Grafik)</td>
    <td>staffworkbar</td>
  </tr>  
  <tr>
    <td>Mitarbeiterarbeitsplan IV (6 Wochen)</td>
    <td>staffsixweeksnobreaks</td>
  </tr>  
  <tr>
    <td>Mitarbeiterarbeitsplan IV (6 Wochen) (Aktivitäten)</td>
    <td>staffsixweeks</td>
  </tr>
  <tr>
    <td>Mitarbeiterarbeitsplan IV (6 Wochen) (ohne Pausen)</td>
    <td>staffsixweekstwo</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 40px;">
<summary><strong>Weitere Mitarbeiterreports</strong></summary>
<br>
<table>
  <thead>
    <tr>
      <th>Reportname</th>
      <th>Wert für cmd-Parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Mitarbeiterwunschplan I (Liste) (nur für On-premise)</td>
    <td>staff_wish</td>
  </tr>
  <tr>
    <td>Arbeitszeiten je Mitarbeiter I</td>
    <td>diff_st</td>
  </tr>
  <tr>
    <td>Arbeitszeiten je Mitarbeiter II</td>
    <td>diff_st_two</td>
  </tr>
  <tr>
    <td>Monatsjournal Mitarbeiter (nur für On-premise)</td>
    <td>journal</td>
  </tr>
  <tr>
    <td>Organigramm</td>
    <td>organ</td>
  </tr>
  <tr>
    <td>Wochenendarbeitsreport I</td>
    <td>weekendwork</td>
  </tr>
  <tr>
    <td>Wochenendarbeitsreport II</td>
    <td>weekendwork2</td>
  </tr>
  <tr>
    <td>Wochenendarbeitsreport III (Verlosung und Zuteilung) (nur für On-premise)</td>
    <td>weekendwork3</td>
  </tr>
  <tr>
    <td>Jubiläumsreport</td>
    <td>jubilee</td>
  </tr>
  <tr>
    <td>Urlaubsschein (nur für On-premise)</td>
    <td>hd_list</td>
  </tr>
  <tr>
    <td>Mitarbeiter pro Vertragsart</td>
    <td>read</td>
  </tr>
  <tr>
    <td>Fluktuationsreport I</td>
    <td>fluct</td>
  </tr>
  <tr>
    <td>Fluktuationsreport II</td>
    <td>detailfluctuation</td>
  </tr>
  <tr>
    <td>Jahresübersicht (nur für On-premise)</td>
    <td>absencejob_cal</td>
  </tr>
  <tr>
    <td>Ausgleichstage für Wochenendarbeit (nur für On-premise)</td>
    <td>comp_week_work</td>
  </tr>
  <tr>
    <td>Mitarbeiterschichtfolgen</td>
    <td>staffshiftseq</td>
  </tr>
  <tr>
    <td>Arbeitszeitplan (nur für On-premise)</td>
    <td>monthly_work_sched</td>
  </tr>
  <tr>
    <td>Arbeitsplatz (nur für On-premise)</td>
    <td>assignedworkplaces</td>
  </tr>
  <tr>
    <td>Feiertagsarbeit (Verlosung und Zuteilung)</td>
    <td>laaholidaywork</td>
  </tr>
  <tr>
    <td>Mindestbelegung nach Standort (nur für On-premise)</td>
    <td>deskminstaffing</td>
  </tr>
  <tr>
    <td>Arbeitsplatzbelegung (nur für On-premise)</td>
    <td>deskalloc</td>
  </tr>
  <tr>
    <td>Stammdatengültigkeit (nur für On-premise)</td>
    <td>masterdatavalidity</td>
  </tr>
  <tr>
    <td>Coach/Trainee - Plandifferenz (nur für On-premise)</td>
    <td>coach_trainee</td>
  </tr>
  <tr>
    <td>Stammdatenübersicht</td>
    <td>employeemasterdata</td>
  </tr>
  <tr>
    <td>Benutzergruppenrechte (nur für On-premise)</td>
    <td>group_auth</td>
  </tr>
  <tr>
    <td>Stammdatenänderungen</td>
    <td>audit</td>
  </tr>
</table>
</details>

## Schichtfolgen einfügen

<!-- {{ 2 | image: 'Insert Shift Sequences', '50%' }} -->

| Parameter    | Beschreibung                                                                                                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delete1      | Ganztägige Aktivitäten löschen<br>Werte: 1 (ja), 0 (nein)                                                                                                                         |
| delete2      | Verfügbarkeitsrahmen löschen<br>Werte: 1 (ja), 0 (nein)                                                                                                                           |
| delete3      | Alle Aktivitäten und Schichten löschen<br>Werte: 1 (ja), 0 (nein)                                                                                                                 |
| level_id     | [Ebenenkennung](#ebenenkennung)                                                                                                                                                   |
| lid          | [Sprachkennung](#sprachkennung)                                                                                                                                                   |
| nr_of_seq    | Anzahl der Mitarbeiter mit Schichtfolgen<br>Wert: alle                                                                                                                            |
| option       | Interne Kennung<br>Wert: 2                                                                                                                                                        |
| planunit_id  | Kennung der Planungseinheit                                                                                                                                                       |
| selection_id | Auswahlen<br>Werte: -1 (alle Auswahlen), einzelne Kennungen durch Bindestrich voneinander (-) getrennt                                                                            |
| shiftseq_id  | Kennungen der Schichtfolgen, die den ausgewählten Mitarbeitern zugewiesen wurden und durch Bindestrich (-) voneinander getrennt sind. Erforderlich, außer der Typ ist festgelegt. |
| type         | (Optional) Wählt alle Schichtfolgen für die ausgewählten Mitarbeiter aus. Wenn dieser Parameter verwendet wird, kann der Parameter shiftseq_id leer bleiben.<br>Wert: alle        |

### Verlosung und Zuteilung

<!-- {{ 3 | image: 'Lottery or Assignment', '50%' }} -->

| Parameter   | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| doreporting | Log-Datei<br>Werte: 1 (ja), 0 (nein)                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| e           | Mitarbeiter<br>Werte: alle, einzelne Kennungen durch Bindestrich (-) voneinander getrennt                                                                                                                                                                                                                                                                                                                                                                                                                |
| lid         | [Sprachkennung](#sprachkennung)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| modelcase   | Interne Kennung<br>Werte: 10 (Schichtzuteilung), 11 (Schichtverlosung)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| observecorr | Toleranzwert für die Startzeit beachten<br>Werte: 0 (nein), 1 (ja)                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| periodid    | Kennung für die Planperiode oder mehrere Kennungen, die durch Komma voneinander getrennt sind. Du kannst die korrekte Kennung für die Planperiode mit den Entwicklertools im Quellcode der Seite finden (erster Teil des Wertes im Element data-flip-id) oder mit der [API](https://legacy-api.injixo.com/#tag/Planning-Periods/operation/getV1PlanningPeriodsStartDate). Wenn im Abschnitt Jobverarbeitungszeitraum der Wert Relativ ausgewählt ist, wird nur die relevante Planperiode berücksichtigt. |
| puid        | Kennung der Planungseinheit                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| staffcount  | Anzahl der Mitarbeiter. Dies ist ein Pflichtparameter, der eingegebene Wert wird aber immer ignoriert. Du kannst jeden Wert eingeben.                                                                                                                                                                                                                                                                                                                                                                    |
| tolerance   | Maximale Abweichung von der durchschnittlichen Startzeit<br>Wert: Zeit im Format HH:MM, 00:00 (wenn der Wert für den observecorr-Parameter 0 ist)                                                                                                                                                                                                                                                                                                                                                        |

### Ebene kopieren

Die Funktionalität **Ebeneninhalte kopieren** findest du unter _Plan > Schedules > Planungsaktionen_{:.breadcrumbs}.

| Parameter     | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| copystartdate | Startdatum zum Einfügen von Daten im [Julianischen Datumsformat](https://www.onlineconversion.com/julian_date.htm). Daten werden verschoben, wenn das Datum nicht dem Startdatum der Planperiode entspricht.                                                                                                                                                                                                                                                                                             |
| deletesource  | Quellebene löschen<br>Werte: 0 (Quellebene kopieren), 1 (Quellebene löschen)                                                                                                                                                                                                                                                                                                                                                                                                                             |
| lid           | [Sprachkennung](#sprachkennung)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| e             | Mitarbeiter<br>Werte: alle, einzelne Kennungen durch Bindestrich (-) voneinander getrennt                                                                                                                                                                                                                                                                                                                                                                                                                |
| modelcase     | Interne Kennung<br>Werte: 15 (Ebene kopieren), 16 (Ebene löschen)                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| periodid      | Kennung für die Planperiode oder mehrere Kennungen, die durch Komma voneinander getrennt sind. Du kannst die korrekte Kennung für die Planperiode mit den Entwicklertools im Quellcode der Seite finden (erster Teil des Wertes im Element data-flip-id) oder mit der [API](https://legacy-api.injixo.com/#tag/Planning-Periods/operation/getV1PlanningPeriodsStartDate). Wenn im Abschnitt Jobverarbeitungszeitraum der Wert Relativ ausgewählt ist, wird nur die relevante Planperiode berücksichtigt. |
| puid          | Kennung der Planungseinheit. Kann nach Kennung gefiltert werden, wenn ein Trennzeichen (-) verwendet wird.                                                                                                                                                                                                                                                                                                                                                                                               |
| sourcelevel   | [Ebenenkennung](#ebenenkennung) (Quelle)                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| targetlevel   | [Ebenenkennung](#ebenenkennung) (Ziel)                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| staffcount    | Erforderlich, aber nicht verwendet. Gib den Wert 0 ein.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| selectionid   | Kennung für die Auswahl<br>Werte: -1 (alle Auswahlen), einzelne Kennungen durch Bindestrich voneinander (-) getrennt                                                                                                                                                                                                                                                                                                                                                                                     |

## E-Mail-Parameter

E-Mail-Parameter sind optional. Wenn keine E-Mail-Parameter konfiguriert sind, kannst du Reports nur im JobProcessor verwenden.

| Parameter  | Beschreibung                                                                                                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| em         | Kennung für die Mitarbeiter<br>Werte: -1 (alle), einzelne Kennungen durch Bindestrich voneinander (-) getrennt                                                                                                                                                |
| sendtoall  | Sende eine E-Mail an alle ausgewählten Mitarbeiter gleichzeitig.<br>Werte: 1 (ja), 0 (nein)                                                                                                                                                                   |
| sendperemp | Sende eine einzelne E-Mail an den ausgewählten Mitarbeiter. Nicht für alle Reports verfügbar. <br>Werte: 1 (ja), 0 (nein)                                                                                                                                     |
| email      | E-Mail-Adresse des Empfängers. Mehrere E-Mail-Empfänger werden nicht unterstützt. Falls nötig, nutze einen E-Mail-Verteiler, der intern auf mehrere Empfänger weiterleitet. Der Parameter email wird nicht verwendet, wenn der Parameter em Kennungen angibt. |
| emailtype  | E-Mail-Adresse des Mitarbeiters<br>Werte: 1 (E-Mail 1), 3 (E-Mail 2), 2 (beide). Die injixo Cloud-Versionen unterstützen E-Mail 2 nicht.                                                                                                                      |
| comments   | Optionaler Text für die E-Mail-Nachricht                                                                                                                                                                                                                      |

## Sprachkennung

Der Parameter **lid** definiert die Sprachkennung für den erzeugten Report und unterstützt die folgenden Kennungen:

Englisch (USA) (1033)<br>
Deutsch (1031)<br>
Französisch (1036)<br>
Italienisch (1040)<br>
Spanisch modern (3082)<br>
Spanisch Standard (1034)<br>
Niederländisch (1043)<br>
Schwedisch (1053)<br>
Englisch UK (2057)<br>
Polnisch (1045)

## Ebenenkennung

Der Parameter **level** legt die Ebene fest, von der Daten gelesen werden, und unterstützt die folgenden Kennungen:

1000 (Plan)<br>
3000 (aktueller Status)<br>
5000 (externes System)<br>
4000 (Zeiterfassung)<br>
2000 (Anfrage)<br>
2001 (Ausweichwunsch)<br>
2002 (Urlaubs-/Abwesenheitsantrag)<br>
6000 (Verfügbarkeit)<br>
6001 (Bereitschaftsdienst)<br>
4001 (Korrektur)<br>
8000 (Version 1)<br>
8001 (Version 2)<br>
8002 (Version 3)
