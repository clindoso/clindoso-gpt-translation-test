---
title: Was sind Planperioden?
description: Nutze Planperioden, um Schichtpläne zu veröffentlichen, Urlaubs- und Abwesenheitsanträge zu ermöglichen, Aktivitäten in Schichtplänen auszutauschen und vieles mehr (SchedulePro).
product_label:
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-employees-to-see-their-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shift-bidding.md
---

In diesem Artikel lernst du:
- was Planperioden sind und wofür sie genutzt werden.
- wie du Planperioden anzeigst, bearbeitest und löschst.

> In diesem Artikel geht es um *WFM > Scheduling > SchedulePro*{:.breadcrumbs}.  
>  
> Wenn du injixo Essential WFM, Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen {% link_new Planperioden | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} unter *Plan > Schedules*{:.breadcrumbs} und {% link_new Abwesenheitsperioden | features/scheduling/time-off/time-off-periods.md %} unter *Plan > Time Off*{:.breadcrumbs}.  

## Wofür werden Planperioden genutzt?

Planperioden sind Zeiträume von einigen Tagen, Wochen oder Monaten bis hin zu einem Jahr. Sie werden für verschiedene Planungszwecke verwendet (siehe unten), daher auch ihr Name.

### Typen

Es gibt zwei Arten von Planperioden: Standard-Planperioden und aktivitätsbezogene Planperioden.

{{ 2 | image: 'Different planning period types', '80%' }}

Mit Standard-Planperioden ermöglichst du deinen Mitarbeitern:

- {% link_new den eigenen Schichtplan einzusehen | features/scheduling/planning-periods/enable-employees-to-see-their-schedules.md %}.
- {% link_new Schichten mit anderen Mitarbeitern zu tauschen | features/scheduling/planning-periods/enable-employees-to-swap-shifts.md %}.
- {% link_new am Schichtwunsch-Verfahren teilzunehmen | features/scheduling/shift-bidding.md %}.

Du kannst Standard-Planperioden außerdem nutzen, um:

- {% link_new Richtzeitkonten | features/scheduling/planning-periods/target-work-accounts.md %} zu bearbeiten oder zu berechnen.
- eine {% link_new Aktivität im Schichtplan mit einer anderen Aktivität zu ersetzen | features/scheduling/planning-periods/batch-replace-an-activity.md %}.
- {% link_new Schichtpläne zu kopieren oder zu sichern | features/scheduling/planning-periods/copy-and-back-up-schedules.md %}.
- {% link_new Schichtpläne zu löschen | features/scheduling/planning-periods/delete-schedules.md %}.

Aktivitätsbezogene Planperioden kannst du dagegen nutzen, um Mitarbeitern die Möglichkeit zu geben, {% link_new Urlaub und andere Abwesenheiten zu beantragen | features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md %}. Aktivitätsbezogene Planperioden nutzen Aktivitäten, die als wünschbar konfiguriert sind. Dies sind Aktivitäten vom Typ Abwesenheit, Urlaub oder Krankheit. Lege für jede Aktivität eine eigene Planperiode an, z. B. eine für das Hinzufügen von Urlaubsanträgen und eine für das Hinzufügen von Krankmeldungen.

### Status

Der Status einer Planperiode bestimmt, wie Mitarbeiter mit dieser interagieren können. Normalerweise änderst du den Status einer Planperiode mehrmals während des Planungsprozesses, z. B. nachdem du die Schichtplanung abgeschlossen hast oder wenn der Zeitraum für das Abgeben von Schichtwünschen abgelaufen ist.

Status | Erklärung
------- | -------
Gesperrt | Mitarbeiter können den veröffentlichten Schichtplan nicht sehen, können nicht am {% link_new Schichtwunsch-Verfahren | features/scheduling/shift-bidding.md %} teilnehmen, können keine Schichten miteinander tauschen und können keine Urlaube oder andere Abwesenheiten beantragen. Verwende diesen Status, wenn du den Schichtplan noch nicht für deine Mitarbeiter freigeben möchtest.
Freigegeben | Mitarbeiter können den veröffentlichten Schichtplan sehen, am Schichtwunsch-Verfahren teilnehmen, Urlaube oder andere Abwesenheiten beantragen und Schichten miteinander tauschen. Dieser Status kann nicht gesetzt werden, wenn der Stichtag der Planperiode bereits abgelaufen ist.
Information | Mitarbeiter können den veröffentlichten Schichtplan sehen und können Schichten miteinander tauschen. Sie können nicht am Schichtwunsch-Verfahren teilnehmen und keine Urlaube oder andere Abwesenheiten beantragen. Dieser Status ist nur für Planperioden vom Typ Standard relevant.
Abgeschlossen | Verwende diesen Status, um anzuzeigen, dass die Planung abgeschlossen ist. Mitarbeiter können noch Schichten miteinander tauschen.

Wie du siehst, werden Planperioden auf viele verschiedene Arten verwendet. Klicke oben auf einen der Links zu den unterschiedlichen Anwendungsfällen, um genaue Anleitungen zu erhalten.

## Planperioden filtern und anzeigen

Wenn du zu *WFM > Scheduling > SchedulePro > Planperioden*{:.breadcrumbs} gehst, werden Dir zunächst keine Planperioden angezeigt. Du musst zuerst mit einem Filter die Planperioden auswählen, die du anzeigen möchtest.

1. Wähle eine **Planungseinheit**.
2. Wähle einen **Typ**.
3. Wähle eine **Auswahl** (optional). Das Auswahlfeld ist in injixo Essential WFM nicht verfügbar.
4. Klicke auf *Anwenden*{:.doc-button}, um die entsprechenden Planperioden anzuzeigen. Wenn es keine Übereinstimmungen mit den Filterkriterien gibt, wird nichts angezeigt.

{{ 1 | image: 'Planperioden', '80%' }}

Die Spalte geerbt kennzeichnet Planperioden übergeordneter Planungseinheiten. Berechne Zeitkonten und Richtzeitkonten auf übergeordneten Planungseinheiten für alle untergeordneten Planungseinheiten oder für jede einzeln. Erstellst du eine Planperiode für eine übergeordnete Planungseinheit, wird ihr Status an alle untergeordneten Planungseinheiten vererbt.

## Neue Planperiode anlegen

Um eine neue Planperiode zu erstellen, klicke auf das {% icon item-add %} in der Aktionsleiste. Es erscheint ein Dialog zum Einstellen des Zeitfensters und des Status' der neuen Planperiode. Da diese Angaben abhängig davon sind, was du mit der Planperiode erreichen möchtest, findest du weitere Informationen in den oben verlinkten Artikeln zu den verschiedenen Anwendungsfällen.

## Planperiode bearbeiten

Der häufigste Grund für die Bearbeitung einer Planperiode ist die Aktualisierung ihres Status'. Um eine Planperiode zu bearbeiten, wähle sie aus. Klicke dann auf _![Bearbeiten](/assets/img/common/item-edit.gif)_{:.doc-button-icon} in der Aktionsleiste.

## Planperiode löschen

Um eine Planperiode zu löschen, wähle diese aus. Klicke dann auf _![delete button](/assets/img/common/item-delete.gif)_{:.doc-button-icon} in der Aktionsleiste.
