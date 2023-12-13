---
title: Schichtfolgen einfügen
product_label:
  - essential
  - advanced
  - enterprise
description: Plane mit Schichtfolgen sich wiederholende Abfolgen von Schichten, Verfügbarkeiten oder Aktivitäten (Modul Kapazitätsplanung).
redirect_from:
  - /de/best-practice-shift-sequences/
  - /de/scheduling-shift-sequences/
  - /de/scheduling-insert-shift-sequences/
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
---

<!-- redirects added after removal of bad best practice article, 2020 July, 2nd -->

In diesem Artikel lernst Du, wie Du Schichtfolgen für ausgewählte Mitarbeiter einfügst.

Schichtfolgen sind feste, sich wiederholende Abfolgen von Schichten, Aktivitäten oder Verfügbarkeiten. Nutze diese für die Planung von regelmäßig wiederkehrenden Aufgaben Deiner Mitarbeiter.

## Voraussetzungen

Bevor Du Schichtfolgen in den Schichtplan einfügen kannst:
1. Gehe zu *WFM > Administration > Scheduling > Schichtfolgen*{:.breadcrumbs} und {% link_new erstelle eine oder mehrere Schichtfolgen | features/administration/shift-sequences.md %}.
2. Gehe zu *WFM > Administration > Scheduling > Mitarbeiter*{:.breadcrumbs} und {% link_new ordne die erstellten Schichtfolgen Deinen Mitarbeitern zu | features/administration/employee-overview.md %}.

## Schichtfolgen anzeigen

1. Gehe zu *Plan > Kapazitätsplanung*{:.breadcrumbs}.    
    (Alternativ) Gehe zu *Plan > Schedules*{:.breadcrumbs}. Klicke auf *Planungsaktionen*{:.doc-button}.  

2. Klicke *Schichtfolgen einfügen*{:.doc-button}.  
3. Wähle eine **Planungseinheit**, eine **Auswahl** (optional) und ein **Zeitraum** (Maximal: 2 Jahre) aus, für den Du Schichtfolgen einfügen möchtest.

    {{ 1 | image: 'Schichtfolgen einfügen', '100%' }}

Die Mitarbeiter-Tabelle zeigt in verschiedenen Spalten Details zu den Schichtfolgen, die den Mitarbeitern zugeordnet sind:

- *Personalnummer*: Personalnummer des Mitarbeiters
- *Name*: Name des Mitarbeiters
- *Schichtfolge*: Name der Schichtfolge
- *Reihenfolge*: Nummer der Schichtfolge <sup>1</sup>
- *Mitarbeiterzeile*: die Zeile der Schichtfolge, die für den Mitarbeiter verwendet wird <sup>2</sup>
- *Referenzdatum*: der Startpunkt für die Schichtfolge. Lerne mehr über das {% link_new Referenzdatum | features/administration/reference-date.md %}. <sup>2</sup>
- *Gültig vom* und *Gültig bis*: der Zeitraum, in dem die Schichtfolge gültig ist <sup>2</sup>

<sup>1</sup> Mitarbeiter können mehrere Schichtfolgen haben. Schichtfolgen mit niedrigeren Werten werden zuerst eingefügt und können von nachfolgenden überschrieben werden.  
<sup>2</sup> Die Daten dieser Spalte stammen aus der Schichtfolgen-Konfiguration innerhalb des Mitarbeiters.

## Schichtfolgen einfügen

1. Um einzelne **Mitarbeiter** auszuwählen, aktiviere die **Checkbox** neben den Mitarbeitern. Um alle Mitarbeiter auf einmal auszuwählen, aktiviere die Checkbox ganz oben.
2. (Optional) Klicke auf **Optionen** unterhalb der Tabelle, um Optionen zum Löschen von vorhandenen Schichtplan-Inhalten anzuzeigen:

    - *Alle Aktivitäten und Schichten löschen*: Bestehende Aktivitäten und alle Schichten der Mitarbeiter auf der Zielebene werden gelöscht und durch die ausgewählte Schichtfolge ersetzt; Verfügbarkeitsrahmen bleiben dabei erhalten.
    - *Ganztägige Aktivitäten löschen*: Bestehende ganztägige Aktivitäten der Mitarbeiter werden vor dem Einfügen aus der Zielebene gelöscht und durch die ausgewählte Schichtfolge ersetzt.
    - *Verfügbarkeitsrahmen löschen*: Bestehende Verfügbarkeitsrahmen der Mitarbeiter werden durch die ausgewählte Schichtfolge überschrieben.

    {{ 2 | image: 'Optionen', '40%' }}

3. (Optional) Aktiviere eine oder mehrere **Checkboxen**, um die Option(en) zu aktivieren. Hinweis: injixo berücksichtigt die Optionen nur beim Einfügen der ersten Schichtfolge eines Mitarbeiters, d.h. der Schichtplan-Inhalt wird nur beim Einfügen der ersten Schichtfolge gelöscht.

4. (Optional) Wähle Ebene *Aktueller Stand* als **Zielebene** aus.

5. Um die Schichtfolgen in die Zielebene einzufügen, klicke *Schichtfolgen einfügen*{:.doc-button}.

6. Um zu prüfen, ob es Fehler beim Einfügen gab, klicke auf **Details anzeigen** im Abschnitt *Historie*. Der Report zeigt Planungsregel-IDs und die Gründe dafür, warum Schichtfolgen nicht eingefügt werden konnten.

    {{ 3 | image: 'Schichtfolgen-Historie', '50%' }}

Um Jobs aus dem Abschnitt *Historie* zu löschen, aktiviere die **Checkboxen** neben den Einträgen. Nutze die Checkbox am oberen Rand der Liste, um alle Aufträge auszuwählen. Klicke auf *Löschen*{:.doc-button}, um die markierten Einträge zu löschen.

## Wie wird bestehender Schichtplan-Inhalt behandelt?

Ganztägige Aktivitäten aus Schichtfolgen ersetzen grundsätzlich bereits geplante ganztägige Aktivitäten, z. B. Krank durch Urlaub.

 Untertägige Aktivitäten oder Schichten überschreiben bereits geplante ganztägige Aktivitäten. Um das zu verhindern, aktiviere die Planungsregel *2645*{:.id-label} *Überschreiben von ganztägigen Aktivitäten durch Schichten oder Aktivitäten*.

 Untertägige Aktivitäten oder Schichten überschreiben andere bereits geplante untertägige Aktivitäten. Um das für Aktivitäten vom Typ *Abwesenheit*, *Krankheit*, *Urlaub* oder *Meeting* zu verhindern, aktiviere die Planungsregel *2648*{:.id-label} *Schreibschutz für Aktivitäten im Schicht Center*.
 
