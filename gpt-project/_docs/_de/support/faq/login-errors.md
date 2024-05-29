---
title: Anmeldefehlermeldungen 256905 und 256907
toc: false
product_label:
  - on-premise
---

Bei der Anmeldung in **injixo Enterprise on-premise** kann es zu diversen Fehlermeldungen kommen, diese sind meist mit der Fehlernummer `256907` und einem Zusatz versehen.

> Siehst Du während bei der Anmeldung die Fehlermeldung `256905-`, aktualisierte zunächst Deinen Client.

Die Meldung **Fehlgeschlagene Anmeldung. Der Client ist nicht oder nicht korrekt installiert. Nummer 256907-100** kann verschiedene Ursachen haben.

- Hast Du die Datei _regdll.bat_ im Client-Verzeichnis ohne Fehlermeldungen ausgeführt? Die Registrierung des Clients muss im Kontext des angemeldeten Windows-Benutzers ausgeführt werden. Nutze die Datei register.bat in einem Logon-Skript oder im Windows Autostart für eine Registrierung im User Context, wenn der Client über eine Software-Verteilung installiert wird.

- Verwendest Du den richtigen Browser (Internet Explorer in 32-Bit)?

- Überprüfe in den Internet-Einstellungen, ob Dein Browser ActiveX-Elemente herunterladen und ausführen darf. Weitere Informationen findest Du im Artikel {% link_new Systemvoraussetzungen | getting-started/system-requirements.md %}. Die aktuell im Internet Explorer geladenen Add-ons sollten ein oder zwei Add-ons von InVision anzeigen. Unter Umständen hilft hier die Server-Adresse in die vertrauenswürdigen Seiten aufzunehmen.

- Möglicherweise sind bestimmte Class IDs (CLSIDs) geblockt. Überprüfe Deine [Windows Gruppenrichtlinien](https://docs.microsoft.com/en-us/internet-explorer/ie11-deploy-guide/enable-and-disable-add-ons-using-administrative-templates-and-group-policy).

Wenn alles nicht funktioniert, {% link_new erstelle ein Ticket | support/create-ticket.md %}.

Alle anderen möglichen Fehlermeldungen haben wir unterhalb noch einmal aufgeführt, die meisten erklären sich selbst, manche enthalten in Klammer weitere Erklärungen.

| Fehlernummer | Meldung                                                                                                                                                                          |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 256907-3     | Der Zugriff auf den Server wurde verweigert. Ihre Anmelde-Eingaben (Benutzername, Passwort) sind nicht korrekt.                                                                  |
| 256907-4     | Sie sind bereits von einem anderen Rechner aus angemeldet. (Nur bei aktivierter Option.)                                                                                         |
| 256907-5     | Der Enterprise Server ist nicht gestartet. Warten Sie mit der Anmeldung, bis der Server gestartet ist.                                                                           |
| 256907-6     | Der Enterprise Server konnte nicht gefunden werden. Wenden Sie sich an Ihren Systemadministrator. (Der URL Parameter in der isps.cfg enthält keine oder eine falsche IP-Adresse) |
| 256907-7     | Die Verbindung zum Server ist abgebrochen. Ursache für diesen Fehler sind zumeist Netzwerkprobleme.                                                                              |
| 256907-8     | Sie können sich derzeit nicht anmelden, da alle Lizenzen benutzt werden.                                                                                                         |
| 256907-9     | Ihr Account ist deaktiviert. (Administratoren können die Checkbox für die Anmeldung des Benutzers erneut setzen. Wenn Du der einzige Administrator bist, starte den Dienst neu.) |
| 256907-10    | Die automatische Anmeldung ist fehlgeschlagen. Bitte melden Sie sich erneut unter Angabe des Benutzernamens und des Passworts an.                                                |
| 256907-11    | Sie versuchen sich mit einem Client anzumelden, der nicht zur Serverversion passt.                                                                                               |
| 256907-12    | Die Sitzungszeit ist abgelaufen. Bitte melden Sie sich erneut unter Angabe des Benutzernamens und des Passworts an.                                                              |
