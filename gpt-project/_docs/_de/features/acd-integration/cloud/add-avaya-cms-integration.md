---
title: Avaya CMS-Integration hinzufügen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du deine Avaya-Datenbank mit injixo verbinden kannst, um Daten zu importieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Eine Avaya CMS-Integration ist eine On-premise-Integration, die Anruf- und Agentenstatus-Daten importiert.

Die Integration verwendet {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Avaya CMS-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der **Avaya CMS**-Kachel auf _Integration hinzufügen_{:.doc-button}.

## Deine neue Avaya CMS-Integration einrichten

1. Gib einen eindeutigen Namen für die neue Integration ein.
   Dieser Name hilft dir, die Datenquelle zu identifizieren und die Queue zu bestimmen, zu der die Integration gehört.<br>Beispiel: Avaya-Integration - Customer-Support-Team
1. Installiere und verbinde {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
1. Richte im Abschnitt **Konfiguration** deine Integration ein:
 - Gib den [Connection String](#connection-string) ein, der die Parameter enthält, um die Verbindung zu deiner CMS-Datenbank herzustellen. 
 - Wähle die Zeitzone der Datenbank aus dem Dropdown-Menü aus.
 - Aktiviere die Checkbox **Agentenstatus mit Details importieren**, um importierten Agentenstatus Informationen über Skills (Agentenprofil) und Splits (Anrufweiterleitung) hinzuzufügen.
 - Um Agentenstatus-Daten in Echtzeit zu importieren, aktiviere die Checkbox **Echtzeitdaten importieren**. Gib in diesem Fall zusätzlich eine Portnummer in das Feld **Port** ein.<br>
   injixo Cloud Link öffnet einen TCP-Socket, der auf dem angegebenen Port lauscht. Der Avaya Generic RTA-Dienst verbindet sich mit diesem Anschluss und streamt Agentenstatus-Daten in Echtzeit. Der Avaya Generic RTA-Dienst ist in Avaya lizenziert und konfiguriert.
1. Klicke auf _Speichern_{:.doc-button}, um die Integration zu erstellen.

Die Integration beginnt, Daten zu injixo zu importieren. Um Agentenstatus-Daten zu importieren, musst du zunächst {% link_new externe Benutzerkennungen und Aktivitäten zuordnen | features/acd-integration/cloud/import-agent-status-data.md %}, sobald deine Avaya-Integration eingerichtet ist. Wenn du zuvor die Option **Echtzeitdaten importieren** ausgewählt hast, pausiere den Datenimport deiner Integration.

## Connection String

Die Avaya CMS-Integration benötigt den Connection String, um die Verbindung zu deiner Avaya CMS-Datenbank herzustellen. Avaya CMS verwendet üblicherweise eine IBM Informix-Datenbank. Deshalb benötigst du einen speziellen Connection String. 

Beispiele für Connection Strings, die den IBM Informix ODBC-Treiber verwenden:<br>
- `DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;` (nativer Zugriff über den ODBC-Treiber)
- `DSN=AvayaCMS;DELIMIDENT=y;` (erfordert eine ODBC-Verbindung mit dem Namen AvayaCMS)
Wenn dein Avaya CMS keine IBM Informix-Datenbank verwendet, musst du selbst dafür sorgen, den passenden Connection String für deinen spezifischen Datenbanktyp und -treiber zu erhalten. Avaya unterstützt nur ODBC-Konnektivität.

## Avaya CMS-Integration bearbeiten

Wenn sich etwas an den Details deiner Integration ändert, z.&nbsp;B. die Zugangsdaten zum Datenbankserver, kannst du die Konfiguration deiner Integration bearbeiten und aktualisieren. Der Datenimport läuft unter der aktualisierten Konfiguration weiter.
