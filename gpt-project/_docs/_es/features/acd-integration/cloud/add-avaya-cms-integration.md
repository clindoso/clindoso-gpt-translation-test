---
title: Añadir una integración de Avaya CMS
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Conecta tu base de datos de Avaya con injixo para importar datos.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Una integración de Avaya CMS es una integración on-premise que importa datos de llamadas y datos sobre los estados de los agentes.

La integración usa {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Avaya CMS

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Avaya CMS**, haz clic en _Añadir integración_{:.doc-button}.

## Configurar tu nueva integración de Avaya CMS

1. Introduce un nombre inequívoco para la nueva integración.
   El nombre te ayudará a identificar la fuente de los datos y determinar a qué integración pertenece cada cola.<br>Ejemplo: Integración Avaya - Equipo de Atención al Cliente
1. Instala y conecta {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
1. En la sección **Configuración**, sigue estos pasos:
 - Introduce la [cadena de conexión](#cadena-de-conexión) que define los parámetros necesarios para conectarse a la base de datos de Avaya. 
 - Selecciona la zona horaria de la base de datos en el menú desplegable.
 - Marca la casilla **Importar detalles de los estados de los agentes** para añadir información sobre skills (perfil del agente) y splits (enrutamiento de llamadas) a los estados de los agentes importados.
 - Marca la casilla **Importar datos en tiempo real** si quieres importar datos sobre los estados de los agentes en tiempo real. En este caso, introduce un número de puerto en el campo **Puerto**.<br>
   injixo Cloud Link abrirá un socket TCP de escucha en el puerto especificado. El servicio Avaya Generic RTA se conectará a este puerto y comenzará a transmitir datos sobre los estados de los agentes en tiempo real. El servicio Avaya Generic RTA se licencia y configura en Avaya.
1. Haz clic en _Guardar integración_{:.doc-button} para crear la integración.

La integración empezará a importar datos a injixo. Para importar datos sobre los estados de los agentes, tienes que {% link_new asignar identificadores de usuarios y estados externos | features/acd-integration/cloud/import-agent-status-data.md %} una vez hayas configurado tu integración de Avaya. Si has activado la opción **Importar datos en tiempo real** durante la configuración, pausa tu integración.

## Cadena de conexión

La integración de Avaya CMS necesita la cadena de conexión para conectarse a tu base de datos de Avaya CMS. Debido a que Avaya CMS utiliza por regla general una base de datos IBM Informix, necesitas usar una cadena de conexión especial. 

Ejemplos de cadenas de conexión que usan el controlador ODBC de IBM Informix:<br>
- `DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;` (acceso nativo a través del controlador ODBC)
- `DSN=AvayaCMS;DELIMIDENT=y;` (requiere una conexión ODBC llamada AvayaCMS)
Si tu Avaya CMS no utiliza una base de datos IBM Informix, necesitas obtener la cadena de conexión adecuada para tu tipo específico de base de datos y controlador ODBC. Avaya solo es compatible con conectividad ODBC.

## Editar una integración de Avaya CMS

Si cualquier detalle de la integración cambia, como las credenciales para el servidor de la base de datos, puedes editar y actualizar la configuración de tu integración. La importación de datos continuará usando la configuración actualizada.
