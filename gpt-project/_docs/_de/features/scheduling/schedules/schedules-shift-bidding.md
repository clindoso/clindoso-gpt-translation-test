---
title: Schichtwunsch-Verfahren einrichten
redirect_from:
  - /de/shift-bidding/
product_label:
  - advanced
  - enterprise
description: Erzeuge Schichten für das Schichtwunsch-Verfahren, lade Mitarbeiter ein, sich diese zu wünschen, führe eine Verlosung durch und veröffentliche den Schichtplan (Schedules).
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/view-approve-shift-swap-requests.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/notifications.md
---

In diesem Artikel lernst Du:

- die Schritte des Schichtwunsch-Verfahrens.
- wie Du Schichten erzeugst.
- wie Du Mitarbeiter einlädst, Wünsche für Schichten abzugeben und eine Verlosung ausführst.
- wie Du verbliebene Schichten zuweist.
- wie Du eine Optimierung des Schichtplans durchführst und den Schichtplan für Deine Mitarbeiter veröffentlichst.

## Wie das Schichtwunsch-Verfahren funktioniert

Das Schichtwunsch-Verfahren erlaubt es Deinen Mitarbeitern sich am Planungsprozess zu beteiligen.

{{ 2 | image: 'Planperioden mit Schicht-Funktionen', '80%' }}

Nachfolgend siehst Du eine Übersicht zum Prozess des Schichtwunsch-Verfahrens. Dieser Artikel bezieht sich auf die Schritte 4 bis 10. Klicke auf die Links für ausführliche Informationen zu den anderen Schritten.

1. Erstelle {% link_new Mitarbeiterbedarf | features/scheduling/edit-or-delete-staff-requirements.md %} mit dem _Forecast_-Modul.
2. (Optional) Wenn Du Schichtfolgen verwendest, füge diese ein. Erfahre mehr über {% link_new Schichtfolgen einfügen | features/scheduling/schedules/schedules-insert-shift-sequences.md %}.
3. Erstelle im Modul _Schedules_ eine {% link_new Planperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #neue-planperiode-anlegen %} mit dem Status _Unveröffentlicht_.
4. Gib für jedes Tagesmodell [Mindest- und Maximalwerte](#lege-fest-welche-schichten-erzeugt-werden) in der Schichtbedarfstabelle ein.
5. [Erzeuge die Schichten](#schichten-erzeugen).
6. Lade Deine Mitarbeiter ein, [Wünsche für Schichten abzugeben](#lade-deine-mitarbeiter-ein-sich-schichten-zu-wünschen) über _injixo Me_.
7. [Verlose](#verlosung-ausführen) die Wünsche der Mitarbeiter.
8. Teile automatisch die [verbliebenen Schichten](#verbliebene-schichten-zuteilen) zu, die nicht von Deinen Mitarbeitern gewünscht wurden.
9. [Optimiere die Aktivitäten und Pausen in Deinem Schichtplan](#schichtwunsch-verfahren-abschließen).
10. [Veröffentliche den Schichtplan für Deine Agenten](#schichtwunsch-verfahren-abschließen).

## Lege fest, welche Schichten erzeugt werden

Bevor Du die Schichten erzeugst, die dann im Schichtwunsch-Verfahren für Deine Mitarbeiter zur Verfügung stehen, lege fest, welche Schichten im Angebot enthalten sein sollen. Du musst diese Anpassungen für jede neue Planperiode vornehmen, bevor Du die Schichterzeugung startest. Wenn dies nicht im Vorfeld passiert, erzeugt der Prozess möglicherweise nicht die richtigen Schichten, um den Mitarbeiterbedarf zu decken.

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Klicke auf _Planperioden_{:.doc-button}.
3. Bewege den Mauszeiger in der Übersicht über eine **Planperiode** und klicke auf _![Kontextmenü Icon](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon} auf der rechten Seite.
4. Wähle _Schichtbedarf_{:.doc-button} im Overflow-Menü. Die Planungseinheit der Planperiode ist vorausgewählt.
5. Gib die **Min**- und **Max**-Werte für jedes Tagesmodell ein und speichere Deine Änderungen. Erfahre, {% link_new welche Werte Du eingeben musst | features/scheduling/schedules/schedules-shift-requirement.md | #benötigte-schichten-in-die-tabelle-eintragen %}.

## Schichten erzeugen

Die Schichterzeugung generiert Schichten für jeden Tag der Planperiode. injixo berücksichtigt vorhandene Schichten im Schichtplan, um die bestmögliche Deckung zu erzeugen.

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Klicke auf _Planperioden_{:.doc-button}.
3. Bewege den Mauszeiger in der Übersicht über eine **Planperiode** und klicke auf _![Kontextmenü Icon](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon} auf der rechten Seite.
4. Klicke auf _Schichten erzeugen_{:.doc-button} im Overflow-Menü.
5. Optional: Passe den Wert für den **Schichterzeugungsbedarf**. Die Prozentzahl, die Du eingibst, entspricht einer der Optionen, die Du unterhalb auswählen kannst:
   - Wenn Du die Option **des Mitarbeiterbedarfs** wählst und einen Wert von 100 % eingibst, deckt injixo den Mitarbeiterbedarf genau zu 100 % ab. Ein Wert größer als 100 % führt zu mehr Schichten als durch den Bedarf vorgegeben. Ein Wert kleiner als 100 % führt zu weniger Schichten (sinnvoll, wenn die Anzahl der verfügbaren Mitarbeiter zu gering ist, um den Bedarf zu decken).
   - Wenn Du die Option **der Stunden laut Vertrag** wählst und 100 % eingibst, stellt injixo sicher, dass alle Mitarbeiter ihre vertraglichen Stunden mit den erzeugten Schichten erreichen können.
6. Klicke auf _Schichten erzeugen_{:.doc-button}, um die Schichterzeugung zu starten. Nach Abschluss kannst Du im JobProcessor unter _WFM > Administration > System > JobProcessor_{:.breadcrumbs} einen Ergebnisbericht aufrufen. Dieser enthält Informationen, Warnungen und Fehler bezüglich der Stammdaten und der Schichterzeugung selbst.

   {{ 3 | image: 'Parameterfenster für die Schichterzeugung', '50%' }}

Hinweis: Im Schicht Center kannst Du das Ergebnis der Schichterzeugung manuell anpassen, indem Du {% link_new die Anzahl der erzeugten Schichten für einen einzelnen Tag änderst | features/scheduling/edit-or-delete-staff-requirements.md %}.

Das Schicht Center stellt Kennzahlen für die Schichterzeugung dar. Du findest sie im {% link_new Kennzahlenfenster | features/scheduling/shiftcenter/shift-center-overview.md | #kennzahlenfenster %} unten auf der Seite:

- _Bedarf_ (im Tab _Tagesmodelle_): Anzahl der erzeugten Schichten für jedes einzelne Tagesmodell
- _Besetzung lt. Schichtbedarf_ (im Tab _Aktivitäten_): Anzahl der erzeugten Schichten mit der ausgewählten Aktivität<!-- Du kannst hier sehen, wie der Mitarbeiterbedarf gedeckt wäre, wenn alle erzeugten Schichten besetzt wären. -->
- _Deckung lt. Schichtbedarf_ (im Tab _Aktivitäten_): Unterschied zwischen erforderlichen und erzeugten Schichten

## Lade Deine Mitarbeiter ein, sich Schichten zu wünschen

Nachdem Du die Schichten erzeugt hast, kannst Du Deine Mitarbeiter einladen, sich diese Schichten zu wünschen:

1. Ändere den Status der {% link_new Planperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #status %} auf _Schichtwünsche freigeschaltet_. Füge optional einen **Stichtag** hinzu, der ein Datum vorgibt, bis zu dem Mitarbeiter Wünsche abgeben können.
2. Die Mitarbeiter haben einen Erst- und einen Zweitwunsch. Mehrere Mitarbeiter können für dieselbe Schicht bieten. Sie sehen auch, wie viele Schichten benötigt werden und wie oft eine bestimmte Schicht bereits gewünscht wurde. So können Deine Mitarbeiter die Wahrscheinlichkeit einschätzen, eine Schicht zu bekommen und ggf. alternative Schichten finden. Hinweis: Mitarbeiter können sich bis zu 100 Tage im Voraus Schichten in injixo Me wünschen.
3. Die abgegebenen Wünsche erscheinen auf der Ebene _Wunsch_ und _Ausweichwunsch_. Du kannst die abgegebenen Schichtwünsche auch in _Schedules_{:.menu-item}-Modul oder im _Schicht Center_{:.menu-item} überprüfen.
4. Nachdem der Zeitraum für die Schichtwünsche vorbei ist, setze die Planperiode zurück auf den Status _Unveröffentlicht_, um den Schichtplan zu bearbeiten. Die Mitarbeiter haben noch keinen Zugriff.

## E-Mail und Browser-Benachrichtigungen

Wenn Du den Status einer Planperiode änderst, werden Deine Mitarbeiter per E-Mail oder Browser-Benachrichtigung darüber informiert, dass sie Schichtpläne sehen und Schichtwünsche abgeben können. Gegenwärtig können Mitarbeiter nur Datumsänderungen sehen. Aktivitätsänderungen werden in den Benachrichtigungen nicht angezeigt.

Um {% link_new Browser-Benachrichtigungen | getting-started/notifications.md %} zu bekommen, müssen Deine Mitarbeiter diese Benachrichtigungen erst in ihrem Browser aktivieren.

Standardmäßig sind sowohl E-Mail- als auch Browser-Benachrichtigungen aktiviert. Um E-Mail- oder Browser-Benachrichtigungen für Deine Mitarbeiter zu deaktivieren, gehe zu _Account > Benachrichtigungen_{:.breadcrumbs}.

## Verlosung ausführen

Plane die Schichtwünsche der Mitarbeiter mithilfe der Verlosung. Dabei werden Wünsche aus den Ebenen _Wunsch_ und _Ausweichwunsch_ in die Ebene _Plan_ kopiert.

> Wenn Du die Schichterzeugung erneut durchführen willst, sichere zunächst alle Schichtwünsche. Eine neue Schichterzeugung löscht alle zuvor abgegebenen Wünsche.

Tipp: Wenn Du möchtest, dass eine bestimmte Gruppe von Mitarbeitern eine höhere Chance hat, die gewünschten Schichten zu bekommen, führe die Verlosung auf der Grundlage von Auswahlen durch. Rotiere die Reihenfolge der Auswahlen in jeder Planperiode, um langfristig eine gerechte Verteilung sicherzustellen. Wähle dazu Mitarbeiter über eine Auswahl aus, bevor Du die Verlosung startest (siehe Schritt 6 unterhalb).

Führen die folgenden Schritte aus, um eine Verlosung durchzuführen:

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Klicke auf _Planperioden_{:.doc-button}.
3. Bewege den Mauszeiger in der Übersicht über eine **Planperiode** und klicke auf _![Kontextmenü Icon](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon} auf der rechten Seite.
4. Klicke auf _Schichten verlosen_{:.doc-button} im Overflow-Menü.
5. Optional: Aktiviere **Durchschnittliche Startzeiten der Schichten berücksichtigen** und gib einen Wert für die **Toleranz** im Format _hh:mm_ ein. Ist die Option nicht aktiviert, können Mitarbeiter Schichten mit zufälligen Startzeiten erhalten. Wenn aktiviert, wird der (durchschnittliche) Schichtbeginn berücksichtigt. Erfahre mehr darüber [wie die Toleranz funktioniert](#die-richtige-toleranz-einstellung-wählen).
6. Wähle einen oder mehrere einzelne Mitarbeiter aus, indem Du die **Checkboxen** neben den Mitarbeiternamen aktivierst. Aktiviere die **Checkbox** ganz oben, um alle Mitarbeiter auszuwählen. Du kannst die Liste auch nach _Auswahlen_ oder _Mitarbeiterfilter_ filtern.
7. Klicke auf _Schichten verlosen_{:.doc-button}. Nach Abschluss kannst Du im JobProcessor unter _WFM > Administration > System > JobProcessor_{:.breadcrumbs} das _Verlosungprotokoll_ aufrufen. Es enthält die Gründe für die Ablehnung von Erst- und Zweitwünschen, die Tages- und Gesamtquote pro Mitarbeiter in % und die Gesamtquote in % für alle Mitarbeiter.

   {{ 4 | image: 'Parameter-Fenster Verlosung', '45%' }}

## Verbliebene Schichten zuteilen

Nachdem die Verlosung Deinen Mitarbeitern Schichten zugewiesen und in den Schichtplan geschrieben hat, gibt es oft einige Schichten, die noch zugewiesen werden müssen. Dies sind typischerweise Schichten, die von keinem Mitarbeiter gewünscht wurden. Sie werden automatisch den Mitarbeitern zugewiesen, die keine oder nur wenige Schichten erhalten haben.

Hinweis: Der Schichtplan kann trotzdem unvollständig bleiben, wenn Du nicht genügend Mitarbeiter hast oder Mitarbeiter bestimmte Schichten aufgrund fehlender Qualifikationen oder Planungsregel-Verletzungen nicht ausführen können.

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Klicke auf _Planperioden_{:.doc-button}.
3. Bewege den Mauszeiger in der Übersicht über eine **Planperiode** und klicke auf _![Kontextmenü Icon](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon} auf der rechten Seite.
4. Klicke auf _Schichten zuteilen_{:.doc-button} im Overflow-Menü.
5. Optional: Aktiviere **Durchschnittliche Startzeiten der Schichten berücksichtigen** und gib einen Wert für die **Toleranz** im Format _hh:mm_ ein. Ist die Option nicht aktiviert, können Mitarbeiter Schichten mit zufälligen Startzeiten erhalten. Wenn aktiviert, wird der (durchschnittliche) Schichtbeginn berücksichtigt. Erfahre mehr darüber [wie die Toleranz funktioniert](#die-richtige-toleranz-einstellung-wählen).
6. Wähle einen oder mehrere einzelne Mitarbeiter aus, indem Du die **Checkboxen** neben den Mitarbeiternamen aktivierst. Aktiviere die **Checkbox** ganz oben, um alle Mitarbeiter auszuwählen. Du kannst die Liste auch nach _Auswahlen_ oder _Mitarbeiterfilter_ filtern.
7. Klicke auf _Schichten zuteilen_{:.doc-button}, um die Zuteilung zu starten. Nach Abschluss kannst Du im JobProcessor unter _WFM > Administration > System > JobProcessor_{:.breadcrumbs} einen Ergebnisbericht für die Zuteilung aufrufen. Er listet zugewiesene und nicht zugewiesene Schichten auf.
   {{ 5 | image: 'Parameterfenster Schichten zuteilen', '45%' }}

Tipp: Anstelle der Zuteilung-Schritts kannst Du auch einen direkt einen {% link_new Optimierten Schichtplan erstellen | features/scheduling/schedules/schedules-optimized-schedules.md %}, um den Mitarbeitern, die noch nicht genug Schichten haben, diese zuzuweisen. Dieses Feature optimiert die Pausenpositionen und ersetzt als _Ersetzbar_ konfigurierte Aktivitäten durch _Planbare_ Aktivitäten, für die Mitarbeiterbedarf besteht.

### Die richtige Toleranz-Einstellung wählen

Die Berechnung der Schicht-Startzeit auf Basis des _Toleranz_-Wertes funktioniert unterschiedlich, je nachdem, ob bereits Schichten im Schichtplan vorhanden sind oder nicht (z. B. aus Schichtfolgen):

- Mit Schichten: injixo ermittelt eine durchschnittliche Startzeit der Schicht und weist dann Schichten innerhalb der Toleranzzeit zu. Wenn vorhandene Schichten um 8:00 und 12:00 Uhr beginnen, ist der Durchschnitt 10:00. Wenn Du den Wert für die Toleranz auf 1 Stunde setzt, können die anderen Schichten zwischen 9:00 und 11:00 beginnen.
- Ohne Schichten: Die erste zugewiesene Schicht bestimmt die Startzeit der Schicht. Wenn z. B. die erste Schicht um 9:00 Uhr beginnt und Du den Wert für die Toleranz auf 1 Stunde setzt, beginnen die anderen Schichten zwischen 8:00 und 10:00.

## Schichtwunsch-Verfahren abschließen

Um die Pausenpositionen und Aktivitäten im Schichtplan zu optimieren, führe eine {% link_new Joboptimierung | features/scheduling/schedules/schedules-job-optimization.md %} für den Zeitraum aus, der von Deiner Planperiode abgedeckt wird. Die Joboptimierung ersetzt die Basisaktivität _Anwesend_ und andere _Ersetzbare_ Aktivitäten durch _Planbare_ Aktivitäten basierend auf ihrem Mitarbeiterbedarf.

Um den {% link_new Schichtplan zu veröffentlichen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} und den Agenten zu ermöglichen Schichten zu tauschen, setze den Status der {% link_new Planperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #status %} auf _Veröffentlicht_. Wenn Du die Option {% link_new Schichttausch | features/scheduling/view-approve-shift-swap-requests.md %} konfiguriert hast, können Mitarbeiter jetzt ihren eigenen Schichtplan einsehen und Schichten {% link_new mit anderen tauschen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.
