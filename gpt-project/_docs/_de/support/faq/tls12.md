---
title: Abgesicherte Verbindungen (TLS 1.2)
description: Konfiguriere TLS 1.2 in Deinem Browser und Betriebssystem für eine sichere Verbindung zu injixo.
product_label:
  - advanced
  - enterprise
  - classic
---

<!-- <div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div> -->

Die injixo-Dienste sind über Internet-Browser zugänglich und nutzen sichere Internetverbindungen nach dem _Transport Layer Security_ (TLS) Standard. Moderne Browser verwenden standardmäßig den sicheren Standard TLS 1.2. Derzeit gilt nur TLS 1.2 als ausreichend sicher.

<!-- Legacy injixo Client-Komponenten, wie der injixo-Client, der Reportserver, Xlink oder eigene Ruby- und .NET-SDK-Anwendungen, verbinden sich direkt mit dem Server unter Verwendung von TLS 1.2, unabhängig von Deiner Browser-Konfiguration. Wenn Du den injixo-Client verwendest, konfiguriere Dein Windows-Betriebssystem entsprechend. -->

## Konfiguriere TLS 1.2 in Microsoft Edge

Microsoft Edge unterstützt TLS 1.2, aber Du musst TLS 1.2 manuell aktivieren:

1. Öffne das **Windows-Startmenü**, gib _Internetoptionen_ ein, und drücke die _Eingabetaste_.
2. Kicke auf den Tab **Erweitert** und scrolle nach ganz unten.
3. Aktiviere **TLS 1.2 verwenden**.
4. Klicke auf _OK_{:.doc-button}.

{{ 1 | image: 'Internetoptionen', '50%' }}

## Windows TLS 1.2 Support

Folgende Windows-Versionen unterstützen TLS 1.2:

- Windows 8, 8.1, 10 und 11
- Windows Server 2012 (R2), 2016 und 2019

In Windows 10, Windows Server 2016, 2019 und neueren Versionen ist TLS 1.2 automatisch aktiviert. In früheren Version musst Du es manuell einschalten.

Ältere Windows-Versionen unterstützen TLS 1.2 nicht. Verwende diese Versionen aus Sicherheitsgründen nicht mit injixo.

<!-- Wenn Du während eines Updates Unterstützung benötigst, wende Dich an Dein Customer Success Team. -->

## TLS 1.2 in Windows konfigurieren

Da Windows kein integriertes Tool zum Konfigurieren und Aktivieren von TLS 1.2 bereitstellt, musst Du ein externes Tool verwenden, z. B. [IIS Crypto 2.0](https://www.nartac.com/Products/IISCrypto).

Wenn Du mit dem Registrierungseditor von Windows vertraut bist, kannst Du TLS 1.2 auch manuell mit regedit.exe aktivieren:

1. Öffne **Regedit.exe** als Administrator.
2. Gehe zum Pfad  
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols`
3. Klicke mit der rechten Maustaste auf **Protokolle**, wähle **Neu**, wähle **Schlüssel**. Erstelle einen neuen Schlüssel mit dem Namen **TLS 1.2**. Überspringe diesen Schritt, wenn der Schlüssel _TLS 1.2_ bereits existiert.
4. Gehe zum neuen Pfad  
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2`.
5. Klicke mit der rechten Maustaste auf **TLS 1.2**, wählen **Neu**, wähle **DWORD-Wert (32-Bit)**. Erstelle einen neuen Eintrag **DisabledByDefault** mit dem Wert **0**.
6. Klicke erneut mit der rechten Maustaste auf **TLS 1.2**, wähle **Neu**, wähle **DWORD-Wert (32-Bit)**. Erstelle einen weiteren Wert **Enabled**.
7. Um den Wert für **Enabled** auf **1** zu ändern, doppelklicke auf **Enabled**, wähle den **Wert auf 1 einstellen** und klicke auf **OK**.
8. Starte den Computer neu.
