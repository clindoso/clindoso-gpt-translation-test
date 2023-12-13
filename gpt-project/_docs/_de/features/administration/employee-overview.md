---
title: Mitarbeiter anlegen und konfigurieren
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
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

In diesem Artikel lernst Du:

- was Mitarbeiter in injixo sind.
- wie Du sie anlegst und bearbeitest.
- welche Mitarbeitereinstellungen es gibt und welche Du für die Planung benötigst.
- wie Du die Mitarbeitereinstellungen konfigurierst.

## Was sind Mitarbeiter in injixo?

Der Bereich _Mitarbeiter_ in _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs} wird hauptsächlich genutzt, um Mitarbeiter für die Planung zu konfigurieren. Du siehst dort eine Liste aller Mitarbeiter, die sowohl Agenten als auch alle anderen injixo Benutzer wie Planer, Trainer, Admins und Supervisoren enthält.

Hinweis: Als Benutzer ohne _Admin-Zugriff_ kannst Du nur Mitarbeiter sehen, die einer Planungseinheit zugewiesen sind, auf die Du Lesezugriff hast. Mitarbeiter ohne zugewiesene Planungseinheiten erscheinen selbst dann nicht in der Liste, wenn Du _Alle_ in den Dropdown-Menüs _Planungseinheit_ und _Auswahl_ auswählst.

{{ 3 | image: 'Mitarbeiterliste', '100%' }}

Es gibt einen weiteren Bereich in injixo, der alle Benutzer anzeigt, nämlich unter _Account > Benutzer_{:.breadcrumbs}. Dort kannst Du mithilfe von Benutzerrollen die Zugriffsrechte von Benutzern verwalten, gesperrte Benutzer entsperren, neue Passwörter vergeben und überprüfen, welche Benutzer aktuell abgerechnet werden und welche nicht.

Sowohl der Bereich _Mitarbeiter_ als auch der Bereich _Benutzer_ enthalten alle Benutzer, die zu injixo hinzugefügt wurden. Die beiden Bereiche werden synchronisiert. injixo erstellt automatisch einen Benutzer mit der Agentenrolle für jeden neuen Mitarbeiter, den Du im Bereich _Mitarbeiter_ anlegst. Wenn Du einen Benutzer im Bereich _Benutzer_ anlegst, erscheint dieser automatisch im Bereich _Mitarbeiter_. Erfahre mehr über {% link_new Benutzer | getting-started/manage-user-accounts.md %}.

> Alle Mitarbeiter bzw. Benutzer, die Du in einem der beiden Bereiche anlegst, werden in Zukunft in die monatliche {% link_new Abrechnung | getting-started/how-does-billing-work.md %} einbezogen, bis Du sie {% link_new deaktivierst oder löschst | features/administration/deactivate-employees.md %}.

## Mitarbeiter anlegen

1. Gehe zu _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs}.
2. Klicke auf das {% icon item-add %} in der Aktionsleiste.
3. Trage eine eindeutige **Personalnummer** ein.
4. Füge mindestens den **Nachnamen** hinzu.
5. Füge bei **injixo Login (E-Mail)** eine E-Mail-Adresse hinzu. Für das Mitarbeiterportal injixo Me wird ein Zugang erstellt. Wenn Du willst, dass sich der Mitarbeiter bei injixo anmelden kann, musst Du allerdings zuvor noch {% link_new ein Passwort festlegen | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %}.

   {{ 1 | image: 'Neuen Mitarbeiter anlegen', '50%' }}

6. Klicke _OK_{:.doc-button}. Das _Eintrittsdatum_ wird automatisch auf den aktuellen Tag gesetzt. Du kannst es später manuell ändern.

Du hast nun einen Mitarbeiter mit den Grundeinstellungen angelegt. Um den Mitarbeiter planen zu können, musst Du einige weitere Elemente hinzufügen, die unten näher erklärt werden.

Hinweis: In injixo Enterprise On-Premise musst Du das korrekte Eintrittsdatum manuell im Abschnitt _Betriebszugehörigkeit_ eingeben. Um automatisch einen verknüpften Benutzer im Bereich _Benutzer_ zu erstellen, musst Du einen _Benutzernamen_ und ein _Passwort_ im Bereich _Mitarbeiter_ vergeben. Das Feld _injixo Login (E-Mail)_ heißt hier _E-Mail 1_ und ist nicht zwingend erforderlich.

## Übersicht über die Mitarbeitereinstellungen

Einige Einstellungen sind für die Planung zwingend notwendig, andere sind nur für bestimmte Anwendungsfälle erforderlich. Im Folgenden erfährst Du, welche Einstellungen Du benötigst. Für viele dieser Einstellungen musst Du zuerst die benötigten Elemente erstellen, z. B. Verträge, Qualifikationen oder Planungseinheiten. Erstelle sie in der {% link_new empfohlenen Reihenfolge | getting-started/set-up-base-configuration.md %}. Danach kannst Du die [erstellten Elemente Deinen Mitarbeitern zuweisen](#mitarbeitereinstellungen-konfigurieren).

### Erforderliche Einstellungen für die Planung

- **{% link_new Verträge | features/administration/create-contracts.md %}**: In Verträgen werden Arbeitszeiten und -regeln für Mitarbeiter festgelegt.
- **{% link_new Qualifikationsstufen | features/administration/work-with-skills.md %}**: Qualifikationen legen fest, welche Art von Arbeit ein Mitarbeiter ausführen kann. Qualifikationsstufen vermitteln, wie qualifiziert ein Mitarbeiter ist, eine bestimmte Tätigkeit auszuführen. Qualifikationen sind immer einer Aktivität zugeordnet.
- **{% link_new Aktivitäten | features/administration/activities.md %}**: Aktivitäten stellen die Arbeit dar, die ein Mitarbeiter aufgrund seiner Qualifikationen ausführen kann. Nachdem Du einem Mitarbeiter eine Qualifikationsstufe zugewiesen hast, wird dieser Bereich automatisch ausgefüllt. Aktivitäten, die alle Mitarbeiter ausführen können, benötigen keine Qualifikation. Dazu gehören z. B. die vordefinierten Aktivitäten _Anwesend_ und _Urlaub_.
- **{% link_new Planungseinheiten | features/administration/create-and-manage-planning-units.md %}**: Planungseinheiten gruppieren Mitarbeiter. Füge für jeden Mitarbeiter eine Planungseinheit mit Priorität 1 hinzu.

> Checkbox Schichtzuteilung im Abschnitt _Weitere Angaben_
>
> Die Checkbox _Schichtzuteilung_ ist standardmäßig aktiviert und wird gesetzt, um Mitarbeiter automatisch zu planen. Deaktiviere die Checkbox, wenn ein Mitarbeiter von der volloptimierten Planung keine Schichten zugewiesen bekommen soll. Du kannst aber weiterhin manuell Schichten zuweisen und Schichtfolgen für diesen Mitarbeiter einfügen.

### Optionale Einstellungen für die Planung

- **Planungssperren**: Um einen Mitarbeiter für bestimmte Zeiträume von der Planung auszuschließen, kannst Du hier die Zeiträume hinzufügen. Dies betrifft die volloptimierte Planung, das Schichtwunsch-Verfahren und die Funktion _Schichtfolgen einfügen_. Eintragungen im Abschnitt _Planungssperren_ werden nur berücksichtigt, wenn die Planungsregel _2608_{:.id-label} _Planungssperre_ aktiviert ist.

- **Coach/Trainee**: Ordne Mitarbeiter als Trainees dem Mitarbeiter zu, der sie coacht. Einem Coach können mehrere Trainees zugewiesen werden. Achte darauf, die Mitarbeiter zur gleichen Zeit wie den Coach zu planen, um sicherzustellen, dass das Coaching direkt bei der Arbeit stattfinden kann. Trainees werden bei Berechnungen der Besetzung und Deckung nicht berücksichtigt. Übertrage im Schicht Center die Schichten und Aktivitäten des Coaches auf die Trainees. Entferne die Trainees vom coachenden Mitarbeiter, sobald das Coaching beendet ist.

- **{% link_new Verfügbarkeit | features/administration/availabilities.md %}**: Lege fest, an welchen Tagen und zu welchen Zeiten ein Mitarbeiter für die Planung zur Verfügung steht. Wenn Du einen Mitarbeiter an einem bestimmten Wochentag immer von der Planung ausschließen willst, setze die Verfügbarkeit für den jeweiligen {% link_new Tagestyp | features/administration/day-types.md %} auf eine Minute. Um die gleiche Verfügbarkeit für mehrere Mitarbeiter auf einmal hinzuzufügen, verwende Tagesmodelle vom Typ _Verfügbarkeit_ im Modul _Schichtfolgen_. Wenn ein Mitarbeiter die ganze Zeit über verfügbar ist, musst Du keine Verfügbarkeiten hinzufügen.

- **{% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %}**: Standardmäßig verwendet injixo alle Tagesmodelle, die der Planungseinheit zugeordnet sind, um Schichtpläne für Deine Mitarbeiter zu erstellen. Wenn Du einem Mitarbeiter hier persönliche Tagesmodelle zuweist, wird die optimierte Planung nur die angegebenen Tagesmodelle für den Mitarbeiter verwenden. Wenn Du möchtest, dass injixo nur Mitarbeiter plant, denen individuelle Tagesmodelle zugewiesen wurden, kannst Du die Planungsregel _2661_{:.id-label} _Tagesmodellzuordnung zum Mitarbeiter_ aktivieren.

- **{% link_new Schichtfolgen | features/administration/shift-sequences.md %}**: Verwende Schichtfolgen, um wiederkehrende Schichten oder Aktivitäten zu planen. Wenn Du Schichtpläne für Mitarbeiter mit Hilfe von Schichtfolgen erstellen möchtest, musst Du diese zunächst hier zuweisen. Lerne, wie Du [einem Mitarbeiter Schichtfolgen zuweist](#eine-schichtfolge-zuweisen).

- **{% link_new Auswahlen | features/administration/selections.md %}**: Mit Hilfe von Auswahlen kannst Du Mitarbeiter filtern oder planen. Der Teamkalender in injixo Me und einige Reports setzen voraus, dass Du mindestens eine Auswahl pro Mitarbeiter zuweist.

- **{% link_new Planungsmodelle | features/administration/work-time-pattern-models.md %}**: Verwende Planungsmodelle, um die automatische Planung auf eine Teilmenge aller verfügbaren Tagesmodelle zu beschränken. Wähle ein {% link_new **Referenzdatum** | features/administration/reference-date.md %}, um den Starttag für das Planungsmodell festzulegen.

### Andere Einstellungen

- **Personalien**, **Weitere Angaben** und **Ausweisnummern**: Die Daten in diesen Abschnitten sind meist nicht relevant für die Planung, können aber je nach Anwendungsfall hilfreich sein. Erfahre mehr über die verschiedenen Felder, indem Du Deine Maus darüber bewegst. Es erscheint ein Hinweistext in der Leiste am unteren Bildschirmrand.
- **Externe Systeme**: Weise {% link_new externe Benutzerkennungen | features/acd-integration/cloud/import-agent-status-data.md | #mitarbeitern-externe-benutzerkennungen-in-injixo-zuordnen %} zu, die für den Agentenstatus-Import aus Deiner ACD benötigt werden.

## Mitarbeitereinstellungen konfigurieren

Du weißt nun, welche Einstellungen möglich sind und welche Du für die Planung brauchst. Du hast außerdem alle Elemente erstellt, die Du zuweisen musst, wie Verträge, Qualifikationen oder Planungseinheiten. Du kannst jetzt Deine Mitarbeiter konfigurieren.

1. Klicke auf einen **Mitarbeiter** in der Liste.
2. Nutze die **Links** am oberen Bildschirmrand, um schnell zwischen den Abschnitten zu navigieren.

   {{ 4 | image:' Mitarbeiter Quicklinks', '80%' }}

3. Klicke auf das {% icon item-add %} in einem Abschnitt, um ein neues Element hinzuzufügen. Klicke auf das {% icon item-edit %}, um bestehende Konfigurationen zu ändern.
4. (Optional) In vielen Abschnitten kannst Du einen Zeitraum mit {% link_new **Gültig von und Gültig bis** | features/administration/set-a-validity-period.md %} definieren, was den Gültigkeitszeitraum für eine Einstellung begrenzt. Du kannst keine Elemente mit sich überschneidenden Gültigkeitszeiträumen hinzuzufügen.  
   Hinweis: Vergangene oder zukünftige Zuweisungen werden ausgeblendet. Um ausgeblendete Zuordnungen einzublenden, klicke auf das {% icon assignment-history %}.
5. Wähle das/die **Element(e)** aus, das/die Du hinzufügen möchtest. Bei einigen Elementen sind zusätzliche Felder erforderlich, z. B. bei Schichtfolgen (siehe unten). Erfahre mehr über die verschiedenen Felder, indem Du Deine Maus darüber bewegst. Es erscheint ein Hinweistext.
6. Klicke auf _OK_{:.doc-button}, um Deine Änderungen zu speichern.

### Massenbearbeitung verwenden

In injixo Advanced und Enterprise WFM kannst Du das Bearbeiten von Mitarbeitern beschleunigen, indem Du die Funktion Massenbearbeitung in der Aktionsleiste benutzt.

So kannst Du die Bereiche _Verträge_, _Qualifikationen_, _Planungseinheiten_, _Schichtfolgen_, _Auswahl_ und _Planungsmodelle_ für mehrere Mitarbeiter auf einmal bearbeiten. injixo Enterprise WFM unterstützt auch die Bearbeitung von Attributen.

1. Wähle die Mitarbeiter, die Du bearbeiten möchtest, mit den Dropdown-Menüs **Planungseinheit** und **Auswahl** aus. Du kannst auch einen **Mitarbeiterfilter** verwenden.
2. Klicke auf das {% icon mass-update %} in der Aktionsleiste. Im Bereich _Parameter_ siehst Du, welche Filter Du ausgewählt hast und die Anzahl der ausgewählten Mitarbeiter.
3. Wähle im Dropdown-Menü **Stammdaten**, welche Konfigurationselemente Du aktualisieren möchtest.
4. Wähle mit den Feldern **Vom** und **Bis** den Zeitraum aus, für den die Konfigurationselemente aktualisiert werden sollen. Wenn Du die Änderungen nicht auf einen Zeitraum beschränken möchtest, lass die Felder leer.
5. Wähle eine **Aktion**. Du kannst **neue Elemente** zuweisen, vorhandene Elemente **ersetzen** oder **löschen**, oder **Gültigkeitszeiträume ändern**.
6. Wähle im Abschnitt **Neue Zuordnung** auf der rechten Seite das **Element** aus, das Du hinzufügen, löschen oder für die Ersetzung verwenden möchtest, je nachdem, welche Aktion Du gewählt hast.
7. Klicke auf _OK_{:.doc-button}, um die Massenbearbeitung zu starten.

### Eine Schichtfolge zuweisen

1. Klicke auf das {% icon item-add %} im Abschnitt _Schichtfolgen_.
2. Wähle eine **Schichtfolge** aus.
3. Wähle im Dropdown-Menü **Mitarbeiterzeile** aus, welche Zeile der {% link_new Schichtfolge | features/administration/shift-sequences.md %} für den Mitarbeiter gilt.
4. Lege einen Wert für die **Reihenfolge** fest. Normalerweise weist Du nur eine Schichtfolge pro Mitarbeiter zu. Wenn Du allerdings mehr als eine Schichtfolge zuweist, ist diese Einstellung wichtig. Schichtfolgen mit niedrigeren Zahlen werden zuerst eingefügt und könnten von nachfolgenden Schichtfolgen überschrieben werden.
5. Setze ein {% link_new **Referenzdatum** | features/administration/reference-date.md %}, um den Starttag für die Schichtfolge festzulegen.
6. Klicke _OK_{:.doc-button}.

Du kannst nun das Modul {% link_new Schichtfolgen einfügen | features/scheduling/capacity/capacity-insert-shift-sequences.md %} nutzen, um die Schichtfolge in den Schichtplan einzutragen.

## Mitarbeiter filtern und sortieren

Verwende die Dropdown-Menüs für **Planungseinheit** und **Auswahl** oder erstelle einen {% link_new Mitarbeiterfilter | features/administration/employee-filter.md %}.

Klicke auf eine Spaltenüberschrift in der Mitarbeiterliste, um z. B. nach **Personalnummer**, **Nachname**, oder **Eintrittsdatum** zu sortieren. Klicke nochmals, um die Sortierreihenfolge umzukehren.

## Mitarbeiter abordnen

Deine Mitarbeiter arbeiten häufig befristet in anderen Planungseinheiten? Nutze die Funktion _Mitarbeiter abordnen_, um Mitarbeitern vorübergehend eine andere Planungseinheit zuzuordnen. Die neue Planungseinheit erhält für den Abordnungszeitraum automatisch die Priorität 1 und der abgeordnete Mitarbeiter wird in der neuen Planungseinheit geplant. Nach Ablauf des Zeitraums gehört der Mitarbeiter automatisch wieder zu seiner vorherigen Planungseinheit. Die Funktion erspart im Vergleich mit der manuellen Neuzuordnung von Planungseinheiten einigen Zeitaufwand.

Die neue Planungseinheit erhält während des Abordnungszeitraums automatisch die Priorität 1 und der abgeordnete Mitarbeiter wird in der neuen Planungseinheit geplant. Nach Ablauf des Zeitraums gehört der Mitarbeiter automatisch zu seiner bisherigen Planungseinheit.

1. Wähle einen **Mitarbeiter** aus.
2. Scrolle zum Abschnitt _Planungseinheiten_.
3. Klicke auf das **Haus-Symbol** in der Überschriftszeile.
4. Wähle im Eingabedialog die **Planungseinheit**, in die der Mitarbeiter abgeordnet werden soll, das **Startdatum** und das **Enddatum** des Abordnungszeitraums.
5. Klicke auf _OK_{:.doc-button}, um die Abordnung durchzuführen.

Hinweis: Ein Mitarbeiter, der gleichzeitig mehreren Planungseinheiten angehört, wird immer von der Planungseinheit mit der höchsten Priorität abgeordnet.
