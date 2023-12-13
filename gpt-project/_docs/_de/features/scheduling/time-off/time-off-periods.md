---
title: Mitarbeitern das Beantragen von Abwesenheit ermöglichen
description: Lerne, wofür Abwesenheitsperioden genutzt werden und wie du sie anzeigst, bearbeitest und löschst.
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-entitlement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-absences-management.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md
---

In diesem Artikel lernst du:
- was Abwesenheitsperioden sind und wofür sie genutzt werden.
- wie du Abwesenheitsperioden anzeigst, bearbeitest und löschst.

## Was sind Abwesenheitsperioden?

Abwesenheitsperioden sind Zeiträume von einigen Tagen, Wochen oder Monaten. Sie steuern, ob und für welche Zeiträume Mitarbeiter Urlaube und Abwesenheiten in injixo Me beantragen können.

Abwesenheitsperioden nutzen Aktivitäten vom Typ Abwesenheit, Urlaub oder Krankheit, die als {% link_new wünschbar | features/administration/activities.md %} konfiguriert sind und {% link_new deiner Planungseinheit zugewiesen | features/administration/create-and-manage-planning-units.md %} sind.

Erstelle eine separate Abwesenheitsperiode für jede Aktivität, die Mitarbeitende beantragen dürfen.

Hinweis: Aktiviere die Option in injixo Me, damit Mitarbeiter diese nutzen können. Klicke auf *Me*{:.breadcrumbs} in der Hauptnavigation und schalte die Option **Urlaub/Abwesenheiten** ein.

Nutze stattdessen {% link_new Planperioden | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %}, wenn du Mitarbeitern ermöglichen willst, den {% link_new Schichtplan zu sehen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %}, {% link_new Schichten zu tauschen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} und {% link_new am Schichtwunsch-Verfahren teilzunehmen | features/scheduling/schedules/schedules-shift-bidding.md %}.

### Status

Jede Abwesenheitsperiode hat einen Status, der festlegt, ob die Mitarbeiter die Abwesenheitsperiode im definierten Zeitraum in injixo Me sehen können oder nicht. Du kannst Abwesenheitsperioden mit einem beliebigen Status erstellen und den Status so oft wie nötig ändern.

Status | Erklärung
------- | -------
Unveröffentlicht | Mitarbeiter können die Abwesenheitsperiode nicht sehen und keine Abwesenheitsanträge einreichen. Verwende diesen Status bist du deinen Mitarbeiter die Abwesenheitsperiode anzeigen möchtest.
Veröffentlicht | Mitarbeiter können die veröffentlichte Abwesenheitsperiode in injixo Me sehen und Abwesenheitsanträge einreichen. Der Zeitraum der Abwesenheitsperiode erscheint in injixo Me mit einem weißen Hintergrund; dieser Status kann nicht gesetzt werden, wenn der Stichtag der Abwesenheitsperiode bereits abgelaufen ist.

## Abwesenheitsperioden filtern und anzeigen

1. Gehe zu *Plan > Urlaub/Abwesenheiten*{:.breadcrumbs}.
2. Klicke oben rechts auf *Abwesenheitsperioden verwalten*{:.doc-button}.
3. Wähle eine **Planungseinheit**, um die Liste zu filtern.
4. Optional: Wähle eine **Auswahl** und/oder eine **Aktivität**.

Du siehst nun eine Liste mit zwei Tabs unterhalb, die die Abwesenheitsperioden der gewählten Planungseinheit, Auswahl und Aktivität enthalten:
- Gültig: Abwesenheitsperioden, deren Zeitraum teilweise oder ganz in der Zukunft liegt.
- Abgelaufen: Abwesenheitsperioden, die vollständig in der Vergangenheit liegen.

Die Tabs sind leer, wenn:
- du noch keine Abwesenheitsperioden angelegt hast.
- die Filterkriterien auf keine deiner Abwesenheitsperioden zutreffen.

{{ 1 | image: 'Abwesenheitsperioden-Liste', '90%' }}

Die Liste der Abwesenheitsperioden auf den Tabs hat sechs Spalten:
- Status: der aktuelle Status der Abwesenheitsperiode
- Auswahl: die Auswahl der Mitarbeiter, die von der Abwesenheitsperiode betroffen sind
- Gültig ab: das Startdatum der Abwesenheitsperiode
- Gültig bis: das Enddatum der Abwesenheitsperiode
- Stichtag: bis zu diesem Datum können Mitarbeiter Abwesenheitsanträge einreichen
- Geerbt von: wenn du eine Abwesenheitsperiode für eine übergeordnete Planungseinheit erstellst, erben alle untergeordneten Planungseinheiten den gleichen Status; die Spalte zeigt dann den Namen der übergeordneten Planungseinheit.

Du kannst die Liste nach einer beliebigen Spalte sortieren, indem du auf die jeweilige **Spaltenüberschrift** klickst. Um die Sortierung umzukehren, klicke erneut.

## Abwesenheitsperiode anlegen

Lege eine Abwesenheitsperiode für den Zeitraum an, in dem du deinen Mitarbeitern ermöglichen möchtest, Urlaube, Krankheiten oder andere Arten von Abwesenheiten zu beantragen:

1. Gehe zu *Plan > Urlaub/Abwesenheiten*{:.breadcrumbs}.
2. Klicke oben rechts auf *Abwesenheitsperiode erstellen*{:.doc-button}.
3. Wähle im Dialog Abwesenheitsperiode erstellen die **Planungseinheit**, für die du das Beantragen von Urlaub oder Abwesenheiten ermöglichen willst.
4. Optional: Wähle eine **Auswahl**, wenn du das Beantragen von Urlaub oder Abwesenheiten auf eine bestimmte Mitarbeitergruppe beschränken willst.
5. Lege einen **Zeitraum** fest.
6. Wähle die wünschbare **Aktivität**, die deine Mitarbeiter eintragen können sollen.
7. Optional. Lege einen **Stichtag** fest. Bis zu diesem Datum, können Mitarbeiter Anträge einreichen.
8. Wähle einen **Status** aus. Deine Mitarbeiter können Urlaub und Abwesenheiten eingeben, wenn du den Status Veröffentlicht wählst.
4. Klicke auf *Speichern*{:.doc-button}, um die neue Abwesenheitsperiode zu erstellen.

    {{ 2 | image: 'Fenster zum Erstellen der Abwesenheitsperioden', '40%' }}

## Abwesenheitsperiode bearbeiten

Der häufigste Grund für die Bearbeitung einer Abwesenheitsperiode ist die Aktualisierung ihres Status links in der Status-Spalte. Wähle einen anderen Status aus dem **Dropdown**. Der geänderte Status wird automatisch gespeichert.

Um alle Einstellungen einer Abwesenheitsperiode (einschließlich des Status) zu bearbeiten, bewege den Mauszeiger über eine Abwesenheitsperiode und klicke rechts auf das **Stift**-Symbol.

## Abwesenheitsperioden löschen

Um eine oder mehrere Abwesenheitsperioden zu löschen, aktiviere die **Checkboxen** auf der linken Seite der Liste. Die oberste Checkbox wählt alle angezeigten Einträge aus. Klicke dann auf *Ausgewählte löschen*{:.doc-button} unterhalb der Liste.
