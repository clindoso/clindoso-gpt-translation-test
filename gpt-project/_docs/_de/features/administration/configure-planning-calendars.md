---
title: Planungskalender konfigurieren
description: Konfiguriere Planungskalender, um deine Standardöffnungszeiten automatisch für Tage mit abweichenden Öffnungszeiten anzupassen.
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
redirect_from:
  - /de/planning-calendar/
redirect_reason: Updated filename on 13 March 2024
---

In einem Planungskalender kannst du Tage mit abweichenden Öffnungszeiten oder besonderem Mitarbeiterbedarf markieren (z.&nbsp;B. Feiertage oder Tage, an denen Marketingkampagnen stattfinden). Du verwendest dazu {% link_new Tagestypen | features/administration/day-types.md %}, um sicherzustellen, dass diese Tage bei der Schichtplanung automatisch berücksichtigt werden. Wenn du dem Planungskalender einen Tagestyp hinzufügst, überschreibt dieser die Standardöffnungszeiten für diesen Tag. Du kannst verschiedene Planungskalender für verschiedene Planungseinheiten oder Regionen erstellen, wenn diese zum Beispiel abweichende Öffnungszeiten oder Feiertage haben.

## Planungskalender konfigurieren

Voraussetzung: Du hast die relevanten benutzerdefinierten {% link_new Tagestypen | features/administration/day-types.md %} erstellt, die du deinem Planungskalender hinzufügen möchtest.

1. Gehe zu _Plan > Konfiguration > Planungskalender_{:.breadcrumbs}.
2. Klicke in der Aktionsleiste auf das Neu-Icon {% icon item-add | icon-only %}.
3. Konfiguriere den Planungskalender:
   - **Jahr**: Gib das Jahr an, für das du den Planungskalender verwenden möchtest.<br>Um einen Planungskalender zu erstellen, der mehr als ein Jahr umfasst, zum Beispiel, wenn du Schichtpläne erstellst, die über ein Jahr hinausgehen, verwende _<_{:.doc-button} und _>_{:.doc-button}, um zu einem früheren oder späteren Jahr zu navigieren. Konfiguriere anschließend den Kalender für jedes Jahr einzeln.
   - **Kalendervorlage**: Wähle die Feiertagsregion aus und klicke auf _Anwenden_{:.doc-button}.<br>Der Planungskalender wird automatisch mit den Feiertagen deiner ausgewählten Region bzw. des von dir ausgewählten Landes befüllt.<br>Wenn du deinem Planungskalender mehrere Regionen hinzufügen möchtest, wiederhole diesen Schritt für jede weitere Region, die dein Planungskalender enthalten soll.<br>Hinweis: Jede Zelle im Planungskalender kann nur einen Feiertag enthalten. Wenn du eine Vorlage auswählst, in der ein Feiertag auf denselben Tag fällt wie bei einer bereits zuvor ausgewählten Vorlage, werden Zellen, in denen bereits Feiertage eingetragen sind, mit Einträgen aus der neuen Vorlage überschrieben.
   - **Tagestyp einfügen**: Wähle den benutzerdefinierten Tagestyp aus dem Dropdown-Menü aus und klicke auf jede Kalenderzelle, in die du den Tagestyp einfügen möchtest.<br>Hinweis: Du kannst nur einen Tagestyp pro Tag zuweisen. Wenn du auf eine Zelle klickst, die bereits einen Tagestyp enthält, wird dieser überschrieben. Wenn du deinem Planungskalender mehr als einen benutzerdefinierten Tagestyp hinzufügen möchtest, wiederhole diesen Schritt für jeden weiteren Tagestyp, den dein Planungskalender enthalten soll.
4. Klicke in der Aktionsleiste auf das Speichern-als-Icon _![Speichern als](/assets/img/common/saveas.gif)_{:.doc-button-icon}.
5. Gib im Bestätigungsfenster einen Namen für den Kalender ein und klicke auf _OK_{:.doc-button}.

## Tagestypen aus dem Planungskalender entfernen

Wenn deine Planungseinheit an bestimmten Tagen geschlossen ist und deine Mitarbeiter kein Feiertagsentgelt für diese Tage erhalten, stelle sicher, dass diese Tage nicht als {% link_new Tagestypen mit Feiertagsmodus | features/administration/day-types.md | #feiertagsmodus %} in deinem Planungskalender enthalten sind. Wenn du diese Tagestypen nicht aus deinem Planungskalender entfernst, reduziert injixo die Zielarbeitszeit für diese Woche und die Mitarbeiter werden für weniger Stunden geplant. Erfahre mehr darüber, wie du {% link_new Feiertage planst | best-practices/scheduling-public-holidays.md | #szenario-1-keine-planung-der-mitarbeiter-am-feiertag %}.

Um Tagestypen aus dem Planungskalender zu entfernen, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Planungskalender_{:.breadcrumbs}.
2. Um einzelne Tagestypen zu entfernen, klicke auf **Löschen**.
3. Klicke auf jede Zelle im Planungskalender, aus der du den Tagestyp entfernen möchtest.
4. (Optional) Um alle Einträge im Kalender für das aktuell ausgewählte Jahr zu löschen, klicke auf _Jahr löschen_{:.doc-button}.
5. (Optional) Um alle Einträge im gesamten Kalenderzeitraum eines Kalenders zu löschen, der mehrere Jahre umfasst, klicke auf _Alle löschen_{:.doc-button}.
6. Klicke auf das Speichern-Icon _![Speichern](/assets/img/common/save.gif)_{:.doc-button-icon}.

## Bestehenden Planungskalender bearbeiten

1. Gehe zu _Plan > Konfiguration > Planungskalender_{:.breadcrumbs}.
2. Wähle in der Aktionsleiste aus dem Dropdown-Menü **Kalender** den Kalender aus, den du bearbeiten möchtest.<br>Wenn du einen Planungskalender vor dem Bearbeiten kopieren möchtest, zum Beispiel, weil du dieselbe Vorlage und dieselben Tagestypen aber für ein anderes Jahr verwenden möchtest, klicke auf das Speichern-als-Icon _![Speichern als](/assets/img/common/saveas.gif)_{:.doc-button-icon} in der Aktionsleiste.
3. Wenn du deine Änderungen abgeschlossen hast, klicke auf das Speichern-Icon _![Speichern](/assets/img/common/save.gif)_{:.doc-button-icon}.

## Planungskalender für die Schichtplanung verwenden

Um einen Planungskalender für die Schichtplanung zu verwenden, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Planungseinheiten_{:.breadcrumbs}.
2. Wähle die Planungseinheit, der du den Planungskalender hinzufügen möchtest.
3. Klicke im Abschnitt **Planungskalender** auf das Neu-Icon {% icon item-add | icon-only %}.
4. Wähle im Konfigurationsfenster **Planungskalender** einen Planungskalender aus.<br>Du kannst einen einzelnen Kalender auswählen, der mehrere Jahre umfasst, zum Beispiel, wenn du einen Schichtplan erstellen möchtest, der über ein Jahr hinausgeht. Wenn du einen eigenen Planungskalender für jedes Jahr zuweisen möchtest, wähle jeden Kalender einzeln aus und verwende die Felder **Gültig vom** und **Gültig bis**, um den Zeitraum festzulegen, in dem er verwendet werden soll. Beachte, dass Planungskalender, die ein einzelnes Jahr umfassen, auch nur für Schichtpläne anwendbar sind, die dieses Jahr umfassen.
5. Klicke auf _OK_{:.doc-button}.

> Hinweis
>
> Wenn deine Planungseinheit untergeordnete Planungseinheiten enthält, wird der Planungskalender diesen nicht automatisch zugewiesen. Bei Bedarf musst du den Planungskalender jeder untergeordneten Planungseinheit manuell zuweisen.
