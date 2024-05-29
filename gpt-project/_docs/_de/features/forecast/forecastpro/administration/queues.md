---
title: Queues
product_label:
  - on-premise
description: Queues repräsentieren alle Kanäle, über die dich deine Kunden kontaktieren können.
---

In diesem Artikel lernst du:

- wofür Queues verwendet werden.
- wie man sie konfiguriert.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls du in deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

Queues repräsentieren alle Kanäle, über die Kunden dich kontaktieren können.

Xlink importiert Anrufstatistiken direkt in eine Kombination aus Queue, Wertetyp und Version. Xlink benötigt hierfür ein Mapping zwischen deiner ACD und injixo. Für das Xlink-Mapping empfehlen wir, ACD-Queues 1:1 auf injixo-Queues abzubilden. Auf diese Weise kannst du die Queues direkt in _injixo Forecast_{:.menu-item} kombinieren.

## Queues erstellen

Das manuelle Erstellen von Queues ist erforderlich, wenn du Xlink zum Importieren von Daten verwendest.

Gehe zu _WFM > Administration > Prognose > Queues_{:.breadcrumbs} und folge diesen Schritten, um eine Queue zu erstellen:

1. Klicke auf das {% icon item-add %} in der Aktionsleiste.
2. Gib einen **Namen** und eine **Kurzbezeichnung** ein, z. B. **Inbound** und **IB**.
3. Setze die Queue auf **Aktiv**.
4. Wähle die **Intervall**-Länge deiner Queue. Diese sollte die gleiche sein wie in deiner ACD.
5. Wähle die **Zeitzone** deiner Queue.
6. Bestätige deine Eingaben mit _OK_{:.doc-button}.
7. Gib die **Ereignistypen** ein.
8. Wähle die **Wertetypen**, die für deine Queue verfügbar sein sollen.

### Felder unter Allgemein konfigurieren

Im Bereich _Allgemein_ hast du verschiedene Felder, um deine Queue zu konfigurieren:

| Feld                 | Beschreibung                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Typ                  | Typ der Queue. Wähle **Standard-Queue**.                                                                          |
| Name/Kurzbezeichnung | Diese Felder werden zur Identifizierung deiner Queue verwendet.                                                   |
| Aktiv                | Setze deine Queue auf aktiv, andernfalls werden keine Daten importiert.                                           |
| Intervall            | Das Intervall richtet sich nach dem Intervall deiner ACD oder deines externen Systems.                            |
| Beschreibung         | Du kannst deiner Queue eine Beschreibung hinzufügen, damit man sofort sehen kann, wofür die Queue verwendet wird. |
| Übergeordnet         | Um eine Hierarchie in deinen Queues zu visualisieren, kannst du eine übergeordnete Queue festlegen.               |
| Zeitzone             | Lege die Zeitzone fest, in der deine Daten vorliegen.                                                             |

### Ereignistypen definieren

Die Öffnungszeiten deiner Queue werden als Ereignistypen dargestellt. Wir empfehlen jeden Wochentag hinzuzufügen und **Startzeit** und **Endzeit** als 00:00 zu definieren, damit du den ganzen Tag abdeckst. Die Öffnungszeiten sind für den Forecast in _ForecastPro_{:.menu-item} relevant, sie haben jedoch keinen Einfluss auf _injixo Forecast_{:.menu-item}.

### Wertetypen hinzufügen

Die Wertetypen repräsentieren die Zahlen, die aus deinem externen System importiert werden, wie z.B. Kontaktvolumen für verschiedene Kanäle. Verwende sie, um Forecasts zu erstellen oder um sie in anderen Modulen anzuzeigen. Für Forecastzwecke werden nur eingegangene und bearbeitete Volumina sowie AHT-Werte benötigt.  
Bevor du in injixo Enterprise on-premise Wertetypen zuweisen kannst, musst du diese unter _Administration > Prognose > Wertetypen_{:.breadcrumbs} erstellen. In den injixo Cloud-Versionen sind die Wertetypen vordefiniert. Weise die richtigen Wertetypen je nach Kanal deinen Workloads zu, z. B. für Anrufe _Anrufe - Eingehende_, _Anrufe - Angenommene_, _Anrufe - AHT_.
