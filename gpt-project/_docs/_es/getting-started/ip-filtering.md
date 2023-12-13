---
title: Filtrado IP
product_label:
  - enterprise
  - advanced
description: Aprende a configurar el filtrado IP para tu tenant de injixo.
toc: true
---

El filtrado IP es una funcionalidad de pago. No está incluido automáticamente en tu plan Enterprise o Advanced WFM
Si tu organización está interesada en esta funcionalidad, ponte en contacto con tu consultor.

El filtrado IP garantiza que tus usuarios solo puedan acceder a tu tenant de injixo desde rangos de direcciones IP específicos. Los usuarios con otras direcciones IP no podrán acceder a injixo. injixo ofrece una [lista de control de acceso a la red](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) (lista de control de acceso o network ACL). Activa la lista de control de acceso para solo permitir el acceso a injixo desde redes seleccionadas (p.&nbsp;ej., la red de tu organización).

## Activar el filtrado IP

Solo los usuarios con acceso de administrador pueden activar el filtrado IP.

> Atención
> 
> Cuando actives el filtrado de IP, se cerrará la sesión de todos los usuarios activos. Dependiendo del área del producto, el marco temporal varía:
> - El cierre de sesión puede ser inmediato
> - El cierre de sesión ocurre con la siguiente recarga o subida de datos
> - El cierre de sesión se programa (solo en el Centro de planificación accesible a través de _Plan > Centro de planificación_{:.breadcrumbs})
> 
> Para seguir trabajando con injixo, los usuarios tendrán que volver a iniciar sesión.

1. Ve a _Account > Seguridad_{:.breadcrumbs} y desplázate hasta la sección **Filtrado IP**.
2. En el campo o campos **Rango de direcciones IP**, introduce los rangos de direcciones IP en [formato CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#:~:text=CIDR%20notation%20specifies%20an%20IP,bits). Puedes añadir un máximo de tres rangos de direcciones IP.
3. Haz clic en _Activar filtrado_{:.doc-button}.

El filtrado IP solo afecta a las interacciones en la interfaz de usuario. Actualmente, el filtrado IP no afecta al Centro de planificación opcional, disponible a través de URL directa.
 
## Editar los rangos de direcciones IP

> Atención
> 
> Si editas los rangos de direcciones IP, se cerrará la sesión de todos los usuarios la próxima vez que interactúen con injixo. Para seguir trabajando con injixo, los usuarios tendrán que volver a iniciar sesión.

1. Ve a _Account > Seguridad_{:.breadcrumbs} y desplázate hasta la sección **Filtrado IP**.
2. Edita los rangos de direcciones IP.
3. Haz clic en _Guardar_{:.doc-button}.

## Desactivar el filtrado IP

1. Ve a _Account > Seguridad_{:.breadcrumbs} y desplázate hasta la sección **Filtrado IP**.
2. Elimina los rangos de direcciones IP.
3. Haz clic en _Desactivar filtrado_{:.doc-button}.

Una vez hayas desactivado el filtrado IP, los usuarios podrán acceder a injixo desde cualquier dirección IP.

> Atención
> 
> Si desactivas el filtrado de IP, se cerrará la sesión de todos los usuarios. Para seguir trabajando con injixo, los usuarios tendrán que volver a iniciar sesión.
