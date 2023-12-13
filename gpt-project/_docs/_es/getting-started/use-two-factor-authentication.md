---
title: Usar la autenticación de dos factores (2FA)
product_label:
  - essential
  - advanced
  - enterprise
description: Aprende cómo activar y desactivar la autenticación de dos factores para tu cuenta.
---

## Qué es la autenticación de dos factores (2FA)

La autenticación de dos factores (2FA) añade una capa de seguridad a tus cuentas en línea.  
Para iniciar sesión en tu cuenta cuando la 2FA está activa, necesitas:
- tus datos de acceso;
- una contraseña adicional, generada por otro dispositivo.

> Activa la 2FA para tu cuenta de injixo lo antes posible para aumentar la seguridad.

## Prerrequisito: instalar una aplicación de autenticación

injixo admite las aplicaciones de autenticación incluidas en la siguiente tabla.  
Si usas un dispositivo Android, descarga la aplicación en la Google Play Store. Si usas un dispositivo de Apple, descarga la aplicación en la App Store de Apple.

|-------|--------|---------|
| Google Authenticator | [App Store de Apple](https://apps.apple.com/us/app/google-authenticator/id388497605) | [Google Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) |
| Microsoft Authenticator | [App Store de Apple](https://apps.apple.com/us/app/microsoft-authenticator/id983156458) | [Google Play Store](https://play.google.com/store/apps/details?id=com.azure.authenticator) |
| Authy | [App Store de Apple](https://apps.apple.com/us/app/authy/id494168017) | [Google Play Store](https://play.google.com/store/apps/details?id=com.authy.authy) |

## Activar la 2FA para tu cuenta

Para activar la 2FA para tu cuenta, necesitas acceso a un dispositivo principal (p.&nbsp;ej., un ordenador) y a tu dispositivo personal.  
En tu ordenador o dispositivo principal, procede de la siguiente manera:

1. Inicia sesión en injixo y haz clic en tu nombre de usuario arriba a la derecha en la barra de navegación.
2. Haz clic en la pestaña **Seguridad**.
3. Haz clic en _Activar 2FA_{:.doc-button}.
4. Introduce tu contraseña.
5. Haz clic en _Continuar_{:.doc-button}.  
   Verás la página **Activar autenticación de dos factores**, donde se explican los pasos que debes seguir a continuación.

En tu dispositivo personal, sigue los pasos explicados en la página Activar autenticación de dos factores:

1. Instala una de las [aplicaciones de autenticación soportadas](#prerrequisito-instalar-una-aplicación-de-autenticación).
2. Abre la aplicación de autenticación y añade injixo.  
   Para ello, elige una de las siguientes opciones:
   - Con la aplicación de autenticación, escanea el código QR en la página **Activar autenticación de dos factores**.
   - Introduce la clave mostrada en la página **Activar autenticación de dos factores** en la aplicación de autenticación.  
Tu aplicación de autenticación ya está configurada y puede generar contraseñas de un solo uso (OTP, por sus siglas en inglés).

En tu ordenador o dispositivo principal, procede de la siguiente manera:

1. En la página **Activar autenticación de dos factores**, introduce un OTP en el campo **Contraseña de un solo uso**.
2. Haz clic en _Continuar_{:.doc-button}.
3. Guarda los códigos de respaldo o descárgalos como archivo. Haz clic en _Descargar_{:.doc-button} o _Copiar_{:.doc-button}. Si no aparecen códigos de respaldo, es porque han sido desactivados para tu cuenta de tu organización. <!-- feature flag -->

   > Guarda tus códigos de respaldo en un lugar seguro.
   >
   > Si pierdes acceso a tu dispositivo personal, solo podrás acceder a tu cuenta utilizando un código de respaldo.<br>Guarda tus códigos de respaldo en un lugar seguro, como un gestor de contraseñas, o imprímelos y asegúrate de que nadie más tiene acceso a ellos.

4. Marca la casilla **He almacenado de manera segura mis códigos de respaldo.**
5. Haz clic en _Activar 2FA_{:.doc-button}.  
   Recibirás un correo electrónico informándote de que la 2FA ha sido activada.  
A partir de ahora, necesitarás tanto tus datos de acceso como un OTP para iniciar sesión en injixo.

## Iniciar sesión con la 2FA activa

1. Introduce tu correo electrónico y contraseña en la página de inicio de sesión de injixo y haz clic en _Inicio de sesión_{:.doc-button}.  
2. Introduce el OTP generado por tu aplicación de autenticación  
   Cada OTP es válido durante solo 30 segundos. Pasado este tiempo, la aplicación genera uno nuevo.
3. Haz clic en _Verificar_{:.doc-button} para completar el inicio de sesión.

Si no puedes iniciar sesión, verifica en tu aplicación de autenticación que el OTP introducido aún es válido. Si no es así, simplemente introduce un nuevo OTP.  
Si continúas teniendo dificultades, sigue las instrucciones a continuación para iniciar sesión con un código de respaldo.

### Iniciar sesión con un código de respaldo

Cuando configuraste la 2FA para tu cuenta, recibiste 10 códigos de respaldo. Si no tienes acceso a tu dispositivo personal, puedes iniciar sesión en injixo con uno de tus códigos de respaldo.

> Atención
>
> Utiliza los códigos de respaldo solo en caso de emergencia. Cada código es válido una sola vez. Por norma general, siempre deberías iniciar sesión con un OTP.

Para iniciar sesión con un código de respaldo en lugar de un OTP:

1. Introduce tu correo electrónico y contraseña en la página de inicio de sesión de injixo y haz clic en _Inicio de sesión_{:.doc-button}.
2. Haz clic en el enlace del código de respaldo debajo del campo **Contraseña de un sólo uso**.
3. Introduce uno de tus 10 códigos de respaldo en el campo de entrada **Código de respaldo**.
4. Haz clic en _Verificar_{:.doc-button} para completar el inicio de sesión.

<!-- a tag required. configured name used in injixo UI link -->

### Iniciar sesión sin dispositivo personal y sin códigos de respaldo

Si no puedes iniciar sesión con 2FA y no puedes acceder a tus códigos de respaldo, contacta con un usuario con acceso de administrador para que desactive la 2FA para tu cuenta. Así podrás iniciar sesión sin OTP y podrás restablecer tu configuración de 2FA.

## Usar la 2FA en un nuevo dispositivo personal

Para utilizar un dispositivo diferente para generar OTP, debes desactivar temporalmente la 2FA en tu cuenta y [activarla otra vez con tu dispositivo nuevo](#activar-la-2fa-para-tu-cuenta).

Si no puedes desactivar la 2FA, contacta con un usuario con acceso de administrador para que la desactive  para tu cuenta.

## Desactivar la 2FA para tu cuenta

> Atención
>
> No se recomienda desactivar la 2FA. Si tus administradores han hecho la 2FA obligatoria para tu cuenta, no puedes desactivarla.

1. Inicia sesión en injixo y haz clic en tu nombre de usuario arriba a la derecha en la barra de navegación.
2. Haz clic en la pestaña **Seguridad**.  
   En la parte superior, puedes ver tu configuración actual de 2FA.
3. Haz clic en _Desactivar 2FA_{:.doc-button}.
4. Introduce tu contraseña.
5. Haz clic en _Continuar_{:.doc-button} para confirmar la desactivación.

Recibirás un correo electrónico informándote de que la 2FA ha sido desactivada. A partir de ahora, puedes iniciar sesión sin introducir un OTP.

> ¿Has recibido el correo de desactivación aunque no has desactivado la 2FA?
>
> Comprueba tu cuenta junto con un administrador de tu organización. Considera si cambiar tu contraseña.
