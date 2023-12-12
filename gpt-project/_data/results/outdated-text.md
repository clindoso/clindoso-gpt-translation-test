---
title: Instalar injixo Cloud Link
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Instala el cliente injixo Cloud Link para importar datos a injixo.
related_articles:
  - overwrite_title: ¿Cómo funcionan las integraciones?
    filepath: features/acd-integration/cloud/how-integrations-work.md
---

¿Las integraciones te son ajenas? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## ¿Qué es injixo Cloud Link?

injixo Cloud Link es un cliente que tienes que instalar para configurar integraciones on-premise. injixo Cloud Link importa datos regularmente a injixo. También puedes instalar injixo Cloud Link cuando configures una integración CSV si quieres importar periódicamente nuevos archivos CSV desde una carpeta.

El directorio de la instalación del cliente contiene:

- el ejecutable injixo-cloud-link.
- uno o más archivos injixo-cloud-link.\*.log.
- el archivo de configuración injixo-cloud-ink.toml.
- una carpeta licenses con las licencias de las librerías open source.

## Prerrequisitos

- Windows: injixo Cloud Link se ejecuta en Windows 10 o superior y en Windows Server 2016 o superior. <!-- what about Linux -->
- Linux: El paquete unixODBC debe estar instalado.
- Firewall/Proxy: El puerto 443 debe estar abierto para tráfico saliente. injixo Cloud Link usa TLS-Encryption con TCP sobre el puerto 443.

Atención: Las integraciones on-premise acceden a un sistema local para extraer datos, p. ej., un ACD o CRM. Dependiendo del tipo de base de datos, debes instalar un controlador de base de datos.

## Instalar injixo Cloud Link

Cuando añades una {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %}, [integración CSV](#csv-integration-best-practices) o [integración de base de datos](#database-integration-best-practices-step-by-step), la sección **injixo Cloud Link** incluye enlaces para descargar el instalador del cliente (para Windows) o el archivo (para Linux).

### Instalación del servicio Windows

Instala el primer servicio con el instalador de cliente Windows:

1. Haz clic en **Descargar para Windows 64-bit** y ejecuta el instalador.
2. Haz clic en **Siguiente**.
3. (Opcional) Cambia el directorio de instalación.
4. Haz clic en **Siguiente** y luego en **Instalar**.  
   [^windows-user]
5. Haz clic en **Finalizar** en el instalador.  
   El instalador crea el servicio Windows **injixo Cloud Link**.

[^windows-user]: Una ventana de consola muestra un PIN que es válido durante 5 minutos. Tras finalizar este proceso, puedes [conectar Cloud Link a tu integración](#connect-cloud-link-to-your-integration]).

### <a name="install-multiple-cloud-link-services-windows">Instalar varios servicios Windows

Puedes instalar hasta ocho servicios adicionales para integraciones diferentes. Para no sobrescribir las instancias de servicio ya instaladas, instala cada servicio en un directorio separado.

Para instalar un segundo servicio de Cloud Link en Windows, añade una integración y sigue estos pasos:

1. Haz clic en **Descargar para Windows 64-bit**.
2. Abre el símbolo de sistema de Windows.
3. Para la segunda instancia, ejecuta este comando:

   ```
   msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS=":instance.1"
   ```

   > Al instalar instancias adicionales, incrementa el ID de la instancia en el parámetro TRANSFORMS.
   >
   > P. ej., el ID de instancia para la tercera instancia debe ser `":instance.2"`, para la cuarta `":instance.3"`, etc.

4. Sigue las instrucciones del instalador.  
   El instalador te sugerirá un nuevo directorio de instalación que incluye la instancia: (Instance 1).
   Recomendación: Para identificar a qué integración pertenece la instalación, añade detalles del ACD y el tipo de importación, p. ej., (ACD - agent import) al directorio de instalación predeterminado.
   Verás el nuevo directorio y un nuevo servicio Windows llamado injixo Cloud Link (Instance {id}).

### Instalación del servicio Linux

Instala el primer servicio basándote en el siguiente ejemplo:

1. Haz clic en **Descargar para Linux 64-bit** y descomprime el archivo en la carpeta de instalación que quieras.
2. Abre la terminal.
3. Instala el servicio injixo Cloud Link:  
   `sudo ./injixo-cloud-link service install`
4. Arranca el servicio recién instalado:  
   `sudo ./injixo-cloud-link service start`
5. Muestra un PIN con el siguiente comando:  
   `sudo ./injixo-cloud-link pin`  
   Una ventana de consola muestra un PIN que es válido durante 5 minutos.  
   [^windows-user]

[^windows-user]: Tras finalizar este proceso, puedes [conectar Cloud Link a tu integración](#connect-cloud-link-to-your-integration]).

### <a name="install-multiple-cloud-link-services-linux">Instalar varios servicios Linux

Puedes instalar varios servicios que se corresponden con distintas integraciones. Para no sobrescribir servicios que ya hayas instalado, deben estar en directorios separados.

Para instalar más servicios en Linux, añade una integración y sigue estos pasos:

1. Crea un nuevo directorio y copia los archivos del directorio de instalación original.
2. Abre el archivo injixo-cloud-link.toml.
3. Modifica el valor **name** en la sección **[app]** a un nuevo identificador:

   ```
   [app]
   name = "com.injixo.cloud-link.instance.1"
   ```

4. Instala y arranca el nuevo servicio desde el nuevo directorio según las instrucciones anteriores.

## Conectar Cloud Link a tu integración

Durante la instalación de Cloud Link, aparece el siguiente mensaje, con un PIN:

```
** Before you are able to run the client,
** link it to your injixo account:
**  1) Log in to injixo.com
**  2) Visit https://www.injixo.com/account/integrations
**  3) Select an integration you want to connect the client to
**  4) Enter your pin: 424242 (expires in 5 minutes)
```

1. Regresa a la página **Añadir una nueva integración** en tu explorador.
2. En la sección **injixo Cloud Link**, introduce el PIN en el campo de entrada six-digit input field **PIN shown during installation**.
3. Haz clic en _Connect_{:.doc-button}.
   Cloud Link se conecta a injixo. Tienes que seguir las instrucciones para configurar tu {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o {% link_new integración CSV | features/acd-integration/cloud/add-csv-integration.md %}.

### ¿Qué hacer si la instalación ha expirado?

¿Necesitas un nuevo PIN porque el otro ha caducado? Reinicia el servicio de injixo Cloud Link. El nuevo PIN aparecerá en un archivo de log en la carpeta de instalación. Puedes registrar este nuevo PIN tras haber finalizado la instalación en el formulario de la sección **injixo Cloud Link**.

Si el problema persiste, contacta a los administradores de tu entorno injixo o consulta la [Guía de solución de problemas|https://www.injixo.com/sites/default/files/guides/de/rotation-documentation.html#troubleshooting-common-installation-terminal-issues].

## Configurar el directorio de importación

Por omisión, injixo Cloud Link importa archivos que se encuentren en su carpeta de instalación. Para configurar una carpeta de importación personalizada para integraciones CSV:

1. Detén injixo Cloud Link.
2. Abre la carpeta de instalación y edite el archivo injixo-cloud-link.toml.
3. En la sección **[app]**, establece el valor para **importDirectory**.

   - Puedes usar rutas relativas o absolutas.
   - Utiliza dos barras invertidas para registrar barras invertidas, como se muestra aquí.

   4. Guarda el archivo e inicia injixo Cloud Link.

## error handling

attetention: Once you've set up and connected your on-premise integration to injixo, the integration type and the associated PIN become immutable.

If a Cloud Link installation needs to be connected to a different on-premise integration, you have to:

- Stop the existing Cloud Link service.
- [Delete the integration in injixo](https://www.quinyx.com/delete-integration).
- Follow the **[instructions below](#uninstall-cloud-link-from-your-system)** for the setup of the new Cloud Link installation.
- The setup will generate a new PIN that needs to be connected to the target on-premise integration following the [instructions above](#connect-cloud-link-to-your-integration).

## Uso de servidores proxy

Cuando se accede a injixo Cloud Link a través de un servidor proxy, incluye el nombre de host del proxy o su dirección IP a la variable de entorno **https_proxy**:

- Windows: Agrega la variable de entorno a la sección **Variables del sistema**. Si los servicios no se ejecutan con la cuenta LocalSystem, configura una variable de usuario.
- Linux: Ajusta la variable de entorno en /etc/environment o en /etc/profile.d

Explicación detallada: [Usar un servidor proxy para conexiones HTTP/HTTPS a internet](https://docs.microsoft.com/es-es/windows_server/administration/windows-commands/http-secure-proxy?context=/Context/WS2016/).

## Compartir direcciones IP de destinos injixo <!-- rethink the name -->

Para que injixo Cloud Link tenga acceso a los servidores en la nube de injixo, añade las siguientes URLs a la lista blanca de tu firewall:

- injixo-\*.s3-eu-west-1.amazonaws.com
- www.injixo.com

No es suficiente con compartir una única dirección IP. Los procesos de despliegue y actualización cambian periódicamente las direcciones de los servidores. Considera instalar injixo Cloud Link en la DMZ [p.&#160;ej., consulta a tu departamente de IT]. De este modo, si una conexión con el servidor falla, los mensajes de error de Windows Socket Error aparecerán en el archivo de registro.

## Registro

injixo Cloud Link rota los archivos de registro a diario y después de reiniciar, pero no los borra. Los archivos de registro actuales están en el archivo injixo-cloud-link.log. Los archivos de registro rotados incluyen la fecha de rotación en el nombre del archivo. Tienes que configurar tú mismo la eliminación periódica de los archivos o hacerlo manualmente.

### Activar registro detallado

Las integraciones de injixo Cloud Link para bases de datos incluyen un modo de registro detallado que puedes activar. Si lo activas, el archivo de registro muestra el [total de filas recuperadas y las diez primeras filas de datos para cada petición].

Puedes activar el modo de registro detallado de las integraciones de injixo Cloud Link de la siguiente forma:

1. Detén injixo Cloud Link.
2. Abre el archivo injixo-cloud-link.toml en la carpeta de instalación.
3. En la sección **[app]**, cambia el valor de **verbose** a **true**.

   ```
   [app]
   verbose = true
   ```

4. Guarda el archivo e inicia injixo Cloud Link.

Atención: No actives el redehubicap0verbose] si no es absolutamente necesario, ya que reduce el rendimiento del sistema.

## Cuestiones frecuentes

<style>
table th:first-of-type {
    width: 25%;
}
table th:nth-of-type(2) {
    width: 75%;
}
</style>

| Pregunta                                                                        | Respuesta                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| How do I get a new PIN if the old one has expired?                              | Reinicia injixo Cloud Link. Aparecerá un nuevo PIN en el archivo de log. Puedes registrar este nuevo PIN tras haber finalizado la instalación en el formulario de la sección **injixo Cloud Link**.                                                                                                                                                                                                                                                      |
| Cómo se desinstala Cloud Link de mi sistema?                                      | 1. Vuelve a ejecutar el instalador de injixo Cloud Link o ve a _Programas > Programas y características_{:.breadcrumbs} en Windows.<br>2. Haz clic con el botón derecho en **injixo Cloud Link** en la lista y selecciona **Desinstalar** o **Modificar/Desinstalar**.<br>3. Sigue las instrucciones en pantalla.<br><br>Para desinstalar instancias adicionales, ve a _Programs > Programs and Features_{:.breadcrumbs} en Windows y sigue los pasos 2 y 3. |
| How do I move injixo Cloud Link to a new server?                                | 1. Haz clic en {% icon pencil %} a la derecha de la integración que quieres editar.<br>2. Haz clic en **Conectar una nueva instalación de injixo Cloud Link**.<br>3. Si es necesario, vuelve a descargar injixo Cloud Link e instala el software en el nuevo servidor.                                                                                                                                                                          |
| How do I change the integration for an existing injixo Cloud Link installation? | 1. Ve al directorio de instalación, copia el PIN del archivo de log.<br>2. Borra la integración existente y crea una nueva.<br>3. Conecta injixo Cloud Link a tu nueva integración en ejecución. Durante el proceso de configuración de la nueva integración, introduce el PIN.