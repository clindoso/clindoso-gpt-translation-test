---
title: Typische Tageskurven
product_label:
  - on-premise
---

Im Menüpunkt *Typische Tageskurve*{:.menu-item} legst Du für jeden Ereignistyp - beispielsweise alle Wochentage und Sondertage - die Verteilung der prognostizierten Werte im Tagesverlauf fest. Die Typische Tageskurve wird im Forecast für die Verteilung des Wertetyps (z.B. Anzahl der eingehenden Anrufe oder durchschnittliche Bearbeitungsdauer) zugrunde gelegt. Das prognostizierte Basisvolumen verteilt sich anhand dieser Kurve auf den Ereignistyp.

> Hinweis
>
> Die Typische Tageskurve zeigt nur die Verteilung des Wertetyps an. Das tatsächlich erwartete Volumen wird erst beim Forecast ermittelt.

## Bearbeitungskategorie Parameter

Wähle die Anzeigeparameter für die Typische Tageskurve. Standardmäßig liegen einer Typischen Tageskurve die Daten aus der Version 'Historisch' zugrunde. Gib einen Wertetyp und einen Zeitraum an, für die Daten aus dem externen System in die Queue importiert wurden. Es ist ebenso möglich, die Typische Tageskurve mit prognostizierten Daten aus der Version 'Standard' zu erstellen.

| Queue | Wähle die Queue aus, deren Daten Du verwenden willst. |
| Wertetyp | Wähle den Wertetyp aus, dessen Daten Du kontrollieren oder bearbeiten willst. |
| Version | Wähle eine Version der Tageskurven aus. In der Version 'Historisch' kannst Du aus dem externen System importierte Tageskurven kontrollieren und für die Ermittlung einer Typischen Tageskurve bearbeiten. In der Version 'Standard' kannst Du prognostizierte Tageskurven weiterverarbeiten. |
| Startdatum | Gib das Startdatum an, ab dem die Tageskurven eines Ereignistyps angezeigt werden sollen. Für eine Typische Tageskurve wird mindestens eine Tageskurve des Ereignistyps (gewöhnlich aus der Version 'Historisch') benötigt. |
| Enddatum | Gib das Enddatum an, bis zu dem die Tageskurven eines Ereignistyps angezeigt werden sollen. |
| Ereignistyp | Wähle den Ereignistyp aus, dessen Tageskurven Du kontrollieren oder bearbeiten möchtest. Es werden Dir nur die Ereignistypen angeboten, die der ausgewählten Queue in der Administration zugeordnet wurden. |

Bestätige Deine Auswahl mit *Anwenden*{:.doc-button}. Das Tabellenfenster, Diagrammfenster und Bearbeitungsfenster wird eingeblendet. Wenn bereits eine Typische Tageskurve vorliegt, wird sie als Tageskurve (gespeichert) (dicke schwarze Linie im Diagrammfenster) angezeigt. Diese Kurve kannst Du manuell nicht verändern.

Die Tageskurve (aktuell) (dicke rote Linie im Diagrammfenster) ist die aktuelle Typische Tageskurve. Sie berücksichtigt bereits den Verlauf der gespeicherten Typischen Tageskurve mit einer Gewichtung von 50 %. Es werden nur die Daten zur Ermittlung des Verlaufs herangezogen, die innerhalb der Betriebszeiten der Queue liegen. Pro Wertetyp-Ereignistyp-Kombination erscheinen alle innerhalb des Zeitraums liegenden Tageskurven.

Für die Kurvendarstellung im Diagramm kannst Du zwischen einer Stufen-, Linien- und Balkenform wählen. Du kannst den Verlauf einer Typischen Tageskurve festlegen, indem Du die Tageskurve (aktuell) (dicke rote Linie) manuell bearbeitest oder eine Typische Tageskurve anhand von importierten Daten ermittelst.

## Typische Tageskurve ohne Daten anlegen

Fehlen Dir für den eingestellten Zeitraum Daten aus dem externen System, stehen im Tabellenfenster Null-Werte. Im Diagrammfenster liegt der Verlauf der einzelnen Tageskurven sowie die Tageskurve (aktuell) ebenfalls bei null.

Du kannst den Verlauf der Tageskurve (aktuell bzw. einer anderen beliebigen Kurve ohne Daten) manuell bearbeiten, indem Du

  - im `Tabellenfenster` die Werte direkt in die Spalte der Tageskurve eingibst.
  - im `Diagrammfenster` die Verlaufspunkte der Tageskurve manuell an die gewünschten Positionen ziehst.

> Hinweis
>
> Im Menüpunkt *Tageskurven bearbeiten*{:.menu-item} lassen sich Kurven durch ein automatisiertes Verfahren ebenfalls berechnen oder bearbeiten.

Die Änderungen am Verlauf der Tageskurven werden nicht automatisch gespeichert.

Wenn Du in der Version 'Historisch' bearbeitete Daten wirklich speichern möchtest, klicke auf die Schaltfläche *Versionsdaten speichern*{:.doc-button}. Durch das Speichern der Versionsdaten in der Version 'Historisch' überschreibst Du Deine importierten Daten. Solange Du die Werte noch nicht gespeichert hast, kannst Du die Änderungen am Kurvenverlauf in der Bearbeitungskategorie `Parameter` noch verwerfen. Klicke dazu auf *Anwenden*{:.doc-button}.

Wenn Du eine Tageskurve (aktuell) erstellt hast, deren Verlauf Du als Typische Tageskurve für den Forecast verwenden möchtest, klicke in der Bearbeitungskategorie `Parameter` auf *Speichern*{:.doc-button}.

Der Verlauf der Tageskurve (gespeichert) (dicke schwarze Linie im Diagrammfenster) wird dabei überschrieben. Die bisherige Tageskurve (aktuell) (dicke rote Linie) wird zur neuen Typischen Tageskurve und aktualisiert die Tageskurve (gespeichert).

## Typische Tageskurve mit Kontrolle der Tages-Versionswerte erstellen

Tageskurven in der Version 'Historisch' zeigen die importierten Daten für einen Zeitraum von 24 Stunden an. Die Typische Tageskurve berücksichtigt aus allen importierten Daten nur die Werte, die innerhalb der Betriebszeiten der Queue liegen.

Du kannst an den Tageskurven sehen, ob Vorgänge auch außerhalb der Betriebszeiten der Queue stattfinden und ob deren Quantität eventuell eine Erweiterung der Betriebszeiten erforderlich macht. Einzelne Kurven können untypische Werte enthalten, z.B. bei Ausfall des externen Systems. Durch eine manuelle Korrektur lässt sich ein typischer Tagesverlauf festlegen.

Die Daten der einzelnen Kurven werden in dem Intervall angezeigt, was in der Administration für die Queue angegeben wurde.

Du kannst die einzelnen Tageskurven manuell bearbeiten, indem Du

  - im Tabellenfenster die Werte direkt in der Spalte der jeweiligen Kurve korrigierst.
  - im Diagrammfenster den Verlauf der fehlerhaften Tageskurve an die gewünschte Position ziehst.
  - im Bearbeitungsfenster einzelne Kurven gewichtest.

Die Änderungen am Verlauf der Tageskurven werden nicht automatisch gespeichert. Wenn Du in der Version 'Historisch' bearbeitete Daten wirklich speichern willst, klicke auf *Versionsdaten speichern*{:.doc-button}. Durch das Speichern der Versionsdaten in der Version 'Historisch' überschreibst Du Deine importierten Daten.

Im Bearbeitungsfenster kannst Du mit Hilfe der *Tendenz-Schaltflächen*{:.doc-button} eine Tendenz für die Gewichtung aller Kurven festlegen. Außerdem kannst Du Kurven auch einzeln mit Hilfe der Schieberegler gewichten oder ganz von der Berechnung ausschließen.

Solange Du die Werte nicht gespeichert hast, kannst Du Deine Änderungen am Kurvenverlauf in der Bearbeitungskategorie `Parameter` verwerfen. Klicke dazu auf *Anwenden*{:.doc-button}.

Wenn Du eine Tageskurve (aktuell) erstellt hast, deren Verlauf Du als Typische Tageskurve für den Forecast verwenden möchtest, speicher die Kurve in der Bearbeitungskategorie `Parameter`, indem Du auf *Speichern*{:.doc-button} klickst.

Der Verlauf der Tageskurve (gespeichert) (dicke schwarze Linie im Diagrammfenster) wird dabei überschrieben. Die bisherige Tageskurve (aktuell) (dicke rote Linie) wird zur neuen Typischen Tageskurve und aktualisiert die Tageskurve (gespeichert).
