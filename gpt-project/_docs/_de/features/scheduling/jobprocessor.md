---
title: JobProcessor
---

Der Menüpunkt JobProcessor ermöglicht Dir einen Überblick über alle Jobs, die in den verschiedenen Programmteilen von injixo gestartet werden können. Hierbei hast Du die Möglichkeit, laufende Jobs zu verfolgen sowie abgeschlossene Jobs einzusehen und Berichte zu diesen aufzurufen.

Dabei führt der JobProcessor nicht-zeitkritische Aktionen im Hintergrund aus und übernimmt hierbei die Steuerung bestimmter Funktionen in den folgenden Modulen:

  - Reports/TimeManager
    - Reports
  - SchedulePro
    - Planperioden, Planungsaktionen
    - Verlosung
    - Zuteilung
    - Austauschen von Aktivitäten
    - Kopieren von Plandaten
    - Löschen von Plandaten
    - Berechnen von Richtzeitkonten
    - Coach/Trainee-Aktionen
    - Einfügen von Schichtfolgen
  - Administration
    - Massenbearbeitung

Der JobProcessor kombiniert Aktionen als Jobtypen: Du kannst das Programm anweisen, diese Jobtypen an verschiedenen Typen über die Einstellungen des Systems zu verarbeiten. Jede einzelne Aktion, wie z.B. das Erstellen von Reports, ist ein Job, den der JobProcessor übernimmt.

Du kannst diese Jobs im Menüpunkt JobProcessor verwalten und in den aktuellen Vorgang eingreifen. Zum Übergeben von Aufgaben an den JobProcessor verwendest Du die betreffenden Module oder Menüpunkte. Nachdem Du den Parameter für die Aktion bestätigt hast, öffnet das System den Dialog zur Jobverarbeitung mit Informationen über den Auftrag und seinen aktuellen Verarbeitungsstatus. Die Einstellungen des Auftrags legen fest, wann er gestartet wird und ob Benutzer ihn überschreiben können oder nicht.

## Jobverarbeitung

Rufe die Aktion oder den Report im entsprechenden Menüpunkt auf. Je nach Jobtyp öffnet sich zunächst ein Parameterdialog zur Abfrage der erforderlichen Aktionsdaten, z.B. des Zeitraums, der Planungseinheit, der Auswahl, des Mitarbeiters, der Ebene usw. Mit der Bestätigung der Angaben erscheint der Startdialog der Jobverarbeitung.

Der Dialog zeigt den Status der Jobverarbeitung, den Job sowie eine Beschreibung der Aktion. *Abbrechen*{:.doc-button} schließt den Dialog, ohne den Job abzuschicken. *Job abschicken*{:.doc-button} schickt den Job zur Verarbeitung ab.

Die erste Zeile im Dialog zeigt den Verarbeitungsstand entsprechend dem Jobstatus an. Die Zahl in Klammern nennt die Verarbeitungsposition des Jobs. Sie verringert sich mit jedem abgearbeiteten Job. Nach dem Status `Job abgeschickt` erscheint im Dialog noch `Jobverarbeitung startet` und während der Verarbeitung `Jobverarbeitung läuft`.

Der Dialog für die Jobverarbeitung bleibt geöffnet, sodass Du den Verarbeitungsfortschritt verfolgen kannst. Damit ist es jederzeit möglich, Änderungen im Kontrollkästchen `Jobergebnis nach Abschluss anzeigen` vorzunehmen. Es ist außerdem jederzeit möglich, die Verarbeitung abzubrechen. *Job abbrechen*{:.doc-button} versetzt den Job in den Status `Abgebrochen`. Er kann später im Menüpunkt *JobProcessor*{:.menu-item} erneut zur Verarbeitung abgeschickt werden. Nach Abschluss der Verarbeitung schließt sich der Dialog. Das Ergebnis wird von selbst eingeblendet, falls Du die entsprechende Option ausgewählt hast. Es erscheint das Fenster mit dem Verarbeitungsergebnis (Report) oder dem Ergebnisbericht. Andernfalls kannst Du das Ergebnis manuell über die Jobübersicht aufrufen.

> Hinweis
>
> Achtung: Durch einen Klick auf *Job abbrechen*{:.doc-button} wird nicht verhindert, dass die Schichtfolge im *Schicht Center*{:.menu-item} eingefügt wird.

Wenn Du den Dialog nach dem Abschicken des Jobs schließt, wird die Verarbeitung entsprechend den Angaben fortgesetzt. Die Ergebnisse lassen sich später in der Jobübersicht abrufen.

> Hinweis
>
> Solltest Du im Menüpunkt *Reports*{:.menu-item} unter Parameter `Empfänger` die Option `Report als E-Mail verschicken an` ausgewählt haben, wird der Report nur an diese Empfänger verschickt. Der Auftraggeber des Jobs bekommt nach Abschluss der Verarbeitung nur den Ergebnisbericht, den er auch in der Jobübersicht abrufen kann. Um den Report selbst zu erhalten, kann er den Job in der Jobübersicht erneut abschicken. Bei der zweiten Verarbeitung erfolgt kein E-Mail-Versand an die Empfänger. Der Report ist über *Ergebnis anzeigen*{:.doc-button} aufrufbar.

## Jobübersicht

Öffne den *JobProcessor*{:.menu-item} im Navigator, um Informationen zu Jobs zu erhalten, zu löschen, abzubrechen oder erneut abzuschicken.

Die Jobübersicht gibt Auskunft über den Status, die Anzahl und die Reihenfolge der abgeschickten Jobs sowie über deren wichtigste Metadaten. Sie lässt sich über ein Auswahlfeld in der Aktionsleiste nach Statusgruppen filtern, sodass entweder alle, nur verarbeitete oder nur unverarbeitete Jobs eingeblendet werden. Ein weiterer Filter lässt auch die Anzeige von Jobs zu, die andere Benutzer angelegt haben.

Die Aktionsleiste informiert Dich, ob der JobProcessor zum aktuellen Zeitpunkt gestartet oder gestoppt ist.

> Hinweis
>
> Die angezeigten Jobs und Bearbeitungsmöglichkeiten sind abhängig von der Rolle des angemeldeten Benutzers sowie von den Rechten seiner Rolle.

Die Übersicht enthält die nachstehend erläuterten Angaben.

| Menüpunkt | Beschreibung
| ------- | ------- |
| Kontrollkästchen | Mit Hilfe dieser Kontrollkästchen lassen sich alle oder einzelne Jobs für eine Funktion auswählen (*Löschen*{:.doc-button}, *Abbrechen*{:.doc-button} oder *Job erneut abschicken*{:.doc-button}). Die Statuszeile gibt neben der Gesamtzahl der Jobs auch die Anzahl der ausgewählten Jobs an. |
| Status | Die Spalte gibt Auskunft über den Verarbeitungsstatus. |
| Ergebnis | Die Spalte enthält für fertig gestellte Jobs ein Symbol zum Aufruf der Ergebnisse der Jobverarbeitung. |
| Typ | In dieser Spalte erscheint der Jobtyp. |
| Benutzer | Die Spalte nennt den Benutzer, der den Job angelegt hat |.
| Abgeschickt | Die Spalte enthält den Zeitpunkt, zu dem der Job abgeschickt wurde. |
| Wartezeit | Die Angabe bezieht sich auf die Zeit, die zwischen dem Abschicken des Jobs bis zur Verarbeitung vergangen ist. |
| Verarbeitungsdauer | Die Spalte gibt die Dauer vom Start bis zum Abschluss der Verarbeitung an. |
| Beendet | Die Spalte nennt den Zeitpunkt, ab dem sich der Job nicht mehr in der Verarbeitung befindet. Es kann entweder der Zeitpunkt des erfolgreichen Fertigstellung oder des Abbruchs sein. |
| Gelesen | In dieser Spalte erscheint der Zeitpunkt, zu dem das Ergebnis der Jobverarbeitung in der Spalte `Ergebnis` erstmalig aufgerufen wurde. |
| Ausgeführt auf | Die Spalte gibt den Namen des Rechners an, auf dem die Jobverarbeitung stattgefunden hat. |
| E-Mail | Die Spalte zeigt an, ob das Ergebnis per E-Mail versendet werden soll bzw. ob der Versand erfolgreich war oder nicht. |
| ID | Die Spalte nennt eine intern vergebene Identifikationsnummer für den Job. |

## Bearbeitungsmaske Jobdetails

Die Bearbeitungsmaske eines Jobs öffnet sich, wenn Du in der Übersicht in eine Jobzeile klicken. Der Job wird farbig hervorgehoben.

In den Bearbeitungskategorien erscheinen Detailinformationen zum Job. Die Bearbeitungskategorie `Allgemein` enthält z.B. Angaben zum Jobtyp, zur ID, zum Anleger und zur Startzeit sowie im Feld `Beschreibung` die wichtigsten Parameter des Jobs. Die Bearbeitungskategorie Jobstatus zeigt neben dem Status die einzelnen Phasen der Jobverarbeitung an. Die Informationen erleichtern die Entscheidung, ob Du einen Job in der Übersicht löschen, abbrechen oder erneut abschicken möchtest.

## Funktionen in der Jobübersicht

Im Menüpunkt JobProcessor sind nachstehend erläuterte Operationen über die Aktionsleiste möglich, in Abhängigkeit von den Rollen des Benutzers.

## Aktualisieren der Übersicht

Die Jobübersicht öffnet sich jeweils mit den aktuellsten Verarbeitungsständen. Danach erfolgt keine selbständige Aktualisierung. Erneuere deshalb vor jeder Aktion die Anzeige. Die Funktion *Jobübersicht aktualisieren*{:.doc-button} nimmt hinzugekommene Jobs und Änderungen des Verarbeitungsstandes auf.

## Abbrechen von Jobs

Die Funktion *Job abbrechen*{:.doc-button} setzt die Verarbeitung von Jobs mit den Status `Abgeschickt` und `Läuft` aus. Sie versetzt alle Jobs mit den genannten Status und aktiviertem Kontrollkästchen in den Status `Abgebrochen`. Du kannst später über den Button *Job erneut abschicken*{:.doc-button} diesen Job wieder abschicken.

## Jobs erneut abschicken

Die Funktion *Job erneut abschicken*{:.doc-button} schickt aktivierte Jobs mit dem Status `Abgebrochen` und `Fertig` erneut zur Verarbeitung ab. Dadurch brauchst Du Jobs, die Du wiederholen möchtest, nur einmal anzulegen. Lasse dazu einen mehrmals benötigten Job nach der Verarbeitung einfach in der Übersicht stehen.
Sobald sich jedoch Ausführungsparameter für den Job ändern, z.B. der Zeitraum, ist der Job neu anzulegen.

## Löschen von Jobs

Die Funktion *Job löschen*{:.doc-button} dient der Bereinigung. Aktiviere dazu das Kontrollkästchen vor nicht mehr benötigten Jobs, um sie anschließend aus der Übersicht zu entfernen. Es können alle Jobs gelöscht werden, die sich nicht gerade im Status `Läuft` befinden.
