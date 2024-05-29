---
title: Logdateien
product_label:
  - on-premise
---

In diesem Artikel geben wir Dir eine Übersicht zu den verfügbaren Logdateien des Xlink. Diese sind wichtig, wenn es beim Xlink Import zu Problemen kommt oder gar keine Daten importiert werden. In diesem Fall enthalten die Logdateien Fehler oder Warnungen. Dein Customer Success Team benötigt diese für eine Problem-Analyse. Eventuell kannst Du mit einem Blick in die Logdateien auch schon selbst ein Problem entdecken. Erläuterungen zu spezifischen Fehlermeldungen enthält dieser Artikel aber nicht.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

## Aktivierung des Loggings

Die Konfigurationsdatei `isps_ul.ini` enthält an zwei Stellen einen Parameter **Protocol**:

- Sektion [General]
- Sektion [Name Deines externen Systems]

Du aktivierst das Logging, indem Du den Wert von 0 auf 1 änderst und nach dem Speichern der Datei den `ISPS Xlink`-Dienst neu startest.

## Logdateien für Dienst und Xlink-Oberfläche

Es wird eine Logdatei für den Import von Anruf- und Agentendaten erzeugt.

Diese Logdateien enthalten:

- Start/Stopp der Xlink-Oberfläche und des Dienstes
- Start/Ende eines Imports
- Informationen zu den eingelesenen Datensätzen
- Geladene Konfigurationsparameter
- Mapping- und Skript-Änderungen
- Mögliche Fehlermeldungen bei Verbindungsproblemen

Bei aktiviertem Logging in der Sektion [General] füllt Xlink folgenden Logdateien mit Daten:

- isps_uls.log
- isps_ul.log
- externes_system_agent_import.log

  _nur bei aktivierter Option für den Agentendaten-Import (TimeLink) im externen System._

### Schnittstellen-spezifisches Logging

Aktiviere das Logging in der Sektion [Name Deines externen Systems], damit der Xlink eine Logdatei für jede gemappte Queue aus dem externen System erzeugt.

Diese Logdateien enthalten:

- die Abfrage auf die Datenquelle (Datenbank oder Datei)
- die zurückgegebenen Werte
- mögliche Fehlermeldungen aufgrund falscher Konfiguration (Universal-Schnittstelle)

Aus Deinem externen System sind 'Queue1' und 'Queue2' mit injixo verknüpft/gemappt, der Xlink erzeugt jetzt zwei Logdateien:

- externes_system_queue1.log
- externes_system_queue1.log

### Zielverzeichnis konfigurieren

Nur für Schnittstellen-Logdateien ist es möglich ein anderes Zielverzeichnis zu konfigurieren. Füge dazu den Parameter `LogDir` mit einem absoluten Pfad in der Sektion [General] der `isps_ul.ini` hinzu:

Beispiel:

```
[General]
LogDir="C:\Xlink\LOGS"
```

## Maximale Dateigröße

Logdateien können eine maximale Größe von 4 GB erreichen. Der Xlink löscht die Dateien nicht automatisch.

Als Folge importiert der Xlink keine Daten mehr. Es gibt zwei mögliche Lösungen:

- Schalte das Logging aus (Protocol=0).
- Lösche die Dateien regelmäßig von Hand oder mithilfe einer bat-Datei in einem geplanten Task.
