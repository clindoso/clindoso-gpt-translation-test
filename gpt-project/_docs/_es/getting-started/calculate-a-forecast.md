---
title: Calcular una previsión
description: Sigue los pasos necesarios para crear una previsión.
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
redirect_from:
  - /es/quickstart-forecasting/
redirect_reason: Updated filename on 29 November 2023
---

Este artículo describe los pasos necesarios para crear tu primera {% link_new previsión | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}. La previsión se basa en datos históricos para calcular el número de empleados necesario para gestionar el volumen entrante para una actividad en una unidad de planificación.
Este artículo ofrece una visión general del proceso para crear una previsión. Para obtener más información sobre los detalles de cada paso, sigue los enlaces en este artículo.

Usa este artículo como una lista de tareas para ayudarte durante el onboarding. Contacta con tu consultor si tienes cualquier duda.

## Prerrequisito

Antes de crear una planificación, asegúrate de haber configurado correctamente tu {% link_new configuración de base | getting-started/set-up-base-configuration.md %}.

## 1. Configurar una integración

En _Account > Integraciones_{:.breadcrumbs}, configura una {% link_new integración | features/acd-integration/cloud/how-integrations-work.md %} con tu sistema externo para importar datos históricos. La integración importará los datos a injixo y creará colas de datos.

## 2. Configurar una carga de trabajo

En _Forecast_{:.breadcrumbs}, crea una {% link_new carga de trabajo | features/forecast/injixo-forecast/manage-workloads.md %} a partir de las colas de datos creadas por tu integración. La previsión se genera en cuestión de minutos.

Ten en cuenta que para {% link_new importar previsiones externas | features/forecast/injixo-forecast/import-forecast.md %} tienes que seleccionar al menos una cola de datos. Si no hay ninguna cola, tienes que subir al menos un punto de datos con una {% link_new integración de archivos CSV | features/acd-integration/cloud/add-csv-integration.md %}.

## 3. Crear y añadir eventos

Crea todos los {% link_new eventos | features/forecast/injixo-forecast/events-and-holidays.md %} que puedan influenciar el cálculo de tu previsión. Añade los eventos creados al historial y la previsión en tu carga o cargas de trabajo para mejorar el resultado del cálculo.

## 4. Guardar una versión de la previsión

Una {% link_new versión de la previsión | features/forecast/injixo-forecast/store-forecast-versions.md %} es una instantánea del resultado actual del cálculo. Guarda la versión de la previsión para revisarla más adelante o comparar tu previsión con el volumen efectivo del día en cuestión, p.&nbsp;ej., en {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %}.

## 5. Calcular requisitos de personal

Para crear planificaciones optimizadas o ejecutar la optimización de tareas, primero debes {% link_new calcular los requisitos de personal | features/forecast/injixo-forecast/calculate-staff-requirements.md %} para las actividades correspondientes en tus cargas de trabajo.

## ¿Y ahora?

¡Listo! Ya puedes {% link_new crear tu primera planificación | getting-started/create-a-schedule.md %} basada en tu previsión y tu necesidad de personal.
