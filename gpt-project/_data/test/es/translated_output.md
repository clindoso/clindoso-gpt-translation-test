---
title: Instalar injixo Cloud Link
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Instala el cliente injixo Cloud Link para importar datos a injixo.
related_articles:
  - overwrite_title: Añadir título para la fuente no traducida
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## ¿Qué es injixo Cloud Link?

injixo Cloud Link es un software cliente que debe instalarse cuando configures las integraciones on-premise. injixo Cloud Link importa regularmente los datos a injixo. También puedes instalar injixo Cloud Link si configuras una integración para importar regularmente nuevos archivos CSV desde una carpeta.

El directorio de instalación del cliente contiene:

- el ejecutable injixo-cloud-link;
- uno o más archivos injixo-cloud-link.\*.log;
- el archivo de configuración injixo-cloud-link.toml;
- una carpeta licenses con las licencias de las bibliotecas de código abierto.

## Requisitos previos

- Windows: injixo Cloud Link solo es compatible con Windows 10 y versiones posteriores. <!-- what about Linux -->
- Linux: tienes que instalar el paquete unixODBC.
  
- Cortafuegos/Proxy: el puerto 443 para tráfico saliente debe estar abierto. injixo Cloud Link utiliza TLS-Encryption con TCP sobre el puerto 443.
En las integraciones on-premise, el acceso a una conexión local es necesario para extraer datos, p. ej., de un ACD o CRM. Dependiendo del tipo de base de datos, es necesario instalar el driver para acceder a la base de datos.

## Instalar injixo Cloud Link

Cuando añadas una {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %}, {% link_new integración DVB | features/acd-integration/cloud/add-csv-integration.md %}, o {% link_new integración de bases de datos | features/acd-integration/cloud/add-database-integration.md %}, en la sección **injixo Cloud Link** encontrarás enlaces para descargar el archivo de instalación (para Windows) o el archivo comprimido (para Linux).

### Instalación del servicio de Windows

Usa el instalador de la aplicación cliente en Windows para instalar el primer servicio en tu sistema:

1. Haz clic en **Descargar para Windows 64-bit** y ejecuta el asistente de instalación.
2. Haz clic en **Siguiente**.
3. (Opcional) Cambia el directorio de instalación.
4. Haz clic en **Siguiente**, luego en **Instalar**.  
   Una consola muestra un PIN válido durante 5 minutos.  
   Sigue las instrucciones en la consola para [conectar Cloud Link a tu integración](#connect-cloud-link-to-your-integration).
5. Haz clic en **Finalizar** en el asistente.  
   El instalador crea el servicio de Windows **injixo Cloud Link**.

### <a name="install-multiple-cloud-link-services-windows">Instalar varios servicios de Windows

Puedes instalar un máximo de ocho servicios adicionales para integraciones independientes. Instálalas en directorios diferentes para evitar que sobrescriban otras instancias.

Para instalar un segundo servicio de Cloud Link en Windows, añade una nueva integración y sigue estos pasos:

1. Haz clic en **Descargar para Windows 64-bit**.
2. Abre una línea de comandos de Windows (cmd).
3. Ejecuta el siguiente comando:

   ```
   msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS=":instance.1"
   ```

   > Aumenta la ID de la instancia en el parámetro TRANSFORMS cuando instales más instancias.
   >
   > Por ejemplo: la tercera instancia requiere `":instance.2"`, la cuarta instancia `":instance.3"`, y así a continuación.

  
4. Sigue las instrucciones del asistente de instalación.  
   El instalador te sugerirá un directorio de instalación nuevo, que incluye una referencia a la instancia, p. ej., (Instancia 1).  
   Sugerencia: para identificar a qué integración pertenece una instancia, puedes añadir la identificación de ACD y el tipo, p. ej., (ACD - importación de agentes) al directorio de instalación propuesto por defecto.  
   Verás el nuevo directorio y un nuevo servicio de Windows injixo Cloud Link etiquetado con el identificador (Instancia {id}).

### Instalación del servicio de Linux

Instala el primer servicio conforme al proncipio:

1. Haz clic en **Descargar para Linux 64-bit** y descomprime el archivo en tu directorio de instalación preferido.
2. Abre una terminal.
3. Instala el servicio injixo Cloud Link:  
   `sudo ./injixo-cloud-link service install`
4. Inicia el servicio instalado:  
   `sudo ./injixo-cloud-link service start`
5. Mostrar un PIN con el comando:  
   `sudo ./injixo-cloud-link pin`  
   Una consola muestra un PIN válido durante 5 minutos.  
   Sigue las instrucciones en la consola para [conectar Cloud Link a tu integración](#connect-cloud-link-to-your-integration).

### <a name="install-multiple-cloud-link-services-linux">Instalar varios servicios en Linux

Puedes instalar varios servicios para distintas integraciones. Instálalas en directorios distintos para evitar que sobrescriban otras instancias.

Para instalar más servicios en Linux, añade una integración nueva y sigue estos pasos:

1. Crea un nuevo directorio y copia en él los archivos del directorio original de instalación.
2. Abre el archivo injixo-cloud-link.toml.
3. Cambia la ID en el valor **name** en la sección **[app]** por una ID nuevo:

   ```
   [app]
   name = "com.injixo.cloud-link.instance.1"
   ```

4. Instala e inicia un nuevo servicio conforme al proceso descrito arriba.

## Connect Cloud Link to your integration

La instalación de Cloud Link muestra el siguiente mensaje que incluye el PIN:

```
** Before you are able to run the client,
** link it to your injixo account:
**  1) Log in to injixo.com
**  2) Visit https://www.injixo.com/account/integrations
**  3) Select an integration you want to connect the client to
**  4) Enter your pin: 424242 (expires in 5 minutes)
```

1. Vuelve a la página **Add a new integration** en tu navegador.
2. En la sección **injixo Cloud Link**, introduce tu PIN en el campo de seis dígitos **PIN shown during installation**.
3. Haz clic en _Connect_{:.doc-button}.
   Cloud Link se conecta a injixo. Puedes continuar el proceso de configuración de tu {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o {% link_new integración DVB | features/acd-integration/cloud/add-csv-integration.md %}.

## Connect through a proxy server

To connect through a proxy server, add the proxy hostname or IP address to the **https_proxy** environment variable:

- Windows: Add the environment variable to the **System variables** section. If services do not run with the LocalSystem account, configure a user variable.
- Linux: Set the environment variable in /etc/environment or in /etc/profile.d

Por ejemplo: `https_proxy=http://your.proxy.example`

Si es necesario, puedes añadir el número de puerto (si no es el puerto 80) y las credenciales de usuario para autenticarte:

Por ejemplo: `https_proxy=http://username:password@your.proxy.example:8080`

## Share injixo destination IP addresses <!-- rethink the name -->

To allow injixo Cloud Link to connect to the injixo cloud servers, share the following URLs:

- injixo-\*.s3-eu-west-1.amazonaws.com
- www.injixo.com

No puedes compartir un solo dirección IP. Los procesos de implementación y actualización periódicamente cambian las direcciones IP de los servidores. Considera instalar injixo Cloud Link en la DMZ. Si la conexión al servidor falla, se muestran errores con respecto a [Windows sockets](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2) en el archivo de registro.

## Registro

injixo Cloud Link gira los archivos de registro a diario y después de un reinicio, pero no los elimina. Los registros actuales se encuentran en el archivo injixo-cloud-link.log. Los registros rotados incluyen la fecha de rotación en el nombre del archivo. Tienes que configurar tu propio script de borrado recurrente, u borrar los archivos manualmente.

### Activar el registro detallado

Para integraciones de base de datos, injixo Cloud Link ofrece uno modo de **registro detallado**. Cuando está activado, el archivo de registro muestra el total de filas extraídas y las primeras diez filas de datos de cada petición.

Puedes activar el registro detallado de la siguiente manera:

1. Detén injixo Cloud Link.
2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.
3. En la sección **[app]**, establece **verbose** a true:

   ```
   [app]
   verbose = true
   ```

4. Guarda el archivo y reinicia injixo Cloud Link.

### Configurar la carpeta de importación

Por defecto, injixo Cloud Link sube archivos que se guarden en su directorio de instalación. Para las integraciones  de CSV, puedes configurar una carpeta de exportación personalizada de la siguiente manera:

1. Detén injixo Cloud Link.
2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.
3. En la sección **[app]**, configura el atributo **importDirectory** con tu carpeta de importación.
   - Puedes usar rutas absolutas o relativas.
   - Escapa las barras invertidas con dobles barras invertidas.
4. Guarda el archivo y reinicia injixo Cloud Link.

## Preguntas frecuentes

<style>
table th:first-of-type {
    width: 25%;
}
table th:nth-of-type(2) {
    width: 75%;
}
</style>

| Pregunta                                                                        | Respuesta                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ¿Cómo puedo generar un nuevo PIN si el viejo ya no es válido?                              | Reinicia injixo Cloud Link e introduce el nuevo PIN del archivo de registro en el campo de seis dígitos en la sección **injixo Cloud Link** en la página de configuración.                                                                                                                                                                                                                                                      |
| ¿Cómo puedo desinstalar injixo Cloud Link de mi sistema?                                      | 1. Desinstala injixo Cloud Link ejecutando el instalador de nuevo o yendo a _Programas > Programas y características_{:.breadcrumbs} en Windows.<br>2. Haz clic en la entrada **injixo Cloud Link** en la lista con el botón derecho y selecciona **Desinstalar** o **Desinstalar/cambiar**.<br>3. Sigue las instrucciones en pantalla.<br><br>Para desinstalar instalaciones adicionales, ve a _Programs > Programs and Features_{:.breadcrumbs} en Windows y sigue los pasos 2 y 3. |
| ¿Cómo puedo mover injixo Cloud Link a un nuevo servidor?                                | 1. Haz clic en {% icon pencil %} a la derecha de una integración para editarla.<br>2. Haz clic en **Conectar una nueva instalación de injixo Cloud Link**.<br>3. Si es necesario, vuelve a descargar injixo Cloud Link e instala el software en el nuevo servidor.                                                                                                                                                                          |
| ¿Cómo puedo cambiar la integración para una instalación existente de injixo Cloud Link? | 1. Ve al directorio de instalación y copia el PIN del archivo de registro.<br>2. Elimina la integración existente y crea una nueva integración.<br>3. Conecta injixo Cloud Link al nuevo servicio en la configuración de la nueva integración. Para ello, introduce el PIN del proceso de configuración de la nueva integración.                                                                                                               |
