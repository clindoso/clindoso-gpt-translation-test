---
title: Planungskalender erstellen und verwenden
description: Lerne, wie Du Planungskalender mit Hilfe von Tagestypen und Kalendervorlagen einrichtest.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/day-types.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-public-holidays.md
---

In diesem Artikel lernst Du:

- was Planungskalender sind und wie sie funktionieren.
- wie Du sie erstellst, bearbeitest, kopierst und löschst.
- wie Du Feiertage und Tagestypen hinzufügst.
- wie Du einen Planungskalender für die Planung verwendest.

## Was ist ein Planungskalender?

Mit einem Planungskalender kannst Du Tage mit abweichenden Öffnungszeiten und abweichendem Mitarbeiterbedarf (z.B. Marketing-Aktionstage oder Feiertage) markieren. So stellst Du sicher, dass sie bei der Planung berücksichtigt werden.

Für die Markierung verwendest Du {% link_new Tagestypen | features/administration/day-types.md %}. Wenn Du einen Tagestyp in den Planungskalender einträgst, überschreibt er die Öffnungszeiten des normalen Wochentags (Mo-So) für diesen Tag.

Es kann sinnvoll sein, verschiedene Planungskalender für verschiedene Planungseinheiten oder Regionen zu erstellen. Ein Kalender kann mehrere Jahre umfassen.

{{ 1 | image: 'leerer Planungskalender' }}

## Einen Planungskalender erstellen

1. Gehe zu _WFM > Administration > Scheduling > Planungskalender_{:.breadcrumbs}
2. Klicke auf das {% icon item-add %} in der Aktionsleiste. Beginne mit der Bearbeitung des leeren Kalenders direkt darunter.
3. Klicke auf das {% icon saveas %} in der Aktionsleiste, um den leeren Kalender zu speichern.
4. Gib einen **Namen** für den Kalender ein und klicke auf _Ok_{:.doc-button}.

Jetzt kannst Du automatisch die Feiertage Deiner Region und einzelne Tagestypen hinzufügen.

### Feiertage Deiner Region hinzufügen

1. Gehe zu _WFM > Administration > Scheduling > Planungskalender_{:.breadcrumbs}
2. Wähle das **Jahr** aus, für das Du Feiertage hinzufügen möchtest.
3. Wähle Dein Land und Deine Region aus dem Dropdown-Menü unter **Kalendervorlage**.
4. Klicke auf _Anwenden_{:.doc-button}, um alle Feiertage aus der Vorlage einzufügen. Wiederhole die Schritte 1 bis 3, wenn Du die Feiertage einer anderen Region oder die gleichen Feiertage für ein anderes Jahr einfügen möchtest. Beachte, dass Tage, die bereits Feiertage enthalten, durch das Einfügen einer anderen Vorlage mit neuen Daten überschrieben werden können.
5. Klicke auf das {% icon save %} in der Aktionsleiste, um den Kalender zu speichern.

Wenn Du eine Kalendervorlage einfügst, erstellt injixo automatisch die {% link_new Tagestypen | features/administration/day-types.md %} für alle in der Vorlage enthaltenen Feiertage, falls sie noch nicht existieren.

Die eingefügten Tage werden automatisch als Feiertage konfiguriert, indem der _Feiertagsmodus_ in den Einstellungen des Tagestyps aktiviert wird. Wenn Du einen bestimmten Feiertag in der Arbeitszeitberechnung wie einen normalen Arbeitstag behandeln willst, deaktiviere den Feiertagsmodus manuell unter _WFM > Administration > Scheduling > Tagestypen_{:.breadcrumbs}.

An Tagen, an denen Deine Planungseinheit geschlossen ist, die Mitarbeiter aber kein Urlaubsgeld erhalten, solltest Du Tagestypen mit Feiertagsmodus aus dem Kalender löschen. Andernfalls wird injixo die Sollarbeitszeit für diese Woche reduzieren und die Mitarbeiter werden für weniger Stunden als normal geplant.

### Benutzerdefinierte Tagestypen zum Planungskalender hinzufügen

Erstelle zuerst die {% link_new Tagestypen | features/administration/day-types.md %}, die Du hinzufügen möchtest.

1. Wähle **Tagestyp einfügen**.
2. Wähle den **Tagestyp** aus der Dropdown-Liste.
3. Um den Tagestyp zu einem Tag hinzuzufügen, klicke auf eine **Tageszelle** innerhalb des Planungskalenders. Du kannst nur einen Tagestyp pro Tag zuweisen. Wenn Du auf eine Zelle klickst, die bereits einen Tagestyp enthält, wird dieser überschrieben.
4. Verwende das {% icon undo %} und das {% icon redo %} in der Aktionsleiste, um Änderungen rückgängig zu machen und wiederherzustellen.
5. Wiederhole den Vorgang für andere Tagestypen, die Du hinzufügen möchtest.
6. Klicke auf das {% icon save %} in der Aktionsleiste, um den Kalender zu speichern.

### Tagestypen aus dem Planungskalender entfernen

Entferne Tagestypen aus dem Planungskalender mit einer der folgenden Optionen:

- Markiere die Option **Löschen** und klicke dann auf eine Zelle im Planungskalender, um den Tagestyp zu löschen.
- Klicke auf den Button **Jahr löschen** auf der rechten Seite, um den Kalenderinhalt für das angezeigte Jahr zu löschen.
- Klicke auf den Button **Alles löschen** auf der rechten Seite, um den Kalenderinhalt für den gesamten Zeitbereich des Kalenders zu löschen.

## Einen bestehenden Planungskalender ändern oder kopieren

1. Wähle über das Dropdownfeld **Kalender** in der Aktionsleiste einen Kalender aus. Um den Kalender vor der Bearbeitung zu kopieren, klicke auf _![save as button](/assets/img/common/saveas.gif)_{:.doc-button-icon}.
2. Füge Tagestypen hinzu, entferne sie oder füge wie oben beschrieben eine Kalendervorlage mit Feiertagen ein. Du kannst den Kalender auch umbenennen, indem Du auf _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon} in der Aktionsleiste klickst.
3. Klicke auf _![save button](/assets/img/common/save.gif)_{:.doc-button-icon}, um den Kalender zu speichern.

## Einen Planungskalender für die Planung verwenden

Um einen Kalender zu verwenden, ordne ihn einer Planungseinheit unter _WFM > Administration > Planung > Planungseinheiten_{:.breadcrumbs} zu:

1. Wähle die **Planungseinheit** aus.
2. Scrolle zum Abschnitt **Planungskalender**.
3. Klicke auf das {% icon item-add %}.
4. Wähle einen **Planungskalender**. Du kannst einen Kalender zuweisen, der mehrere Jahre enthält. Wenn Du verschiedene Planungskalender für jedes Jahr zuweisen möchtest, wähle jeden Kalender einzeln aus und verwende **Gültig vom** und **Gültig bis**, um den Zeitraum festzulegen, in dem er verwendet werden soll.
5. Klicke auf _Ok_{:.doc-button}

Enthält Deine Planungseinheit untergeordnete Planungseinheiten, wird der Planungskalender diesen _nicht_ automatisch zugewiesen. Bei Bedarf kannst Du den Planungskalender dort manuell zuweisen.
