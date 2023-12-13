---
title: Besondere Ereignisse berücksichtigen
product_label:
  - on-premise
---

Besondere Ereignisse wie zum Beispiel Feiertage sorgen oft für abweichende Tages- oder Wochenkurven. Im Folgenden zeigen wir Dir Lösungsansätze auf, wie Du verschiedene Abweichungen bei Deinem Forecast berücksichtigen kannst:

## Auswirkung des Ereignisses

Zum Einstieg in den Umgang mit Ereignissen sollte vorab überlegt werden, welchen Einfluss das Ereignis im Vergleich zu einem normalen Tag auf die Tageskurve hat.

  - `Gleichbleibende Tageskurve` (bei abweichendem Volumen):
    Die Tageskurve ist im Verlauf gleichbleibend zu einem normalen Tag, nur das Volumen ist prozentual abweichend. Beispiel: Bei einer Hotline kommt es an einem Feiertag zu einem 25% geringeren Anrufvolumen bei gleichbleibender Verteilung über den Tag.
  - `Abweichende Tageskurve`:
    Die Tageskurve ist im Verlauf deutlich abweichend zu einem normalen Tag. Beispiel: Bei einer Hotline kommt es an einem Feiertag zu einem wesentlich geringeren Anrufvolumen am Vormittag, dafür steigt dieses drastisch im Verlaufe des Nachmittags gegenüber einem normalen Tag.

## Gleichbleibende Tageskurve

Bei einer gleichbleibenden Tageskurve mit abweichendem Volumen bietet es sich an, das Ereignis nach dem Forecast zu bearbeiten - jedoch vor der Bedarfsberechnung. Durch dieses Vorgehen ersparst Du Dir den Aufwand der Anlage von Ereignistypen sowie benutzerdefinierter Tages- und Wochenkurven.

Im ersten Schritt führst Du den Forecast wie gewohnt für den Zeitraum durch, in dem Dein Ereignistyp liegt. Danach nutzt Du die Möglichkeit, Tageskurven zu bearbeiten (*Prognose > ForecastPro > Tageskurven bearbeiten*{:.breadcrumbs}):

  - Wähle unter den Parametern Deine Queue aus.
  - Wähle unter den Parametern Deinen Wertetyp aus.
    Hinweis: Die Berechnung ist pro Wertetyp des Forecast vorzunehmen, standardmäßig 'eingehende Anrufe' und 'durchschnittliche Anrufdauer'
  - Wähle als Version `Forecast` aus, damit Du die historischen Daten nicht überschreibst
  - Wähle als Start- und Enddatum den Tag aus, auf den das Ereignis fällt
  - Rufe die Forecast-Werte auf, indem Du auf *Anwenden*{:.doc-button} klickst
  - Markiere in der erscheinenden Tabelle den betreffenden Tag
  - Wähle nun unter der `Berechnung` die Option `Tag` und gib Deinen gewünschten Aufschlag oder Abschlag ein und führe diesen durch einen Klick auf *Anwenden*{:.doc-button} aus.
  - Speicher die Änderung im Forecast unter den Parametern. Klick dazu auf *Speichern*{:.doc-button}.

Das abweichende Volumen ist entsprechend für den Tag gespeichert und der Forecast kann durch die Bedarfsberechnung wie gewohnt abgeschlossen werden.

## Abweichende Tageskurve

### Wiederkehrendes Ereignis bei gleichbleibendem Wochentag

Bei dem Ereignis handelt es sich zum Beispiel um einen Feiertag, der immer auf den gleichen Wochentag fällt, wie zum Beispiel der Pfingstmontag immer auf einen Montag fällt. Bei unserem Beispiel gehen wir von einem Forecast- sowie Planungszeitraum von vier Wochen aus.


#### 1. Ereignistyp anlegen und zuweisen

  - Unter *Administration > Prognose > Ereignistypen*{:.breadcrumbs} findest Du die vom System vorgegebenen Wochentage Montag bis Sonntag.
  - Leg über die Aktionsleiste einen neuen Ereignistypen an. Vergib einen `Namen` und eine `Kurzbezeichnung`. “Faktoren” sind in diesem Szenario nicht notwendig und können daher ignoriert werden.
  - Im nächsten Schritt weist Du unter *Administration > Prognose > Queues*{:.breadcrumbs} den entsprechend gewünschten Queue(s) den Ereignistyp zu. Hierzu wählst Du eine Queue aus und fügst in der Bearbeitungsmaske unter Ereignistypen den Typ zu und hinterlegst die entsprechende Öffnungszeit.
  - Um das Ereignis mit einem Datum zu verbinden, ruf über *Administration > Prognose*{:.breadcrumbs} den *Prognosekalender*{:.menu-item} auf. Wähle eine Queue aus, der Du im Schritt zuvor das Ereignis zugewiesen hast und bestätige Deine Auswahl mit *Anwenden*{:.doc-button}. Wähle rechts bei den Optionen den Ereignistyp aus und klick anschließend auf die Tageszelle des entsprechenden Datums im Kalender. Damit ist der Ereignistyp dem Datum zugeordnet.

> Tipp
>
> Um das Ereignis auf Basis von historischen Daten im Forecast berücksichtigen zu können, ist es bereits an dieser Stelle sinnvoll, das Ereignis auch rückwirkend im Prognosekalender zu hinterlegen. Bei unserem Beispiel empfiehlt es sich den Pfingstmontag für das aktuelles Jahr sowie für die vergangenen letzten 2-3 Jahre einzutragen (abhängig wie weit Deine historischen Daten zurückgehen).

  - Mit der Anlage und Zuweisung des Ereignistypen zu Queues und dem Prognosekalender sind die notwendigen Vorarbeiten abgeschlossen und wir können in den Forecast-Prozess wechseln.

#### 2. Typische Tageskurve erstellen

  - Ruf *Prognose > ForecastPro > Typische Tageskurve*{:.breadcrumbs} auf. Der Ablauf für die Tageskurve ist wie gewohnt - ruf die Queue und Wertetypen mit dem Ereignistyp über das entsprechende Datum auf. In unserem Beispiel wäre dieses für das Jahr 2016 ein Start- und Enddatum am 16.05.2016 sowie “Pfingstmontag” als Ereignistyp.
  - Durch das Aufrufen und Speichern weiterer historischer Daten zum Ereignistyp (im Beispiel Pfingstmontag 2015, 2014, etc.) wird die typische Tageskurve für den Ereignistypen noch genauer.

> Hinweis
>
> Identisch zum generellen Vorgehen bei Tageskurven sollte darauf geachtet werden, ob eine `Tageskurve gespeichert` in schwarzer Farbe bereits vorliegt. Ist das nicht der Fall, sollte diese deaktiviert werden - Entferne dazu den Haken `aktiv` unter der `Tageskurve gespeichert`. Faustformel: Beim ersten Aufrufen und Speichern ist noch keine Tageskurve gespeichert.

#### 3. Benutzerdefinierte Wochenkurve erstellen

  - Als nächsten Schritt erstellen wir eine typische Wochenkurve die den Ereignistypen enthält. Damit unsere `Standard Wochenkurve` nicht beeinflusst wird, legen wir hierzu eine benutzerdefinierte Wochenkurve an.
  - Unter *Prognose > ForecastPro > Typische Wochenkurve*{:.breadcrumbs} wählst Du die gewünschte Queue und Wertetypen aus und gibst die Länge sowie das Start- und Enddatum vor. In unserem Beispiel für den Pfingstmontag 2016 eine `Länge der Wochenkurve` mit 1 sowie das `Start- und Enddatum` vom 16.05.2016 bis 22.05.2016. Der Ereignistyp muss an dieser Stelle nicht ausgewählt werden, da durch den `Prognosekalender` das Datum dem System bereits bekannt ist.
  - Ruf über den *Anwenden*{:.doc-button} Button die Wochenkurve entsprechend auf, wodurch der Button *Neu*{:.doc-button} auf Höhe der *Wochenkurve-Auswahl*{:.doc-button} erscheint. Über den Button legst Du nun eine benutzerdefinierte Wochenkurve an. Danach speicherst Du die Wochenkurve wie gewohnt ab.
  - Durch das Aufrufen und Speichern weiterer historischer Wochen, in denen sich der Ereignistyp befindet (Pfingstmontags-Woche 2015, 2014, etc.), wird die typische Wochenkurve für den Ereignistypen noch genauer.

#### 4. Forecast

  - Der Ablauf des Forecast ist wie gewohnt, lediglich bei der Wahl des Forecast-Zeitraums ist der Ereignistyp zu berücksichtigen.
  - Dieses wird an unserem Beispiel ersichtlich. Hier beträgt unser Forecast-Zeitraum vier Wochen. 2017 fällt Pfingstmontag auf den
    05.06.2017, also in unseren Forecast-Zeitraum vom 29.05. bis
    25.06.2017. Somit haben wir in Forecast-Wochen folgende Situation:
    1. Woche = normale Woche
    2. Woche = abweichende Woche mit Ereignistyp Pfingstmontag
    3. Woche = normale Woche
    4. Woche = normale Woche
  - Aus diesem Grund empfehlen wir im ersten Schritt wie gewohnt den Forecast für die 4 Wochen mit der Standard-Wochenkurve vorzunehmen. Danach wird der Forecast nur für die abweichende Woche mit der benutzerdefinierten Wochenkurve vorgenommen und überschreibt somit diesen einwöchigen Zeitraum (im Beispiel die 2. Woche).

### Wiederkehrendes Ereignis bei abweichenden Wochentag

Bei dem Ereignis handelt es sich beispielsweise um einen Feiertag, der aufgrund seines festen Datums jährlich auf unterschiedliche Wochentage fällt, wie zum Beispiel der 'Tag der Arbeit' am ersten Mai. Bei unserem Beispiel gehen wir von einem Forecast- sowie Planungszeitraum von vier Wochen aus. Folgende Schritte werden im Weiteren detailliert beschrieben:

Die ersten beiden Schritte [1. Ereignistyp anlegen und zuweisen] und [ 2. Typische Tageskurve erstellen] sind vom Vorgehen identisch zum oben beschriebenen Vorgehen.

#### 3. Benutzerdefinierte Wochenkurve erstellen

  - Als nächsten Schritt erstellen wir eine typische Wochenkurve, die den Ereignistypen enthält. Damit unsere “Standard Wochenkurve” nicht beeinflusst wird, legen wir hierzu eine benutzerdefinierte Wochenkurve an.
  - Unter *Prognose > ForecastPro > Typische Wochenkurve*{:.breadcrumbs} wähle die gewünschte `Queue` und `Wertetypen` aus und gib die Länge sowie das `Start- und Enddatum` vor. In unserem Beispiel für den Tag der Arbeit 2016 ist das eine “Länge der Wochenkurve” mit 1 sowie das Start- und Enddatum vom 25.04.2016 bis 01.05.2016. Der `Ereignistyp` muss an dieser Stelle nicht ausgewählt werden, da durch den Prognosekalender das Datum dem System bereits bekannt ist.
  - Ruf über *Anwenden*{:.doc-button} die Wochenkurve entsprechend auf, wodurch der Button *Neu*{:.doc-button} auf Höhe der *Wochenkurve-Auswahl*{:.doc-button} erscheint. Über den Button legst Du nun eine benutzerdefinierte Wochenkurve an. Achte darauf die `Wochenkurve gespeichert` in schwarzer Farbe auf jeden Fall zu deaktivieren (Haken `aktiv` unter der `Tageskurve gespeichert` entfernen). Dieses ist notwendig, da ansonsten das Ereignis durch den gespeicherten Durchschnitt verfälscht wird!

  - Durch das Aufrufen und Speichern weiterer historischer Wochen, in denen sich der Ereignistyp befindet (Tag der Arbeit-Woche 2015, 2014, etc.), wird die typische Wochenkurve für den Ereignistypen noch genauer (hier ebenfalls nicht den Durchschnitt berücksichtigen).

#### 4. Forecast

  - Der Ablauf des Forecast ist wie gewohnt, lediglich bei der Wahl des Forecast-Zeitraums ist der Ereignistyp zu berücksichtigen.
  - Dieses wird an unserem Beispiel ersichtlich. Hier beträgt unser Forecast-Zeitraum vier Wochen. In unseren Forecast-Zeitraum vom 01.05. bis 28.05.2017. Somit haben wir in Forecast-Wochen folgende Situation:
    1. Woche = abweichende Woche mit Ereignistyp Tag der Arbeit
    2. Woche = normale Woche
    3. Woche = normale Woche
    4. Woche = normale Woche
  - Aus diesem Grund empfehlen wir im ersten Schritt wie gewohnt den Forecast für die 4 Wochen mit der Standard-Wochenkurve vorzunehmen. Danach wird der Forecast nur für die abweichende Woche mit der benutzerdefinierten Wochenkurve vorgenommen und überschreibt somit diesen einwöchigen Zeitraum (im Beispiel die 1. Woche).

### Eventreihe von mehreren Ereignissen innerhalb eines Forecast-Zeitraums

Bei einer Eventreihe liegen mehrere Ereignis innerhalb eines Forecast-Zeitraums, wie zum Beispiel Ostern mit Karfreitag, Ostersonntag und Ostermontag. Das Vorgehen ist unverändert zu den bereits beschriebenen Fällen.

Lediglich beim `Benutzerdefinierten Wochenkurven` ist zu berücksichtigen, in welchem Zeitraum die einzelnen Ereignistypen fallen. Diese Eventreihe, in unserem Fall Karfreitag, Ostersonntag und Ostermontag, sollte in einer einzelnen benutzerdefinierten Wochenkurve gespeichert werden. Für unser Beispiel sollte diese in einer zwei Wochen langen typische Wochenkurve gespeichert werden.
