---
title: Schichttausch-Anfragen einsehen und genehmigen
product_label:
  - essential
  - advanced
  - enterprise
description: Erfahre, wie du ausstehende Schichttausch-Anfragen einsehen und genehmigen bzw. ablehnen kannst und wie du vergangene Schichttausch-Anfragen einsiehst.
archive_ref: 20210802-de-shift-exchange-overview
redirect_from:
  - de/shift-exchange-overview/
redirect_reason: Updated filename on 19 April 2023
---

In injixo Me können Benutzer mit der Rolle Agent {% link_new ihre Schichten miteinander tauschen | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #schichten-tauschen %}. Außerdem können sie freie Tage miteinander tauschen. Beides ist sowohl am selben Tag als auch an unterschiedlichen Tagen möglich.

So funktioniert der Schichttausch:

1. Ein Mitarbeiter bietet eine Schicht in injixo Me zum Tausch an.
2. Andere Mitarbeiter können die angebotene Schicht sehen und im Gegenzug ihre eigene Schicht anbieten.
3. Der anbietende Mitarbeiter wählt das Gegenangebot aus, das ihm am besten passt.
4. injixo bestätigt die Auswahl automatisch oder erstellt ggf. eine Genehmigungsanfrage.
5. Ein Benutzer mit Admin-Zugriff oder der Rolle Planer prüft den angefragten Tausch, genehmigt ihn oder lehnt ihn ab. Um automatische Genehmigungen zuzulassen, ändere den Wert der Einstellung _48152_{:.id-label} von 0 auf 1.

Um zu erfahren, wie Mitarbeiter Schichten in injixo Me tauschen können, lies {% link_new Tausche Schichten mit deinen Kollegen | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #schichten-tauschen %}.

> Tipp
>
> In injixo Me können Mitarbeiter unter {% link_new Team Kalender | features/injixo-me/set-up-injixo-me/configure-injixo-me.md | #team-kalender %} die Arbeitszeiten ihrer Kollegen einsehen.

## Voraussetzungen

Mitarbeiter mit der Rolle Agent können eine Schicht zum Tausch anbieten, wenn folgendes zutrifft:

- Unter Me ist die Option {% link_new Schichttauschbörse aktiviert | features/injixo-me/set-up-injixo-me/configure-injixo-me.md | #schichttauschbörse %}.
- Alle Aktivitäten in einer Schicht sind als {% link_new Tauschbar beim Schichttausch | features/administration/activity-types-and-properties.md | #aktivitätseigenschaften %} konfiguriert.
- Es gibt eine {% link_new Planperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} mit dem Status Schichtwünsche freigeschaltet, Veröffentlicht oder Abgeschlossen.
- Der Stichtag für die Planperiode ist noch nicht verstrichen.
- Der in der Einstellung _48151_{:.id-label} konfigurierte Wert legt fest, für wie viele Tage ab dem aktuellen Datum kein Schichttausch möglich ist. Wenn du dort z.&nbsp;B. 0 eingibst, können am heutigen Tag und an allen folgenden Tagen Schichten getauscht werden. Wenn du 1 eingibst, können ab dem morgigen Tag Schichten getauscht werden.
- Mitarbeiter haben Lesezugriff auf injixo Me.

## Schichttausch-Anfragen genehmigen oder ablehnen

Nur Benutzer mit Admin-Zugriff oder der Rolle Planer können Schichttausch-Anfragen prüfen, genehmigen und ablehnen.

Um Schichttausch-Anfragen zu prüfen, zu genehmigen oder abzulehnen, gehe wie folgt vor:

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Wähle aus dem Dropdown-Menü _Planungsaktionen_{:.doc-button} die Option **Tauschanfragen genehmigen**.
3. Wähle aus den Dropdown-Menüs eine **Planungseinheit** und optional eine **Auswahl** aus.
4. Wähle einen **Zeitraum**.<br>Wenn du unter _Schedules_{:.menu-item} noch keinen Datumsbereich ausgewählt hast, beginnt der Datumsbereich automatisch am aktuellen Tag und endet sieben Tage später.
5. Aktiviere die Checkboxen neben den Einträgen, die du genehmigen oder ablehnen möchtest. Mit der Checkbox ganz oben wählst du alle Einträge auf einmal aus.
6. Klicke auf _Ausgewählte genehmigen_{:.doc-button} bzw. _Ausgewählte ablehnen_{:.doc-button}.  
   Nachdem die ausstehenden Anträge genehmigt bzw. abgelehnt sind, werden diese in den Tab **Information** verschoben.

Der Report Tauschstatistik unter _WFM > Controlling > Reports_{:.breadcrumbs} zeigt den Status der Schichttausch-Ereignisse (vorgeschlagen, unbearbeitet, abgelehnt und genehmigt) für einen konfigurierbaren Zeitraum an.

## Vergangene Schichttausch-Anfragen einsehen

Auf der Seite **Tauschanfragen genehmigen** zeigt der Tab **Information** an, welcher Mitarbeiter welche Schicht zu welchem Zeitpunkt getauscht hat. Die Liste zeigt genehmigte, abgelehnte und stornierte Anfragen. Weitere Informationen zu stornierten Anfragen erhältst du, wenn du den Mauszeiger über das {% icon info_circle %} bewegst.

## Einstellungen für den Schichttausch

Unter _WFM > Administration > System > Einstellungen_{:.breadcrumbs} gibt es verschiedene Einstellungen, mit denen du den Schichttausch-Prozess für dein Unternehmen anpassen kannst:

- _48151_{:.id-label} _Stichtag für die Tauschbörse_: Anzahl der Tage ab dem aktuellen Datum, für die kein Schichttausch mehr möglich ist (Standard: 3 Tage).
- _48152_{:.id-label} _Austauschmodus_: Lege fest, ob ein Benutzer mit Admin-Zugriff oder der Rolle Planer den Schichttausch zwischen Mitarbeitern genehmigen muss. Standardmäßig ist der Wert 0 für erforderliche Genehmigungen eingestellt. Wähle 1 für den automatischen Tausch ohne Genehmigung.
- _48153_{:.id-label} _Tauschberechtigung_: Erlaube Schichttausch zwischen Mitarbeitern, die derselben Planungseinheit (Wert 0, Standard), derselben Auswahl (Wert 1) oder verschiedenen Planungseinheiten (Wert 2) zugewiesen sind.
- _48555_{:.id-label} _Tauscherlaubnis zwischen Arbeitstagen und freien Tagen_: Erlaube Mitarbeitern, Schichten gegen freie Tage zu tauschen (Standard: 0, nein).
- _48556_{:.id-label} _Tauscherlaubnis zwischen verschiedenen Tagen_: Erlaube Mitarbeitern, Schichten an unterschiedlichen Wochentagen zu tauschen (Standard: 0, nein).
- _48999_{:.id-label} _Überprüfung der Teilaktivitäten von Multiaktivitäten_: injixo überprüft die Qualifikation für jede Teilaktivität in Verbindung mit der Planungsregel 2605, wenn Multiaktivitäten getauscht werden (Standard: 0, keine Überprüfung).

## Warum wird der Schichttausch verhindert?

Mitarbeiter können Schichten sehen und tauschen, die in injixo Me angeboten werden, wenn ihre Tauschanfrage mit den für ihren Vertrag konfigurierten Arbeitszeiten übereinstimmt und wenn sie über die erforderlichen Qualifikationen verfügen.

Um herauszufinden, warum der Tausch in injixo Me verhindert wird, stelle den Tausch im Schicht Center nach. Wenn du die entsprechenden Schichten kopierst und einfügst, zeigt die {% link_new Meldungsanzeige | features/scheduling/shiftcenter/shift-center-overview.md | #meldungsanzeige %} am unteren Bildschirmrand an, welche {% link_new Planungsregel | features/administration/create-contracts.md | #planungsregeln %} dafür sorgt, dass der Schichttausch verhindert wird. Außerdem wird der Grund angezeigt, z.&nbsp;B. falsche Qualifikation oder andere vertragliche Einschränkungen.
