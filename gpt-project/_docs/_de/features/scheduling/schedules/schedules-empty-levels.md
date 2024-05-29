---
title: Schichtpläne löschen
product_label:
  - advanced
  - enterprise
description: Lösche Schichtpläne in einer oder mehreren Ebenen für einen bestimmten Datumsbereich (Schedules-Modul).
toc: false
---

In diesem Artikel lernst Du, wie Du:

- Schichtpläne (Aktivitäten und Tagesmodelle) aus einer oder mehreren Ebenen für einen bestimmten Datumsbereich löschst.
- nur Daten für bestimmte Mitarbeiter löschst.

Die Anleitung bezieht sich auf _Plan > Schedules_{:.breadcrumbs}.

## Schichtpläne für einen bestimmten Datumsbereich löschen

> Sei vorsichtig beim Einstellen der Parameter - das Löschen eines Schichtplans kann nicht rückgängig gemacht werden.

> Lösche keine Urlaubs- und Abwesenheitsanfragen
>
> Genehmigte {% link_new Abwesenheits-Anfragen | features/scheduling/time-off/vacation-absences-management.md %} werden ausschließlich in der Ebene _Plan_ gespeichert. Wenn Du bereits Anfragen genehmigt hast, dann lösche Deinen Schichtplan nicht wie hier beschrieben. Denn dann würdest Du auch die bereits genehmigten Abwesenheitsanfragen im gewählten Zeitraum löschen. Lösche stattdessen die Schichten von Hand.

So löschst Du den Inhalt einer Ebene in _Plan > Schedules_{:.breadcrumbs}:

1. Klicke auf _Planungsaktionen_{:.doc-button}.
2. Wähle **Ebenen leeren**.
3. Wähle unter _Einstellungen_ eine **Planungseinheit**.
4. Ändere den **Zeitraum** (optional). Der Zeitraum ist auf den aktuell in _Schedules_ ausgewählten Zeitraum voreingestellt.
5. Kreuze bei **Zu leerende Ebene(n)** ein oder mehrere Kästchen an, um die Ebenen auszuwählen, in denen Du Daten löschen möchtest.
6. Setze unter _Mitarbeiter_ ein Häkchen bei denjenigen **Mitarbeitern**, für die Du Schichtpläne löschen willst. Du kannst auch eine Auswahl oder einen Mitarbeiterfilter im Dropdown-Menü auswählen.
7. Um das Löschen zu starten, klicke auf _Ebenen leeren_{:.doc-button}. Das Löschen kann einige Zeit in Anspruch nehmen. Du kannst auf den Link **JobProcessor** unten rechts klicken, bevor Du den Job startest, um den Fortschritt zu verfolgen. Klicke oben auf _![Zurück-Schaltfläche](/assets/img/common/injixo-ui/back.png)_{:.doc-button-icon} oder unten auf _Abbrechen_{:.doc-button}, um zu _Schedules_ zurückzukehren, ohne den Job auszuführen.

{{ 1 | image: 'Ebenen leeren Dialog', '80%' }}

Nachdem Du den Job für das Löschen gestartet hast, öffnet sich wieder das Schedules-Modul. Eine grüne oder rote Benachrichtigung am oberen Rand zeigt an, ob der Job erfolgreich gestartet werden konnte oder nicht.
