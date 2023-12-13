EN,DE,File
---,---,translated_output.md
title: Instalar injixo Cloud Link,title: Instalar injixo Cloud Link,translated_output.md
product_label:,product_label:,translated_output.md
- essential,- essential,translated_output.md
- advanced,- advanced,translated_output.md
- enterprise,- enterprise,translated_output.md
- classic,- classic,translated_output.md
description: Instala el cliente injixo Cloud Link para importar datos a injixo.,description: Instala el cliente injixo Cloud Link para importar datos a injixo.,translated_output.md
related_articles:,related_articles:,translated_output.md
- overwrite_title: Añadir título para la fuente no traducida,- overwrite_title: Añadir título para la fuente no traducida,translated_output.md
filepath: features/acd-integration/cloud/how-integrations-work.md,filepath: features/acd-integration/cloud/how-integrations-work.md,translated_output.md
- overwrite_title: Add title for untranslated source,- overwrite_title: Add title for untranslated source,translated_output.md
filepath: features/acd-integration/cloud/import-agent-status-data.md,filepath: features/acd-integration/cloud/import-agent-status-data.md,translated_output.md
---,---,translated_output.md
¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.,¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.,translated_output.md
## ¿Qué es injixo Cloud Link?,## ¿Qué es injixo Cloud Link?,translated_output.md
injixo Cloud Link es un software cliente que debe instalarse cuando configures las integraciones on-premise. injixo Cloud Link importa regularmente los datos a injixo. También puedes instalar injixo Cloud Link si configuras una integración para importar regularmente nuevos archivos CSV desde una carpeta.,injixo Cloud Link es un software cliente que debe instalarse cuando configures las integraciones on-premise. injixo Cloud Link importa regularmente los datos a injixo. También puedes instalar injixo Cloud Link si configuras una integración para importar regularmente nuevos archivos CSV desde una carpeta.,translated_output.md
El directorio de instalación del cliente contiene:,El directorio de instalación del cliente contiene:,translated_output.md
- el ejecutable injixo-cloud-link;,- el ejecutable injixo-cloud-link;,translated_output.md
- uno o más archivos injixo-cloud-link.\*.log;,- uno o más archivos injixo-cloud-link.\*.log;,translated_output.md
- el archivo de configuración injixo-cloud-link.toml;,- el archivo de configuración injixo-cloud-link.toml;,translated_output.md
- una carpeta licenses con las licencias de las bibliotecas de código abierto.,- una carpeta licenses con las licencias de las bibliotecas de código abierto.,translated_output.md
## Requisitos previos,## Requisitos previos,translated_output.md
- Windows: injixo Cloud Link solo es compatible con Windows 10 y versiones posteriores. <!-- what about Linux -->,- Windows: injixo Cloud Link solo es compatible con Windows 10 y versiones posteriores. <!-- what about Linux -->,translated_output.md
- Linux: tienes que instalar el paquete unixODBC.,- Linux: tienes que instalar el paquete unixODBC.,translated_output.md
- Cortafuegos/Proxy: el puerto 443 para tráfico saliente debe estar abierto. injixo Cloud Link utiliza TLS-Encryption con TCP sobre el puerto 443.,- Cortafuegos/Proxy: el puerto 443 para tráfico saliente debe estar abierto. injixo Cloud Link utiliza TLS-Encryption con TCP sobre el puerto 443.,translated_output.md
"En las integraciones on-premise, el acceso a una conexión local es necesario para extraer datos, p. ej., de un ACD o CRM. Dependiendo del tipo de base de datos, es necesario instalar el driver para acceder a la base de datos.","En las integraciones on-premise, el acceso a una conexión local es necesario para extraer datos, p. ej., de un ACD o CRM. Dependiendo del tipo de base de datos, es necesario instalar el driver para acceder a la base de datos.",translated_output.md
## Instalar injixo Cloud Link,## Instalar injixo Cloud Link,translated_output.md
"Cuando añadas una {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %}, {% link_new integración DVB | features/acd-integration/cloud/add-csv-integration.md %}, o {% link_new integración de bases de datos | features/acd-integration/cloud/add-database-integration.md %}, en la sección **injixo Cloud Link** encontrarás enlaces para descargar el archivo de instalación (para Windows) o el archivo comprimido (para Linux).","Cuando añadas una {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %}, {% link_new integración DVB | features/acd-integration/cloud/add-csv-integration.md %}, o {% link_new integración de bases de datos | features/acd-integration/cloud/add-database-integration.md %}, en la sección **injixo Cloud Link** encontrarás enlaces para descargar el archivo de instalación (para Windows) o el archivo comprimido (para Linux).",translated_output.md
### Instalación del servicio de Windows,### Instalación del servicio de Windows,translated_output.md
Usa el instalador de la aplicación cliente en Windows para instalar el primer servicio en tu sistema:,Usa el instalador de la aplicación cliente en Windows para instalar el primer servicio en tu sistema:,translated_output.md
1. Haz clic en **Descargar para Windows 64-bit** y ejecuta el asistente de instalación.,1. Haz clic en **Descargar para Windows 64-bit** y ejecuta el asistente de instalación.,translated_output.md
2. Haz clic en **Siguiente**.,2. Haz clic en **Siguiente**.,translated_output.md
3. (Opcional) Cambia el directorio de instalación.,3. (Opcional) Cambia el directorio de instalación.,translated_output.md
"4. Haz clic en **Siguiente**, luego en **Instalar**.","4. Haz clic en **Siguiente**, luego en **Instalar**.",translated_output.md
Una consola muestra un PIN válido durante 5 minutos.,Una consola muestra un PIN válido durante 5 minutos.,translated_output.md
Sigue las instrucciones en la consola para [conectar Cloud Link a tu integración](#connect-cloud-link-to-your-integration).,Sigue las instrucciones en la consola para [conectar Cloud Link a tu integración](#connect-cloud-link-to-your-integration).,translated_output.md
5. Haz clic en **Finalizar** en el asistente.,5. Haz clic en **Finalizar** en el asistente.,translated_output.md
El instalador crea el servicio de Windows **injixo Cloud Link**.,El instalador crea el servicio de Windows **injixo Cloud Link**.,translated_output.md
"### <a name=""install-multiple-cloud-link-services-windows"">Instalar varios servicios de Windows","### <a name=""install-multiple-cloud-link-services-windows"">Instalar varios servicios de Windows",translated_output.md
Puedes instalar un máximo de ocho servicios adicionales para integraciones independientes. Instálalas en directorios diferentes para evitar que sobrescriban otras instancias.,Puedes instalar un máximo de ocho servicios adicionales para integraciones independientes. Instálalas en directorios diferentes para evitar que sobrescriban otras instancias.,translated_output.md
"Para instalar un segundo servicio de Cloud Link en Windows, añade una nueva integración y sigue estos pasos:","Para instalar un segundo servicio de Cloud Link en Windows, añade una nueva integración y sigue estos pasos:",translated_output.md
1. Haz clic en **Descargar para Windows 64-bit**.,1. Haz clic en **Descargar para Windows 64-bit**.,translated_output.md
2. Abre una línea de comandos de Windows (cmd).,2. Abre una línea de comandos de Windows (cmd).,translated_output.md
3. Ejecuta el siguiente comando:,3. Ejecuta el siguiente comando:,translated_output.md
```,```,translated_output.md
"msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS="":instance.1""","msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS="":instance.1""",translated_output.md
```,```,translated_output.md
> Aumenta la ID de la instancia en el parámetro TRANSFORMS cuando instales más instancias.,> Aumenta la ID de la instancia en el parámetro TRANSFORMS cuando instales más instancias.,translated_output.md
>,>,translated_output.md
"> Por ejemplo: la tercera instancia requiere `"":instance.2""`, la cuarta instancia `"":instance.3""`, y así a continuación.","> Por ejemplo: la tercera instancia requiere `"":instance.2""`, la cuarta instancia `"":instance.3""`, y así a continuación.",translated_output.md
4. Sigue las instrucciones del asistente de instalación.,4. Sigue las instrucciones del asistente de instalación.,translated_output.md
"El instalador te sugerirá un directorio de instalación nuevo, que incluye una referencia a la instancia, p. ej., (Instancia 1).","El instalador te sugerirá un directorio de instalación nuevo, que incluye una referencia a la instancia, p. ej., (Instancia 1).",translated_output.md
"Sugerencia: para identificar a qué integración pertenece una instancia, puedes añadir la identificación de ACD y el tipo, p. ej., (ACD - importación de agentes) al directorio de instalación propuesto por defecto.","Sugerencia: para identificar a qué integración pertenece una instancia, puedes añadir la identificación de ACD y el tipo, p. ej., (ACD - importación de agentes) al directorio de instalación propuesto por defecto.",translated_output.md
Verás el nuevo directorio y un nuevo servicio de Windows injixo Cloud Link etiquetado con el identificador (Instancia {id}).,Verás el nuevo directorio y un nuevo servicio de Windows injixo Cloud Link etiquetado con el identificador (Instancia {id}).,translated_output.md
### Instalación del servicio de Linux,### Instalación del servicio de Linux,translated_output.md
Instala el primer servicio conforme al proncipio:,Instala el primer servicio conforme al proncipio:,translated_output.md
1. Haz clic en **Descargar para Linux 64-bit** y descomprime el archivo en tu directorio de instalación preferido.,1. Haz clic en **Descargar para Linux 64-bit** y descomprime el archivo en tu directorio de instalación preferido.,translated_output.md
2. Abre una terminal.,2. Abre una terminal.,translated_output.md
3. Instala el servicio injixo Cloud Link:,3. Instala el servicio injixo Cloud Link:,translated_output.md
`sudo ./injixo-cloud-link service install`,`sudo ./injixo-cloud-link service install`,translated_output.md
4. Inicia el servicio instalado:,4. Inicia el servicio instalado:,translated_output.md
`sudo ./injixo-cloud-link service start`,`sudo ./injixo-cloud-link service start`,translated_output.md
5. Mostrar un PIN con el comando:,5. Mostrar un PIN con el comando:,translated_output.md
`sudo ./injixo-cloud-link pin`,`sudo ./injixo-cloud-link pin`,translated_output.md
Una consola muestra un PIN válido durante 5 minutos.,Una consola muestra un PIN válido durante 5 minutos.,translated_output.md
Sigue las instrucciones en la consola para [conectar Cloud Link a tu integración](#connect-cloud-link-to-your-integration).,Sigue las instrucciones en la consola para [conectar Cloud Link a tu integración](#connect-cloud-link-to-your-integration).,translated_output.md
"### <a name=""install-multiple-cloud-link-services-linux"">Instalar varios servicios en Linux","### <a name=""install-multiple-cloud-link-services-linux"">Instalar varios servicios en Linux",translated_output.md
Puedes instalar varios servicios para distintas integraciones. Instálalas en directorios distintos para evitar que sobrescriban otras instancias.,Puedes instalar varios servicios para distintas integraciones. Instálalas en directorios distintos para evitar que sobrescriban otras instancias.,translated_output.md
"Para instalar más servicios en Linux, añade una integración nueva y sigue estos pasos:","Para instalar más servicios en Linux, añade una integración nueva y sigue estos pasos:",translated_output.md
1. Crea un nuevo directorio y copia en él los archivos del directorio original de instalación.,1. Crea un nuevo directorio y copia en él los archivos del directorio original de instalación.,translated_output.md
2. Abre el archivo injixo-cloud-link.toml.,2. Abre el archivo injixo-cloud-link.toml.,translated_output.md
3. Cambia la ID en el valor **name** en la sección **[app]** por una ID nuevo:,3. Cambia la ID en el valor **name** en la sección **[app]** por una ID nuevo:,translated_output.md
```,```,translated_output.md
[app],[app],translated_output.md
"name = ""com.injixo.cloud-link.instance.1""","name = ""com.injixo.cloud-link.instance.1""",translated_output.md
```,```,translated_output.md
4. Instala e inicia un nuevo servicio conforme al proceso descrito arriba.,4. Instala e inicia un nuevo servicio conforme al proceso descrito arriba.,translated_output.md
## Connect Cloud Link to your integration,## Connect Cloud Link to your integration,translated_output.md
La instalación de Cloud Link muestra el siguiente mensaje que incluye el PIN:,La instalación de Cloud Link muestra el siguiente mensaje que incluye el PIN:,translated_output.md
```,```,translated_output.md
"** Before you are able to run the client,","** Before you are able to run the client,",translated_output.md
** link it to your injixo account:,** link it to your injixo account:,translated_output.md
**  1) Log in to injixo.com,**  1) Log in to injixo.com,translated_output.md
**  2) Visit https://www.injixo.com/account/integrations,**  2) Visit https://www.injixo.com/account/integrations,translated_output.md
**  3) Select an integration you want to connect the client to,**  3) Select an integration you want to connect the client to,translated_output.md
**  4) Enter your pin: 424242 (expires in 5 minutes),**  4) Enter your pin: 424242 (expires in 5 minutes),translated_output.md
```,```,translated_output.md
1. Vuelve a la página **Add a new integration** en tu navegador.,1. Vuelve a la página **Add a new integration** en tu navegador.,translated_output.md
"2. En la sección **injixo Cloud Link**, introduce tu PIN en el campo de seis dígitos **PIN shown during installation**.","2. En la sección **injixo Cloud Link**, introduce tu PIN en el campo de seis dígitos **PIN shown during installation**.",translated_output.md
3. Haz clic en _Connect_{:.doc-button}.,3. Haz clic en _Connect_{:.doc-button}.,translated_output.md
Cloud Link se conecta a injixo. Puedes continuar el proceso de configuración de tu {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o {% link_new integración DVB | features/acd-integration/cloud/add-csv-integration.md %}.,Cloud Link se conecta a injixo. Puedes continuar el proceso de configuración de tu {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o {% link_new integración DVB | features/acd-integration/cloud/add-csv-integration.md %}.,translated_output.md
## Connect through a proxy server,## Connect through a proxy server,translated_output.md
"To connect through a proxy server, add the proxy hostname or IP address to the **https_proxy** environment variable:","To connect through a proxy server, add the proxy hostname or IP address to the **https_proxy** environment variable:",translated_output.md
"- Windows: Add the environment variable to the **System variables** section. If services do not run with the LocalSystem account, configure a user variable.","- Windows: Add the environment variable to the **System variables** section. If services do not run with the LocalSystem account, configure a user variable.",translated_output.md
- Linux: Set the environment variable in /etc/environment or in /etc/profile.d,- Linux: Set the environment variable in /etc/environment or in /etc/profile.d,translated_output.md
Por ejemplo: `https_proxy=http://your.proxy.example`,Por ejemplo: `https_proxy=http://your.proxy.example`,translated_output.md
"Si es necesario, puedes añadir el número de puerto (si no es el puerto 80) y las credenciales de usuario para autenticarte:","Si es necesario, puedes añadir el número de puerto (si no es el puerto 80) y las credenciales de usuario para autenticarte:",translated_output.md
Por ejemplo: `https_proxy=http://username:password@your.proxy.example:8080`,Por ejemplo: `https_proxy=http://username:password@your.proxy.example:8080`,translated_output.md
## Share injixo destination IP addresses <!-- rethink the name -->,## Share injixo destination IP addresses <!-- rethink the name -->,translated_output.md
"To allow injixo Cloud Link to connect to the injixo cloud servers, share the following URLs:","To allow injixo Cloud Link to connect to the injixo cloud servers, share the following URLs:",translated_output.md
- injixo-\*.s3-eu-west-1.amazonaws.com,- injixo-\*.s3-eu-west-1.amazonaws.com,translated_output.md
- www.injixo.com,- www.injixo.com,translated_output.md
"No puedes compartir un solo dirección IP. Los procesos de implementación y actualización periódicamente cambian las direcciones IP de los servidores. Considera instalar injixo Cloud Link en la DMZ. Si la conexión al servidor falla, se muestran errores con respecto a [Windows sockets](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2) en el archivo de registro.","No puedes compartir un solo dirección IP. Los procesos de implementación y actualización periódicamente cambian las direcciones IP de los servidores. Considera instalar injixo Cloud Link en la DMZ. Si la conexión al servidor falla, se muestran errores con respecto a [Windows sockets](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2) en el archivo de registro.",translated_output.md
## Registro,## Registro,translated_output.md
"injixo Cloud Link gira los archivos de registro a diario y después de un reinicio, pero no los elimina. Los registros actuales se encuentran en el archivo injixo-cloud-link.log. Los registros rotados incluyen la fecha de rotación en el nombre del archivo. Tienes que configurar tu propio script de borrado recurrente, u borrar los archivos manualmente.","injixo Cloud Link gira los archivos de registro a diario y después de un reinicio, pero no los elimina. Los registros actuales se encuentran en el archivo injixo-cloud-link.log. Los registros rotados incluyen la fecha de rotación en el nombre del archivo. Tienes que configurar tu propio script de borrado recurrente, u borrar los archivos manualmente.",translated_output.md
### Activar el registro detallado,### Activar el registro detallado,translated_output.md
"Para integraciones de base de datos, injixo Cloud Link ofrece uno modo de **registro detallado**. Cuando está activado, el archivo de registro muestra el total de filas extraídas y las primeras diez filas de datos de cada petición.","Para integraciones de base de datos, injixo Cloud Link ofrece uno modo de **registro detallado**. Cuando está activado, el archivo de registro muestra el total de filas extraídas y las primeras diez filas de datos de cada petición.",translated_output.md
Puedes activar el registro detallado de la siguiente manera:,Puedes activar el registro detallado de la siguiente manera:,translated_output.md
1. Detén injixo Cloud Link.,1. Detén injixo Cloud Link.,translated_output.md
"2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.","2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.",translated_output.md
"3. En la sección **[app]**, establece **verbose** a true:","3. En la sección **[app]**, establece **verbose** a true:",translated_output.md
```,```,translated_output.md
[app],[app],translated_output.md
verbose = true,verbose = true,translated_output.md
```,```,translated_output.md
4. Guarda el archivo y reinicia injixo Cloud Link.,4. Guarda el archivo y reinicia injixo Cloud Link.,translated_output.md
### Configurar la carpeta de importación,### Configurar la carpeta de importación,translated_output.md
"Por defecto, injixo Cloud Link sube archivos que se guarden en su directorio de instalación. Para las integraciones  de CSV, puedes configurar una carpeta de exportación personalizada de la siguiente manera:","Por defecto, injixo Cloud Link sube archivos que se guarden en su directorio de instalación. Para las integraciones  de CSV, puedes configurar una carpeta de exportación personalizada de la siguiente manera:",translated_output.md
1. Detén injixo Cloud Link.,1. Detén injixo Cloud Link.,translated_output.md
"2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.","2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.",translated_output.md
"3. En la sección **[app]**, configura el atributo **importDirectory** con tu carpeta de importación.","3. En la sección **[app]**, configura el atributo **importDirectory** con tu carpeta de importación.",translated_output.md
- Puedes usar rutas absolutas o relativas.,- Puedes usar rutas absolutas o relativas.,translated_output.md
- Escapa las barras invertidas con dobles barras invertidas.,- Escapa las barras invertidas con dobles barras invertidas.,translated_output.md
4. Guarda el archivo y reinicia injixo Cloud Link.,4. Guarda el archivo y reinicia injixo Cloud Link.,translated_output.md
## Preguntas frecuentes,## Preguntas frecuentes,translated_output.md
<style>,<style>,translated_output.md
table th:first-of-type {,table th:first-of-type {,translated_output.md
width: 25%;,width: 25%;,translated_output.md
},},translated_output.md
table th:nth-of-type(2) {,table th:nth-of-type(2) {,translated_output.md
width: 75%;,width: 75%;,translated_output.md
},},translated_output.md
</style>,</style>,translated_output.md
| Pregunta                                                                        | Respuesta                                                                                                                                                                                                                                                                                                                                                                                                           |,| Pregunta                                                                        | Respuesta                                                                                                                                                                                                                                                                                                                                                                                                           |,translated_output.md
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |,| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |,translated_output.md
| ¿Cómo puedo generar un nuevo PIN si el viejo ya no es válido?                              | Reinicia injixo Cloud Link e introduce el nuevo PIN del archivo de registro en el campo de seis dígitos en la sección **injixo Cloud Link** en la página de configuración.                                                                                                                                                                                                                                                      |,| ¿Cómo puedo generar un nuevo PIN si el viejo ya no es válido?                              | Reinicia injixo Cloud Link e introduce el nuevo PIN del archivo de registro en el campo de seis dígitos en la sección **injixo Cloud Link** en la página de configuración.                                                                                                                                                                                                                                                      |,translated_output.md
"| ¿Cómo puedo desinstalar injixo Cloud Link de mi sistema?                                      | 1. Desinstala injixo Cloud Link ejecutando el instalador de nuevo o yendo a _Programas > Programas y características_{:.breadcrumbs} en Windows.<br>2. Haz clic en la entrada **injixo Cloud Link** en la lista con el botón derecho y selecciona **Desinstalar** o **Desinstalar/cambiar**.<br>3. Sigue las instrucciones en pantalla.<br><br>Para desinstalar instalaciones adicionales, ve a _Programs > Programs and Features_{:.breadcrumbs} en Windows y sigue los pasos 2 y 3. |","| ¿Cómo puedo desinstalar injixo Cloud Link de mi sistema?                                      | 1. Desinstala injixo Cloud Link ejecutando el instalador de nuevo o yendo a _Programas > Programas y características_{:.breadcrumbs} en Windows.<br>2. Haz clic en la entrada **injixo Cloud Link** en la lista con el botón derecho y selecciona **Desinstalar** o **Desinstalar/cambiar**.<br>3. Sigue las instrucciones en pantalla.<br><br>Para desinstalar instalaciones adicionales, ve a _Programs > Programs and Features_{:.breadcrumbs} en Windows y sigue los pasos 2 y 3. |",translated_output.md
"| ¿Cómo puedo mover injixo Cloud Link a un nuevo servidor?                                | 1. Haz clic en {% icon pencil %} a la derecha de una integración para editarla.<br>2. Haz clic en **Conectar una nueva instalación de injixo Cloud Link**.<br>3. Si es necesario, vuelve a descargar injixo Cloud Link e instala el software en el nuevo servidor.                                                                                                                                                                          |","| ¿Cómo puedo mover injixo Cloud Link a un nuevo servidor?                                | 1. Haz clic en {% icon pencil %} a la derecha de una integración para editarla.<br>2. Haz clic en **Conectar una nueva instalación de injixo Cloud Link**.<br>3. Si es necesario, vuelve a descargar injixo Cloud Link e instala el software en el nuevo servidor.                                                                                                                                                                          |",translated_output.md
"| ¿Cómo puedo cambiar la integración para una instalación existente de injixo Cloud Link? | 1. Ve al directorio de instalación y copia el PIN del archivo de registro.<br>2. Elimina la integración existente y crea una nueva integración.<br>3. Conecta injixo Cloud Link al nuevo servicio en la configuración de la nueva integración. Para ello, introduce el PIN del proceso de configuración de la nueva integración.                                                                                                               |","| ¿Cómo puedo cambiar la integración para una instalación existente de injixo Cloud Link? | 1. Ve al directorio de instalación y copia el PIN del archivo de registro.<br>2. Elimina la integración existente y crea una nueva integración.<br>3. Conecta injixo Cloud Link al nuevo servicio en la configuración de la nueva integración. Para ello, introduce el PIN del proceso de configuración de la nueva integración.                                                                                                               |",translated_output.md
