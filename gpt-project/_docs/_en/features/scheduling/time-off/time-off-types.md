---
title: Configure Time Off
description: Learn how to configure time-off types, time-off periods and edit your people's personal balances.
product_label:
  - essential
  - advanced
  - enterprise
beta-feature: true
beta-feature: true
---

Before your people can request time off in injixo Me, you need to create time-off types with an entitlement period, and at least one time-off period with the status Published.

## Time-off type

A time-off type is an absence category. Using time-off types, your organization can distinguish between different reasons for absences, such as sickness, vacation, or parental leave. For example, if your organization offers one day of leave per year for volunteering at an NGO, you can add the time-off type Volunteering leave.

When you create a time-off type in Time Off <span class="beta-icon">Beta</span>, an absence activity with the same name is automatically created in _Plan > Configuration > Activities_{:.breadcrumbs}. It is configured as a requestable full-day activity by default. If the time-off type is paid, the activity will also be configured as paid. This allows injixo to represent the time off in Schedules and Shift Center.

Time-off types include entitlement periods, e.g. the entitlement period for a time-off type Vacation is typically one year, and needs to be re-created every year. To allow people to request time off that was not taken in the previous year, define a longer time frame for the entitlement period, e.g. 18&nbsp;months. Vacation entitlement that has not been taken within the entitlement period will expire after the last day of the entitlement period and can no longer be requested.

> Entitlement periods cannot overlap
> 
> If you create an entitlement period that is longer than a year, you can only create the next entitlement period after the previous one has ended. For example, if your entitlement period spans from 1 January 2023 to 30 June 2024, the next entitlement period can only start on 1 July 2024. 


Time-off types can be paid or unpaid, depending on your organization's needs and national legislation. If you configure a time-off type as paid, injixo automatically creates a paid absence activity with the same name that is displayed in Schedules and Shift Center.

### Replace unpaid activities and fill up non-working hours

injixo allows you to block unscheduled times around a person's time off to avoid scheduling during those times.

> To use this option, create an unpaid time-off type first.

When a person requests time off and the time-off type is paid, the paid absence activity for the time-off type replaces any paid presence activities in the person's schedule. Any unpaid activities, e.g. breaks, remain as scheduled. The person's schedule is overwritten with the paid absence activity for the same time as the previously scheduled presence activities but it is open for the time before and after. As a consequence, the person may be automatically scheduled for the open times. 

To avoid people being scheduled for open times around their time off, create an unpaid time-off type and use it to replace unpaid activities. If you check the checkbox in the **Schedule setting** section in the time-off type configuration, injixo will convert the unpaid time-off type into an unpaid absence activity. Unpaid activities in the person's schedule will be replaced with this unpaid absence activity. Additionally, non-working hours will be filled up with this unpaid absence activity to block open times from scheduling.

### Create a time-off type

To create, edit and delete time-off types, go to _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span> and click _Time-off configuration_{:.doc-button}.

1. Click _New time-off type_{:.doc-button} on the right.
2. Enter the following information:
 - **Name**
 - **Paid**: Check this checkbox if people should get paid when they request time off of this type (e.g. Sickness).<br>Depending on national legislation, some time-off types must be paid. 
 - **Time unit**: Select whether you want to calculate the time off taken in hours or days.<br>Depending on national legislation, it may be mandatory to calculate time off in hours or days.<br>You cannot change the time unit after saving the new time-off type.
 3. (Optional) In the **Schedule setting** section, check the checkbox to activate the [fill-up functionality](#replace-unpaid-activities-and-fill-up-non-working-hours).
 4. Click **Add entitlement period**.
 5. Select a **Start date** and an **End date**.<br>You cannot change an entitlement period once a person has requested time off within that entitlement period.
 6. Click _Create time-off type_{:.doc-button}.


### Edit a time-off type

1. Click the time-off type that you want to edit.
2. Edit the information.
3. Click _Save changes_{:.doc-button}.
   
### Delete a time-off type

1. Click the time-off type that you want to delete.
2. Click _Delete time-off type_{:.doc-button}.<br>A confirmation window opens.
3. In the confirmation window, click _Delete time-off type_{:.doc-button}.

> Time-off type and absence activity
>
> When you delete a time-off type, the corresponding absence activity with the same name is deleted as well. This also applies vice versa: When you delete an absence activity that was automatically created while creating a time-off type, the corresponding time-off type is deleted. Deleted time-off types cannot be restored but you can still see them in injixo.

After deleting a time-off type or the corresponding absence activity, the following applies:
- You can still view, reject and cancel time-off requests created with that time-off type.
- You can no longer approve time-off requests created with that time-off type. If there is a pending time-off request with a deleted time-off type, you have the following options:  
   -  Reject the pending request
   - Ask the person to withdraw the request and to create a new time-off request, if necessary<br>
- You can still see the absence activity in the schedule if it has already been planned.
- You can no longer plan the absence activity in a new schedule.
- People can no longer submit new time-off requests with that time-off type.

## Time-off period

A time-off period is the period for which your people can request time off. Limiting the period for which people can request time off allows you to have better control of the schedule. For example, if you want to avoid people requesting time off for the Christmas holidays before October, create a time-off period from 1&nbsp;October until 31&nbsp;December. This way, your people cannot request time off for this time period at the beginning of the year. People who join the organization at a later time in the year will have the same chance to take time off during Christmas as everyone else.<br>Typically, a time-off period covers one business or calendar year. Depending on the time-off type and seasons with a high demand for time off, like Christmas or the summer break, you might want to set up additional time-off periods with a shorter time range. Note that time-off periods cannot overlap. You can create all required time-off periods at the beginning of the year and set their status to Unpublished until you want to publish them. {% link_new Learn more | features/scheduling/time-off/time-off-periods.md %} about time-off periods.

### Create a time-off period

To create, edit and delete time-off periods, go to _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span> and click _Time-off configuration_{:.doc-button}. 

> Time-off periods always require a time-off type. 

1. Click **Time-off periods** on the left.
2. Click _Create time-off period_{:.doc-button} on the right.
3. Configure the elements for the time-off period:
 - **Planning unit**: The planning unit cannot be edited later.
 - (Optional) **Selection**
 - **Activity**: Select the absence activity, i.e. the time-off type.
 - **Date range**
 - **Deadline**: Determine until when people need to submit their time-off requests.
 - **Status**: People can only request time off for time-off periods with the status Published.<br>The status is set to Published by default. If you want to create a time-off period for which people can only request time off later in the year, set the status to Unpublished.
4. Click _Save_{:.doc-button}.

### Edit a time-off period

1. Click **Time-off periods** on the left.
2. Hover over the time-off period you want to edit and click the {% icon pencil %} on the right.
3. Edit the information you want to change and click _Save_{:.doc-button}.

### Delete a time-off period

1. Click **Time-off periods** on the left.
2. Select the time-off period that you want to delete.
3. Click _Delete entries_{:.doc-button}.

> Note
>
> If you delete a time-off period for which time-off requests already exist, the existing requests will remain. 
>
>You can still approve or reject these requests.

## Personal balances

For each person, you can define a yearly entitlement for each time-off type you offer. To define personal balances for your people, you first need to configure at least one time-off type, and that time-off type must have at least one entitlement period. When a person requests time off, you will see the remaining entitlement in their personal balances based on the entitlement defined for the time-off type. If you do not define an entitlement for a time-off type for a person and that person requests time off of that type, their personal balance will be negative.
Editing a person's taken time off may be necessary for the following reasons, for example:
- You want to migrate from a previously used time-off solution to Time Off <span class="beta-icon">Beta</span> and need to synchronize the remaining personal balances of your people.
- You manually changed approved time off in Schedules. As this is not reflected in Time Off <span class="beta-icon">Beta</span>, you need to update the taken time off manually.

### Create and edit a person's entitlement

To create or edit an entitlement for a person, proceed as follows:

1. Go to _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span>.
2. Click _Personal balances_{:.doc-button} on the right.
3. Select or search for the person whose balance you want to create or edit.<br>Make sure you have selected the planning unit to which the person belongs.
4. Select a **Time-off type** and an **Entitlement period**.
5. In the **Remaining** panel on the right, click the {% icon pencil %} next to **Entitlement**.
6. Edit the entitlement:
- **New entitlement**: Enter a number or use the arrows to increase or reduce the entitlement.
- **Reason for the change**: Explain why you changed the entitlement. This field is mandatory.
7. Click _Save change_{:.doc-button}.<br>All changes and reasons will be recorded in the table overview.

### Bulk-edit entitlements

If you want to change the entitlement for several people at once, e.g. for everyone within a planning unit, proceed as follows:

1. In _Personal balances_{:.doc-button}, select the correct planning unit and click the tile showing several people.<br>A list displays everyone's entitlement in the planning unit.
2. In the **Entitlement** column, enter a number or use the arrows to increase or reduce the entitlement for each person individually.
3. At the bottom left, enter a **Reason for the change**. This field is mandatory.
4. Click _Save changes_{:.doc-button}.

