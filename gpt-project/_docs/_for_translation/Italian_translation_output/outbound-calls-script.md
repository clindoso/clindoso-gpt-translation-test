---
title: Script per le chiamate in uscita <!-- TM 100 -->
description: Calcola il fabbisogno di personale per le chiamate in uscita. <!-- TM 100 -->
toc: true
product_label:
- essential
- advanced
- enterprise
- classic
redirect_from:
- "/requirement-outbound/"
redirect_reason: Updated filename on 18 March 2024
gpt_translation: true
---

Utilizza lo script per le chiamate in uscita per calcolare il fabbisogno di personale per le campagne con chiamate in uscita. Il calcolo si basa sul totale di contatti gestiti nella campagna, sulla durata della campagna e sul tempo medio di gestione (AHT) previsto. <!-- TM 100 -->

## Prerequisiti <!-- TM 100 -->

Per calcolare il fabbisogno di personale con una previsione sulla distribuzione delle chiamate, devi prima esportare la previsione: <!-- TM 100 -->

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload. <!-- TM 100 -->
2. Seleziona il periodo nel selettore di data. Clicca sul numero della settimana per selezionare la settimana per intero, oppure clicca e trascina per selezionare un periodo più breve o più lungo. <!-- TM 100 -->
3. Dal {% icon ellipsis_v %} in alto a destra, seleziona **Utilizza previsione**. <!-- TM 100 -->
4. Nella finestra **Utilizza questa previsione per calcolare il fabbisogno di personale**, seleziona la previsione che vuoi utilizzare. <!-- TM 100 -->
5. Clicca su _Utilizza previsione_{:.doc-button}. <!-- TM 100 -->
6. Clicca su _Chiudi_{:.doc-button}. <!-- TM 100 -->

In alternativa, puoi utilizzare lo script per le chiamate in uscita per calcolare il fabbisogno di personale senza nessuna previsione. Scopri come configurare i parametri per farlo nella tabella relativa alla sezione [Dati della campagna](#sezione-dati-della-campagna). <!-- TM 100 -->

## Configurare lo script <!-- TM 100 -->

1. Vai su _Forecast > Script di fabbisogno_{:.breadcrumbs}. <!-- TM 100 -->
2. Nel riquadro **Chiamate - In uscita**, clicca su _Apri_{:.doc-button}.   <!-- GPT translation -->

La finestra di configurazione dello script include tre sezioni. Scopri come configurare i parametri nelle tabelle seguenti. <!-- TM 100 -->

### Sezione Dati della campagna <!-- TM 100 -->

| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 100 -->
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Servizio                        | Seleziona la coda per la quale vuoi utilizzare lo script.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | <!-- TM 100 -->
| Record                      | Il numero totali di contatti per la tua campagna. Seleziona **fisso** e inserisci un valore nel campo sottostante per calcolare il fabbisogno di personale senza una previsione. Seleziona **variabile** e seleziona un tipo di valore con una previsione sui contatti da raggiungere.                                                                                                                                                                                                                                                                                                                                                                                                                                                             | <!-- TM 100 -->
| Valutazione contatto (%) (tasso di connessione)             | La percentuale di chiamate in uscita che ricevono risposta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | <!-- TM 100 -->
| Tasso di ricomposizione (%)              | La percentuale di contatti che vengono richiamati dopo dei tentativi infruttuosi. I tentativi di ricomposizione sono distribuiti lungo tutto il periodo che configuri con i parametri **Data d’inizio** e **Data di fine**. Per saperne di più sul tasso di ricomposizione vai alla [sezione dedicata](#che-cosè-il-tasso-di-ricomposizione). | <!-- TM 100 -->
| Data d’inizio                   | L’inizio del periodo utilizzato per il calcolo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | <!-- TM 100 -->
| Data di fine                     | La fine del periodo utilizzato per il calcolo. Seleziona **Data** e inserisci una data nel campo sottostante, o seleziona **Giorni durata della campagna** e inserisci un valore nel campo sottostante.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | <!-- TM 100 -->
| Valutazione collegamento parte giusta (%) (tasso di connessioni riuscite) | La percentuale di chiamate alle quali rispondono gli interlocutori desiderati. Seleziona **fisso** e inserisci un valore nel campo sottostante, o seleziona **variabile** e seleziona un tipo di valore con una previsione sul tasso di connessioni riuscite.                                                                                                                                                                                                                                                             | <!-- TM 100 -->
| Riduzione (%)                | (Facoltativo) La percentuale di ore lavorative retribuite durante la quale i dipendenti non sono disponibili a gestire i contatti, per esempio a causa di pause o assenze per malattia non pianificate.     | <!-- TM 100 -->

### Sezione Durata media di gestione <!-- TM 100 -->

| Parametro        | Descrizione                                                                      | <!-- TM 100 -->
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fisso/variabile   | Seleziona **fisso** e inserisci dei valori fissi nei campi sottostanti, oppure seleziona **variabile** e inserisci dei tipi di valori nei campi sottostanti.                                                                                                                                                                                                                         | <!-- TM 100 -->
| RPC espresso in secondi   | L’AHT, espresso in secondi, per una chiamata con l’interlocutore desiderato. Questo valore include l’elaborazione post-chiamata.                                                                                                                                                                                                                                                       | <!-- TM 100 -->
| WPC espresso in secondi   | L’AHT, espresso in secondi, per una chiamata a cui risponde l’interlocutore sbagliato, per esempio una chiamata a cui risponde un’altra persona o una chiamata che viene inoltrata alla segreteria telefonica.              | <!-- TM 100 -->


### Sezione Carico di lavoro <!-- TM 100 -->

| Parametro        | Descrizione                                                                                                                                                                                                      | <!-- TM 100 -->
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unità pianificativa    | L’unità pianificativa per la quale vuoi calcolare il fabbisogno di personale. Se cambi l’unità di pianificazione, il menu a tendina **Attività** viene aggiornato con le attività assegnate all’unità di pianificazione. | <!-- TM 100 -->
| Attività         | L’attività per la quale vuoi calcolare il fabbisogno di personale.                                                                                                                                            | <!-- TM 100 -->
| Risorse minime    | Il numero minimo di dipendenti necessari per intervallo. Inserisci un valore per sovrascrivere gli intervalli che hanno un fabbisogno di personale più basso.                                                                                          | <!-- TM 100 -->
| Risorse massime    | Il numero massimo di dipendenti necessari per intervallo. Inserisci un valore per sovrascrivere gli intervalli che hanno un fabbisogno di personale più alto.                                                                                         | <!-- TM 100 -->

## Avviare lo script <!-- TM 100 -->

- Per avviare il calcolo, clicca su _OK_{:.doc-button}.<br>Si apre una finestra che mostra i parametri che hai selezionato e i risultati dello script. <!-- TM 100 -->

 Puoi vedere il {% link_new fabbisogno di personale salvato nel Centro dei turni | features/scheduling/edit-or-delete-staff-requirements.md %}. <!-- GPT translation -->

Nota: in injixo Enterprise on-premise vai su *WFM > Prev. > ForecastPro > Forecast* o su *WFM > Admin. > Forecasting > Scripts*. Lo script richiede una previsione esistente per la combinazione di coda, tipo di valore e versione. Il nome dello script potrebbe variare, dato che è possibile inserire un nome personalizzato durante la creazione dello script. <!-- GPT translation -->

## Che cos’è il tasso di ricomposizione? <!-- TM 100 -->

Il tasso di ricomposizione è la percentuale di chiamate che vengono ritentate dopo dei tentativi infruttuosi. I tentativi di chiamata vengono ripetuti finché il numero di chiamate senza risposta è minore di 1.<br>Esempio: vuoi raggiungere un totale di 5000 persone. Un tasso di ricomposizione del 10% significa che durante il secondo tentativo vengono ritentate 500 chiamate senza risposta, durante il terzo tentativo vengono ritentate 50 chiamate senza risposta, durante il quarto tentativo vengono ritentate 5 chiamate senza risposta. In questo esempio il numero totale di chiamate effettuate è 5555. <!-- TM 100 -->

