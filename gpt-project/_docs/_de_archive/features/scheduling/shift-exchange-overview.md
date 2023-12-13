---
title: Anzeigen und Genehmigen von Tauschanträgen
description: Tauschanträge genehmigen und ablehnen, vergangene Tauschanträge ansehen und die Tauscheinstellungen anpassen.
redirect_reason: deleted article july 2020
archive_ref: 20210816-de-shift-exchange-overview
archived_date: 2021-08-16
---

In diesem Artikel lernst Du:
- was ein Schichttausch ist und wie er funktioniert.
- welche Voraussetzungen für den Schichttausch erfüllt sein müssen.
- wie Du einen Schichttausch genehmigst oder ablehnst.
- wie Du vergangene Tauschanträge auflistest.
- welche Einstellungen sich auf den Schichttausch auswirken.

## Was ist ein Schichttausch?

Mit injixo Me können Mitarbeiter ihre Schichten oder freien Tage untereinander tauschen und zwar sowohl am selben Tag als auch an verschiedenen Tagen.

Der Tauschvorgang in Kürze:
1. In injixo Me bietet ein Mitarbeiter eine Schicht an.
2. Andere Mitarbeiter können die angebotene Schicht sehen und im Gegenzug ihre eigene Schicht anbieten.
3. Der anbietende Mitarbeiter wählt das Gegenangebot aus, das ihm am besten passt.
4. injixo bestätigt die Auswahl automatisch oder erstellt ggf. eine Genehmigungsanfrage.
5. Ein Benutzer mit *Admin-Zugriff* oder der Rolle *Planer* prüft den angefragten Tausch, genehmigt ihn oder lehnt ihn ab. Wenn Du die Einstellung *48152*{:.id-label} *Tauschmodus* änderst, um [automatische Genehmigungen zu aktivieren](#einstellungen-für-den-schichttausch), ist dieser Schritt nicht erforderlich.

Um zu verstehen, wie Mitarbeiter injixo verwenden können, lies den Artikel {% link_new injixo Me verwenden | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #schichten-tauschen %}. 

Tipp: Der {% link_new Teamkalender | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} ermöglicht es Mitarbeitern, die Arbeitszeiten von Kollegen einzusehen und sie zu bitten, Schichten zu tauschen.

## Voraussetzungen

Mitarbeiter können eine Schicht anbieten, wenn:

* das {% link_new Schichttausch-Feature in injixo Me aktiviert ist | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %}.
* alle Aktivitäten der Schicht {% link_new tauschbar | features/administration/activity-types-and-properties.md | #aktivitätseigenschaften %} sind.
* eine {% link_new Planperiode | features/scheduling/planning-periods/what-are-planning-periods.md | #status %} mit dem Status *Freigeben*, *Information* oder *Abgeschlossen* für den Zeitraum des Schichttausches existiert.
* der für die Planperiode definierte *Stichtag* noch nicht verstrichen ist.
* der in Einstellung *48151*{:.id-label} konfigurierte Wert es erlaubt. Dieser definiert die Anzahl der Tage ab dem aktuellen Tag, an denen ein Schichttausch nicht stattfinden kann. Mit dieser Einstellung stellst Du sicher, dass der aktuelle Schichtplan für diesen Zeitraum nicht mehr verändert werden kann.

## Tauschanträge genehmigen oder ablehnen

Um Schichttausch-Anträge zu prüfen, zu genehmigen oder abzulehnen, führe folgende Schritte aus:

1. Gehe zu *WFM > Scheduling > SchedulePro > Tauschübersicht*{:.breadcrumbs}.
2. Wähle ein **Startdatum** und ein **Enddatum**. Der *Stichtag* zeigt das Datum an, bis zu dem kein Tausch stattfinden kann, basierend auf der Einstellung 48151.
3. Wähle eine **Planungseinheit**.
4. Wähle eine **Auswahl** (optional).
5. Aktiviere unter *Optionen* das Feld **Genehmigung**, um offene Tauschanträge aufzulisten, die noch nicht genehmigt oder abgelehnt wurden.
6. Klicke auf *Mitarbeiterliste aufbauen*{:.doc-button}, um die Liste der offenen Tauschanträge anzuzeigen. Die Meldung *Es sind keine Tauschpaare mit Tauschangeboten oder anderen Tauschdaten vorhanden* erscheint, wenn für die ausgewählten Parameter keine Daten verfügbar sind.
7. Aktiviere die **Checkbox** vor einem oder mehreren Einträgen, die Du genehmigen oder ablehnen möchtest.
8. Klicke auf *Genehmigen*{:.doc-button} oder *Ablehnen*{:.doc-button}.

    {{ 3 | image: 'Tauschübersicht in SchedulePro', '80%' }}

Der Report _Tauschstatistik_ unter _WFM > Controlling > Reports_{:.breadcrumbs} listet den Status von Tauschanträgen (als _vorgeschlagen_, _noch nicht gestartet_, _abgelehnt_ und _genehmigt_) für einen frei definierbaren Zeitraum auf.

## Vergangene Tauschanträge auflisten

Um nachzuvollziehen, welcher Mitarbeiter wann welche Schicht getauscht hat, kannst Du die Liste der vergangenen Tauschvorgänge wie folgt einsehen:

1. Gehe zu *WFM > Scheduling > SchedulePro > Tauschübersicht*{:.breadcrumbs}.
2. Wähle ein **Startdatum** und ein **Enddatum**. Der *Stichtag* zeigt das Datum an, bis zu dem kein Tausch stattfinden kann, basierend auf der Einstellung 48151.
3. Wähle eine **Planungseinheit**.
4. Wähle eine **Auswahl** (optional).
5. Aktiviere unter *Optionen* das Feld **Information**.
6. Klicke auf *Mitarbeiterliste aufbauen*{:.doc-button}, um die Liste der vergangenen Tauschanträge anzuzeigen. Die Meldung *Es sind keine Tauschpaare mit Tauschangeboten oder anderen Tauschdaten vorhanden* erscheint, wenn für die ausgewählten Parameter keine Daten verfügbar sind.

Die Liste enthält die folgenden Symbole in der Spalte *Status*:

{{ 1 | image: 'Übersicht über die verschiedenen Tauschsymbole', '60%' }}

## Einstellungen für den Schichttausch

Unter *WFM > Administration > System > Einstellungen*{:.breadcrumbs} gibt es verschiedene Einstellungen, um den Schichttausch-Prozess an die Bedürfnisse Deines Unternehmens anzupassen:

* *48151*{:.id-label} *Stichtag für die Tauschbörse*: Anzahl der Tage ab dem aktuellen Datum, an denen kein Tausch möglich ist. (Standard: 3 Tage).  
* *48152*{:.id-label} *Tauschmodus*: Lege fest, ob ein Benutzer mit *Admin-Zugriff* oder der Rolle *Planer* den Schichttausch zwischen Mitarbeitern genehmigen muss (Standard: 0). Verwende 0, wenn Du willst, dass Tauschanträge genehmigt werden müssen. Wähle 1 für den automatischen Tausch ohne Genehmigung.
* *48153*{:.id-label} *Tauschberechtigung*: Hier definierst Du, zwischen welchen Mitarbeitergruppen ein Schichttausch möglich ist: Tauschen zwischen Mitarbeitern einer Planungseinheit (Wert 0, Standard), einer Auswahl (Wert 1) oder unterschiedlicher Planungseinheiten (Wert 2, nicht empfohlen).
* *48555*{:.id-label} *Tauscherlaubnis zwischen Arbeitstagen und freien Tagen*: Hier legst Du fest, ob ein freier Tag gegen einen Tag mit Schichten getauscht werden kann (Standard: 0). Verwende 0, wenn ein solcher Tausch nicht möglich sein soll und 1, wenn er erlaubt sein soll.
* *48556*{:.id-label} *Tauscherlaubnis zwischen verschiedenen Tagen*: Erlaube das Tauschen von Schichten zwischen verschiedenen Tagen (1) oder verbiete es (0, Standard).  
* *48999*{:.id-label} *Überprüfung der Teilaktivitäten von Multiaktivitäten*: Aktiviere eine Überprüfung der Qualifikationen von Teilaktivitäten beim Tauschen von Multiaktivitäten (1) oder deaktiviere sie (0, Standard).  

## Was verhindert einen Schichttausch?

Mitarbeiter können Schichten tauschen, wenn der Tausch die Regeln der entsprechenden Verträge erfüllt (tägliche Arbeitszeiten, Qualifikationen, Wochentagsarbeitszeiten usw.). Wenn zum Beispiel ein Mitarbeiter eine Schicht in injixo Me anbietet, wird ein anderer Mitarbeiter diese nicht sehen, wenn diese Schicht außerhalb seiner vertraglichen Arbeitszeit liegt. Lerne mehr über {% link_new Planungsregeln | features/administration/create-contracts.md %}.

Wenn Du Dir nicht sicher bist, warum ein Schichttausch nicht stattfinden kann, simuliere den Tausch im *Schicht Center* durch Kopieren und Einfügen der Schichten. Bei einem fehlgeschlagenen Tausch wird in der {% link_new Meldungsanzeige | features/scheduling/shiftcenter/shift-center-overview.md | #meldungsanzeige %} am unteren Bildschirmrand die Planungsregel und der genaue Grund für die Verletzung angezeigt, z. B. falsche Qualifikationen, Arbeitszeiten, etc. Auf diese Weise siehst Du, welche Planungsregeln den Tausch verhindern.
