---
title: Datenimport konfigurieren und starten
description: Konfiguration verschiedener Import-Modi für Deinen Xlink-Import
product_label:
  - on-premise
redirect_from: /de/xlink-import-modus/
redirect_reason: Renamed file in April 2022
---

In diesem Artikel lernst Du, wie Du:

- den automatischen Import-Modus konfigurierst.
- einen Import manuell startest.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

Der Import erfolgt immer für den gesamten Tag, d.&nbsp;h. bei einem historischen Import für einen größeren Zeitraum werden immer mehrere aufeinander folgende Importvorgänge für die jeweiligen Einzeltage ausgeführt.  
Der gewählte Import-Modus gilt für alle externen Systeme. Es ist nicht möglich unterschiedliche Modi nur für bestimmte Schnittstellen zu konfigurieren.

## Automatischer Import

Importiere fortlaufend Daten für den aktuellen Tag oder einmal am Tag rückwirkend für den Vortag.

Die beschriebenen Einstellungen kannst Du separat für den Import von Gesprächs- und Mitarbeiterdaten vornehmen. Wähle in der Xlink-Oberfläche im Menü _Einstellungen_{:.menu-item} den Menüpunkt _Auto-Import_{:.menu-item} aus, um den automatischen Import zu konfigurieren.

{{ 1 | image: 'Die verschiedenen Import-Modi', '80%' }}

### Aktuelle Tagesdaten importieren alle x Minuten

Um die Daten alle x Minuten zu importieren, lege das Intervall fest, in welchem der Import stattfinden soll. Das gewählte Intervall darf nicht kleiner sein, als die tatsächliche Dauer des Imports. Je öfter Daten abgefragt werden, desto höher ist unter Umständen die Netzwerklast und die Last auf der ACD-Datenbank. Stelle den Wert daher nicht geringer ein als nötig.

Außerdem muss die ACD zum Zeitpunkt des Imports die Daten bereits fertig geschrieben haben und diese müssen vollständig in der abgefragten Tabelle vorhanden sein. Da dies bis zu einige Minuten dauern kann, kannst Du über die _Referenzzeit_ einen Zeitversatz angeben, wann der Import nach dem eigentlichen Ende des Intervalls beginnen soll. Ein Wert von 00:05 bewirkt bei einem Import alle 15 Minuten, dass der Import nicht zur vollen Viertelstunde erfolgt, sondern 5 Minuten später, also jeweils 5, 20, 35 und 50 Minuten nach jeder vollen Stunde.

### Vortagesdaten importieren um...

Mit dieser Option importiert Xlink Daten des Vortages zu einer festen Uhrzeit. Verwende die Option, wenn Dein externes System keine Daten für den aktuellen Tag, sondern nur für den Vortag liefert. Um weiter zurückliegende Daten zu importieren, nutze den [manuellen Import](#manueller-import).

### Kein Auto-Import

Wähle diese Option, wenn Du keinen automatischen Import durchführen möchtest. In der Regel verwendest Du diese Option nur, wenn kein direkter Zugriff auf die Datenbank der ACD besteht oder CSV-Dateien nur unregelmäßig verfügbar sind. Nutze in diesem Fall den [manuellen Import](#manueller-import).

## Manueller Import

Du kannst den Xlink-Import auch manuell über das Menü _Datei > Import > Gesprächsdaten_{:.breadcrumbs} starten. Zusätzlich stellt das Menü folgende Buttons zur Verfügung:

{{ 2 | image: 'Einen manuellen Import starten', '25%' }}

Für den Import von Gesprächsdaten wähle die Zielflagge. Für den Import von Mitarbeiter-Aktivitätsdaten wähle die entsprechende Option aus dem Menü oder den zweiten Button mit dem Köpfen.

Ein manueller Import ist notwendig, wann immer historische Daten nachimportiert werden müssen, z.B. wenn neue Mappings erstellt worden sind. Für die Dauer eines manuellen Imports wird der Auto-Import unterbrochen, ein Nachimport nicht importierter aktueller Intervalle findet beim nächsten automatischen Import statt.

## Null-Werte schreiben (Parameter WriteAlways)

Ist die Option _Einstellungen > Null-Werte schreiben_{:.breadcrumbs} aktiviert, werden für Intervalle, die beim Import keine Werte zurückgeben, 0 Anrufe angenommen. Dies führt dazu, dass eventuell vorhandene Werte in Deinen WFM-Queues mit 0 überschrieben werden. Eine Änderung über die Xlink-Oberfläche aktualisiert den Parameter _WriteAlways_ in der Datei `isps_ul.ini`.

Dies kann der Fall sein, wenn z.B. ein Zeitraum importiert wird, für den Deine ACD keine Daten mehr gespeichert hat, kann aber korrekt sein, wenn Du zum Beispiel ein Mapping geändert hast und Du tatsächlich vorhandene Daten mit 0 überschreiben möchtest.

_Null-Werte schreiben_ kann hilfreich sein, wenn Daten aufgrund eines Sommer-/Winterzeitwechsels falsch importiert wurden und Du tatsächlich das erste oder letzte Intervall des Tages mit 0 überschreiben musst.  
Es ist jedoch in der Regel ratsam, die Option _Null-Werte schreiben_ nicht permanent zu setzen, damit nicht versehentlich vorhandene Daten mit 0 überschrieben werden.

## Import von Daten im Konsolen-Modus

Um Daten automatisiert zu importieren, die nicht am selben Tag oder vom Vortag bereitstehen, z.B. wenn Dir Dein Dienstleister nur einmal die Woche historische ACD-Daten zur Verfügung stellt, nutze für den Import die Befehlszeilen-Parameter der Xlink-Oberfläche _isps_ul.exe_ in einer Windows Kommandozeile, z.B. `ISPS_UL.EXE -t -d MM/DD/YYYY -L 7`.

Die folgenden Parameter sind vorhanden (Kopie aus der Kontexthilfe):

- -p = Import von Gesprächsdaten (PhoneLink)
- -t = Import von Mitarbeiter-Aktivitätsdaten (TimeLink)
- -d = Startdatum im angegebenen Format
- -L = Importzeitraum in Tagen
