---
title: Crear una planificación
description: Sigue los pasos necesarios para crear una planificación.
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/resolve-optimization-issues.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/why-level-copy.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/meetings-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-extra-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-replace-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-public-holidays.md
---

Crear planificaciones es una parte esencial del {% link_new ciclo de WFM | getting-started/the-wfm-cycle-in-injixo.md %}. Las planificaciones contienen los turnos y actividades planificadas para tus empleados.  

Usa este artículo como una lista de tareas para ayudarte durante el onboarding.

Atención: en injixo Essential WFM no puedes hacer una copia de seguridad de las solicitudes de permiso o la planificación definitiva.

## Prerrequisitos

Antes de crear una planificación, asegúrate de haber {% link_new configurado correctamente tu configuración de base | getting-started/set-up-base-configuration.md %} y {% link_new generado una previsión | getting-started/calculate-a-forecast.md %}. 

## Orden de la configuración

Recomendamos configurar los elementos en el orden presentado en la siguiente sección. No hay dos configuraciones iguales, por lo que el orden óptimo para tu organización puede ser diferente al presentado aquí. Contacta con tu consultor si tienes cualquier duda.

## Configurar los permisos

Los empleados pueden solicitar permisos en injixo Me. Para configurar los permisos, ve a _Plan > Vacaciones/Ausencias_{:.breadcrumbs}.

1. Introduce el {% link_new saldo de permisos | features/scheduling/time-off/vacation-entitlement.md %} de tus empleados para el año en curso.
2. Crea un {% link_new período de disfrute | features/scheduling/time-off/time-off-periods.md %} y publícalo. Un período de disfrute define el marco de tiempo en el que los empleados pueden solicitar permiso de vacaciones y otras ausencias. Tus empleados recibirán una notificación en injixo Me y podrán comenzar a crear solicitudes de permiso para ese período.

## Insertar actividades de tipo enfermedad o ausencia

En {% link_new Planificar | features/scheduling/schedules/schedules-overview.md %} y en el {% link_new Centro de planificación | features/scheduling/shiftcenter/shift-center-overview.md %} puedes gestionar la planificación de tu equipo. Inserta cualquier {% link_new actividad | features/administration/activity-types-and-properties.md | #tipos-de-actividades %} existente de tipo enfermedad o ausencia en la planificación.

## Gestionar solicitudes de permiso

En _Plan > Vacaciones/Ausencias_{:.breadcrumbs} puedes aprobar o rechazar las {% link_new solicitudes pendientes | features/scheduling/time-off/vacation-absences-management.md %}.

> Crea una copia de seguridad de la planificación actual en otro nivel.
>
> Usa {% link_new copiar contenido del nivel | features/scheduling/schedules/schedules-copy-level-content.md %} para guardar una copia de tu planificación. De este modo, si borras la planificación para volver a empezar, no perderás las solicitudes aprobadas y las ausencias introducidas.

## Crear la planificación

En {% link_new Planificar | features/scheduling/schedules/schedules-overview.md %}, el {% link_new Centro de planificación | features/scheduling/shiftcenter/shift-center-overview.md %} o {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %} puedes comprobar si los {% link_new requisitos de personal | features/forecast/injixo-forecast/staff-requirement.md %} para tus actividades están configurados correctamente.

1. Inserta {% link_new rotaciones de turnos | features/scheduling/schedules/schedules-insert-shift-sequences.md %} para tus empleados.
2. Configura y aplica {% link_new métodos de planificación | features/scheduling/scheduling-methods.md %} adicionales para completar la planificación.
3. Ejecuta la {% link_new optimización de tareas | features/scheduling/schedules/schedules-job-optimization.md %}. Puedes saltarte este paso si has {% link_new creado una planificación optimizada | features/scheduling/schedules/schedules-optimized-schedules.md %}.

Consejo: si estás creando una planificación de prueba, puedes usar {% link_new niveles vacíos | features/scheduling/schedules/schedules-empty-levels.md %}. Copia las ausencias y solicitudes de permiso guardadas de vuelta al nivel Plan antes de comenzar la fase de prueba.

## Guardar una copia de seguridad de tu planificación definitiva

Antes de realizar cualquier {% link_new cambio manual | features/scheduling/shiftcenter/modify-items.md %} a tu planificación original, {% link_new guarda una copia de seguridad | features/scheduling/schedules/schedules-copy-level-content.md %} en el nivel Estado actual. De este modo, podrás comparar la calidad de tu planificación original con otras versiones posteriores.

## Publicar la planificación y permitir el intercambio de turnos

1. Crea un período de planificación para que los empleados puedan {% link_new ver sus planificaciones | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} en injixo Me.
2. (Opcional) {% link_new Permitir que los empleados intercambien turnos | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.  
    Por defecto, tienes que {% link_new consultar y aprobar todas las solicitudes de intercambio | features/scheduling/view-approve-shift-swap-requests.md %}, pero también puedes permitir el intercambio automático con la configuración 48152.
3. Comparte el artículo {% link_new Explora injixo Me | features/injixo-me/use-injixo-me/explore-injixo-me.md %} con tus empleados.
