---
title: Zeitversatz-Korrektur nach Zeitumstellung (Avaya)
---

In diesem Artikel lernst Du, wie Du die Konfiguration der Lucent/Avaya CMS-Schnittstelle so anpasst, dass nach dem Wechsel auf die Sommer- bzw. Winterzeit zeitversetzt angezeigte Daten wieder korrigiert werden.

Daten können nach der Zeitumstellung im Herbst eine Stunde zu früh, im Frühjahr eine Stunde zu spät angezeigt werden. Hinweis: Die im Artikel verwendeten Beispiele gelten für Deutschland. Die Abweichung zur Coordinated Universal Time (UTC) beträgt im Winter eine Stunde (UTC+1) und im Sommer zwei Stunden (UTC+2).

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

## Ursache

Dein Avaya CMS-System speichert:

- Telefoniedaten in der lokalen Zeitzone vom Standort der Telefonanlage.
- Agentendaten immer in UTC, unabhängig von Winter- oder Sommerzeit und dem Standort der Telefonanlage.

Die Telefoniedaten sind immer korrekt. Die Telefonieanlage wechselt automatisch die Zeitzone. Eine Änderung des TimeZone-Parameters wäre nicht notwendig. Die Agentendaten müssen aber für die korrekte Anzeige in die lokale Zeit verschoben werden.

Der Xlink-Parameter `TimeZone` stellt den Versatz in Stunden zu UTC dar. Für die verwendete Avaya Schnittstelle bedeutet ein Wert von 12, dass es keinen Versatz gibt, ein Wert von 11 stellt eine Verschiebung einer Stunde dar (UTC+1), 10 korrigiert einen Versatz von zwei Stunden (UTC + 2).

Änderst Du nun den Wert `TimeZone`, um die Agentendaten zu korrigieren, verschieben sich die bereits korrekt dargestellten Telefoniedaten.

## Lösung

Benutze neben dem Parameter `TimeZone` zusätzlich den Parameter `TimeZone_TimeLink`, welcher nur für den Import von Agentendaten gilt.

### Anpassung der Xlink-Konfiguration

Füge _TimeZone_TimeLink_ zur Datei **isps_ul.ini** hinzu, wenn dieser Parameter nicht vorhanden ist.

#### Sommerzeit

```
[Avaya_CMS]
...
TimeZone=12
TimeZone_TimeLink=10
...
```

#### Winterzeit

```
[Avaya_CMS]
...
TimeZone=12
TimeZone_TimeLink=11
...
```

## Nachträgliche Datenkorrektur

Änderst Du den Parameter `TimeZone_TimeLink` zu spät, werden die Daten in injixo nicht mehr im korrekten Intervall angezeigt und Du musst sie korrigieren. Da die Zeitumstellung immer am Wochenende passiert, kommt dies oft vor.

> Achtung
>
> Sind vor einem bestimmten Datum keine Daten mehr vorhanden, überschreibt ein Nachimport wie unten beschrieben die Daten unwiederbringlich mit Nullen. Fallen Dir die falschen Daten sehr spät auf (> 30 Tage), stelle vor einem erneuten Import sicher, dass für den überschriebenen Zeitraum noch Daten in der ACD vorhanden sind.

Bereits falsch importierte Daten korrigierst Du wie folgt:

1. Korrigiere den Parameter `TimeZone_TimeLink`.
2. Aktiviere die Option _Nullwerte schreiben_ über die isps_ul.ini; setze `WriteAlways=1`.
3. Starte den _ISPS Xlink_ Dienst neu.
4. Importiere Deine Daten ab dem fehlerhaften Tag erneut, beachte den Hinweis oberhalb.
5. Deaktiviere _Nullwerte schreiben_ wieder über die isps_ul.ini; setze `WriteAlways=0`.
6. Starte den _ISPS Xlink_ Dienst neu.

Tip: Deaktiviere _Nullwerte schreiben_ wieder. Sonst können bereits importierte Daten von Nachimporten mit Nullwerten überschrieben werden.
