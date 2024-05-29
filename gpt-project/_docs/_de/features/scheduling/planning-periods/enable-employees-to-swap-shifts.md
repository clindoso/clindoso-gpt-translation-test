---
title: Schichttausch zwischen Mitarbeitern ermöglichen
toc: false
description: Ermögliche Deinen Mitarbeitern, im Mitarbeiterportal injixo Me Schichten untereinander zu tauschen (SchedulePro).
product_label:
  - classic
redirect_from: /de/enable-employees-to-exchange-shifts/
redirect_reason: file renamed in March 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shift-bidding.md
---

In diesem Artikel lernst Du, wie Du Deinen Mitarbeitern ermöglichst, im Mitarbeiterportal injixo Me Schichten untereinander zu tauschen.

Hierfür verwendest Du Planperioden. Lies daher zuerst den Artikel {% link_new Was sind Planperioden? | features/scheduling/planning-periods/what-are-planning-periods.md %}.

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Wenn Du injixo Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen {% link_new Planperioden | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} unter _Plan > Schedules_{:.breadcrumbs}.

## Schichttausch zwischen Mitarbeitern ermöglichen

Um den Schichttausch zu ermöglichen, musst Du zunächst die Option in injixo Me aktivieren. Klicke auf _Me_{:.breadcrumbs} in der Hauptnavigation und aktiviere die Option **Schichttauschbörse**.

1. Gehe zu _WFM > Scheduling > SchedulePro > Planperioden_{:.breadcrumbs}.
2. Wähle eine **Planungseinheit** aus.
3. Wähle den **Typ** _Standard_.
4. Wähle eine **Auswahl**, wenn Du die Möglichkeit zum Schichttausch auf eine bestimmte Gruppe von Mitarbeitern beschränken möchtest. Wähle ansonsten **[Alle]**.
5. Klicke auf _Anwenden_{:.doc-button}.
6. Wähle die Planperiode mit dem Datumsbereich aus, für den Du das Tauschen von Schichten zulassen möchtest und klicke auf das {% icon item-edit %} in der Aktionsleiste. Wenn es keine passende Planperiode in der Liste gibt, erstelle eine neue mit einem Klick auf das {% icon item-add %}.

In beiden Fällen erscheint der folgende Dialog:

{{ 3 | image: 'Define Planning Period', '60%' }}

1. Lege bei einer neuen Planperiode mit **Gültig von** und **Gültig bis** den Zeitraum fest, für den Du das Tauschen von Schichten erlauben willst.
2. Wähle den **Status** _Freigegeben_.
3. Optional: Setze einen **Stichtag**. Bis zu diesem Datum können Mitarbeiter Schichten tauschen.
4. Klicke auf _Ok_{:.doc-button}.

Deine Mitarbeiter können nun im Mitarbeiterportal injixo Me für den durch die Planperiode definierten Zeitraum Schichten tauschen. Voraussetzung hierfür ist, dass die entsprechenden {% link_new Aktivitäten | features/administration/activity-examples.md %} als **Tauschbar beim Schichttausch** konfiguriert sind.
