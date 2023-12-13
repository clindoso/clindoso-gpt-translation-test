---
title: Bedarf für Multiaktivitäten
toc: false
---

Das Bedarfsskript *Anrufe - Multiaktivität* berechnet den Bedarf der Mitarbeiter zur Bearbeitung des prognostizierten Volumens für jede Teilaktivität, um eine Multiaktivität zu planen.

{% include reusables/{{ page.lang }}/scripts/cloud-special-method.md %}
{% include reusables/{{ page.lang }}/scripts/cloud-prerequisites.md %}
{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}{% include reusables/{{ page.lang }}/scripts/on-prem-forecast-required.md %}

Das Skript kann nur ausgeführt werden, wenn mindestens eine Multiaktivität in injixo vorhanden ist. Der Forecast muss zuvor für alle Teilaktivitäten der Multiaktivität erstellt/exportiert werden.  

## Verfügbare Parameter

Die Skriptoberfläche ist in mehrere Abschnitte unterteilt.  

{{ 1 | image: 'Multiaktivität Skript Oberfläche', '80%' }}

{% include reusables/{{ page.lang }}/scripts/steps/start-calculation.md %}

## Datum

1. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}

### Planungseinheiten-Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
2. Wähle eine **Multiaktivität**. Der Dialog zeigt weitere Eingabefelder für deren Teilaktivitäten.

### Teilaktivität

Konfiguriere diese Parameter für jede Teilaktivität:  

1. Wähle als **Berechnungsmethode** zwischen Chat, Erlang C oder Linear.

#### Queue-Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/version.md %}

#### Erlang C-Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/service-level.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}

Zusätzliche Anmerkung für Chats: {% include reusables/{{ page.lang }}/scripts/steps/seq-percent.md %}

{% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}
