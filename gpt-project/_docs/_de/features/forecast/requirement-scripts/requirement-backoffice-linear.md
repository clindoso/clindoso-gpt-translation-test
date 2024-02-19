---
title: Linearbedarf für Backoffice
toc: false
---

Das Bedarfsskript *Backoffice - Linear* berechnet die Anforderungen an die Mitarbeiterplanung für die Bearbeitung nicht anrufbezogener Aktivitäten im Backoffice, wie Briefe, E-Mails und Faxe.

{% include reusables/{{ page.lang }}/scripts/cloud-other-method.md %}
{% include reusables/{{ page.lang }}/scripts/cloud-prerequisites.md %}
{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}{% include reusables/{{ page.lang }}/scripts/on-prem-forecast-required.md %}

## Verfügbare Parameter

Die Skriptoberfläche ist in mehrere Abschnitte unterteilt.  

{{ 1 | image: 'Backoffice Linear Skript UI', '50%' }}

{% include reusables/{{ page.lang }}/scripts/steps/start-calculation.md %}

### Queue-Parameter  

1. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/processes.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/aht.md %}
4. {% include reusables/{{ page.lang }}/scripts/steps/version.md %}

### Planungseinheiten-Parameter

1. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/activity.md %}
3. Setze **Zu bestehendem Bedarf addieren**, um das Berechnungsergebnis zu bereits bestehendem Bedarf zu addieren. Entferne das Häkchen, um den Bedarf zu überschreiben.

### Backoffice-Jobparameter

1. Falls nötig, füge einen Wert für **Aufschlag (%)** ein, um den Mitarbeiterbedarf zu erhöhen, um so dem Schwund (Shrinkage) Rechnung zu tragen.
2. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/aht-fixed.md %}

4. Definiere einige Backoffice-spezifische Parameter. Wähle eine Option und füge Werte in das dazugehörige Feld ein:   
  * **Jobs innerhalb von x Stunden bearbeiten** bestimmt den Zeitrahmen, in dem Dokumente bearbeitet werden müssen, z.B. Dokumente, die innerhalb von 8 Stunden bearbeitet werden müssen.
  * **Jobs vor x um y bearbeiten**. Verwende diese Option, um die Anzahl der Dokumente zu verarbeiten, die bis zum Zeitpunkt X in der Warteschlange vor dem Zeitpunkt Y eingegangen sind. Beispiel: 230 Dokumente sind über Nacht eingetroffen. Alle Dokumente, die vor 8 Uhr morgens eingegangen sind, müssen bis zum Geschäftsschluss, d.&nbsp;h. bis 17 Uhr desselben Tages, verarbeitet werden.
5. Setze **Nur unter den Öffnungszeiten verteilen**, um die berechneten Werte innerhalb der Queue-Öffnungszeiten zu verteilen. Entferne das Häkchen, um 24 Stunden zu nutzen.

### Datum

1. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %}

{% include reusables/{{ page.lang }}/scripts/shrinkage_vs_add_percent.md %}
