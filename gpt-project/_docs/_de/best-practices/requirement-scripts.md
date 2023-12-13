---
title: Welches Bedarfsberechnungsskript Du wann nutzen solltest
toc: false
---

injixo bietet Dir eine Vielzahl von Methoden zur Berechnung des Mitarbeiterbedarfs.
Während das Servicelevel-Ziel Deines Contact Centers darauf ausgerichtet ist, dass 80% aller Anrufe innerhalb von 20 Sekunden angenommen werden, ist Erlang-C möglicherweise nicht immer das optimale Skript zur Ermittlung des Mitarbeiterbedarfs.
Stattdessen ist es von verschiedenen Faktoren abhängig, welche Berechnungsmethode am besten zu den Anforderungen Deines Contact Centers passt. <br>
Dieser Best Practice Artikel hilft Dir dabei herauszufinden, welches Bedarfsberechnungsskript für Dein Unternehmen am besten geeignet ist.

## Entscheidungshilfe

Das folgende Diagramm hilft Dir bei der Frage, welches Bedarfsberechnungsskript das richtige für Dich ist:

{{ 1 | image: 'Workflow', '60%' }}

## Übersicht über die Bedarfsberechnungsskripte

Für ein vollständiges Bild über alle verfügbaren Berechnungsmethoden erhältst Du hier eine Übersicht:

- {% link_new Konstanter Bedarf | features/forecast/requirement-scripts/requirement-constant.md %}: Für jede Art von Aktivität, für die kein Forecast vorliegt, du aber genau weißt, wie viele Personen Du zu welchem Zeitpunkt benötigst. Hinterlege bei Bedarf Werte für mehrere Zeiträume und Aktivitäten auf einmal.
- {% link_new Linearbedarf | features/forecast/requirement-scripts/requirement-linear.md %}: Für indirekte Kommunikation wie Briefe, E-Mails oder Bestellungen, basierend auf der Annahme, dass dieses Volumen sequentiell abgearbeitet wird. Das Berechnungsergebnis basiert auf dem prognostizierten Volumen und optional auch der AHT.
- {% link_new Linearbedarf für Backoffice | features/forecast/requirement-scripts/requirement-backoffice-linear.md %}: Für indirekte Kommunikation (Briefe, E-Mails usw.), die Du in einem vordefinierten Zeitrahmen bearbeiten möchtest. Wähle zwischen der Bearbeitung innerhalb von x Stunden oder gib vor, dass alles, was z.B. bis 8 Uhr morgens eingegangen ist, bis zum Ende des Arbeitstages bearbeitet werden soll.
- {% link_new Chat Bedarf | features/forecast/requirement-scripts/requirement-chat.md %}: Erlang-C-basierte Berechnungsmethode mit einen zusätzlichen Parameter, mit dem Du die maximale Anzahl paralleler Chat-Sitzungen pro Mitarbeiter festsetzen kannst.
- {% link_new Erlang-C (Single Activity) | features/forecast/requirement-scripts/requirement-erlangc.md %}: Standard-Berechnungsmethode für Anrufe auf Grundlage des Volumens und des zu erreichenen Servicelevels.
- {% link_new Bedarf für Multiaktivitäten | features/forecast/requirement-scripts/requirement-multiactivity.md %}: Plane Multiskill-Agenten und kombiniere verschiedene Kanäle (z.B. mehrere Hotlines oder eine Kombination aus Anrufen und Chats).
- {% link_new Bedarf mit durchschnittlicher Antwortzeit (ASA) | features/forecast/requirement-scripts/requirement-asa.md %}: Erlang-C Variante mit Fokus auf die durchschnittliche Zeit, die Deine Agenten benötigen, um die eingehenden Anrufe zu beantworten.
- {% link_new Erlang C Bedarf mit Abbrecher-Quote | features/forecast/requirement-scripts/requirement-abandoned-calls.md %}: dieses Skript basiert auf Erlang-C. Definiere Dein Servicelevel-Ziel als die maximale Quote abgebrochener Anrufe. Mit diesem Skript kannst Du auch die Quote der angenommenen Anrufe definieren. Hierzu musst Du lediglich den Wert umkehren: für eine Zielquote von 80% angenommener Anrufe, hinterlegst Du stattdessen 20% Abbrecher-Quote.
- {% link_new Outbound Bedarf | features/forecast/requirement-scripts/requirement-outbound.md %}: Für Kampagnen mit ausgehenden Anrufen. Enthält Parameter zur Angabe von Kampagnendauer, Wahlwiederholungsrate, Kontaktrate des richtigen Ansprechpartners usw.

Bist Du Dir noch unsicher, welches Skript Du verwenden sollst? Wirf einen Blick auf die folgende Tabelle, um Dir die Entscheidung zu erleichtern!

{{ 2 | image: 'Überblick zu den Berechnungsskripten'}}
