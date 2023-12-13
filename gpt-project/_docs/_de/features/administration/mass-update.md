---
title: Massenbearbeitung
product_label:
  - advanced
  - enterprise
  - classic
---

In diesem Artikel lernst Du, was das Feature *Massenbearbeitung* ist und wie Du es verwendest.

Mit der Massenbearbeitung kannst Du die Stammdaten-Zuordnungen für mehrere Mitarbeiter gleichzeitig bearbeiten. Die Massenbearbeitung funktioniert für Verträge, Qualifikationen, Planungseinheiten, Auswahlgruppen, Schichtfolgen und Planungsmodelle. In injixo Enterprise WFM kannst Du die Funktion zusätzlich für Attribute nutzen.

## Die Massenbearbeitung starten

1. Gehe zu *WFM > Administration > Scheduling > Mitarbeiter*{:.breadcrumbs}.
2. Wähle eine **Auswahl** oder einen **Mitarbeiterfilter**.
3. Klicke auf _![Button Massenbearbeitung](/assets/img/common/mass-update.gif)_{:.doc-button-icon} in der Aktionsleiste.  

Die Seite für die Massenbearbeitung mit den Bereichen *Parameter* und *Aktion* öffnet sich. Der Bereich *Parameter* zeigt Informationen zum angewendeten Filter und der Anzahl der ausgewählten Mitarbeiter.

1. Wähle im Feld *Stammdaten* einen **Eintrag** aus, um zu definieren, welche Stammdaten Du bearbeiten möchtest.
2. Optional: Schränke den Zeitraum für die Massenbearbeitung über die Felder **Vom** und **Bis** ein. Lass Felder leer, wenn Du Änderungen nicht auf einen Zeitraum beschränken möchtest.
3. Wähle eine **Aktion**. Unterhalb lernst Du mehr über die [verfügbaren Aktionen](#aktionen-verstehen).
4. Wähle rechts in den Abschnitten *Bisherige Zuordnungen*, *Neue Zuordnung* oder *Neuer Gültigkeitszeitraum* die **Elemente** aus, die Du hinzufügen, löschen oder ersetzen möchtest (abhängig von der Aktion).
5. Klicke auf *OK*{:.doc-button}, um die Massenbearbeitung zu starten.

    {{ 1 | image: 'Programmfenster', '50%' }}

## Aktionen verstehen

Abhängig von Deiner Auswahl im Feld *Stammdaten* ändern sich die Bereiche *Aktion* sowie der Bereich auf der rechten Seite, um die Stammdaten auszuwählen, die Du zuordnen oder ersetzen möchtest. Dort erscheint entweder der Bereich *Neue Zuordnung*, *Bisherige Zuordnungen* oder beide Bereiche.

### Zuordnungen hinzufügen oder überschreiben

- **Hinzufügen:** Ordne Mitarbeitern die gewählten Stammdaten zu.
- **Hinzufügen für Zeiträume ohne Zuordnung:** Ordne Mitarbeitern die gewählten Stammdaten für Zeiträume zu, in denen bisher keine Zuordnung besteht.
- **Alles überschreiben:** Überschreibe alle bestehenden Zuordnungen mit den gewählten Stammdaten.

{{ 2 | image: 'Bereich neue Zuordnung', '75%'}}

### Bestehende Zuordnungen ersetzen oder löschen

- **Hinzufügen für Zeiträume ohne Zuordnung und bestehende Zuordnungen ersetzen:** Ordne Mitarbeitern die gewählten Stammdaten für Zeiträume zu, in denen es bisher keine Zuordnung gibt. Bisherige Zuordnungen werden zusätzlich ersetzt, wenn sie den definierten Kriterien entsprechen. Alle anderen Zuordnungen bleiben bestehen.
- **Hinzufügen für Zeiträume mit bestimmten Zuordnungen:** Ordne Mitarbeitern die gewählten Stammdaten für Zeiträume zu, in denen sie bisher die ausgewählten Zuordnungen haben.
- **Zuordnungen ersetzen:** Ersetze die gewählten Stammdaten bei Mitarbeitern, die bisher diese Zuordnung haben.
- **Zuordnungen mit gleicher Qualifikationsstufe ersetzen:** Ersetze Qualifikationsstufen bei Mitarbeitern. Aktiviere die Checkbox *Bisherige Qualifikationsstufe überschreiben*, um bestehende Zuordnungen mit der ausgewählten Qualifikationsstufe zu überschreiben. Deaktiviere die Checkbox, wenn bisherige Zuordnungen beibehalten werden sollen.
- **Löschen:** Lösche alle bestehenden Zuordnungen im ausgewählten Zeitraum.

{{ 3 | image: 'Bisherige und neue Zuordnungen', '75%' }}

### Gültigkeitszeiträume ändern

**Gültigkeitszeitraum ändern:** Wähle die Option *Gültig vom*, um das Startdatum der Stammdaten zu ändern. Wähle stattdessen die Option *Gültig bis* für Enddatum. Wähle dann im Abschnitt *Neuer Gültigkeitszeitraum* ein neues Datum, welches das bestehende Start- oder Enddatum ersetzen soll. Wenn Du einen Zeitraum verlängerst, in dem bereits eine andere Zuordnung für diesen Mitarbeiter besteht, erscheint eine Fehlermeldung. Der Mitarbeiter wird ganz von der Aktion ausgeschlossen.

Wenn Stammdaten einem Mitarbeiter über den Bearbeitungszeitraum hinaus zugeordnet sind, kann es zu Zeiträumen ohne Zuordnung kommen. Beispiel: Ein Mitarbeiter hat einen Vertrag von 1. März bis 31. Mai. Der Bearbeitungszeitraum ist der gesamte April, das neue Enddatum der 15. April. Am Ende besteht keine Vertragszuordnung mehr vom 16. April bis 31. Mai.

{{ 4 | image: 'Bisherige Zuordnungen, neuer Gültigkeitszeitraum', '75%'}}
