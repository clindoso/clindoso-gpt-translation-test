---
title: Crear contratos
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Crea contratos para definir las horas laborables semanales y otras normas para tus empleados.
redirect_from:
  - /es/contract-creation/
redirect_reason: Updated filename on 08 December 2023
---

En _Plan > Configuración > Contratos_{:.breadcrumbs} puedes configurar los contratos de los empleados que quieras planificar. Puedes crear tantos contratos como quieras. Los contratos te permiten definir restricciones temporales para la planificación:

- el número mínimo y máximo de días laborables semanales;
- el número mínimo, efectivo y máximo de horas laborables diarias;
- el número mínimo, efectivo y máximo de horas laborables semanales;
- el número máximo de horas laborables mensuales.

Los contratos también reflejan información sobre las políticas de horario laboral de tu organización, como el número de días de descanso entre turnos. También puedes definir parámetros de planificación para la funcionalidad **Crear planificación optimizada**.

## Crear un contrato

Para crear un nuevo contrato, ve a _Plan > Configuración > Contratos_{:.breadcrumbs} y sigue los pasos a continuación:

1. Haz clic en el {% icon item-add %} arriba a la izquierda.
2. En la sección **General**, introduce la información básica del contrato:<br>
    - **Nombre**: introduce un nombre inequívoco (máx. 50 caracteres).
    - **Abreviatura**: introduce el nombre o una versión más corta del mismo (máx. 25 caracteres).
    - **Color**: el color puede ayudarte a identificar el contrato.
3. En el campo **Laborables / semana**, introduce el número de días laborables por semana.
4. En el campo **Calcular días laborables**, elige un método de cálculo: <br>
    - **Estándar** respeta el orden de los días en la semana de planificación.<br>
    - **Flexible** elige libremente los días laborales dentro del horario de apertura de la unidad de planificación.
5. Configura las secciones [**Horarios laborales de referencia**](#horarios-laborales-de-referencia) y [**Distribución horario laboral**](#distribución-horario-laboral).
6. (Opcional) Configura las secciones [**Parámetros de AutoScheduler**](#parámetros-de-autoscheduler) y [**Parámetros de planificación**](#reglas-de-planificación).
7. Haz clic en _Aceptar_{:.doc-button}.

## Horarios laborales de referencia

Los horarios laborales de referencia para las horas laborables mínimas, efectivas y máximas son esenciales para la planificación. Los horarios laborales de referencia funcionan en combinación con los parámetros de planificación y los parámetros de AutoScheduler.

### Día

- **Mínimo**: introduce un número mínimo de horas laborables diarias. Si dejas el campo vacío, el valor efectivo que configures se considerará como mínimo. Este parámetro se verifica mediante la regla de planificación _2615_{:.id-label}.
- **Efectivo**: introduce el número óptimo de horas laborables diarias. Recomendamos introducir un valor entre 0 y 24 horas, y tener en cuenta el horario laborable estándar.
- **Máximo**: introduce un número máximo de horas laborables diarias. Si dejas el campo vacío, el valor efectivo que configures se considerará como máximo. Este parámetro se verifica mediante la regla de planificación _2614_{:.id-label}.

### Semana

- **Mínimo**: introduce un número mínimo de horas laborables semanales. Puedes configurar el inicio de la semana de planificación con el parámetro de configuración _48420_{:.id-label}. Puedes configurar el número de días del fin de semana con el parámetro de configuración _48421_{:.id-label}.
- **Efectivo**: introduce el número óptimo de horas laborables semanales. Este valor es obligatorio si dejas en blanco la sección **Distribución horario laboral**. Puedes configurar el inicio de la semana de planificación con el parámetro de configuración _48420_{:.id-label}.
- **Máximo**: introduce un número mínimo de horas laborables semanales. Este parámetro se verifica mediante las reglas de planificación _2618_{:.id-label} y _2629_{:.id-label}. 

### Mes

- **Máximo**: introduce un número máximo de horas laborables mensuales. Este parámetro se verifica mediante la regla de planificación _2619_{:.id-label}.


## Distribución horario laboral

Puedes definir el número de horas laborables diarias para los empleados con este contrato. En la configuración de los **Horarios laborales de referencia**, esta sección es opcional. De todos modos, resulta útil a la hora de calcular ausencias pagadas, como vacaciones o bajas de enfermedad.

Ejemplo:<br>
Un empleado trabaja 40 horas a la semana y 8 horas al día, y libra los miércoles y domingos. Para asegurar que las horas de trabajo se distribuyan adecuadamente durante la semana, introduce 8:00 en los campos para lunes, martes, jueves, viernes y sábado, e introduce 0:00 en los campos para miércoles y domingo. Si el empleado está enfermo o está de vacaciones pagadas, sus horas laborables se siguen calculando en función de las horas que configuraste aquí.

Si dejas un campo en blanco, injixo recurrirá a la formula: [Horas efectivas semanales/número de días laborables]. Esto puede resultar en cálculos erróneos porque injixo asumirá una distribución uniforme de las horas de trabajo en todos los días laborables.

## Parámetros de AutoScheduler


- **N° máx. de días laborables consecutivos**: completa este campo si tu unidad de planificación abre todos los días de la semana. Introduce el número máximo de días laborables consecutivos que la funcionalidad **Crear planificación optimizada** debe tener en cuenta. Por ejemplo, si un empleado trabaja 5 días a la semana, usa este parámetro para evitar que trabajen 10 días consecutivos.
- **N° mín. de días libres a la semana**: completa este campo si tu unidad de planificación abre los fines de semana. Introduce el número máximo de días laborables consecutivos que la funcionalidad **Crear planificación optimizada** debe tener en cuenta.
- **N° mín. de días libres consecutivos a la semana**: completa este campo si quieres garantizar que tus empleados tengan un período mínimo de días libres consecutivos por semana. Introduce el mínimo de días libres consecutivos que la funcionalidad **Crear planificación optimizada** debe tener en cuenta para cada semana de planificación.
- **Número máximo de días libres consecutivos**: completa este campo si quieres limitar el número de días libres consecutivos de tus empleados para garantizar niveles de personal constantes y evitar ausencias largas. Introduce el número máximo de días libres consecutivos que la funcionalidad **Crear planificación optimizada** debe tener en cuenta. Este valor no se comprueba por semana, sino en términos absolutos.
- **Tiempo de descanso mín. (horas) entre dos turnos**: completa este campo si necesitas cumplir con legislación laboral que regule períodos de descanso entre turnos. Introduce el período de descanso mínimo que la funcionalidad **Crear planificación optimizada** debe tener en cuenta entre dos turnos consecutivos.	
- **Horario mínimo de trabajo semanal**: completa este campo para mantener un nivel mínimo de personal en tu unidad de planificación a lo largo de la semana. Así te aseguras de que siempre haya suficiente personal para manejar el volumen de trabajo esperado. Introduce el mínimo de días laborables que deben ser planificados cada semana de planificación.
- **Utilizar cuenta de horas previstas en lugar de horario efectivo semanal según contrato**: marca esta casilla si quieres usar los valores de las cuentas de horas previstas en la funcionalidad **Crear planificación optimizada**. Aprende más al respecto en {% link_new cuentas de horas previstas | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Máximo un sábado laborable cada n semanas**: completa este campo si quieres garantizar una distribución justa del trabajo de fin de semana entre tus empleados y evitar que las mismas personas trabajen constantemente los sábados. Introduce el máximo de semanas (1-5) en las que un empleado puede trabajar los sábados. Por ejemplo, un valor de 2 significa uno de cada dos sábados.
- **Planificar un día de trabajo después de un día entero de vacaciones**: completa este campo si quieres obligar a la funcionalidad **Crear horario optimizado** a planificar un día laborable después de un día completo de vacaciones. Si un empleado está varios días de vacaciones, el día laborable se planifica tras el último día libre.

## Reglas de planificación

Las reglas de planificación definen un conjunto de reglas generales y relacionadas con los contratos para tu proceso de planificación. En la configuración del contrato, las reglas de planificación se llaman parámetros de planificación.

Para ver una lista de todas las reglas de planificación disponibles, ve a _WFM > Gestión > Sistema > Reglas de planificación_{:.breadcrumbs}. Para ver la descripción de una regla, haz clic en la regla respectiva en la lista. Las reglas de planificación se configuran por regla general durante el onboarding con tu consultor de injixo.

Los usuarios con acceso de administrador pueden modificar todas las reglas, establecer excepciones, e incluso revertir los valores específicos de usuarios a la configuración predeterminada.

> Posible riesgo de errores de planificación
>
> Los cambios en las reglas de planificación son complejos y pueden resultar en errores de planificación si no se realizan correctamente. No los cambies tú mismo si no estás seguro de las consecuencias. Si necesitas cambiar una regla de planificación, contacta con tu consultor.

Las reglas de planificación específicas del contrato garantizan que las condiciones de cada contrato sean tenidas en cuenta durante la planificación. Por ejemplo, si un contrato especifica una cierta duración de período de descanso, o un número máximo de horas laborables diarias, las reglas de planificación aseguran que se cumplan estas condiciones. Incumplir estas reglas puede llevar a conflictos de planificación, insatisfacción de los empleados, y posibles incumplimientos de contrato.

### Indicador de estado

Puedes ver el estado de cada regla de planificación en la lista:

  - gris: la regla está desactivada y no se tendrá en cuenta durante la planificación.
  - amarillo: la regla está en modo suave. Incumplir esta regla generará una advertencia durante la planificación, pero la acción seguirá adelante.
  - rojo: la regla está completamente activada. Cualquier violación del contrato resultará en un mensaje de error que detalla específicamente el incumplimiento de la regla.