---
title: Outbound
description: Ermittle den Mitarbeiterbedarf für ausgehende Anrufe.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /de/requirement-outbound/
redirect_reason: Updated filename on 19 March 2024
---

Verwende das Outbound-Skript, um den Mitarbeiterbedarf für Kampagnen mit ausgehenden Anrufen zu berechnen. Die Berechnung erfolgt auf Basis der Gesamtzahl der Kontakte, die während der Kampagne kontaktiert werden, der Kampagnendauer und der erwarteten durchschnittlichen Bearbeitungszeit (AHT).

## Voraussetzungen

Um den Mitarbeiterbedarf mit einer prognostizierten Anrufverteilung zu berechnen, exportiere als erstes den Forecast:

1. Wähle in _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Wähle mit der Datumsauswahl den Zeitraum aus. Klicke auf eine Kalenderwoche, um die ganze Woche auszuwählen oder auf einen beliebigen Tag und ziehe dann mit der Maustaste, um einen Zeitraum kürzer oder länger als eine Woche auszuwählen.
3. Klicke oben rechts auf das {% icon ellipsis_v %} und wähle die Option **Forecast verwenden**.
4. Wähle im Fenster **Verwende diesen Forecast für die Berechnung des Mitarbeiterbedarfs** den Forecast aus, den du verwenden möchtest.
5. Klicke auf _Forecast verwenden_{:.doc-button}.
6. Klicke auf _Schließen_{:.doc-button}.

Alternativ kannst du das Outbound-Skript verwenden, um den Mitarbeiterbedarf ohne einen Forecast zu berechnen. Erfahre in der Tabelle zum [Abschnitt Kampagnendaten](#abschnitt-kampagnendaten), wie du die Parameter entsprechend konfigurierst.

## Skript konfigurieren

1. Gehe zu _Forecast > Bedarfsskripte_{:.breadcrumbs}.
2. Klicke in der Kachel **Anrufe - Outbound** auf _Öffnen_{:.doc-button}.

Das Skript-Konfigurationsfenster besteht aus drei Abschnitten. Erfahre in den folgenden Tabellen, wie du die einzelnen Parameter konfigurierst.

### Abschnitt Kampagnendaten

| Parameter                            | Beschreibung                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Queue                                | Wähle die Queue aus, für die du das Skript ausführen möchtest.                                                                                                                                                                                                                                                                                          |
| Aufzeichnungen                       | Die Gesamtzahl der Zielkontakte für deine Kampagne. Wähle die Option **konstant** aus und gib einen Wert in das Feld darunter ein, um den Mitarbeiterbedarf ohne Forecast zu berechnen. Wähle alternativ die Option **variabel** aus und wähle aus dem Dropdown-Menü darunter einen Wertetyp mit prognostizierten Zielkontakten aus.                    |
| Kontaktrate (%)                      | Der Prozentsatz der beantworteten ausgehenden Anrufe.                                                                                                                                                                                                                                                                                                   |
| Wahlwiederholungsquote (%)           | Der Prozentsatz der Kontakte, die nach einem erfolglosen Kontaktversuch erneut kontaktiert werden. Die Wahlwiederholungsversuche werden in dem Datumsbereich erfasst, den du mit den Parametern **Startdatum** und **Enddatum** konfigurierst. Erfahre mehr über die Wahlwiederholungsquote in [diesem Abschnitt](#was-ist-die-wahlwiederholungsquote). |
| Startdatum                           | Anfang des Datumsbereichs für die Berechnung.                                                                                                                                                                                                                                                                                                           |
| Enddatum                             | Das Ende des Datumsbereichs für die Berechnung. Wähle die Option **Datum** aus und gib ein Datum in das Feld darunter ein oder wähle die Option **Kampagnendauer in Tagen** aus und gib einen Wert in das Feld darunter ein.                                                                                                                            |
| Rate zuständiger Ansprechpartner (%) | Der Prozentsatz an Anrufen, die von den richtigen Personen beantwortet werden. Wähle die Option **konstant** aus und gib einen Wert in das Feld darunter ein oder wähle die Option **variabel** aus und wähle aus dem Dropdown-Menü darunter einen Wertetyp mit prognostizierten Werten für die Right-Party-Kontakt-Rate aus.                           |
| Schwindung (%)                       | (Optional) Der Prozentsatz bezahlter Arbeitszeit, während derer Mitarbeiter keine Kontakte bearbeiten können, z.&nbsp;B. aufgrund unvorhergesehener Pausen oder Krankheiten. Dieser Wert ist auch bekannt als Shrinkage oder Schwund.                                                                                                                   |

### Abschnitt Durchschnittliche Vorgangsdauer

| Parameter | Beschreibung |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| |
| konstant/variabel | Wähle die Option **konstant** aus und gib feste Werte in die Felder darunter ein oder wähle die Option **variabel** aus und wähle aus den Dropdown-Menüs darunter Wertetypen aus. |
| RPC in Sekunden | AHT in Sekunden für ein Telefonat mit dem zuständigen Ansprechpartner. In diesem Wert ist auch die Nachbearbeitungszeit enthalten. |
| WPC in Sekunden | AHT in Sekunden für ein Telefonat mit dem falschen Ansprechpartner, z.&nbsp;B. wenn der Anruf von einem nicht zuständigen Ansprechpartner oder einem automatischen Anrufbeantworter beantwortet wird. |

### Abschnitt Mitarbeiter-Auslastung

| Parameter        | Beschreibung                                                                                                                                                                                                                             |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Planungseinheit  | Die Planungseinheit, für die du den Mitarbeiterbedarf berechnen möchtest. Wenn du die Planungseinheit änderst, aktualisiert sich das Dropdown-Menü **Aktivität** und zeigt alle Aktivitäten an, die der Planungseinheit zugewiesen sind. |
| Aktivität        | Die Aktivität, für die du den Mitarbeiterbedarf berechnen möchtest.                                                                                                                                                                      |
| Mindestbesetzung | Die Mindestanzahl an Mitarbeitern, die pro Intervall benötigt wird. Gib einen Wert ein, um Intervalle mit niedrigeren Werten für den Mitarbeiterbedarf zu überschreiben.                                                                 |
| Maximalbesetzung | Die Höchstanzahl an Mitarbeitern, die pro Intervall benötigt wird. Gib einen Wert ein, um Intervalle mit höheren Werten für den Mitarbeiterbedarf zu überschreiben.                                                                      |

## Skript starten

- Um die Berechnung zu starten, klicke auf _OK_{:.doc-button}.<br>Ein Fenster öffnet sich und zeigt die ausgewählten Eingabeparameter und die Ergebnisse des Skripts an.

Du kannst den {% link_new gespeicherten Mitarbeiterbedarf im Schicht Center einsehen | features/scheduling/edit-or-delete-staff-requirements.md %}.

Hinweis: Gehe in injixo Enterprise on-premise zu _WFM > Prognose > ForecastPro > Forecast_{:.breadcrumbs} oder zu _WFM > Administration > Prognose > Skripts_{:.breadcrumbs}. Für das Skript muss es bereits einen Forecast geben für die Kombination von Queue, Wertetyp und Version. Der Skript-Name kann variieren, weil du beim Erstellen des Skripts einen eigenen Namen vergeben kannst.

## Was ist die Wahlwiederholungsquote?

Die Wahlwiederholungsquote ist der Prozentsatz der Anrufe, die nach einem erfolglosen Kontaktversuch erneut durchgeführt werden. Die Kontaktversuche (Wahlwiederholung) werden so lange wiederholt, bis die Anzahl der unbeantworteten Anrufe kleiner als 1 ist.<br>Beispiel: Du möchtest insgesamt 5.000 Personen erreichen. Eine Wahlwiederholungsquote von 10% bedeutet, dass 500 unbeantwortete Anrufe in einem zweiten Versuch erneut durchgeführt werden, 50 unbeantwortete Anrufe in einem dritten Versuch und 5 unbeantwortete Anrufe in einem vierten Versuch. In diesem Fall beträgt die Gesamtzahl der versuchten Anrufe 5.555.
