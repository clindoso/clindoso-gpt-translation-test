---
title: Gruppentermine planen
product_label:
  - advanced
  - enterprise
description: Erzeuge Terminvorschläge für Gruppentermine, die die Deckung Deiner anderen Aktivitäten möglichst wenig beeinträchtigen (Meetings-Modul).
toc: false
---

In diesem Artikel lernst Du, wie Du Terminvorschläge für Gruppentermine erzeugst, die die Deckung Deiner anderen Aktivitäten möglichst wenig beeinträchtigen.

Neu im Meetings-Modul? Lerne zuerst {% link_new die Grundlagen | features/scheduling/meetings/meetings-overview.md %}.

## Terminvorschläge für Gruppentermine generieren

Gruppentermine finden normalerweise zwischen einem Gastgeber (typischerweise dem Teamleiter) und einer Gruppe von Teilnehmern statt. Ein Gastgeber ist jedoch nicht zwingend erforderlich.

1. Gehe zu *Plan > Meetings*{:.breadcrumbs}.
2. Klicke oben auf der Seite auf *Erstellen*{:.doc-button} in der Karte *Gruppentermine*.
3. Wähle im Abschnitt *Eckdaten* die **Planungseinheit** aus, für die Du Gruppentermine planen möchtest. Wähle einen Eintrag aus der Liste oder beginne mit der Eingabe des Namens der Planungseinheit, um die Liste zu filtern. Nach der Auswahl einer Planungseinheit erscheint eine Hinweisbox, die Dich darüber informiert, wie viele Aktivitäten vom Typ *Anwesenheit* in der Planungseinheit nicht als *Ersetzbar* konfiguriert sind.
4. Wähle bei **Zu planende Aktivität** die Gruppentermin-Aktivität aus, die Du planen möchtest. Die Liste enthält alle Aktivitäten vom Typ *Meeting*, die der Planungseinheit zugewiesen sind. Wähle einen Eintrag aus der Liste oder beginne mit der Eingabe des Namens der Aktivität, um die Liste zu filtern. Wenn Du noch keine {% link_new Meeting-Aktivität | features/administration/activities.md %} erstellt hast, tue es jetzt.
5. Wähle den **Zeitraum** aus, in dem Du Meetings planen möchtest. Standardmäßig ist der Datumsbereich auf die nächste Arbeitswoche (Montag - Sonntag) nach dem aktuellen Datum eingestellt.
6. Lege eine **Meetinglänge** in Minuten fest. Der Standardwert ist 60 Minuten.
7. Aktiviere **Zusätzliche Verfügbarkeitsbedingungen einstellen**, wenn Du bestimmte Zeitfenster festlegen möchtest, in denen die Gruppentermine stattfinden sollen.
    1. Wähle im Feld **Tag** einen Tag aus. Ändere dann ggf. bei **Von** und **Bis** die Start- und Endzeit. 
    2. Optional: Klicke auf **+ Zeitspanne**, um einen weiteren Zeitraum für den Tag hinzuzufügen. Um einen Zeitraum an einem anderen Tag hinzuzufügen, klicke auf *Tag und Zeitspanne hinzufügen*{:.doc-button}. Um Tage wieder zu entfernen, klicke auf **Tag entfernen**.
    {{ 1 | image: 'Settings', '60%' }}

8. Im Abschnitt *Gastgeber* kannst Du zwischen drei Optionen wählen:
  - **Ohne Gastgeber**: Wenn Du auf einen Gastgeber für Gruppentermine verzichtest, können Gruppentermine parallel stattfinden.
  - **Interner Gastgeber**: Wähle diese Option, wenn der Gastgeber in injixo geplant wird. injixo wird die Verfügbarkeit des Gastgebers aus dessen Schichtplan abrufen. Du kannst einen Gastgeber aus einer anderen Planungseinheit auswählen, aber die Planungseinheiten des Gastgebers und der Teilnehmer müssen auf das gleiche Intervall eingestellt sein. Wenn Du diese Option auswählst, schreibt injixo die geplanten Meetings auch in den Schichtplan des Gastgebers. Wähle eine **Planungseinheit** und einen **Mitarbeiter** aus.
  - **Externer Gastgeber**: Wähle diese Option, wenn der Gastgeber nicht in injixo geplant wird.
    {{ 2 | image: 'Gruppentermine ohne Gastgeber', '60%' }}
9. Im Abschnitt *Die Gruppentermine finden statt zwischen* wählst Du die Teilnehmer für die Gruppentermine aus.
    - Optional: Wähle die Option {% link_new **Auswahl** | features/administration/selections.md %} oder **Mitarbeiterfilter** über die Buttons oben aus und wähle rechts ein Element aus dem Dropdown-Menü, um die Liste aller Mitarbeiter zu filtern.
    - Aktiviere die **Checkbox** links neben einem Mitarbeiter, um diesen auszuwählen. Aktiviere die Checkbox oben in der Liste, um alle Mitarbeiter auf einmal aus- oder abzuwählen.
10. Aktiviere **Teile das Meeting in mehrere Termine auf**, wenn Du die Gruppe der Teilnehmer auf Basis ihrer Verfügbarkeit auf mehrere Gruppentermine verteilen möchtest. Verwende dann das Dropdown-Menü **Minimale Anzahl an Teilnehmer pro Zeitfenster**, um die Mindestteilnehmerzahl pro Meeting festzulegen.
    {{ 3 | image: 'Teilnehmer', '60%' }}
11. Um Terminvorschläge für Gruppentermine zu erzeugen, klicke auf *Termine vorschlagen*{:.doc-button} unten auf der Seite. Du gelangst zurück zur Übersichtsseite.

Nachdem die Terminvorschläge erzeugt wurden, musst Du sie {% link_new in den Schichtplan eintragen | features/scheduling/meetings/scheduling-suggestions.md %}.
