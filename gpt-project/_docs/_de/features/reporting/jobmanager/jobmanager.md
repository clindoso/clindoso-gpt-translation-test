---
title: JobManager
product_label:
  - enterprise
description: Konfiguriere regelmäßige Jobs, z.B. zur automatischen Erstellung von Reports.
promote-service: enhanced-reporting
---

Der *JobManager*{:.menu-item} in *Administration > System > JobManager*{:.breadcrumbs} erlaubt Benutzern mit *Admin-Zugriff* wiederkehrende Jobs zu konfigurieren. Diese Jobs können auch mit den Rechten bestimmter Benutzer laufen. Aktivierte Vorlagen werden vom JobProcessor zum festgelegten Zeitpunkt ausgeführt.

Es stehen diverse Jobtypen zur Verfügung, z.B.:
- Schichtfolgen einfügen
- Reports erstellen
- Verlosung/Zuteilung
- Richtzeitkonten berechnen

## Erstellen von Vorlagen

1. Wähle einen **Namen**.
2. Setze das Häkchen **Aktiv**, um die Jobausführung zu aktivieren.
3. Definiere den **Jobtyp**.
4. Gib einen Wert zwischen 1 und 10 für die **Priorität** an. 1 entspricht der höchsten Priorität.
5. Wähle den **Benutzer** aus, mit dem der Job ausgeführt wird. Der Benutzer benötigt ausreichende Benutzerrechte.

Nach dem Speichern der Vorlage musst Du den Jobverarbeitungszeitraum, die -parameter, die -termine und die -optionen zuweisen. Bestehende Vorlagen können jederzeit bearbeitet werden. Jobverarbeitungsvorlagen können über einen Button in der Aktionsleiste manuell gestartet werden; das ist z.B. nützlich zum Testen von deaktivierten Vorlagen.

{{ 1 | image: "Job Konfiguration", '50%' }}

### Jobverarbeitungszeitraum

Der Jobverarbeitungszeitraum legt fest, für welchen Zeitraum der Job ausgeführt werden soll.

1. Definiere die **Art der Zeitangabe**, wähle
  - *Absolut* für absolute Zeiträume
  - *Relativ* für variable Zeiträume

2. Gib einen **Bezugswert vom/bis** ein.  
  Wähle einen vordefinierten Zeitraum über einen der Links aus, z.B. **letzte Woche**.  
  Stelle andere Zeiträume selbst ein, z.B. letztes Jahr oder gestern (Bezugswert vom/bis jeweils *-1* und Tag).

Parameter für den Jobverarbeitungszeitraum werden automatisch in der Kategorie Jobverarbeitungsparameter hinzugefügt.

## Jobverarbeitungsparameter

In dieser Sektion musst Du manuell jobspezifische Parameter über das {% icon item-add %} hinzufügen.

> Details zu den jobspezifischen Parametern findest Du in den {% link_new JobManager-Beispielen | features/reporting/jobmanager/jobmanager-examples.md %}.

Einige Jobverarbeitungsparameter wie die Sprache und die Quellebene sind für alle Jobs gleich.

### Verfügbare Sprachen

Der Parameter **lid** (kurz für language id) wird bei allen Jobtypen mitgesendet und definiert die Sprache, in der ein Report erstellt wird. Verfügbare Sprachen sind:
- 1033 (Englisch US)
- 2057 (Englisch UK)
- 1031 (Deutsch)
- 1036 (Französisch)
- 1040 (Italienisch)
- 1043 (Niederländisch)
- 3082 (Spanisch modern)
- 1034 (Spanisch)
- 1053 (Schwedisch)
- 1045 (Polnisch)

### Ebene

Der Parameter **level** definiert die Ebene, aus welcher die Daten gelesen bzw. in welche diese geschrieben werden. Folgende Ebenen werden unterstützt:
- 1000 (Plan)
- 3000 (Aktueller Stand)
- 5000 (Externes System)
- 4000 (Zeiterfassung)
- 2000 (Wunsch)
- 2001 (Ausweichwunsch)
- 2002 (Urlaubs-/Abwesenheitswunsch)
- 6000 (Verfügbarkeit)
- 6001 (Rufbereitschaft)
- 4001 (Korrektur)
- 8000 (Version 1)
- 8001 (Version 2)
- 8002 (Version 3)

### Jobverarbeitungstermine

Jobverarbeitungstermine legen fest, an welchen Tagen und zu welcher Uhrzeit die Vorlage gestartet und der Job abgeschickt werden soll. Du kannst mehrere Verarbeitungstermine hinterlegen.

Es stehen Dir die Optionen zur Verfügung:  
- Wochentag (Montag - Sonntag)
- Monatstag (1 - 31)
  Diese erwartet ein Datum, das auch im Verarbeitungszeitraum vorkommt. So wird z.B. ein Job, der jeweils für den 30. eines Monats geplant ist, im Februar nicht ausgeführt.  
- Monatsletzter

Lösche oder editiere gespeicherte Termine nachträglich über _![x button](/assets/img/common/item-edit.gif)_{:.doc-button-icon} bzw. _![x button](/assets/img/common/item-delete.gif)_{:.doc-button-icon} in der Liste der Termine.

### Jobverarbeitungsoptionen

Konfiguriere eine automatische Mitteilung nach der Fertigstellung eines Jobs oder lass Dir das Ergebnis direkt im Anhang zusenden (sinnvoll bei Reports). Beides ist nur für Benutzer möglich, die auch Mitarbeiter zugeordnet haben.
