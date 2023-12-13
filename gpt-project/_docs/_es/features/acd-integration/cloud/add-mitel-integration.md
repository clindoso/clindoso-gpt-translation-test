---
title: Añadir una integración de Mitel
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprende cómo conectar tu CRM de Mitel a injixo para importar datos.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Una integración de Mitel es una integración on-premise que importa historiales de llamadas, correos electrónicos, chats y redes sociales, así como datos sobre los estados de los agente.

La integración usa {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Mitel

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Mitel**, haz clic en _Añadir integración_{:.doc-button}.

## Configura tu integración de Mitel

1. Introduce un nombre inequívoco para la integración que identifique el origen de los datos.
2. Instala y conecta {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. En la sección **Configuraciones regionales**, selecciona tu **zona horaria del ACD**.
4. En la sección **Credenciales de la base de datos**, configura tu integración:
 - Introduce el host y el puerto de tu base de datos.
 - Introduce tu nombre de usuario y contraseña para tu base de datos.
5. Si quieres importar datos sobre los estados de los agentes, marca la casilla **Importar estados de los agentes** en la sección **Configuración**.<br>Ten en cuenta que si quieres importar datos de los estados de los agentes, primero tienes que {% link_new asignar los identificadores de usuarios y estados externos | features/acd-integration/cloud/import-agent-status-data.md %}.
6. Haz clic en _Guardar integración_{:.doc-button}.

La integración empezará a importar datos a injixo. 

## Editar una integración de Mitel

Si cualquier detalle de la integración cambia, como las credenciales para el servidor de la base de datos, puedes editar y actualizar la configuración de tu integración. La importación de datos continuará con la configuración actualizada.
