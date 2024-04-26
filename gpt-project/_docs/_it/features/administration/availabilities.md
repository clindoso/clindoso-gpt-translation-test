---
title: Disponibilità
product_label:
  - advanced
  - enterprise
  - classic
description: Crea disponibilità riutilizzabili per definire i periodi in cui puoi pianificare i dipendenti.
redirect_from:
  - /it/availability-periods/
redirect_reason: rename article September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Che cos’è il Centro dei turni?
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
---

Con le disponibilità puoi definire quando un dipendente non è disponibile o è disponibile solo parzialmente per essere pianificato in giorni o orari specifici. Puoi anche restringere ulteriormente le limitazioni già definite dagli orari di apertura delle tue unità di pianificazione e dai contratti dei tuoi dipendenti.

Puoi inserire un turno o un’attività nella pianificazione soltanto se rientra nel periodo specificato. I dipendenti senza nessuna disponibilità configurata sono considerati sempre disponibili durante gli orari di apertura.

Puoi utilizzare le disponibilità per rispondere a diverse esigenze, come per esempio:

- configurare dei giorni o delle ore lavorative fisse per ogni settimana;
- alternare le disponibilità tra le settimane;
- configurare dipendenti che sono disponibili temporaneamente.

Per impostazione predefinita, injixo rispetta le disponibilità durante la creazione di pianificazioni ottimizzate. Le disponibilità non sono tenute in considerazione durante la generazione dei turni, ma durante la loro assegnazione.

injixo verifica le disponibilità soltanto se la regola di pianificazione _2611_{:.id-label} è attiva. Disattiva questa regola per permettere ai dipendenti di richiedere e ricevere turni che oltrepassano la loro disponibilità.

## Configurare le disponibilità

Puoi configurare le disponibilità nei seguenti due modi:

- Disponibilità individuali: configura le disponibilità temporanee o permanenti per i singoli dipendenti in _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
- Disponibilità per i modelli di orario: aggiungi le disponibilità alle rotazioni per assegnare la stessa disponibilità a più dipendenti.

Nota: le disponibilità per i modelli di orario sovrascrivono sia le disponibilità individuali che le disponibilità che sono state inserite manualmente.

## Configurare dei giorni o delle ore lavorative fisse per ogni settimana

Esempio: un dipendente che deve prendersi cura dei figli può lavorare soltanto la mattina dalle 8 a mezzogiorno il mercoledì e il venerdì. Puoi configurare la sua disponibilità come di seguito:

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Seleziona il dipendente dall’elenco.
3. Nella sezione **Disponibilità** a destra, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.
4. Configura la disponibilità:
    - (Facoltativo) **Validità dal** e **fino al**: se la disponibilità è valida soltanto per uno specifico periodo, queste date limitano il suo {% link_new periodo di validità | features/administration/set-a-validity-period.md %}.
    - **Tipi di giorno**: seleziona mercoledì e venerdì. Tieni premuto il tasto CTRL per selezionare più voci.
    - **dalle**: inserisci 08:00.
    - **alle**: inserisci 12:00.
5. Clicca su _OK_{:.doc-button}.

## Alternare le disponibilità tra le settimane

Le sezioni seguenti spiegano come utilizzare le disponibilità per pianificare nel caso seguente o in un caso simile:

- Il contact center è aperto dalle 8 alle 20.
- Nelle settimane pari, l’unità di pianificazione A fa i turni mattutini e l’unità di pianificazione B fa i turni pomeridiani.
- Nelle settimane dispari, l’unità di pianificazione B fa i turni mattutini e l’unità di pianificazione A fa i turni pomeridiani.
- Il turno mattutino va dalle 8 alle 14.
- Il turno pomeridiano va dalle 14 alle 20.

### Creare modelli di orario del tipo Margine di disponibilità

Per {% link_new creare modelli di orario | features/administration/daymodels/daymodel-creation.md %}, vai su _Plan > Configurazione > Modelli di orario_{:.breadcrumbs}, e clicca sull’icona Nuovo {% icon item-add | icon-only %}.<br>L’esempio seguente mostra come impostare due modelli di orario per alternare un turno mattutino e un turno pomeridiano.

Per configurare il modello di orario per il turno mattutino procedi come di seguito:

1. Crea un nuovo modello di orario.
2. Configura il modello di orario:
    - **Tipo**: seleziona **Margine di disponibilità**.
    - **Nome** e **Abbreviazione**: inserisci un nome e un’abbreviazione unici, per esempio Disponibilità 8-14 e Disp 8-14.
    - (Facoltativo) **Colore**: scegli un colore che ti aiuti a identificare il modello di orario.
    - **Inizio del margine di disponibilità**: inserisci 08:00.
    - **Fine del margine di disponibilità**: inserisci 14:00.<br> In alternativa, imposta la **Durata del margine di disponibilità**. Il massimo consentito è 48 ore.
3. Clicca su _OK_{:.doc-button}.

Per configurare il modello di orario per il turno pomeridiano procedi come di seguito:

1. Crea un nuovo modello di orario.
2. Configura il modello di orario:
    - **Tipo**: seleziona **Margine di disponibilità**.
    - **Nome** e **Abbreviazione**: inserisci un nome e un’abbreviazione unici, per esempio Disponibilità 14-20 e Disp 14-20.
    - (Facoltativo) **Colore**: scegli un colore che ti aiuti a identificare il modello di orario.
    - **Inizio del margine di disponibilità**: inserisci 14:00.
    - **Fine del margine di disponibilità**: inserisci 20:00.<br> In alternativa, imposta la **Durata del margine di disponibilità**. Il massimo consentito è 48 ore.
3. Clicca su _OK_{:.doc-button}.

### Creare e assegnare una rotazione

Per utilizzare per la pianificazione i due modelli di orario che hai appena creato, segui questi passaggi:

1. {% link_new Crea una rotazione | features/administration/shift-sequences.md | #creare-le-rotazioni %}: inserisci 2 nel campo **Righe** e 14 nel campo **Giorni**.<br>
2. Nella rotazione inserisci i modelli di orario che si alternano. Nella riga 1 inserisci il modello di orario mattutino nella settimana 1 e il modello di orario pomeridiano nella settimana 2. Nella riga 2 inserisci i modelli di orario nell’ordine inverso.
3. {% link_new Assegna la rotazione | features/administration/employee-overview.md | #assegnare-una-rotazione %} ai dipendenti.
    - Per i dipendenti dell’unità di pianificazione A, seleziona la prima riga.
    - Per i dipendenti dell’unità di pianificazione B, seleziona la seconda riga.
    - Imposta una **data di riferimento** per stabilire quando la rotazione comincia a essere pianificata. Imposta come data di riferimento il giorno della settimana in cui comincia la tua settimana pianificativa, per esempio un lunedì.
4. {% link_new Inserisci la rotazione | features/scheduling/schedules/schedules-insert-shift-sequences.md | #inserire-le-rotazioni %} nella tua pianificazione.

## Configurare dipendenti che sono disponibili temporaneamente

Esempio: uno dei tuoi dipendenti in una settimana specifica può lavorare soltanto dalle 9 alle 12.<br>Per configurare la sua disponibilità, segui la procedura per [configurare dei giorni o delle ore lavorative fisse per ogni settimana](#configurare-dei-giorni-o-delle-ore-lavorative-fisse-per-ogni-settimana). Aggiungi il {% link_new periodo di validità | features/administration/set-a-validity-period.md %} corrispondente e i valori corretti nei campi **dalle** e **alle**.

## Modificare le disponibilità

Puoi modificare le disponibilità che hai configurato per un singolo dipendente:

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Seleziona il dipendente per il quale vuoi modificare la disponibilità.
3. Nel pannello a destra, clicca su **Disponibilità**.
4. Accanto alla disponibilità che vuoi modificare, clicca sull’icona {% icon pencil %}.
5. Modifica la disponibilità.
6. Nella finestra **Disponibilità**, clicca su _OK_{:.doc-button}.
7. In fondo al pannello a destra, clicca su _OK_{:.doc-button}.

Se hai configurato delle disponibilità con i modelli di orario del tipo **Margine di disponibilità**, modifica il modello di orario come descritto di seguito:

1. Vai su _Plan > Configurazione > Modelli di orario_{:.breadcrumbs}.
2. Seleziona il modello di orario che vuoi modificare.
3. Modifica il modello di orario.
4. Clicca su _OK_{:.doc-button}.

Puoi modificare le disponibilità anche nel Centro dei turni. Scopri come {% link_new aggiungere ed eliminare le disponibilità nel Centro dei turni | features/scheduling/shiftcenter/add-and-delete-items.md | #add-an-availability %}. Per le modifiche temporanee, puoi copiare e incollare le disponibilità individuali e le disponibilità per i modelli di orario in una cella per renderle disponibilità aggiunte manualmente.

Nel Centro dei turni le disponibilità sono indicate in ciascun livello dal simbolo `<>`. Passa il mouse sopra al simbolo per vedere i dettagli. Nelle celle giornaliere, le disponibilità sono mostrate come elementi in arancione. Nelle celle giornaliere espanse, le disponibilità dei dipendenti sono mostrate come barre bianche sottolineate in arancione.

## Eliminare le disponibilità

Per eliminare le disponibilità che hai configurato per un singolo dipendente, procedi come di seguito:

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Seleziona il dipendente per il quale vuoi eliminare la disponibilità.
3. Nel pannello a destra, clicca su **Disponibilità**.
4. Accanto alla disponibilità che vuoi eliminare, clicca sull’{% icon item-delete %}.
5. Nella finestra di **Conferma**, clicca su _Sì_{:.doc-button}.
6. Clicca su _OK_{:.doc-button}.

Se hai configurato delle disponibilità con il modello di orario del tipo **Margine di disponibilità**, elimina il modello di orario:

1. Vai su _Plan > Configurazione > Modelli di orario_{:.breadcrumbs}.
2. Seleziona il modello di orario che vuoi eliminare.
3. Clicca sull’{% icon item-delete %} nella barra delle azioni.
4. Nella finestra di **Conferma**, clicca su _Sì_{:.doc-button}.

## Disponibilità in injixo Me

Puoi permettere ai {% link_new dipendenti di impostare le loro disponibilità | features/injixo-me/use-injixo-me/explore-injixo-me.md | #impostare-le-tue-disponibilità-disponibilità %} in injixo Me. I dipendenti possono aggiungere fino a un massimo di 14 disponibilità. I pianificatori devono eliminare regolarmente ogni voce obsoleta dalla lista prima di creare una pianificazione per evitare potenziali errori di pianificazione.

Per permettere ai dipendenti di impostare le loro disponibilità in injixo Me, segui questi passaggi:

1. Vai su **Me**.
2. Attiva l’opzione **Disponibilità**.

I dipendenti possono adesso aggiungere o modificare le loro disponibilità settimanali in Me. La loro disponibilità apparirà nei loro dati di configurazione.