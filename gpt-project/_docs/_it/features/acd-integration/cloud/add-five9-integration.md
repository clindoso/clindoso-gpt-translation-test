---
title: Aggiungere un’integrazione Five9
description: Connetti il tuo sistema ACD Five9 con injixo e prepara un report personalizzato per utilizzare il raggruppamento delle code in base alle qualifiche.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Un'integrazione Five9 è un'integrazione cloud che importa la cronologia delle chiamate, i dati sugli stati degli agenti e sull’aderenza in tempo reale.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Prerequisiti

Se raggruppi le code in base alla campagna, l’integrazione legge il report standard sulle chiamate di Five9.

Se raggruppi le code in base alla qualifica, l’integrazione richiede a Five9 un report personalizzato sulle chiamate che includa le qualifiche. Per importare i dati dalle code raggruppate in base alle qualifiche, segui i passaggi seguenti in Five9:

 1. Crea una nuova cartella condivisa per i report, con il nome ‘Shared Reports (injixo)’.
 2. Personalizza il report sulle chiamate includendo la colonna ‘SKILL’.
 3. Salva il report personalizzato con il nome ‘Call Log with Skills’ nella nuova cartella condivisa.

Per avere informazioni più dettagliate sulle modalità di personalizzazione dei report, consulta l’Help Center di Five9.

## Aggiungere un’integrazione Five9

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro di **Five9** clicca su _Aggiungi integrazione_{:.doc-button}.
4. Inserisci un nome unico per la nuova integrazione che identifichi l’origine dei dati.
5. Inserisci il nome utente e la password di un utente Five9 con i ruoli ADMIN e REPORTING.
6. Nella sezione **Configurazione**, seleziona la regione dell’account e il metodo di raggruppamento.
7. Clicca su _Salva integrazione_{:.doc-button}.

L’integrazione adesso importa dati in injixo. La prima importazione può richiedere fino a 15 minuti. Tutte le code provenienti dal sistema connesso saranno automaticamente disponibili all’assegnazione nella {% link_new schermata di configurazione dei workload | features/forecast/injixo-forecast/create-workloads.md | #creare-un-workload %} in injixo Forecast.

## Che cosa succede in caso di stati degli agenti paralleli?

I rapporti Five9 a volte contengono più stati per un unico agente nello stesso periodo, come, per esempio:

| Stato   | Ora di inizio | Ora di fine |
| ------- | ---------- | -------- |
| Disponibile   | 13:00:00   | 13:00:05 |
| Entrante | 13:00:00   | 13:03:00 |

Per evitare che uno stato sovrascriva l’altro, l’integrazione modifica l’inizio dello stato più lungo. L’inizio dello stato più lungo diventa la fine dello stato più breve:

| Stato   | Ora di inizio | Ora di fine |
| ------- | ---------- | -------- |
| Disponibile   | 13:00:00   | 13:00:05 |
| Entrante | 13:00:05   | 13:03:00 |
