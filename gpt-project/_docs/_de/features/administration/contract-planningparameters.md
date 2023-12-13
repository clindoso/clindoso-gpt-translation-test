---
title: Planungsparameter
toc: false
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

In den Planungsparametern kannst Du pro Vertrag Kriterien definieren, die beim Einfügen von Schichten oder Aktivitäten berücksichtigt werden. Bei Aktivierung der entsprechenden Planungsregel erfolgt eine Gültigkeitsprüfung.

**2621 Arbeitstage an Samstagen**  
Gib die Anzahl der Samstage pro Monat an (0 - 5), an denen gearbeitet werden darf.

**2622 Arbeitstage an Sonntagen**  
Gib die Anzahl der Sonntage pro Monat an (0 - 5), an denen gearbeitet werden darf. Dieser Wert wird von Planungsregeln *2622*{:.id-label} und *2643*{:.id-label} beachtet.

**2617 Schicht-Nettozeit Minimum**  
Gib die minimale Schichtdauer ein. Dieser Wert wird von Planungsregeln *2615*{:.id-label} und *2617*{:.id-label} beachtet.

**2616 Schicht-Nettozeit Maximum**  
Gib die maximale Schichtdauer ein. Die Nettozeit entspricht der Dauer aller bezahlten Aktivitäten einer Schicht. Einem Mitarbeiter werden nur Schichten zugeteilt, die die angegebenen Nettozeiten nicht über- bzw. unterschreiten. Dieser Wert wird von der Planungsregel *2614*{:.id-label} und *2616*{:.id-label} beachtet.

**2601 Ruhezeit zwischen zwei Buchungstagen**  
Gib einen Wert für die Ruhezeit zwischen dem Ende der letzten Schicht des einen Buchungstags und dem Beginn der ersten Schicht des folgenden Buchungstags an.

**2602 Maximale Dauer einer Aktivität**  
Gib einen Wert für die maximale Dauer einer Aktivität an. Ganztägige Aktivitäten werden von dieser  Planungsregel **nicht** geprüft.

Aktiviere die entsprechenden Option der Regel, wenn Du die Prüfung für Aktivitäten vom Typ `Krankheit` und/oder `Urlaub` generell ausschließen willst, für Urlaube prüfe die Planungsregel *2641*{:.id-label}.

**2603 Minimaler Abstand zwischen zwei Aktivitäten am selben Buchungstag**  
Gib einen Wert für den Mindestabstand zwischen zwei Aktivitäten am selben Tag an. Der Wert wird nur beachtet, wenn Aktivitäten nicht direkt aufeinander folgen und im `Schicht Center` ein Abstand eingegeben wird.

**2604 Maximaler Abstand zwischen zwei Aktivitäten am selben Buchungstag**  
Gib einen Wert für den maximalen Abstand zwischen zwei Aktivitäten am selben Tag an.

**2613 Maximale Anzahl von Schichten an einem Buchungstag**  
Gib einen Wert für die maximale Anzahl von Schichten an einem Buchungstag an.

**2614 Maximale Arbeitszeit/Tag (Tagesmodelle und Aktivitäten)**  
Aktiviere eines der oder beide Kontrollkästchen, wenn die Summe der Arbeitszeit aus Tagesmodellen und/oder Aktivitäten pro Tag den Maximalwert nicht überschreiten darf.

**2620 Minimale Anzahl freier Wochenenden im Monat gemäß Vertrag**  
Ist diese Regel aktiviert, müssen einem Mitarbeiter so viele freie Wochenenden zugewiesen werden, wie im Vertrag festgelegt sind.

Als Wochenende gelten die Tage, die in den Einstellungen *48421*{:.id-label} *Anzahl der Wochenendtage (Planung)* *48421*{:.id-label} und *48449*{:.id-label} *Erster Tag des Wochenendes (Planung)* *48449*{:.id-label} eingetragen sind. Ein Tag zählt als frei, wenn dafür keine Arbeitszeit gebucht wird. Wochenenden, auf die Arbeitszeit eines anderen Buchungstages entfällt, werden somit als frei betrachtet.

**2623 Maximale Anzahl von Arbeitstagen pro Woche**  
Gib einen Wert für die maximale Anzahl von Arbeitstagen pro Woche an.

**2624 Maximale Anzahl aufeinander folgender Arbeitstage**  
Gib einen Wert für die maximale Anzahl aufeinander folgender Arbeitstage an.

Über die entsprechenden Checkboxen kannst Du die Prüfung für bezahlte Aktivitäten vom Typ `Krankheit` und/oder `Urlaub` generell ausschließen.

**2625 Minimale Anzahl aufeinander folgender freier Tage pro Woche**  
Gib einen Wert für die Mindestanzahl aufeinander folgender freier Tage pro Woche an.

**2626 Maximale Arbeitszeit innerhalb von 24 Stunden**  
Gib einen Wert für die maximale Arbeitszeit aus Tagesmodellen und Aktivitäten innerhalb von 24 Stunden an.

**2627 Mindestanzahl freier Arbeitstage pro Woche unter Berücksichtigung bereits erfolgter Samstagsarbeit**  
Gib die Mindestanzahl freier Tage pro Planungswoche an, die einem Mitarbeiter in der Folgewoche zwischen Montag und Freitag gewährt werden sollen, wenn der Mitarbeiter am Samstag der Vorwoche gearbeitet hat bzw. bereits für eine Schicht geplant ist.

**2628 Mindestanzahl freier Arbeitstage pro Woche unter Berücksichtigung bereits erfolgter Sonntagsarbeit**  
Gib die Mindestanzahl freier Tage pro Planungswoche an, die einem Mitarbeiter in der Folgewoche zwischen Montag und Freitag gewährt werden sollen, wenn er am Sonntag der Vorwoche gearbeitet hat bzw. bereits für eine Schicht geplant ist.

Die Planungsregeln 2627 und 2628 gewährleisten, dass ein Mitarbeiter mit diesem Vertrag, der am Samstag/Sonntag arbeitet, die angegebene Anzahl freier Tage zwischen Montag und Freitag erhält. Er kann aber am Samstag oder Sonntag der aktuellen Woche erneut eine Schicht zugewiesen bekommen.

**2629 Schwellwert für die Überschreitung der Arbeitszeit in aufeinander folgenden Wochen (Tagesmodelle und Aktivitäten)**  
Gib einen Schwellwert pro Woche an. Der Standardwert (168) gibt die pro Woche verfügbare Zeit an.

Als Woche gilt die in den Einstellungen konfigurierte Planungswoche. Gib im Feld `Anzahl Wochen` die Anzahl der aufeinander folgenden Wochen an, in denen der Schwellwert überschritten werden darf. Einem Mitarbeiter können nur so viele Tagesmodelle und Aktivitäten zugeordnet werden, solange der im Vertrag festgelegte Schwellwert für die Überschreitung der Arbeitszeit pro Woche höchstens für die im Vertrag angegebene Anzahl aufeinander folgender Wochen überschritten wird. Ist z. B. für einen Vertrag ein Schwellwert von 40 h pro Woche für drei aufeinander folgende Wochen festgelegt, dann dürfen keine vier aufeinander folgenden Wochen existieren, in denen ein Mitarbeiter mit diesem Vertrag mehr als 40 h pro Woche arbeitet. Der Mitarbeiter dürfte dann maximal in drei aufeinander folgenden Wochen mehr als 40 h pro Woche arbeiten. Die Prüfung durch die Regel *2629*{:.id-label} *Schwellwert für die Überschreitung der Arbeitszeit in aufeinander folgenden Wochen gemäß Vertrag (Tagesmodelle und Aktivitäten)* soll verhindern, dass Mitarbeiter über eine unbegrenzte Anzahl von Wochen hinweg Überstunden haben. Der Schwellwert entspricht in diesem Fall dem im Vertrag angegebenen Soll pro Woche.

**2631 Keine Zuordnungen an Feiertagen (Tagesmodelle und Aktivitäten)**  
Aktiviere das Kontrollkästchen, wenn die Zuordnung von Tagesmodellen und Aktivitäten an Feiertagen unterbunden werden soll. Die Zuordnung wird geprüft für Feiertage im Planungskalender der Planungseinheit, die dem Mitarbeiter mit der höchsten Priorität zugeordnet ist und für die im Menüpunkt *Tagestypen*{:.menu-item} das Kontrollkästchen `Feiertagsmodus` aktiviert ist.

**2632 Maximale Anzahl an Buchungstagen mit Nachtarbeit pro Woche**  
Gib einen Wert für die maximale Anzahl von Buchungstagen mit Nachtarbeit pro Woche an.

**2633 Maximale Anzahl an Buchungstagen mit Nachtarbeit pro Monat**  
Gib einen Wert für die maximale Anzahl von Buchungstagen mit Nachtarbeit pro Monat an.

**2634 Maximale Anzahl von aufeinander folgenden Buchungstagen mit Nachtarbeit**  
Gib einen Wert für die maximale Anzahl aufeinander folgender Buchungstage mit Nachtarbeit an.

**2639 Wöchentliche zusammenhängende Ruhezeit ohne Berücksichtigung von ganzen Kalendertagen**  
Gib einen Wert für die zusammenhängende wöchentliche Ruhezeit an. Bei weniger als 48 Stunden, ist es möglich, dass die Ruhezeit so auf zwei Tage verteilt ist, dass kein ganzer Kalendertag in der Ruhezeit enthalten ist.

**2640 Wöchentliche zusammenhängende Ruhezeit unter Berücksichtigung von mindestens einem ganzen Kalendertag**  
Gib einen Wert für die zusammenhängende wöchentliche Ruhezeit an. Bei Ruhezeiten zwischen 24 und 48 Stunden wird die Ruhezeit immer so gewährt, dass mindestens ein ganzer Kalendertag in der Ruhezeit enthalten ist.

**2641 Maximale Dauer einer Aktivität (Ausnahme: Aktivitätstyp `Abwesenheit`)**  
Gib einen Wert für die maximale Dauer einer Aktivität ohne Prüfung des Aktivitätstyps `Abwesenheit` an.

Für Aktivitäten vom Typ `Krankheit` und/oder `Urlaub` prüfe die Planungsregel *2602*.

**2643 Maximale Anzahl verplanter Sonn- und Feiertage pro Monat**  
Gib einen Wert für die maximale Anzahl von geplanten Sonn- und Feiertagen an. Für einen Mitarbeiter, der im Monat laut Vertrag an 2 Sonntagen arbeiten darf und der zusätzlich an einem Feiertag eingesetzt werden darf, gib den Wert 3 an.

**2646 Ruhezeit nach Feiertagsarbeit ohne Berücksichtigung von ganzen Kalendertagen**  
Gib einen Wert für die Ruhezeit nach Feiertagsarbeit an. Beträgt die Ruhezeit weniger als 48 Stunden, ist es möglich, dass die Ruhezeit so auf zwei Tage verteilt ist, dass kein ganzer Kalendertag in der Ruhezeit enthalten ist.

**2647 Ruhezeit nach Feiertagsarbeit unter Berücksichtigung von mindestens einem ganzen Kalendertag**  
Gib einen Wert für die Ruhezeit nach Feiertagsarbeit an. Die Ruhezeit wird immer so gewährt, dass mindestens ein ganzer Kalendertag in der Ruhezeit enthalten ist.

Für die Planungsregeln *2646*{:.id-label} und *2647*{:.id-label} prüft das System  Feiertage in der Planungseinheit, die dem Mitarbeiter mit der höchsten Priorität zugeordnet ist und für die im Menüpunkt *Tagestypen*{:.menu-item} das Kontrollkästchen `Feiertagsmodus` aktiviert ist.

Ist die Regel aktiviert, muss einem Mitarbeiter nach jedem Feiertag, an dem er eine Schicht oder Aktivität ausführt, für die in der `Administration` im Menüpunkt *Aktivitäten*{:.menu-item} das Kontrollkästchen `Ruhezeit einhalten` aktiviert wurde, die im Vertrag festgelegte Ruhezeit gewährt werden. Ganztägige Aktivitäten werden von dieser Regel **nicht** geprüft und dürfen die Ruhezeit verletzen.

**2649 Maximale Anzahl verplanter Sonntage in Folge (monatsübergreifend)**  
Gib die maximale Anzahl aufeinander folgenden Sonntage an, an denen ein Mitarbeiter mit diesem Vertrag arbeiten darf.

**2650 Maximale Anzahl verplanter Wochenenden in Folge (monatsübergreifend)**  
Gib die maximale Anzahl aufeinander folgenden Wochenenden an, an denen ein Mitarbeiter mit diesem Vertrag arbeiten darf. Als Wochenende gelten die in den Einstellungen zur Konfigurierung der Planungswoche angegebenen Tage.

**2659 Maximale Anzahl Tagesmodelle innerhalb von 24 Stunden**  
Gib das Maximum an Tagesmodellen (1 - 100) an, die innerhalb von 24 Stunden beginnen dürfen.

Die Prüfung erfolgt jeweils für die 24 Stunden vor und nach dem Beginn jeder Schicht. Die Planungsregel kann zur Einhaltung einer 24-Stunden-Frist zwischen dem Schichtbeginn am ersten Tag und dem Schichtbeginn am Folgetag verwendet werden. Bei Angabe des Wertes 1 erhält ein Mitarbeiter mit einer Schicht um 20:00 Uhr erst ab 20:00 Uhr des Folgetages die nächste Schicht.

**2662 Maximal zulässige Abweichung der Arbeitszeit vom Richtzeitkonto pro Planperiode**  
Gib einen Wert für die maximale Abweichung in Stunden  ein (00:00 - 999:59), die zulässig ist, wenn die Gesamtarbeitszeit über der zulässigen Arbeitszeit Richtzeitkonto liegt.
