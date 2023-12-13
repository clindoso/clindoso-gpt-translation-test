---
title: Configuración del navegador
description: Aprende cómo configurar tu navegador para trabajar con injixo.
product_label:
  - on-premise
  - classic
related_articles:
  - overwrite_title: Errores de instalación del cliente
    filepath: support/faq/client-installer-errors.md
  - overwrite_title: Mensaje «Se ha superado el tiempo de espera de tu sesión»
    filepath: support/faq/session-timeout-message.md
redirect_from:
  - /es/setup-guide/
redirect_reason: Nombre de archivo actualizado el 27 de julio de 2023
---

En este artículo aprenderás cómo configurar tu navegador para injixo.

Para trabajar con funciones basadas en ActiveX en WFM, usa {% link_new Microsoft Edge en modo Internet Explorer (IE) | support/faq/configure-edge-internet-explorer-mode.md %}. Puedes encontrar una lista de navegadores compatibles en {% link_new Requisitos del sistema | getting-started/system-requirements.md | #requisitos-de-navegador %}.

Si no tienes los permisos necesarios para modificar los ajustes de tu navegador o para instalar software, ponte en contacto con tu departamento de informática.

## Configurar los sitios de confianza y los ajustes de la zona de seguridad

injixo Classic e injixo Enterprise WFM incluyen controles ActiveX. Tienes que autorizar al navegador (Edge en modo IE) para ejecutar los controles ActiveX.

En los ajustes del navegador, añade todas las páginas injixo (_*.injixo.com_) a los sitios de confianza:

1. Abre el **menú de inicio de Windows**, introduce _opciones de Internet_ y presiona _Enter_.
2. En la pestaña **Seguridad**, selecciona **Sitios de confianza** y haz clic en _Sitios_{:.doc-button}.
3. En el campo **Añadir este sitio web a la zona de:**, introduce https://\*.injixo.com.
4. Marca la casilla **Requerir comprobación del servidor (https:) para todos los sitios de esta zona**.
5. Haz clic en **Agregar**.
6. Haz clic en **Cerrar**.

{{ 1 | image: 'Ajustes de seguridad', '45%', 'jpg' }}

Ajusta el nivel de la zona de seguridad para los sitios de confianza:

1. Abre el **menú de inicio de Windows**, introduce _opciones de Internet_ y presiona _Enter_.
2. En la pestaña **Seguridad**, selecciona **Sitios de confianza**.
3. Desmarca la casilla **Habilitar el modo protegido**.  
   Atención: Esta casilla ya no está disponible en Windows 11 y versiones posteriores.
4. En la pestaña **Seguridad**, ajusta el nivel de seguridad para **Sitios de confianza** a **Medio** o **Medio-Bajo**. Medio-Bajo te permite omitir los pasos 6 al 9.
5. Haz clic en _Aceptar_{:.doc-button}.
6. Haz clic en _Nivel personalizado..._{:.doc-button}.
7. En la ventana **Ajustes de seguridad**, modifica los siguientes ajustes:

   | Ajuste                                           | Estado             |
   | ------------------------------------------------- | ----------------- |
   | Generar scripts de los controles ActiveX marcados como seguros para scripts | Habilitar           |
   | Ejecutar controles y complementos de ActiveX                  | Habilitar           |
   | Descargar los controles ActiveX firmados                  | Preguntar o habilitar |
   | Pedir intervención del usuario automática para controles ActiveX          | Habilitar           |

8. Haz clic en _Aceptar_{:.doc-button}.
   Verás el siguiente mensaje: _¿Está seguro de que desea cambiar la configuración de esta zona?_
9. Haz clic en _Sí_{:.doc-button}.
10. Haz clic en _Aceptar_{:.doc-button}para cerrar la ventana de diálogo.

## Instalar el cliente injixo

injixo Classic e injixo Enterprise WFM incluyen controles ActiveX, que requieren {% link_new Microsoft Edge en modo IE | support/faq/configure-edge-internet-explorer-mode.md %} y el cliente injixo.

Si ves un mensaje de error al iniciar sesión o dentro de injixo:

- utiliza un {% link_new navegador compatible | getting-started/system-requirements.md | #requisitos-de-navegador %}.
- instala el cliente de injixo (sigue las instrucciones en la siguiente sección).

### Instalación automática del cliente (página de inicio de WFM)

Si estás utilizando la configuración del navegador mencionada anteriormente, el cliente se instalará automáticamente cuando accedas a WFM.

1. Ve a _WFM_{:.menu-item}.
2. Espera a que termine la descarga y comience la instalación del cliente.
3. El navegador mostrará el mensaje _Esta página web quiere ejecutar el siguiente complemento: 'injixo Enterprise' de 'InVision AG'_. Si el mensaje no aparece, pide ayuda al departamento de informática de tu empresa.
4. Haz clic en _Instalar_{:.doc-button} para instalar el complemento requerido.
5. Haz clic en _Instalar_{:.doc-button} para instalar el cliente.

Cuando se haya completado la instalación, podrás acceder a los componentes ActiveX.

### Instalación manual del cliente

Instala el cliente manualmente para injixo WFM Enterprise on-premise o si la instalación automática ha fallado.

Ten en cuenta que si utilizas una herramienta de distribución de software, deberás ejecutar el instalador para el usuario que usará el equipo en el futuro, p.&nbsp;ej., usando el archivo de Microsoft _msiexec.exe_ con la opción _runas /user_.

1. Descarga la versión más reciente del [cliente injixo](https://downloads.injixo.com/en#client-components).
2. Para ejecutar el instalador MSI, haz clic en _Ejecutar_{:.doc-button}.
3. Para continuar, haz clic en _Siguiente_{:.doc-button}.
4. (Opcional) Edita la ruta de instalación.
5. Si distintos usuarios comparten el ordenador, selecciona **Todos**.
6. Para continuar, haz clic en _Siguiente_{:.doc-button}.
7. Para comenzar la instalación, haz clic en _Instalar_{:.doc-button}.
   Verás el siguiente mensaje: _¿Quieres permitir que esta aplicación de un editor desconocido haga cambios en el PC?_
8. Haz clic en _Sí_{:.doc-button} para confirmar el mensaje.

Cuando se haya completado la instalación, podrás acceder a los componentes ActiveX.
