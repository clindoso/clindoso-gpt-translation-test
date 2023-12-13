---
title: Was ist das Meetings-Modul?
product_label:
  - advanced
  - enterprise
permalink: /de/meetings-overview/
permalink_reason: /de/meetings-overview/ used in email and in Intercom message
description: Plane mit dem Meetings-Modul automatisch 1:1-Meetings, Gruppentermine und Self-learning Sessions für Deine Mitarbeiter.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/scheduling-suggestions.md
---

In diesem Artikel lernst Du:
- wie Du 1:1-Meetings, Gruppentermine und Self-learning Sessions mit dem *Meetings*-Modul planst.
- welche Voraussetzungen erfüllt sein müssen.
- welche Einschränkungen es beim Planen von Meetings gibt.

## Was ist das Meetings-Modul?

Unter *Plan > Meetings*{:.breadcrumbs} kannst Du drei Arten von Meetings für Deine Mitarbeiter planen:
- {% link_new 1:1-Meetings | features/scheduling/meetings/one-on-ones.md %}: plane Einzelgespräche zwischen Mitarbeitern und ihrem Teamleiter
- {% link_new Gruppentermine | features/scheduling/meetings/group-meetings.md %}: plane Meetings für Gruppen von Mitarbeitern mit oder ohne Gastgeber
- {% link_new Self-learning Sessions | features/scheduling/meetings/self-learning-sessions.md %}: plane individuelle Trainingseinheiten für Deine Mitarbeiter

Das Modul *Meetings* spart Dir kostbare Zeit, da Du die Meetings nicht mehr manuell hin- und herschieben musst, bis Du den optimalen Platz im Schichtplan gefunden hast. Die mathematische Optimierung sorgt dafür, dass die Auswirkungen der Meeting-Termine auf die Deckung der bestehenden Aktivitäten minimal ausfallen.

{{ 1 | image: 'Übersichtsseite' }}

## Voraussetzungen und Beschränkungen

Bevor Du beginnst, solltest Du ein paar wichtige Dinge über das *Meetings*-Modul wissen:  

- Das Meetings-Modul benötigt einen bereits existierenden Schichtplan in der Ebene *Plan*.
- Es kann ausschließlich {% link_new Aktivitäten | features/administration/activities.md %} ersetzen, die den Aktivitätstyp *Anwesenheit* haben und als *Ersetzbar* konfiguriert sind.
    - Aktivitäten, die nicht als *Ersetzbar* konfiguriert sind, werden nicht ersetzt.
    - Das Meetings-Modul ändert keine Aktivitäten mit anderen Aktivitätstypen als *Anwesenheit*, selbst wenn diese als *Ersetzbar* konfiguriert sind.
- Es erzeugt keine Terminvorschläge für Mitarbeiter, die nicht zu der Planungseinheit gehören, die bei der Konfiguration der Meetings ausgewählt wurde.
- Es nutzt die Zeitzone der Planungseinheit.
- Es läuft maximal 10 Minuten und nutzt die beste in dieser Zeit gefundene Lösung.


## Vorschläge für Meeting-Termine generieren


1. Gehe zu *Plan > Meetings*{:.breadcrumbs}.
2. Entscheide, welchen Meeting-Typ Du planen möchtest. Du kannst zwischen {% link_new 1:1-Meetings | features/scheduling/meetings/one-on-ones.md %}, {% link_new Gruppenterminen | features/scheduling/meetings/group-meetings.md %} und {% link_new Self-learning Sessions | features/scheduling/meetings/self-learning-sessions.md %} wählen. Klicke in der jeweiligen Karte auf die Schaltfläche **Erstellen**.
3. Konfiguriere die erforderlichen **Parameter** für den ausgewählten Meeting-Typ. Die Parameter unterscheiden sich je nach Meeting-Typ. Klicke oben auf einen der Links, um mehr zur Einrichtung des jeweiligen Meeting-Typs zu erfahren.
4. Klicke auf **Termine vorschlagen**.

## Vorschläge prüfen und in den Schichtplan schreiben

Nachdem Du den Prozess zur Erstellung von Meeting-Vorschlägen gestartet hast, erscheint ein Eintrag in der Tabelle *Generierte Vorschläge*. Er zeigt an, wann der Prozess gestartet wurde, den Meeting-Typ und die ausgewählte Planungseinheit. Der Prozess kann einige Zeit in Anspruch nehmen. Anschließend
1. {% link_new überprüfst Du, ob der Prozess erfolgreich | features/scheduling/meetings/scheduling-suggestions.md | #prüfen-ob-der-prozess-erfolgreich-war %} war,
2. {% link_new siehst Dir die Vorschläge für Meeting-Termine | features/scheduling/meetings/scheduling-suggestions.md | #vorschläge-prüfen-und-übernehmen %} an und schreibst ausgewählte oder alle Vorschläge in den Schichtplan und
3. {% link_new prüfst die Planungsergebnisse | features/scheduling/meetings/scheduling-suggestions.md | #planungsergebnisse-prüfen %}.

Klicke auf die Links, um mehr zu erfahren.
