---
title: Schichtplan bearbeiten
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aktivitäten und Schichten im Schichtplan bearbeiten, hinzufügen und löschen (Schedules-Modul).
---

In diesem Artikel lernst Du, wie Du:

- Aktivitäten in Deinem Schichtplan mit _Plan > Schedules_{:.breadcrumbs} bearbeitest, hinzufügst und löschst.
- komplette Schichten direkt im Schichtplan kopierst, ausschneidest, einfügst und löschst.

Neu im Modul _Schedules_? Lerne zuerst {% link_new die Grundlagen | features/scheduling/schedules/schedules-overview.md %}.

## Aktivitäten hinzufügen

1. Doppelklicke auf eine **Zelle** im Schichtplan, um die Bearbeitungsansicht zu öffnen.
2. Wähle auf der linken Seite einen **Aktivitätstyp** aus (optional), um vorher festzulegen, welchen Aktivitätstyp Du hinzufügen möchtest. Standardmäßig ist _Alle_ ausgewählt.
3. Klicke auf _Neue Aktivität hinzufügen_{:.doc-button}, um eine neue Aktivität zu erstellen, oder klicke auf _Neue ganztägige Aktivität hinzufügen_{:.doc-button}, um eine neue ganztägige Aktivität zu erstellen. Auf der rechten Seite wird eine neue Zeile mit der Aktivität hinzugefügt. Multiaktivitäten werden mit dem _Symbol_{:.multiactivity-icon} gekennzeichnet, ganztägige Aktivitäten mit einem Tagesstatus mit dem _Symbol_{:.daystatus-icon}.
4. Wähle in der Zeile der neuen Aktivität eine Aktivität aus dem **Dropdown**. Wenn Du in Schritt 2 einen Aktivitätstyp ausgewählt hast, kannst Du nur Aktivitäten dieses Typs auswählen.
5. Konfiguriere die **Startzeit** und **Endzeit** für die neue Aktivität. Du kannst auch das Datum ändern, wenn die Aktivität am Vortag beginnen oder am Folgetag enden soll. Wiederhole die Schritte 2 bis 5, um weitere Aktivitäten hinzuzufügen.
6. Klicke auf _Speichern_{:.doc-button}.

   {{ 1 | image: 'Aktivitäten und Multiaktivitäten hinzufügen'}}

## Aktivitäten bearbeiten

1. Doppelklicke auf eine **Zelle**, um die Bearbeitungsansicht zu öffnen.
2. Ändere die Werte für **Aktivität**, **Startzeit** oder **Endzeit** auf der rechten Seite.
3. Klicke auf _Speichern_{:.doc-button}.

   {{ 2 | image: 'Aktivitäten bearbeiten', '80%' }}

Ein kleiner gelber Punkt neben den Tabs _Bearbeiten_ oder _Verlauf_ auf der linken Seite weist auf nicht gespeicherte Änderungen im jeweiligen Tab hin.

Manchmal kommt es vor, dass Du ungespeicherte Änderungen in beiden Tabs hast. Wenn Du jetzt die Änderungen in einem der Tabs speichern willst, erscheint eine Warnmeldung, dass in diesem Fall die Änderungen im anderen Tab verloren gehen:

{{ 4 | image: 'Warnung: ungespeicherte Änderungen in einem anderen Tab', '50%'}}

> Einzeltage innerhalb eines mehrtägigen Urlaubsblocks bearbeiten oder löschen
>
> Wenn Du einzelne Tage innerhalb eines mehrtägigen Blocks aus genehmigten Urlaubsaktivitäten in der Ebene _Plan_ bearbeiten oder löschen willst, musst Du immer zunächst den gesamten Urlaubs-Aktivitätsblock löschen. Anschließend kannst Du einzelne Tage über den Tab {% link_new Verlauf | features/scheduling/schedules/schedules-edit.md %} wiederherstellen.

## Aktivitäten löschen

1. Doppelklicke auf eine **Zelle**, um die Bearbeitungsansicht zu öffnen.
2. Klicke rechts auf den **X**-Button neben einer Aktivität, um diese für das Löschen zu markieren. Klicke erneut, wenn Du dies rückgängig machen willst. Klicke auf _Alle Aktivitäten löschen_{:.doc-button}, um alle Zeilen auf einmal zu markieren.
3. Klicke auf _Speichern_{:.doc-button}. Dies löscht alle für das Löschen markierte Aktivitäten.

   {{ 3 | image: 'Aktivität löschen', '80%'}}

## Schichten direkt im Schichtplan ändern

Du kannst komplette Schichten direkt im Schichtplan mit Hilfe von Tastaturkürzeln kopieren, ausschneiden, einfügen und löschen:

| Tastaturkürzel | Funktion                                                                                                         |
| -------------- | ---------------------------------------------------------------------------------------------------------------- |
| **STRG + C**   | Kopiert die Schicht in der ausgewählten Zelle. Du kannst sie nun in anderen Zellen einfügen.                     |
| **STRG + X**   | Schneidet die Schicht in der ausgewählten Zelle aus. Du kannst sie nun einmalig in einer anderen Zelle einfügen. |
| **STRG + V**   | Fügt eine kopierte Schicht in die ausgewählte Zelle ein.                                                         |
| **STRG + L**   | Löscht den Inhalt der ausgewählten Zelle.                                                                        |
| **←**/**Entf** | Löscht den Inhalt der ausgewählten Zelle.                                                                        |
| **ESC**        | Entfernt die Auswahl von einer ausgewählten Zelle.                                                               |

Hinweis: Die Tastaturkürzel funktionieren nicht in der Detailansicht eines Tages.
