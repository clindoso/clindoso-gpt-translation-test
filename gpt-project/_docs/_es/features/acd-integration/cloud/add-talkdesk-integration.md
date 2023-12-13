---
title: Añadir una integración de Talkdesk
description: Aprende cómo conectar tu ACD de Talkdesk a injixo para importar datos.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Una integración de Talkdesk es una integración cloud que importa datos históricos de llamadas y datos de los estados de los agentes.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Talkdesk

1. Ve a _Account > Integraciones_{:.breadcrumbs}.  
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Vonage**, haz clic en _Añadir integración_{:.doc-button}.
4. Introduce un nombre inequívoco para la nueva integración que identifique el origen de los datos.
5. En la sección **Credenciales de usuario**, completa el formulario con información específica de Talkdesk:

   - Introduce el nombre de tu cuenta de Talkdesk.
   - Ingrese el ID de cliente y la clave secreta de un cliente OAuth de Talkdesk.

     > Para el ID de cliente y la clave secreta de cliente, [crea un nuevo cliente OAuth](https://docs.talkdesk.com/docs/creating-a-new-oauth-client) en Talkdesk.
     >
     > También puedes usar un cliente OAuth que ya exista, siempre que tenga la siguiente configuración:
     >
     > - Tipo de autorización: client-credentials
     > - Ámbitos: data-reports:read y data-reports:write

6. En la sección **Configuración**, selecciona tu región de acceso.

7. Haz clic en _Guardar integración_{:.doc-button}.  
   La integración verificará la conexión y reportará si surje algún problema.  
   Una vez la verificación tenga éxito, la integración comenzará a importar datos a injixo.

<!-- ## Talkdesk Data in injixo -->

## ¿Y ahora?

Una vez los datos de llamadas hayan sido importados a las colas, podrás crear tu primera carga de trabajo. Para aprender más sobre cómo configurar los datos de los estados de los agentes, consulta los artículos relacionados.
