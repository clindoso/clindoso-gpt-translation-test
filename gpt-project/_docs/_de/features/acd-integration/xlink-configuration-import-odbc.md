---
title: ODBC-Import
redirect_from: /de/xlink-configuration-import-odbc/
product_label:
  - on-premise
redirect_reason: renamed file in September 2021
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-mapping-telephony.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-mapping-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-import-mode.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-log-files.md
  - overwrite_title: Add title for untranslated source
    filepath: support/faq/xlink-frequent-error-messages.md
---

In diesem Artikel lernst Du, wie Du verschiedene Xlink-ODBC-Schnittstellen konfigurierst, um Daten aus Datenbanktabellen oder Datenbank-Views in injixo zu importieren.

Xlink bietet verschiedene Standardschnittstellen mit einer festen Logik und die konfigurierbare Universal-Schnittstelle.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

## Voraussetzungen

Um eine ODBC-Schnittstelle konfigurieren zu können, benötigst Du folgendes:

- Eine korrekte {% link_new Xlink-Installation | features/acd-integration/xlink-installation-configuration.md %} und ein {% link_new externes System für eine ODBC-Schnittstelle | features/acd-integration/new-external-system.md %}, z.B. Avaya CMS, Bosch BCC (Avaya CIE) oder die Universal-Schnittstelle (Beispiel für Avaya Aura unterhalb).

- Eine funktionierende 32-Bit-ODBC-Verbindung, die als _System-DSN_ unter _c:\Windows\SysWOW64\\odbcad32.exe_ angelegt wurde und auf die der im Xlink-Dienst konfigurierte Benutzer zugreifen kann.  
  Hinweis: Erstelle nicht versehentlich eine 64-Bit-ODBC-Verbindung und stelle sicher, dass Du keine User-DSN mit demselben Namen hast.

Erkundige Dich bei Deinem ACD-Hersteller nach speziellen ODBC-Treibern, die für die Verbindung erforderlich sein könnten. Der Benutzer, der sich mit der Datenbank verbindet, benötigt Lesezugriff auf die von der Schnittstelle verwendeten Tabellen oder Views.

## Standard-Schnittstelle einrichten

1. Doppelklicke auf die Datei **isps_ul.exe**, um die Xlink-Benutzeroberfläche zu öffnen.
2. Rechtsklicke auf das konfigurierte **externe System** auf der linken Seite und wähle _Konfiguration_{:.menu-item}, um den Konfigurationsdialog zu öffnen.
3. Gib den **Namen der ODBC-Verbindung**, den **Datenbankbenutzer** und das **Passwort** ein.
4. Klicke auf _Ok_{:.doc-button}, um die Einstellungen zu speichern.

Nachdem Du diese Schritte durchgeführt hast, wird in der Konfigurationsdatei _isps_ul.ini_ der dazugehörige Konfigurationsabschnitt erzeugt.

Die linke Seite der Xlink-Anwendung zeigt eine Baumstruktur unter dem externen System an, wenn die Verbindung erfolgreich war. Falls nicht, überprüfe den Inhalt der Datei _call_tree.log_.

## Universal-Schnittstelle einrichten

Die Universal-Schnittstelle unterstützt die folgenden Datenbanksysteme: Oracle, Microsoft SQL Server, MySQL, Caché DBMS, Microsoft Access, Informix, PostgreSQL

Die Parameter der Universal-Schnittstelle für den Anruf- und Agentstatus-Import sind in der Dokumentation beschrieben, die unter [downloads.injixo.com](https://downloads.injixo.com) verfügbar ist.

So erstellst Du die initiale Konfiguration:

1. Doppelklicke auf die Datei **isps_ul.exe**, um die Xlink-Benutzeroberfläche zu öffnen.
2. Rechtsklicke auf das konfigurierte **externe System** auf der linken Seite und wähle _Konfiguration_{:.menu-item}, um den Konfigurationsdialog zu öffnen.
3. Gib den **Namen der ODBC-Verbindung**, den **Datenbankbenutzer** und das **Passwort** ein.
4. Klicke auf _Ok_{:.doc-button}, um die Einstellungen zu speichern.
5. Öffne die Konfigurationsdatei **isps_ul.ini** und füge der neuen Sektion _[Name Deines externen Systems]_ folgende Zeilen hinzu:

   ```
   QueueSQL = select queue_name (or queue id) from queue_table order by queue_name
   ValueTypes = valuetype_1;valuetype_2;valuetype_3
   TimeStampColumn = start_date_column
   QueueNameColumn = queue_name_column
   CallDataTable = source_table_name

   ActivitySQL = SELECT DISTINCT activiy_name_column, activity_ID_column FROM source table
   ActivityTimeSpanType = 1 ;(start and end time only)
   ActivityColumn = activity_name_column
   AgentColumn = agent_login_id_column
   ActivityStartTimeStampColumn = start_time_column
   ActivityStartTimeStampType = 2 ;(date/time field)
   ActivityEndTimeStampColumn = end_time_column
   ActivityEndTimeStampType = 2 ;(date/time field)
   AgentActivityTable = source table name
   ```

6. Das Beispiel oberhalb dient nur zur Veranschaulichung. Passe die einzelnen Spalten und Tabellen- oder View-Namen an Deine Quell-Datenbank an. Du musst die Werte für die Datenbankfelder für _queue_name_, _queue_table_, \*valuetype\_\**, *start_date_column*, *queue_name_column* und *source_table_name* durch die entsprechende Quelldatenbank oder -tabelle ersetzen. Dasselbe gilt für die Felder der *Activity\*-Parameter\*.
7. Ändere den Wert für den Parameter _Protocol_ von 0 auf 1.
8. Speichere die Änderungen an der Datei.
9. Starte den **ISPS XLink** Dienst neu.
10. Öffne die **isps_ul.exe** erneut.

Nachdem Du diese Schritte durchgeführt hast, wird in der Konfigurationsdatei _isps_ul.ini_ der dazugehörige Konfigurationsabschnitt erzeugt.

Die linke Seite der Xlink-Anwendung zeigt eine Baumstruktur unter dem externen System an, wenn die Verbindung erfolgreich war. Falls nicht, überprüfe den Inhalt der Datei _call_tree.log_ auf SQL-Fehler.

### Die Konfiguration der Universal-Schnittstelle individuell anpassen

Um die Universal-Schnittstelle konfigurieren zu können, musst Du die Struktur bzw. Spalten und die Datentypen in der Tabelle kennen, aus der die Daten gelesen werden.

Du kannst die PhoneLink-und TimeLink Parameter nach Deinen Bedürfnissen anpassen. Informationen zu den Parametern findest Du in der Dokumentation, die unter [downloads.injixo.com](https://downloads.injixo.com) verfügbar ist.

Einige weitere nützliche Hinweise:

Für den Parameter _ActivitySQL_ benötigt Xlink sowohl den Namen als auch die ID der Aktivität in der ACD, z.B. _SELECT DISTINCT activiy_name_column, activity_ID_column FROM source_table_. Fragst Du nur den Namen ab, funktioniert der Import später nicht. In der Logdatei erscheint dann nur Activity 0.

_ActivityStartTimeStampType_ und _ActivityEndTimeStampType_ definieren, wie Datum- und Zeitangaben interpretiert werden, standardmäßig als Date/Time-Feld (Wert 2); andere mögliche Werte sind 0 (Character String) oder 1 (Unix Zeitstempel). Liegt das Datum als Character String vor, verwende Wert 0 und zusätzlich die Parameter _ActivityStartTimeStampFormat_ und _ActivityEndTimeStampFormat_.

_ActivityStartTimeStampColumn_ definiert die Spalte, die die Startzeit einer zu importierenden Aktivität enthält. Je nachdem, welche Information Deine Datenbank bereithält, verwende zusätzlich:

- _ActivityDurationColumn_ und _ActivityTimeSpanType=0_ für
  den Import mit Startzeit und Dauer.
- _ActivityEndTimeStampColumn_ und _ActivityTimeSpanType=1_ für den Import mit Startzei und Endzeit.

* _ActivityTimeSpanType=2_ und _LogOffActivities_ für den Import nur über die Starzeit. Die Aktivität wird automatisch beendet, wenn eine neue Aktivität startet. _LogOffActivities_ definiert (über eine Semikolon-getrennte Liste von IDs) die Aktivitäten aus der ACD, die einen Logout darstellen.

### PhoneLink-Beispiel für die Universal-Schnittstelle für Avaya Aura

1. Doppelklicke auf die Datei **isps_ul.exe**, um die Xlink-Benutzeroberfläche zu öffnen.
2. Rechtsklicke auf das konfigurierte **externe System** auf der linken Seite und wähle _Konfiguration_{:.menu-item}, um den Konfigurationsdialog zu öffnen.
3. Gib den **Namen der ODBC-Verbindung**, den **Datenbankbenutzer** und das **Passwort** ein.
4. Klicke auf _Ok_{:.doc-button}, um die Einstellungen zu speichern.
5. Öffne die Konfigurationsdatei **isps_ul.ini** und füge der bestehenden Sektion _[Name des externen Systems]_ folgende Zeilen hinzu:

   ```
   QueueSQL=select Name from Application order by Name
   QueueMappingSQL=select Name, ApplicationID from Application order by Name
   ValueTypes=CallsOffered;TalkTime;WaitTime;PostCallProcessingTime;CallsAnswered
   TimeStampColumn=""Timestamp""
   TimeStampType=2
   QueueNameColumn=ApplicationID
   QueueNameType=1
   RetrieveValueTypesUsing=1
   CallDataTable=iApplicationStat
   ```

6. Speichere Deine Änderungen.
7. Starte den **ISPS XLink** Dienst neu.
8. Öffne die _isps_ul.exe_ erneut. Eine Baumstruktur unter dem konfigurierten externen System auf der linken Seite zeigt Queues und Wertetypen. Falls nicht, prüfe die Datenbank-Verbindung und die Log-Dateien.

<!-- Für TimeLink wird keine Baumstruktur angezeigt, prüfe in der Xlink-Oberfläche unter *Ansicht > Aktivitäten*{:.breadcrumbs}, welche Aktivitäten aus dem externen System den injixo-Aktivitäten zugeordnet wurden. -->

Erstelle Mappings zwischen Deiner ACD und injixo, um bestimmte Daten zu importieren. Überprüfe die Protokolldateien auf mögliche SQL-Fehler, die durch eine falsche Konfiguration verursacht wurden. Passe die Konfiguration an, starte den Dienst neu und führe mehrere Importe durch, um alle Fehler zu beheben und den korrekten Datenimport sicherzustellen.
