---
title: Typische Wochenkurven
product_label:
  - on-premise
---

Im Menüpunkt *Typische Wochenkurve*{:.menu-item} legst Du die Verteilung der prognostizierten Werte im Forecastzeitraum fest. Die Typische Wochenkurve wird beim Forecast für die Verteilung des Wertetyps auf den Forecastzeitraum zugrunde gelegt. Das beim Forecast prognostizierte Basisvolumen (oder der Durchschnitt) verteilt sich anhand dieser Kurve auf den Prognosezeitraum (Anzahl der Wochen). Als Woche gilt die in der Administration konfigurierte Planungswoche.

> Hinweis
>
> Die Typische Wochenkurve zeigt nur die Verteilung des Wertetyps an. Das Volumen des Wertetyps wird erst beim Forecast ermittelt.

Um eine Typische Wochenkurve zu bearbeiten, öffne den gleichnamigen Menüpunkt.

## Bearbeitungskategorie Parameter

Wähle in dieser Bearbeitungskategorie die Anzeigeparameter für die Typische Wochenkurve aus. Standardmäßig liegen einer Typischen Wochenkurve die Daten aus der Version 'Historisch' zugrunde. Gib einen Wertetyp und einen Zeitraum an, für die Daten aus dem externen System in die Queue importiert wurden. Es ist aber auch möglich, die Typische Wochenkurve aus prognostizierten Daten in der Version 'Standard' zu erstellen.

| Queue | Wähle in diesem Feld die Queue aus, deren Daten Du kontrollieren oder bearbeiten möchtest. |
| Wertetyp | Wähle in diesem Feld den Wertetyp aus, dessen Wochenkurven Du kontrollieren oder bearbeiten möchtest. |
| Version | Wähle in diesem Feld die Version aus, deren Daten Du kontrollieren oder bearbeiten möchtest. In der Version 'Historisch' kannst Du aus dem externen System importierte Wochenkurven kontrollieren und für die Ermittlung einer Typischen Wochenkurve bearbeiten. In der Version 'Standard' kannst Du prognostizierte Wochenkurven kontrollieren und bearbeiten. |
| Wochenkurve | Wähle eine Wochenkurve, wenn Du die Typische Wochenkurve für eine von den eingestellten Parametern abweichende Queue-Wertetyp-Kombination speichern willst. Für die gleiche Queue-Wertetyp-Kombination wähle 'Standard'. Eine Typische Wochenkurve ist immer an eine bestimmte Queue-Wertetyp-Kombination gebunden. Du hast die Möglichkeit, benutzerdefinierte Wochenkurven anzulegen und diesen die Queue-Wertetyp-Kombination einer beliebigen Typischen Wochenkurve zuzuweisen. So kannst Du auf der Grundlage einer einzigen Wochenkurve einen Forecast für unterschiedliche Queue-Wertetyp-Kombinationen erstellen. |
| Länge der Wochenkurve | Gib die Anzahl der Wochen an, über die sich die Typische Wochenkurve erstrecken soll. Der Wertebereich liegt zwischen 1 und 55. Der Zeitraum für den Forecast entspricht der von Dir angegebenen Länge der Wochenkurve. Damit ist es möglich, Typische Wochenkurven und benutzerdefinierte Wochenkurven nicht nur über den Zeitraum einer Woche, sondern einer aus mehreren Wochen bestehenden Planperiode bis zu einem ganzen Jahr zu erstellen. Beachte, dass die Typische Wochenkurve am ersten Tag einer Planungswoche beginnt und am letzten Tag einer Planungswoche endet. |

> Wichtiger Hinweis
>
> Bitte beachte, dass die hier gewählte Länge auch immer Deinem Forecastzeitraum entspricht. Im nächsten Schritt der Prognose (*Prognose > ForecastPro > Forecast*{:.breadcrumbs}) kannst Du zwar den Startpunkt für den Forecast bestimmen, der Endpunkt wird jedoch anhand der Wochenkurvenlänge automatisch gesetzt. Das bedeutet, wenn Du beispielsweise eine Wochenkurve von der Länge 1 hast, Dein Planungsrhythmus jedoch fünf Wochen umfasst, musst Du den Forecast fünfmal durchführen, um für den gesamten Zeitraum Forecast-Werte zu erhalten.

| Startdatum | Gib das Startdatum an, ab dem die Wochenkurven angezeigt werden sollen. Für eine Typische Wochenkurve wird mindestens 1 Zeitraum von der Länge einer Wochenkurve (gewöhnlich aus der Version 'Historisch') benötigt. |
| Enddatum | Gib das Enddatum an, bis zu dem die Wochenkurven angezeigt werden sollen. |

Bestätige Deine Auswahl mit *Anwenden*{:.doc-button}. Das `Tabellenfenster`, `Diagrammfenster` und `Bearbeitungsfenster` werden eingeblendet.

Wenn bereits eine Typische Wochenkurve vorliegt, wird sie als Wochenkurve (gespeichert) (dicke schwarze Linie im Diagrammfenster) angezeigt. Diese Kurve kann nicht verändert werden.

Die Wochenkurve (aktuell) (dicke rote Linie) ist die aus den zugrunde liegenden Daten ermittelte Typische Wochenkurve. Sie berücksichtigt bereits den Verlauf der gespeicherten Typischen Wochenkurve mit einer Gewichtung von 50 %. Es werden nur die Daten zur Ermittlung der Tagessummen herangezogen, die innerhalb der Betriebszeiten der Queue liegen.

Pro Wertetyp erscheinen alle innerhalb des Zeitraums liegenden Wochenkurven.

Die Kurvendarstellung im Diagramm kannst Du wählen.

Du kannst den Verlauf einer Typischen Wochenkurve festlegen, indem Du die vorhandene Wochenkurve (aktuell) (dicke rote Linie) manuell bearbeitest (siehe [Typische Wochenkurve ohne Daten bearbeiten](#typische-wochenkurve-ohne-daten-bearbeiten)) oder eine Typische Wochenkurve anhand von importierten Daten erstellst (siehe [Typische Wochenkurve mit Kontrolle der Wochen-Versionswerte erstellen](#typische-wochenkurve-mit-kontrolle-der-wochen-versionswerte-erstellen)).

## Typische Wochenkurve ohne Daten bearbeiten

Fehlen für den eingestellten Zeitraum Daten aus dem externen System, stehen im `Tabellenfenster` Null-Werte. Im `Diagrammfenster` liegt der Verlauf der einzelnen Wochenkurven sowie der Wochenkurve (gespeichert) und der Wochenkurve (aktuell) ebenfalls bei null.

Du kannst den Verlauf der Wochenkurve (aktuell bzw. einer anderen beliebigen Kurve ohne Daten) manuell bearbeiten, indem Du

  - im `Tabellenfenster` die Werte direkt in die Spalte der Wochenkurve (aktuell) oder einer beliebigen Wochenkurve eingibst.
  - im `Diagrammfenster` die Verlaufspunkte der Wochenkurve (aktuell) oder einer beliebigen Wochenkurve manuell an die gewünschten Positionen ziehst.

Da eine Wochenkurve aus bis zu 55 Wochen bestehen kann, wird jeder in der Tabellenspalte aufgeführte Ereignistyp durch die entsprechende Nummer der Woche gekennzeichnet.

Solange Du die Werte noch nicht gespeichert hast, kannst Du die Änderungen am Kurvenverlauf in der Bearbeitungskategorie `Parameter` noch verwerfen. Klicke dazu auf *Anwenden*{:.doc-button}.

Wenn Du eine Wochenkurve (aktuell) erstellt hast, deren Verlauf Du als Typische Wochenkurve für den Forecast verwenden möchtest, klicke in der Bearbeitungskategorie `Parameter` auf *Speichern*{:.doc-button}.

Der Verlauf der Wochenkurve (gespeichert) (dicke schwarze Linie im Diagrammfenster) wird dabei überschrieben. Die bisherige Wochenkurve (aktuell) (dicke rote Linie) wird zur neuen Typischen Wochenkurve und aktualisiert die Wochenkurve (gespeichert).

## Typische Wochenkurve mit Kontrolle der Wochen-Versionswerte erstellen

Wochenkurven in der Version 'Historisch' zeigen die importierten Daten des Wertetyps pro Ereignistyp als Summen- oder Durchschnittswert an. In diesen Wert fließen nur die Daten ein, die innerhalb der Betriebszeit der Queue eingegangen sind.

Einzelne Kurven können untypische Werte enthalten, z.B. bei Ausfall des externen Systems. Durch eine manuelle Korrektur lässt sich ein typischer Wochenverlauf festlegen.

Du kannst die Wochenkurven manuell bearbeiten, indem Du im `Tabellenfenster` die Werte direkt in der Spalte der jeweiligen Kurve korrigierst und/oder im `Diagrammfenster` den Verlauf der fehlerhaften Wochenkurve manuell an die gewünschte Position ziehst.

Im `Bearbeitungsfenster` kannst Du einzelne Kurven gewichten. Da eine Wochenkurve aus bis zu 55 Wochen bestehen kann, wird jeder in der Tabellenspalte aufgeführte Ereignistyp durch die entsprechende Nummer der Woche gekennzeichnet.

> Hinweis
>
> Änderungen an den Wochenkurven wirken sich nicht auf gespeicherte Daten aus.

Im `Bearbeitungsfenster` kannst Du mit Hilfe der *Tendenz-Schaltflächen*{:.doc-button} eine Tendenz für die Gewichtung aller Kurven festlegen und Kurven einzeln mit Hilfe der Schieberegler  gewichten oder ganz von der Berechnung ausschließen.

Solange Du die Werte nicht gespeichert hast, kannst Du Änderungen am Kurvenverlauf in der Bearbeitungskategorie `Parameter` verwerfen. Klicke dazu auf *Anwenden*{:.doc-button}.

Wenn Du eine Wochenkurve (aktuell) erstellt hast, deren Verlauf Du als Typische Wochenkurve für den Forecast verwenden möchtest, klicke in der Bearbeitungskategorie `Parameter` auf *Speichern*{:.doc-button}.

Der Verlauf der Wochenkurve (gespeichert) (dicke schwarze Linie im Diagrammfenster) wird dabei überschrieben. Die bisherige Wochenkurve (aktuell) (dicke rote Linie) wird zur neuen Typischen Wochenkurve und die Wochenkurve (gespeichert) wird aktualisiert.
