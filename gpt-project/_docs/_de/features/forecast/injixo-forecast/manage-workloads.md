---
title: Workloads erstellen
redirect_from:
  - /de/workloads/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erstelle Workloads, um historische und prognostizierte Kontaktvolumen und AHT darzustellen. Erfahre mehr über die verschiedenen Arten von Workloads.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
---

Um Workloads zu erstellen, zu bearbeiten oder zu löschen, gehe zu _Forecast_{:.breadcrumbs}.

Workloads bilden die Eingangskanäle deines externen Systems ab, das die Details deiner Kundeninteraktionen erfasst. injixo Forecast berechnet auf der Grundlage der importierten Kontaktdaten, die in Queues gespeichert werden, einen Forecast für den Workload. Konfigurierbare Ereignisse, Feiertage oder Geschäftszeiten beeinflussen, wie der Forecast ausfällt. Du kannst {% link_new den Forecast auch in Workloads importieren | features/forecast/injixo-forecast/import-forecast.md %}.

In Workloads konfigurierst du, wie der Mitarbeiterbedarf ermittelt wird. Der Mitarbeiterbedarf wird für die Schichtplanung benötigt.

Neu bei injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Voraussetzungen

- Füge eine {% link_new native oder eine CSV-Integration | features/acd-integration/cloud/how-integrations-work.md %} hinzu und importiere historische Daten für mindestens eine Queue.
- Importiere eingehende Kontakte, durchschnittliche Bearbeitungszeit (AHT) und bearbeitete Kontakte. Workloads mit mehreren Queues benötigen die bearbeiteten Kontakte, um die AHT anzuzeigen und gewichtete Durchschnittswerte zu berechnen.

injixo erstellt Queues aus den Daten, die von einer Integration importiert werden. Das Intervall für den Datenimport bestimmt das Intervall der Queues, die aus diesen Daten erstellt werden. Du kannst einem Workload nur Queues mit demselben Intervall hinzufügen.

## Queues und Kanäle

Von einer Integration importierte Kontaktdaten werden in Queues gespeichert. Diese Queues sind immer mit einem Kanal verbunden. Wenn du [Workloads erstellst](#workloads-erstellen), kannst du Queues nach Kanal filtern, um sie dem Workload hinzuzufügen. Native Integrationen legen den Kanal für Queues automatisch fest. Nicht alle Integrationen unterstützen alle Kanäle.
Bei einer CSV-Integration musst du den Kanal manuell festlegen. Du kannst einen Kanal pro Spalte hinzufügen oder einen Kanal für die Datei auswählen, wenn du {% link_new die Spalten einer CSV-Datei zuordnest | features/acd-integration/cloud/add-csv-integration.md | #spalten-zuordnen %}.

Integrationen unterstützen die folgenden Kanäle:

- Anrufe
- Chats
- E-Mails
- Tickets
- Dokumente
- Social Media

injixo Forecast gruppiert Queues nach Kanal. Du kannst einem Workload nur Queues mit demselben Kanal hinzufügen.

<!-- anchor for intercom forecast tour -->

## Workloads erstellen

Erstelle einen Workload für jede Aktivität mit Mitarbeiterbedarf, die du planen möchtest. Für Multiaktivitäten benötigst du einen Workload für die Multiaktivität und je einen Workload pro Teilaktivität.

1. Klicke unter _Forecast > Workloads_{:.breadcrumbs} oberhalb der Liste auf _Neuer Workload_{:.doc-button}.
2. Gib die allgemeinen Informationen für deinen Workload ein:

   - **Name**: Ein eindeutiger Name, mit dem du deinen Workload identifizieren kannst.
   - **Zeitzone**: Die {% link_new Zeitzone | best-practices/working-with-timezones.md %} für den Workload kann später nicht mehr bearbeitet werden.

     > Hinweis
     >
     > - Um Mitarbeiterbedarf für eine Planungseinheit zu speichern, müssen die Zeitzone des Workloads und die der Planungseinheit übereinstimmen.
     > - Wenn du eine andere Zeitzone für deinen Workload auswählst als die Zeitzone der Integration, mit der du Daten importierst, werden die importierten Daten in deinem Workload als zeitlich verschoben angezeigt. Wenn beispielsweise eine CSV-Integration auf UTC-Zeit eingestellt ist und dein Workload auf CEST-Zeit (UTC&nbsp;+2&nbsp;Stunden), werden importierte Daten, die für 08:00&nbsp;Uhr markiert waren, im Workload für 10:00&nbsp;Uhr angezeigt.

   - (Optional) **Feiertagsregion**: Enthält nationale Feiertage, die sich auf deinen Forecast auswirken können.
   - (Optional) **Planungseinheit** und **Aktivität**: Erforderlich, um im Abschnitt **Öffnungszeiten** die Option {% link_new Forecast nur innerhalb der Öffnungszeiten aktivieren | features/forecast/injixo-forecast/forecast-activate-business-hours.md %} zu können.

3. (Nur injixo Classic) Wähle aus dem Abschnitt **Preismodell** eine Option aus:

   - **Live-Modus** (kostenpflichtig): Wird monatlich abgerechnet. Kann nicht in den Test-Modus zurückgesetzt werden.
   - **Test-Modus** (kostenlos): Du kannst Forecasts nur ansehen und keinen Mitarbeiterbedarf für die Planung übertragen.

4. Wähle im Abschnitt **Queues zuweisen** die Queues für deinen Workload aus.

   So kannst du die angezeigten Queues einschränken:

   - Filtere die Queues nach Kanal (Anrufe, Chats usw.).
   - Verwende die Checkboxen, um ausgewählte, nicht ausgewählte oder inaktive Queues anzuzeigen. Inaktive Queues wurden von Integrationen importiert, die gelöscht wurden.
   - Verwende das Suchfeld über der Tabelle. Du kannst nach Queue, Integration oder dem Namen des Workloads suchen.

   Hinweis: Wenn das Intervall oder der Kanal einer Queue nicht mit dem der ausgewählten Queue übereinstimmt, werden alle nicht passenden Queues ausgegraut.

5. Klicke auf _Workload erstellen_{:.doc-button}.

   Die Seite zeigt historische Daten und eine vorläufige Version des Forecasts an.  
   Wenn die Berechnung abgeschlossen ist, lade die Seite neu, um die finale Version des Forecasts zu sehen.  
   Der neue Workload wird in der Workload-Liste angezeigt.

Wenn du injixo Essential verwendest, kannst du Basic Workloads erstellen. Basic Workloads erfordern historische Daten von mindestens zwei Wochen. Basic Workloads unterstützen keine Öffnungszeiten.

Wenn du injixo Advanced oder Enterprise WFM verwendest, kannst du Smart Workloads erstellen. Smart Workloads können bereits mit historischen Daten von nur einem Tag einen Forecast erstellen. Smart Workloads unterstützen Öffnungszeiten.

Wenn du injixo Classic verwendest, musst du zudem für jeden Workload das Forecast-Modell (Smart oder Basic) auswählen. Für Smart Workloads musst du zwischen dem Live-Modus und dem Test-Modus wählen. Der Test-Modus ist kostenlos. Allerdings kannst du damit den Forecast nur sehen und keinen Mitarbeiterbedarf für die Planung übertragen. Der Live-Modus bietet die volle Funktionalität und wird monatlich abgerechnet. Smart Workloads im Live-Modus können nicht in den Test-Modus zurückgesetzt werden.

<!-- hidden: feature not live yet -->
<!-- ## Create workloads without historical data

You only need an integration and historical data import if you want injixo to create forecasts. To add forecast data by {% link_new importing a forecast | features/forecast/injixo-forecast/import-forecast.md %} that has been generated externally or to {% link_new create constant staff requirements | features/forecast/requirement-scripts/requirement-constant.md %}, you can create a workload using the tab *Forecast Import*:

1. Go to **Forecast**{:.breadcrumbs}.
2. Click _Create Workload_{:.doc-button} in the upper right corner of the forecast page.
3. In the *Basic configuration* section, enter a **Name** for your new workload.
4. Select the **Time zone** to display data. Note: The set time zone must match the planning unit to save staff requirements.
5. (Optional) Select the **Holiday region** to acknowledge all public holidays that affect your forecast for the year.
6. Select the **Planning unit** and the **Activity**. This is required to calculate staff requirements.
    {{ 4 | image: 'Import Workload basic configuration section' }}
7. Click the tab **Forecast import**.
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file.
    {{ 5 | image: 'Import Workload parameters' }}
9. Click *Create workload*{:.doc-button}. -->

## Workloads bearbeiten

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus der Workload-Liste aus oder gib den Namen des Workloads in das Suchfeld ein.
2. Um einen Workload zu bearbeiten, klicke auf das {% icon pencil %}.<br>  
   Im Abschnitt **Queues zuweisen** kannst du Queues hinzufügen oder entfernen. Wenn das Intervall oder der Kanal einer Queue nicht mit dem der ausgewählten Queue übereinstimmt, werden alle nicht passenden Queues ausgegraut. Wenn du eine Queue entfernst, werden die importierten Daten nicht gelöscht. Die Queue kann weiterhin anderen Workloads zugewiesen werden.
3. Klicke auf _Workload speichern_{:.doc-button}.  
   Die neue Konfiguration aktualisiert ggf. den Forecast.

## Workloads löschen

1. Klicke unter _Forecast > Workloads_{:.breadcrumbs} auf das {% icon trash %} neben dem Workload, den du löschen möchtest.
2. Klicke im Bestätigungsfenster auf _Workload löschen_{:.doc-button}.  
   injixo speichert die zugehörigen historischen Daten. Um die Daten wiederzuverwenden, füge die Queue bzw. Queues einem anderen Workload hinzu.

## Workload-Seite im Überblick

Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus, um die Workload-Seite zu öffnen. Die Seite enthält die folgenden drei Abschnitte:

- Volumen
- AHT
- Mitarbeiterbedarf

Jeder Abschnitt enthält einen Graphen und Bearbeitungsfunktionalitäten.

Standardmäßig zeigen die Graphen Daten aus der aktuellen Woche an.

- Um einen anderen Zeitraum auszuwählen, verwende die Datumsauswahl. Klicke auf eine Kalenderwoche, um die ganze Woche auszuwählen oder auf einen beliebigen Tag und ziehe dann mit der Maustaste, um einen Zeitraum kürzer oder länger als eine Woche auszuwählen.
- Verwende _<_{:.doc-button} und _>_{:.doc-button}, um ausgehend vom aktuell ausgewählten Zeitraum zurück bzw. vorwärts zu navigieren.

### Der Abschnitt Volumen

Der Graph im Abschnitt Volumen zeigt Kontaktvolumen für historische Daten, importierte Forecasts und erzeugte Forecasts an.
Bewege den Mauszeiger über dem Graphen, um detaillierte Informationen über Volumen, AHT, Mitarbeiterbedarf, manuelle Anpassungen und hinzugefügte Ereignisse anzuzeigen.<br>
Erfahre, wie du {% link_new das Volumen anpassen | features/forecast/injixo-forecast/manual-adjustments.md | #volumen-oder-aht-anpassen%} kannst.

### Der Abschnitt AHT

Der Abschnitt AHT ist standardmäßig ausgeblendet, wenn du die Workload-Seite öffnest oder neu lädst. Um den Abschnitt AHT anzuzeigen, klicke auf das {% icon eye_slash %}.
Der AHT-Graph ist nur für Workloads mit Queues verfügbar, die AHT-Daten enthalten.<br>
Erfahre, wie du {% link_new die AHT anpassen | features/forecast/injixo-forecast/manual-adjustments.md | #volumen-oder-aht-anpassen%} kannst.

### Der Abschnitt Mitarbeiterbedarf

Der Graph im Abschnitt Mitarbeiterbedarf zeigt den berechneten Mitarbeiterbedarf an.
Unter dem Graphen kannst du die konfigurierten Parameter für den Mitarbeiterbedarf und die Gesamtpersonenstunden einsehen. Bewege den Mauszeiger über dem Graphen, um detaillierte Informationen über AHT, Volumen, Mitarbeiterbedarf, jegliche manuelle Anpassungen und hinzugefügte Ereignisse anzuzeigen.<br>
Erfahre, wie du den {% link_new Mitarbeiterbedarf für die Schichtplanung verwendest | features/forecast/injixo-forecast/calculate-staff-requirements.md | #mitarbeiterbedarf-für-schichtplanung-verwenden %}.

## Häufig gestellte Fragen

| Frage                                     | Antwort                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Warum zeigen die Graphen auf einer Workload-Seite nichts an? | injixo erzeugt einen Forecast für 365&nbsp;Tage nach dem letzten Datenimport. Wenn die Graphen auf einer Workload-Seite keine Daten für einen bestimmten Zeitraum in der Zukunft anzeigen, überprüfe unter _Account > Integrationen_{:.breadcrumbs}, ob deine Integration weiterhin Daten importiert. Überprüfe zudem in der Workload-Konfiguration, ob dem Workload die richtigen Queues zugewiesen sind. |
