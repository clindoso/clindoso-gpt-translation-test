---
title: Chat Bedarf
toc: false
---

Das Bedarfsskript _Chat - WebChat_ basiert auf Erlang C und berechnet die Anzahl der Mitarbeiter, die das prognostizierte Volumen für eine Chat-Aktivität bewältigen müssen, um ein bestimmtes Service-Level zu erreichen. Lege fest, dass Mitarbeiter mehrere Chats gleichzeitig bearbeiten können.

{% include reusables/{{ page.lang }}/scripts/cloud-automatic-method.md %}
{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}{% include reusables/{{ page.lang }}/scripts/on-prem-forecast-required.md %}

## Verfügbare Parameter

Die Skriptoberfläche ist in mehrere Abschnitte unterteilt.

{{ 1 | image: 'Chat Skript UI', '50%' }}

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
5. {% include reusables/{{ page.lang }}/scripts/steps/seq-percent.md %}

## Datum

1. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}

{% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}
