---
title: Anzeigen und Genehmigen von Tauschanträgen
product_label:
  - essential
  - advanced
  - enterprise
description: Tauschanträge genehmigen und ablehnen, vergangene Tauschanträge ansehen und die Tauscheinstellungen anpassen.
redirect_from:
  - /de/best-practice-list-past-exchanges/
  - /de/shift-exchange-overview/
redirect_reason: Updated filename on 19 April 2023
archive_ref: 20210816-de-shift-exchange-overview
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
5. Ein Benutzer mit *Admin-Zugriff* oder der Rolle *Planer* prüft den angefragten Tausch, genehmigt ihn oder lehnt ihn ab. Um automatische Genehmigungen zu aktivieren, kannst Du Wert 1 in der Einstellung *48152*{:.id-label} *Austauschmodus* verwenden.

Wenn Du die Einstellung *48152*{:.id-label} *Tauschmodus* änderst, um [automatische Genehmigungen zu aktivieren](#einstellungen-für-den-schichttausch), ist dieser Schritt nicht erforderlich.

Für die Mitarbeiterperspektive lies den Artikel {% link_new injixo Me verwenden | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #schichten-tauschen %}. Tipp: Der {% link_new Teamkalender | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} ermöglicht es Mitarbeitern, die Arbeitszeiten von Kollegen einzusehen und sie zu bitten, Schichten zu tauschen.

## Voraussetzungen

Mitarbeiter können eine Schicht anbieten, wenn:

* das {% link_new Schichttausch-Feature in injixo Me aktiviert ist | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %}.
* alle Aktivitäten der Schicht {% link_new tauschbar | features/administration/activity-types-and-properties.md | #aktivitätseigenschaften %} sind.
* eine {% link_new Planperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #status %} mit dem Status *Schichtwünsche freigeschaltet*, *Veröffentlicht* oder *Abgeschlossen* für den Zeitraum des Schichttausches existiert.
* der für die Planperiode definierte *Stichtag* noch nicht verstrichen ist.
* der in Einstellung *48151*{:.id-label} konfigurierte Wert es erlaubt. Dieser definiert die Anzahl der Tage ab dem aktuellen Tag, an denen ein Schichttausch nicht stattfinden kann. Mit dieser Einstellung stellst Du sicher, dass der aktuelle Schichtplan für diesen Zeitraum nicht mehr verändert werden kann.

## Tauschanträge genehmigen oder ablehnen

Um Schichttausch-Anträge zu prüfen, zu genehmigen oder abzulehnen, führe folgende Schritte aus:

1. Gehe zu *Plan > Schedules*{:.breadcrumbs}.
2. Klicke auf *Planungsaktionen*{:.doc-button}.
3. Wähle **Tauschanfragen genehmigen**.
4. Wähle eine **Planungseinheit**.
5. Optional: Wähle eine **Auswahl**.
6. Wähle einen **Zeitraum**. Hast Du in Schedules noch keinen Zeitraum ausgewählt, wird heute + sieben Tage genutzt.
7. Aktiviere die **Checkboxen** neben den Einträgen, die Du genehmigen oder ablehnen möchtest. Mit der Checkbox ganz oben wählst Du alle Einträge auf einmal aus.
8. Klicke auf *Ausgewählte genehmigen*{:.doc-button} or *Ausgewählte ablehnen*{:.doc-button}. Nachdem die ausstehenden Anträge genehmigt/abgelehnt sind, werden diese in den Tab *Information* verschoben. <!-- check labels -->

Der Report *Tauschstatistik* unter *WFM > Controlling > Reports*{:.breadcrumbs} listet den Status von Tauschanträgen (als *vorgeschlagen*, *noch nicht gestartet*, *abgelehnt* und *genehmigt*) für einen frei definierbaren Zeitraum auf.

## Vergangene Tauschanträge auflisten

Der Tab *Informationen* zeigt, welcher Mitarbeiter wann welche Schicht getauscht hat. Die Liste zeigt genehmigte, abgelehnte und stornierte Anträge. Weitere Informationen zu stornierten Anträgen erhältst Du, wenn Du mit dem Mauszeiger über das Symbol fährst, um einen Text mit zusätzlichen Informationen anzuzeigen. Für diese Anträge ist keine weitere Aktion möglich.

## Einstellungen für den Schichttausch

Unter *WFM > Administration > System > Einstellungen*{:.breadcrumbs} gibt es verschiedene Einstellungen, um den Schichttausch-Prozess an die Bedürfnisse Deines Unternehmens anzupassen:

* *48151*{:.id-label} *Stichtag für die Tauschbörse*: Anzahl der Tage ab dem aktuellen Datum, an denen kein Tausch möglich ist. (Standard: 3 Tage).  
* *48152*{:.id-label} *Tauschmodus*: Lege fest, ob ein Benutzer mit *Admin-Zugriff* oder der Rolle *Planer* den Schichttausch zwischen Mitarbeitern genehmigen muss (Standard: 0). Verwende 0, wenn Du willst, dass Tauschanträge genehmigt werden müssen. Wähle 1 für den automatischen Tausch ohne Genehmigung.
* *48153*{:.id-label} *Tauschberechtigung*: Hier definierst Du, zwischen welchen Mitarbeitergruppen ein Schichttausch möglich ist: Tauschen zwischen Mitarbeitern einer Planungseinheit (Wert 0, Standard), einer Auswahl (Wert 1) oder unterschiedlicher Planungseinheiten (Wert 2, nicht empfohlen).
* *48555*{:.id-label} *Tauscherlaubnis zwischen Arbeitstagen und freien Tagen*: Hier legst Du fest, ob ein freier Tag gegen einen Tag mit Schichten getauscht werden kann (Standard: 0). Verwende 0, wenn ein solcher Tausch nicht möglich sein soll und 1, wenn er erlaubt sein soll.
* *48556*{:.id-label} *Tauscherlaubnis zwischen verschiedenen Tagen*: Erlaube das Tauschen von Schichten zwischen verschiedenen Tagen (1) oder verbiete es (0, Standard).  
* *48999*{:.id-label} *Überprüfung der Teilaktivitäten von Multiaktivitäten*: Aktiviere eine Überprüfung der Qualifikationen von Teilaktivitäten beim Tauschen von Multiaktivitäten (1) oder deaktiviere sie (0, Standard).  

## Was verhindert einen Schichttausch?

Mitarbeiter können angebotene Schichten in injixo Me sehen und tauschen, wenn der Tausch die Regeln des jeweiligen Vertrags erfüllt (vertragliche Arbeitszeit, etc.) und über die gleichen Qualifikationen verfügen.

Um herauszufinden, warum der Tausch in injixo Me verhindert wird, simuliere den Tausch im *Schicht Center*{:.menu-item}. Beim Kopieren und Einfügen der Schichten zeigt die {% link_new Meldungsanzeige | features/scheduling/shiftcenter/shift-center-overview.md | #meldungsanzeige %} am unteren Bildschirmrand die {% link_new Planungsregel | features/administration/create-contracts.md %} und den Grund, z. B. falsche Qualifikationen oder andere vertragliche Beschränkungen.
