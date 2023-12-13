---
title: Erlang C Bedarf mit Abbrecher Quote
toc: false
---

Das Bedarfsskript *Anrufe - Abbrecher Quote (Erlang C)* berechnet die Mitarbeiter, die benötigt werden, um das prognostizierte Anrufvolumen für eine Aktivität abzuwickeln, basierend auf dem Volumen abgebrochener Anrufe sowie der Dauer bis zum Auflegen eines Anrufers. Dabei ähnelt es sehr stark dem standardmäßigen Erlang C-Skript. Verwende dieses Skript, wenn Du den Erfolg durch das Erreichen einer bestimmten Abbruchrate definierst.

Das Skript benötigt drei Eingabe-Parameter:
1. Die durchschnittliche Zeit, bevor ein Anrufer auflegt. Die durchschnittliche Anzahl wird normalerweise von Deinem Telefonsystem aufgezeichnet.
2. Der Prozentsatz der zu beantwortenden Anrufe.
3. Die Anzahl der Sekunden, in denen dieser Prozentsatz beantwortet werden sollte.

{% include reusables/{{ page.lang }}/scripts/cloud-other-method.md %}
{% include reusables/{{ page.lang }}/scripts/cloud-prerequisites.md %}
{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}{% include reusables/{{ page.lang }}/scripts/on-prem-forecast-required.md %}

## Verfügbare Parameter

Die Skriptoberfläche ist in mehrere Abschnitte unterteilt.  

{{ 1 | image: 'Abandoned Calls Script UI', '50%' }}

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

1. Definiere eine **Abbruchrate (%)**.
2. Definiere die **Zeit bis zum Abbruch (Sek.)**.  
    *Die beiden oben genannten Parameter definieren den Prozentsatz der abgebrochenen Anrufe und die Wartezeit, die Anrufer in der Leitung bleiben, bevor sie auflegen. Das Skript geht davon aus, dass, wenn Du 93% der Anrufe in N Sekunden beantwortest, die übrigen 7% der Anrufe abgebrochen werden.*
3. {% include reusables/{{ page.lang }}/scripts/steps/add-percent.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
5. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}

### Datum

1. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}

{% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}
