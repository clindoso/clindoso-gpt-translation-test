---
title: Añadir una integración de Zendesk
description: Conecta tu ACD de Zendesk a injixo y utiliza los datos importados en injixo Forecast.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-five9-integration.md
---

La integración de Zendesk importa volúmenes de contacto vía correo electrónico, formularios en línea, chats, llamadas y mensajería social de Zendesk Support y Zendesk Talk. La integración solo importa llamadas entrantes, no salientes. El tiempo medio de operación (TMO) solo está disponible para Zendesk Talk.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Zendesk

En tu cuenta de Zendesk, crea un token de API para un usuario con [Permisos administrativos](https://support.zendesk.com/hc/es/articles/4408843355290-Integraci%C3%B3n-de-Zendesk-para-Salesforce-Permisos-de-perfil-necesarios).

Para añadir una nueva integración de Zendesk en injixo, sigue los pasos a continuación:

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Zendesk**, haz clic en _Añadir integración_{:.doc-button}.
4. Introduce un nombre inequívoco para la nueva integración que refleje el origen de los datos.
5. En la sección **Credenciales de usuario**, introduce tus credenciales de Zendesk:
   * Introduce el nombre completo de tu dominio de Zendesk, subdominio incluido, p.&nbsp;ej., ejemplo.zendesk.com.
   * Introduce tu nombre de usuario de Zendesk.
   * Introduce tu token del API.
6. En la sección **Configuración**, selecciona un método de agrupamiento. Selecciona IVR (Interactive Voice Response) o número de teléfono. El método que selecciones determina cómo injixo [nombra las colas de origen resultantes](#nombres-de-las-colas-de-zendesk-talk) para las vistas de Zendesk Talk. La opción IVR usa el grupo de destino, la opción Número de teléfono usa el número del receptor para generar el nombre de la cola de origen. Una llamada sin la información relevante aparecerá sin agrupar. Esto no afecta a las colas de origen para Zendesk Support.

   > No puedes modificar el método de agrupamiento una vez hayas guardado la configuración de la integración en injixo.

7. Haz clic en _Guardar integración_{:.doc-button}.

## Datos de Zendesk en injixo

### Tickets e interacciones

Por norma general, un ticket de Zendesk incluye diversas interacciones a través de distintos canales de comunicación entre miembros de tu equipo y tus clientes.

Cada interacción representa una tarea que los miembros de tu equipo deben llevar a cabo. Una interacción puede ser un ticket nuevo o un cambio en un ticket ya existente.

Por ejemplo, un usuario crea un ticket mandando un correo electrónico. Un miembro del equipo responde y cierra el ticket. Dos días después, el usuario envía otro correo en respuesta al correo de tu equipo, lo que vuelve a abrir el ticket. En injixo, esto se contaría como dos correos, aunque ocurran en el marco de un solo ticket.

### Vistas

injixo se basa en tus vistas de Zendesk para crear colas de origen. Tras la importación inicial de datos, verás una cola de origen para cada vista que hayas creado en Zendesk. Si una vista incluye eventos de distintos canales (p.&nbsp;ej., chat y correo electrónico), estos aparecerán en distintos canales en injixo.

Atención: añadir vistas de Zendesk nuevas después de haber guardado la integración generará automáticamente nuevas colas y sus historias correspondientes en injixo.

### Vistas no compatibles

injixo puede crear colas de origen para la mayoría de las vistas, pero actualmente no es compatible con las vistas que usan los siguientes campos de ticket:

- Horarios comerciales
- SLA
- Canal
- Cualificaciones
- Condiciones con valores específicos del cliente (p.&nbsp;ej., asignado a (usuario actual))

Si tienes vistas de Zendesk con condiciones que se refieran a al menos uno de los campos mencionados, injixo ignorará las vistas y no creará colas relacionadas.

### Asignación de canales de Zendesk en injixo

Todo cambio a un evento en un ticket de Zendesk puede ser contabilizado en varios canales en injixo.

Por ejemplo, un correo electrónico crea un ticket que aparecerá en la cola de correo electrónico en injixo. Si ese mismo ticket entra en una vista de chat, también será contabilizado en la cola de chat en injixo.

| Canal de Zendesk                           | injixo       |
| ----------------------------------------- | ------------ |
| email                                     | email        |
| mobile                                    | email        |
| web                                       | email        |
| chat                                      | chat         |
| native_messaging                          | chat         |
| sms                                       | social_media |
| any_channel                               | social_media |
| facebook                                  | social_media |
| twitter                                   | social_media |
| sunshine_conversations_facebook_messenger | social_media |
| instagram_dm                              | social_media |
| voice                                     | call         |
| api                                       | case         |
| answer_bot_for_web_widget                 | case         |
| chat_transcript                           | case         |
| mobile_sdk                                | case         |

### Nombres de las colas de Zendesk Support

Los nombres de las colas de origen de Zendesk Support siguen la siguiente convención:

"nombre de la vista + (canal en injixo)"

Ejemplos:

- Tickets de asistencia (chat)

### Nombres de las colas de Zendesk Talk

Los nombres de las colas de origen de Zendesk Talk siguen la siguiente convención:

"Calls Inbound For + método de agrupamiento"

Ejemplos:

- Calls Inbound For +49123456789 (número de teléfono)
- Calls Inbound For Senior Agents (IVR)
- Calls Inbound Ungrouped
