---
title: Wiederkehrende Jobs mit JobManager automatisieren <!-- TM 100 -->
product_label:
  - enterprise
description: Automatisiere das Erstellen von Reports und mehr mit dem JobManager. <!-- TM 100 -->
promote-service: enhanced-reporting
deepl_translation: true
---

Unter _WFM > Administration > System > JobManager_{:.breadcrumbs} können Mitarbeiter mit Admin-Zugriff Vorlagen für wiederkehrende Jobs erstellen, wie z.&nbsp;B. das Einfügen von Schichtfolgen oder das Erstellen von Reports, die Schichtverlosung und -zuteilung oder das Berechnen von Richtzeitkonten. <!-- TM 100 -->

 <!-- that can run with the privileges of other users. -->

<!-- The JobProcessor runs activated templates at the specified time. -->

## Jobvorlagen erstellen <!-- TM 100 -->

1. Klicke auf das {% icon item-add %}.<br> <!-- TM 89 -->
2. Gib einen eindeutigen Namen (max. 50 Zeichen) ein.<br> <!-- TM 90 -->
3. Aktiviere die Checkbox **Aktiv**, damit der Job wie geplant ausgeführt wird. <!-- TM 100 -->
4. Wähle einen Jobtyp aus. Diese Kategorie hat keine Auswirkungen, aber du kannst später nach Jobtyp sortieren. <!-- TM 100 -->
5. Setze eine **Priorität**. Wertebereich: 1 bis 10 (niedrigster) <!-- TM 100 -->
6. (Optional) Wähle einen anderen **Benutzer** aus. Standardmäßig ist der angemeldete Benutzer ausgewählt. Kann verwendet werden, um Jobtypen mit unterschiedlichen Berechtigungen auszuführen. <!-- TM 100 -->
7. Klicke auf _OK_{:.doc-button}.<br> <!-- TM 100 -->
   Für das Ausführen von Jobs können weitere Parameter erforderlich sein. Konfiguriere diese in den Abschnitten Jobverarbeitungszeitraum, Jobverarbeitungsparameter und Jobverarbeitungstermine. <!-- TM 100 -->

<!-- To edit existing templates, click an item in the list. -->
<!-- Existing templates with the configured parameters can be edited via _JobManager_{:.menu-item} at any time. -->

<!-- outdated for cloud -->
<!-- {{ 1 | image: "Job Configuration", '50%' }} -->

### Jobverarbeitungszeitraum konfigurieren <!-- TM 100 -->

Lege fest, an welchen Tagen eine als aktiv gekennzeichnete Vorlage ausgeführt werden soll. Der Zeitraum kann absolut sein, wenn du einen festen Zeitraum wählst oder relativ für die aktuellen oder vorherigen Wochen oder Monate. Zeiträume relativ zum aktuellen Datum sind nützlich für wiederkehrende Jobs. <!-- TM 100 -->

Wenn du beispielweise jeden Tag um 6&nbsp;Uhr einen Report für den Vortag erstellen möchtest, wähle folgendes aus: <!-- TM 100 -->

- Art der Zeitangabe: Relativ <!-- TM 100 -->
- Bezugswert bis: -1 (Wähle **Tag** aus dem Dropdown-Menü aus) <!-- TM 100 -->
- Bezugswert von: -1 (verfügbar, nachdem du auf **OK** geklickt hast, um die anderen allgemeinen Einstellungen der Vorlage zu speichern) <!-- TM 100 -->

### Jobverarbeitungsparameter konfigurieren <!-- TM 100 -->

Wenn du einen Job speicherst, wird nur der Zeitraum für die Jobverarbeitung festgelegt. Um weitere allgemeine und job-spezifische Parameter für jeden Job einzeln hinzuzufügen, gehe wie folgt vor: <!-- TM 100 -->

1. Klicke auf das {% icon item-add %}.<br> <!-- TM 100 -->
   Ein Dialogfenster öffnet sich. <!-- TM 100 -->
2. Gib einen **Namen** für den Parameter ein. <!-- TM 100 -->
3. Gib einen **Wert** für den Parameter ein. <!-- TM 100 -->

Erfahre mehr über die verfügbaren Parameter und Werte im Artikel {% link_new Anwendungsbeispiele für JobManager | features/reporting/jobmanager/jobmanager-examples.md %}. <!-- TM 100 -->

### Jobverarbeitungstermine konfigurieren <!-- TM 100 -->

Lege die Tage und Zeiten fest, an denen der JobProcessor aktive Vorlagen ausführt. Du kannst für jeden Job einen oder mehrere Termine festlegen. <!-- TM 100 -->

Wähle aus den folgenden Optionen: <!-- TM 100 -->

- Wochentag (Montag-Sonntag) <!-- TM 100 -->
- Monatstag (1-31): Wähle ein Datum aus, das in jedem Monat des Jobverarbeitungszeitraums vorkommt. Zum Beispiel wird der 30.&nbsp;Februar nicht ausgeführt. <!-- TM 100 -->
- Monatsletzter <!-- TM 100 -->

Gib für jede Option die Zeit im Format HH:MM ein. <!-- TM 100 -->

### Jobverarbeitungsoptionen konfigurieren <!-- TM 100 -->

Um Jobs nach der Verarbeitung zu löschen, aktiviere die Checkbox. Dies ist nützlich, wenn du Jobs nur einmalig planen und ausführen möchtest. <!-- more functionality in on-premise --> <!-- TM 83 -->
