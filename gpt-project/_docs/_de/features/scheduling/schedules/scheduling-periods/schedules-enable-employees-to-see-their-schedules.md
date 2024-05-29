---
title: Mitarbeitern Schichtpläne anzeigen
toc: false
description: Ermögliche Deinen Mitarbeitern, ihre Schichten im Mitarbeiterportal injixo Me zu sehen (Schedules).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/notifications.md
---

In diesem Artikel lernst Du, wie Du Mitarbeitern über injixo Me Zugriff auf ihre Schichtpläne gibst.

Hierfür verwendest Du Planperioden. Lies daher zuerst den Artikel {% link_new Was sind Planperioden? | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %}.

## Ermögliche Mitarbeitern, ihre Schichtpläne zu sehen

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Klicke auf _Planperioden_{:.doc-button}.
3. Wähle die **Planungseinheit**, für die Du Schichtpläne veröffentlichen möchtest.
4. Wähle eine **Auswahl**, wenn Du die Veröffentlichung der Schichtpläne auf eine bestimmte Gruppe von Mitarbeitern beschränken möchtest (optional). Wenn Du möchtest, dass alle Mitarbeiter in der Planungseinheit ihre Schichtpläne sehen können, lass das Feld leer.
5. Finde eine bestehende Planperiode mit dem Datumsbereich, für den Du die Schichtpläne veröffentlichen möchtest. Klicke auf das **Dropdown** in der Spalte _Status_ und ändere den Status auf _Veröffentlicht_. Hinweis: Wenn der Status auf _Schichtwünsche freigegeben_ voreingestellt ist, können Agenten bereits ihre Schichtpläne sehen, aber zusätzlich auch am Schichtwunsch-Verfahren teilnehmen. Wenn Du den Status wieder auf _Information_ stellst, funktioniert das Schichtwunsch-Verfahren nicht mehr.

Wenn es für den Datumsbereich noch keine Planperiode gibt, klicke auf _Planperiode erstellen_{:.doc-button}:

1. Lege einen **Zeitraum** fest, um den Datumsbereich zu definieren, für den Du die Schichtpläne veröffentlichen möchtest.
2. Wähle den **Status** _Veröffentlicht_.
3. Bei **Stichtag** musst Du nichts einstellen. Ein Stichtag ist nur relevant für das Tauschen von Schichten und das Schichtwunsch-Verfahren.
4. Bestätige mit _Speichern_{:.doc-button}.

   {{ 3 | image: 'Konfiguriere die Planperiode', '40%' }}

Deine Mitarbeiter werden nun per E-Mail und Browser-Push-Benachrichtigung darüber informiert, dass der Schichtplan im Mitarbeiterportal injixo Me sichtbar ist, ein Link führt sie direkt dorthin.

Hinweis: injixo schickt E-Mail-Benachrichtigungen an die E-Mail-Adresse der ausgewählten Benutzer. Hinweis: {% link_new Browser-Benachrichtigungen | getting-started/notifications.md %} müssen Deine Mitarbeiter erst aktivieren.
