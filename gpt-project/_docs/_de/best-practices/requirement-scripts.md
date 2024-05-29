---
title: Berechnungsmethode für Mitarbeiterbedarf auswählen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, welche Bedarfsberechnungsmethode für dich am besten geeignet ist.
toc: true
---

In injixo gibt es verschiedene Berechnungsmethoden und Bedarfsskripte zur Berechnung des Mitarbeiterbedarfs.

## Berechnungsmethoden

- Erlang-C: Berechnungsmethode für eingehende Kontakte basierend auf dem zu erwartenden Volumen und dem angestrebten Service-Level.
- Chat: Auf Erlang-C basierende Berechnungsmethode mit einen zusätzlichen Parameter, mit dem du die maximale Anzahl paralleler Chat-Sitzungen pro Mitarbeiter festlegen kannst.
- Linear: Berechnungsmethode für Kontakte, die nicht in Echtzeit bearbeitet werden müssen (z.&nbsp;B. Briefe, E-Mails, Tickets oder Bestellungen). Das Berechnungsergebnis basiert auf dem prognostizierten Volumen und optional auch der AHT.

Erfahre, wie du die {% link_new Berechnungsmethoden konfigurieren | features/forecast/injixo-forecast/calculate-staff-requirements.md %} kannst.

## Bedarfsskripte

- {% link_new Konstanter Bedarf | features/forecast/requirement-scripts/requirement-constant.md %}: Für Aktivitäten, für die du keinen Forecast hast, aber für die du die Anzahl der benötigten Mitarbeiter pro Zeitraum kennst. Du kannst deine eigenen Werte für den Mitarbeiterbedarf eingeben. Du kannst zudem Werte für mehrere Zeiträume und Aktivitäten festlegen.
- {% link_new Multiaktivität | features/forecast/requirement-scripts/multiactivity-script.md %}: Um Multiskill-Mitarbeiter zu planen und verschiedene Kanäle (z.&nbsp;B. mehrere Hotlines oder eine Kombination von Chats und Anrufen) zu kombinieren.
- {% link_new Outbound | features/forecast/requirement-scripts/outbound-calls-script.md %}: Für Kampagnen mit ausgehenden Anrufen. Mit den Parametern kannst du die Kampagnendauer, Wahlwiederholungsrate, Kontaktrate des richtigen Ansprechpartners usw. festlegen.
- Backoffice linear: Für indirekte Kommunikation, wie Briefe oder E-Mails, die innerhalb eines festgelegten Zeitraums bearbeitet werden müssen. Um dieses Skript zu verwenden, kontaktiere deinen Consultant.
- Durchschnittliche Antwortzeit (ASA): Auf Erlang-C basierendes Skript, das die durchschnittliche Wartezeit betrachtet. Um dieses Skript zu verwenden, kontaktiere deinen Consultant.
- Abbrecher-Quote: Auf Erlang-C basierendes Skript, mit dem du die maximale Quote an abgebrochenen Anrufen als Service-Ziel festlegen kannst. Du kannst dieses Skript auch verwenden, wenn dein Service-Ziel die Quote der angenommenen Anrufe ist. Um dieses Skript zu verwenden, kontaktiere deinen Consultant.

## Datentypen und relevante Bedarfsberechnungsmethoden

Die folgende Tabelle zeigt, welche Berechnungsmethoden und Bedarfsskripte für welchen Datentyp geeignet sind, wenn der Mitarbeiterbedarf berechnet wird:

| Datentyp oder Parameter                                       | Erlang-C (Methode) | Chat (Methode) | Linear (Methode) | Konstanter Bedarf (Skript) | Multi-Aktivitäten (Skript) | Outbound (Skript) |
| ------------------------------------------------------------- | ------------------ | -------------- | ---------------- | -------------------------- | -------------------------- | ----------------- |
| Lagerfähige Daten (z.&nbsp;B. E-Mails, Tickets, Bestellungen) | Nein               | Nein           | Nein             | Nein                       | Ja                         | Ja                |
| Anrufe                                                        | Ja                 | Nein           | Nein             | Nein                       | Ja                         | Nein              |
| Chat                                                          | Nein               | Ja             | Nein             | Ja                         | Ja                         | Nein              |
| Eingehende Kontakte                                           | Ja                 | Ja             | Ja               | Ja                         | Ja                         | Nein              |
| Ausgehende Kontakte                                           | Nein               | Nein           | Nein             | Nein                       | Nein                       | Ja                |
| Einzelner Service                                             | Ja                 | Ja             | Ja               | Ja                         | Nein                       | Ja                |
| Mehrere Services                                              | Nein               | Nein           | Nein             | Nein                       | Ja                         | Nein              |
| Historische Daten                                             | Ja                 | Ja             | Ja               | Nein                       | Ja                         | Ja                |
| Art des Service-Ziels                                         | Ja                 | Ja             | Nein             | Nein                       | Ja                         | Ja                |
| Service-Level (z.&nbsp;B. 80/20)                              | Ja                 | Ja             | Nein             | Nein                       | Ja                         | Ja                |
