---
title: Mitarbeitern das Beantragen von Urlaub und Abwesenheiten ermöglichen
toc: false
description: Ermögliche deinen Mitarbeitern, im Mitarbeiterportal injixo Me Urlaub und Abwesenheiten zu beantragen.
product_label:
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shift-bidding.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/target-work-accounts.md
---

In diesem Artikel lernst du, wie du deinen Mitarbeitern ermöglichst, im Mitarbeiterportal injixo Me Urlaub und Abwesenheiten zu beantragen.

Hierfür verwendest du Planperioden. Lies daher zuerst den Artikel {% link_new Was sind Planperioden? | features/scheduling/planning-periods/what-are-planning-periods.md %}.

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Wenn du injixo Essential WFM, Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen {% link_new Planperioden | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} unter _Plan > Schedules_{:.breadcrumbs} und {% link_new Abwesenheitsperioden | features/scheduling/time-off/time-off-periods.md %} unter _Plan > Time Off_{:.breadcrumbs}.

## Mitarbeitern das Beantragen von Urlaub und Abwesenheiten ermöglichen

Um das Beantragen von _Urlaub oder Abwesenheiten_ zu ermöglichen, musst du zunächst die Option in injixo Me aktivieren. Klicke auf _Me_{:.breadcrumbs} in der Hauptnavigation und schalte die Option **Urlaub/Abwesenheiten** ein.

1. Gehe zu _WFM > Scheduling > SchedulePro > Planperioden_{:.breadcrumbs}.
2. Wähle die **Planungseinheit**, für die du das Beantragen von Urlaub oder Abwesenheiten ermöglichen willst.
3. Wähle als **Typ** eine _wünschbare_ Aktivität aus der Liste. Wenn du noch keine {% link_new Aktivität als wünschbar | features/administration/activities.md %} konfiguriert hast, hole das jetzt nach und {% link_new weise die Aktivität der Planungseinheit zu | features/administration/create-and-manage-planning-units.md %}.
4. Wähle eine **Auswahl**, wenn du das Beantragen von Urlaub oder Abwesenheiten auf eine bestimmte Mitarbeitergruppe beschränken willst. Wähle ansonsten **[Alle]**.
5. Klicke auf _Anwenden_{:.doc-button}.
6. Existiert eine passende Planperiode, wähle diese aus und klicke auf _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon} in der Aktionsleiste. Wenn es keine passende Planperiode in der Liste gibt, erstelle eine neue mit einem Klick auf das {% icon item-add %}.

In beiden Fällen erscheint der folgende Dialog:

{{ 3 | image: 'Define Planning Period', '60%' }}

1. Lege bei einer neuen Planperiode mit **Gültig von** und **Gültig bis** einen Zeitraum fest, z.B. drei Monate oder auch das ganze Jahr. Eine Planperiode für Urlaub oder andere Abwesenheiten ist meist länger als nur eine Woche.
2. Wähle den **Status** _Freigegeben_.
3. Optional: Setze einen **Stichtag**. Bis zu diesem Datum, können Mitarbeiter Anträge einreichen.

Deine Mitarbeiter können nun im Mitarbeiterportal injixo Me Urlaubs- und sonstige Abwesenheitsanträge für den durch die Planperiode definierten Zeitraum einreichen. Als Planer kannst du die Anträge dann {% link_new genehmigen oder ablehnen | features/scheduling/time-off/vacation-absences-management.md %}.
