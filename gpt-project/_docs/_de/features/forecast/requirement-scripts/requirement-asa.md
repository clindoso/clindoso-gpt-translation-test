---
title: Bedarf mit durchschnittlicher Antwortzeit (ASA)
toc: false
---

Das Bedarfsskript *Anrufe - Durchschnittliche Antwortgeschwindigkeit* berechnet die Anzahl der Mitarbeiter, die erforderlich ist, um Dein Serviceziel basierend auf der durchschnittlichen Antwortzeit (ASA) zu erreichen. Die ASA ist die durchschnittliche Wartezeit, bevor ein Anruf beantwortet wird. Das Skript berechnet die Anzahl der Mitarbeiter, für die die durchschnittliche Antwortzeit niedriger ist als der angegebene Zielwert.

{% include reusables/{{ page.lang }}/scripts/cloud-other-method.md %}
{% include reusables/{{ page.lang }}/scripts/cloud-prerequisites.md %}
{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}{% include reusables/{{ page.lang }}/scripts/on-prem-forecast-required.md %}


## Verfügbare Parameter

Die Skriptoberfläche ist in mehrere Abschnitte unterteilt.  

{{ 1 | image: 'ASA Script UI', '50%' }}

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

1. Nutze **ASA (Sek.)**, um die durchschnittliche Zeit in Sekunden vorzugeben, in der ein Mitarbeiter Anrufe beantworten muss.
2. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}

## Datum

1. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}

{% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}
