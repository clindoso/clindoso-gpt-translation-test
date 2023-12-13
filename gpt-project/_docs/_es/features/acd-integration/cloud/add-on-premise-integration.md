---
title: Añadir una integración on-premise
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Conecta tu base de datos on-premise a injixo para importar el volumen de contactos, TMO y datos de los estados de los agentes.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Instalar injixo Cloud Link
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Importar datos sobre los estados de los agentes
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Qué es una integración on-premise

Las integraciones on-premise usan {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} para conectarse a un sistema en tu red local. Una vez conectadas, las integraciones on-premise intentarán importar hasta tres años de datos históricos.

## Añadir una integración on-premise

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Selecciona tu sistema externo y haz clic en _Añadir integración_{:.doc-button}. Si existen distintos modelos de tu sistema externo, haz clic en _Selecciona el modelo_{:.doc-button} y después en _Añadir integración_{:.doc-button} en el modelo relevante.
3. Rellena el formulario con la información requerida. Para poder identificar la fuente de los datos más adelante, introduce un nombre inequívoco para la integración.
4. Instala el {% link_new cliente de injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
5. Haz clic en _Guardar integración_{:.doc-button}.

 La primera importación de datos puede tardar cierto tiempo. Todas las colas del sistema conectado aparecen automáticamente como disponibles para ser asignadas en la {% link_new página de configuración de cargas de trabajo | features/forecast/injixo-forecast/manage-workloads.md | #crear-cargas-de-trabajo %} en injixo Forecast.

Si tu integración soporta la importación de datos de los estados de los agentes, primero tienes que {% link_new asignar los identificadores de usuarios externos y las actividades externas | features/acd-integration/cloud/import-agent-status-data.md %} para poder importar datos de los estados de los agentes.
