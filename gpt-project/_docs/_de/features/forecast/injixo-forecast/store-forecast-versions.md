---
title: Forecast-Versionen erstellen und verwenden
description: Verwende Forecast-Versionen, um (kurz- oder langfristige) Forecasts untereinander oder mit dem tatsächlichen Volumen vergleichen zu können.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /de/versions/
redirect_reason: Updated filename on 29 March 2023
---

In diesem Artikel lernst Du:
- was Forecast-Versionen sind und wann Du sie verwenden solltest.
- wie Du Daten in einer Forecast-Version speicherst.
- wie Du Daten einer Forecast-Version anzeigst.
- wie Du Versionsdaten für die Bedarfsberechnung verwendest.

Neu in injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} und {% link_new was Workloads sind | features/forecast/injixo-forecast/manage-workloads.md %}.

## Was sind Forecast-Versionen?

Da der Forecast ständig aktualisiert wird, zeigt der *Auto-Forecast* immer den  aktuellsten verfügbaren Forecast für Deinen Workload an.

Mit Forecast-Versionen kannst Du:
- bestimmte Teile des *Auto-Forecasts* zu einem bestimmten Zeitpunkt speichern.
- den gespeicherten Forecast mit den aktuellen Werten vergleichen.
- den ursprünglichen Forecast, z. B. bevor Du Ereignisse hinzufügst, mit dem aktuellen Forecast vergleichen.

Die folgenden Forecast-Versionen sind verfügbar:
- *Operativ*: speichere den Forecast, den Du als Grundlage für die Schichtplanung verwendest, bevor Du den Bedarf berechnest
- *Strategisch*: speichere langfristige Forecasts, die für die Kapazitätsplanung verwendet werden

Änderungen am *Auto-Forecast* überschreiben nicht die in einer Forecast-Version gespeicherten Daten.

## Speichere den *Auto-Forecast* in einer Forecast-Version

1. Gehe zu *Forecast*{:.menu-item}.
2. Wähle einen **Workload**.
3. Wähle mithilfe der Zeit-Navigation oberhalb einen **Zeitraum** aus, für den Du die Forecast-Version speichern möchtest.
4. Klicke auf _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon}, um das Kontextmenü zu öffnen.
5. Klicke auf _Forecast in Version ablegen_{:.doc-button}.
6. Wähle die **Operative** oder **Strategische** Forecast-Version.
7. Bestätige Deine Auswahl mit _Speichern_{:.doc-button}.

Es kann nur eine operative und eine strategische Forecast-Version für einen bestimmten Zeitraum geben. Wenn Du Daten innerhalb desselben Zeitraums erneut speicherst, werden bereits bestehende Daten überschrieben.  

## Forecast-Versionen anzeigen

Wenn Du einen Zeitraum auswählst, in dem Versionsdaten vorhanden sind, wird eine zusätzliche farbige Linie je Forecast-Version angezeigt.

Du kannst diese in den Volumen- und AHT-Diagrammen innerhalb der Tages-, Wochen-, Monats- oder Jahresansicht sehen. Um eine Forecast-Version auszublenden, klicke auf das **Augensymbol** neben der Legende am unteren Rand des jeweiligen Diagramms.

{{ 1 | image: 'Volumen und AHT Forecast mit operativer Version'}}

## Versionsdaten für die Bedarfsberechnung verwenden

Es gibt zwei Methoden der {% link_new Mitarbeiterbedarfsberechnung | features/forecast/injixo-forecast/staff-requirement.md %}: *Automatisch* und *Andere*. Je nachdem, welche Methode Du nutzt, musst Du unterschiedliche Schritte ausführen.

So verwendest Du die Daten aus einer Forecast-Version für eine automatische Bedarfsberechnung:

1. Gehe zu *Forecast*{:.menu-item}.
2. Wähle einen **Workload**.
3. Wähle mithilfe der Zeit-Navigation oberhalb einen **Zeitraum** aus, für den Du die Forecast-Version gespeichert hast.
4. Wähle im Abschnitt *Mitarbeiterbedarf* die **Forecast-Version** aus dem ersten Dropdown-Menü über dem Diagramm. Du kannst auch den **Auto-Forecast** auswählen.
5. Klicke auf _Mitarbeiterbedarf verwenden_{:.doc-button}, um den aktuell sichtbaren Mitarbeiterbedarf für die Schichtplanung zu speichern.

Wenn Du die Daten aus einer Forecast-Version in einer alternativen Methode verwenden möchtest, musst Du die Daten für diesen Zeitraum aus der Forecast-Version ins WFM übertragen:

1. Gehe zu *Forecast*{:.menu-item}.
2. Wähle einen **Workload**.
3. Wähle mithilfe der Zeit-Navigation oberhalb einen **Zeitraum** aus, für den Du die Forecast-Version gespeichert hast.
4. Klicke im Abschnitt *Volumen und AHT* auf _Forecast verwenden_{:.doc-button}.
5. Wähle die **Forecast-Version** im Fenster *Forecast für den Mitarbeiterbedarf bereitstellen*. Du kannst auch den **Auto-Forecast** auswählen.
6. Klicke auf *Diesen Forecast verwenden*{:.doc-button}, um die Versionsdaten in die WFM-Version zu übertragen, die auch *Auto-Forecast* heißt.

Jetzt kannst Du eine der alternativen Berechnungsmethoden basierend auf den Daten der Forecast-Version ausführen. Im Bedarfsskript musst Du die WFM-Version *Auto-Forecast* als *Version* auswählen.
