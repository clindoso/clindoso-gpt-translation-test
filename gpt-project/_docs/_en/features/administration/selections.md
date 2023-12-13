---
title: Create and manage selections
description: Create selections and assign people to them.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from: /selections-overview/
redirect_reason: renamed file in April 2022
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/filter-with-selections.md
---

Selections are grouping criteria that you can assign people to for filtering purposes. Selections work similarly to {% link_new employee filters | features/administration/employee-filter.md %}. The difference between them is:

- For selections, you can create your own grouping criteria.
- For employee filters, the grouping criteria are based on configuration elements, e.g. planning unit, skill, and contract.

Also, employee filters are available only in injixo Classic, Advanced, and Enterprise.

Selections are commonly used to group people who:

- Report to a certain supervisor.
- Work from home.
- Have been hired recently and might need extra support or monitoring.
- Can step in for other people on short notice.
- Have additional responsibilities that are not relevant for scheduling but may be important, e.g. people who have first aid training.

If you are using injixo Essential, you can use selections to group people according to configuration elements, e.g. planning unit, skill, and contract.

## Create selections

1. Go to _Plan > Configuration > Selections_{:.breadcrumbs}.
2. Click the {% icon item-add %} in the upper left.  
    A configuration panel opens on the right side.
3. Complete the following fields:
    - **Name**: Unique name for the selection (max. 50 characters).
    - **Abbreviation**: Abbreviation for the name (max. 25 characters).
    - **Description**: Optional description so that other users understand what the selection represents.
4. Click _OK_{:.doc-button}.

## Assign people to selections

To assign people to selections, you need to {% link_new create a selection | features/administration/selections.md | #create-selections %} first.

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. Click the person you want to assign to a selection.  
   A configuration panel opens on the right.
3. In the **Selections** section, click the {% icon item-add %}.
4. Complete the following fields:  
   - **Selection**: Click the selection you want to assign the person to.
   - (Optional) **Valid from/Valid to**: Date range to limit the selection's validity period. If you leave these fields blank, the selection is always valid. Learn more about {% link_new validity periods | features/administration/set-a-validity-period.md %}.
5. Click _OK_{:.doc-button}.

To edit a selection to which a person is assigned, click the {% icon item-edit %}. To remove the selection assignment, click the {% icon item-delete %}.

## Manage people in a selection

In _Plan > Configuration > Employees_{:.breadcrumbs}, you can have an overview of the people in a selection and access their settings.

You can filter the people in a selection with the following drop-down menus:

- **Planning unit**: Select all planning units.
- **Selection**: Select a selection.  
   If the **Selection** drop-down menu is not displayed, click the **Activate Standard Filter** icon {% icon selection | icon-only %} on the top.

injixo displays all the people in the selection. To access a person's settings, click their row on the list.

## Combine selections

injixo Classic, Advanced, and Enterprise customers can assign selections to an existing selection. The selection to which other selections are assigned becomes a parent selection. The assigned selections are child selections of the parent selection. This allows you to filter employees from all the child selections at once by using the parent selection.

To create a selection hierarchy between child selections and a parent selection, {% link_new create the parent and the child selections | features/administration/selections.md | #create-selections %} first.

To assign a selection to another selection, proceed as follows:

1. Go to _Plan > Configuration > Selections_{:.breadcrumbs}.
2. Click the selection you want to use as a parent selection in the selections list.  
   A configuration panel opens on the right side.
3. In the **Selections** section, click the {% icon item-add %}.
4. Complete the following fields:  
   - **Selections**: Click the selection you want to assign as a child selection.
   - (Optional) **Valid from/Valid to**: Date range to limit the period in which the child selections are assigned to the parent selection. If you leave the fields blank, the assignment is always valid.
5. Click _OK_{:.doc-button}.

To edit or remove a child selection, click the {% icon item-edit %} or the {% icon item-delete %}.

> Selection hierarchy
>
> The hierarchy between parent selections and child selections is not visible in _Plan > Configuration > Employees_{:.breadcrumbs}. To check if a selection is a parent selection, go to _Plan > Configuration > Selections_{:.breadcrumbs} and click a selection in the **Selections** section. Alternatively, give names to parent selections that make the selection hierarchy obvious.

## Delete a selection

1. Go to _Plan > Configuration > Selections_{:.breadcrumbs}.
2. In the list, click the selection you want to delete.
3. Click the {% icon item-delete %} in the upper left.
4. To confirm, click _Yes_{:.doc-button}.
