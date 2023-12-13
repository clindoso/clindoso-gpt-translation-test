---
title: Instalar injixo Cloud Link
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Instala el cliente de injixo Cloud Link para importar datos a injixo.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Qué es injixo Cloud Link

injixo Cloud Link es un cliente de software que necesitas instalar para configurar una integración on-premise. injixo Cloud Link importa datos a injixo con regularidad. También puedes instalar injixo Cloud Link cuando configures integraciones de CSV para importar regularmente nuevos archivos CSV de una carpeta.

El directorio de instalación del cliente contiene:

- el archivo ejecutable injixo-cloud-link;
- uno o varios archivos injixo-cloud-link.*.log;
- el archivo de configuración injixo-cloud-link.toml;
- una carpeta de licencias con licencias para bibliotecas de código abierto (open source).

## Prerrequisitos

- Windows: injixo Cloud Link es compatible con Windows 10 y superior, y con Windows Server 2016 y superior. <!-- what about Linux -->
- Linux: el paquete unixODBC tiene que estar instalado.
- Cortafuegos/proxy: el puerto 443 tiene que estar abierto para tráfico saliente. injixo Cloud Link usa encriptación TLS con TCP a través del puerto 443.

Ten en cuenta que las integraciones on-premise acceden a un sistema local, como un ACD o CRM, para extraer datos. Según el tipo de base de datos, tendrás que instalar un controlador de base de datos.

## Instalar injixo Cloud Link

Cuando añades una {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %}, una {% link_new integración de archivos CSV | features/acd-integration/cloud/add-csv-integration.md %}, o una {% link_new integración de base de datos | features/acd-integration/cloud/add-database-integration.md %}, en la sección **injixo Cloud Link** encontrarás enlaces para descargar el instalador del cliente (para Windows) o los archivos del cliente (para Linux).

### Instalación del servicio de Windows

Instala el primer servicio con el instalador del cliente de Windows:

1. Haz clic en **Descargar para Windows 64-bit** y ejecuta el archivo.
2. Haz clic en **Next**.
3. (Opcional) Modifica el directorio de instalación.
4. Haz clic en **Next** y después en **Install**.  
   Una ventana de la consola te muestra un PIN que es válido durante cinco minutos.  
   Para [conectar injixo Cloud Link a tu integración](#conectar-injixo-cloud-link-a-tu-integración), sigue las instrucciones de la consola.
5. Haz clic en **Finish** en el instalador.  
   El instalador crea el servicio de Windows **injixo Cloud Link**.

### <a name="install-multiple-cloud-link-services-windows">Instalar múltiples servicios de Windows

Puedes instalar un máximo de ocho servicios adicionales para cada integración. Para evitar sobrescribir las instancias de servicio anteriores, instálalas en directorios separados.

Para instalar un segundo servicio de Cloud Link en Windows, añade una nueva integración y sigue los siguientes pasos:

1. Haz clic en **Descargar para Windows 64-bit**.
2. Abre la línea de comandos de Windows (cmd).
3. Para la segunda instancia, ejecuta el siguiente comando:

   ```
   msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS=":instance.1"
   ```

   > Aumenta la instancia ID en el parámetro TRANSFORMS cuando instales más instancias.
   >
   > Por ejemplo, la tercera instancia requiere `":instance.2"`, la cuarta instancia `":instance.3"`, y así sucesivamente.

  
4. Sigue las instrucciones en el procedimiento de instalación.  
   El instalador sugerirá un nuevo directorio de instalación predeterminado que incluye la instancia, p.&nbsp;ej. (Instancia 1).  
    Para identificar a qué integración pertenece la instalación, añade detalles de ACD y del tipo de importación, p.&nbsp;ej. (ACD - agent import) al directorio de instalación predeterminado.  
   Cuando se complete la instalación, verás un servicio de Windows nuevo con el nombre injixo Cloud Link (Instance {id}).

### Instalación del servicio de Linux

Instala el primer servicio basado en el siguiente ejemplo:

1. Haz clic en **Descargar para Linux 64-bit** y extrae el archivo al directorio de instalación que prefieras.
2. Abre un terminal.
3. Instala el servicio injixo Cloud Link:  
   `sudo ./injixo-cloud-link service install`
4. Lanza el servicio instalado:  
   `sudo ./injixo-cloud-link service start`
5. Muestra un PIN usando el comando:  
   `sudo ./injixo-cloud-link pin`  
   Una ventana de la consola te muestra un PIN que es válido durante cinco minutos.  
   Para [conectar injixo Cloud Link a tu integración](#conectar-injixo-cloud-link-a-tu-integración), sigue las instrucciones de la consola.

### <a name="install-multiple-cloud-link-services-linux">Instalar múltiples servicios de Linux

Puedes instalar múltiples servicios para gestionar distintas integraciones. Para evitar sobrescribir servicios instalados previamente, usa directorios separados.

Para instalar más servicios en Linux, añade una nueva integración y sigaue los siguientes pasos:

1. Crea un nuevo directorio y copia los archivos del directorio de instalación original.
2. Abre el archivo injixo-cloud-link.toml.
3. Modifica el valor de **name** en la sección **[app]** con un nuevo ID:

   ```
   [app]
name = "com.injixo.cloud-link.instance.1"
   ```

4. Instala e inicia el nuevo servicio desde el nuevo directorio, como se ha descrito anteriormente.

## Conectar injixo Cloud Link a tu integración

La instalación de injixo Cloud Link muestra el siguiente mensaje, que incluye un PIN:

```
** Before you are able to run the client,
** link it to your injixo account:
**  1) Log in to injixo.com
**  2) Visit https://www.injixo.com/account/integrations
**  3) Select an integration you want to connect the client to
**  4) Enter your pin: 424242 (expires in 5 minutes)
```

1. Vuelve a la página **Añadir una nueva integración** en tu navegador.
2. En la sección **injixo Cloud Link**, introduce el PIN en el campo **PIN mostrado durante la instalación**.
3. Haz clic en _Conectar_{:.doc-button}.
   Cloud Link se conecta a injixo. Ya puedes continuar configurando tu {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o {% link_new integración de CSV | features/acd-integration/cloud/add-csv-integration.md %}.

## Conectarse vía un servidor proxy

Para conectarte vía servidor proxy, añade el nombre del host del proxy o su dirección IP a la variable de entorno **https_proxy**:

- Windows: añade la variable de entorno en la sección Variables del sistema. Si los servicios no funcionan con la cuenta de LocalSystem, configura una variable de usuario.
- Linux: configura la variable de entorno en /etc/environment o en /etc/profile.d.

Ejemplo: `https_proxy=http://your.proxy.example`

Si es necesario, puedes añadir el número de puerto (si no es el puerto 80) y el nombre de usuario y contraseña para la autenticación:

Ejemplo: `https_proxy=http://username:password@your.proxy.example:8080`

## Compartir las direcciones IP de destino de injixo <!-- rethink the name -->

Para permitir que injixo Cloud Link se conecte a los servidores en la nube de injixo, comparte las siguientes URL:

- injixo-*.s3-eu-west-1.amazonaws.com
- www.injixo.com

No puedes compartir una única dirección IP. Los procesos de distribución y actualización modifican con regularidad las direcciones IP de un servidor. Valora si instalar injixo Cloud Link en el DMZ. Si la conexión al servidor falla, verás [códigos de error de sockets de Windows](https://learn.microsoft.com/es-es/windows/win32/winsock/windows-sockets-error-codes-2) en el archivo de registro.

## Registro

injixo Cloud Link rota los archivos de registro diariamente y tras cada reinicio, pero no los borra. Los archivos actuales se encuentran en injixo-cloud-link.log. Los archivos de registro rotados incluyen la fecha de rotación en el nombre del archivo. Para borrarlos, tienes que configurar un borrado regular o borrarlos manualmente.

### Activar el registro detallado

Para las integraciones de base de datos, injixo Cloud Link ofrece un modo de registro detallado. Con él activado, el archivo de registro muestra el número total de filas recuperadas y las primeras diez filas de datos para cada demanda.

Para activar el registro detallado, sigue estos pasos:

1. Pausa injixo Cloud Link.
2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.
3. En la sección **[app]**, define **verbose** como true:

   ```
   [app]
verbose = true
   ```

4. Guarda el archivo y reinicia injixo Cloud Link.

## Configurar la carpeta de importaciones

Por defecto, injixo Cloud Link sube los archivos guardados en su carpeta de instalación. Para las integraciones de CSV, puedes configurar una carpeta de importaciones personalizada. Para ello, sigue estos pasos:

1. Pausa injixo Cloud Link.
2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.
3. En la sección **[app]**, define tu carpeta de importaciones como valor de **importDirectory**.
   - Usa rutas relativas o absolutas.
   - Usa una segunda barra invertida como secuencia de escape para la barra invertida.
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
| ¿Cómo puedo obtener un nuevo PIN si el antiguo ha expirado?                              | Reinicia injixo Cloud Link. Introduce el nuevo PIN del archivo de registro en el campo con seis dígitos en la sección **injixo Cloud Link** de la página de configuración.                                                                                                                                                                                                                                                      |
| ¿Cómo puedo eliminar Cloud Link de mi sistema?                                      | 1\. Vuelve a ejecutar el instalar de injixo Cloud Link o ve a _Programas > Programas y características_{:.breadcrumbs} en Windows.<br>2\. Haz clic con la tecla derecha en **injixo Cloud Link** en la lista y selecciona **Desintalar** o **Desinstalar o cambiar**.<br>3\. Sigue las instrucciones en la pantalla.<br><br>Para desinstalar otras instancias, ve a _Programas > Programas y características_{:.breadcrumbs} en Windows y sigue los pasos 2 y 3. |
| ¿Cómo puedo mover injixo Cloud Link a un servidor nuevo?                                | 1\. Haz clic en {% icon pencil %} junto a una integración.<br>2\. Haz clic en **Conectar una nueva instalación de injixo Cloud Link**.<br>3\. Si es necesario, vuelve a descargar injixo Cloud Link e instálalo en el servidor nuevo.                                                                                                                                                                          |
| ¿Cómo modifico mi integración para una instalación de injixo Cloud Link que ya existe? | 1\. Ve al directorio de instalación y copia el PIN del archivo de registro.<br>2\. Borra la integración existente y crea una nueva.<br>3\. Conecta el injixo Cloud Link en curso con la integración nueva. Para ello, introduce el PIN durante la configuración de la integración nueva.                                                                                                               |
