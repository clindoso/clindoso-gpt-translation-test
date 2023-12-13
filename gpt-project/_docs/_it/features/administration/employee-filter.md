---
title: Configurare i filtri personalizzati
description: Usa l'editor dei filtri personalizzati per filtrare i dipendenti in base a una combinazione di criteri.
product_label:
  - advanced
  - enterprise
  - classic
---

Con i filtri personalizzati è possibile creare elenchi di dipendenti che soddisfano diversi criteri. Le opzioni di modifica dipendono dai tuoi diritti utente.

I filtri personalizzati funzionano in modo simile ai {% link_new gruppi di selezione | features/administration/selections.md %}. Ecco le differenze tra i filtri personalizzati e i gruppi di selezione:

- Nei filtri personalizzati i criteri di raggruppamento sono basati sugli elementi della configurazione, come per esempio le unità di pianificazione, le qualifiche, o i contratti.
- Nei gruppi di selezione puoi creare i tuoi criteri di raggruppamento.

I filtri personalizzati sono disponibili soltanto in injixo Classic, Advanced ed Enterprise.
  
1. Per accedere all’editor dei filtri, vai su _Plan > Centro dei turni_{:.breadcrumbs}.
2. Se il riquadro Gruppi di selezione {% icon selection-filter-s | icon-only %} è selezionato: seleziona il riquadro Filtro personalizzato {% icon schedules-filter-employees-u | icon-only %}.
3. Clicca sul link **Editor filtri**.

## Creare un filtro personalizzato

1. Nella sezione **Filtro personalizzato**, clicca sull’icona Nuovo {% icon item-add | icon-only %}.
2. Seleziona il **Tipo di periodo**.<br>
    - **Assoluto**: imposta manualmente il periodo desiderato. Seleziona una data di inizio (**dal**) e una data di fine (**al**).<br>
    - **Relativo**: specifica un periodo per la settimana, il mese o l’anno: passato/a, corrente, o prossimo/a.<br>
    - **Derivato**: il periodo viene impostato automaticamente sul giorno in corso.
3. Definisci un [**filtro**](#definire-un-filtro).
4. Per visualizzare i risultati del filtro, clicca su _Applica_{:.doc-button}.
5. Per aggiungere il filtro appena creato al filtro personalizzato, clicca su _Applica_{:.doc-button}.
6. Per salvare il filtro, clicca sull’{% icon save %}.<br>Per salvare un filtro esistente con un altro nome, clicca sull’{% icon saveas %}.

## Definire un filtro

Un filtro è formato da una serie di condizioni che permettono di selezionare alcuni dati da un insieme di dati più esteso. È possibile definire dei criteri e ottenere un elenco dei dipendenti che li soddisfano.

1. Nella sezione **Criteri per il filtro**, clicca sull’{% icon item-add %}.
2. Nel primo menu a tendina, seleziona un tipo di dati di configurazione.
3. Nel secondo menu a tendina, seleziona una condizione.
4. (Facoltativo) Seleziona la [priorità e gli operatori relazionali](#utilizzare-la-priorità-e-gli-operatori-relazionali) per le unità di pianificazione, le categorie di dipendenti o le qualifiche.
5. Clicca su _Applica_{:.doc-button}.

Per modificare un filtro, clicca sull’{% icon item-edit %}.

## Utilizzare le condizioni

### IS IN

La condizione **IS IN** mostra i risultati che corrispondono esattamente al tuo filtro.
 
1. Seleziona un tipo di dati di configurazione dal primo menu a tendina.
2. Seleziona **IS IN** dal secondo menu a tendina.
3. Clicca su _Record di dati fissi_{:.doc-button} per vedere l’elenco dei criteri disponibili e selezionarne uno.
4. Per aggiungere dei criteri alla tua selezione, clicca su {% icon right-arrow-blue %}.
5. Nella finestra **Record di dati fissi**, clicca su _Applica_{:.doc-button}.
6. (Facoltativo) Seleziona [le opzioni e gli operatori relazionali](#utilizzare-la-priorità-e-gli-operatori-relazionali) per le unità di pianificazione, le categorie di dipendenti o le qualifiche.
7. Clicca su _Applica_{:.doc-button}.

### IS LIKE

La condizione **IS LIKE** mostra i risultati che corrispondono parzialmente al tuo filtro.

1. Seleziona un tipo di dati di configurazione dal primo menu a tendina.
2. Seleziona **IS LIKE** dal secondo menu a tendina.
3. Inserisci il testo che vuoi utilizzare per filtrare i risultati.
    - Per sostituire diversi caratteri, utilizza l’asterisco (*) come segnaposto.
    - Per sostituire esattamente un carattere, usa il punto interrogativo (?) come segnaposto.
4. (Facoltativo) Seleziona [le opzioni e gli operatori relazionali](#utilizzare-la-priorità-e-gli-operatori-relazionali) per le unità di pianificazione, le categorie di dipendenti o le qualifiche.
5. Clicca su _Applica_{:.doc-button}.

## Utilizzare la priorità e gli operatori relazionali

Con la casella Priorità e gli operatori relazionali, puoi includere i dipendenti in base alla loro priorità e assegnazione all’unità di pianificazione/categoria di dipendenti selezionata.  

1. Seleziona **Unità pianificativa** o **Categoria di dipendenti** dal menu a tendina.
2. Spunta la casella **Priorità**.
3. Seleziona un operatore relazionale dal menu a tendina.
4. Inserisci un valore per la priorità.

Con l’elemento di configurazione Qualifica puoi utilizzare gli operatori relazionali per includere solo i dipendenti con un certo livello di qualifica.  

1. Seleziona **Qualifica** dal menu a tendina.
2. Spunta la casella **Livelli di qualifica**.
3. Scegli un operatore relazionale dal menu a tendina.
4. Inserisci il valore del livello di qualifica.

## Combinare i filtri

È possibile combinare diversi filtri.

1. Crea o seleziona un [filtro personalizzato](#creare-un-filtro-personalizzato).
2. Definisci un [filtro](#definire-un-filtro).
3. Seleziona un operatore logico:<br>
  - **AND**: include i dipendenti che soddisfano tutte le condizioni.  
  - **OR**: include i dipendenti che soddisfano almeno una delle condizioni.  
  - **NOT**: esclude i dipendenti che soddisfano la condizione che segue NOT.
4. Crea un secondo filtro.
5. Clicca su _Applica_{:.doc-button}.

Per creare un gruppo, apri una parentesi. Per chiuderlo, chiudi la parentesi. Utilizza le frecce verso l’alto e verso il basso per spostare i singoli filtri e cambiarne l’ordine in qualsiasi momento.

## Esempio di filtro

Per filtrare i dipendenti dell’unità di pianificazione di New York che non hanno un contratto a tempo pieno di 40 ore e non appartengono al gruppo di selezione Ore extra, il filtro deve avere la struttura seguente:


```
Unità pianificativa IS IN "New York"
AND
NOT
(
Contratto IS IN "Tempo pieno 40h"
AND
Gruppo di selezione IS IN "Ore extra"
)
```

Questo filtro seleziona tutti i dipendenti dell’unità di pianificazione New York ed esclude i dipendenti che hanno un contratto a tempo pieno di 40 ore e appartengono al gruppo di selezione Ore extra:

- **IS IN** definisce la condizione per l’unità di pianificazione.
- **AND** combina le condizioni del filtro.
- **NOT** esclude le condizioni che seguono.
- Le parentesi aprono e chiudono il gruppo di condizioni da escludere.
- **IS IN** seleziona i dipendenti che hanno un contratto a tempo pieno di 40 ore.
- **AND** combina le condizioni incluse tra parentesi.
- **IS IN** seleziona i dipendenti che appartengono al gruppo di selezione Ore extra.

## Modificare i filtri personalizzati

1. Nel menu a tendina **Filtro personalizzato** seleziona un filtro.
2. Modifica le informazioni che vuoi cambiare.
3. (Facoltativo) Per cambiare il nome del filtro, clicca sull’{% icon item-edit %}.
4. Per salvare, clicca sull’{% icon save %}.<br>Per salvare un filtro esistente con un altro nome, clicca sull’{% icon saveas %}.
