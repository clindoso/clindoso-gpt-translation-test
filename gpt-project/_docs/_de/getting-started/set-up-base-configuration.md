---
title: Grundkonfiguration einrichten
description: Konfigurationsdaten, die zum Erstellen eines Schichtplans nötig sind.
redirect_from:
  - /de/configuration-hints/
  - /de/quickstart-base-configuration/
redirect_reason: Updated filename on 24 July 2023
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
---

Bevor du mit der Schichtplanung beginnen kannst, musst du die Grundkonfiguration in injixo einrichten. Einige der Konfigurationselemente sind zwingend erforderlich, damit injixo einen Schichtplan erstellen kann, während andere optional sind, abhängig von der {% link_new Planungsmethode | features/scheduling/scheduling-methods.md %}.

## Konfigurationsreihenfolge

Wir empfehlen, die Konfigurationselemente in der Reihenfolge einzurichten, wie sie in den nächsten beiden Abschnitten gezeigt wird. Konfigurationselemente hängen voneinander ab und können einander zugewiesen werden. Sieh dir die Links in den beiden Tabellen an, um mehr über die einzelnen Konfigurationselemente zu erfahren und wie sie jeweils konfiguriert werden.
Keine Konfiguration ist wie die andere. Deshalb kann die optimale Reihenfolge für dein Unternehmen anders aussehen. Verwende diesen Artikel als ergänzende Checkliste für dein Onboarding. Falls du Fragen hast, kontaktiere deinen Consultant.

### Erforderliche Konfigurationselemente

Die folgende Tabelle enthält eine Übersicht über die erforderlichen Konfigurationselemente, die du in injixo einrichten musst, unabhängig von der Planungsmethode.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Konfigurationselement</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Qualifikationen | features/administration/work-with-skills.md %}</td>
      <td>Qualifikationen stehen für die Fähigkeiten deiner Mitarbeiter. Wenn du Mitarbeitern Qualifikationen zuweist, können sie bestimmte Aktivitäten bearbeiten. injixo setzt voraus, dass du Qualifikationen zu Aktivitäten hinzufügst, die nur bestimmte Mitarbeiter bearbeiten können. Du musst keine Qualifikationen zu Aktivitäten hinzufügen, die von allen Mitarbeitern bearbeitet werden können.</td>
    </tr>
    <tr>
      <td>{% link_new Aktivitäten | features/administration/activities.md %}</td>
      <td>Aktivitäten sind die Aufgaben, Meetings und Abwesenheiten, die du in deinem Unternehmen planst und zu denen du Reports erstellst.<br> Aktivitäten werden zu Tagesmodellen und Planungseinheiten hinzugefügt.</td>
    </tr>
    <tr>
      <td>{% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %}</td>
      <td>Tagesmodelle sind Vorlagen für Schichten. Sie legen die Start- und Endzeiten einer Schicht fest wie auch die Anzahl an Stunden, die ein Mitarbeiter pro Tag arbeitet. Sie enthalten alle Anwesenheits-, Pausen- und Abwesenheitsaktivitäten einer Schicht.<br>Tagesmodelle werden zu Planungseinheiten hinzugefügt. Sie können zudem in Wochenmodellen gruppiert werden (optional).</td>
    </tr>
    <tr>
      <td>{% link_new Planungseinheiten | features/administration/create-and-manage-planning-units.md %}</td>
      <td>Planungseinheiten stehen für die realen oder virtuellen Unternehmensstandorte. Sie dienen dazu, Mitarbeiter zu Planungszwecken zu gruppieren.</td>
    </tr>
    <tr>
      <td>{% link_new Verträge | features/administration/create-contracts.md %}</td>
      <td>Verträge enthalten Informationen über die vertraglich vereinbarten Arbeitsbedingungen. Dazu gehören die Sollstunden sowie die minimale und maximale Arbeitszeit pro Tag, Woche oder Monat.<br>Verträge werden Mitarbeitern zugewiesen.</td>
    </tr>
    <tr>
      <td>{% link_new Mitarbeiter | features/administration/employee-overview.md %}</td>
      <td>Unter Mitarbeiter kannst du Informationen zu jedem Mitarbeiter eintragen, den du planst. Diese Informationen und die Konfigurationselemente, die Mitarbeitern zugewiesen werden (Tagesmodelle, Planungseinheiten, Verträge, Qualifikationen), dienen injixo als Grundlage für die Planung, wann und woran Mitarbeiter arbeiten können.</td>
    </tr>
  </tbody>
</table>

### Optionale Konfigurationselemente

Die folgende Tabelle bietet eine Übersicht über die optionalen Konfigurationselemente, die du in injixo einrichten kannst. Sie hängen größtenteils von der Planungsmethode und den Gegebenheiten in deinem Unternehmen ab.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Konfigurationselement</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Schichtfolgen | features/administration/shift-sequences.md %} (erforderlich für fixe Schichtplanung)</td>
      <td>Eine Schichtfolge ist eine Abfolge von Tagesmodellen oder Aktivitäten, die sich regelmäßig wiederholt.<br>Schichtfolgen werden Mitarbeitern zugewiesen.</td>
    </tr>
    <tr>
      <td>{% link_new Auswahlen | features/administration/selections.md %}</td>
      <td>Mit Auswahlen kannst du Mitarbeiter anhand verschiedenster Parameter filtern, gruppieren oder planen, z.&nbsp;B. Mitarbeiter, die demselben Team angehören oder den gleichen Vertragstyp haben.<br> Auswahlen werden Mitarbeitern zugewiesen.</td>
    </tr>
    <tr>
      <td>{% link_new Planungsmodelle und Wochenmodelle | features/administration/work-time-pattern-models.md %}</td>
      <td>Planungsmodelle und Wochenmodelle helfen dir dabei, deine Schichten so aufzubauen, dass du sie gerecht unter den Mitarbeitern rotieren kannst. Planungsmodelle bestehen aus einem oder mehreren Wochenmodellen. Wochenmodelle gruppieren Schichten nach Parametern wie Startzeit, Schichtlänge oder Aktivitäten. Sie enthalten eine Zusammenstellung von Tagesmodellen.<br>Wochenmodelle werden zu Planungsmodellen hinzugefügt. Planungsmodelle werden Mitarbeitern zugewiesen.</td>
    </tr>
    <tr>
      <td>{% link_new Planungskalender und Tagestypen | features/administration/planning-calendar.md %}</td>
      <td>Planungskalender enthalten Tage mit abweichenden Geschäftszeiten und Mitarbeiterbedarf (z.&nbsp;B. Marketingkampagnen oder bundesweite Feiertage). Diese speziellen Tage werden mit Tagestypen konfiguriert. Dies sorgt dafür, dass sie bei der Schichtplanung automatisch ohne weiteren manuellen Aufwand berücksichtigt werden.<br> Planungskalender werden zu Planungseinheiten hinzugefügt.</td>
    </tr>
  </tbody>
</table>

## Wie geht’s weiter?

Geschafft! Du kannst jetzt deinen ersten {% link_new Forecast erstellen | getting-started/calculate-a-forecast.md %}. Viel Spaß beim Planen!
