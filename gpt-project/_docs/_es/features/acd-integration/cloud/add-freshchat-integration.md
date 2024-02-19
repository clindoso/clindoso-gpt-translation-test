---
title: Añadir una integración de Freshchat
description: Aprende cómo conectar tu CRM de Freshchat a injixo para importar datos.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
redirect_from:
  - /es/add-freshdesk-messaging-integration/
redirect_reason: Updated filename on 15 September 2023
---

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Freshchat

Para añadir una integración de Freshchat en injixo, necesitas una cuenta de Freshchat Pro o Enterprise.

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Freshworks**, haz clic en _Selecciona el modelo_{:.doc-button}.
4. En la sección **Freshchat**, haz clic en _Añadir integración_{:.doc-button}.

## Configurar tu integración de Freshchat

1. Introduce un nombre inequívoco para la integración que identifique el origen de los datos.
2. En la sección **Credenciales**, introduce el nombre completo de tu dominio de Freshchat, incluido el subdominio, p.&nbsp;ej., ejemplo.freshchat.com.
3. Ve a Freshchat y copia una clave de API válida de un usuario con el rol Account Administrator.
4. Vuelve a injixo y copia la clave de la API en el campo **Clave de la API**.
5. Haz clic en _Guardar integración_{:.doc-button}.

### Instalar la aplicación injixo

La integración de Freshchat requiere una aplicación de cliente. Después de haber guardado tu configuración, puedes acceder a la sección **Instalar la aplicación injixo** en la parte inferior de la página.

Genera y copia la **clave de la API de injixo**.

Para configurar la aplicación de injixo en tu cuenta de Freshchat, sigue las instrucciones en la pantalla. Para más información, consulta [Freshworks marketplace](https://www.freshworks.com/apps/injixo_connect).

## Datos de Freshchat en injixo

### Contactos

Por norma general, los chats de Freshchat contienen múltiples conversaciones entre tus empleados y tus clientes. En injixo, cada chat resuelto se cuenta como un contacto, independientemente del número de conversaciones.

Pongamos el siguiente ejemplo:

Un cliente abre un chat en la página web. Una persona de tu equipo responde, pero no resuelve el problema hasta el día siguiente, porque necesita recolectar más información. Esto contaría como un contacto en injixo.

### Convenciones para los nombres de las colas de origen

Las colas de origen que injixo crea derivadas de tus chats siguen esta convención:

"group name"

Examples:

- Customer Support
- Undefined_Queue

### Chats eliminades y de spam

Un chat puede ser eliminado o marcado como spam cuando es actualizado. En este caso, la integración no puede determinar el nombre del grupo. Las colas de origen que cuentan estos chats se llaman Undefined_Queue. Por lo general, estas colas no son relevantes para planificar la carga de trabajo de tus empleados.

## Preguntas frecuentes

| Pregunta                                                                                                                                                                       | Respuesta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| De repente, injixo deja de mostrar datos nuevos de Freshchat, pero en la página **Account > Integraciones** mi integración de Freshchat tiene el estado Operativo. ¿Qué puedo hacer? | La aplicación de injixo obtiene datos de Freshchat y envía eventos a injixo. En caso de errores de comunicación entre la aplicación injixo e injixo, es posible que no se muestren los datos de Freshchat. La integración de Freshchat no puede detectar estos errores de comunicación.<br><br>Verifica que la clave de la API de injixo que introdujiste al configurar la aplicación de injixo en tu cuenta de Freshchat siga siendo válida. Si la clave de la API ya no es válida, actualiza la clave de la API de injixo en la página de instalación de la aplicación injixo. Si la clave de API sigue siendo válida, ponte en contacto con la asistencia técnica de injixo. |
