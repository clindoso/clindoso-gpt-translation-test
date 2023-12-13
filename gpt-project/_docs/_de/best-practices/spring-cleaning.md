---
title: Anleitung zum Frühjahrsputz
promote-service: health-check
---

Wenn in Deinem Unternehmen injixo bereits eine Weile im Einsatz ist oder ihr in letzter Zeit verschiedene Anpassungen vorgenommen habt, wird es Zeit für einen Frühjahrsputz!
Damit stellst Du sicher, dass Dein injixo auch weiterhin aufgeräumt ist und Du problemlos den Überblick behältst.
Um zu vermeiden, dass Du noch benötigte Daten löschst, geben wir Dir im Folgenden einige Tipps, wie Du dabei am besten vorgehst.

Allgemeine Hinweise zum Löschen von Stammdaten:

- Bevor Du etwas löschst, stelle sicher, dass Du nicht gegen die Datenaufbewahrungspflicht verstößt. Lösche niemals überstürzt Informationen, die Deine Plandaten beeinflussen können. Beispielsweise kann das Löschen eines Vertrages dazu führen, dass die Arbeitszeitberechnung Deiner Mitarbeiter nicht mehr stimmt. Überprüfe daher vorab, welche Unternehmensrichtlinien zur Aufbewahrung von Informationen bei Dir gelten, bevor Du wichtige Daten (z. B. für die Abrechnung) entfernst.
- Die meisten Stammdaten sind miteinander verknüpft. Starte daher immer am Ende der Stammdatenliste und löse bestehende Verknüpfungen zunächst auf. Ansonsten können dadurch Probleme in Deiner Planung oder korrupte Daten entstehen.

    {{ 1 | image: 'Reihenfolge beim Löschen von Stammdaten', '20%'}}

- Wenn Stammdaten in kursiv geschrieben sind (z. B. Aktivitäten im *Schicht Center*{:.menu-item}), bedeutet das, dass die Stammdaten an sich bereits gelöscht wurden, die Verknüpfung aber weiterhin besteht. Um die Übersicht zu behalten, solltest Du diese Verknüpfungen ebenfalls entfernen.

    {{ 2 | image: 'Beispiel für korrupte Daten', '20%'}}

## Ausgetretene Mitarbeiter
Mitarbeiter kündigen, werden in einen anderen Bereich versetzt oder gehen in Rente. Fluktuation ist einer der häufigsten Gründe, warum Dein injixo veraltete Daten enthält. Bevor Du jedoch Daten löschst, prüfe, wie lange die Daten gespeichert werden müssen. Nach Ablauf der Aufbewahrungsfrist kannst Du im Flukationsreport herausfinden, wessen Betriebszugehörigkeit zum entsprechenden Zeitpunkt ausgelaufen ist.

Folge diesen Schritten:

1. Überprüfe in *WFM > Administration > Scheduling > Mitarbeiter*{:.breadcrumbs} die Mitarbeiter mit einem entsprechenden Austrittsdatum und lösche sie.
2. Zusätzlich solltest Du kontrollieren, ob für diese Mitarbeiter individuelle Stammdaten angelegt wurden z.B. *Verträge*{:.menu-item} oder *Tagesmodelle*{:.menu-item}.

Zum besseren Verständnis haben wir Dir die beiden Schritte in diesem GIF veranschaulicht:
{{ 3 | image: 'Schritte zum Löschen eines Mitarbeiters', '100%', 'gif' }}


## Anpassungen am Schicht-Setup
Wenn Du kürzlich Änderungen an Deinem Schicht-Setup vorgenommen hast, existieren in Deinem injixo vermutlich noch veraltete Tagesmodelle.
Bevor Du Tagesmodelle löschst, stelle sicher, dass die Tagesmodelle nicht in Deinem aktuellen Planungszyklus verwendet werden. Besonders wenn Du das Schicht-Wunsch-Verfahren nutzt, solltest Du darauf achten, dass keine offenen Schichtwünsche vorliegen. Andernfalls können diese ungültig werden.
Um sicherzustellen, dass durch das Löschen keine Probleme in Deinem nächsten Planungsdurchlauf entstehen, folge diesen Schritten in *WFM > Administration > Scheduling*{:.breadcrumbs}:

1. Prüfe in *Mitarbeiter*{:.menu-item}, ob die veralteten Tagesmodelle irgendwelchen Mitarbeitern direkt zugeordnet sind.
2. Kontrolliere in *Planungseinheiten*{:.menu-item}, ob in dem Abschnitt **Tagesmodelle** die Option *[ALLE]* ausgewählt ist. Wenn nicht, entferne die entsprechenden Tagesmodelle aus der Liste.
3. Überprüfe in *Schichtfolgen*{:.menu-item}, ob die zu löschenden Tagesmodelle in einer Schichtfolge enthalten sind. Du kannst sie entweder löschen oder direkt ersetzen.
4. Prüfe in *Wochenmodelle*{:.menu-item}, ob das Tagesmodell in einem Wochenmodell enthalten ist. Das ist besonders wichtig, wenn es das einzige Tagesmodell im Wochenmodell ist. In diesem Fall wird das gesamte Planungsmodell ungültig.
5. Lösche das Tagesmodell in *Tagesmodelle*{:.menu-item}.

Alle Schritte haben wir Dir hier an einem Beispiel verdeutlicht:
{{ 4 | image: 'Schritte zum Löschen eines Tagesmodells', '100%', 'gif' }}

## Neuordnung und Umstrukturierungen im Unternehmen
Gab es in Deinem Unternehmen strukturelle Veränderungen? Zum Beispiel hast Du zusätzliche Verantwortungsbereiche übernommen oder Du hast Aufgaben an einen externen Dienstleister delegiert. Dementsprechend wirst Du auch die Struktur in injixo angepasst haben. Daraus können Altlasten resultieren, die Du bisher noch nicht aufgeräumt hast. Das betrifft vor allem Auswahlen und Planungseinheiten. Um Dich dieser ordnungsgemäß zu entledigen, folge den nachfolgenden Schritten im *WFM > Administration > Scheduling*{:.breadcrumbs}:

1. Prüfe unter *Mitarbeiter*{:.menu-item}, ob die Auswahl oder Planungseinheit noch Mitarbeitern zugewiesen ist. Falls ja, kannst Du die Zuordnung über die Massenbearbeitung löschen.
2. Gehe zu *Auswahlen*{:.menu-item} und überprüfe, ob die Auswahl einer anderen untergeordnet ist. Sobald Du diese Verknüpfung aufgelöst hast, kannst Du die Auswahl löschen.
3. Für Planungseinheiten musst Du vorab klären, ob die Kennzahlen (Bedarf, Besetzung, Deckung) noch benötigt werden. Falls ja, kannst Du über *Dashboards*{:.menu-item} die Daten kopieren und diese extern abspeichern (z. B. in Excel). Anschließend gehe zu *WFM > Administration > Scheduling > Planungseinheiten*{:.breadcrumbs} und lösche die Planungseinheit.

Wir haben die Punkte (ohne *Dashboards*{:.menu-item}) in diesem Video zusammengefasst:
{{ 5 | image: 'Schritte zum Löschen von Auswahlen und Tagesmodellen', '100%', 'gif' }}
