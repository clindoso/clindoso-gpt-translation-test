---
title: Internet-Explorer-Modus in Microsoft Edge einrichten
product_label:
  - advanced
  - enterprise
  - classic
description: Richte den Internet-Explorer-Modus in Microsoft Edge ein, um alle Module von injixo nutzen zu können - auch solche, die ActiveX verwenden.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

In diesem Artikel lernst Du:
- wie Du Microsoft Edge einrichtest, um injixo zu nutzen.
- wie Du den Internet-Explorer-Modus (IE-Modus) in Microsoft Edge konfigurierst.

Das WFM-Modul (https://\*.injixo.com/iwfm/\*) benötigt Microsoft&nbsp;Edge im [Internet-Explorer-Modus](https://docs.microsoft.com/de-de/deployedge/edge-ie-mode) (IE-Modus). injixo unterstützt Microsoft&nbsp;Edge ab Version 97. In Microsoft&nbsp;Edge kannst Du die Version unter der URL *edge://version* überprüfen.

Um folgende Schritte auszuführen, benötigst Du Windows-Administratorrechte. Wende Dich ggf. an Deine IT-Abteilung. 

## Client vorbereiten

1. Öffne das **Windows-Startmenü**.
2. Suche nach **Internetoptionen**.
3. Im Tab **Sicherheit**, aktiviere den **Geschützten Modus** für die Zone **Internet**.
4. Klicke *Sites*{:.doc-button}. 
5. Klicke *Hinzufügen*{:.doc-button}.
6. Füge *\*.injixo.com* zu den vertrauenswürdigen Seiten hinzu.
7. Um Deine Änderungen zu speichern, klicke *OK*{:.doc-button}.

    {{ 4 | image: "Geschützter Modus in den Internetoptionen",  '30%' }}

## Internet Explorer Modus in Edge konfigurieren

Konfiguriere den Internet Explorer Mode mithilfe einer XML-Datei, die eine Sitelist enthält. 

Hinweis: Das Beispiel unterhalb verwendet eine lokal gespeicherte Sitelist-Datei. Alternativ kannst Du die Datei auch auf einem Server hosten und sie so für alle Benutzer verfügbar machen.

### 1. Sitelist-XML-Datei erstellen

1. Erstelle eine neue XML-Datei (z. B. *sitelist.xml*) mit folgendem Inhalt:

    ```
    <site-list version="1.0">
      <!-- iwfm-xxxx muss Dein injixo-Host sein. Du findest ihn in der URL des injixo WFM-Moduls -->
      <site url="https://iwfm-xxxx.injixo.com/iwfm/">
        <compat-mode>Default</compat-mode>
        <open-in>IE11</open-in>
      </site>
      <shared-cookie 
        domain=".injixo.com" 
        name="injixo_session" 
        source-engine="MSEdge">
      </shared-cookie>
      <shared-cookie 
        domain=".injixo.com" 
        name="iwfm_language_id" 
        source-engine="MSEdge">
      </shared-cookie>
    </site-list>
    ```

2. Klicke in injixo auf **WFM**, um das WFM-Modul aufzurufen, und kopiere die angezeigte **URL**.
3. Ersetze in der XML-Datei den Wert für die URL durch Deine injixo-Host-URL. 
4. Speichere die Datei auf Deinem Computer.

Erfahre mehr in der [Microsoft-Dokumentation](https://docs.microsoft.com/en-us/deployedge/edge-ie-mode). 

### 2. Windows-Registrierung anpassen

1. Um in den Registrierungseditor zu gelangen, öffne das Windows-Startmenü, gib **regedit** ein und drücke **Enter**. 
2. Gehe zu **HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft**.
3. Um das Kontextmenü zu öffnen, rechtsklicke den **Microsoft**-Ordner. 
4. Erstelle einen neuen Schlüssel **Edge** (falls dieser noch nicht existiert).

Füge den Eintrag *InternetExplorerIntegrationLevel* hinzu: 

1. Um das Kontextmenü zu öffnen, rechtsklicke auf den neuen **Edge**-Ordner.
2. Füge einen neuen **DWORD-Wert 32-bit** hinzu.
3. Nenne den neuen Eintrag *InternetExplorerIntegrationLevel*.  
4. Doppelklicke auf den neuen **DWORD**-Eintrag 
5. Gib *1* (oder hexadezimal: 0x00000001) ein.

Füge den Eintrag *InternetExplorerIntegrationSiteList* hinzu: 

1. Um das Kontextmenü zu öffnen, rechtsklicke auf den neuen **Edge**-Ordner.
2. Füge eine **Zeichenfolge** hinzu.
3. Nenne den neuen Eintrag *InternetExplorerIntegrationSiteList*. 
4. Doppelklicke auf den neuen **REG_SZ**-Eintrag.
5. Gib den Pfad zur Sitelist-XML-Datei an (z. B. *file:///c:/path/to/sitelist.xml*).  
   Hinweis: Wenn Du die Sitelist hostest, gib die Server-URL ein, z. B. *https://your.company.com/sitelist.xml*.

Um alle Änderungen zu speichern, klicke *Ok*{:.doc-button}. 

### 3. Die neue Sitelist aktivieren

Damit Edge die neue Sitelist verwendet, fahre wie folgt fort:

1. Starte Edge neu.
2. Um die Sitelist-Konfiguration anzuzeigen (und zur Fehlersuche), gehe zu [edge://compat](edge://compat). 
3. Um die Konfiguration zu übernehmen, klicke **Update erzwingen**{:.doc-button}. 

Die Liste aktualisiert sich und zeigt die konfigurierte URL unter *Domain* an.

Du kannst Dich jetzt bei injixo anmelden. Nur das WFM-Modul verwendet den IE-Modus (gekennzeichnet durch ein Internet Explorer-Symbol neben der URL). Alle anderen Module (z. B. Plan) verwenden den normalen Edge-Modus.

> Wenn Edge nicht vom IE-Modus in den Standard-Edge-Modus zurückschaltet, lösche die Cookies in Edge.

Tipp: Um die konfigurierten Registrierungseinträge und Richtlinien zu sehen, gehe zu [edge://policy/](edge://policy/).

## Sleeping Tabs deaktivieren

Standardmäßig gehen Edge-Tabs nach zwei Stunden Inaktivität in den Ruhezustand über. In injixo Advanced und Enterprise WFM wird die Verbindung zum Schicht Center unterbrochen. 

Um zu verhindern, dass Tabs in den Ruhezustand übergehen, füge *injixo.com* zur Blockierliste in den Edge-Einstellungen hinzu:

1. Öffne Microsoft Edge.
2. Klicke auf **Einstellungen und mehr** (...) oder drücke **Alt+F**.
3. Klicke auf **Einstellungen**.
4. Klicke links auf **System**.
5. Klicke im Abschnitt *Ressourcen sparen* neben *Niemals diese Seiten in den Ruhezustand versetzen* auf **Hinzufügen**.
6. Gib im Eingabefeld *https://www.injixo.com* ein.
7. Klicke auf **Hinzufügen**.
8. Schließe den Tab **Einstellungen**.

Hinweis: Windows-Administratoren können diese Ausnahme und das Intervall für den Ruhezustand auch über Gruppenrichtlinien konfigurieren.
