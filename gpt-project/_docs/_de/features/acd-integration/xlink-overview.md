---
title: Xlink-Übersicht
promote-service: acd-integration-support
product_label:
  - on-premise
description: Nutze die Xlink-Anwendung, um Daten in injixo zu importieren. Erfahre, wie Du sie installierst und konfigurierst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-installation-configuration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-import-mode.md
---

Xlink ist die Applikation zum Import aus externen Systemen wie ACD-Systemen in Dein injixo System. Die _Xlink Suite_{:.menu-item} steht als Download unter [downloads.injixo.com](https://downloads.injixo.com) zur Verfügung.

Xlink importiert zwei verschiedene Datentypen:

- Anrufdaten in Queues (**PhoneLink**)
- Mitarbeiterbezogene Anmelde-/Abmeldedaten (**TimeLink**).

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

## Technische Voraussetzungen

- Betriebssystem: Windows Server 2012/Windows 7 (oder höher)
- CPU : 2 Kerne \@2,2GHz (oder höher)
- RAM: 2 GB (ohne Betriebssystem)
- Festplatte: 20 GB Festplatte (ohne Betriebssystem)

Hinweis: XLink kann auch in einer virtualisierten Umgebung installiert werden.

## Xlink Windows-Dienst (isps_uls.exe)

Xlink nutzt einen Windows-Dienst für den Datenimport. Der Dienst mit dem Namen _ISPS XLink_ importiert immer alle Daten eines ganzen Tages. Der Dienst kann nur einmal auf demselben Rechner installiert werden und startet nach der Installation automatisch.

Gib **isps_uls.exe** in der Windows-Kommandozeile ein, um die verfügbaren Parameter zu sehen:

- _-install_/_-remove_: installiert oder deinstalliert den _ISPS XLink_ Dienst. Bei der Installation steht der Parameter _Starttyp_ standardmäßig auf _Automatisch_, um einen Dienst-Neustart nach einem Server-Neustart zu gewährleisten.
- _-console_: startet den Dienst im Konsolenmodus. Dieser Modus verwendet das Benutzerkonto, das mit der Windows-Sitzung verknüpft ist. Mit dieser Option kannst Du Konfigurationsprobleme identifizieren.

Hinweis: Nach der Installation nutzt der Windows-Dienst standardmäßig die Anmelde-Option _Lokales Systemkonto_ (Tab _Anmelden als_). Konfiguriere ein Administrator-Konto, wenn trotz korrekter Konfiguration keine Werte importiert werden oder Xlink nicht auf den Import-Ordner zugreifen kann.

Lies den Artikel {% link_new Xlink installieren und konfigurieren | features/acd-integration/xlink-installation-configuration.md %} für detaillierte Installationsanweisungen.

## Xlink Benutzeroberfläche (isps_ul.exe)

Xlink hat eine Benutzeroberfläche, in welcher Du Einstellungen vornehmen, {% link_new PhoneLink-Mappings erstellen/ändern | features/acd-integration/xlink-mapping-telephony.md %} oder den {% link_new Datenimport konfigurieren/manuell starten | features/acd-integration/xlink-import-mode.md %} kannst.

Hinweis: Die Benutzeroberfläche nutzt standardmäßig Englisch. Um dies zu ändern, kopiere die beiden Dateien aus den Unterordnern Deiner bevorzugten Sprache in das Installationsverzeichnis. Überschreibe die vorhandenen Dateien.

Führe die Datei **isps_ul.exe** aus, um die Benutzeroberfläche zu starten.

{{ 1 | image: 'Xlink-Benutzeroberfläche'}}

Die Benutzeroberfläche besteht aus drei Bereichen:

- _Schnittstelle_: Unter _WFM_{:.menu-item} angelegte externe Systeme.
- _iWFM Queues_: Erstellte Queues und zugeordnete Wertetypen aus Deinem injixo-Tenant.
- _Zugeordnete Kennzahlen_: Mappings für die ausgewählte Queue. Keine Einträge, wenn keine Mappings vorhanden sind.

## Konfiguration und Mappings sichern

Um die Konfiguration nach einer Neuinstallation (im Falle eines Datenverlustes) wieder herstellen zu können, sichere die folgenden Dateien regelmäßig:

- isps_ul.ini
- acd_map.ini
- isps.cfg
- \*.bas
