---
title: Configurar los roles de usuario
redirect_from:
  - /es/user-and-role-authorization/
redirect_reason: renamed file in June 2021
description: Aprende qué roles de usuario están disponibles, modifica sus permisos, crea nuevos roles y asigna roles a usuarios.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
---

## ¿Qué son los roles de usuario?

Los roles de usuario determinan los permisos de acceso de un grupo de usuarios a:

- los productos y funcionalidades de injixo, p.&nbsp;ej., _Forecast_{:.menu-item};
- las funcionalidades en WFM, p.&nbsp;ej., _WFM > Gestión_{:.breadcrumbs}.

injixo tiene categorías de roles, cada una con un {% link_new rol de usuario predeterminado | getting-started/default-user-roles.md | #roles-de-usuario-predeterminados %} con permisos o derechos de acceso predefinidos. Cuando añades un nuevo rol de usuario a una categoría de roles, este tendrá acceso a los mismos productos y funcionalidades que el rol de usuario predeterminado.<br>
La categoría de rol Otro no incluye ningún rol de usuario predeterminado.

### Consultar y organizar los roles de usuario

Ve a _Account > Roles de usuario_{:.breadcrumbs}.  
   Los roles de usuario se agrupan en categorías predefinidas (como la categoría Planificador). Estas categorías te ayudan a organizar los permisos de acceso. Puedes arrastrar y soltar un rol de usuario de una categoría a otra o usar la búsqueda para buscar roles de usuario por su nombre.
   
   > Los permisos para las nuevas funcionalidades se asignan según las categorías de roles de usuario.  
   >   
   >Los permisos para las nuevas funcionalidades de injixo se asignan automáticamente a los roles de usuario de acuerdo con su categoría de rol. Por ejemplo, una nueva funcionalidad para planificadores será accesible para todos los usuarios en la categoría Planificador. Si has movido un rol de la categoría Planificador a otra categoría, ya no se le asignarán automáticamente permisos para la nueva funcionalidad para planificadores. En caso necesario, los usuarios con acceso de administrador pueden asignarle los permisos al rol de usuario manualmente. Los roles de usuario en la categoría de rol Otro tampoco reciben permisos automáticamente. A los roles de esta categoría siempre hay que asignarles los permisos manualmente.

   {{ 1 | image: "Categorías en la panorámica de roles de usuario", '80%' }}

### Crear nuevos roles de usuario

1. Haz clic en el {% icon blue_plus | icon-only %} icono de crear nuevo rol de usuario en cualquier categoría de rol. Sitúa el cursor sobre el {% icon info_circle %} para leer más sobre cada categoría de rol.

   - Categoría Otro: se crea un rol vacío sin permisos predefinidos.
   - {% link_new Categorías de roles predeterminadas | getting-started/default-user-roles.md %}: los permisos predeterminados para los componentes de injixo están preseleccionados. Los derechos de acceso a las funcionalides en WFM no están preseleccionados. 
  > Atención
  >
  > Cuando creas un nuevo rol de usuario, necesitas configurar manualmente los [derechos de acceso a las funciones en WFM](#establecer-permisos-para-wfm).

2. En la página **Crear rol de usuario**, configura el rol de usuario:

   - **Información básica**: introduce un **nombre**, una **abreviatura** y, opcionalmente, una **descripción**.
   - **Categoría de rol**: muestra la **categoría de rol** preseleccionada.

3. (Opcional) Modifica los permisos predeterminados. En la sección **Permisos**, una marca de verificación gris junto al nombre de un componente indica que todos los permisos para este componente se otorgan de forma predeterminada. Un símbolo de menos gris indica que algunos permisos para este componente no se conceden por defecto.  
   - Componente: para otorgar permisos para todas las funcionalidades de un componente, marca la casilla junto al nombre del componente.
   - Funcionalidad: para otorgar permisos para una funcionalidad concreta, haz clic en la flecha hacia abajo junto al nombre de un componente. Marca la casilla o casillas junto a la funcionalidad o funcionalidades para las que quieras otorgar permisos.
   - Para ver u ocultar todas las secciones, haz clic en **Expandir todo** o **Contraer todo**.
   - Para anular tu selección y restablecer los valores predeterminados para el rol de usuario predeterminado, haz clic en **Restablecer los permisos predeterminados**.
4. Para guardar el nuevo rol de usuario, haz clic en _Crear_{:.doc-button}. Para [otorgar permisos para WFM](#establecer-permisos-para-wfm) al nuevo rol de usuario, haz clic en _Crear e ir a Autorizaciones de los roles_{:.doc-button}.

   {{ 2 | image: "Página Crear rol de usuario", '80%' }}

### Asignar roles de usuario a los usuarios

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en un nombre.
3. En **Asignar rol(es) de usuario**, marca una o varias casillas. Para filtrar los roles de usuario mostrados, usa el campo **Buscar roles de usuario**.
4. Haz clic en _Guardar_{:.doc-button}.

   {{ 6 | image: 'Asignar roles de usuario', '80%'}}

## Establecer permisos para WFM

1. En _Account > Roles de usuario_{:.breadcrumbs}, selecciona un rol de usuario.
2. En la sección **Permisos**, haz clic en _Ir a Autorizaciones de los roles_{:.doc-button}.  
   injixo te redirige a _WFM > Gestión > Sistema > Autorizaciones de los roles_{:.breadcrumbs}.
3. En la sección **Panel de navegación** en la derecha, marca o desmarca las casillas para añadir o retirar permisos.

{{ 4 | image: "Sección Panel de navegación en la página Autorizaciones de los roles en WFM", '60%' }}

Recomendamos usar solo permisos basados en roles de usuario. Si es necesario, también puedes modificar los permisos para usuarios individuales. Para ello, ve a _WFM > Gestión > Sistema > Derechos de usuario_{:.breadcrumbs}.

## Gestionar el acceso a los equipos: restringir el acceso a los datos de configuración

Si tu organización incluye distintos equipos y quieres restringir el acceso a los datos de los equipos, puedes asignar varios roles a un mismo usuario. injixo combina los permisos de los distintos roles de usuario. Puedes restringir el acceso a elementos como unidades de planificación, modelos de horario, actividades o informes.

**Ejemplo**

Quieres que todos los planificadores tengan acceso a la planificación. Al mismo tiempo, quieres que cada planificador pueda editar solamente los datos de su propia unidad de planificación. En este caso, puedes asignar dos roles a cada planificador.

Puedes crear un rol sin acceso a unidades de planificación específicas o retirarle a un rol existente el acceso a todas las unidades de planificación. Para retirarle a un rol el acceso a todas las unidades de planificación, sigue estos pasos:

1. Ve a _Account > Roles de usuario_{:.breadcrumbs}.
2. Selecciona el rol de usuario.
3. Haz clic en _Ir a Autorizaciones de los roles_{:.breadcrumbs}.
4. Desplázate hasta la sección **Unidades de planificación** (o usa el enlace en la parte superior).
5. Haz clic en el {% icon item-delete %} junto a [Todas] para retirar el acceso a todas las unidades de planificación.
6. Haz clic en _Aceptar_{:.doc-button}.

Para otorgar a otros roles acceso a unidades de planificación específicas, sigue estos pasos:

1. Selecciona el segundo rol de usuario.
2. En la sección **Unidades de planificación**, haz clic en el {% icon item-add %}.
3. Selecciona la unidad o unidades de planificación en cuestión. Mantén pulsada la tecla **Ctrl** o **Mayús** mientras haces clic para seleccionar varias unidades de planificación.
4. En **Derechos de acceso**, marca las casillas para permitir **Leer**, **Editar** o **Eliminar**.
5. Haz clic en _Aceptar_{:.doc-button}.

Para completar tu configuración, ve a _Account > Usuarios_{:.breadcrumbs} y [asigna roles de usuario a tus usuarios](#asignar-roles-de-usuario-a-los-usuarios)


## Modificar roles de usuario predeterminados o personalizados

1. Ve a _Account > Roles de usuario_{:.breadcrumbs}.
2. Selecciona el rol de usuario que quieres modificar.
3. Lleva a cabo los cambios y haz clic en _Guardar cambios_{:.doc-button}.

## Eliminar roles de usuario personalizados

1. Ve a _Account > Roles de usuario_{:.breadcrumbs}.
2. Selecciona el rol de usuario.
3. Haz clic en _Eliminar rol de usuario_{:.doc-button} abajo a la derecha. No puedes eliminar roles de usuario predeterminados.
