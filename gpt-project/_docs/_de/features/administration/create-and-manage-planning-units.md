---
title: Planungseinheiten erstellen und verwalten
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du Planungseinheiten erstellst, konfigurierst und löschst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-use-virtual-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
redirect_from:
  - /de/planning-unit-configuration/
redirect_reason: Updated filename on 21 August 2023
---

Planungseinheiten gruppieren Mitarbeiter und Stammdaten für Planungszwecke. Deine Unternehmensstandorte müssen nicht zwingend mit deinen Planungseinheiten übereinstimmen. Beispielsweise können Mitarbeiter, die an zwei verschiedenen Standorten arbeiten, einer Planungseinheit {% link_new zugewiesen | features/administration/employee-overview.md | #mitarbeitereinstellungen-konfigurieren %} sein.

## Wie viele Planungseinheiten sollte ich verwenden?
	
Um deinen Arbeitsaufwand zu verringern, kannst du Mitarbeiter, die innerhalb einer Planungseinheit an verschiedenen Standorten oder in verschiedenen Teams arbeiten, mit {% link_new Auswahlen | features/administration/selections.md %} planen. In folgenden Fällen ist es sinnvoll, mehr als eine Planungseinheit zu verwenden:
-  Mitarbeiter arbeiten in unterschiedlichen Zeitzonen.
-  Planer sind nur für bestimmte Gruppen von Mitarbeitern verantwortlich, z.&nbsp;B. für bestimmte Geschäftsbereiche. In injixo Advance und Enterprise WFM können benutzerdefinierte Benutzerrollen {% link_new Zugriff auf Planungseinheiten einschränken | getting-started/configure-user-roles.md | #teamzugriff-verwalten-zugriff-auf-stammdaten-einschränken %}.
- Es gibt gemeinsamen Mitarbeiterbedarf, z.&nbsp;B. bei Überlauf-Szenarien.
- Du möchtest Reports erstellen, die die Gesamtzahlen aus mehreren Planungseinheiten enthalten.
	
	
> Tipps für das Arbeiten mit mehreren Planungseinheiten
>
> - Um Zahlen über mehrere Planungseinheiten hinweg zu gruppieren, füge allen relevanten Planungseinheiten eine übergeordnete Planungseinheit hinzu.
> - Du kannst die Zuweisung eines Mitarbeiters von einer Planungseinheit zu einer anderen vorübergehend ändern.<br>Erfahre mehr darüber, wie du {% link_new Mitarbeiter abordnest | features/administration/employee-overview.md | #mitarbeiter-abordnen %}.
	
<!-- Typically, you assign one planning unit to a person at a time. Reassign a planning unit using valid from and valid to dates in the employee configuration. In rare cases, you will need to assign more than one planning unit to a person. The person's main planning unit is assigned with priority 1. The person is scheduled in this main planning unit. A person's schedule will be displayed in other planning units with lower priority. You can also manually reschedule people in other planning units if needed. -->

## Planungseinheiten erstellen


1. Gehe zu _Plan > Konfiguration > Planungseinheiten_{:.breadcrumbs}.
2. Klicke oben links auf das Neu-Icon {% icon item-add | icon-only %}.  
   Ein Konfigurationsfenster öffnet sich auf der rechten Seite.
3. Fülle folgende Felder aus:

   - **Name**: Eindeutiger Name für die Planungseinheit (max. 50 Zeichen).
   - **Kurzbezeichnung**: Kurzbezeichnung für den Namen (max. 25 Zeichen).
   - **Farbe**: Optionale Farbe für die Planungseinheit. Die Farbe wird in Schedules verwendet.
   - **Intervall**: Wirkt sich auf den Detailgrad der Daten aus, die in Schedules angezeigt werden, z.&nbsp;B. Deckung und Mitarbeiterbedarf. Das Intervall der Planungseinheit sollte nicht länger sein als das Intervall der Importe deiner Kontakt- und Agentenstatus-Daten. Das Dropdown-Menü zeigt Intervalle der Planungseinheit in Minuten an. Wir empfehlen, die Option **15** Minuten zu verwenden. Das Intervall kann nach dem Speichern nicht mehr geändert werden. Erfahre mehr über {% link_new Datenimport über Integrationen | features/acd-integration/cloud/how-integrations-work.md %}.
   - **Übergeordnete Planungseinheit**: Optionale Planungseinheit, der die Planungseinheit untergeordnet ist, die du erstellst. Erfahre mehr über {% link_new übergeordnete Planungseinheiten | best-practices/how-to-use-virtual-planning-units.md %}.
   - **Zeitzone**: Zeitzone der Planungseinheit. Die Zeitzone kann nach dem Speichern der Planungseinheit nicht mehr geändert werden. Erfahre mehr darüber, wie du {% link_new mit Zeitzonen arbeitest | best-practices/working-with-timezones.md %}.

     > Hinweis
     >
     > Die ausgewählte Zeitzone muss mit der Zeitzone deiner Workloads in Forecast übereinstimmen. Andernfalls kannst du keinen Mitarbeiterbedarf für die Schichtplanung übertragen. Eine Integration passt die importierten Daten entsprechend der Zeitzone deiner Workloads an.

4. Klicke auf _OK_{:.doc-button}.  
   Du kannst nun Öffnungszeiten und Aktivitäten hinzufügen oder {% link_new Tagesmodelle einschränken | features/administration/create-and-manage-planning-units.md | #tagesmodelle-einschränken %}.

### Öffnungszeiten hinzufügen

Um einer Planungseinheit Öffnungszeiten hinzuzufügen, erstelle zunächst {% link_new die Planungseinheit  | features/administration/create-and-manage-planning-units.md | #planungseinheiten-erstellen %}.

Zu Planungszwecken musst du den Tagestypen deiner Planungseinheit Öffnungszeiten hinzufügen. Die Öffnungszeiten schränken die Zeiten ein, für die du pro Tag den {% link_new Mitarbeiterbedarf berechnen | features/forecast/injixo-forecast/calculate-staff-requirements.md %} und {% link_new optimierte Schichtpläne erstellen | features/scheduling/schedules/schedules-optimized-schedules.md %} kannst. <!-- special public holiday day types or part of the linked article? -->

1. Klicke im Abschnitt **Öffnungszeiten** des Konfigurationsfensters der Planungseinheit auf das {% icon item-add %}.  
   Ein Dialogfenster öffnet sich.
2. Wähle im Abschnitt **Tagestyp** einen oder mehrere {% link_new Tagestypen | features/administration/day-types.md %} aus.
3. Gib die Start- und Endzeit in den Feldern **von** und **bis** (im 24-Stunden-Format) ein. Wenn deine Planungseinheit 24&nbsp;Stunden geöffnet ist, gib in beiden Feldern 00:00 ein.
4. (Optional) Gib in den Feldern **Gültig vom** und **Gültig bis** einen Zeitraum an, für den die Öffnungszeiten gelten. Wenn deine Öffnungszeiten immer gelten, lasse diese Felder leer. Erfahre mehr über {% link_new Gültigkeitszeiträume | features/administration/set-a-validity-period.md %}.
5. Klicke auf _OK_{:.doc-button}.

Um die Öffnungszeiten zu ändern oder zu entfernen, klicke auf das {% icon item-edit %} bzw. das {% icon item-delete %}.

### Aktivitäten hinzufügen

Um einer Planungseinheit Öffnungszeiten hinzuzufügen, erstelle zunächst {% link_new die Planungseinheit | features/administration/create-and-manage-planning-units.md | #planungseinheiten-erstellen %}.

Bevor du Schichtpläne erstellst, musst du den Planungseinheiten alle relevanten Aktivitäten vom Typ Anwesenheit hinzufügen. Du kannst Mitarbeiter nur für Aktivitäten planen, die du ihrer Planungseinheit hinzugefügt hast. Standardmäßig enthalten alle Planungseinheiten die Aktivität Anwesend, die nicht gelöscht werden kann.
Damit deine Reports auch Aktivitäten eines anderen Typs enthalten, musst du den relevanten Planungseinheiten die jeweiligen Aktivitäten hinzufügen.

Um einer Planungseinheit Aktivitäten hinzuzufügen, gehe wie folgt vor:

1. Klicke im Abschnitt **Aktivitäten** des Konfigurationsfensters der Planungseinheit auf das {% icon item-add %}.  
   Ein Dialogfenster öffnet sich.
2. Klicke auf die Aktivität, die du hinzufügen möchtest.
3. Gib mit den Feldern **von** und **bis** eine Zeitspanne an. Die Funktionalität {% link_new Optimierten Plan erstellen | features/scheduling/schedules/schedules-optimized-schedules.md %} kann die Aktivität innerhalb dieser Zeitspanne verwenden. Wenn beide Felder den Wert 00:00 haben, verwendet injixo die Öffnungszeiten der Planungseinheit. Benutzer mit Admin-Zugriff können dieses Standardverhalten in der Einstellung _48408_{:.id-label} _Berücksichtigung von Öffnungszeiten im AutoScheduler_ anpassen.
4. (Optional) Gib einen Datumsbereich in den Feldern **Gültig vom** und **Gültig bis** an, innerhalb dessen die Aktivität für die Schichtplanung verwendet werden kann.<br>Wenn du die Felder **Gültig vom** und **Gültig bis** leer lässt, ist die Aktivität unbegrenzt für die Schichtplanung verfügbar.
5. Klicke auf _OK_{:.doc-button}.

Um eine Aktivität zu bearbeiten oder zu löschen, klicke auf das {% icon item-edit %} bzw. das {% icon item-delete %}.

### Multiaktivitäten hinzufügen

Um eine {% link_new Multiaktivität | features/administration/activity-types-and-properties.md | #teilaktivitäten %} zu einer Planungseinheit hinzuzufügen, musst du ihr zunächst alle relevanten Teilaktivitäten zuweisen. Die Multiaktivität wird in der Übersicht der Aktivitäten fett hervorgehoben. In injixo Essential WFM sind keine Multiaktivitäten verfügbar.

### Tagesmodelle einschränken

Standardmäßig werden deinen Planungseinheiten alle {% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %} zugewiesen. Wenn du für eine Planungseinheit nicht alle Tagesmodelle benötigst, kannst du die Anzahl der Tagesmodelle für diese Planungseinheit einschränken.

Das Einschränken von Tagesmodellen kann die Schichtplanung mit der Funktionalität Optimierten Plan erstellen beschleunigen. Beachte, dass du jedoch nur die der Planungseinheit zugewiesenen Tagesmodelle verwenden kannst, um Schichten zu erzeugen, Reports oder optimierte Schichtpläne zu erstellen. Dies kann zu einem erhöhten Aufwand in der Pflege anderer Konfigurationsdaten führen, z.&nbsp;B. von Wochenmodellen. Das Löschen eines verwendeten Tagesmodells hat keine Auswirkungen auf die Schichtpläne und Schichten, die mit diesem Tagesmodell erzeugt wurden.

> Hinweis
>
> Wenn du alle Tagesmodelle einer Planungseinheit löschst, kannst du Aktivitäten nur noch manuell planen oder indem du sie {% link_new in Schichtfolgen einfügst | features/administration/shift-sequences.md %}. Du kannst die Funktionalität **Optimierten Plan erstellen** nicht mehr verwenden.

Um die Anzahl der Tagesmodelle einzuschränken, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Planungseinheiten_{:.breadcrumbs}.
2. Wähle die Planungseinheit aus, die du bearbeiten möchtest und scrolle im Konfigurationsfenster bis zum Abschnitt **Tagesmodelle**.
3. Um die Anzahl der Tagesmodelle einzuschränken, musst du die Standardzuweisung der Tagesmodelle entweder ersetzen oder löschen:
   - Klicke auf das {% icon item-edit %} neben der Option **[Alle]** und wähle ein Tagesmodell aus.
   - Um die Option **[Alle]** zu löschen, klicke stattdessen auf das {% icon item-delete %}.
4. Klicke auf das {% icon item-add %}, um deiner Planungseinheit ein oder mehrere Tagesmodelle zuzuweisen. Du kannst dasselbe Tagesmodell nicht zweimal hinzufügen. Um ein hinzugefügtes Tagesmodell zu bearbeiten oder zu löschen, klicke auf das {% icon item-add %} bzw. das {% icon item-edit %}.
5. Klicke auf _OK_{:.doc-button}.

## Planungseinheiten löschen

> Achtung
>
> Wenn du eine Planungseinheit löschst, kannst du nicht mehr auf die zugehörigen Schichtpläne zugreifen.

1. Gehe zu _Plan > Konfiguration > Planungseinheiten_{:.breadcrumbs}.
2. Wähle die Planungseinheit aus, die du löschen möchtest.
3. Klicke oben links auf das {% icon item-delete %}.
4. Um zu bestätigen, klicke auf _Ja_{:.doc-button}.


