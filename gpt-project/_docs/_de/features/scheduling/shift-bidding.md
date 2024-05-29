---
title: Schichtwunsch-Verfahren einrichten
description: Setze die Schichterzeugung, Verlosung und Zuteilung ein, um Deine Mitarbeiter am Planungsprozess zu beteiligen und ihre Zufriedenheit zu steigern (SchedulePro).
promote-service: new-planner-training
product_label:
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/what-are-planning-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shift-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/view-approve-shift-swap-requests.md
---

Mit dem Schichtwunsch-Verfahren ermöglichst Du Deinen Mitarbeitern, sich aktiv in den Planungsprozess einzubringen.

Das Wichtigste in Kürze:

- Du erzeugst auf Grundlage des {% link_new Mitarbeiterbedarfs | features/scheduling/edit-or-delete-staff-requirements.md %} und eines {% link_new Schichtbedarfs | features/scheduling/shift-requirement.md %} Schichten.
- Dann wünschen sich die Mitarbeiter in _injixo Me_{:.menu-item} die erzeugten Schichten.
- Du verlost die gewünschten Schichten.
- Nicht gewünschte, z.B. unbeliebte Schichten, werden zugeteilt.

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Wenn Du injixo Advanced WFM oder Enterprise WFM verwendest, nutze für das {% link_new Schichtwunsch-Verfahren | features/scheduling/schedules/schedules-shift-bidding.md %} stattdessen Planperioden unter _Plan > Schedules_{:.breadcrumbs}.

Gesamtprozesses:

- [Workflow Schichtwunsch-Verfahren](/assets/img/{{ page.lang }}/features/shift-bidding/image-1.png)

Zu beachten:

- Der Prozess funktioniert mit Planperioden des Typs _Standard_.
- Der Status der Planperiode steuert die Sichtbarkeit der Daten für die Mitarbeiter.
- Die Verlosung von Schichten kann mit der volloptimierten Planung kombiniert werden.

## Erzeugen, Verlosen, Zuteilen über Planperioden

In _WFM > Scheduling > SchedulePro > Planperioden_{:.breadcrumbs} steht nach dem Auswählen einer Planperiode auf der rechten Seite der Navigationsblock **Schichten** zur Verfügung:

{{ 2 | image: 'Planperioden mit Funktionen zu Schichten'}}

## Vorbereitung

Die für den Prozess benötigten Menüpunkte befinden sich alle in _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.

1. Überprüfe, ob {% link_new Mitarbeiterbedarf | features/scheduling/edit-or-delete-staff-requirements.md %} vorhanden ist. Dieser ist neben dem Schichtbedarf die Grundlage für die Schichterzeugung.

2. (Optional) Wenn Du Schichtfolgen verwendest, füge diese ein. Erfahre mehr über {% link_new Schichtfolgen einfügen | features/scheduling/schedules/schedules-insert-shift-sequences.md %}.

3. Du benötigst eine {% link_new Planperiode | features/scheduling/planning-periods/what-are-planning-periods.md %} vom Typ _Standard_ mit dem Status _[Gesperrt]_. Die Daten der Planung sind so (noch) nicht für die Mitarbeiter einsehbar. So kannst Du auch im Vorfeld schon die Planperioden für mehrere zukünftige Planungen vorbereiten.

4. Du benötigst {% link_new Schichtbedarf | features/scheduling/shift-requirement.md %}, um Schichten zum Wünschen erzeugen zu können. Prüfe in der Ebene _Plan_ eingetragene Urlaube und sonstige Abwesenheiten im anstehenden Planungszeitraum und aktualisiere die Tabelle vor jeder Schichterzeugung, sodass kein Überangebot an Schichten erzeugt wird.

Hinweise zum Schichtbedarf:

- Bearbeitest Du den Schichtbedarf nicht korrekt oder gar nicht, kann es passieren, dass ein Teil der Mitarbeiter nicht geplant wird. Ohne Einschränkungen kann es beispielsweise dazu kommen, dass injixo nur Teilzeitschichten erzeugt, da diese den Bedarf am besten abdecken können.
- Um das Generieren von Schichten auf die Öffnungszeiten der Planungseinheit zu beschränken, stelle sicher, dass kein Mitarbeiterbedarf außerhalb der Geschäftszeiten besteht. Gib Nullen für Tage ein, an denen die Planungseinheit geschlossen ist (z.B. Feiertage).
- Je flexibler die Arbeitsverträge Deiner Mitarbeiter gestaltet sind, desto aufwendiger wird die Bearbeitung des Schichtbedarfs. Daher ist unsere Empfehlung - evtl. auf Kosten der Flexibilität Deiner Planung - nur eine begrenzte Anzahl von Tagesmodellen für Vollzeit- und Teilzeit-Mitarbeiter einzusetzen. Optimal ist ein Mix aus kurzen und langen flexiblen Schichten, um so die vertraglich vereinbarte Arbeitszeit zu erreichen.
- Um größtmögliche Flexibilität in der Planung zu haben, nutze _Anwesend_ als {% link_new Basisaktivität Deiner Tagesmodelle | features/administration/daymodels/daymodel-basics.md | #basisaktivität-und-schichtdauer %}.

## Schichten zum Wünschen erzeugen

Die Schichterzeugung generiert für jeden Tag der Planperiode Schichten und versucht, eine möglichst gute Deckung der Bedarfskurve zu erreichen. Bereits im Schichtplan vorhandene Schichten werden dabei berücksichtigt.

1. Wähle eine Planperiode vom Typ _Standard_ in der Übersicht aus.
2. Klicke im Bereich Schichten auf _Erzeugen_{:.doc-button}.
3. Das Fenster mit den Parametern für die Schichterzeugung öffnet sich:
   {{ 3 | image: 'Parameter-Fenster für die Schichterzeugung', '50%' }}
4. Passe optional die folgenden Parameter an:
   - Das voreingestellte **Startdatum**/**Enddatum** der Planperiode.
   - Den Wert für den **Schichterzeugungsbedarf**. Ein Wert über 100 % erzeugt entsprechend mehr Schichten als vom Bedarf vorgegeben. Ein Wert unter 100 % kann erforderlich sein, wenn die Personalkapazität zu niedrig ist, um den Bedarf zu decken.
   - Die Optionen **des Mitarbeiterbedarfs** und **der Stunden laut Vertrag**. Diese legen fest, ob der Bedarf auf Grundlage des Mitarbeiterbedarfs oder der Stunden laut Vertrag erreicht werden soll.
5. Klicke auf _Ok_{:.doc-button}, um die Schichterzeugung zu starten.

Aktiviere die Option _Jobergebnis nach Abschluss anzeigen_{:.menu-item}, um den **Planungsreport** zu erzeugen. Dieser enthält grundlegenden Informationen, Warnungen und Fehler zu den eingelesenen Daten und zur Schichterzeugung selbst (Laufzeit, Schreiben der Bedarfsdaten, Verstöße gegen Planungsregeln).
Der Fortschrittsbalken im Jobverarbeitungsdialog zeigt den Verlauf der Schichterzeugung an. Du kannst auch den _Dialog schließen_{:.doc-button}; die Schichterzeugung läuft im Hintergrund weiter. Während der Prozess läuft, sind die Plandaten im Optimierungszeitraum geschützt. Es können währenddessen keine Planänderungen vorgenommen werden.

## Schichtwunsch Deiner Agenten

Ändere den Status der {% link_new Planperiode | features/scheduling/planning-periods/what-are-planning-periods.md %} in _Freigegeben_, damit die erzeugten Schichten für Deine Mitarbeiter sichtbar und wünschbar sind.
Die Mitarbeiter haben jeweils einen Normalwunsch und einen Ausweichwunsch zur Verfügung. Mehrere Mitarbeiter können sich die gleiche Schicht wünschen. Dabei sehen sie, wie viele Schichten benötigt werden und wie oft eine bestimmte Schicht bereits gewünscht wurde. So können sie selbst abschätzen, wie hoch die Wahrscheinlichkeit ist, dass sie eine Schicht bekommen und sich ggf. Ausweichschichten suchen.
Während der Verlosungsphase wird immer zuerst geprüft, ob der Normalwunsch erfüllt werden kann.
Definiere einen Stichtag in Deiner Planperiode, um den Zeitraum festzulegen, in dem Deine Mitarbeiter Wünsche eintragen können.
Die abgegebenen Wünsche tauchen in der Ebene Wunsch und Ausweichwunsch in _Schedules_{:.menu-item} bzw. im _Schicht Center_{:.menu-item} auf.

## Erzeugte Schichten planen

Setze die Planperiode nach dem Stichtag wieder auf den Status _[Gesperrt]_, damit Du den Schichtplan bearbeiten kannst, ohne dass Deine Mitarbeiter bereits Einsicht erhalten.

### Verlosung gewünschter Schichten

Starte die Verlosung:

1. Wähle die **Planperiode** in der Übersicht aus.
2. Klicke auf _Verlosen_{:.doc-button} im Bereich Schichten.
3. Wähle die [gewünschten Parameter](#parameter-für-verlosung-und-zuteilung) im erscheinenden Fenster aus.
4. Klicke auf _Ok_{:.doc-button}, um die Verlosung zu starten.

Aktiviere bei Bedarf das Kontrollkästchen **Verlosungsprotokoll erzeugen**. Dieser Report enthält die gewählten Parameter (Benutzername, Planungseinheit, Startdatum und Enddatum), Informationen zu Mitarbeitern (Personalnummer, Richtzeitkonto, Arbeitszeitkonto) und zu verlosten Schichten und Ablehnungsgründen für Normalwünsche/Ausweichwünsche. Zusätzlich enthalten sind die Ergebnisse der Verlosung von Normal- und Ausweichwünschen und die Tages- und Gesamtquoten pro Mitarbeiter in % und die Gesamtquote in % für alle Mitarbeiter.

Mit der Verlosung verteilst Du die gewünschten Schichten auf die Mitarbeiter. Normal- und Ausweichwünsche aus der Ebene _Wunsch_ und der Ebene _Ausweichwunsch_ werden dabei in die Ebene _Plan_ kopiert.

> Hinweis
>
> Eine erneute Schichterzeugung löscht bereits abgegebene Wünsche.

Für eine faire Vergabe verlose optional Mitarbeitergruppen über Auswahlen nacheinander. Wenn Du die Verlosung in jeder Planung über die Auswahlen rotieren lässt, kannst Du gewährleisten, dass immer eine Gruppe bevorzugt wird und somit eine höhere Chance hat, die gewünschten Schichten zu erhalten. <!-- add correct explation for Tages- und Gesamtquoten if requested -->

### Zuteilung übrig gebliebener Schichten

Starte die Zuteilung:

1. Wähle die **Planperiode** in der Übersicht aus.
2. Klicke auf _Zuteilen_{:.doc-button} im Bereich Schichten.
3. Wähle die [gewünschten Parameter](#parameter-für-verlosung-und-zuteilung) im erscheinenden Fenster aus.
4. Klicke auf _Ok_{:.doc-button}, um die Zuteilung zu starten.

Aktiviere bei Bedarf das Kontrollkästchen **Zuteilungsprotokoll erzeugen**. Der Report enthält die gewählten Parameter (Benutzername, Planungseinheit, Startdatum und Enddatum), Informationen zu Mitarbeitern (Personalnummer, Richtzeitkonto, Arbeitszeitkonto) und zu zugeteilten Schichten und Ablehnungsgründen.

Die Zuteilung ordnet Mitarbeitern zufällig Schichten zu, für die es keine oder zu wenige Anmeldungen in _injixo Me_{:.menu-item} gab.
Sind zu wenige Mitarbeiter vorhanden, bleiben diese Schichten unbesetzt. Können Mitarbeiter bestimmte Schichten aufgrund von Aktivitäten oder Schichtlänge nicht ausführen, bleibt der Schichtplan unter Umständen unvollständig. Prüfe daher das Zuteilungsprotokoll und den Schichtplan nach der Zuteilung.

### Parameter für Verlosung und Zuteilung

Die beiden Eingabefenster für Parameter der Verlosung und Zuteilung enthalten im Prinzip die gleichen Felder, hier das Fenster für die Verlosung:

{{ 4 | image: 'Parameter Fenster Verlosung', '65%' }}

Du hast folgende Optionen:

- Wähle _Alle_ Mitarbeiter, eine oder mehrere _Auswahlgruppen_ oder einzelne _Mitarbeiter_
- Ändere das Start- oder Enddatum.
- Erzeuge ein Protokoll im PDF-Format.
- Aktiviere die Beachtung eines Zeitkorridors für den Beginn der Schicht. Gib die **Toleranz** im Format HH:MM ein. In diesem Zeitraum dürfen die Schichten vom durchschnittlichen Schichtbeginn abweichen.

Der Zeitkorridor für die **Toleranz** verhält sich unterschiedlich, je nachdem ob bereits Schichten vorhanden sind oder nicht:

| Fall           | Berechnung                                                                                                                                                                                                                                                                                                                             |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ohne Schichten | Der Zeitkorridor wird nach der Vergabe der ersten Schicht für alle weiteren Schichten beachtet.<br>Wenn die erste Schicht um 9 Uhr beginnt und Du eine Toleranz von 1 Stunde einstellst, beginnen alle weiteren Schichten zwischen 8 und 10 Uhr.                                                                                       |
| Mit Schichten  | Ein durchschnittlicher Schichtbeginn wird ermittelt. Dieser ist dann ausschlaggebend für die Vergabe innerhalb des Zeitkorridors.<br>Wenn bereits Schichten mit Beginn um 8 Uhr und um 12 Uhr geplant sind, wird als Mittelwert 10 Uhr genutzt. Alle weiteren Schichten starten bei einer Toleranz von 1 Stunde zwischen 9 und 11 Uhr. |

## Ersetze Anwesend in Schichten mit der Joboptimierung

Führe die {% link_new Joboptimierung | features/scheduling/scheduling-optimization.md | #was-ist-die-joboptimierung %} aus, wenn Deine Schichten noch nicht die finalen Aktivitäten enthalten. Dadurch wird die als Platzhalter fungierende Aktivität _Anwesend_ (aber auch andere ersetzbare Aktivitäten) durch planbare Aktivitäten ersetzt, für die Mitarbeiterbedarf vorhanden ist.

## Veröffentliche den Schichtplan und ermögliche das Tauschen von Schichten

Setze den Status der {% link_new Planperiode | features/scheduling/planning-periods/what-are-planning-periods.md %} auf _Information_, damit Deine Mitarbeiter die Schichtpläne einsehen können. Wenn Du den {% link_new Schichttausch | features/scheduling/view-approve-shift-swap-requests.md %} konfiguriert hast, können Deine Mitarbeiter nun Schichten untereinander tauschen.

## Kombinierter Planungsansatz

Du kannst die Schichterzeugung in Kombination mit der volloptimierten Planung nutzen. Dabei erzeugst Du nur eine bestimmte Anzahl der insgesamt benötigten Schichten, z.B. 50% und lässt Deine Mitarbeiter die Schichten wünschen. Die Schichten werden verlost. Anstelle der Zuteilung nutzt Du dann die volloptimierte Planung, um die weiteren Schichten zu planen.
