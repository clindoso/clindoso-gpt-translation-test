---
title: Konstanter Bedarf
toc: true
description: Lege konstante Werte für deinen Mitarbeiterbedarf fest.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

Verwende das Bedarfsskript Konstanter Bedarf, um auf Grundlage deiner Eingaben einen festen Mitarbeiterbedarf zu speichern. Erstelle einen neuen Mitarbeiterbedarf oder überschreibe einen bestehenden Mitarbeiterbedarf für deine Aktivitäten zu einem bestimmten Zeitraum.

Verwende das Bedarfsskript Konstanter Bedarf in den folgenden Fällen:

- Du hast keine historischen Daten, um den Mitarbeiterbedarf mit einer anderen Berechnungsmethode zu berechnen.
- Einige Aktivitäten erfordern eine feste Anzahl von Mitarbeitern über einen bestimmten Zeitraum. Zum Beispiel benötigst du jeden Nachmittag zwei Mitarbeiter, um E-Mails zu bearbeiten.

## Voraussetzungen

- Erstelle mindestens einen {% link_new Workload | features/forecast/injixo-forecast/create-workloads.md | #workloads-erstellen %}.

Jeder Workload benötigt mindestens eine Queue. Es gibt zwei Möglichkeiten, Queues zu erstellen:

- {% link_new Füge eine Integration hinzu | features/acd-integration/cloud/how-integrations-work.md %} und importiere Daten. injixo erstellt automatisch eine Queue.
- Erstelle eine Queue, indem du {% link_new einen Beispieldatensatz | features/forecast/injixo-forecast/import-forecast.md | #queue-erstellen %} importierst. Verwende diese Methode, wenn du keine historischen Daten hast und einen konstanten Mitarbeiterbedarf erstellen möchtest.

## Skript konfigurieren

1. Gehe zu _Forecast > Bedarfsskripte_{:.breadcrumbs}.
2. Klicke in der Kachel **Allgemein - Konstanter Bedarf** auf _Öffnen_{:.doc-button}.
3. Konfiguriere im Skript-Konfigurationsfenster folgende Einstellungen:
   - Im Abschnitt **Datum**:
     - **Startdatum**: Gib das Startdatum für die Berechnung des Mitarbeiterbedarfs ein.
     - **Anzahl Tage**: Gib die Anzahl der Tage ab dem Startdatum ein, für die du den Mitarbeiterbedarf berechnen möchtest.
     - **Wochentagsabhängig**: Wenn du **Ja** auswählst, zeigt das Skript im Abschnitt **Daten** die Namen der Wochentage an.<br> Wenn du **Nein** auswählst, zeigt das Skript die Tage nummeriert an als Tag 1, Tag 2, Tag 3 usw. Tag 1 entspricht dem **Startdatum**.<br>Erfahre im [untenstehenden Abschnitt](#wie-wirkt-sich-die-option-wochentagsabhängig-auf-die-berechnung-aus) mehr über die Option.
     - **Zu bestehendem Bedarf addieren**: Checkbox aktiviert: Die Werte, die du unten eingibst, werden dem bestehenden Mitarbeiterbedarf hinzugefügt. Checkbox nicht aktiviert: Die Werte, die du unten eingibst, überschreiben den bestehenden Mitarbeiterbedarf.
     - **Bedarf in Überschneidungszeiträumen addieren**: Checkbox aktiviert: Die Werte, die du unten eingibst, werden dem bestehenden Mitarbeiterbedarf für Zeiträume, die sich teils überschneiden, hinzugefügt. Checkbox nicht aktiviert: Die Werte, die du unten eingibst, überschreiben den bestehenden Mitarbeiterbedarf für Zeiträume, die sich teils überschneiden.
     - **Öffnungszeiten der Planungseinheit beachten**: Aktiviere die Checkbox, wenn du den Mitarbeiterbedarf nur für Intervalle speichern möchtest, die innerhalb der für die jeweilige Planungseinheit konfigurierten Öffnungszeiten liegen.
   - Wähle aus den folgenden Dropdown-Menüs Werte aus. Wenn du einen Wert auswählst, aktualisiert sich das Skript-Konfigurationsfenster nach einigen Sekunden und zeigt andere Parameter an, je nachdem, welche Werte du ausgewählt hast.
     - **Tage mit Zeitabschnitten**: Die Anzahl der Tage ab dem Startdatum, für die du einen Mitarbeiterbedarf eingeben kannst.
     - **Zeitabschnitte pro Tag**: Die Anzahl an Zeitabschnitten pro Tag, für die du einen Mitarbeiterbedarf eingeben kannst. Im Abschnitt **Daten** gibt es für jeden Zeitabschnitt ein Eingabefeld.
     - **Anzahl Aktivitäten**: Die Anzahl der Aktivitäten, für die du einen Mitarbeiterbedarf eingeben kannst. Im Abschnitt **Daten** wird für jede Aktivität eine Spalte angezeigt.
   - Im Abschnitt **Daten**:
     - Wähle eine **Planungseinheit** und eine **Aktivität** für jede Aktivitätenspalte aus.
     - Gib für jeden Zeitabschnitt einen **Beginn** und ein **Ende** ein. Verwende das 24-Stunden-Format.
     - Gib im Feld **Mitarbeiter** die Anzahl der Mitarbeiter ein, die je Zeitabschnitt benötigt werden.
     - Aktiviere die Checkboxen neben den Tagen, für die du den Mitarbeiterbedarf berechnen möchtest.

## Skript ausführen

Wenn du das Skript konfiguriert hast, klicke auf _OK_{:.doc-button}, um die Berechnung zu starten.  
Ein Fenster zeigt die von dir ausgewählten Planungseinheiten und Aktivitäten sowie die Ergebnisse der Berechnung an. Erfahre, wo du {% link_new den gespeicherten Mitarbeiterbedarf einsehen | features/scheduling/edit-or-delete-staff-requirements.md | #mitarbeiterbedarf-einsehen-und-bearbeiten %} kannst.

Hinweis: Gehe in injixo Enterprise on-premise zu _WFM > Prognose > ForecastPro > Forecast_{:.breadcrumbs} oder zu _WFM > Administration > Prognose > Skripts_{:.breadcrumbs}. Der Skript-Name kann variieren, weil du beim Erstellen des Skripts einen eigenen Namen vergeben kannst.

## Wie wirkt sich die Option Wochentagsabhängig auf die Berechnung aus?

Das Skript verwendet den Wert, den du im Feld **Anzahl Tage** eingegeben hast als Datumsbereich, ausgehend vom ersten Tag des Datumsbereichs.  
Wenn du einen Wert kleiner oder gleich 7 eingibst, berechnet injixo den Mitarbeiterbedarf nur für die Anzahl von Tagen, die zum Datumsbereich gehören.<br>
Wenn du einen höheren Wert als 7 eingibst, berechnet injixo den Mitarbeiterbedarf auf Grundlage des Wertes, den du für die Option **Wochentagsabhängig** ausgewählt hast:

- Ja: injixo berechnet den Mitarbeiterbedarf für die gewählten Wochentage bis zum Ende des Datumsbereichs.
- Nein: injixo berechnet den Mitarbeiterbedarf immer wieder neu, beginnend mit Tag 1 und unabhängig vom Wochentag bis zum Ende des Datumsbereichs.
