---
title: Mitarbeiter konfigurieren
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erstelle und konfiguriere Mitarbeiter, um sie bei der Schichtplanung zu berücksichtigen.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-extra-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

In injixo gibt es drei Stellen, an denen du Mitarbeiter erstellen und bearbeiten kannst, je nach Anwendungsfall. In der folgenden Tabelle erfährst du, wo sich die verschiedenen Stellen für die Mitarbeiterkonfiguration in injixo befinden und was du dort jeweils tun kannst.

| Stelle                                           | Beschreibung              |
| ----------------------------------------------- | ------------------------ |
| _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}   | {% link_new Konfiguriere Mitarbeiter für die Schichtplanung | features/administration/employee-overview.md | #übersicht-über-die-mitarbeitereinstellungen %}. Mitarbeiter ohne zugewiesene Planungseinheiten werden nicht in der Liste angezeigt.      |
| _Account > Benutzer_{:.breadcrumbs}                                 | Verwalte den Benutzerzugriff über {% link_new Benutzerrollen | getting-started/configure-user-roles.md | #neue-benutzerrolle-erstellen %}, {% link_new schalte gesperrte Benutzer frei | getting-started/manage-user-accounts.md | #benutzer-entsperren %}, {% link_new setze ein neues Benutzerpasswort | getting-started/manage-user-accounts.md | #neues-benutzerpasswort-setzen %} und {% link_new überprüfe, welche Benutzer abgerechnet werden | getting-started/how-does-billing-work.md | #abgerechnete-und-nicht-abgerechnete-benutzer-anzeigen %} und welche nicht. Zudem kannst du {% link_new Benutzer löschen | getting-started/manage-user-accounts.md | #benutzerkonto-löschen %}, damit diese nicht mehr abgerechnet werden. |
| **People**                                                           | {% link_new Erstelle und verwalte | features/people/manage-people.md %} das Benutzerkonto und die Kontakt- und Adressinformationen eines Mitarbeiters. |

In _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs} können Benutzer ohne Admin-Zugriff nur die Mitarbeiter sehen, die den Planungseinheiten zugewiesen sind, für die sie Berechtigungen haben. Mitarbeiter, die keiner Planungseinheit zugeordnet sind, erscheinen nicht in der Liste, selbst wenn in den Dropdown-Menüs **Planungseinheit** und **Auswahl** jeweils die Option **Alle** ausgewählt ist. Benutzer mit Admin-Zugriff können alle Mitarbeiter sehen.

injixo synchronisiert die Bereiche Mitarbeiter, Benutzer und People. Deshalb musst du einen Mitarbeiter nur einmal anlegen und dieser wird auch nur einmal abgerechnet.

> Alle Mitarbeiter bzw. Benutzer, die du in einem der drei Bereiche anlegst, sind in Zukunft in der monatlichen {% link_new Abrechnung | getting-started/how-does-billing-work.md %} enthalten, bis du sie {% link_new deaktivierst oder löschst | features/administration/deactivate-employees.md %}.

## Mitarbeiter anlegen

Damit du einen Mitarbeiter mit den Basiseinstellungen erstellen kannst, musst du in injixo alle Pflichtfelder ausfüllen. Bevor du den Mitarbeiter in Schichten einteilen kannst, musst du weitere [Mitarbeitereinstellungen](#übersicht-über-die-mitarbeitereinstellungen) [konfigurieren](#mitarbeitereinstellungen-konfigurieren).
Um einen Mitarbeiter mit den Basiseinstellungen zu erstellen, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Klicke in der Aktionsleiste auf das {% icon item-add %}.
3. Gib im Abschnitt **Allgemein** eine eindeutige **Personalnummer** ein.
4. Gib im Abschnitt **Personalien** mindestens den **Nachnamen** des Mitarbeiters ein.
5. Gib im Feld **injixo Login (E-Mail)** eine E-Mail-Adresse ein. Mit dieser E-Mail-Adresse kann sich der Mitarbeiter bei injixo Me anmelden.
6. {% link_new Lege ein Passwort fest | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %}, mit dem sich der Mitarbeiter bei injixo anmelden kann.<br>Dies ist auch noch möglich, nachdem du die Grundkonfiguration für den Mitarbeiter erstellt hast.
7. Klicke auf _OK_{:.doc-button}.<br>Das System legt als Eintrittsdatum automatisch den aktuellen Tag fest. Du kannst es später im Abschnitt [Betriebszugehörigkeit](#weitere-einstellungen) manuell ändern.

Wenn du einen Mitarbeiter anlegst, erstellt injixo automatisch einen Benutzer mit der Rolle Agent.

<!-- In injixo Enterprise on-premise, you need to set the correct join date for the employee in the Employment Period section manually. To automatically create a linked user in the Users section, you need to add a User name and a Password in the Employee section. The injixo Login (Email) field is called Email 1 here and is not mandatory. --->

## Mitarbeitereinstellungen konfigurieren

Wenn du einen Mitarbeiter mit den erforderlichen Grundeinstellungen angelegt hast, kannst du die planungsbezogenen Einstellungen konfigurieren. Gehe dazu wie folgt vor:

Voraussetzung: Du hast {% link_new alle für die Schichtplanung erforderlichen Konfigurationselemente | getting-started/set-up-base-configuration.md | #erforderliche-konfigurationselemente %} eingerichtet.

1. Klicke auf einen Mitarbeiter in der Liste.<br>
Über die blauen Links oben rechts kannst du direkt zu einem Abschnitt springen.
2. Klicke in einem Abschnitt auf das {% icon item-add %}, um eine neue Einstellung hinzuzufügen. Um eine vorhandene Einstellung zu bearbeiten, klicke auf das {% icon item-edit %}.<br>Erfahre mehr über die [Optionen im Einzelnen](#übersicht-über-die-mitarbeitereinstellungen).
3. (Optional) In einigen Abschnitten kannst du einen Zeitraum mit den Feldern {% link_new Gültig von und Gültig bis| features/administration/set-a-validity-period.md %} festlegen und damit die Gültigkeitsdauer für eine Einstellung begrenzen.
4. Um deine Änderungen zu speichern, klicke auf _OK_{:.doc-button}.


## Übersicht über die Mitarbeitereinstellungen

In den folgenden Abschnitten erhältst du Informationen über die erforderlichen und die optionalen planungsbezogenen Einstellungen der Mitarbeiterkonfiguration.

### Erforderliche Einstellungen für die Planung

Die folgende Liste enthält die erforderlichen Konfigurationselemente, die du deinen Mitarbeitern zuweisen musst, um sie planen zu können. Um mehr über jedes Konfigurationselement zu erfahren, klicke auf die jeweiligen Links.

> Hinweis
>
> Du kannst keine Elemente mit sich überschneidenden {% link_new Gültigkeitszeiträumen | features/administration/set-a-validity-period.md %} hinzufügen.
> Vergangene oder zukünftige Zuweisungen werden standardmäßig ausgeblendet. Wenn du sie anzeigen möchtest, klicke auf das Alle-anzeigen-Icon {% icon assignment-history | icon-only %}.


- {% link_new Verträge | features/administration/create-contracts.md %}: Das Dropdown-Menü zeigt alle verfügbaren Verträge an. Wähle den richtigen Vertrag für deinen Mitarbeiter aus und weise dem Mitarbeiter den Vertrag zu.
- {% link_new Qualifikationsstufen | features/administration/work-with-skills.md %}: Qualifikationsstufen geben an, wie qualifiziert ein Mitarbeiter ist, eine bestimmte Tätigkeit auszuführen. Wähle eine oder mehrere Qualifikationsstufen aus dem Dropdown-Menü aus.
- {% link_new Aktivitäten | features/administration/activities.md %}: Aktivitäten sind die Aufgaben, an denen ein Mitarbeiter basierend auf seinen Qualifikationen arbeiten kann. Der Abschnitt Aktivitäten wird automatisch ausgefüllt, nachdem du einem Mitarbeiter eine Qualifikationsstufe zugewiesen hast. Aktivitäten, die alle Mitarbeiter ausführen können, benötigen keine Qualifikation. Dazu gehören z.&nbsp;B. die vordefinierten Aktivitäten Anwesend und Urlaub.
- {% link_new Planungseinheiten | features/administration/create-and-manage-planning-units.md %}: Planungseinheiten gruppieren Mitarbeiter. Ein Mitarbeiter kann mehreren Planungseinheiten zugewiesen werden, benötigt jedoch mindestens eine Planungseinheit mit der Priorität&nbsp;1. Jedem Mitarbeiter können weitere Planungseinheiten mit einem Wert zwischen 1 und 100 zugewiesen werden, wobei 1 für die höchste Priorität steht.

### Optionale Einstellungen für die Planung

Die folgenden Einstellungen sind nicht zwingend erforderlich, können aber auch für die Planung verwendet werden. Um mehr über jedes Konfigurationselement zu erfahren, klicke auf die jeweiligen Links.

- {% link_new Verfügbarkeiten | features/administration/availabilities.md %}: Lege fest, an welchen Tagen und zu welchen Zeiten ein Mitarbeiter für die Planung verfügbar ist. Wenn du einen Mitarbeiter für einen bestimmten Wochentag immer von der Planung ausschließen möchtest, setze die Verfügbarkeit für den entsprechenden {% link_new Tagestypen | features/administration/day-types.md %} auf eine Minute. Um dieselbe Verfügbarkeit für mehrere Mitarbeiter auf einmal festzulegen, nutze Tagesmodelle vom Typ {% link_new Verfügbarkeitsrahmen | features/administration/daymodels/daymodel-creation.md | #verfügbarkeitsrahmen %} in Schichtfolgen. Wenn ein Mitarbeiter uneingeschränkt verfügbar ist, musst du keine Verfügbarkeiten hinzufügen.

- {% link_new Tagesmodelle: | features/administration/daymodels/daymodel-creation.md %} Standardmäßig verwendet injixo alle Tagesmodelle, die der Planungseinheit zugeordnet sind, um Schichtpläne für deine Mitarbeiter zu erstellen. Wenn du einem Mitarbeiter persönliche Tagesmodelle zuweist, wird die Schichtplanoptimierung nur die angegebenen Tagesmodelle für den Mitarbeiter verwenden. Wenn du möchtest, dass injixo nur Mitarbeiter plant, denen individuelle Tagesmodelle zugewiesen wurden, kannst du die Planungsregel _2661_{:.id-label} _Tagesmodellzuordnung zum Mitarbeiter_ aktivieren.

- {% link_new Schichtfolgen | features/administration/shift-sequences.md %}: Schichtfolgen enthalten Tagesmodelle oder Aktivitäten mit einem Muster, das sich wöchentlich wiederholt. Wenn du Schichtfolgen verwenden möchtest, um Schichtpläne für deine Mitarbeiter zu erstellen, musst du zunächst Schichtfolgen erstellen und sie [einem Mitarbeiter zuweisen](#eine-schichtfolge-zuweisen). Du kannst einem Mitarbeiter auch mehr als eine Schichtfolge zuweisen, zum Beispiel, wenn du unterschiedliche Schichtfolgen für Wochentage und Wochenenden verwenden möchtest. 

- {% link_new Auswahl | features/administration/selections.md %}: Auswahlen sind eine Art Filter, den du nutzen kannst, um in einer Übersicht eine Gruppe von gefilterten Mitarbeitern anzuzeigen oder um eine Aktion für eine Gruppe von mehreren Mitarbeiter auf einmal auszuführen. Du kannst aus dem Dropdown-Menü **Auswahl** eine oder mehrere Auswahlen auswählen. Du kannst zum Beispiel eine Gruppe von Mitarbeitern in einer Auswahl zusammenfassen, die immer gleich geplant werden, den gleichen Vertrag haben, in Schichtfolgen arbeiten, gemeinsam zur Arbeit fahren oder die als Vollzeitmitarbeiter als erstes geplant werden.

- {% link_new Planungsmodelle | features/administration/work-time-pattern-models.md %}: Verwende Planungsmodelle, um die automatische Planung auf eine Untergruppe aller verfügbaren Tagesmodelle zu beschränken. Du kannst einem Mitarbeiter ein oder mehrere Planungsmodelle zuweisen. Deren Gültigkeitszeiträume dürfen sich aber nicht überschneiden. Setze ein Referenzdatum, um das Startdatum für das Planungsmodell festzulegen.


- Externe Systeme: Weise {% link_new externe Benutzerkennungen | features/acd-integration/cloud/import-agent-status-data.md | #mitarbeitern-externe-benutzerkennungen-in-injixo-zuordnen %} zu, die für den Import von Agentenstatus-Daten aus deiner ACD benötigt werden.

### Weitere Einstellungen

Der folgende Abschnitt gibt einen Überblick über die weiteren Einstellungen in der Mitarbeiterkonfiguration. Die meisten von ihnen sind nicht relevant für die Planung. Wenn du Details zu einer Einstellung erfahren möchtest, kannst du auch in der Oberfläche den Mauszeiger über eine Einstellung bewegen.

- Betriebszugehörigkeit: Wenn du [einen Mitarbeiter mit den Grundeinstellungen anlegst](#mitarbeiter-anlegen), wird das Eintrittsdatum automatisch festgelegt. Hier kannst du bei Bedarf das Eintrittsdatum ändern bzw. ein Austrittsdatum festlegen.

- Personalien: Gib die persönlichen Daten für deinen Mitarbeiter ein, z.&nbsp;B. Adressdaten, Telefonnummer und Land.

- Ausweisnummern: Gib die Nummer des Mitarbeiterausweises oder eine andere persönliche Ausweisnummer ein.

- Weitere Angaben

Einige der Einstellungen im Abschnitt Weitere Angaben sind für die Planung relevant und andere nicht. Die folgende Tabelle gibt einen Überblick über die Einstellungen.

| Einstellung        | Relevant für die Planung | Beschreibung                |
|----------------| ------------------------|----------------------------|
|Farbe       | Nein                      | Wähle eine Farbe, um den Mitarbeiter schnell im Schichtplan zu identifizieren.  |
|Geburtsdatum und -ort  |       Nein |  Trage das Geburtsdatum und den Geburtsort des Mitarbeiters ein.  |
|Planposition  | Ja | Legt die Sortierreihenfolge für die Sortierung nach der Funktionalität {% link_new Sortierung nach Planposition | features/scheduling/shiftcenter/sort-and-filter-items.md | #elemente-einer-ebene-sortieren %} im Schicht Center fest. Der Standardwert ist 0 und Schicht Center sortiert aufsteigend.  |
|Schichtzuteilung | Ja | Die Checkbox ist standardmäßig aktiviert und wird benötigt, wenn du Mitarbeiter automatisch planen möchtest. Wenn du dies nicht möchtest, deaktiviere die Checkbox. Du kannst weiterhin manuell Schichten zuweisen und Schichtfolgen für diesen Mitarbeiter einfügen.  |

## Massenbearbeitung verwenden

In injixo Advanced und Enterprise WFM kannst du mit der Funktionalität {% link_new Massenbearbeitung | features/administration/mass-update.md %} mehrere Mitarbeiter auf einmal bearbeiten.

## Eine Schichtfolge zuweisen

Eine Schichtfolge ist eine Abfolge von Tagesmodellen oder Aktivitäten, die sich regelmäßig wiederholt. Erfahre, wie du {% link_new Schichtfolgen erstellst | features/administration/shift-sequences.md %} und diese in den Schichtplan einfügst.

Um eine Schichtfolge zuzuweisen, gehe wie folgt vor:

1. Klicke im Abschnitt **Schichtfolgen** auf das {% icon item-add %}.
2. Wähle eine Schichtfolge aus.
3. Wähle im Dropdown-Menü Mitarbeiterzeile aus, welche Zeile der {% link_new Schichtfolge | features/administration/shift-sequences.md %} für den Mitarbeiter gilt.
4. Lege die Reihenfolge fest.<br>Diese Einstellung ist nur relevant, wenn du einem Mitarbeiter mehr als eine Schichtfolge zuweisen möchtest. Schichtfolgen mit niedrigeren Werten werden zuerst eingefügt und können von nachfolgenden überschrieben werden.
5. Setze ein Referenzdatum, um das Startdatum für die Schichtfolge festzulegen.
6. Klicke auf _OK_{:.doc-button}.
Jetzt kannst du {% link_new Schichtfolgen | features/scheduling/schedules/schedules-insert-shift-sequences.md %} in den Schichtplan einfügen.

## Mitarbeiter abordnen

Wenn deine Mitarbeiter häufig für eine bestimmte Zeit in anderen Planungseinheiten arbeiten, kannst du mit der Funktionalität Mitarbeiter abordnen deine Mitarbeiter vorübergehend einer anderen Planungseinheit zuweisen.

Während der Mitarbeiter abgeordnet ist, hat die neue Planungseinheit automatisch Priorität bei der Schichtplanung. Wenn die Abordnung endet, wird der Mitarbeiter automatisch wieder in seiner alten Planungseinheit geplant. Die Funktionalität Mitarbeiter abordnen spart Zeit im Vergleich zur manuellen Zuweisung der Planungseinheit.

Um einen Mitarbeiter abzuordnen, gehe wie folgt vor.

1. Wähle einen Mitarbeiter aus.
2. Gehe zum Abschnitt **Planungseinheiten**.
3. Klicke auf das {% icon delegate-employees %} in der Überschriftszeile.
4. Wähle die Planungseinheit, zu der der Mitarbeiter abgeordnet werden soll.
5. Gib ein Start- und ein Enddatum für die Abordnung ein.
6. Klicke auf _OK_{:.doc-button}.

> Hinweis
>
> Ein Mitarbeiter, der gleichzeitig mehreren Planungseinheiten zugewiesen ist, wird immer von der Planungseinheit mit der höchsten Priorität abgeordnet.
