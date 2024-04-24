---
title: Spring cleaning guide
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Remove data and configurations that you aren't using from injixo.
promote-service: health-check
---

If you have been using injixo for a while now or have recently made various changes, it is time for spring cleaning!
This way you can ensure that your injixo stays clear and you keep track of everything. In order to avoid the deletion of required data, here is some advice on how to remove it correctly.

Three general remarks to keep your injixo clean:

- Always remember your organizations obligation to preserve records and the associated data retention periods. Don't delete data that could cause inconsistencies in schedule data. For example, if you delete a contract, this effects the work time calculation of your agents. This can invalidate schedules in the past. Check internally which corporate guidelines must be adhered to before deleting important information (e.g. for the payroll).
- As most configuration data is linked to other items, always start at the bottom of each configuration element. Remove existing assignments before deleting items. Otherwise, this could lead to scheduling issues or corrupt data.
  {{ 6 | image: 'Order for Deleting', '20%'}}
- If some configuration data is written in italics (e.g. activities in the _Shift Center_{:.menu-item}), this means that the associated configuration has already been deleted, but is still assigned.
  {{ 5 | image: 'Corrupt Data', '20%'}}

## Resigned employees

Employees quit their job, move to another department or retire. Fluctuation is one of the biggest reasons that your injixo contains obsolete information. Keep in mind that you have to store the data because of your organizations obligation to preserve records. If the data retention period is over, check in the fluctuation report whose staff membership ended in the past.

1. In _WFM > Administration > Scheduling > Employees_{:.breadcrumbs}, check for the agents with a past leave date and these employees.
2. Additionally, check for existing configuration items which have been created only for them, such as _Contracts_{:.menu-item} or _Day Models_{:.menu-item}.

For a better understanding, we show you the two steps in this gif:
{{ 1 | image: 'Steps to Delete Employee', '100%', 'gif' }}

## Changes to shift setup

If you have made any changes regarding the setup of your shifts, there may be outdated day models.
Be careful whenever you delete shifts: Make sure that they are not used for your current scheduling cycle. Especially when using shift bidding ensure that there are no open shift requests. Otherwise, they could become invalid.
To ensure that the deletions do not cause trouble with your next scheduling period, follow these steps in _WFM > Administration > Scheduling_{:.breadcrumbs}:

1. Check in _Employees_{:.menu-item} if the day models are directly assigned to any agents.
2. Check in _Planning Units_{:.menu-item} in the section **Day Models** if the option _[ALL]_ is used. If not, remove the relevant day models from this list.
3. Check in _Shift Sequences_{:.menu-item} if the day model is assigned to a shift sequence. Delete or replace it.
4. Check in _Week Time Patterns_{:.menu-item} if the day model is included in a week time pattern. This is especially relevant if it is the only day model associated with the week time pattern. In this case the Work Time Pattern Model becomes invalid.
5. Delete the day model in _Day Models_{:.menu-item}.

Have a look at this visualization to see the accomplishment:
{{ 3 | image: 'Steps to Delete Day Models', '100%', 'gif' }}

## Organizational restructuring

Have you had any organizational restructuring lately? For example, you have taken on additional responsibilities or you have delegated tasks to an external service provider. Accordingly, you have also adapted the structure in injixo. In this context, however, there are often also legacy issues, so you may not have cleaned up everything yet. This mainly affects selections and planning units. To clean them up properly, follow the steps below in _WFM > Administration > Scheduling_{:.breadcrumbs}:

1. Check in _Employees_{:.menu-item} if the selection or planning unit is still assigned to any agents. If so, you can simply delete the corresponding assignments using mass update.
2. Go to _Selections_{:.breadcrumbs} and check if the selection is subordinate to another selections. Once you have removed the link, delete the selection.
3. For the planning units clarify before deleting if the key figures (requirement, staffing, coverage) are still needed. If this is the case, you can copy them from _Dashboards_{:.menu-item}. Save them externally, e.g. in Excel. Afterwards go to _WFM > Administration > Scheduling > Planning Units_{:.breadcrumbs} and delete the planning unit.

We have visualized the instructions (without copying and saving data from _Dashboards_{:.menu-item}) in this short video:
{{ 4 | image: 'Steps to Delete Selection and Planning Unit', '100%', 'gif' }}
