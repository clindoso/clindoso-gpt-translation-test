---
title: Falsche Mappings automatisch korrigieren
description: Korrigiere Mappings nach Änderung von übergeordneten Queues automatisch.
toc: true
product_label:
  - on-premise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-mapping-telephony.md
---

In diesem Artikel lernst Du, wie Du den Parameter _AutomaticMappingCorrection_ im Xlink konfigurierst, um ungültige Mappings automatisch zu korrigieren.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

## Wofür gibt es den Parameter _AutomaticMappingCorrection_?

Um Anrufdaten zu importieren, benötigst Du Queue-Mappings. Existierende Queue-Mappings werden ungültig, wenn Du in einer Queue deren übergeordnete Queue änderst.  
Es kann zu doppelten Mappings kommen, wenn Du in der Xlink-Benutzeroberfläche neue Mappings für die Queue erstellst. Diese Mappings können zu falschen oder fehlenden Daten führen.

## Den Parameter _AutomaticMappingCorrection_ aktivieren

Hinweis: Der Parameter _AutomaticMappingCorrection_ ist Teil der Xlink-Beispielkonfiguration und kann bereits in der Datei _isps_ul.ini_ enthalten sein.

1. Stoppe den Dienst **ISPS Xlink** auf dem Computer, auf dem der Xlink installiert ist.
2. Öffne die Datei _isps_ul.ini_ im Xlink-Ordner
3. Füge den Parameter **AutomaticMappingCorrection=1** im Abschnitt _[GENERAL]_ hinzu. Ist der Parameter bereits vorhanden, ändere den konfigurierten Wert ggf. von 0 auf 1.
4. Starte den Dienst **ISPS Xlink** neu.
5. Öffne die Xlink-Benutzeroberfläche **isps_ul.exe** neu.

Xlink prüft bestehende Mapping-Einträge in der Datei _acd_map.ini_. Xlink erkennt falsche Mappings und korrigiert oder entfernt diese. Ein Dialogfenster informiert Dich, wenn falsche Mappings entdeckt wurden.

## Mapping-Änderungen prüfen

Alle Mapping-Änderungen werden in der Datei _isps_ul.log_ geloggt. Es gibt zwei verschiedene Meldungen:

- _Invalid Mapping detected and automatically corrected_: Ein Mapping-Eintrag mit einer ungültigen übergeordneten Queue wird auf die richtige Queue-ID geändert.
- _Invalid Mapping(s) detected and automatically removed_: Ein Mapping-Eintrag mit ungültigen IDs ist mehrfach vorhanden. Die zusätzlichen Einträge werden entfernt.

Beispiel:

```
03/17/22 12:15:48 > ** ANALYSING MAPFILE STARTED **

03/17/22 12:15:48 > Invalid Mapping(s) detected and automatically removed:
03/17/22 12:15:48 > 	R4-System:1001:1016:1009=$350.BAS
03/17/22 12:15:48 > 	R4-System:1001:1016:1009=Avaya CMS:1:VDN:123:ACDTIME
03/17/22 12:15:48 > The following valid mapping was identified:
03/17/22 12:15:48 > 	R4-System:1:1016:1009=$473.BAS
03/17/22 12:15:48 > 	R4-System:1:1016:1009=Avaya CMS:1:VDN:123:ACDTIME

03/17/22 12:15:48 > Invalid Mapping detected and automatically corrected:
03/17/22 12:15:48 > 	R4-System:1104:1108:1023=$522.BAS
03/17/22 12:15:48 > 	R4-System:1104:1108:1023=Avaya CMS:1:Split:Test:Holdtime
03/17/22 12:15:48 > Updated to:
03/17/22 12:15:48 > 	R4-System:0:1108:1023=$522.BAS
03/17/22 12:15:48 > 	R4-System:0:1108:1023=Avaya CMS:1:Split:Test:Holdtime
03/17/22 12:16:03 > The file 'C:\Program Files\InVision Enterprise WFM\XLink\Acd_map.ini' has been backed up to the file 'C:\Program Files\InVision Enterprise WFM\XLink\Acd_map220317121603.ini'

03/17/22 12:16:03 > ** ANALYSING MAPFILE COMPLETED **
```
