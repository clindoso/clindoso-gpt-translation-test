---
title: Odigo-Integration hinzufügen
description: Erfahre, wie du deine Odigo-ACD mit injixo verbinden kannst, um Daten zu importieren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Die Odigo-Integration importiert in Echtzeit Agentenstatus-Daten und Daten zur Planeinhaltung.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Odigo-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Odigo**-Kachel auf _Integration hinzufügen_{:.doc-button}.
4. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
5. (Optional) Konfiguriere den Import von Agentenstatus Pause mit Details:
- Aktiviere die Checkbox **Agentenstatus Pause mit Details importieren**.<br>Beim Importieren von Pausenstatus fügt injixo Informationen über den Pausentyp hinzu.<br>Hinweis: Wenn du diese Checkbox aktivierst, musst du auch die {% link_new Zuordnung der Aktivitäten | features/acd-integration/cloud/import-agent-status-data.md | #aktivitäten-aus-externen-systemen-den-aktivitäten-in-injixo-zuordnen %} aktualisieren.
- Gib deine Odigo-URL mit der Tenant-ID ein.
- Gib den Benutzernamen und das Passwort für den Webservice ein.
6. Klicke auf _Integration speichern_{:.doc-button}.

## Odigo-Integration einrichten

1. Klicke im Abschnitt **injixo URL-Token erzeugen** auf _Generieren_{:.doc-button}.
2. Speichere den injixo URL-Token in der Zwischenablage.<br>
Der injixo URL-Token wird nur einmalig angezeigt. Wenn du die Einrichtung nicht unmittelbar abschließen kannst, speichere den Token an einem sicheren Ort, z.&nbsp;B. in einem Passwort-Manager.
3. Aktiviere im Administrationsbereich deiner Odigo-Schnittstelle das Versenden von Benachrichtigungen an einen externen Server. Wende dich dazu an Odigo.
4. Füge den kopierten **injixo URL-Token** aus der Zwischenablage als Benachrichtigungs-URL ein.
5. Speichere deine Einstellungen in Odigo und kehre zu injixo zurück.

Damit die Integration aktiviert wird, musst du den Server neu starten. Wende dich dazu an Odigo.<br>
injixo beginnt dann mit dem Import von RTA-Daten. Allerdings sind die Daten erst sichtbar, nachdem du deinen Mitarbeitern die externen Benutzerkennungen zugeordnet hast.

## Mitarbeitern externe Benutzerkennungen zuordnen

1. Gehe zu _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs}.
2. Ordne deinen Mitarbeitern externe Benutzerkennungen zu.

Erfahre mehr darüber, wie du {% link_new deinen Mitarbeitern externe Benutzerkennungen zuordnest | features/acd-integration/cloud/import-agent-status-data.md | #mitarbeitern-externe-benutzerkennungen-in-injixo-zuordnen %}.

## Agentenstatus den Aktivitäten in injixo zuordnen

1. Gehe zu _WFM > Administration > Scheduling > Aktivitäten_{:.breadcrumbs}.
2. Ordne die Odigo-Aktivitäten den Aktivitäten in injixo zu.

Erfahre mehr darüber, wie du {% link_new externe Aktivitäten den injixo-Aktivitäten zuordnest | features/acd-integration/cloud/import-agent-status-data.md | #aktivitäten-aus-externen-systemen-den-aktivitäten-in-injixo-zuordnen %}.
