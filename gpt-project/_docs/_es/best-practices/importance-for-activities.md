---
title: Valor de importancia para las actividades
product_label:
  - advanced
  - enterprise
  - classic
description: Usa el valor de importancia para priorizar ciertas actividades durante la planificación optimizada.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
---

Puedes definir un valor de importancia para cada actividades en _Plan > Configuración > Actividades_{:.breadcrumbs}.

## ¿Para qué necesito el valor de importancia para las actividades?

Por defecto, la optimización de tareas planifica a los empleados primero para actividades con menores requisitos de personal. El exceso de personal en actividades con mayores requisitos de personal tiene un menor impacto negativo que la falta de personal en actividades con menores requisitos de personal.

En consecuencia, las actividades con mayores requisitos de personal podrían quedar faltas de personal si no hay suficientes empleados disponibles. Puedes omitir esta configuración y priorizar actividades con mayores requisitos de personal con el valor de importancia (predeterminado: 100&nbsp;%). Cuanto mayor sea el valor de importancia de una actividad, más intentará la optimización de tareas cumplir con los requisitos del personal con la mayor exactitud posible.
Puedes usar esta funcionalidad, p.&nbsp;ej. si necesitas priorizar una actividad sobre otra, como Línea directa B2B sobre Línea directa B2C.

Si una actividad requiere cinco empleados, planificar cinco empleados resultaría en una cobertura óptima. Para priorizar esta actividad, fija un valor de importancia alto (100&nbsp;%). La optimización de tareas intentará planificar a los empleados de manera que se cumplan los requisitos del personal de manera precisa. 

Las actividades que pueden tener exceso de personal en tu planificación deben tener un valor de importancia más bajo. Con un valor de importancia del 20&nbsp;%, la optimización de tareas planificaría el número exacto de empleados requeridos, o más, si hay suficientes empleados disponibles.

## Prerrequisitos

Para priorizar actividades con el valor de importancia, deben cumplirse las siguientes condiciones:
- Las actividades que deben ser priorizadas están configuradas como **Planificables** y **Sustituibles**.
- Los empleados que tienen que trabajar en las actividades prioritarias están planificados para trabajar en la actividad **Presente** (ID 1).

Si tus empleados tienen planificadas otras actividades no sustituibles, o si hay un bloque de actividades ya planificado en su modelo de horario, el valor de importancia no tiene efecto. La optimización de tareas no puede cambiar la actividad para ese día, o para ciertos intervalos del día.
Además, las cualificaciones de tus empleados o las propiedades de la actividad, como la opción **Planificable**, podríanimpedir que la optimización de tareas asigne más recursos a esta actividad.

## Ejemplo

- Tienes dos actividades, A y B.
- Hay 26 empleados disponibles y cualificados para trabajar en las actividades A y B.
- Los requisitos de personal para cada actividad son 10 empleados.
- La actividad A tiene un valor de importancia del 20&nbsp;% y la actividad B del 100&nbsp;%.

La optimización de tareas planifica 10 empleados para cada actividad, cumpliendo así exactamente con los requisitos de personal. Sin embargo, todavía hay seis empleados más que tienen que ser planificados.
Dado que el valor de importancia de la actividad A es cinco veces menor, la optimización de tareas puede asignar cinco empleados más a la actividad A antes de que esto tenga el mismo impacto negativo en la cobertura general que asignar un empleado más a la actividad B. Por lo tanto, injixo tiende a asignar empleados a la actividad A de manera desproporcionada.
