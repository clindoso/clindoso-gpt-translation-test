---
title: Linearbedarf
toc: false
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
---

Das Bedarfsskript *Bedarfsskript (linear)* verwendet eine lineare Berechnung, um auf Grundlage eines Forecasts den Mitarbeiterbedarf für lagerfähige Vorgänge, wie z.B. E-Mails oder Briefe, zu ermitteln.

{% include reusables/{{ page.lang }}/scripts/cloud-automatic-method.md %}
{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}{% include reusables/{{ page.lang }}/scripts/on-prem-forecast-required.md %}

## Verfügbare Parameter

Das Skript ist in mehrere Abschnitte unterteilt:

{{ 1 | image: 'Linear Script UI', '50%' }}

### Queue-Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/version.md %}

### Planungseinheiten-Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/activity.md %}

### Zusätzliche Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}

## Datum

1. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}


Wenn Du die beschriebenen Parameter eingegeben hast, klicke auf *Ok*{:.doc-button}, um die Berechnung zu starten.
