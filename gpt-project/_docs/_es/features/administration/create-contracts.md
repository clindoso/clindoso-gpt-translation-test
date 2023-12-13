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

En _WFM > Gestión > Planificación > Contratos_{:.breadcrumbs}, puedes introducir los contratos para los empleados que quieres planificar. Puedes crear tantos contratos como quieras. Los contratos te permiten definir las siguientes restricciones temporales para la planificación:

- el número mínimo y máximo de días laborables semanales;
- el número mínimo, efectivo y máximo de horas laborables diarias;
- el número mínimo, efectivo y máximo de horas laborables semanales.

Los contratos también reflejan información sobre las políticas de horario laboral de tu organización, como el número de días de descanso entre turnos. También puedes definir parámetros de planificación para la funcionalidad Crear planificación optimizada.

## Crear un contrato

1. Haz clic en el icono Nuevo {% icon item-add | icon-only %}.
2. En la sección **General**, introduce la información básica del contrato:<br>
    - Introduce un **nombre** (máximo 50 caracteres).
    - Introduce una **abreviatura** (máximo 25 caracteres).
    - Selecciona un color.
3. En el campo **Laborables / semana**, introduce el número de días laborables por semana.
4. En el campo **Calcular días laborables**, elige un método de cálculo: <br>
    - **Estándar** respeta el orden de los días en la semana de planificación.<br>
    - **Flexible** elige libremente los días laborables dentro del horario de apertura de la unidad de planificación.
5. Configura las secciones [**Horarios laborales de referencia**](#horarios-laborales-de-referencia) y [**Distribución horario laboral**](#distribución-horario-laboral).
6. (Opcional) Configura las secciones [**Parámetros de AutoScheduler**](#parámetros-de-autoscheduler) y **Parámetros de planificación**.
7. Para guardar tu contrato, haz clic en _Aceptar_{:.doc-button}.

## Horarios laborales de referencia

Los horarios laborales de referencia para las horas laborables mínimas, efectivas y máximas son esenciales para la planificación. Los horarios laborales de referencia funcionan en combinación con las reglas y parámetros de planificación.

### Día

- **Mínimo**: introduce un número mínimo de horas laborables diarias. Si dejas el campo vacío, el valor efectivo que configures se considerará como mínimo. Este parámetro se verifica a través de la regla de planificación _2615_{:.id-label}.
- **Efectivo**: introduce el número óptimo de horas laborables diarias. Recomendamos introducir un valor entre 0 y 24 horas y tener en cuenta el horario laboral estándar.
- **Máximo**: introduce un número máximo de horas laborables diarias. Si dejas el campo vacío, el valor efectivo que configures se considerará como máximo. Este parámetro se verifica a través de la regla de planificación _2614_{:.id-label}.

### Semana

- **Mínimo**: introduce un número mínimo de horas laborables semanales. Puedes configurar el inicio de la semana de planificación con el parámetro de configuración _48420_{:.id-label}. Puedes configurar el número de días del fin de semana con el parámetro de configuración _48421_{:.id-label}.
- **Efectivo**: introduce el número óptimo de horas laborables semanales. Este valor es obligatorio si dejas en blanco la sección Distribución horario laboral. Puedes configurar el inicio de la semana de planificación con el parámetro de configuración _48420_{:.id-label}.
- **Máximo**: introduce un número máximo de horas laborables semanales. Este parámetro se verifica a través de las reglas de planificación _2618_{:.id-label} y _2629_{:.id-label}. 

### Mes

- **Máximo**: introduce un número máximo de horas laborables mensuales. Este parámetro se verifica a través de la regla de planificación _2619_{:.id-label}.


## Distribución horario laboral

Puedes definir el número de horas laborables diarias para los empleados con este contrato. Si has configurado la sección Horarios laborales de referencia, no es obligatorio que completes esta sección. De todos modos, resulta útil a la hora de calcular ausencias pagadas (p.&nbsp;ej., vacaciones o enfermedades).

Ejemplo:
Un empleado está de permiso el viernes y su contrato especifica 8 horas laborables para los viernes. Se calcularán 8 horas laborables para ese día.

Introduce un valor máximo de horas laborables para cada día de la semana. Introduce 0:00 horas para los días no laborables. Si dejas un campo en blanco, injixo recurrirá a la formula: [Horas efectivas semanales/número de días laborables]. Esta fórmula puede dar como resultado cálculos erróneos.

## Parámetros de AutoScheduler


- **N° máx. de días laborables consecutivos**: introduce el máximo de días laborables consecutivos que la funcionalidad Crear planificación optimizada debe tener en cuenta. Puede dejarse en blanco para unidades de planificación sin horarios de apertura los fines de semana. Por ejemplo, si un empleado trabaja 5 días a la semana, usa este parámetro para evitar que trabajen 10 días consecutivos.
- **N° mín. de días libres a la semana**: introduce el mínimo de días libres que la funcionalidad Crear planificación optimizada debe tener en cuenta para cada semana de planificación. Puede dejarse en blanco para unidades de planificación sin horarios de apertura los fines de semana.
- **N° mín. de días libres consecutivos a la semana**: introduce el mínimo de días libres consecutivos que la funcionalidad Crear planificación optimizada debe tener en cuenta para cada semana de planificación.
- **Número máximo de días libres consecutivos**: introduce el máximo de días libres consecutivos que la funcionalidad Crear planificación optimizada debe tener en cuenta. Este valor no se comprueba por semana sino en términos absolutos.
- **Tiempo de descanso mín. (horas) entre dos turnos**: introduce el período de descanso mínimo que la funcionalidad Crear planificación optimizada debe tener en cuenta entre dos turnos.	
- **Horario mínimo de trabajo semanal**: introduce el mínimo de días laborables que deben ser planificados cada semana de planificación.
- **Utilizar cuenta de horas previstas en lugar de horario efectivo semanal según contrato**: marca esta casilla si quieres usar los valores de las cuentas de horas previstas en Crear planificación optimizada. Aprende más al respecto en {% link_new cuentas de horas previstas | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Máximo un sábado laborable cada n semanas**: introduce el máximo de semanas (1-5) en las que un empleado puede trabajar los sábados. Por ejemplo, un valor de 2 significa uno de cada dos sábados.
- **Planificar un día de trabajo después de un día entero de vacaciones**: fuerza Crear planificación optimizada a planificar un día laborable siempre que el empleado tome un día entero de vacaciones. Si una persona está varios días de vacaciones, el día laborable se planifica tras el último día libre.