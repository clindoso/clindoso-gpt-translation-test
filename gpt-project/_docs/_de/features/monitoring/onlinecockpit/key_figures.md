---
title: Kennzahlen für Queues, Aktivitäten & Schichten
product_label:
  - on-premise
---

Du kannst Dir die Gesamtwerte zu jedem Aktivitätstyp und Kennzahlen zu jeder einzelnen Aktivität anzeigen lassen.
Für jede Aktivität werden abhängig vom Aktivitätstyp Werte zum Mitarbeiterbedarf, zu den Ebenen Plan, Aktueller Stand und Externes System, zur Netto-Maximalkapazität, zur Besetzung, zur Deckung sowie die Anmeldungen für Schichten aus injixo Me ausgewertet.

{{ 1 | image: 'Gesamtwerte Kennzahlen', '50%' }}

## Queues

Alle Queues, die Du in der *Administration*{:.menu-item} angelegt hast, sowie alle exportierten Workloads werden unter Queues gelistet.
Die verfügbaren Kennzahlen sind die der Queue zugeordneten *Wertetypen*{:.menu-item}. Für jede Kennzahl kannst Du auswählen, welche Version ausgegeben werden soll. Dabei stehen Dir die Informationen aus den Versionen Historisch (z.B. für den Import aus der ACD), Forecast (für ForecastPro) und Auto-Forecast (für injixo Forecast) zur Verfügung.

## Aktivitäten

Alle im System verfügbaren Aktivitäten werden angezeigt und können einzeln oder mit den anderen verfügbaren Aktivitätstypen angezeigt werden

### Gesamtwerte

Gesamtwerte stellen Kennzahlen für Bedarf, Besetzung und Deckung zur Verfügung.

* **Gesamtbedarf**  
  Gesamtzahl an Mitarbeitern, die benötigt werden, um den im Forecast ermittelten Bedarf für alle Aktivitäten zu decken.

* **Gesamt-Besetzung**  
  Gesamtzahl der geplanten Mitarbeiter, für alle Aktivitäten vom Typ *Anwesenheit* in den Ebenen *Plan* oder *Aktueller Stand* bzw. die Anzahl der im externes System registrierten Mitarbeiter.

* **Gesamt-Deckung**  
  Differenz zwischen der Gesamtzahl der geplanten Mitarbeiter und dem Gesamt-Mitarbeiterbedarf für alle Aktivitäten vom Typ `Anwesenheit` für das angezeigte Intervall in der Ebene Plan.

Die Tageswerte zeigen Dir pro Tag die durchschnittliche Differenz pro Intervall zwischen allen geplanten Mitarbeitern und dem Gesamt-Mitarbeiterbedarf für alle Aktivitäten vom Typ `Anwesenheit`.

### Typ Anwesenheit

Die Angaben entsprechen für alle Aktivititätstypen der Anzeige in der entsprechenden Ebene im *Schicht Center*{:.menu-item} in *SchedulePro*{:.menu-item}.

* **Bedarf**  
  Bedarf an Mitarbeitern in der Planungseinheit für die gewählte Aktivität (Tagesintervallwerte). Für das angezeigte Intervall wird die Anzahl an Mitarbeitern angegeben, die benötigt wird, um den im Forecast ermittelten Bedarf zu decken.

* **Besetzung**  
  Anzahl der geplanten Mitarbeiter für die Aktivität und für das angezeigte Intervall (Tagesintervallwerte).

* **Deckung Plan**  
  Differenz zwischen der Anzahl der geplanten Mitarbeiter und dem Mitarbeiterbedarf für die Aktivität und für das angezeigte Intervall.

* **Netto-Maximalkapazität**  
  Maximal verfügbare Anzahl aller bereits für die Planungseinheit geplanten und für die Aktivität qualifizierten Mitarbeiter.

* **Besetzung/Deckung lt. Schichtbedarf**  
  Anzahl Schichten im angezeigten Intervall, die als Schichtbedarf hinterlegt bzw. erzeugt worden sind. Wie wäre die ausgewählte Aktivität besetzt, wenn alle dafür erzeugten Schichten mit Mitarbeitern besetzt würden. Deckung als Differenz zwischen der Kennzahl Besetzung lt. Schichtbedarf und dem Mitarbeiterbedarf für die ausgewählte Aktivität an.

* **Besetzung Externes System**  
  Anzahl der vom externen System registrierten Mitarbeiter für die Aktivität und für das angezeigte Intervall.

### Typ Meeting

Unter diesem Punkt werden alle in der *Administration*{:.menu-item} unter Stammdaten definierten und der Planungseinheit zugeordneten Aktivitäten vom Typ `Meeting` aufgeführt. Da mit diesem Aktivitätstyp ein kompletter Planungsworkflow genauso möglich ist, wie mit Aktivitäten vom Typ `Anwesenheit`, werden alle Kennzahlen angezeigt.

* Gesamt-Besetzung Plan/Aktueller Stand
* Bedarf
* Besetzung Plan/Aktueller Stand
* Deckung Plan/Aktueller Stand
* Besetzung lt. Schichtbedarf
* Deckung lt. Schichtbedarf
* Besetzung Externes System

### Typ Krankheit, Pause, Urlaub, Abwesenheit

Unter diesem Punkt werden alle in der *Administration*{:.menu-item} unter Stammdaten definierten und der Planungseinheit zugeordneten Aktivitäten vom Typ `Krankheit` aufgeführt.

* Gesamt-Besetzung Plan/Aktueller Stand
* Besetzung Plan/Aktueller Stand
* Anmeldungen
  Die Kennzahl Anmeldungen wird nur für die Aktivitäten dieses Typs angezeigt, wenn im Administrationsbereich das Kontrollkästchen Wünschbar aktiviert wurde. Für im Voraus planbare Krankheitsgründe der Mitarbeiter in der Planungseinheit zu nutzen (z.B. Kur, Therapie, Arztbesuch).

## Schichten

Du kannst Dir Kennzahlen zu allen Schichten, die Du im *Schicht Center*{:.menu-item} geplant hast, anzeigen lassen. Für alle Kennzahlen wird in der Ansicht Tagesintervallwerte die Anzahl der Schichten angezeigt. Wenn Du bei den Tagesmodellen Deiner Planungseinheit nicht **[Alle]** ausgewählt hast, werden Dir nur die hinterlegten Tagesmodelle in dieser Ansicht präsentiert.

### Kennzahlen

Pro Tagesmodell stehen folgende Kennzahlen zur Verfügung.

* **Anmeldungen**  
  Anzahl der von den Mitarbeitern gewünschten Schichten für die ausgewählte Schicht in der Planungseinheit und für das angezeigte Intervall (Tagesintervallwerte). Anzahl Schichten, die bereits gewünscht wurden (Tageswerte).

* **Bedarf**  
  Anzahl aller für die Planungseinheit und das ausgewählte Tagesmodell erzeugten Schichten pro Intervall. Anzahl der benötigten Schichten (Tageswerte).

* **Besetzung**  
  Besetzung der mit dem ausgewählten Tagesmodell erzeugten Schichten durch Mitarbeiter pro Intervall für die ausgewählte Planungseinheit. Anzahl der vergebenen Schichten (Tageswerte).

* **Deckungsdifferenz**  
  Differenz zwischen der Anzahl der tatsächlich besetzten Schichten und dem Schichtbedarf für die gewählte Schicht und für das angezeigte Intervall in der Planungseinheit an (Tagesintervallwerte). Differenz zwischen den tatsächlich besetzten und den erzeugten Schichten (Tageswerte).

* **Deckungsdifferenz mit Anmeldungen**  
  Differenz zwischen der Anzahl der tatsächlich besetzten Schichten und den gewünschten Schichten und dem Schichtbedarf für die gewählte Schicht und für das angezeigte Intervall in der Planungseinheit (Tagesintervallwerte).  Differenz zwischen den erzeugten, den tatsächlich besetzten und den gewünschten Schichten (Tageswerte).

> Hinweis
>
> Die Tageswerte zeigen für Aktivitäten Durchschnittswerte pro Tag innerhalb der Öffnungszeiten der Planungseinheit, bei Queues hängt es vom Typ des Ereignistyp ab, bei Summe werden auch Summen angezeigt. Die Tagesintervallwerte zeigen die Gesamtwerte pro Intervall, auch außerhalb der Öffnungszeiten.  
> Die Angaben entsprechen der Anzeige in der entsprechenden Ebene im *Schicht Center*{:.menu-item} in *SchedulePro*{:.menu-item}.
> <div>
