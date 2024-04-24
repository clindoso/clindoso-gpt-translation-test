---
title: Backup and compare schedules
product_label:
  - advanced
  - enterprise
  - classic
description: Learn about the importance of schedule backups and how to do them.
redirect_from:
  - /best-practice-level-copy/
---

As a contact center planner, you need lots of options to modify shifts, both when building new shifts and when changing shifts in response to external factors such as spikes in requirement or employee sickness. _Shift Center_{:.menu-item} includes a one-step undo function and you can view the history for individual employees. _Shift Center_{:.menu-item} also includes the concept of multiple versions of schedules, called **Levels**.

The **Copy Level** function lets you keep safe copies of schedules for entire planning units, track the changes you made to schedules and experiment with corrective changes to schedules in a 'sandbox'-environment before settling upon the best solution.

> Note
>
> Please bear in mind that the destination level will be completely overwritten during copying. Filled days will be overwritten by empty days. Copying levels cannot be undone.

## What are the benefits of the Copy level content feature?

Nothing is more annoying than making a mistake during scheduling and having no way of restoring the previous state. Therefore, it makes sense that you save the schedules. This gives you the opportunity to restore the original state.

### Save pre-scheduled vacations and absences

If your schedules contain approved vacations and your employees are looking forward to taking time off - and you then overwrite or delete the schedules, the vacations will be lost and you will have a riot on your hands. Therefore, it makes sense to keep a backup copy from which you can restore the original state of your schedules. We recommend that you keep a copy of schedules containing approved vacations in _Version 1_ level.

### Compare different versions of the schedule

Deviation in call volume or AHT from the forecast is a fact of life in contact center planning. When this happens, you will naturally want to adjust your schedules to cope with the new requirement. So that you do not mess up your published schedules while experimenting with changes, we recommend making a copy of the published schedules on _Actual_ level. In this way you can see at a glance the advantages and disadvantages that arise from the changes you propose, e.g. the impact on coverage in the heat map.

### Separate scheduling and intraday management

A famous soldier once said “no plan survives contact with the enemy” and nowhere is that more true than in contact center planning. Deviations from plan and subsequent corrections are part of the day-to-day business of every planner.  
The most important thing is to learn from the changes that you need to make to schedules. In order to understand what adjustments are made on-the-day, e.g. by the real-time team or the supervisors, you should copy your schedules from the _Schedule_ level to the _Actual_ level and perform all other your intraday adjustments and re-optimizations in the _Actual_ level.

By comparing _Schedule_ and _Actual_ levels, you then can identify which factors had the biggest impact on your planning, so you can learn and be prepared in the future. For example, if you repeatedly find that you have to adjust schedules to cover for sickness, you might increase the shrinkage factor that you use in staffing calculations; or suggest action such as return-to-work interviews to reduce sickness levels.

## How do you copy levels?

The article about planning period functions explains {% link_new how to run a level copy | features/scheduling/planning-periods/copy-and-back-up-schedules.md | #copy-or-back-up-a-schedule %}. Selecting **Clear contents after copying** allows you to start scheduling from scratch after copying the schedules. If, on the other hand, you want to leave the source level intact, make sure that the option is not selected.
