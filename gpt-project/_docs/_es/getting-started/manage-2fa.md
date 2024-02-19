---
title: Gestionar la autenticación de dos factores (2FA)
product_label:
  - essential
  - advanced
  - enterprise
description: Aprende cómo activar y desactivar la 2FA para las cuentas de tus empleados.
redirect_from:
  - /es/2fa/
redirect_reason: Updated filename on 14 July 2023
---

> Solo los usuarios con acceso de administrador pueden administrar la autenticación de dos factores para otros usuarios.

## Ver la configuración de 2FA de otros usuarios

Para ver el estado actual de la 2FA de otros usuarios, sigue estos pasos:
1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. En la columna **2FA** a la derecha, un icono de escudo indica el estado de la 2FA de cada usuario. Mueve el cursor sobre el icono para ver más información.
  - Icono rojo {% icon 2FA-red | icon-only %}: la 2FA no está activa.
  - Icono naranja con signo de exclamación {% icon 2FA-orange | icon-only %}: un administrador ha hecho la 2FA obligatoria para el usuario. El usuario tendrá que activar la 2FA cuando inicie sesión la próxima vez.
  - Icono naranja con marca de verificación {% icon 2FA-activated | icon-only %}: la 2FA está activa. El usuario la activó por decisión propia.
  - Icono verde con marca de verificación {% icon 2FA-green | icon-only %}: la 2FA está activa. La 2FA es obligatoria.

## Hacer la 2FA obligatoria para otros usuarios
Puedes obligar a otros usuarios a activar la 2FA. Hacer la 2FA obligatoria para otros usuarios tiene las siguientes consecuencias:

- Los usuarios no podrán iniciar sesión si no activan la 2FA.
- Los usuarios no podrán desactivar la 2FA para sus cuentas.

Antes de hacer la 2FA obligatoria para otros usuarios, asegúrate de que tengan acceso a una {% link_new aplicación de autenticación compatible | getting-started/use-two-factor-authentication.md | #prerrequisito-instalar-una-aplicación-de-autenticación %}.

### Hacer la 2FA obligatoria para usuarios concretos

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en el **nombre** del usuario para quien quieres hacer la 2FA obligatoria.  
   Verás la página con los detalles del usuario.
3. En la sección **Seguridad**, marca la casilla **Forzar la activación de 2FA**.
4. Haz clic en _Guardar_{:.doc-button}.

### Hacer la 2FA obligatoria para todos los usuarios

1. Ve a _Account > Seguridad_{:.breadcrumbs}. En esta página puedes ver la distribución actual de la 2FA entre tus usuarios.
2. Haz clic en _Activar obligatoriedad de 2FA para todos los usuarios_{:.doc-button}.  
   Verás un mensaje verde de confirmación. El texto del botón cambiará a _Revocar obligatoriedad_{:.doc-button}.

### Desactivar la 2FA para usuarios concretos

En algunos casos, querrás desactivar la 2FA temporalmente para usuarios concretos, o excluirlos por completo de la obligatoriedad de 2FA.

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en el **nombre** del usuario para el que quieres desactivar la 2FA.  
   Verás la página con los detalles del usuario.
3. En la sección **Seguridad**, desmarca la casilla **Forzar la activación de 2FA**.
4. Haz clic en _Guardar_{:.doc-button}.
