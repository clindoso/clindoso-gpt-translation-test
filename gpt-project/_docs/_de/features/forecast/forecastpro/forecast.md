---
title: Forecast mit ForecastPro
redirect_from:
  - /de/best-practice-forecast/
product_label:
  - on-premise
---

Der Forecast sagt die zukünftige Entwicklung für Anrufe und die durchschnittliche Bearbeitungszeit anhand historischer Werte voraus.

*ForecastPro*{:.menu-item} ist ein altes Modul, welches nur noch injixo Enterprise on-premise Kunden zur Verfügung steht. In diesem Artikel erläutern wir dir, wie du einen Forecast mit *ForecastPro*{:.menu-item} erstellst.

{{ 1 | image: 'Ablauf des Forecast', '75%' }}

## Benötigte Stammdaten

Die Stammdateneingabe erfolgt in *WFM > Administration > Prognose*{:.breadcrumbs}:

- Ereignistypen sind die Wochentage Montag bis Sonntag und {% link_new besondere Tage | features/forecast/forecastpro/special-events.md %}, wie z.&nbsp;B. Feiertage oder Tage, an denen Marketing-Aktionen stattfinden. Ereignistypen müssen der Queue zugeordnet sein. Nur dann kannst du die besonderen Tage im Prognosekalender der Queue zuweisen, damit sie beim Forecast berücksichtigt werden.

- {% link_new Queues | features/forecast/forecastpro/administration/queues.md %} repräsentieren deine Eingangskanäle. Den Queues müssen Wertetypen und Ereignistypen zugeordnet sein. Bei einem Datenimport aus Xlink werden die Daten aus dem externen System in der Version Historisch gespeichert.

- *Wertetypen*{:.menu-item} stellen die Kennzahlen dar, die aus einem externen System importiert werden, z.B. Anrufvolumen und Bearbeitungsdauer. Die Wertetypen müssen der Queue zugeordnet sein, damit diese für den Forecast auswählbar sind.

- *Versionen*{:.menu-item} Es gibt zwei vordefinierte Versionen: Historisch und Standard. Die aus Xlink importierten Daten werden in der Version 'Historisch' gespeichert. Kennzahlen aus ForecastPro werden in der Version 'Standard' gespeichert.

## Vorbereitung

Die {% link_new typische Tageskurve | features/forecast/forecastpro/typical-daily-curve.md %} bildet die relative Verteilung von eingehenden Vorgängen oder Bearbeitungszeit über den Tag ab. Bestimme alle typische Tageskurven für die gewünschten Wertetypen pro Ereignistyp.

Die {% link_new typische Wochenkurve | features/forecast/forecastpro/typical-weekly-curves.md %} bildet die charakteristische Verteilung für das Eingangsvolumen und die Bearbeitungszeit über die Woche ab.

Der Wochenverlauf ist nicht auf sieben Tage begrenzt, sondern kann auch ein Vielfaches sein, z.B. um Muster über mehrere Wochen abzubilden. Die Länge, die du für die Wochenkurve festlegst, wird auch für deinen Forecastzeitraum genutzt. Nutze für den Forecast den gleichen oder einen längeren Zeitraum wie für deine Planung.

## Forecast

Die prognostizierten Daten werden in einer Forecast-Version gespeichert - in der Regel in der Version 'Standard'. Der Mitarbeiterbedarf wird als Planungsgrundlage an SchedulePro übermittelt.

Die Voraussetzungen für den Forecast-Prozess sind erfüllt, wenn du eine typische Tageskurve für jeden Ereignistyp der Woche und eine typische Wochenkurve für den Prognosezeitraum erzeugt hast.

Der Forecast-Prozess läuft in drei Schritten ab, die nachfolgend erläutert werden:

1. Forecast der Wochenwerte mit Bestimmung des Basisvolumens
2. Forecast der Tageswerte
3. Bedarfsermittlung und Skriptausführung

Um einen Forecast durchzuführen, öffne den Menüpunkt *Forecast*{:.menu-item}.

### Parameterauswahl

In der Bearbeitungskategorie `Parameter` wählst du die Herkunft der Daten für den Forecast aus.

| Quell-Queue | Wähle die Queue aus, deren Typische Wochenkurven und Typische Tageskurven du für den Forecast verwenden willst (normalerweise “Historische Daten”). |
| Wertetyp | Bestimme zunächst den Wertetyp für den Forecast und wähle die Ziel-Queue aus (normalerweise “eingehende Anrufe” und “durchschnittliche Bearbeitungszeit”) |
| Ziel-Queue | Wähle in diesem Feld die Queue aus, unter der die prognostizierten Werte gespeichert werden. Bei aktivierter Zeitzonendarstellung muss die Zeitzone der Quell- und Ziel-Queue identisch sein. Im Auswahlfeld werden nur die Queues angezeigt, die den gleichen Wertetyp wie die Quell-Queue enthalten. Quell-Queue und Ziel-Queue können identisch sein. |
| Wochenkurve | Du kannst für den Forecast eine benutzerdefinierte Wochenkurve angeben, wenn du dafür im Menüpunkt *Typische Wochenkurve*{:.menu-item} Daten in einer benutzerdefinierten Wochenkurve gespeichert hast. Damit hast du die Möglichkeit, einen Forecast für unterschiedliche Queue-Wertetyp-Kombinationen auszuführen, ohne für jede einzelne eine Typische Wochenkurve zu erstellen. Diese Vorgehensweise empfiehlt sich, wenn derselbe Wochenverlauf für mehrere Queue-Wertetyp-Kombinationen zutrifft. Wenn du differenzierte Forecasts für jede einzelne Queue-Wertetyp-Kombination erstellen willst, dann wähle 'Standard'. |
| Quell-Version | Lege die Version fest, deren Daten für den Forecast verwendet werden sollen (gewöhnlich die Version 'Historisch' mit den Daten aus dem externen System). |
| Ziel-Version | Wähle die Version aus, in die die prognostizierten Daten gespeichert werden sollen (gewöhnlich die Version 'Standard'). |
| Forecast Startdatum | Gib hier den Beginn des Prognosezeitraums an. Das Startdatum sollte der erste Wochentag einer Planungswoche sein, da die Typische Wochenkurve an diesem Tag beginnt. Fiele das Startdatum auf einen anderen Wochentag als den ersten, z.B. auf den dritten, so läge den prognostizierten Werten für den ersten und zweiten Tag nicht die aktuelle Typische Wochenkurve zugrunde. |
| Forecast Enddatum | Das Enddatum wird durch das Programm automatisch ermittelt. Der Prognosezeitraum hat die gleiche Länge wie die gespeicherte Typische Wochenkurve. |

### Forecast der Wochenwerte

Wähle in der Bearbeitungskategorie `Forecast der Wochenwerte` den Auswertungszeitraum für die Berechnung des Basisvolumens aus.

| Start Auswertung | Gib den Beginn des Auswertungszeitraums an, aus dem das Basisvolumen errechnet werden soll. Das Startdatum muss dem ersten Tag der Planungswoche entsprechen. Der Forecast wertet Wochenkurven von Tag 1 bis Tag 7 einer Planungswoche aus. Unterscheiden sich der Wochentag des Startdatums und der Tag 1 der Planungswoche, lässt sich das Basisvolumen nicht korrekt berechnen. Die Berechnung einer Tendenz erfordert die Angabe eines Zeitraums von mindestens zwei Typischen Wochenkurven. |
| Ende Auswertung | Gib das Enddatum für den Auswertungszeitraum an. Das Enddatum muss mit dem letzten Wochentag der Planungswoche identisch sein. |

Bestätige deine Auswahl mit *Anwenden*{:.doc-button}. `Tabellenfenster`, `Diagrammfenster` und `Bearbeitungsfenster` werden eingeblendet.

In der Bearbeitungskategorie Forecast der Wochenwerte bestimmst Du das Basisvolumen bzw. den Basisdurchschnitt des Wertetyps für den Forecast. Der Wert kann manuell im Feld Basisvolumen eingetragen oder anhand vorliegender Daten ermittelt werden.

Für jede Wochenkurve des ausgewählten Zeitraums wird die Wochensumme des angegebenen Wertetyps angezeigt. Die Summe oder der Durchschnitt berücksichtigt nur Daten innerhalb der Öffnungszeiten der Queue. Bevor Du das Basisvolumen berechnest, hast Du die Möglichkeit, die Wochensummen zu prüfen, zu korrigieren oder zu gewichten.

> Hinweis
>
> Das Basisvolumen für den Forecast errechnet sich aus den Summen der einzelnen Wochenkurven des Wertetyps. Korrekturen der Wochenwerte wirken sich nicht auf die importierten oder prognostizierten Daten aus. Sie gehen aber in die Ermittlung des Basisvolumens ein.

Du kannst deine Änderungen jederzeit in der Bearbeitungskategorie `Forecast der Wochenwerte` verwerfen. Klicke dazu auf *Anwenden*{:.doc-button}.

Nach Abschluss der Kontrolle und Gewichtung der einzelnen Wochenkurven startest Du die Ermittlung, indem Du auf *Berechnen*{:.doc-button} klickst. Das Ergebnis erscheint im Feld `Basisvolumen`. Im `Diagrammfenster` wird die Tendenzlinie für die Entwicklung des Wertetyps eingeblendet. Es besteht jederzeit die Möglichkeit der Neuberechnung.

> Hinweis
>
> Wenn du prognostizierte Wochen-Versionswerte sichten oder bearbeiten willst, kannst du dir die Daten im Menüpunkt *Typische Wochenkurve*{:.menu-item}, in der Version 'Standard' anzeigen lassen und bearbeiten.

Nach Bestimmung der Tendenz und des Basisvolumens für den Forecast der Wochenwerte, kannst du den Forecast der Tageswerte errechnen lassen.

### Forecast der Tageswerte

Nachdem du das Basisvolumen für den Forecast in der Bearbeitungskategorie `Forecast der Wochenwerte` ermittelt hast, erstellst Du in der Bearbeitungskategorie `Forecast der Tageswerte` einen Forecast für alle Ereignistypen im Forecast-Zeitraum.

| Forecast Datum | Wähle das Datum aus, für das nach der Berechnung die Tageswerte angezeigt werden sollen. Der Name des Ereignistyps wird im Feld Ereignistyp angezeigt. |
| Ereignistyp | In diesem Feld wird automatisch der Name des Ereignistyps angezeigt, der dem im Feld 'Forecast Datum' ausgewählten Datum im Prognosekalender zugeordnet ist. |

Um den Forecast der Tageswerte zu berechnen, bestätige deine Auswahl, indem du auf *Berechnen*{:.doc-button} klickst. Für den im Feld `Forecast Datum` eingestellten Tag wird ein `Tabellenfenster` und ein `Diagrammfenster` geöffnet.

Durch Auswahl eines Datums kannst du den Forecast-Wert für jeden Ereignistyp kontrollieren und bei Bedarf manuell korrigieren. Die Datumsangaben sind in der für den Forecast ausgewählten Zielversion gespeichert. Du kannst die Forecast-Werte und damit den Kurvenverlauf manuell ändern. Trage in der Tabellenspalte der prognostizierten Tageskurve den korrigierten Wert für den Zeitraum ein. Die Änderung im Kurvenverlauf ist anschließend im `Diagrammfenster` sichtbar.

Soll das prognostizierte Tagesvolumen verändert werden, kannst du den Summenwert in der letzten Tabellenzeile ändern. Der neue Summenwert wird automatisch entsprechend der Tageskurve auf die Intervalle verteilt.

Zum Speichern der geänderten Forecast-Daten klicke für jeden einzelnen Ereignistypen auf *Speichern*{:.doc-button}.

> Hinweis
>
> Wenn du prognostizierte Tagesversionswerte später überprüfen oder bearbeiten möchtest, werden Dir die Daten im Menüpunkt *Tageskurven bearbeiten*{:.menu-item} normalerweise in der Version 'Standard' angezeigt. Die Forecast-Werte können dort kurzfristig an veränderte Situationen angepasst werden. Möglich sind Änderungen einzelner 'Tagesintervallwerte', Änderungen der 'Tagesgesamtwerte', Änderungen der 'Summe aller Tagesgesamtwerte' innerhalb des Anzeigezeitraums bzw. die Erhöhung oder Reduktion aller Tagesintervallwerte. Außerdem kannst du eine gänzlich neue Tageskurve erstellen. Der prognostizierte Kurvenverlauf kann beeinflusst werden.

## Bedarfsberechnung und Skriptausführung

Der Mitarbeiterbedarf kann ermittelt werden, wenn du den Forecast der Wochenwerte und den Forecast der Tageswerte für den Forecast-Zeitraum im Menüpunkt *Forecast*{:.menu-item} durchgeführt oder die einzelnen Tageskurven im Menüpunkt *Tageskurven bearbeiten*{:.menu-item} bearbeitet hast.

Das Skript zur Bedarfsermittlung kannst du im selben Menüpunkt in der Bearbeitungskategorie `Bedarfsberechnung` starten.

Je nach gewünschter Bedarfsberechnung ist es notwendig, den Forecast der Wochen- und Tageswerte pro Wertetyp durchzuführen. Zum Beispiel beim Einsatz des Bedarfsberechnungs-Skript “Anrufe - Single Activity (Erlang C)”. Hier sollte vor der Bedarfsberechnung für die Wertetypen “eingehende Anrufe” und “durchschnittliche Bearbeitungsdauer” der Forecast erfolgen.

### Bedarfsberechnung

Die Bedarfsberechnungen steht Dir in den Menüpunkten *Forecast*{:.menu-item} und *Tageskurven bearbeiten*{:.menu-item} unter der Bearbeitungskategorie `Bedarfsberechnung` zur Verfügung.

Wähle das gewünschte Skript aus, mit dem du den Bedarf ermitteln willst.

Klicke auf *Ausführen*{:.doc-button}, um eines der Skripte auszuwählen. Gib im Parameterdialog für die Skriptausführung die zur Berechnung erforderlichen Parameter ein (siehe Dokumentation zu den einzelnen Skripten).

Nachdem du alle Angaben richtig eingegeben hast, bestätige die Ausführung des Skripts mit *Ok*{:.doc-button}. Das Skript wird ausgeführt. Der Mitarbeiterbedarf wird nun berechnet und gespeichert. Dabei wird eine Gültigkeitsprüfung durch die Planungsregel *2606*{:.id-label} *Aktivitätszuordnung zu den Planungseinheiten* durchgeführt. Wenn die Berechnung oder Übertragung des Mitarbeiterbedarfs eine Planungsregel mit dem Status 'hart' verletzt, wird der Mitarbeiterbedarf nicht ermittelt bzw. gespeichert. Nach dem erfolgreichen Abschluss des Berechnungs- und Übertragungsprozesses wird Dir im `Forecast-Fenster` das Berechnungsergebnis angezeigt.

### Skriptausführung

Du erhältst ein Protokoll mit dem genauen Inhalt der Bedarfsberechnung.

Wenn das Skript Forecast-Daten verarbeitet, zeigt das Protokoll für jeden Tag des Forecast-Zeitraums die prognostizierten Volumen für die ausgewählten Wertetypen zusammen mit dem resultierenden Mitarbeiterbedarf pro Intervall an. Der Mitarbeiterbedarf wird nur für den Zeitraum innerhalb der Betriebszeiten der Queue berechnet, auch wenn der Bedarf über die Öffnungszeiten hinausgeht.

Der ermittelte {% link_new Mitarbeiterbedarf | features/scheduling/employee-requirement.md %} steht in injixo für die weitere Verarbeitung zur Verfügung und kann auch bearbeitet werden. Der Mitarbeiterbedarf wird stets in der Ortszeit der Planungseinheit angegeben.
