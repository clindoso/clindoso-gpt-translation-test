---
title: Añadir una integración de Genesys Engage
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprenda cómo conectar tu CMS de Genesys Engage a injixo para importar datos.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Una integración de Genesys Engage es una integración on-premise que importa historiales de llamadas y datos sobre los estados de los agentes.

Esta integración usa {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Genesys Engage

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Genesys**, haz clic en _Seleccionar modelo_{:.doc-button}.
4. En la sección **Genesys Engage**, haz clic en _Añadir integración_{:.doc-button}.

## Configurar tu integración de Genesys Engage

1. Introduce un nombre inequívoco para la integración que identifique el origen de los datos.
2. Instala y conecta {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. En la sección **Credenciales de la base de datos**, configura tu integración:
 - Selecciona tu adaptador de base de datos.
 - Introduce el host y el puerto de tu base de datos.
 - Introduce el nombre de usuario y la contraseña de tu base de datos.
 - Introduce el nombre de la base de datos ETL.
 - Introduce el nombre de la base de datos de configuración.
4. Si quieres importar datos de los estados de los agentes, marca la casilla **Importar datos sobre el estado del agente** en la sección **Configuración**.<br>
Ten en cuenta que si quieres importar datos de los estados de los agentes, primero tienes que {% link_new asignar los identificadores de usuarios y estados externos | features/acd-integration/cloud/import-agent-status-data.md | #asignar-identificadores-de-usuarios-externos-a-los-empleados-en-injixo %}.
5. Haz clic en _Guardar integración_{:.doc-button}.

La integración empezará a importar datos a injixo. 

## Editar una integración de Genesys Engage

Si cualquier detalle de la integración cambia, como las credenciales para el servidor de la base de datos, puedes editar y actualizar la configuración de tu integración. La importación de datos continuará con la configuración actualizada.
