---
title: Valor de prioridad para las actividades
product_label:
  - advanced
  - enterprise
  - classic
description: Aprende cómo proteger las actividades para que no sean sobrescritas con otras actividades.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Valor de importancia para las actividades
    filepath: best-practices/importance-for-activities.md
---

Puedes definir un valor de prioridad para cada actividad en _Plan > Configuración > Actividades_{:.breadcrumbs}.
El valor de prioridad define qué actividades pueden ser sobrescritas por otras actividades durante actualizaciones manuales de la planificación o durante la optimización de tareas.

## ¿Para qué necesito el valor de prioridad para las actividades?

Por defecto, todas las actividades tienen la misma prioridad. En consecuencia, ciertas actividades pueden ser sustituidas por otras si tienen requisitos de personal distintos. Para asegurarte de que ciertas actividades nunca sean sobrescritas, usa el valor de prioridad (por defecto: 1).

Una actividad con un valor de prioridad alto (valor más alto: 1) no puede ser sustituida por actividades que tengan un valor de prioridad más bajo. Puedes usar esta funcionalidad si quieres asegurarte de que una actividad nunca sea sustituida.

## Prerrequisitos

Para priorizar actividades con el valor de prioridad, deben cumplirse las siguientes condiciones:

- Las actividades que deben ser priorizadas están configuradas como {% link_new Sustituibles | features/administration/activity-types-and-properties.md | #propiedades-de-las-actividades %}.
- Si son de tipo Presencia, las actividades deben tener requisitos de personal.
- La regla de planificación _2660_{:.id-label} está activada.

## Ejemplo 1: actividades de tipo Presencia

- Hay dos actividades: Línea directa B2B y Línea directa B2C.
- Ambas actividades son de tipo {% link_new Presencia | features/administration/activity-types-and-properties.md | #tipos-de-actividades %}.
- Línea directa B2B es una actividad crítica y nunca debe ser sustituida por Línea directa B2C.

Después de crear una planificación inicial, vuelves a calcular tus requisitos de personal para ambas actividades de acuerdo con los eventos actuales para verificar si tu personal todavía puede cubrir correctamente las actividades. Si los requisitos de personal para Línea directa B2C han aumentado, ejecutas la optimización de tareas para asegurarte de que las actividades estén correctamente equilibradas. Sin embargo, al hacer esto, la optimización de tareas podría reasignar empleados de Línea directa B2B a Línea directa B2C en esta planificación.

Para asegurarte de que Línea directa B2B nunca sea sustituida por Línea directa B2C, asígnale un valor de prioridad de 1 a Línea directa B2B y un valor de prioridad más bajo (un número mayor que 1) a Línea directa B2C.

Si no hay suficiente personal para trabajar en ambas actividades simultáneamente, injixo se asegurará de cubrir siempre Línea directa B2B antes que Línea directa B2C.

## Ejemplo 2: Enfermedad y Teletrabajo

- Hay dos actividades: Enfermedad y Teletrabajo.
- Ambas actividades son de tipo {% link_new Ausencia | features/administration/activity-types-and-properties.md | #tipos-de-actividades %}.

Dado que ambas actividades son de tipo Ausencia, no tienen requisitos de personal. Si insertas rotaciones de turnos que incluyen Teletrabajo sin definir una prioridad, injixo podría sustituir Enfermedad con Teletrabajo. Esto podría resultar en problemas para los empleados que estén enfermos ese día y que tuvieran planificado teletrabajar.

Para evitar que Enfermedad sea sustituida por Teletrabajo, asigna un valor de prioridad de 1 a Enfermedad y un valor de prioridad de 2 (o superior) a Teletrabajo. Esto garantizará que la actividad Enfermedad no pueda ser sustituida por la actividad Teletrabajo.
