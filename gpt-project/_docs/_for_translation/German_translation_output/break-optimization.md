---
title: Pausen optimieren <!-- DeepL translation -->
product_label:
  - essential
  - advanced
  - enterprise
permalink: /break-optimization/
permalink_reason: /break-optimization/ used in email and in Intercom message
description: Erfahre, wie du die Verteilung der Pausen in deinem Schichtplan optimieren kannst, um die Deckung zu verbessern. <!-- DeepL translation -->
promote-service: schedule-optimization-workshop
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-activity-coverage.md
deepl_translation: true
---

Die Funktionalität **Pausen optimieren** verschiebt Pausen innerhalb deines Schichtplans, um die Deckung der Aktivitäten mit dem Mitarbeiterbedarf zu optimieren.<br> <!-- DeepL translation -->
Die Start- und Endzeiten der Schichten ändern sich nicht. Die Funktionalität **Pausen optimieren** verändert nicht die Pausenkorridore, die du in Tagesmodellen konfiguriert hast, sondern verschiebt die Pausen innerhalb dieser Korridore. Du kannst weitere Pausenoptimierungen durchführen, wenn sich der Mitarbeiterbedarf ändert. <!-- DeepL translation -->

### Wann sollte ich die Pausen optimieren? <!-- DeepL translation -->

Das folgende Beispiel zeigt eine mögliche Situation: <!-- TM 100 -->

Zwei Mitarbeiter haben am selben Tag eine Schichtplanerstellung mit einer Pause von 12&nbsp;PM bis 13&nbsp;PM. Ihre Pausen können zwischen 12 und 15 Uhr alle 30 Minuten beginnen.<br> <!-- DeepL translation -->
Nutze die Pausenoptimierung, um die Deckung für die Aktivitäten des Typs Anwesenheit um die Mittagszeit zu verbessern. Die Pausenoptimierung verschiebt mindestens eine der Pausen auf einen späteren Zeitpunkt, zwischen 12&nbsp;PM und 15&nbsp;PM. <!-- DeepL translation -->

### Voraussetzungen <!-- TM 100 -->

Um die Funktionalität **Pausen optimieren** zu nutzen, müssen die folgenden Bedingungen erfüllt sein: <!-- DeepL translation -->

- Es gibt eine Schichtplanerstellung in der Schichtplanung [Ebene](/glossary/overview/#level). <!-- Link zu den Ebenen hinzufügen, sobald er überarbeitet wurde https://help.injixo.com/tips-on-shift-center-usage#tip-9-working-with-different-levels --> --> <!-- DeepL translation -->
- Dein Schichtplan enthält Aktivitäten des Typs Anwesenheit für die Zeiträume, die du optimieren möchtest. Die Pausenoptimierung ersetzt solche Aktivitäten durch Pausen. <!-- DeepL translation -->
- Deine Tagesmodelle enthalten {% link_new break corridors | features/administration/daymodels/daymodel-creation.md | #add-a-break-activity %}. <!-- DeepL translation -->

## Führe eine Pausenoptimierung durch <!-- DeepL translation -->

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}. <!-- TM 100 -->
2. Wähle aus dem Dropdown-Menü _Planungsaktionen_{:.doc-button} die Option **Tauschanfragen genehmigen**. <!-- TM 73 -->
3. Im Abschnitt **Pausenoptimierung einrichten** konfigurierst du die Pausenoptimierung: <!-- DeepL translation -->

   - **Planungseinheit**: Die Planungseinheit, für die du die Pausenoptimierung durchführen willst. <!-- DeepL translation -->
   - (Optional) **Auswahl** <!-- DeepL translation -->
   - **Datumsbereich**: Du kannst von einem Tag bis zu zwei Monaten in der Zukunft wählen. <!-- DeepL translation -->
   <!-- do NOT explain feature-flag-based *Use Smart Optimization* checkbox-->

4. Klicke auf den _Optimize breaks_{:.doc-button}. <!-- wird nicht als JobProcessor Job behandelt --> <!-- DeepL translation -->

Der Optimierungsprozess kann bis zu 60&nbsp;Minuten dauern. Die Dauer des Prozesses wird von Faktoren wie der Anzahl der Mitarbeiter, der Anzahl der Pausen in der Schichtplanung und der Länge des zu optimierenden Zeitraums beeinflusst. <!-- Die Funktionalität **Pausen optimieren** verwendet die beste Lösung, die während des Optimierungsprozesses gefunden wurde - wie würde sie sonst funktionieren? ist das notwendig? --> <!-- DeepL translation -->
Während des Optimierungsprozesses kannst du den Schichtplan für den betroffenen Datumsbereich nicht bearbeiten.<br>Nach Abschluss der Optimierung speichert injixo die optimierte Planung in der Ebene Schichtplanerstellung<!-- füge den Link zum Artikel Ebenen https://help.injixo.com/tips-on-shift-center-usage#tip-9-working-with-different-levels hinzu, nachdem er aktualisiert wurde --> und aktualisiert den Status im Abschnitt **Pausenoptimierung Verlauf**. <!-- DeepL translation -->

## Verstehe den Optimierungsstatus <!-- DeepL translation -->

Jede Pausenoptimierung erzeugt einen Eintrag in der Tabelle im Abschnitt **Pausenoptimierungsverlauf**. Die Tabelle enthält Angaben über das Startdatum der Optimierung, die Person, die die Optimierung durchgeführt hat, die Planungseinheit, die Auswahl, den Zeitraum und den Status. Wenn das Enddatum einer Optimierung mit dem aktuellen Datum übereinstimmt, wird der Eintrag aus der Liste entfernt. <!-- DeepL translation -->

In der folgenden Tabelle findest du weitere Informationen zu den möglichen Optimierungsstatus: <!-- DeepL translation -->

| Parameter | Beschreibung | <!-- TM 78 -->
| ------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Optimierte Schichtplanung | Die Pausenoptimierung war erfolgreich.          | Die resultierende Schichtplanung wurde auf der Ebene der Schichtplanerstellung gespeichert.                                                | <!-- DeepL translation -->
| Teilweise optimierte Schichtplanung | Die Optimierung konnte nicht alle Pausen optimieren. | Erfahre mehr über diesen Status im [entsprechenden Abschnitt unten](#partly-optimized-schedule).             | <!-- DeepL translation -->
| Optimierung fehlgeschlagen | Die Optimierung konnte nicht gestartet werden.          | Versuche, die Optimierung neu zu starten. Wenn dieser Status weiterhin besteht, erstelle ein Ticket, um mit unserem Support-Team in Kontakt zu treten. | <!-- DeepL translation -->

Optimierten Schichtplan erstellen <!-- TM 66 -->

<!-- Do not change this heading: /break-optimizations#partly-optimized-schedule is used within the break optimization UI -->

Der Status Teilweise optimierter Schichtplan wird angezeigt, wenn die Pausenoptimierung nicht alle Pausen im ausgewählten Zeitraum optimieren konnte. Es gibt drei mögliche Ursachen: <!-- DeepL translation -->

- Bei der Optimierung wurden einige Pausen nicht verschoben, weil sie z.B. Aktivitäten vom Typ Meeting überlagern würden. Die Pausen behalten die Positionen, die sie vor Beginn der Optimierung hatten. <!-- DeepL translation -->
- Bei der Optimierung wurden einige Pausen nicht berücksichtigt, weil sie z.B. kürzer als 5 Minuten sind oder weil sie nicht mit dem {% link_new interval used by the planning unit | features/administration/create-and-manage-planning-units.md | #create-planning-units %} übereinstimmen. <!-- DeepL translation -->
- Bei der Optimierung wurden einige Pausen ignoriert, um {% link_new scheduling rule | features/administration/create-contracts.md | #scheduling-rules %} Verstöße zu verhindern, z.B. die Schichtplanerstellung für eine Aktivität, für die die Person nicht die erforderliche(n) Qualifikation(en) besitzt. <!-- DeepL translation -->

## Berechnungsergebnisse einsehen <!-- TM 77 -->

Um die Details einer abgeschlossenen Pausenoptimierung zu sehen, klicke auf _Ergebnisse_{:.doc-button}. <!-- DeepL translation -->
In dem sich öffnenden Fenster zeigt die Kachel **Status** die Anzahl der optimierten Pausen an.<br> <!-- DeepL translation -->
Ein Diagramm mit zwei Graphen zeigt den Unterschied zwischen der Deckung vor der Pausenoptimierung (dargestellt durch eine gelbe Linie) und der Deckung nach der Pausenoptimierung (dargestellt durch eine grüne Linie).<br> <!-- DeepL translation -->
Die horizontale Achse stellt die Daten des ausgewählten Zeitraums dar.<br> <!-- DeepL translation -->
Die vertikale Achse stellt die Gesamtdeckung für alle geplanten Aktivitäten in der ausgewählten Planungseinheit und/oder Auswahl im ausgewählten Zeitraum dar, ausgedrückt in absoluten Werten. Ein Wert von 5 kann zum Beispiel entweder eine Unterdeckung (5 Mitarbeiter weniger als erforderlich geplant) oder eine Überdeckung (5 Mitarbeiter mehr als erwartet geplant) bedeuten. Um mehr über die Deckung zu erfahren, {% link_new check your schedule in the Schichtplanerstellung | features/scheduling/schedules/schedules-activity-coverage.md %}.<br> <!-- DeepL translation -->

<!-- From this sentence on, we need to change the information about coverage and the graph. "Perfect coverage" is not a term that has any meaning, see: https://ivx.slack.com/archives/C9Y6W10NS/p1691742308844969?thread_ts=1690371315.535319&cid=C9Y6W10NS. The graph label on the y-axis is also very confusing, "coverage - Total deviation from 0. It does not display clearly what is the value in the graph. The deviation is just the absolute value between the real coverage and the optimized coverage. -->

Je näher die grüne Linie bei 0 liegt, desto mehr hat die Pausenoptimierung die Deckung verbessert. <!-- DeepL translation -->

### Wie werden die Diagrammwerte berechnet? <!-- DeepL translation -->

Das folgende Beispiel zeigt eine mögliche Situation: <!-- TM 100 -->

Du planst zwei Aktivitäten in deiner Planungseinheit: Kundenbetreuung und Finanzangelegenheiten. Deine Planungseinheit verwendet ein Intervall von 15&nbsp;Minuten, was vier Intervalle pro Stunde ergibt.<br>Die folgende Tabelle zeigt die Deckungswerte und die Deckung ausgedrückt in absoluten Werten: <!-- DeepL translation -->

<!-- left-align table -->
<style>
table { <!-- TM 100 -->
   margin-left: 0px; <!-- TM 100 -->
}
</style> <!-- TM 100 -->

| Name der Aktivität | Deckungswerte pro Intervall | Deckungswerte absolut pro Intervall | <!-- DeepL translation -->
| ---------------- | ---------------------------- | ------------------------------------- |
| Kundenbetreuung | [0, -2, -1, 0] | [0, 2, 1, 0] | <!-- DeepL translation -->
| Finanzielle Angelegenheiten | [3, 2, -2, 0] | [3, 2, 2, 0] | <!-- DeepL translation -->

Für dieses Beispiel ergeben sich auf der vertikalen Achse die folgenden Werte für die Gesamtdeckung: 3, 4, 3 und 0. <!-- DeepL translation -->

### Anzeige der Intervalle eines Tages <!-- DeepL translation -->

Wenn du einen Zeitraum von bis zu drei Tagen auswählst, zeigt das Diagramm standardmäßig die Intervalle für jeden Tag an.<br> <!-- DeepL translation -->
Wenn du einen Zeitraum von vier Tagen oder mehr auswählst, zeigt das Diagramm die Gesamtwerte für jeden Tag an. Um die Intervalle für einen Tag anzuzeigen, gehst du wie folgt vor: <!-- DeepL translation -->

1. Bewege den Mauszeiger über einen Tag im Diagramm und klicke ihn an. <!-- DeepL translation -->
2. Klicke auf _Tag_{:.doc-button}, um in die Tagesansicht zu wechseln. <!-- TM 68 -->
