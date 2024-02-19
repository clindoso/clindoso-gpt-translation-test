---
title: Añadir una integración de Freshdesk
description: Conecta tu CRM de Freshdesk a injixo y utiliza los datos importados en injixo Forecast.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

La integración de Freshdesk importa volúmenes de contacto vía correo electrónico, formularios en línea, chats, llamadas y mensajería social.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Freshdesk

Para añadir una integración de Freshdesk en injixo, necesitas una cuenta de Freshdesk Pro o Enterprise.

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Freshworks**, haz clic en _Selecciona el modelo_{:.doc-button}.
4. En la sección **Freshdesk**, haz clic en _Añadir integración_{:.doc-button}.

## Configurar tu integración de Freshdesk

1. Introduce un nombre inequívoco para la integración que identifique el origen de los datos.
2. En la sección **Credenciales**, introduce el nombre completo de tu dominio de Freshdesk, incluido el subdominio, p.&nbsp;ej., ejemplo.freshdesk.com.
3. Ve a Freshdesk y copia una clave de API válida.
4. Vuelve a injixo y copia la clave de la API en el campo **Clave de la API**.
5. Haz clic en _Guardar integración_{:.doc-button}.

## Instalar la aplicación injixo

La integración de Freshdesk requiere una aplicación cliente. Cuando hayas guardado tu configuración, podrás acceder a la sección **Instalar la aplicación injixo**.

Genera y copia la **clave de la API de injixo**.

Para configurar la aplicación de injixo en tu cuenta de Freshdesk, sigue las instrucciones en la pantalla. Para más información, consulta el [Freshworks marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## Datos de Freshdesk en injixo

injixo importa todos los datos de los tickets de Freshdesk. Por norma general, los tickets contienen múltiples conversaciones entre personas de tu equipo y clientes.

### Tickets y conversaciones

En injixo, las conversaciones se agrupan según el canal de comunicación de Freshdesk (Source). Una conversación puede ser un ticket nuevo o una respuesta a un ticket ya existente.

En injixo, las conversaciones en un ticket de Freshdesk se contabilizan por separado como contacto entrante.

Pongamos el siguiente ejemplo:

Un usuario abre un ticket vía correo electrónico. Una persona del equipo responde y cierra el ticket. Dos días después, otro correo reabre el ticket, lo que inicia una conversación nueva.

### Eventos con distintos orígenes

En un ticket de Freshdesk, las respuestas se pueden monitorizar en distintas colas de injixo usando el canal Casos.

Por ejemplo, si recibes una respuesta a un ticket vía correo electrónico, verás el contacto en una cola de injixo correspondiente al grupo de Freshdesk y al nombre de la fuente. Un chat perteneciente al mismo ticket aparecerá en otra cola distinta.

### Convenciones para los nombres de las colas de origen

injixo crea colas de origen para tus tickets. Las convenciones para los nombres de estas colas dependen del estado de la importación de los datos (inicial o continua). Durante la importación inicial, el nombre de las colas de origen seguirá esta convención:

- "nombre del grupo + nombre de la fuente + Tickets"
- "nombre del grupo + nombre de la fuente + Replies"

Ejemplos:

- CustomerService chat Tickets
- CustomerService email Replies
- Unknown group/source Tickets

Un ticket nuevo creará una cola de ticket. Una respuesta a un ticket creará una cola de respuestas que también registrará todas las respuestas siguientes. Para obtener toda la información sobre un ticket, tendrás que consultar tanto la cola de ticket como la cola de respuestas.

#### Tickets eliminados y de spam

No se puede determinar el nombre del grupo y de la fuente cuando se modifica un ticket que previamente ha sido eliminado o marcado como spam. Las colas de origen que contabilizan estos tickets se llamarán "Unknown group/source Tickets" o "Unknown group/source Replies". Por norma general, estas colas no son relevantes para planificar el trabajo de tu equipo.

## Preguntas frecuentes

| Pregunta                                                                                                                                                                       | Respuesta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| De repente, injixo deja de mostrar datos nuevos de Freshdesk, pero en la página **Account > Integraciones** mi integración de Freshdesk tiene el estado Operativo. ¿Qué puedo hacer? | La aplicación de injixo obtiene datos de Freshdesk y envía eventos a injixo. En caso de errores de comunicación entre la aplicación injixo e injixo, es posible que no se muestren los datos de Freshdesk. La integración de Freshdesk no puede detectar estos errores de comunicación.<br><br>Verifica que la clave de la API de injixo que introdujiste al configurar la aplicación de injixo en tu cuenta de Freshdesk siga siendo válida. Si la clave de la API ya no es válida, actualiza la clave de la API de injixo en la página de instalación de la aplicación injixo. Si la clave de API sigue siendo válida, ponte en contacto con la asistencia técnica de injixo. |