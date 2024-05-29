---
title: Ersatzmitarbeiter für Aktivitäten, ganze Tage oder unterbesetzte Schichten finden
product_label:
  - advanced
  - enterprise
  - classic
description: Finde Mitarbeiter, die bei Abwesenheiten oder unterbesetzten Schichten unterstützen. Tausche Schichten zwischen zwei Mitarbeitern.
redirect_from: /de/find-functions/
redirect_reason: renamed file in March 2021
---

In diesem Artikel lernst Du, wie Du:

- einen Ersatzmitarbeiter für eine bestimmte Aktivität oder Schicht oder für einen ganzen Tag findest.
- Mitarbeiter für unterbesetzte Schichten findest.
- Aktivitäten und Tagesmodelle zwischen zwei Mitarbeitern tauschst.

Neu im Schicht Center? Lerne zuerst {% link_new die Grundlagen | features/scheduling/shiftcenter/shift-center-overview.md %}

## Ersatzmitarbeiter für einzelne Aktivitäten und ganze Tage finden

Wenn ein geplanter Mitarbeiter eine bestimmte Aktivität oder Schicht nicht ausführen oder einen ganzen Tag lang nicht arbeiten kann (z.B. wegen Krankheit), musst Du einen Ersatzmitarbeiter finden. Dieser Mitarbeiter braucht die Qualifikationen, um die jeweiligen Aktivitäten oder Schichten übernehmen zu können.

Um einen Ersatzmitarbeiter für einen ganzen Tag zu finden:

1. Klicke im Planfenster auf die **Spaltenüberschrift eines Tages**, um den Tag auszuklappen.
2. Klicke mit der rechten Maustaste auf eine **Zelle** im ausgeklappten Tag.
3. Wähle **Ersatzmitarbeiter für Tag finden...** oder drücke **Strg + Q**.

Um einen Ersatz für eine einzelne Aktivität zu finden:

1. Klicke im Planfenster mit der rechten Maustaste auf die jeweilige **Aktivität** in einem ausgeklappten Tag.
2. Wähle **Ersatzmitarbeiter finden...** oder drücke **STRG + R**.

{{ 1 | image: "Ersatzmitarbeiter finden Kontextmenü", '50%' }}

In beiden Fällen erscheint eine Liste von Mitarbeitern, die über die Qualifikationen verfügen, die Aktivitäten oder Schichten zu übernehmen. Du kannst jetzt zusätzliche Optionen auswählen, um die in der Liste angezeigten Mitarbeiter weiter zu filtern:

1. Klicke auf den Tab **Optionen**.
   - Wähle in der Zeile _Auswahl_ die Option **Beachten**, wenn Du nur Ersatzmitarbeiter anzeigen möchtest, die zur gleichen Auswahlgruppe gehören wie der Mitarbeiter.
   - In der Zeile _Einsatz_ kannst Du entscheiden, ob Du nur Mitarbeiter **Mit gleicher Arbeitszeit und gleichem Datum**, mit **Mindestens einer am gleichen Buchungstag** oder mit **Keiner am gleichen Buchungstag** anzeigen möchtest. Die letzten beiden Optionen beziehen sich darauf, ob bereits Elemente im Schichtplan des Mitarbeiters am Buchungstag vorhanden sind oder nicht.
2. Gehe zurück auf den Tab **Ersatzmitarbeiter**. Wenn es keine Ersatzmitarbeiter gibt, die Deinen Filterkriterien entsprechen, bleibt der Tab inaktiv. Andernfalls zeigt er qualifizierte Mitarbeiter an, die Deinen Filterkriterien entsprechen.
3. Klicke auf einen **Ersatzmitarbeiter**. Die Zeile wird hervorgehoben. Beachte, dass die Mitarbeiter an diesem Tag bereits Aktivitäten oder Schichten in ihrem Schichtplan haben könnten, die (teilweise) ersetzt werden.
   {{ 2 | image: "Details zum Ersatzmitarbeiter finden", '60%' }}
4. Klicke auf _Ok_{:.doc-button}. Bevor die Ersetzung durchgeführt wird, prüft injixo, ob die Planungsregeln eingehalten wurden. Die Elemente werden dann auf den ausgewählten Mitarbeiter übertragen.

## Mitarbeiter für unterbesetzte Schichten finden

Das Kennzahlenfenster zeigt unterbesetzte Schichten in rot an. Um einen Mitarbeiter für eine unterbesetzte Schicht zu finden:

1. Wechsle auf den Tab **Tagesmodelle**.
2. Klicke mit der rechten Maustaste auf eine **Daten-Zelle** und wähle **Mitarbeiter für Schicht finden...**.
   {{ 3 | image: "Details zum Ersatzmitarbeiter finden", '60%' }}

3. Im Tab **Mitarbeiter** siehst Du das Tagesmodell und dessen Startzeit. Bei Tagesmodellen vom Typ _Variable Schicht_ kannst Du die **Startzeit** anpassen. Unten siehst Du eine Liste von Mitarbeitern, die für die von Dir gewählte unterbesetzte Schicht verfügbar sind.
   {{ 4 | image: "Details zum Ersatzmitarbeiter Tagesmodell auswählen", '60%' }}
4. Klicke auf den Tab **Optionen**. Hier kannst Du die in der Liste angezeigten Mitarbeiter weiter filtern. Wenn Du **Keiner am gleichen Buchungstag** bei _Einsatz_ auswählst, werden nur die Mitarbeiter angezeigt, die an dem ausgewählten Tag keine Elemente im Schichtplan haben.
5. Gehe zurück auf den Tab **Mitarbeiter**. Wenn es keine Ersatzmitarbeiter gibt, die Deine Filterkriterien erfüllen, bleibt der Tab inaktiv. Andernfalls zeigt er qualifizierte Mitarbeiter an, die Deinen Filterkriterien entsprechen.
6. Wähle einen **Mitarbeiter** aus. Beachte, dass die Mitarbeiter an diesem Tag bereits Aktivitäten oder Schichten in ihrem Schichtplan haben könnten, die (teilweise) ersetzt werden.
7. Bestätige die Zuweisung des Tagesmodells mit _Ok_{:.doc-button}. Bevor die Zuweisung durchgeführt wird, prüft injixo, ob die Planungsregeln eingehalten wurden.

## Schichten zwischen zwei Mitarbeitern tauschen

<!-- move into separate article -->

Du kannst alle Aktivitäten und Schichten eines bestimmten Tages zwischen zwei Mitarbeitern tauschen.

1. Klicke mit der rechten Maustaste auf eine **Tageszelle** im Planfenster.
2. Wähle **Tauschpartner finden**. Es erscheint eine Liste mit Mitarbeitern, deren Fähigkeiten und Vertragsparameter mit denen des ausgewählten Mitarbeiters übereinstimmen.
   {{ 5 | image: "Kontextmenü Tauschpartner finden", '60%' }}
3. Klicke auf den Tab **Optionen**, um zusätzliche Filterkriterien auszuwählen.
   - Wähle in der Zeile _Auswahl_ die Option **Beachten**, wenn Du nur Ersatzmitarbeiter anzeigen möchtest, die zur gleichen Auswahlgruppe gehören wie der Mitarbeiter.
   - In der Zeile _Einsatz_ kannst Du Dich entscheiden, nur Mitarbeiter **Mit gleicher Arbeitszeit und gleichem Datum**, mit **Mindestens einer am gleichen Buchungstag** oder mit **Keiner am gleichen Buchungstag** anzuzeigen. Die letzten beiden Optionen beziehen sich darauf, ob bereits Elemente im Schichtplan des Mitarbeiters am Buchungstag vorhanden sind oder nicht.
4. Gehe zurück auf den Tab **Tauschpartner finden**. Wenn es keine Austauschmitarbeiter gibt, die Deine Filterkriterien erfüllen, bleibt der Tab inaktiv. Ansonsten zeigt er qualifizierte Mitarbeiter an, die Deine Filterkriterien erfüllen.
5. Wähle einen **Mitarbeiter** aus und klicke auf _Ok_{:.doc-button}, um den Austausch zu bestätigen. Bevor der Austausch durchgeführt wird, prüft injixo, ob die Planungsregeln eingehalten wurden.
   {{ 6 | image: "Tauschpartner auswählen ", '60%' }}
