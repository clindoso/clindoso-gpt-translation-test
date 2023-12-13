---
title: Añadir una integración de Sikom
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprende cómo conectar tu CRM de Sikom a injixo para importar datos.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Una integración de Sikom es una integración on-premise que importa historiales de llamadas, datos de los estados de los agentes y datos de adherencia en tiempo real.

La integración usa {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Sikom

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Sikom**, haz clic en _Añadir integración_{:.doc-button}.

## Configura tu nueva integración de Sikom

1. Introduce un nombre de la integración inequívoco que identifique el origen de los datos.
2. Instala y conecta {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. En la sección **Credenciales de la base de datos**, configura tu integración:
 - Selecciona la zona horaria de tu base de datos.
 - Introduce el host y el puerto de tu base de datos.
 - Introduce un nombre de usuario y contraseña para tu base de datos.
4. Si quieres importar datos de los estados de los agentes, marca la casilla **Importar datos sobre el estado del agente** en la sección **Configuración**.<br>Ten en cuenta que si quieres importar datos de los estados de los agentes, primero tienes que {% link_new asignar los identificadores de usuarios y estados externos | features/acd-integration/cloud/import-agent-status-data.md %}.
5. Haz clic en _Guardar integración_{:.doc-button}.

La integración empezará a importar datos a injixo. 

## Edita una integración de Sikom

Si cualquier detalle de la integración cambia, como las credenciales para el servidor de la base de datos, puedes editar y actualizar la configuración de tu integración. La importación de datos continuará usando la configuración actualizada.
