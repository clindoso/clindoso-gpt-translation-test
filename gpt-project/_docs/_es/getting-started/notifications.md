---
title: Notificaciones
product_label:
  - advanced
  - enterprise
description: Aprende cómo se usan las notificaciones en injixo y a configurarlas.
related_articles:
  - overwrite_title: Notificar cambios en la planificación
    filepath: features/scheduling/schedules/schedules-notify-scheduling-changes.md
  - overwrite_title: Intercambiar turnos con tu equipo
    filepath: features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md
  - overwrite_title: Oferta de turnos
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Permitir que tus empleados vean su planificación
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
---

injixo puede enviar notificaciones push y por correo electrónico.

Por defecto, injixo envía notificaciones para informar a los empleados sobre sucesos del proceso de planificación:

- planificaciones publicadas
- cambios en la planificación
- solicitudes de cambio de turno

Las notificaciones de correo electrónico se envían a las direcciones de correo con las que los usuarios inician sesión. Las notificaciones push del navegador aparecen como notificaciones emergentes si has iniciado sesión en injixo en al menos una pestaña del navegador. Si haces clic en la notificación, el navegador mostrará la pestaña de injixo.

## Configurar notificaciones

Los usuarios con acceso de Administrador pueden desactivar notificaciones específicas.

1. Ve a _Account > Notificaciones_{:.breadcrumbs}.
2. Haz clic en una pestaña para cambiar la categoría de notificación.  
   > Atención
   > 
   > Si desactivas las notificaciones por correo electrónico de Me, tus empleados no podrán invitar a sus compañeros a intercambiar turnos en injixo Me.
3. Marca o desmarca las casillas **Correo electrónico** o **Push del navegador**.

Los ajustes de notificaciones se guardan automáticamente. Los ajustes seleccionados se aplican a todos los usuarios.

## Permitir notificaciones push en el navegador

Si las notificaciones no han sido configuradas mediante políticas de grupo en el sistema operativo, cada usuario puede activarlas para el navegador actual en su perfil de usuario:

1. Haz clic en tu **nombre de usuario** arriba a la derecha para abrir tu perfil de usuario.
2. En la sección **Notificaciones**, haz clic en _Permitir las notificaciones de injixo_{:.doc-button}.
3. Se abrirá una ventana emergente en tu navegador en la que puedes permitir las notificaciones push de forma permanente.

## Solucionar problemas con las notificaciones push del navegador

Las notificaciones push son gestionadas por el navegador y el sistema operativo, por lo que ambos deben permitir el envío de notificaciones. Los modos de No molestar y las configuraciones de enfoque (p.&nbsp;ej., alarmas y prioridad) pueden evitar las notificaciones. Asegúrate también de que tu navegador esté actualizado. Borra la caché y las cookies del navegador si es necesario.

Consulta cómo solucionar problemas con las notificaciones en diferentes navegadores y sistemas operativos:

- Chrome: [Guía de Google Chrome](https://support.google.com/chrome/answer/3220216?hl=es)
- Firefox: [Mozilla Firefox Support](https://support.mozilla.org/es/kb/notificaciones-push-en-firefox)
- Safari: [Manual de uso de Safari](https://support.apple.com/es-es/guide/safari/sfri40734/15.1/mac/12.0)
- Windows: [Soporte técnico de Windows](https://support.microsoft.com/es-es/windows/cambiar-la-configuraci%C3%B3n-de-notificaci%C3%B3n-en-windows-8942c744-6198-fe56-4639-34320cf9444e#WindowsVersion=Windows_10)
- Android: [Ayuda de Android](https://support.google.com/android/answer/9079661?hl=es)
- Mac: [Manual de uso de macOS](https://support.apple.com/es-es/guide/mac-help/mchl2fb1258f/mac)
- iOS: [Soporte de Apple iOS](https://support.apple.com/es-es/HT201925)

## Verificar las notificaciones push del navegador

Para comprobar si las notificaciones push del navegador funcionan en tu dispositivo y con el navegador de tu elección,
ve a <https://www.bennish.net/web-notifications.html/>.
