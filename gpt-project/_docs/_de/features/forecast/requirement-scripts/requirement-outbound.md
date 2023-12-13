---
title: Outbound Bedarf
toc: false
---

Das Bedarfsberechnungsskript *Anrufe - Outbound* bestimmt die Anzahl der benötigten Mitarbeiter für eine Kampagne mit ausgehenden Anrufen anhand der Anzahl der Kontakte, der Kampagnendauer und der voraussichtlichen Bearbeitungszeit pro Anruf.

{% include reusables/{{ page.lang }}/scripts/cloud-special-method.md %}
{% include reusables/{{ page.lang }}/scripts/on-prem-usage.md %}

## Verfügbare Parameter

Die Skriptoberfläche ist in mehrere Abschnitte unterteilt.  

{{ 1 | image: 'Outbound Skript', '50%' }}

{% include reusables/{{ page.lang }}/scripts/steps/start-calculation.md %}

## Kampagnendaten

1. {% include reusables/{{ page.lang }}/scripts/steps/queue.md %}
2. **Aufzeichnungen** stellt die Anzahl der Zielkontakte Deiner Kampagne dar. Gib einen festen Wert ein oder wähle eine Queue mit Forecastwerten aus.
3. Definiere die **Kontaktrate (%)**. Hierbei handelt es sich um den Prozentsatz der ausgehenden Anrufe, die angenommen werden.
4. Gib einen Wert für die **Wahlwiederholungsquote (%)** z.B. 10% an. Alle Anrufe (Wahlwiederholungen) erfolgen innerhalb der Kampagnendauer und die zusätzlichen Anrufversuche werden über den gesamten Zeitraum verteilt. Es gibt mehrere Wahlwiederholungsversuche. Beispiel: Es sollen insgesamt 5.000 Kontakte während einer Kampagne erreicht werden. Eine Wahlwiederholungsrate von 10 % bedeutet, dass 500 unerreichte Kontakte erneut angewählt werden (zweiter Versuch). Dann werden 50 weitere Wahlwiederholungen durchgeführt (dritter Versuch), und so weiter. Dies wird so lange fortgesetzt, bis die Anzahl der unbeantworteten Anrufe kleiner als 1 ist. In diesem Beispiel beträgt die Anzahl der Gesamt-Kontakte 5.555.
5. {% include reusables/{{ page.lang }}/scripts/steps/startdate.md %}
6. {% include reusables/{{ page.lang }}/scripts/steps/number-of-days.md %} Alternativ kannst Du auch ein **Enddatum** angeben.
7. Lege die **Rate zuständiger Ansprechpartner (%)** fest. Gib einen festen Wert an oder wähle eine Queue mit prognostizierten Werten. Die Rate zuständiger Ansprechpartner ist notwendig, um den Anteil an Anrufen zu definieren, bei denen direkt der richtige Ansprechpartner erreicht wird. Ein Dialer selbst kann nicht differenzieren, ob der richtige oder falsche Kontakt (z.B. die Ehefrau) oder ein Anrufbeantworter das Gespräch entgegennimmt. 
8. Falls notwendig, gib eine **Schwindung(%)** an. Sie definiert, wie viel Zeit im Contact Center verloren geht, weil Mitarbeiter z.B. in einer ungeplanten Pause oder krank sind. Mit diesem Wert wird die verlorene Zeit kompensiert, damit das Serviceziel erreichbar bleibt.


### Durchschnittliche Vorgangsdauer

Wähle eine feste oder variable durchschnittliche Vorgangsdauer. Abhängig davon gib direkt einen Wert ein oder wähle eine Queue mit dem Wertetyp aus für
  * **RPC in Sekunden**. Dieser Wert steht für die Gesprächsdauer mit dem richtigen Ansprechpartner (RPC = Right Party Connect) sowie die Nachbearbeitungszeit.
  * **WPC in Sekunden**. Der Parameter WPC (Wrong Party Connect) in Sekunden gibt die Zeit an, die benötigt wird, um die Person am Telefon als falschen Gesprächspartner zu identifizieren und das Gespräch zu beenden.

### Mitarbeiter-Auslastung

1. {% include reusables/{{ page.lang }}/scripts/steps/planunit.md %}
2. {% include reusables/{{ page.lang }}/scripts/steps/activity.md %}
3. {% include reusables/{{ page.lang }}/scripts/steps/min-max-staff.md %}
