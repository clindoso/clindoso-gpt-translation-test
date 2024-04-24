---
title: Configurare i calendari di pianificazione
description: Configura i calendari di pianificazione per adattare automaticamente gli orari di apertura standard ai giorni con orari di apertura diversi.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/day-types.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Pianificare i giorni festivi
    filepath: best-practices/scheduling-public-holidays.md
redirect_from:
  - /it/planning-calendar/
redirect_reason: Updated filename on 13 March 2024
---

In un calendario pianificativo puoi utilizzare i {% link_new tipi di giorno | features/administration/day-types.md %} per contrassegnare i giorni con orari di apertura o con esigenze di personale diversi dal solito (per esempio i giorni con le campagne di marketing o i giorni festivi). In questo modo puoi far sì che questi giorni siano presi in considerazione automaticamente durante la pianificazione. Se aggiungi un tipo di giorno al calendario pianificativo gli orari di apertura standard per il giorno in questione verranno sovrascritti. È possibile creare diversi calendari pianificativi per le diverse unità di pianificazione o regioni, per esempio se hanno orari di apertura o giorni festivi diversi.

## Configurare un calendario pianificativo

Prerequisito: Hai creato i {% link_new tipi di giorno | features/administration/day-types.md %} personalizzati che vuoi aggiungere al tuo calendario pianificativo.

1. Vai su _Plan > Configurazione > Calendari di pianificazione_{:.breadcrumbs}.
2. Clicca sull’icona Nuovo {% icon item-add | icon-only %} nella barra delle azioni.
3. Configura il calendario pianificativo:
    - **Anno**: specifica l’anno per cui vuoi utilizzare il calendario pianificativo.<br>Per creare un calendario pianificativo che si estende per più di un anno, per esempio se crei pianificazioni che si estendono per più di un anno, utilizza _<_{:.doc-button} e _>_{:.doc-button} per spostarti su un anno passato o futuro. In seguito, configura separatamente il calendario di ogni anno.
    - **Modello di calendario**: scegli il calendario dei festivi dello stato o della regione e clicca su _Applica_{:.doc-button}.<br>Nel calendario pianificativo compaiono automaticamente i giorni festivi dello stato o della regione selezionati.<br>Se in un calendario pianificativo vuoi includere diversi stati o regioni, ripeti questo passaggio per ogni stato o regione che vuoi aggiungere.<br>Nota: ogni cella del calendario pianificativo può contenere soltanto un giorno festivo. Se selezioni un modello che include un giorno festivo nello stesso giorno di un modello che avevi scelto precedentemente, le celle che contengono già un festivo verranno sovrascritte.
    - **Inserimento di un tipo di giorno**: dal menu a tendina seleziona il tipo di giorno personalizzato e clicca su ogni cella del calendario in cui vuoi inserire il tipo di giorno.<br>Nota: puoi assegnare a ogni giorno soltanto un tipo di giorno. Se clicchi su una cella che contiene già un tipo di giorno, il contenuto della cella verrà sovrascritto. Se in un calendario pianificativo vuoi includere diversi tipi di giorno, ripeti questo passaggio per ogni tipo di giorno che vuoi aggiungere.
4. Nella barra delle azioni, clicca sull’icona Salva con nome _![save as button](/assets/img/common/saveas.gif)_{:.doc-button-icon}.
5. Nella finestra che si apre, inserisci il nome del calendario e clicca su _OK_{:.doc-button}.

## Eliminare i tipi di giorno dal calendario pianificativo

Se la tua unità di pianificazione è chiusa in determinati giorni e i dipendenti non ricevono un compenso per le festività in quei giorni, assicurati che quei giorni non siano inclusi nel calendario pianificativo come {% link_new tipi di giorno in modalità festività | features/administration/day-types.md | #modalità-festività %}. Se non elimini quei tipi di giorno dal calendario di pianificazione, injixo ridurrà il totale delle ore lavorative da svolgere per quella settimana, e i dipendenti verranno pianificati per un numero inferiore di ore. Scopri come {% link_new pianificare i giorni festivi | best-practices/scheduling-public-holidays.md | #closed-use-the-planning-calendar %}.

Per eliminare i tipi di giorno dal calendario di pianificazione, procedi come di seguito:
1. Vai su _Plan > Configurazione > Calendari di pianificazione_{:.breadcrumbs}.
2. Per eliminare singoli tipi di giorno, clicca su **Elimina**.
3. Clicca su ogni cella del calendario di pianificazione dalla quale vuoi eliminare il tipo di giorno.
4. (Facoltativo) Per eliminare tutte le voci del calendario per l’anno selezionato, clicca su _Elimina anno_{:.doc-button}.
5. (Facoltativo) Per eliminare tutte le voci del calendario per tutto il periodo, clicca su _Elimina tutto_{:.doc-button}.
5. Clicca sull’icona Salva _![save button](/assets/img/common/save.gif)_{:.doc-button-icon}.

## Modificare un calendario di pianificazione esistente

1. Vai su _Plan > Configurazione > Calendari di pianificazione_{:.breadcrumbs}.
2. Dal menu a tendina **Calendario pianificativo** nella barra delle azioni seleziona il calendario che vuoi modificare.<br>Se vuoi fare una copia del calendario di pianificazione prima di modificarlo, per esempio per utilizzare lo stesso modello e gli stessi tipi di giorno per un anno diverso, clicca sull’icona Salva con nome _![save as button](/assets/img/common/saveas.gif)_{:.doc-button-icon} nella barra delle azioni.
3. Quando hai completato le modifiche, clicca sull’icona Salva _![save button](/assets/img/common/save.gif)_{:.doc-button-icon}.

## Utilizzare un calendario di pianificazione per la pianificazione

Per utilizzare un calendario di pianificazione per la pianificazione, procedi come di seguito:

1. Vai su _Plan > Configurazione > Unità di pianificazione_{:.breadcrumbs}.
2. Seleziona l’unità di pianificazione alla quale vuoi aggiungere il calendario di pianificazione.
2. Nella sezione **Calendari pianificativi**, clicca sull’icona Aggiungi {% icon item-add %}.
3. Nella finestra di configurazione **Calendari pianificativi,** seleziona un calendario pianificativo.<br>Puoi scegliere un calendario che si estende per diversi anni, per esempio se crei una pianificazione che si estende per più di un anno. Se vuoi assegnare un diverso calendario pianificativo per ogni anno, scegli un calendario alla volta e utilizza i campi **Validità dal** e **fino al** per impostare il periodo in cui il calendario deve essere utilizzato. Nota che i calendari pianificativi per un solo anno funzionano soltanto per le pianificazioni di un solo anno.
4. Clicca su _OK_{:.doc-button}.

> Nota
>
> Se l’unità di pianificazione contiene delle unità di pianificazione inferiori, il calendario pianificativo non verrà automaticamente assegnato alle unità di pianificazione inferiori. Se necessario, assegna manualmente il calendario pianificativo a ogni unità di pianificazione inferiore.
