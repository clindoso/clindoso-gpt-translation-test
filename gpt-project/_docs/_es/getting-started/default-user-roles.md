---
title: Roles de usuario predeterminados
description: Aprende sobre los derechos de acceso de los roles de usuario predeterminados en injixo
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /es/user-roles-in-detail/
redirect_reason: Updated filename on 05 December 2022
---
## Roles de usuario predeterminados

En cada categoría de rol, injixo incluye un rol de usuario predeterminado con derechos de acceso predefinidos. En injixo Advanced y Enterprise WFM, puedes modificar los roles de usuario predeterminados o {% link_new crear nuevos roles de usuario | getting-started/configure-user-roles.md %}. Ten en cuenta que la categoría de rol Otro no incluye rol de usuario predeterminado.

| **Categoría de rol**                | **Derechos de acceso predeterminados**                                                                                                                                                                      |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Agente                 | Acceso a injixo Me: ver turnos, solicitar permisos, pujar por turnos, intercambiar turnos.                                                                           |
| Planificador               | Acceso completo a los datos de configuración y a todas las funcionalidades necesarias para la previsión, planificación y gestión intradiaria.                                                                    |
| Supervisor (básico)    | Acceso de solo lectura al nivel **Plan** en {% link_new Planificar                                                                                                               | features/scheduling/schedules/schedules-overview.md %} y el {% link_new Centro de planificación | features/scheduling/shiftcenter/shift-center-overview.md %}. Acceso a {% link_new Gestión de intercambios | features/scheduling/view-approve-shift-swap-requests.md %} y {% link_new Vacaciones/Ausencias | features/scheduling/time-off/vacation-absences-management.md %} para gestionar las solicitudes de permiso y los intercambios de turno. |
| Supervisor (avanzado) | Todas las funciones de Supervisor (básico), acceso completo al Centro de Planificación y a Planificar, permisos para modificar planificaciones en la gestión intradiaria y acceso de solo lectura a los datos de configuración. |
| Formador               | Acceso a Academy para facilitar la formación en injixo Me.                                                                                                                            |
| Finanzas               | Acceso a los datos de los usuarios y de facturación, además de a las facturas por los servicios injixo.                                                                                                  |


Para conceder acceso de administrador a un usuario, {% link_new edita el usuario | getting-started/manage-user-accounts.md %} y marca la casilla **Conceder acceso de administrador**. Esta acción sobrescribe todos los otros roles de usuario y concede acceso completo.

Ten en cuenta que las tablas en este artículo listan componentes y funcionalidades para los roles de usuario predeterminados relevantes. El icono verde de verificación <i class="fa fa-check" style="color:#1cb396"></i> indica acceso completo (de lectura y edición). Dado que tu plan WFM también determina tus derechos de acceso, puede que no tengas acceso a todas las funcionalidades de la lista.

## Acceso a componentes y funcionalidades

El acceso a los componentes en la navegación principal y a las funcionalidades relacionadas que se encuentran bajo cada elemento, ambas indicadas aquí en negrita.

Ten en cuenta que en injixo Classic todas las funcionalidades de planificación están en _Planificación > SchedulePro_{:.breadcrumbs}. Consulta la sección [Acceso a las funcionalidades en WFM](#acceso-a-las-funcionalidades-en-wfm) para leer más sobre las funcionalidades de injixo Classic.

<div class="table__wrapper table__with-subsections" markdown="1">

|                                         |          Administrador          |         Planificador         |  Supervisor (avanzado)  |   Supervisor (básico)    |
| --------------------------------------- | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Forecast**                            |                         |                         |                         |                         |
| **Forecast**                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |        Solo lectura        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Intraday**                            |                         |                         |                         |                         |
| **Adherencia en tiempo real**                 | <i class="fa fa-check"> |        Solo lectura        |        Solo lectura        |        Solo lectura        |
| **Adherencia intradiaria**                  | <i class="fa fa-check"> |        Solo lectura        |        Solo lectura        |        Solo lectura        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Plan**                                |                         |                         |                         |                         |
| **Planificar**                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |
| **Centro de planificación**                        | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |
| **Períodos de planificación**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |                         |
| Generar turnos                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Empezar sorteo de turnos                     | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Asignar turnos                           | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Ajustar la generación de turnos                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| **Acciones de planificación**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Insertar rotaciones de turnos                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Crear planificación optimizada               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Optimización de tareas                        | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Optimizar las pausas                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Planificar actividades extra               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Sustituir actividades                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Vaciar niveles                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Copiar contenido del nivel                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Aprobar intercambio de turnos                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |        Solo lectura        |
| **Reuniones**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Vacaciones/Ausencias**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |
| Periodos para permisos                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |                         |
| Editar derechos                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |                         |
| **Configuración**                       |                         |                         |                         |                         |
| Cualificaciones                                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |                         |
| --------------------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Analyze**                             |                         |                         |                         |                         |
| **Dashboards**                          | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

## Acceso a los datos de cuentas, usuarios e integraciones

Haz clic en _Account_{:.menu-item} en la navegación principal para acceder a las siguientes funcionalidades.

<div class="table__wrapper table__with-subsections" markdown="1">

|                    |          Administrador          |         Planificador         |         Finanzas         |
| ------------------ | :---------------------: | :---------------------: | :---------------------: |
| **Account**        |                         |                         |                         |
| **Usuarios**           | <i class="fa fa-check"> |                         |                         |
| **Roles de usuario**     | <i class="fa fa-check"> |                         |                         |
| **Facturación**        |                         |                         |                         |
| Suscripción       | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Facturas           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Contactos           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Detalles            | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| **Administración** |                         |                         |                         |
| Detalles de la compañía    | <i class="fa fa-check"> |                         |                         |
| **Integraciones**   | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Seguridad**       | <i class="fa fa-check"> |                         |                         |

</div>

## Acceso a las funcionalidades en WFM

Haz clic en _WFM_{:.menu-item} en la navegación principal para acceder a las siguientes funcionalidades.

Ten en cuenta que en injixo Advanced y Enterprise WFM solo **Supervisión** y **Gestión** están disponibles. El resto de las funcionalidades de planificación que estaban en _Planificación > SchedulePro_{:.breadcrumbs} han sido trasladadas a _Plan > Planificar_{:.breadcrumbs} y _Plan > Vacaciones/Ausencias_{:.breadcrumbs}. Puedes leer más en [Acceso a componentes y funcionalidades](#acceso-a-las-funcionalidades-en-wfm).

<div class="table__wrapper table__with-subsections" markdown="1">

|                                      |          Administrador          |         Planificador         |  Supervisor (avanzado)  |   Supervisor (básico)    |
| ------------------------------------ | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Planificación**                       |                         |                         |                         |                         |
| **SchedulePro**                        |                         |                         |                         |                         |
| Centro de planificación                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |
| Optimización                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Períodos de planificación                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |                         |
| Meeting Planner                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Insertar rotaciones de turnos               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Necesidad de turnos                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Gestión de intercambios                    | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |        Solo lectura        |
| **TimeManager**                        |                         |                         |                         |                         |
| Cuentas de horas previstas                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Derecho de vacaciones                 | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Supervisión**                       |                         |                         |                         |                         |
| Reports                              | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Gestión**                   |                         |                         |                         |                         |
| **Planificación**                         |                         |                         |                         |                         |
| Actividades                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Modelos de horario                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Modelos semanales                   | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |                         |
| Modelos de planificación             | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |                         |
| Rotaciones de turnos                      | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Tipos de día                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Unidades de planificación                       | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Calendarios de planificación                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Grupos                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Contratos                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |                         |
| Empleados                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lectura        |                         |
| **Previsión**                      |                         |                         |                         |                         |
| Tipos de evento                          | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Datos en cola                               | <i class="fa fa-check"> |        Solo lectura        |                         |                         |
| **Sistema**                           |                         |                         |                         |                         |
| Reglas de planificación                     | <i class="fa fa-check"> |        Solo lectura        |                         |                         |
| Configuraciones                             | <i class="fa fa-check"> |                         |                         |                         |
| Sistemas externos                     | <i class="fa fa-check"> |                         |                         |                         |
| Autorizaciones de los roles                   | <i class="fa fa-check"> |                         |                         |                         |
| Derechos de usuario                   | <i class="fa fa-check"> |                         |                         |                         |
| JobProcessor                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |

</div>

## Acceso a injixo Me

Los usuarios con el rol Agente pueden hacer clic en _Me_{:.menu-item} en la navegación principal para ver su calendario, solicitar permisos e intercambiar turnos. **Agenda personal** es la única funcionalidad disponible por defecto.


Los usuarios con acceso de administrador pueden hacer clic en _Me_{:.menu-item} y {% link_new configurar injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} para otorgar a los usuarios con el rol Agente acceso a funcionalidades adicionales.
