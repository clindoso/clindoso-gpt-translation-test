---
title: Planungsfehler beheben
toc: true
promote-service: schedule-optimization-workshop
redirect_from:
  - /de/optimization-issues/
  - /de/autoscheduler-scheduling-report-and-errors/
product_label:
  - advanced
  - enterprise
  - classic
description: Identifiziere und behebe typische Planungsfehler bei der Verwendung von automatischen Planungsprozessen.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
---

In diesem Artikel lernst Du:

- wie Du mithilfe des Planungsreports und der Meldungsanzeige im Schicht Center Planungsfehler identifizierst.
- wie Du häufige Planungsfehler behebst.

## Problem-Analyse mit dem Planungsreport

Der _Planungsreport_ ist für automatische Planungsprozesse wie den _Volloptimierten Plan_, die _Joboptimierung_ oder die _Pausenoptimierung_ verfügbar. Er enthält Informationen über Planungsschritte, Warnungen und Fehlermeldungen.

Verwende den Report, um zu prüfen, ob der Planungsprozess für alle Mitarbeiter erfolgreich war und um einen Anhaltspunkt zu haben, wie Probleme zu beheben sind.

Nachdem eine {% link_new Volloptimierung | features/scheduling/schedules/schedules-optimized-schedules.md | #configure-injixo-for-optimal-results | #injixo-konfigurieren-um-optimale-ergebnisse-zu-erzielen %} abgeschlossen ist, findest Du den Planungsreport in injixo Advanced WFM und Enterprise WFM unter _WFM > Administration > System > JobProcessor_{:.breadcrumbs}.

In injixo Classic kannst Du zusätzlich unter _WFM > Scheduling > SchedulePro > Optimierung_{:.breadcrumbs} auf die Reports für die {% link_new verschiedenen Optimierungen | features/scheduling/scheduling-optimization.md %} zugreifen. In injixo Enterprise On-Premise erscheint der Planungsreport automatisch nach dem Speichern des Plans im _AutoScheduler_.

### Was zeigt die Textfarbe an?

- _Schwarzer Text_: Beschreibt die Planungsschritte, die vom automatischen Planungsprozess durchgeführt werden.
- _Blaue Meldungen_: Zeigen an, dass die Soll-Arbeitszeit für einen Mitarbeiter nicht eingehalten werden konnte. Das kann ein Problem sein, muss es aber nicht. Flexible Verträge ermöglichen flexible Wochenarbeitszeiten, indem sie Mindest-, Soll- und Maximalwerte für die Arbeitszeit pro Woche festlegen. Wenn Du flexible Arbeitszeiten nutzt und die Arbeitszeit des Mitarbeiters zwischen den definierten Mindest- und Sollwerten liegt, kann das einfach auf einen geringeren Bedarf hinweisen.
  {{ 4 | image: 'Report mit blauen Warnmeldungen'}}
- _Rote Meldungen_: Zeigen an, dass ein Problem verhindert hat, dass ein Mitarbeiter einen Plan erhält. Details findest Du weiter unten.
  {{ 1 | image: 'Report mit roten Meldungen für Mitarbeiter'}}

## Problem-Analyse mit der Meldungsanzeige

Wenn ein bestimmtes Tagesmodell nicht zugewiesen wurde oder ein Mitarbeiter aus der Optimierung ausgeschlossen wurde, kannst Du über die Meldungsanzeige des Schicht Centers die zugrunde liegende Ursache ermitteln:

1. Drücke **STRG + K**, um die Meldungsanzeige am unteren Rand des Schicht Centers zu einzublenden.
2. Füge das Tagesmodell, das laut Planungsreport von der Optimierung ausgelassen wurde, im Planfenster ein. Möglicherweise erscheint nun ein Pop-up oder eine Meldung in der Meldungsanzeige, die darüber informiert, welche Planungsregel das Hinzufügen der Schicht verhindert. In vielen Fällen ist dies auch die Planungsregel, die das Hinzufügen der Schicht durch den automatischen Planungsprozess verhindert.

Hinweis: Die volloptimierte Planung kann anders funktionieren als das manuelle Einfügen von Schichten, da die {% link_new Konfiguration der Planungsregeln | features/administration/create-contracts.md %} je Benutzer unterschiedlich sein kann.

{{ 2 | image: "Schicht Center mit Hinweis auf Planungsregel" }}

## Konfigurationsfehler beheben

Planungsfehler hängen oft damit zusammen, wie Du injixo konfiguriert hast. Überprüfe die folgenden Einstellungen.

### Mitarbeiter-Einstellungen

Gehe zu _Administration > Scheduling > Mitarbeiter_{:.breadcrumbs} und wähle den zu überprüfenden Mitarbeiter aus:

- Stelle sicher, dass im Abschnitt _Betriebszugehörigkeit_ das _Austrittsdatum_ nicht auf ein Datum in der Vergangenheit gesetzt ist.
- Aktiviere im Abschnitt _Weitere Angaben_ das Kästchen _Schichtzuteilung_.
- Prüfe, ob im Abschnitt _Aktivitäten_ die richtigen Aktivitäten auftauchen. Weise ansonsten weitere Qualifikationen im Abschnitt _Qualifikationsstufen_ hinzu. Die zugehörigen Aktivitäten werden automatisch erstellt.
- Prüfe, ob im Abschnitt _Tagesmodelle_ persönliche Tagesmodelle zugeordnet sind. Diese schränken die Optimierung ein, da falls vorhanden nur diese Tagesmodelle für den Mitarbeiter verwendet werden. Entferne persönliche Tagesmodelle, um für die Optimierung alle Tagesmodelle zu verwenden, die der Planungseinheit zugewiesen wurden.
- Stelle sicher, dass verfügbare Tagesmodelle mit den unter _Verfügbarkeit_ definierten Verfügbarkeitsbeschränkungen des Mitarbeiters zusammenpassen.

### Einstellungen zu Verträgen und Tagesmodellen

- Weise Deiner Planungseinheit alle Tagesmodelle zu, indem Du _[Alle]_ zum Abschnitt _Tagesmodelle_ der Planungseinheit hinzufügst.
- Stelle sicher, dass Du einen {% link_new Mitarbeiterbedarf | features/forecast/injixo-forecast/calculate-staff-requirements.md %} für die Aktivität, die Du planen möchtest, berechnet und gespeichert hast, bevor Du die Optimierung startest.
- Prüfe, ob Du die richtigen {% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %} angelegt hast. Ihre Länge muss zu den Arbeitszeitvorgaben passen, die im {% link_new Vertrag | features/administration/create-contracts.md %} definiert sind. Tagesmodelle geben eine Brutto-Gesamtarbeitszeit an, während Verträge nur die Nettoarbeitszeit zählen. Um die korrekte Nettoarbeitszeit zu erhalten, musst du eventuell Pausen oder andere unbezahlte Tätigkeiten von der Bruttoarbeitszeit abziehen.
- Überprüfe andere Vertragsparameter.

### Weiteres

- Überprüfe die Konfiguration Deiner Planungsregeln unter _WFM > Administration > System > Planungsregeln_{:.breadcrumbs}.
- Stelle sicher, dass nicht bereits Aktivitäten hinzugefügt wurden, die Zeiträume im Schichtplan blockieren. Unbezahlte ganztägige Aktivitäten könnten als Blocker für bestimmte Tage allerdings korrekt sein.
- Stelle sicher, dass die Planungsmodelle Deiner Mitarbeiter die richtigen Tagesmodelle enthalten. Überprüfe dies unter _WFM > Administration > Scheduling > Planungsmodelle_{:.breadcrumbs}.
- Prüfe, ob der Wert für die Arbeitstage pro Woche im Vertrag mit der tatsächlichen Anzahl der Arbeitstage übereinstimmt. Lege bei Bedarf einen niedrigeren Wert für _Mindestanzahl Arbeitstage pro Woche_ im Vertrag fest.
- Überprüfe, ob die Rotation des Mitarbeiter-Planungsmodells, die durch den jeweiligen Typ festgelegt wird, evtl. die Verwendung der korrekten Tagesmodelle verhindert. Dies kann bei {% link_new Planungsmodellen | features/administration/work-time-pattern-models.md %} vom Typ B, C und D der Fall sein.

## Häufige Fehler beheben

- **Der Mitarbeiter hat keinen gültigen Vertrag.**<br>Stelle sicher, dass der Mitarbeiter den richtigen Vertrag zugeordnet hat und dass der Vertrag richtig konfiguriert ist.<br><br>

- **Es sind keine Schichten vorhanden, die den Vertrag einhalten.**<br>Es gibt keine Kombination von Schichten, die zu den im Vertrag definierten Werten im Abschnitt _Arbeitszeitvorgaben_ passt. Dies könnte an einer falschen Länge der Tagesmodelle liegen oder an Verfügbarkeiten, Qualifikationen oder dem Mitarbeiterbedarf.<br><br>

- **Der Mitarbeiter ist für die Planung gesperrt oder er gehört dem Unternehmen noch nicht bzw. nicht mehr an.**<br>Prüfe, ob für den Mitarbeiter in den Mitarbeitereinstellungen im Abschnitt _Planungssperren_ eine Planungssperre vorhanden ist. Stelle außerdem sicher, dass im Abschnitt _Betriebszugehörigkeit_ kein Austrittsdatum gesetzt wurde, das in der Vergangenheit liegt.<br><br>

- **Die Schichtzuteilung ist nicht aktiviert.**<br>Gehe zu _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs}. Klick auf den Mitarbeiter und stell sicher, dass im Abschnitt _Weitere Angaben_ das Häkchen für _Schichtzuteilung_ gesetzt ist.<br><br>

- **Bestehender Planinhalt kann nicht optimiert werden.**<br>Prüfe, ob bereits Schichten oder Aktivitäten im Schichtplan des Mitarbeiters vorhanden sind, die eine Planung verhindern.<br><br>

- **An diesem Tag ist ein Feiertag, der die Zuweisung von Aktivitäten und/oder Schichten nicht erlaubt.**<br>Deaktiviere den Feiertagsmodus in den Einstellungen des jeweiligen {% link_new Tagestyps | features/administration/day-types.md %} oder entferne den Tag aus dem Planungskalender, wenn Du Deine Mitarbeiter an einem Feiertag planen möchtest.<br><br>

- **Dem Mitarbeiter wurde ein Planungsmodell zugewiesen, das keine Wochenmodelle enthält.**<br>Prüfe das Planungsmodell des Mitarbeiters. Weise mindestens ein {% link_new Wochenmodell | features/administration/work-time-pattern-models.md %} zu.<br><br>

- **Der Tag ist durch eine existierende, unbezahlte, ganztägige Aktivität nicht planbar.**<br>Normalerweise nur eine Warnung. Der Mitarbeiter hat eine ganztägige unbezahlte Abwesenheit als Blocker oder _Urlaub_ in seinem Schichtplan.<br><br>

- **Der Vertrag enthält keinen erfüllbaren Wert, um die Wochenarbeitszeiten zu garantieren.**<br>Wochenarbeitszeiten und verfügbare Tagesmodelle müssen zusammen passen. Der Mitarbeiter muss in der Lage sein, seine Wochenarbeitszeit mithilfe der der Planungseinheit zugeordneten Tagesmodelle sowie der Anzahl der Arbeitstage in seinem Vertrag zu erfüllen. Normalerweise kannst Du einfach die Nettoarbeitsstunden für das Tagesmodell mit den maximalen Arbeitstagen pro Woche im Vertrag multiplizieren.<br><br>

- **Teilweise angegebene Wochentagsarbeitszeiten werden nicht unterstützt.**<br>Wenn Du _Wochentagsarbeitszeit_ im Vertrag des Mitarbeiters verwendest, trage für jeden Wochentag einen Wert ein. Nutze 00:00 für Tage, an denen der Mitarbeiter nicht arbeiten soll.<br><br>

- **Die Summe der Wochentagsarbeitszeiten unter- bzw. überschreitet die Mindest- bzw. Maximalwochenarbeitszeit.**<br>Passe die _Wochentagsarbeitszeiten_ oder die Mindest- oder Maximalwochenarbeitszeit im Vertrag des Mitarbeiters an.<br><br>

- **Mindestens ein Tag kann nicht geplant werden, da keine Schicht mit der benötigten Dauer vorhanden ist.**<br>Überprüfe die erwarteten Schichtlängen im Vertrag. Erstelle ein weiteres Tagesmodell, das der benötigten Dauer entspricht.<br><br> <!-- net vs. gros times? -->

- **Es wurden keine gültigen Sollarbeitszeiten definiert.**<br>Definiere gültige Sollarbeitszeiten im Vertrag des Mitarbeiters.<br><br>

- **Die maximale Anzahl aufeinander folgender Arbeitstage (wochenübergreifend) wurde im Vertrag nicht angegeben.**<br>Prüfe den Vertrag des Mitarbeiters und passe den Wert für _Maximale Anzahl aufeinander folgender Arbeitstage_ (2624) an.<br><br>

- **Die freie Zeit zwischen den Einsätzen kann nicht eingehalten werden.**<br>Freie Zeit bezieht sich auf die Ruhezeit zwischen zwei Schichten. Prüfe den Vertrag und passe den Wert für _Ruhezeit zwischen zwei Buchungstagen_ (2601) an.<br><br>
