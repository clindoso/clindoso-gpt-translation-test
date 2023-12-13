---
title: Inicio de sesión único (SSO)
product_label:
  - advanced
  - enterprise
description: Aprende cómo configurar y usar el SSO en injixo.
---

El inicio de sesión único (SSO, por sus siglas en inglés) es un mecanismo de autenticación que permite identificarse en distintas aplicaciones y sitios web con un único set de nombre de usuario y contraseña. Se establece una relación de confianza entre un servicio central de administración de identidades (proveedor de identidad o IdP) y una aplicación (proveedor de servicio o SP), en este caso, injixo.

El proveedor de identidad es un producto de terceros, como OneLogin, Microsoft Azure AD, Okta o Google. El uso de SSO significa que tu organización se beneficiará de políticas de seguridad alineadas, como la autenticación de dos factores y la rotación de contraseñas. Los usuarios se autentican frente al proveedor de identidad que redirige a injixo.

La configuración del IdP ha sido probada con los proveedores de identidad mencionados anteriormente. Si no puedes integrar tu proveedor de identidad específico, contacta con nosotros.

## Requisitos

Estos son los requisitos para integrar injixo con tu proveedor de identidad:

- Compatibilidad con el protocolo SAML 2.0.
- Acceso por internet a la URL de metadatos de federación.
- La dirección de correo electrónico registrada en injixo y en tu IdP debe estar conectada a un buzón de correo.

> Para reforzar la seguridad, recomendamos encarecidamente activar las aserciones cifradas y el cifrado de tokens.

## Activar el SSO para tu cuenta

Solo los usuarios con acceso de administrador pueden activar el SSO.

1. Registra injixo como nueva aplicación SAML o SSO en tu IdP.  
   Puedes descargar [este logo de injixo](/assets/img/common/injixo-logo.png) y añadirlo a la página de aplicación web.

2. En injixo, ve a _Account > Seguridad_{:.breadcrumbs} y configura el SSO en **Inicio de sesión único**.

3. En la sección **Metadatos de injixo SAML** tienes dos opciones, dependiendo de si tu IdP permite subir archivos:

   - Permite subir archivos: haz clic en _{% icon download | icon-only %}Descargar_{:.doc-button} y completa la configuración del IdP con el archivo XML descargado.
   - No permite subir archivos: haz clic en **Detalles del proveedor del servicio** y añade las URL mostradas a la configuración de tu IdP.

4. (Opcional) Si usas aserciones SAML encriptadas, haz clic en _{% icon download | icon-only %} Descarga_{:.doc-button} en la sección **Cifrado de tokens**. Añade los certificados descargados a la configuración de tu IdP.
5. Dependiendo de si tu IdP genera una URL de metadatos de federación, hay dos opciones para finalizar la configuración:

   - El IdP genera URL de metadatos de federación: en el IdP, copia tu URL de metadatos de federación para la aplicación registrada. Pega la URL en el campo **URL de metadatos de federación** en la sección **Proveedor de identidad**.
   - El IdP no genera URL de metadatos de federación: descarga el archivo XML de metadatos de federación y alójalo localmente. A modo de ejemplo, puedes leer cómo configurar tu propia [aplicación SAML con Google](https://support.google.com/a/answer/6087519?hl=en).

6. Haz clic en _Guardar configuración_{:.doc-button}.  
   El SSO está activado, pero los usuarios todavía pueden iniciar sesión con su nombre de usuario y contraseña.

> Para garantizar un mayor nivel seguridad, puedes [activar el SSO para todos los usuarios](#activar-el-sso-para-todos-los-usuarios).

## Comprobar la configuración de SSO

Haz clic en _Probar configuración_{:.doc-button} para probar el inicio de sesión con el IdP. El IdP genera una respuesta SAML que se envía a injixo. injixo te redirige a la página de inicio de sesión de tu IdP. Introduce los datos de acceso del IdP. Si la configuración del IdP es correcta y el proceso de autenticación tiene éxito, se iniciará tu sesión en injixo.

{{ 4 | image: 'Configuración de SSO comprobada con éxito para el usuario actual', '80%' }}

<!-- A valid SubjectConfirmation was not found on this Response in our internal server logs -->

La respuesta SAML del IdP contiene la afirmación del usuario autenticado con atributos e información de perfil. Si el proceso no tiene éxito y ves un mensaje de error, verifica la configuración de la aplicación, la configuración del usuario, y los atributos Recipient, InResponseTo, NotBefore y NotOnOrAfter definidos en el IdP. 

Puedes usar las herramientas de desarrollo de tu navegador o herramientas SAML externas para corregir errores en el elemento XML SubjectConfirmation en la respuesta SAML. Para ver la respuesta sin encriptar en texto sin formato, desactiva las afirmaciones encriptadas.

Ejemplo para el elemento XML SubjectConfirmation en una respuesta SAML:

```
<saml:Subject>
    <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">email@company.org</saml:NameID>
    <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
        <saml:SubjectConfirmationData NotOnOrAfter="2022-08-11T08:25:25Z"
            Recipient="https://www.injixo.com/sso/saml/acs"
            InResponseTo="_abcdefgh-0444-4567-abcd-abcdabcdabcd"
    />
    </saml:SubjectConfirmation>
</saml:Subject>
```

## Activar el SSO para todos los usuarios

Para comprobar si la configuración ha tenido éxito, puedes hacer el SSO obligatorio para todos los usuarios y así desactivar el inicio de sesión con nombre de usuario y contraseña. Antes de hacerlo, asegúrate de que:

- todos los usuarios existen en el IdP y en injixo;
- el correo electrónico de injixo coincide con el del IdP;
- todos los usuarios de injixo han sido asignados a la aplicación SSO de injixo en el IdP.

Una vez el SSO sea obligatorio, ya no es posible:

- iniciar sesión con nombre de usuario y contraseña (todas las contraseñas serán desactivadas);
- restablecer las contraseñas en injixo (ni por parte de los usuarios ni de los administradores);
- gestionar el acceso a injixo fuera del IdP.

Activa el SSO para todos los usuarios en la sección **3\. Activar el SSO para todos los usuarios**. El botón _Activar el SSO para todos los usuarios_{:.doc-button} se activa una vez hayas comprobado con éxito tu configuración de SSO.

{{ 5 | image: 'Botón para activar el SSO para todos los usuarios', '80%' }}

## Modificar la dirección de correo electrónico con el SSO activado

Con el SSO activo, los usuarios no pueden modificar su dirección de correo electrónico autónomamente, porque la dirección de correo de injixo tiene que corresponder con la dirección usada en el IdP.

Solo los usuarios con acceso de administrador pueden modificar las direcciones de correo electrónico en injixo.

## Iniciar sesión con el SSO

Cuando el SSO está activado, los usuarios pueden iniciar sesión en [https://www.injixo.com/login/sso](https://www.injixo.com/login/sso). Tras introducir su dirección de correo electrónico, se les redirige a la página de inicio de sesión del IdP. Si los usuarios ya han iniciado sesión, se les redirige automáticamente de vuelta a injixo. En caso contrario, tienen que introducir la contraseña del IdP.

## Revocar el acceso a injixo

Para revocar el acceso a injixo con SSO de un usuario, tienes que desasignar al usuario injixo en el IdP. Ten en cuenta que si el usuario sigue existiendo en injixo, será incluido en la facturación. Para evitar costes adicionales, tienes que {% link_new desactivar o eliminar el usuario | features/administration/deactivate-employees.md %}.

## Desactivar el SSO

Si quieres desactivar el SSO y volver a autorizar el inicio de sesión con nombre de usuario y contraseña, los usuarios con acceso de administrador pueden desactivar el SSO. Al hacer esto, se eliminará la conexión con el IdP y todos los datos de configuración introducidos. Una vez el SSO haya sido desactivado, todos los usuarios activos recibirán un correo para establecer una nueva contraseña en injixo. Hecho esto, los usuarios pueden volver a iniciar sesión con nombre de usuario y contraseña en [https://www.injixo.com/login](https://www.injixo.com/login).
