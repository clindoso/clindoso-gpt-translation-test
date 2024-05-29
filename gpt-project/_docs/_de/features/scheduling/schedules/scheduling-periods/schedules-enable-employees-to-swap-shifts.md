---
title: Schichttausch zwischen Mitarbeitern ermöglichen
toc: false
description: Ermögliche Deinen Mitarbeitern, im Mitarbeiterportal injixo Me Schichten untereinander zu tauschen (Schedules).
product_label:
  - essential
  - advanced
  - enterprise
redirect_from: /de/schedules-enable-employees-to-exchange-shifts/
redirect_reason: file renamed in March 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
---

In diesem Artikel lernst Du, wie Du Deinen Mitarbeitern ermöglichst, im Mitarbeiterportal injixo Me Schichten untereinander zu tauschen.

Hierfür verwendest Du Planperioden. Lies daher zuerst den Artikel {% link_new Was sind Planperioden? | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %}.

## Schichttausch zwischen Mitarbeitern ermöglichen

Um den Schichttausch zu ermöglichen, musst Du zunächst die Option in injixo Me aktivieren. Klicke auf _Me_{:.breadcrumbs} in der Hauptnavigation und aktiviere die Option **Schichttauschbörse**.

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Klicke auf _Planperioden_{:.doc-button}.
3. Wähle die **Planungseinheit**, in der Du den Schichttausch aktivieren möchtest.
4. Wähle eine **Auswahl**, wenn Du die Möglichkeit des Schichttausches auf eine bestimmte Gruppe von Mitarbeitern beschränken möchtest (optional). Wenn Du möchtest, dass alle Mitarbeiter in der Planungseinheit Schichten miteinander tauschen können, lass das Feld leer.
5. Finde eine bestehende Planperiode mit dem Datumsbereich, für den Du den Schichttausch aktivieren möchtest. Klicke auf das **Dropdown** in der Spalte _Status_ und ändere den Status auf _Information_.

Hinweis: Der Status _Schichtwünsche freigegeben_ ermöglicht es Deinen Mitarbeitern sowohl Schichten zu tauschen als auch sich im Schichtwunsch-Verfahren Schichten zu wünschen. Im Status _Veröffentlicht_ können sie nur Schichten tauschen.

Wenn es noch keine Planperiode für diesen Zeitraum gibt, klicke auf _Planperiode erstellen_{:.doc-button}:

1. Lege einen **Zeitraum** fest, um den Datumsbereich zu definieren, für den Du den Schichttausch aktivieren möchtest.
2. Wähle den **Status** _Veröffentlicht_.
3. Optional: Setze einen **Stichtag**. Bis zu diesem Datum können die Mitarbeiter Schichten tauschen.
4. Bestätige mit _Speichern_{:.doc-button}.

   {{ 3 | image: 'Termin festlegen', '40%' }}

Deine Mitarbeiter können jetzt für den durch die Planperiode definierten Zeitraum bis zum gesetzten Stichtag im Mitarbeiterportal injixo Me Schichten tauschen. Dies ist für alle {% link_new Aktivitäten | features/administration/activity-examples.md %} möglich, die als _tauschbar_ konfiguriert sind.
