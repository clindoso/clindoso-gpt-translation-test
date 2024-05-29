---
title: Talkdesk-Integration hinzufügen
description: Erfahre, wie du deine Talkdesk-ACD mit injixo verbinden kannst, um Daten zu importieren.
toc: false
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Overwrite untranslated EN title
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

Eine Talkdesk-Integration ist eine Cloud-Integration, die historische Anruf- und Agentenstatus-Daten importiert.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Talkdesk-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Talkdesk**-Kachel auf _Integration hinzufügen_{:.doc-button}.
4. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
5. Gib im Formular im Abschnitt **Zugangsdaten** deine Talkdesk-spezifischen Informationen ein:

   - Gib deinen Talkdesk-Accountnamen ein.
   - Gib die Client-ID und das Client-Secret eines Talkdesk-OAuth-Clients ein.

     > Erstelle für die Client-ID und das Client-Secret in Talkdesk einen [neuen OAuth-Client](https://docs.talkdesk.com/docs/creating-a-new-oauth-client).
     >
     > Du kannst auch einen bestehenden OAuth-Client verwenden, der wie folgt konfiguriert ist:
     >
     > - Berechtigungstyp: client-credentials
     > - Berechtigungen: data-reports:read und data-reports:write

6. Wähle im Abschnitt **Konfiguration** deine Kontoregion aus.

7. Klicke auf _Integration speichern_{:.doc-button}.  
   Die Integration testet die Verbindung und meldet Probleme, sofern vorhanden.  
   Wenn die Prüfung erfolgreich war, beginnt die Integration mit dem Importieren von Daten in injixo.

<!-- ## Talkdesk Data in injixo -->

## Wie geht’s weiter?

Wenn Anrufdaten in Queues importiert wurden, kannst du deinen ersten Workload erstellen. Um mehr darüber zu erfahren, wie du Agentenstatus-Daten einrichtest, sieh dir die verwandten Artikel an.
