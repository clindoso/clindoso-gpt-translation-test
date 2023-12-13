---
title: JobManager Beispiele
product_label:
  - enterprise
---

In diesem Artikel findest Du Beispiele für unterschiedliche Jobtypen, die Du mit dem JobManager automatisieren kannst.

### Report per E-Mail versenden

{{ 1 | image: 'JobManager Report per E-Mail versenden', '65%' }}

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

Parameter | Bedeutung
------- | -------
**cmd** | Interner Name des Reports, *absolutes Pflichtfeld*, siehe {% link_new Namen | features/reporting/jobmanager/jobmanager-reportnames.md %}.
**p** | ID der Planungseinheit.
**e** | Mitarbeiter, all für alle oder IDs mit Trennzeichen (-).
**c** | Verträge, all für alle oder IDs mit Trennzeichen (-).
**se** | Auswahl, all für alle oder  IDs mit Trennzeichen (-).
**level** | {% link_new ID der Ebene | features/reporting/jobmanager/jobmanager.md | #ebene %}, hier *Plan*.
**lid** | {% link_new Sprach-ID | features/reporting/jobmanager/jobmanager.md | #jobverarbeitungsparameter %}, z.&nbsp;B. 1031 für Deutsch.
**targethtml** | Ausgabe-Format, 0 für pdf, 1 für html.
**targetanonymous** | normale (0) oder anonymisierte (1) Auswertung.
**jobnameid** | ID des Reports, kein Pflichtfeld.

#### E-Mail-Parameter

Alle E-Mail-Parameter sind optional, ohne Angabe dieser Parameter liegt der Report nur im JobProcessor-Verzeichnis auf dem Server.

<style>
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

Parameter | Bedeutung
------- | -------
**em** | Ausgewählte Empfänger, Mitarbeiter-IDs mit Trennzeichen (-), -1 für alle.
**sendtoall** | Sammelemail an alle Mitarbeiter der Auswahlliste.
**sendperemp** | E-Mail an jeden Mitarbeiter persönlich, 1 oder 0, nicht für alle Reports verfügbar.
**email** | Einzelne Empfänger E-Mail-Adresse. Für mehrere E-Mail-Empfänger nutze einen E-Mail-Verteiler, der intern auf mehrere Empfänger weiterleitet. Bei Angabe von IDs in **em** fällt der Parameter *email* weg.
**emailtype** | Auswahl der Mitarbeiter E-Mail-Adresse (erste - 1, zweite - 3, beide - 2).
**comments** | Optionaler Text für E-Mail-Nachricht.

### Schichtfolgen einfügen

{{ 2 | image: 'Schichtfolgen einfügen', '65%' }}

<style>
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

Parameter | Bedeutung
------- | -------
**delete1** | 1 zum Löschen von ganztägigen Aktivitäten, sonst 0.
**delete2** | 1 zum Löschen von Verfügbarkeitsrahmen, sonst 0.
**delete3** | 1 zum Löschen aller Aktivitäten und Schichten, sonst 0.
**level_id** | {% link_new ID der Ebene | features/reporting/jobmanager/jobmanager.md | #ebene %}, hier *Plan*.
**lid** | {% link_new Sprach-ID | features/reporting/jobmanager/jobmanager.md | #jobverarbeitungsparameter %}, z.&nbsp;B. 1031 für Deutsch.
**nr_of_seq** | Anzahl der Mitarbeiter mit Schichtfolgen (Pflichtparameter), Wert: all.
**option** | Pflichtparameter, der nur den Wert 2 haben kann.
**planunit_id** | ID der Planungseinheit.
**selection_id** | ID der Auswahl, 0 für alle, Mehrfachangabe möglich.
**shiftseq_id** | Interne ID der Zuordnung der Schichtfolge zum Mitarbeiter, Trennzeichen (-). Pflichtparameter, nicht notwendig, wenn type gesetzt ist.
**type** | Auswahl aller Schichtfolgen der aufgeführten Mitarbeiter, nur 'all' möglich. Optionaler Parameter. Wenn gesetzt, müssen in shiftseq_id keine IDs aufgeführt werden.

### Verlosung und Zuteilung

{{ 3 | image: 'Verlosung oder Zuteilung', '65%' }}

<style>
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

Parameter | Bedeutung
------- | -------
**doreporting** | Zum Erzeugen eines Protokolls Wert 1, sonst 0.
**e** | Mitarbeiter, all für alle oder IDs mit Trennzeichen (-).
**lid** | {% link_new Sprach-ID | features/reporting/jobmanager/jobmanager.md | #jobverarbeitungsparameter %} für Protokoll, z.&nbsp;B. 1031 für Deutsch.
**modelcase** | Interne ID des Vorgangs, 10 = Zuteilung, 11 = Verlosung.
**observecorr** | Wert 1 für die Berücksichtigung des Zeitkorridor im Verhältnis zur Startzeit. Sonst 0.
**periodid** | ID der Planperiode, Mehrfachauswahl möglich mit Trennzeichen (,). Bei relativem Zeitraum wird nur die zutreffende Planperiode berücksichtigt.
**puid** | ID der Planungseinheit.
**staffcount** | Anzahl zu verarbeitender Mitarbeiter, Pflichtwert, der ignoriert wird, aber da sein muss.
**tolerance** | 00:00 - Wert für die Abweichung vom durchschnittlichen Schichtbeginn. Pflichtparameter, der auch gesetzt werden muss, wenn observecorr = 0.

### Ebenen kopieren

{{ 4 | image: 'Ebenen kopieren', '65%' }}

<style>
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

Parameter | Bedeutung
------- | -------
**copystartdate** | Startdatum zum Einfügen der Daten aus der Quellebene (Pflichtparameter), Angabe im [julianischem Datumsformat (!)](https://www.onlineconversion.com/julian_date.htm). Muss zum Startdatum und zur Planperiode passen.
**deletesource** | Umgang mit Quellebene, 0 = Quellebene wird nicht gelöscht, 1 = Quellebene wird gelöscht.
**lid** | {% link_new Sprach-ID | features/reporting/jobmanager/jobmanager.md | #jobverarbeitungsparameter %} für Fehlermeldungen, z.B. 1031 für Deutsch.
**e** | Mitarbeiter, all für alle oder IDs mit Trennzeichen (-).
**modelcase** | Interne ID des Typs der Ebenenbearbeitung (Pflichtfeld), 15 = Ebene kopieren, 16 = Ebene löschen.
**periodid** | ID der Planperiode, Mehrfachauswahl möglich mit Trennzeichen (,). Bei relativem Zeitraum wird nur die zutreffende Planperiode berücksichtigt. 
**puid** | ID der Planungseinheit, Einschränkung über ID möglich, Liste mit Trennzeichen (-).
**sourcelevel** | {% link_new ID der Quellebene | features/reporting/jobmanager/jobmanager.md | #ebene %}, hier *Plan*.
**targetlevel** | {% link_new ID der Zielebene | features/reporting/jobmanager/jobmanager.md | #ebene %}, hier *Aktueller Stand*.
**staffcount** | Anzahl zu verarbeitender Mitarbeiter. Pflichtwert, dessen Wert aber ignoriert wird, trage hier einfach irgendeine Zahl ein.
**selectionid** | -1 für alle Auswahlen, Einschränkung über ID möglich.
**staffids** | -1 für alle Mitarbeiter, Einschränkung über ID möglich, Liste mit Trennzeichen (-).
