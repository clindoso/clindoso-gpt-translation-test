---
title: Self-learning Sessions planen
product_label:
  - advanced
  - enterprise
toc: false
description: Erzeuge Terminvorschläge für Self-learning Sessions, die die Deckung Deiner anderen Aktivitäten möglichst wenig beeinflussen (Meetings-Modul).
---

In diesem Artikel lernst Du, wie Du Terminvorschläge für Self-learning Sessions erzeugst, die die Deckung Deiner anderen Aktivitäten möglichst wenig beeinflussen.

Neu im Meetings-Modul? Lerne zuerst {% link_new die Grundlagen | features/scheduling/meetings/meetings-overview.md %}.

## Terminvorschläge für Self-learning Sessions erzeugen

Self-learning Sessions sind Meetings für einzelne Mitarbeiter ohne Meeting-Gastgeber.

1. Gehe zu *Plan > Meetings*{:.breadcrumbs}.
2. Klicke auf *Erstellen*{:.doc-button} in der *Self-learning Sessions*-Karte oben auf der Seite.
3. Wähle im Bereich *Eckdaten* die **Planungseinheit** aus, für die Du Self-learning Sessions planen möchtest. Wähle einen Eintrag aus der Liste oder beginne den Namen der Planungseinheit zu tippen, um die Liste zu filtern. Nach der Auswahl einer Planungseinheit erscheint eine Hinweisbox, die Dich darüber informiert, wie viele Aktivitäten vom Typ *Anwesenheit* in der Planungseinheit nicht als *Ersetzbar* konfiguriert sind.
4. Wähle unter **Zu planende Aktivität** die Aktivität für die Self-learning Session aus, die Du planen möchtest. Self-learning Sessions werden in injixo als *Meetings* betrachtet. Daher siehst Du nun eine Liste, die alle Aktivitäten vom Typ *Meeting* enthält, die der Planungseinheit zugewiesen wurden. Wähle einen Eintrag aus der Liste oder beginne den Namen der Aktivität zu tippen, um die Liste zu filtern. Wenn Du noch keine {% link_new Meeting-Aktivität | features/administration/activities.md %} für die Self-learning Session erstellt hast, tue es jetzt.
5. Wähle den **Zeitraum** aus, in dem Du die Self-learning Sessions planen möchtest. Standardmäßig ist der Datumsbereich auf die nächste Arbeitswoche (Montag - Sonntag) nach dem aktuellen Datum voreingestellt.
6. Lege eine **Länge der Session** in Minuten fest. Der Standardwert ist 60 Minuten.
7. Lege mit **Sessions pro Teilnehmer** fest, wie viele Sitzungen Du für jeden Teilnehmer planen möchtest.

    {{ 1 | image: 'Eckdaten', '60%' }}

8. Aktiviere im Abschnitt *Optionale Eckdaten* einen Haken bei **Beschränke für jeden Teilnehmer die Anzahl der Sessions pro Tag auf maximal**, wenn Du die Anzahl der Self-learning Sessions pro Tag für jeden Teilnehmer begrenzen möchtest. Gib dann unten die maximale **Anzahl** der Sitzungen pro Tag ein.
9. Aktiviere die Checkbox **Plane eine Pause zwischen den Sessions für jeden Teilnehmer**, wenn Du sicherstellen möchtest, dass für jeden Teilnehmer ein bestimmter Zeitpuffer zwischen zwei Sessions eingehalten wird. Wähle darunter einen passenden **Wert** aus dem Dropdown.

    {{ 3 | image: 'Eckdaten', '60%' }}

10. Im Abschnitt *Teilnehmer* definierst Du die Liste der Teilnehmer, für die Self-learning Sessions geplant werden:
    - Optional: Wähle die Option {% link_new **Auswahl** | features/administration/selections.md %} oder **Mitarbeiterfilter** über die Buttons oben aus und wähle rechts ein Element aus dem Dropdown-Menü, um die Liste aller Mitarbeiter zu filtern.
    - Aktiviere die **Checkbox** links neben einem Mitarbeiter, um diesen auszuwählen. Aktiviere die Checkbox oben in der Liste, um alle Mitarbeiter auf einmal aus- oder abzuwählen.

    {{ 2 | image: 'Teilnehmer', '60%' }}

11. Um Terminvorschläge für Self-learning Sessions zu erzeugen, klicke auf *Termine vorschlagen*{:.doc-button} unten auf der Seite. Du gelangst zurück zur Übersichtsseite.

Nachdem die Terminvorschläge für Self-learning Sessions generiert wurden, musst Du sie {% link_new in den Schichtplan eintragen | features/scheduling/meetings/scheduling-suggestions.md %}.
