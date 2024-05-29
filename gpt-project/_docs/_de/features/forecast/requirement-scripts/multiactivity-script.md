---
title: Multiaktivitäten
description: Ermittle den Mitarbeiterbedarf für Multiaktivitäten.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /de/requirement-multiactivity/
redirect_reason: Updated filename on 06 March 2024
---

Verwende das Multiaktivitäten-Skript, um den Mitarbeiterbedarf für deine Multiaktivitäten zu berechnen. Die Berechnung erfolgt mit Erlang-C oder auf Basis eines Service-Levels.

## Voraussetzungen

- Erstelle mindestens eine {% link_new Multiaktivität | features/administration/activity-types-and-properties.md | #teilaktivitäten %} und weise sie deiner Planungseinheit zu.
- Erstelle für jede Teilaktivität einer Multiaktivität einen {% link_new Workload | features/forecast/injixo-forecast/create-workloads.md | #workloads-erstellen %}.

## Forecast für alle Workloads von Teilaktivitäten exportieren

Bevor du das Multiaktivitäten-Skript ausführen kannst, exportiere für alle Teilaktivitäten den Forecast für die Workloads:

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} den Workload aus, den du für eine Teilaktivität erstellt hast.
2. Wähle mit der Datumsauswahl den Zeitraum aus. Klicke auf eine Kalenderwoche, um die ganze Woche auszuwählen oder auf einen beliebigen Tag und ziehe dann mit der Maustaste, um einen Zeitraum kürzer oder länger als eine Woche auszuwählen.
3. Klicke oben rechts auf das {% icon ellipsis_v %} und wähle die Option **Forecast verwenden**.
4. Wähle im geöffneten Fenster den Forecast aus, den du verwenden möchtest.
5. Klicke auf _Forecast verwenden_{:.doc-button}.
6. Klicke auf _Schließen_{:.doc-button}.
7. Wiederhole die Schritte 1 bis 6 für alle Workloads für deine Teilaktivitäten.

injixo speichert die Daten, die zur Berechnung des Mitarbeiterbedarfs benötigt werden, in Queues. Du findest diese unter _WFM > Administration > Prognose > Queues_{:.breadcrumbs}. Jede Queue ist genauso benannt wie der dazugehörige Workload. Zusätzlich beginnt ihr Name mit einem Sternchen, z.&nbsp;B. \*deinWorkloadName.

## Skript konfigurieren

1. Gehe zu _Forecast > Bedarfsskripte_{:.breadcrumbs}.
2. Klicke in der Kachel **Anrufe - Multi-Activity** auf _Öffnen_{:.doc-button}.
3. Konfiguriere im Skript-Konfigurationsfenster folgende Einstellungen:
   - Im Abschnitt **Datum**:
     - **Startdatum**: Gib das Startdatum für die Berechnung des Mitarbeiterbedarfs ein.
     - **Anzahl Tage**: Gib die Anzahl der Tage nach dem Startdatum ein, für die du den Mitarbeiterbedarf berechnen möchtest.
   - Im Abschnitt **Planungseinheiten-Parameter**:
     - **Planungseinheit** und **Multiaktivität**:<br>
       Das Skript-Konfigurationsfenster lädt neu und zeigt die Berechnungsparameter für die entsprechenden Teilaktivitäten an.
   - Im Abschnitt **Teilaktivität** kannst du verschiedene Berechnungsparameter für jede Teilaktivität konfigurieren. Beginne mit den Parametern im Abschnitt **Queue-Parameter**:
   - **Berechnungsmethode**: Wähle **Erlang C**, **Linear** oder **Chat** aus.<br>Das Skript-Konfigurationsfenster lädt neu und zeigt die entsprechenden konfigurierbaren Parameter an. Sieh dir die [folgende Tabelle](#berechnungsparameter-im-abschnitt-erlang-c-parameter) an, um zu erfahren, welche Parameter für welche Berechnungsmethode konfigurierbar sind.
   - **Queue**: Wähle die Queue mit den Daten aus, die du für die Berechnung verwenden möchtest.
   - **Vorgänge**: Wähle den Wertetyp des Kontaktvolumens aus, z.&nbsp;B. Anrufe - Eingehende.
   - **Durchschnittliche Vorgangsdauer**: Wenn deine Workloads eine prognostizierte durchschnittliche Bearbeitungszeit (AHT) enthalten, wähle den entsprechenden Wertetyp aus. Wähle ansonsten **[Keine]** aus.
   - **Version**: Wähle **Auto-Forecast** aus. In injixo Enterprise On-premise kannst du eine andere Version auswählen.

## Berechnungsparameter im Abschnitt Erlang C-Parameter

| Parameter                                 | Beschreibung                                                                                                                                                                                                                                                                                      | Konfigurierbar in Erlang-C | Konfigurierbar in Linear | Konfigurierbar in Chat |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------ | ---------------------- |
| Service-Level (%)                         | Prozentsatz der Kontakte, die innerhalb der Zeit bearbeitet werden sollen, die du unter **Service-Level (Sek.)** konfiguriert hast.                                                                                                                                                               | Ja                         | Nein                     | Ja                     |
| Service-Level (Sek.)                      | Zeit, in der der Prozentsatz der Kontakte bearbeitet werden soll, den du unter **Service-Level (%)** konfiguriert hast.                                                                                                                                                                           | Ja                         | Nein                     | Ja                     |
| Aufschlag (%)                             | Der Prozentsatz, um den du den berechneten Mitarbeiterbedarf erhöhen möchtest. Erfahre, wie du [diesen Parameter konfigurierst](#parameter-aufschlag--zum-shrinkage-ausgleich-konfigurieren), um Shrinkage auszugleichen.                                                                         | Ja                         | Ja                       | Ja                     |
| Mindestbedarf                             | Gib einen Wert ein, um einen niedrigeren Mitarbeiterbedarf zu überschreiben.                                                                                                                                                                                                                      | Ja                         | Ja                       | Ja                     |
| Maximalbedarf                             | Gib einen Wert ein, um einen höheren Mitarbeiterbedarf zu überschreiben.                                                                                                                                                                                                                          | Ja                         | Ja                       | Ja                     |
| Konstante durchschnittliche Vorgangsdauer | Wenn du im Abschnitt **Queue-Parameter** beim Parameter **Durchschnittliche Vorgangsdauer** einen Wertetyp ausgewählt hast, behalte hier den Standardwert.<br> Wenn du beim Parameter **Durchschnittliche Vorgangsdauer** die Option **[Keine]** ausgewählt hast, gib einen Wert in Sekunden ein. | Ja                         | Ja                       | Ja                     |
| Seq (%)                                   | Prozentsatz der AHT, den Mitarbeiter für Aufgaben aufwenden, die sie nicht parallel erledigen können, wie zum Beispiel Nachbearbeitungszeit.                                                                                                                                                      | Nein                       | Nein                     | Ja                     |
| Max Sitzungen                             | Maximale Anzahl von parallelen Chats, die ein Mitarbeiter gleichzeitig bearbeiten kann.                                                                                                                                                                                                           | Nein                       | Nein                     | Ja                     |

### Parameter Aufschlag (%) zum Shrinkage-Ausgleich konfigurieren

Um den Parameter **Aufschlag (%)** so zu konfigurieren, dass du damit Shrinkage ausgleichen kannst, verwende die folgende Formel, wobei % für deine Shrinkage-Rate steht: 1/(1-s%)-1. Das Ergebnis wird als Prozentsatz ausgegeben und entspricht dem Wert, den du beim Parameter **Aufschlag (%)** eingeben musst. Um beispielsweise eine Shrinkage von 20% auszugleichen, lautet die Berechnung 1/(1-0.2)-1, was 25% entspricht.

## Skript ausführen

- Um die Berechnung zu starten, klicke auf _OK_{:.doc-button}.<br>Ein Fenster öffnet sich und zeigt die ausgewählten Eingabeparameter und die Ergebnisse des Skripts an. <br>

## Berechnungsergebnisse einsehen

Du kannst den aktualisierten Mitarbeiterbedarf für die ausgewählte Planungseinheit und Multiaktivität unter {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %} oder im Parameterfenster unter {% link_new Schicht Center | features/scheduling/edit-or-delete-staff-requirements.md %} bzw. {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %} einsehen.
