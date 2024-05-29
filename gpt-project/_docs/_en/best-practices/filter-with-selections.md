---
title: Filter with selections
description: Learn how to use selections as a filter.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
---

New to selections? Learn {% link_new the basics | features/administration/selections.md %} first.

When managing your team, you often need to group people with similar working conditions, e.g. people with daycare needs or people who report to a specific supervisor. Selections allow you to create your own grouping criteria. This is useful if you need grouping options beyond the scope of {% link_new planning units | features/administration/create-and-manage-planning-units.md %} and {% link_new employee filters | features/administration/employee-filter.md %}.

Planning units help you group people according to your organizational structure, e.g. by assigning people in different time zones to different planning units, and employee filters work based on injixo's configuration elements, such as contracts and activities. Selections help you group people to meet the specific needs of your organization.

You can create a selection to refine filters within a planning unit or to manage people across planning units. For example, you can create a selection to make sure that people with daycare needs have their schedules managed separately, or to filter schedules of people from different planning units for a marketing campaign in different time zones.

## Use selections to filter people within planning units

injixo provides planning unit and selection filters in **Plan** and **Intraday**. After selecting the planning unit, you can additionally filter people by selection.

For example, you have three planning units and one of the planning units includes people who are taking part in a training program. You can use selections to group them and manage their schedules separately, e.g. to plan specific meetings.

## Use selections to manage people across planning units

In injixo, there are three ways of filtering with selections across planning units. You can find respective examples of how to filter with selections below this section.

The following table presents an overview of the three different options to filter by selection across planning units. You can find these options in injixo components or functionalities.

| Component/functionality | Filtering option                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| Schedules               | All planning units and one selection.                                                       |
| Time Off                | All planning units and one selection.                                                       |
| Real-Time Adherence     | One selection and no planning unit.                                                         |
| Intraday Adherence      | One selection and no planning unit.                                                         |
| Shift Center            | One selection (no planning unit filter available).                                          |
| Notify people           | One planning unit and one selection. Repeat for all planning units that you want to filter. |
| Scheduling periods      | One planning unit and one selection. Repeat for all planning units that you want to filter. |
| Meetings                | One planning unit and one selection. Repeat for all planning units that you want to filter. |
| Time-off periods        | One planning unit and one selection. Repeat for all planning units that you want to filter. |
| Vacation entitlement    | One planning unit and one selection. Repeat for all planning units that you want to filter. |

For all functionalities in _Plan > Schedules > Scheduling actions_{:.breadcrumbs}, you need to select one planning unit and one selection, and apply the scheduling action to each planning unit that you want to filter.

The following examples provide more details about the three filtering options for selections as described in the table above.

## Examples

The examples below use a selection named Onboarding. The Onboarding selection is intended to group people who are in the onboarding phase in your organization independent of their planning unit. Using the Onboarding selection makes it easier to manage their schedules and track their needs.

With the following configuration, you can use the Onboarding selection as a filter across planning units:

1. {% link_new Create and configure a selection | features/administration/selections.md | #create-selections %} named Onboarding.
2. {% link_new Assign the people | features/administration/selections.md | #assign-people-to-selections %} who are in the onboarding phase to the Onboarding selection.

### Filtering option 1: All planning units and one selection

In _Plan > Schedules_{:.breadcrumbs}, you can filter the schedules of people in the Onboarding selection with the following drop-down menus:

- **Planning unit**: Select **All planning units**.
- **Choose selection**: Select **Onboarding**.  
   If the **Choose selection** drop-down menu is not displayed, click the {% icon selection-filter-u %} on the top left.

### Filtering option 2: One selection and no planning unit

In _Intraday > Real-Time Adherence_{:.breadcrumbs}, you can filter the scheduled activities of the people in the Onboarding selection and compare them with a person's actual status in real time. This is useful to check, for example, if a person is carrying out the activities scheduled for their onboarding phase.

To filter by selection, use the following drop-down menus:

- **Planning unit**: Make sure that no planning unit is selected.
- **Selection**: Select **Onboarding**.

### Filtering option 3: One selection and one planning unit

If you have specific time-off conditions for people in the onboarding phase, you can create specific time-off periods for the Onboarding selection. Consider that you have the following planning units for three different offices: Office 1, Office 2, and Office 3. These three offices have people in the onboarding phase who are assigned to the Onboarding selection.

To create specific time-off periods for the Onboarding selection:

1. In _Plan > Time Off_{:.breadcrumbs}, click _Time-off periods_{:.doc-button}.  
   You will be redirected to the **Time-off Periods** page.
2. Click _Create time-off period_{:.doc-button}.  
   A dialog window opens.
3. Filter by selection with the following drop-down menus:
   - **Planning unit**: Select **Office 1**.
   - **Selection**: Select **Onboarding**.
4. Complete the remaining fields.  
   Learn more about the configuration of {% link_new time-off periods | features/scheduling/time-off/time-off-periods.md %}.
5. Click _Save_{:.doc-button}.
6. Repeat the steps 1 to 5 for planning units Office 2 and Office 3.
