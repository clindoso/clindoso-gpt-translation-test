---
title: El ciclo WFM en injixo
description: Aprende cómo injixo te apoya a lo largo del ciclo de WFM.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

El objetivo del workforce management (WFM) es optimizar la asignación de personal para cumplir con los objetivos comerciales y de nivel de servicio. injixo te ayuda a ser más eficiente en todas las etapa del ciclo de WFM.

  {{ 1 | image: "Ciclo de WFM: previsión, planificación, optimización de los turnos, gestión intradiaria, análisis", '60%' }}

- Previsión: predice tu carga de trabajo a corto, medio y largo plazo.
- Planificación: establece estrategias de reclutamiento, presupuesto y formación para el futuro.
- Optimización de turnos: crea los mejores turnos para tus empleados y las necesidades de tu negocio.
- Gestión intradiaria: adapta tu planificación a eventos imprevistos en tiempo real.
- Análisis: comprende, predice y mejora el rendimiento de tu negocio.

En este artículo encontrarás una descripción general de cómo injixo puede ayudarte en todas las etapas del ciclo de WFM.
El primer paso es proporcionar a injixo los datos necesarios para generar una previsión fiable. Para ello, necesitas configurar una integración con tus sistemas de distribución automática de llamadas (ACD, por sus siglas en inglés) o de gestión de relaciones con el cliente (CRM, por sus siglas en inglés).

¿Estás empezando en el workforce management? Aprende sobre los conceptos clave y definiciones en nuestro [glosario](https://help.injixo.com/glossary/overview).

## 1\. Previsión

### Configurar una integración

Para predecir la carga de trabajo a la que se enfrentará tu organización en cualquier momento futuro, injixo necesita acceso a tus datos de contacto y/o a los estados de los agentes de sistemas externos (como ACD o CRM). Para que injixo pueda importar y procesar estos datos, tienes que {% link_new integrar tus sistemas externos con injixo | features/acd-integration/cloud/how-integrations-work.md %}. injixo ofrece integraciones nativas específicas para distintos proveedores e integraciones universales. Según la integración, inijixo recibe los datos cada 15, 30 o 60 minutos (importe de datos históricos), o incluso en cuestión de segundos (importe de datos en tiempo real). 

Una vez añades una integración, esta envía datos a injixo automática y continuamente.
Los datos de contacto importados se almacenan en colas, que siempre están asociadas a un canal. Necesitas las colas para crear cargas de trabajo en las que basar tu previsión.

Puedes configurar tus integraciones en _Account > Integraciones_{:.breadcrumbs}.

### Crear una carga de trabajo  

Para utilizar injixo Forecast, primero tienes que {% link_new crear una carga de trabajo | features/forecast/injixo-forecast/manage-workloads.md | #crear-cargas-de-trabajo %} con las colas importadas por tu integración. Las cargas de trabajo contienen todos tus datos históricos y las previsiones relacionadas. Para crear una carga de trabajo, tu ACD debe estar conectado correctamente y las colas importadas deben estar disponibles.

Puedes crear cargas de trabajo en _Forecast > Workloads_{:.breadcrumbs}. 

### Generar una previsión

{% link_new injixo Forecast | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} combina tus datos históricos con los algoritmos más apropiados para generar previsiones de alta calidad.

Cada nueva importación de datos actualiza la previsión generada. También puedes {% link_new añadir eventos | features/forecast/injixo-forecast/events-and-holidays.md %} que influirán en tu previsión.

### Calcular requisitos de personal

Una vez hayas generado una previsión, puedes {% link_new calcular los requisitos de personal | features/forecast/injixo-forecast/staff-requirement.md %}, es decir, la cantidad de personas que deben ser planificadas para cubrir la carga de trabajo esperada. Puedes utilizar varios {% link_new métodos de cálculo | best-practices/requirement-scripts.md %} para determinar tus requisitos de personal. Los métodos de cálculo tienen en cuenta factores como la reducción de productividad (shrinkage), los objetivos de nivel de servicio o de tiempo de respuesta, etc. También puedes escribir requisitos de personal constantes sin una previsión, si fuera necesario.

Puedes utilizar tus requisitos de personal durante la planificación para crear horarios optimizados para unidades de planificación, actividades y periodos de tiempo específicos.

## 2\. Planificación

Usa los datos generados por injixo Forecast para comparar tus requisitos de personal con los recursos reales disponibles. La previsión a largo plazo te permite tomar mejores decisiones en el momento adecuado. Por ejemplo, a la hora de decidir si aprobar solicitudes de permiso, cuándo publicar ofertas de trabajo o qué programas de formación deben completar tus empleados para estar preparados para los próximos proyectos.

## 3\. Optimización de turnos

### Crear planificaciones

Una vez que hayas calculado tus requisitos de personal, injixo ofrece diferentes {% link_new métodos de planificación | features/scheduling/scheduling-methods.md %} que puedes elegir o combinar para crear la mejor planificación de tus empleados y satisfacer las necesidades de tu organización.

En _Plan > Planificar_{:.breadcrumbs}, puedes configurar reglas de planificación y limitaciones para cumplir con regulaciones laborales y acuerdos contractuales, a la vez que tomas en cuenta las preferencias de tus empleados.

injixo ofrece múltiples funcionalidades de planificación, como la {% link_new notificar cambios en el horario a los empleados | features/scheduling/schedules/schedules-optimized-schedules.md %}, {% link_new notificar cambios en el horario a los empleados | features/scheduling/schedules/schedules-notify-scheduling-changes.md %}, o {% link_new permitir que los empleados intercambien turnos | features/scheduling/planning-periods/enable-employees-to-swap-shifts.md %} con sus compañeros.

### Planificar permisos

{% link_new Vacaciones/Ausencias | features/scheduling/time-off/vacation-absences-management.md %} te permite gestionar los saldos y solicitudes de permisos de vacaciones, días de asuntos propios, bajas por enfermedad y otros tipos de ausencias. Los empleados pueden crear sus solicitudes de permiso en {% link_new injixo Me | features/injixo-me/use-injixo-me/explore-injixo-me.md %}. Puedes aprobar o rechazar las solicitudes de acuerdo con los requisitos de personal, la disponibilidad de los empleados, y reglas o restricciones predefinidas.

Configura los permisos en _Plan > Vacaciones/Ausencias_{:.breadcrumbs}.

## 4\. Gestión intradiaria

En {% link_new Gestión intradiaria | features/intraday/adherence-intraday.md %} puedes comparar las actividades planificadas con las actividades en las que tus empleados realmente trabajan, e identificar discrepancias. Muestra estadísticas detalladas y una puntuación de adherencia.

Puedes hacer lo mismo en tiempo real en {% link_new Adherencia en tiempo real | features/intraday/real-time-adherence.md %}, que ofrece una vista general completa, opciones de filtrado y una puntuación ajustable de objetivo de adherencia.

Con esa información, puedes hacer ajustes de última hora en la planificación para lidiar con eventos imprevistos y evitar tener exceso o falta de personal.

## 5\. Análisis
 
Con injixo puedes {% link_new crear paneles de control | features/monitoring/dashboards/dashboards-overview.md %} con gráficos para visualizar mejor diferentes métricas, p.&nbsp;ej., una comparación de los requisitos de personal y la cobertura real, o de las llamadas entrantes pronosticadas frente a las llamadas reales, para diferentes periodos de tiempo.

injixo también puede {% link_new generar múltiples tipos de informes | features/reporting/standard-reports/creating-reports.md %} que te ayudan a mantener una visión de conjunto de las métricas relevantes, como capacidad según el tipo de contrato, el tiempo trabajado por unidad de planificación o el resumen de vacaciones.
