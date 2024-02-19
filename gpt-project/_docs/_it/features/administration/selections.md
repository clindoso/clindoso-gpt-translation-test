---
title: Creare e gestire i gruppi di selezione
description: Crea gruppi di selezione e assegna loro dei dipendenti.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
related_articles:
  - overwrite_title: Utilizzare i gruppi di selezione per filtrare i dipendenti
    filepath: best-practices/filter-with-selections.md
---

I gruppi di selezione sono criteri di raggruppamento che puoi utilizzare per filtrare i dipendenti. I gruppi di selezione funzionano in modo simile ai {% link_new filtri personalizzati | features/administration/employee-filter.md %}. Si differenziano per le seguenti caratteristiche:

- Nei gruppi di selezione puoi definire criteri di raggruppamento personalizzati.
- Nei filtri personalizzati i criteri di raggruppamento sono basati sugli elementi della configurazione, come, per esempio, le unità di pianificazione, le qualifiche, o i contratti.

Inoltre, i filtri personalizzati sono disponibili soltanto in injixo Classic, Advanced e Enterprise.

I gruppi di selezione sono generalmente utilizzati per raggruppare i dipendenti che:

- hanno lo stesso supervisore;
- lavorano da remoto;
- sono stati assunti di recente e hanno bisogno di un supporto o di una supervisione speciale;
- possono sostituire altri dipendenti in caso di assenze improvvise;
- hanno responsabilità aggiuntive che non sono rilevanti per la pianificazione ma che sono comunque importanti, come, per esempio, gli addetti al primo soccorso.

Se utilizzi injixo Essential, puoi utilizzare i gruppi di selezione per raggruppare i dipendenti in base agli elementi di configurazione, come, per esempio, le unità di pianificazione, le qualifiche e i contratti.

## Creare i gruppi di selezione

1. Vai su _Plan > Configurazione > Gruppi di selezione_{:.breadcrumbs}.
2. Clicca sull’icona Nuovo {% icon item-add | icon-only %} in alto a sinistra.  
    Si aprirà un pannello di configurazione a destra.
3. Compila i campi seguenti:
    - **Nome**: nome unico per il gruppo di selezione (massimo 50 caratteri).
    - **Abbreviazione**: abbreviazione del nome (massimo 25 caratteri).
    - **Descrizione**: descrizione facoltativa che aiuta gli altri utenti a capire che cosa rappresenta il gruppo di selezione.
4. Clicca su _OK_{:.doc-button}.

## Assegnare i dipendenti ai gruppi di selezione

Per assegnare i dipendenti ai gruppi di selezione, è necessario prima {% link_new creare un gruppo di selezione | features/administration/selections.md | #creare-i-gruppi-di-selezione %}.

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Clicca sul dipendente che vuoi assegnare a un gruppo di selezione.  
   Si aprirà un pannello di configurazione a destra.
3. Nella sezione **Gruppi di selezione**, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.
4. Compila i campi seguenti:  
   - **Gruppo di selezione**: clicca sul gruppo di selezione a cui vuoi assegnare il dipendente.
   - (Facoltativo) **Validità dal/fino al**: date che stabiliscono il periodo di validità del gruppo di selezione. Se lasci vuoti questi campi, il gruppo di selezione è sempre valido. Scopri di più sui {% link_new periodi di validità | features/administration/set-a-validity-period.md %}.
5. Clicca su _OK_{:.doc-button}.

Per modificare il gruppo di selezione a cui un dipendente è assegnato, clicca sull’{% icon item-edit %}. Per rimuovere l'assegnazione al gruppo di selezione, clicca sull’{% icon item-delete %}.

## Gestire i dipendenti di un gruppo di selezione

In _Plan > Configurazione > Dipendenti_{:.breadcrumbs}, puoi avere una visione d’insieme dei dipendenti assegnati a un gruppo di selezione e accedere alle loro impostazioni.

Per filtrare i dipendenti in un gruppo di selezione, utilizza i seguenti menu a tendina:

- **Unità pianificativa**: scegli **[Tutte]**.
- **Gruppo di selezione**: scegli un gruppo di selezione.  
   Se il menu a tendina **Gruppo di selezione** non viene visualizzato, clicca sull’icona **Filtro standard** {% icon selection | icon-only %} in alto.

La pagina mostrerà tutti i dipendenti che appartengono al gruppo di selezione. Per accedere alle impostazioni di un dipendente, clicca sulla riga corrispondente.

## Combinare i gruppi di selezione

I clienti injixo Classic, Advanced e Enterprise possono assegnare dei gruppi di selezione a un gruppo di selezione esistente. Il gruppo di selezione a cui vengono assegnati altri gruppi di selezione diventa un gruppo di selezione superiore. I gruppi di selezione assegnati diventano gruppi di selezione inferiori del gruppo di selezione superiore. In questo modo puoi utilizzare un gruppo di selezione superiore per filtrare i dipendenti assegnati a tutti i suoi gruppi di selezione inferiori.

Per creare una gerarchia tra i gruppi di selezione inferiori e un gruppo di selezione superiore, devi prima {% link_new creare i gruppi di selezione superiore e inferiori | features/administration/selections.md | #creare-i-gruppi-di-selezione %}.

Per assegnare un gruppo di selezione a un altro gruppo di selezione, procedi come di seguito:

1. Vai su _Plan > Configurazione > Gruppi di selezione_{:.breadcrumbs}.
2. Clicca sul gruppo di selezione che vuoi utilizzare come gruppo di selezione superiore nell’elenco dei gruppi di selezione.  
   Si aprirà un pannello di configurazione a destra.
3. Nella sezione **Gruppi di selezione**, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.
4. Compila i campi seguenti:  
   - **Gruppi di selezione**: clicca sul gruppo di selezione che vuoi assegnare come gruppo di selezione inferiore.
   - (Facoltativo) **Validità dal/fino al**: date che stabiliscono il periodo in cui i gruppi di selezione inferiori sono assegnati al gruppo di selezione superiore. Se lasci vuoti questi campi, l’assegnazione è sempre valida.
5. Clicca su _OK_{:.doc-button}.

Per modificare un gruppo di selezione inferiore, clicca sull’{% icon item-edit %}. Per rimuoverlo, clicca sull’{% icon item-delete %}.

> Gerarchia dei gruppi di selezione
>
> La gerarchia tra i gruppi di selezione superiori e i gruppi di selezione inferiori non è visibile in _Plan > Configurazione > Dipendenti_{:.breadcrumbs}. Per controllare se un gruppo di selezione è un gruppo di selezione superiore, vai su _Plan > Configurazione > Gruppi di selezione_{:.breadcrumbs} e clicca su un gruppo di selezione nella sezione **Gruppi di selezione**. In alternativa, assegna ai gruppi di selezione superiori dei nomi che rendano visibile la gerarchia dei gruppi di selezione.

## Eliminare un gruppo di selezione

1. Vai su _Plan > Configurazione > Gruppi di selezione_{:.breadcrumbs}.
2. Nell’elenco, clicca sul gruppo di selezione che vuoi eliminare.
3. Clicca sull’{% icon item-delete %} in alto a sinistra.
4. Per confermare, clicca su _Sì_{:.doc-button}.
