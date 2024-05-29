---
title: Mitarbeitern Schichtpläne anzeigen
toc: false
description: Ermögliche Deinen Mitarbeitern, ihre Schichten im Mitarbeiterportal injixo Me zu sehen (SchedulePro).
product_label:
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md
---

In diesem Artikel lernst Du, wie Du Mitarbeitern über injixo Me Zugriff auf ihre Schichtpläne gibst.

Hierfür verwendest Du Planperioden. Lies daher zuerst den Artikel {% link_new Was sind Planperioden? | features/scheduling/planning-periods/what-are-planning-periods.md %}.

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Wenn Du injixo Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen {% link_new Planperioden | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} unter _Plan > Schedules_{:.breadcrumbs}.

## Mitarbeitern Ihre Schichtpläne anzeigen

1. Gehe zu _WFM > Scheduling > SchedulePro > Planperioden_{:.breadcrumbs}.
2. Wähle eine **Planungseinheit** aus.
3. Wähle den **Typ** _Standard_.
4. Setze die **Auswahl** auf **[Alle]**, wenn Du die Veröffentlichung der Schichtpläne nicht auf eine bestimmte Mitarbeitergruppe beschränken willst. Wenn Du die Veröffentlichung einschränken willst, wähle die entsprechende Auswahl.
5. Klicke auf _Anwenden_{:.doc-button}.
6. Wenn schon eine Planperiode für den Zeitraum existiert, in dem Du Schichten veröffentlichen willst, wähle diese aus und klicke auf das {% icon item-add %} in der Aktionsleiste. Wenn es keine passende Planperiode in der Liste gibt, erstelle eine neue mit einem Klick auf das {% icon item-add %} in der Aktionsleiste.

In beiden Fällen erscheint der folgende Dialog:

{{ 3 | image: 'Define Planning Period', '60%' }}

1. Lege bei einer neuen Planperiode mit **Gültig von** und **Gültig bis** den Zeitraum fest, in dem Du die Schichtpläne veröffentlichen möchtest.
2. Wähle den **Status** _Information_, wenn Du nur möchtest, dass Mitarbeiter ihre Schichtpläne sehen können. Wenn die Planperiode auch für das {% link_new Schichtwunsch-Verfahren | features/scheduling/shift-bidding.md %} und für den {% link_new Schichttausch | features/scheduling/planning-periods/enable-employees-to-swap-shifts.md %} zwischen Mitarbeitern verwendet wird, wähle _Freigegeben._
3. Optional: Setze einen **Stichtag** (nur relevant für das Schichtwunsch-Verfahren und den Schichttausch). Schichtpläne sind auch nach Ablauf der Frist weiterhin sichtbar.
4. Klicke auf _Ok_{:.doc-button}.

## E-Mail und Browser-Benachrichtigungen

Wenn Du möchtest, dass Deine Mitarbeiter in injixo Me ihre Schichten einsehen können, kannst Du Deine Mitarbeiter per E-Mail oder Browser-Benachrichtigung darüber informieren.

Um {% link_new Browser-Benachrichtigungen | getting-started/notifications.md %} zu bekommen, müssen Deine Mitarbeiter diese Benachrichtigungen erst in ihrem Browser aktivieren.

Standardmäßig sind sowohl E-Mail- als auch Browser-Benachrichtigungen aktiviert. Um E-Mail- oder Browser-Benachrichtigungen für Deine Mitarbeiter zu deaktivieren, gehe zu _Account > Benachrichtigungen_{:.breadcrumbs}.
