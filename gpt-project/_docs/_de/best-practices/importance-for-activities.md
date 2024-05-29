---
title: Was ist der Stellenwert von Aktivitäten?
product_label:
  - advanced
  - enterprise
  - classic
description: Über den Stellenwert kannst du Aktivitäten bei der optimierten Schichtplanung priorisieren.
toc: false
---

Du kannst für jede Aktivität einen Stellenwert unter _Plan > Konfiguration > Aktivitäten_{:.breadcrumbs} festlegen.

Je höher der Stellenwert einer Aktivität, umso eher wird der Mitarbeiterbedarf dafür bei der Optimierung berücksichtigt. Wenn eine Aktivität einen geringeren Stellenwert hat, ist es wahrscheinlicher, dass sie überbesetzt wird, wenn du Kapazitäten übrig hast. Wenn du nicht genügend Kapazität hast, ist es ebenso möglich, dass sie unterbesetzt wird.

Bei einem Stellenwert von 100 für eine Aktivität zielt die Optimierung darauf ab, den Bedarf so genau wie möglich zu besetzen. Wenn du zum Beispiel für eine Aktivität fünf Mitarbeiter benötigst, ergibt die Zuordnung von fünf Mitarbeitern die beste Deckung.

Wird der Stellenwert auf 20 reduziert, kann die Optimierung fünf, sieben oder zehn Mitarbeiter planen, je nach Verfügbarkeit. Technisch betrachtet wirkt sich eine Überbesetzung bei dieser Aktivität nur geringfügig auf die objektive Funktion der Optimierung aus.
Daher sollten Aktivitäten, die überbesetzt sein sollen, einen geringeren Stellenwert haben. Dies funktioniert nur, wenn du mehr Kapazität hast als benötigt.

Beispiel:

- 50 Mitarbeiter sind für die Aktivitäten A und B qualifiziert.
- Der Mitarbeiterbedarf für jede Aktivität ist 10.
- Aktivität A hat einen Stellenwert von 20 und B einen Stellenwert von 100.

Alle Mitarbeiter werden auf die Aktivität Anwesend geplant (ID 1). Die Optimierung muss den Mitarbeitern entweder die Aktivität A oder B zuordnen. Die Optimierung plant die ersten 20 Mitarbeiter auf die Aktivitäten A und B.
Nachdem 20 von 50 Mitarbeitern geplant sind, muss die Optimierung entscheiden, was als nächstes folgt.

Die Zuordnung von einem weiteren Mitarbeiter auf die Aktivität B wirkt sich negativ auf die Deckung und das Ziel der Optimierung aus, Über- und Unterbesetzung zu vermeiden. Aufgrund des geringeren Stellenwerts kann die Optimierung fünf Mitarbeiter der Aktivität A zuordnen, bevor sie die gleichen negativen Auswirkungen auf die Gesamtdeckung hat. Deshalb neigt injixo dazu, die Aktivität A überproportional überzubesetzen.

Beide Aktivitäten müssen als _Planbar_ und _Ersetzbar_ konfiguriert sein. Dies setzt auch voraus, dass die Mitarbeiter für die Systemaktivität _Anwesend_ (ID 1) geplant sind. Wenn Mitarbeiter für andere nicht ersetzbare Aktivitäten geplant werden oder Tagesmodelle vordefinierte Aktivitätsblöcke enthalten, kann die Optimierung für das jeweilige Intervall keine Anpassungen vornehmen.
Vorgeplante Aktivitätsblöcke, die Qualifikation der Mitarbeiter oder die Eigenschaften der Aktivität, wie z.&nbsp;B. _Planbar_, könnten verhindern, dass die Optimierung mehr Ressourcen für Aktivität A bereitstellt.
