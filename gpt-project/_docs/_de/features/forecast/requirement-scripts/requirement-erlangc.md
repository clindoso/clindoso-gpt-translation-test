---
title: Erlang C Bedarfsberechnung
toc: false
---

Das Bedarfsskript _Anrufe - Single Activity (Erlang C)_ verwendet die Erlang-C-Methode zur Berechnung des Mitarbeiterbedarfs basierend auf einer Ziel-Wartezeit und dem gewünschten Servicelevel.

{% include reusables/{{ page.lang }}/scripts/cloud-automatic-method.md %}
{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}{% include reusables/{{ page.lang }}/scripts/on-prem-forecast-required.md %}

## Verfügbare Parameter

Die Skriptoberfläche ist in mehrere Abschnitte unterteilt.

{{ 1 | image: 'Erlang C Skript Oberfläche', '50%' }}

{% include reusables/{{ page.lang }}/scripts/steps/start-calculation.md %}

### Queue-Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/version.md %}

### Planungseinheiten-Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/activity.md %}

### Erlang C-Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/service-level.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}

## Datum

1. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}

{% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}

<!-- 1. Wähle ein **Startdatum** und die **Anzahl Tage** aus. Der Zeitraum sollte Deinem Planungszeitraum entsprechen.
2. Wähle eine **Queue** als Quelle für die Bedarfsberechnung aus.
3. Wähle als **Vorgänge** einen der zugeordneten Wertetypen aus, welcher idealerweise Deine eingehenden Anrufe oder Vorgänge enthält.
4. Definiere einen Wertetyp für die prognostizierte **durchschnittliche Vorgangsdauer** (AHT).
   Alternativ wählst Du hier [keine] aus, um dann im Feld **Konstante durchschnittliche Vorgangsdauer** die durchschnittliche Vorgangsdauer als festen Wert in Sekunden anzugeben.
5. Gib die **Version** an, deren Werte verwendet werden sollen.
6. Wähle eine **Planungseinheit** und **Aktivität** aus, für die der Mitarbeiterbedarf gespeichert wird.
7. In **Service-Level (%)** und **Service-Level (Sek.)** legst Du Dein Service-Ziel fest, z.B. 80% der Anrufe in 20 Sekunden.

Optional kannst Du einen **Aufschlag in Prozent** angeben, z.B. 10% als geschätzte Kranken-/Abwesenheitsquote, außerdem eine **Mindestbesetzung** und **Maximalbesetzung**. -->
