---
title: Schichtfolgen erstellen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Verwende Schichtfolgen für wiederkehrende Schichtpläne.
redirect_from:
  - /shift-sequence-overview/
redirect_reason: filename used in old product onboarding
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-insert-shift-sequences.md
---

Eine Schichtfolge ist eine Abfolge von Tagesmodellen oder Aktivitäten in einem Wochenmuster. Mit Schichtfolgen kannst du diese wiederkehrenden Muster schnell in deinen Schichtplan einfügen. injixo optimiert dann den Rest deines Schichtplans.

Schichtfolgen sparen dir zahlreiche Arbeitsstunden, da du wiederkehrende Muster nicht jedes Mal manuell planen musst.

Es gibt vier Anwendungsfälle für Schichtfolgen:

- Anwendungsfall 1: Tage angeben, an denen bestimmte Schichten geplant werden müssen
- Anwendungsfall 2: Wiederkehrende Aktivitäten planen
- Anwendungsfall 3: Tage angeben, an denen Mitarbeiter nicht arbeiten
- Anwendungsfall 4: Angeben, wann Schichten auf Basis der Mitarbeiterverfügbarkeiten geplant werden können

Schichtfolgen bestehen aus einer oder mehreren Zeilen. Jede Zeile steht für ein individuelles Muster, das in den Schichtplan eingefügt werden kann.<br>
Jede Zeile enthält Zellen, die die Wochentage repräsentieren. In diese Zellen fügst du die Tagesmodelle oder Aktivitäten ein, die du mit der jeweiligen Schichtfolge planen möchtest.<br>
Jede Zeile steht für ein wöchentliches Muster in deinem Schichtplan. Deshalb muss die Anzahl der Zellen in einer Zeile ein Vielfaches von sieben sein. Eine Schichtfolge kann höchstens 53&nbsp;Zeilen haben, da sie nicht länger als ein Jahr laufen kann.

## Voraussetzungen

Um Schichtfolgen zu erstellen, musst du zunächst {% link_new Aktivitäten | features/administration/activities.md %} oder {% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %} erstellen.<br>
Wenn du Schichtfolgen erstellt hast, musst du sie {% link_new deinen Mitarbeitern zuweisen | features/administration/employee-overview.md | #eine-schichtfolge-zuweisen %}, bevor du sie in deinen Schichtplan einfügen kannst.<br>
Wenn du einem Mitarbeiter eine Schichtfolge zuweist, musst du ein Referenzdatum setzen. Das Referenzdatum ist der Tag, ab dem die Schichtfolge in der Planung verwendet wird. Ab diesem Datum wird die Schichtfolge ohne Unterbrechung wiederholt, solange sie gültig ist.<br>
Weil Schichtfolgen als Wochenmuster angelegt werden, setze das Referenzdatum auf einen Montag bzw. auf den Wochentag, an dem deine Arbeitswoche beginnt.

>Hinweis
>
>Standardmäßig beginnt die Arbeitswoche am Montag.
>
>Du kannst den Tag für den Wochenbeginn mit der Einstellung _48420_{:.id-label} _Wochenbeginn (Planung)_ ändern.

## Schichtfolgen erstellen

Bevor du deine erste Schichtfolge erstellst, lege fest, wie viele Schichtfolgen du benötigst und wie viele Zeilen und Zellen diese jeweils enthalten sollen. Dies hängt ausschließlich von den Anforderungen deines Unternehmens ab, z.&nbsp;B. wie viele verschiedene Schichten geplant werden sollen, ob es wiederkehrende Meetings gibt usw.

Um Schichtfolgen zu erstellen, gehe zu _Plan > Konfiguration > Schichtfolgen_{:.breadcrumbs} und gehe wie folgt vor:

1. Klicke oben links auf das Neu-Icon {% icon item-add | icon-only %}.
2. Konfiguriere die Schichtfolge:<br>
  **Name**: Gib einen eindeutigen Namen ein (max. 50 Zeichen).<br>
  **Kurzbezeichnung**: Gib den Namen oder eine Kurzversion davon ein (max. 25 Zeichen).<br>
  **Mitarbeiterzeile(n)**: Gib die Anzahl der Mitarbeiterzeilen für die Schichtfolge ein (max. 53).<br>Jeder Zeile wird eine Nummer zugewiesen. Doppelklicke auf eine Zeile, um sie umzubenennen. Um die Zeile später einem Mitarbeiter zuzuweisen, benötigst du die Nummer bzw. den Namen der Zeile.<br>
  **Länge**: Gib einen Wert zwischen 7 und 371 Tagen ein. Die Länge muss ein Vielfaches von sieben sein.
6. Klicke auf _OK_{:.doc-button}.

>Hinweis
>
>Die Länge der Schichtfolge muss immer ein Vielfaches von sieben sein, auch wenn dein Unternehmen nur an fünf oder sechs Tagen pro Woche geöffnet ist. Schichtfolgen wiederholen sich automatisch. Eine Schichtfolge von 5&nbsp;Tagen würde die Montagsschicht in eine Samstagszelle einfügen, die Dienstagsschicht in eine Sonntagszelle usw.
>
>Wenn du Muster mit unterschiedlichen Längen planen möchtest (z.&nbsp;B. eines für wöchentliche Meetings und eines für zweiwöchentliche Meetings), musst du separate Schichtfolgen erstellen.

Wenn du eine Schichtfolge erstellst hast, kannst du den {% link_new Gültigkeitszeitraum | features/administration/set-a-validity-period.md %} dafür festlegen:

1. Klicke auf das {% icon item-edit %} über der Tabelle.
2. Gib in den Feldern **Gültig vom** und **Gültig bis** die Daten ein bzw. wähle sie aus.
3. Klicke auf _OK_{:.doc-button}.

### Tagesmodelle einfügen

1. Wähle in der Kachel **Optionen** rechts oberhalb der Tabelle im Dropdown-Menü die Option **Tagesmodell einfügen**.
2. Wähle das Tagesmodell, das du einfügen möchtest, aus dem Dropdown-Menü **Tagesmodell** aus.
3. Gib eine Anzahl ein. Dies ist die Anzahl aufeinanderfolgender Tage, an denen du das Tagesmodell einfügen möchtest.
4. Klicke in der Tabelle auf die erste Zelle, in die du das Tagesmodell einfügen möchtest.<br>
  Wenn du eine Anzahl größer eins eingegeben hast, wird das Tagesmodell in diese Zelle und die rechts davon folgenden Zellen eingefügt, bis die festgelegte Anzahl erreicht ist.

Die Schichtfolge wird automatisch gespeichert.

> Tipp
>
> Verwende Aktivitäten oder fixe Tagesmodelle. Wenn du variable Tagesmodelle in eine Schichtfolge einfügen möchtest, beginnt die Schicht immer zum frühestmöglichen Zeitpunkt.

### Aktivitäten einfügen

1. Wähle in der Kachel **Optionen** rechts oberhalb der Tabelle im Dropdown-Menü die Option **Aktivität einfügen**.
2. Wähle die Aktivität, die du einfügen möchtest, aus dem Dropdown-Menü **Aktivität** aus.
3. Gib eine Anzahl ein. Dies ist die Anzahl aufeinanderfolgender Tage, an denen du die Aktivität einfügen möchtest.
4. Um festzulegen, zu welcher Zeit die Aktivität geplant werden soll, gib einen Zeitraum (24-Stunden-Format) in die Felder **von** und **bis** ein oder aktiviere die Checkbox **Ganztägig**.
5. Klicke in der Tabelle auf die erste Zelle, in die du die Aktivität einfügen möchtest.<br>
  Wenn du eine Anzahl größer eins eingegeben hast, wird die Aktivität in diese Zelle und die rechts davon folgenden Zellen eingefügt, bis die festgelegte Anzahl erreicht ist.

> Aktivitäten, die nach Mitternacht enden
>
> Wenn du Aktivitäten einfügen möchtest, die nach Mitternacht enden, füge 24 zur Endzeit hinzu, z.&nbsp;B. wenn die Aktivität um 1:00&nbsp;Uhr am nächsten Tag enden soll, gib 25:00 ein.

## Schichtfolgen bearbeiten

1. Wähle in der Kachel **Schichtfolge** links oberhalb der Tabelle eine Schichtfolge aus dem Dropdown-Menü aus.
2. Klicke auf _Anwenden_{:.doc-button}.
3. Klicke auf den {% icon item-edit %} in der oberen Aktionsleiste, um den Namen, die Kurzbezeichnung, die Anzahl der Mitarbeiterzeilen und die Länge zu bearbeiten.<br>Wenn du fertig bist, klicke auf _OK_{:.doc-button}.
4. Klicke in der Aktionsleiste über der Tabelle auf den {% icon item-edit %}, um die Gültigkeitszeiträume zu bearbeiten.<br>Wenn du fertig bist, klicke auf _OK_{:.doc-button}.

### Elemente aus einer Schichtfolge löschen

Um ein oder mehrere Elemente aus der Schichtfolge zu löschen, gehe wie folgt vor:
1. Wähle in der Kachel **Schichtfolge** links oberhalb der Tabelle eine Schichtfolge aus dem Dropdown-Menü aus.
2. Klicke auf _Anwenden_{:.doc-button}.
3. Wähle in der Kachel **Optionen** aus dem Dropdown-Menü die Option **Löschen** aus.
4. Klicke auf die Zellen, deren Elemente du löschen möchtest.<br>
  Die Elemente werden automatisch gelöscht.

Um alle Elemente aus einer Schichtfolge zu löschen, gehe wie folgt vor:

1. Wähle in der Kachel **Schichtfolge** links oberhalb der Tabelle eine Schichtfolge aus dem Dropdown-Menü aus.
2. Klicke auf _Anwenden_{:.doc-button}.
3. Wähle in der Kachel **Optionen** aus dem Dropdown-Menü die Option **Löschen** aus.
4. Aktiviere die Checkbox **Alles löschen** und klicke auf _Anwenden_{:.doc-button}.<br>
  Die Elemente werden automatisch gelöscht.

## Schichtfolgen löschen

1. Wähle in der Kachel **Schichtfolge** links oberhalb der Tabelle eine Schichtfolge aus dem Dropdown-Menü aus.
2. Klicke auf _Anwenden_{:.doc-button}.
3. Klicke in der oberen Aktionsleiste auf das {% icon item-delete %}.
4. Klicke im Bestätigungsdialog auf _Ja_{:.doc-button}.

## Anwendungsfälle

Du kannst Schichtfolgen für diverse Anwendungsfälle verwenden.

### Anwendungsfall 1: Tage angeben, an denen bestimmte Schichten geplant werden müssen

Dieser Anwendungsfall ist relevant, wenn du zum Beispiel Früh- und Spätschichten für verschiedene Gruppen von Mitarbeitern planen möchtest. Oder wenn einer deiner Mitarbeiter montags nicht vor 11&nbsp;Uhr arbeiten kann, obwohl er an allen anderen Wochentagen früher verfügbar ist. 
 
Erfahre im folgenden Academy-Trainingsvideo mehr darüber, ob dieser Anwendungsfall auf dich zutrifft und wie du dementsprechend deine Schichtfolgen konfigurieren musst:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-1.vtt" kind="subtitles" srclang="en" label="English" default>
   </video>
</div>
<br>

### Anwendungsfall 2: Wiederkehrende Aktivitäten planen

Dieser Anwendungsfall ist z.&nbsp;B. relevant, wenn du wöchentlich stattfindende Meetings planen möchtest oder wenn du einen Mitarbeiter jeden Tag zu einer bestimmten Zeit für eine Stunde Backoffice-Tätigkeiten planen möchtest.

Erfahre im folgenden Academy-Trainingsvideo mehr darüber, ob dieser Anwendungsfall auf dich zutrifft und wie du dementsprechend deine Schichtfolgen konfigurieren musst:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-2.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-2.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

### Anwendungsfall 3: Tage angeben, an denen Mitarbeiter nicht arbeiten

Dieser Anwendungsfall ist z.&nbsp;B. relevant, wenn du für einzelne Mitarbeiter bestimmte Muster von Abwesenheiten festlegen möchtest. 

Erfahre im folgenden Academy-Trainingsvideo mehr darüber, ob dieser Anwendungsfall auf dich zutrifft und wie du dementsprechend deine Schichtfolgen konfigurieren musst:

  <div class="inline-video-container">
    <video class="inline-video-player-v" controls> 
     <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-3.mp4" type="video/mp4">
     <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-3.vtt" kind="subtitles" srclang="en" label="English" default>
    </video>
  </div>
<br>

### Anwendungsfall 4: Angeben, wann Schichten auf Basis der Mitarbeiterverfügbarkeiten geplant werden können

Dieser Anwendungsfall ist relevant, wenn du Mitarbeiter mit unterschiedlichen Verfügbarkeiten planen möchtest.

Erfahre im folgenden Academy-Trainingsvideo mehr darüber, ob dieser Anwendungsfall auf dich zutrifft und wie du dementsprechend deine Schichtfolgen konfigurieren musst:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-4.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-4.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

## Report erzeugen

Du kannst einen Report im PDF-Format erzeugen, der alle Daten zu einer Schichtfolge enthält. Um den Report zu erzeugen, gehe wie folgt vor:

1. Wähle in der Kachel **Schichtfolge** links oberhalb der Tabelle die Schichtfolge aus dem Dropdown-Menü aus, für die du einen Report erzeugen möchtest.
2. Klicke auf _Anwenden_{:.doc-button}.
3. Klicke direkt über der Tabelle auf _Report_{:.doc-button}.
4. Im Dialog kannst du die Checkbox aktivieren, um den Report an deine injixo-E-Mail-Adresse zu senden.

Der Report zeigt die Start- und Endzeiten der Aktivitäten oder Tagesmodelle, die in der Schichtfolge enthalten sind, sowie ihre Nettodauer in Stunden. Der Report ist nach Wochen strukturiert.
Zusätzlich zeigt der Report die folgenden Gesamt- und Durchschnittswerte der Nettodauer:

- Zeile **Summe**: Nettodauer aller Aktivitäten oder Tagesmodelle in der Schichtfolge.
- Spalte **Summe**: Gesamtsumme der Nettodauer der Aktivitäten oder Tagesmodelle pro Woche.
- Zeile **Durchschnitt**: Durchschnittswert für alle Werte in der Zeile **Summe**.
