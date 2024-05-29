---
title: Was sind Planperioden?
description: Lerne, wofür Planperioden genutzt werden und wie du sie anzeigst, bearbeitest und löschst (Schedules-Modul).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
---

In diesem Artikel lernst du:

- was Planperioden sind und wofür sie genutzt werden.
- wie du Planperioden anzeigst, bearbeitest und löschst.

## Wofür werden Planperioden genutzt?

Planperioden sind Zeiträume von einigen Tagen, Wochen oder Monaten. Verwende sie, wenn du Mitarbeitern ermöglichen möchtest:

- {% link_new den eigenen Schichtplan einzusehen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %}.
- {% link_new Schichten mit anderen Mitarbeitern zu tauschen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.
- {% link_new am Schichtwunsch-Verfahren teilzunehmen | features/scheduling/schedules/schedules-shift-bidding.md %}.

Um deinen Mitarbeitern zu ermöglichen, Urlaube und Abwesenheiten zu beantragen, nutze {% link_new Abwesenheitssperioden | features/scheduling/time-off/time-off-periods.md %}.

### Status

Jede Planperiode hat einen Status. Der Status schaltet bestimmte Optionen für Mitarbeiter für den Zeitraum der Planperiode frei oder schränkt sie ein. Normalerweise änderst du den Status einer Planperiode mehrmals während des Planungsprozesses, z. B. nachdem du die Schichtplanung abgeschlossen hast oder wenn der Zeitraum für das Abgeben von Schichtwünschen abgelaufen ist.

| Status                        | Erklärung                                                                                                                                                                                                                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unveröffentlicht              | Mitarbeiter können den veröffentlichten Schichtplan nicht sehen, können nicht am {% link_new Schichtwunsch-Verfahren                                                                                                                      | features/scheduling/schedules/schedules-shift-bidding.md %} teilnehmen und können keine Schichten miteinander tauschen. Verwende diesen Status, wenn du den Schichtplan noch nicht für deine Mitarbeiter freigeben möchtest. |
| Schichtwünsche freigeschaltet | Mitarbeiter können den veröffentlichten Schichtplan sehen, am Schichtwunsch-Verfahren teilnehmen und Schichten miteinander tauschen. Dieser Status kann _nicht_ gesetzt werden, wenn der Stichtag der Planperiode bereits abgelaufen ist. |
| Veröffentlicht                | Mitarbeiter können den veröffentlichten Schichtplan sehen und können Schichten miteinander tauschen. Sie können _nicht_ am Schichtwunsch-Verfahren teilnehmen.                                                                            |
| Abgeschlossen                 | Verwende diesen Status, um anzuzeigen, dass die Planung abgeschlossen ist. Mitarbeiter können noch Schichten miteinander tauschen.                                                                                                        |

## Planperioden filtern und anzeigen

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Klicke auf _Planperioden_{:.doc-button}.
3. Wähle eine **Planungseinheit** oder tippe, um die Liste zu filtern.
4. Optional: Wähle eine **Auswahl**.

Darunter erscheinen nun alle Planperioden der gewählten Planungseinheit bzw. Auswahl. Im Tab Gültig siehst du Planperioden, deren Zeitraum teilweise oder ganz in der Zukunft liegt. Der Tab Abgelaufen zeigt Planperioden an, die vollständig in der Vergangenheit liegen. Die Tabs sind leer, wenn du noch keine Planperioden angelegt hast oder wenn die Filterkriterien auf keine deiner Planperioden zutreffen.

Die Liste der Planperioden hat sechs Spalten:

- Status: der aktuelle Status der Planperiode
- Auswahl: die Auswahl der Mitarbeiter, die von der Planperiode betroffen sind
- Gültig ab: das Startdatum der Planperiode
- Gültig bis: das Enddatum der Planperiode
- Stichtag: bis zu diesen Datum können Mitarbeiter am Schichtwunsch-Verfahren teilnehmen und Schichten tauschen
- Geerbt von: wenn du eine Planperiode für eine übergeordnete Planungseinheit erstellst, wird ihr Status an alle untergeordneten Planungseinheiten vererbt; die Spalte zeigt dann den Namen der übergeordneten Planungseinheit an

Du kannst die Liste nach einer beliebigen Spalte sortieren, indem du auf die jeweilige **Spaltenüberschrift** klickst. Um die Sortierung umzukehren, klicke erneut.

{{ 1 | image: 'Planperioden-Liste', '80%' }}

## Neue Planperiode anlegen

Um eine neue Planperiode zu erstellen, klicke oben rechts auf _Planperiode erstellen_{:.doc-button}. Es erscheint ein Dialog, in dem du eine Planungseinheit, zu der die Planperiode gehören soll, eine Auswahl, einen Zeitraum, einen Stichtag und einen Status auswählen kannst. Da diese Informationen davon abhängen, was du mit der Planperiode erreichen willst, findest du weitere Informationen in den [oben verlinkten Artikeln](#wofür-werden-planperioden-genutzt) zu den jeweiligen Anwendungsfällen.

## Planperiode bearbeiten

Der häufigste Grund für die Bearbeitung einer Planperiode ist die Aktualisierung ihres Status. Du kannst den Status einer Planperiode einfach links in der _Status_-Spalte ändern. Wähle einfach einen anderen Status aus dem **Dropdown**. Der geänderte Status wird automatisch gespeichert.

Um alle anderen Einstellungen einer Planperiode (einschließlich des Status) zu bearbeiten, bewege den Mauszeiger über eine Planperiode und klicke rechts auf das **Stift**-Symbol.

## Planperioden löschen

Um eine oder mehrere Planperioden zu löschen, aktiviere die **Checkboxen** auf der linken Seite der Liste. Die oberste Checkbox wählt alle angezeigten Einträge aus. Klicke dann auf _Ausgewählte löschen_{:.doc-button} unterhalb der Liste.
